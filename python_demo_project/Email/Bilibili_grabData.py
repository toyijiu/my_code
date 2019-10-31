# -*- coding:utf-8 -*-

#grab bilibili's videos data
import time
import requests
import sys
from prettytable import PrettyTable
import importlib
import threading

#encoding
importlib.reload(sys)

#the logic code
def start_craw_cartoon(url,begin_num,numbers):
    times = 0
    headers = {}

    while(times < numbers):
        lock.acquire()
        myRequest = requests.get(url.format(begin_num),headers = {})
        if myRequest.status_code == 200:
            try:
                jsMap = myRequest.json()['data']
                favorite = str(jsMap['favorite'])
                danmaku = str(jsMap['danmaku']) + " "
                coin = str(jsMap['coin'])
                view = str(jsMap['view'])
                share = str(jsMap['share'])
                reply = str(jsMap['reply'])
                av_num = "av" + str(begin_num)
                print('begin to crew the cartoon,,beginNum = %d,number=%d,status=%d,times=%d' % (begin_num, numbers, myRequest.status_code,times))
                tableItem.add_row([av_num,view,danmaku,reply,favorite,coin,share])
                print(tableItem)
            except Exception as e:
                pass
            finally:
                lock.release()

        else:
            print('error:begin to crew the cartoon,,beginNum = %d,number=%d,status=%d' % (begin_num, numbers, myRequest.status_code))
            break

        begin_num += 1
        times += 1

    #print(tableItem)
    print('craw over~')

#some input parameters
threads = []

tableItem = PrettyTable(['cartton number', 'amount of play', 'bullet of screen', 'reply', 'collect', 'coin number', 'share number'])
url = 'https://api.bilibili.com/x/web-interface/archive/stat?aid={}'
counts = int(input('please enter the craw numbers per thread:'))
start_id = int(input('please input the start video id:'))
thread_num = int(input('please input the thread number you want:'))
lock = threading.Lock()

for num in range(thread_num):
    threads.append(threading.Thread(target=start_craw_cartoon,args=(url,start_id,counts,)))
    start_id += counts


if __name__ == '__main__':
    for thread in threads:
        thread.start()
        #thread.join()

    print(tableItem)

