#-*-coding:utf-8-*-

import requests
import json
import random
import pymysql
import sys
import datetime
import time
from imp import reload
from multiprocessing.dummy import Pool as ThreadPool

#set coding
reload(sys)

##global data_structure define
head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://space.bilibili.com/45388',
    'Origin': 'http://space.bilibili.com',
    'Host': 'space.bilibili.com',
    'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
}
proxies = { 'http': 'http://61.155.164.108:3128',
            'http': 'http://116.199.115.79:80',
            'http': 'http://42.245.252.35:80',
            'http': 'http://106.14.51.145:8118',
            'http': 'http://116.199.115.78:80',
            'http': 'http://123.147.165.143:8080',
            'http': 'http://58.62.86.216:9999',
            'http': 'http://202.201.3.121:3128',
            'http': 'http://119.29.201.134:808',
            'http': 'http://61.155.164.112:3128',
            'http': 'http://123.57.76.102:80',
            'http': 'http://116.199.115.78:80',
}
##function define
#datetime to ms
def datetimeToMs():
    return int(round(time.time()*1000))

#analysis uesr agent info in file
def handleUesrAgentInfo(filePath):
    HandleduserInfo = []
    with open(filePath,'rb') as userAgentFile:
        for singleUserAgent in userAgentFile:
            if singleUserAgent:
                HandleduserInfo.append(singleUserAgent.strip()[1:-1 - 1])

    random.shuffle(HandleduserInfo)
    return HandleduserInfo

##decode the jsFile of each user
def getUrlResource(urlInfo):
    print('url:%s pageId:%d' %(urlInfo[0],urlInfo[1]))
    payload = {
        '_': datetimeToMs(),
        'mid': urlInfo[0].replace('https://space.bilibili.com/','')
    }
    userInfo = random.choice(handledUserAgentInfo)
    userHead = {'User-Agent': userInfo,
                'Referer': 'https://space.bilibili.com/' + str(urlInfo[1]) + '?from=search&seid=' + str(random.randint(10000, 50000))
    }
    userJsContent = requests.session().post('http://space.bilibili.com/ajax/member/GetInfo',headers=userHead, data=payload, proxies=proxies).text

    #decode the js file
    try:
        print('before')
        print('jsContent:'+userJsContent)
        jsDict = json.loads(userJsContent)
        print('after')
        statusJs = jsDict['status'] if 'status' in jsDict.keys() else False
        print('url:%s pageId:%d statusJs=%d' % (urlInfo[0], urlInfo[1],statusJs))
        if statusJs == True:
            if 'data' in jsDict.keys():
                jsData = jsDict['data']
                mid = jsData['mid']
                name = jsData['name']
                sex = jsData['sex']
                face = jsData['face']
                coins = jsData['coins']
                spacesta = jsData['spacesta']
                birthday = jsData['birthday'] if 'birthday' in jsData.keys() else 'noBirthday'
                place = jsData['place'] if 'place' in jsData.keys() else 'noPlace'
                description = jsData['description']
                article = jsData['article']
                playNum = jsData['playNum']
                sign = jsData['sign']
                level = jsData['level_info']['current_level']
                exp = jsData['level_info']['current_exp']
                try:
                    fansContent = requests.get('https://api.bilibili.com/x/space/navnum?mid=' + str(mid) + '&jsonp=jsonp').text
                    fansDict = json.loads(fansContent)
                    following = fansDict['data']['following']
                    fans = fansDict['data']['follower']
                except:
                    following = 0
                    fans = 0
            else:
                print('Warning:'+urlInfo[0]+' has no data')

            # store this user's data to DB
            try:
                connection = pymysql.connectconnect(host='localhost', user='root', passwd='920919',
                                                    db='biliUserInfo', charset='utf8')
                cur = connection.cursor()
                cur.execute('INSERT INTO biliUserInfo(mid,name,sex,face,coins,spacesta,birthday,place,description,\
                                 article,following,fans,playNum,sign,level,exp) \
                                 VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' \
                            % (
                            mid, name, sex, face, coins, spacesta, birthday, place, description, article, following,
                            fans, playNum, sign, level, exp))
                connection.commit()
                print("craw Succeed: " + mid + "\t" + str(time.time() - startTime))
            except Exception as e:
                print('DB Error:' + e)

        else:
            print('Error:'+urlInfo[0])
    except Exception as e:
        pass


##logic code
handledUserAgentInfo = handleUesrAgentInfo('user_agents.txt')
startTime = time.time()
threadCount = 100
##multi thread
for threadId in range(99,101):
    urls = []
    for pageId in range(threadId*threadCount,(threadId + 1)*threadCount):
        urls.append(['https://space.bilibili.com/' + str(pageId),pageId])

    pool = ThreadPool(1)
    try:
        result = pool.map(getUrlResource,urls)
    except:
        print('Connection error')
        pool.close()
        pool.join()
        time.sleep(10)
        pool = ThreadPool(1)
        result = pool.map(getUrlResource, urls)
    time.sleep(10)

pool.close()
pool.join()
