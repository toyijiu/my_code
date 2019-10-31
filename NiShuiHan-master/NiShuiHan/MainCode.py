# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 19:35:51 2018

@author: Administrator
"""
import win32gui
import win32ui
import win32con
from ctypes import windll
from PIL import Image
import win32api,win32con
import time
import aircv as ac
import random
import win32clipboard as w
import math
from enum import Enum
from direct_keys import *
import random
#import itchat

shenhou_flag = -1
qingming_flag = -1
#鼠标定位
def mouse_move(hwd,x,y):  
    long_position = win32api.MAKELONG(x,y)
    win32api.SendMessage(hwd, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON, long_position)
    
#鼠标双击
def double_click(x=0,y=0):
    mouse_move(x,y)
    time.sleep(0.05)    #延迟时间，尤其是在电脑反映不是很快的时候，
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0) #点击鼠标
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0,0,0)  #抬起鼠标
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0,0,0)
def get_picture(hwnd):
    # 获取要截取窗口的句柄
    #hwnd = win32gui.FindWindow("xPeadK1RDTbDoA16dzTgXUFI4r", "逆水寒 Version:563196")
    
    # 获取句柄窗口的大小信息
    # 可以通过修改该位置实现自定义大小截图
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top
    
    # 返回句柄窗口的设备环境、覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    hwndDC = win32gui.GetWindowDC(hwnd)
    
    # 创建设备描述表
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    
    # 创建内存设备描述表
    saveDC = mfcDC.CreateCompatibleDC()
    
    # 创建位图对象
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    
    # 截图至内存设备描述表
    #img_dc = mfcDC
    #mem_dc = saveDC
    #mem_dc.BitBlt((0, 0), (w, h), img_dc, (100, 100), win32con.SRCCOPY)
    
    # 将截图保存到文件中
    #saveBitMap.SaveBitmapFile(mem_dc, 'screenshot.bmp')
    
    
    # 改变下行决定是否截图整个窗口，可以自己测试下
    # result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
    #print(result)
    
    # 获取位图信息
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    # 生成图像
    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)
    
    # 内存释放
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    
    # 存储截图
    if result == 1:
        #PrintWindow Succeeded
        im.save("test.png")
        #im.show()

def mouse_press_to(hwd, x_position, y_position, x2_position,y2_position,sleep):
    """
    鼠标左键按压移动到指定坐标
    :param hwd: 
    :param x_position: 
    :param y_position: 
    :param sleep: 
    :return: 
    """
    # 将两个16位的值连接成一个32位的地址坐标
    long_position = win32api.MAKELONG(x_position, y_position)
    long_position2 = win32api.MAKELONG(x2_position, y2_position)
    
    # 点击左键
    win32api.SendMessage(hwd, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON, long_position)
    time.sleep(2)
    win32api.SendMessage(hwd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    time.sleep(2)
    win32api.SendMessage(hwd, win32con.WM_MOUSEMOVE , win32con.MK_LBUTTON, long_position2)
    time.sleep(2)
    win32api.SendMessage(hwd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position2)
    time.sleep(int(sleep))
  
def key_event(hwd,input_key,sleep = 0.25,final_sleep=0.5):
    win32gui.SetForegroundWindow(hwd)
    #win32gui.SetWindowPos(hwd, win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_SHOWWINDOW)
    PressKey(DK_CODE[input_key])
    time.sleep(sleep)
    ReleaseKey(DK_CODE[input_key])  
    time.sleep(final_sleep)
    '''
    win32api.keybd_event(VK_CODE[input_key], 0, 0, 0)
    win32api.keybd_event(VK_CODE[input_key], 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(1)
    '''
def set_message(hwd,x,y,content,sleep=1,is_enter = False):
    click_position(hwd, x, y, 2)
    key_input(hwd,content)
    if is_enter:
        key_event(hwd,'enter')
        
    
def wheel_move(hwd,value,x,y):
    long_position = win32api.MAKELONG(x, y)
    long_position2 = win32api.MAKELONG(0, value)
    win32api.SendMessage(hwd, win32con.WM_MOUSEWHEEL, long_position2, long_position)
def right_click_position(hwd, x_position, y_position, sleep):
    """
    鼠标右键点击指定坐标
    :param hwd: 
    :param x_position: 
    :param y_position: 
    :param sleep: 
    :return: 
    """
    # 将两个16位的值连接成一个32位的地址坐标
    long_position = win32api.MAKELONG(x_position, y_position)
    # 点击左键
    win32api.SendMessage(hwd, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, long_position)
    time.sleep(random.uniform(0.1,0.2))
    win32api.SendMessage(hwd, win32con.WM_RBUTTONUP, win32con.MK_RBUTTON, long_position)
    time.sleep(int(sleep))
    
def click_position(hwd, x_position, y_position, sleep):
    """ 
    鼠标左键点击指定坐标
    :param hwd: 
    :param x_position: 
    :param y_position: 
    :param sleep: 
    :return: 
    """
    # 将两个16位的值连接成一个32位的地址坐标
    long_position = win32api.MAKELONG(x_position, y_position)
    # 点击左键
    win32api.SendMessage(hwd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    time.sleep(0.1)
    win32api.SendMessage(hwd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)
    time.sleep(int(sleep))
    
def click_keys(hwd, *args):
    """
    定义组合按键
    :param hwd: 
    :param args: 
    :return: 
    """
    for arg in args:
        win32api.SendMessage(hwd, win32con.WM_KEYDOWN, arg, 0)
    time.sleep(0.25)
    for arg in args:
        win32api.SendMessage(hwd, win32con.WM_KEYUP, arg, 0) 
def click_key(hwd, value,stop_time=0.25):
    """
    定义组合按键
    :param hwd: 
    :param args: 
    :return: 
    """
    #long_position = win32api.MAKELONG(0, value)
    #long_position2 = win32api.MAKELONG(740, 360)
    win32api.SendMessage(hwd, win32con.WM_KEYDOWN, value, 0)
    time.sleep(stop_time)
    win32api.SendMessage(hwd, win32con.WM_KEYUP, value, 0) 

def getText():
    # 读取剪切板
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d
def setText(aString):
    # 写入剪切板
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, aString)
    w.CloseClipboard()

def key_input(hwd,input_words=''):
    for word in input_words:
        print('word:',word)
        key_event(hwd,word)
        '''
        win32api.keybd_event(VK_CODE[word], 0, 0, 0)
        win32api.keybd_event(VK_CODE[word], 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.2)
        '''
def get_pic_location(imobj,imsrc):
    # find the match position
    pos = ac.find_template(imsrc, imobj)
    if pos is None:
        return None,None,None

    circle_center_pos = pos['result']
    circle_center_posX = int(circle_center_pos[0])
    circle_center_posY = int(circle_center_pos[1])

    return circle_center_posX,circle_center_posY,pos['confidence']
#图片路径，描述,匹配度要求，图片左上坐标，右下左边，图片当前状态值
class State(Enum):
    mainline_0_25 = 1
    mainline_30_39 = 2
    shenhou = 3
    qinming = 4
    yabiao = 5
    upgrade_42 = 6
    mainline_42 = 7
    upgrade_46 = 8
    
    idle = 9
    shenhou_remain = 10
    teaming = 11
    follow = 12
    shenhou_in_map = 13
    shenhou_over = 14
    
    qingming_remain = 15
    qingming_over = 16
    branch = 17
    common_operation = 18
    
    
fight_index = 12
mainline_index = 5
choice_index = 14
keyF_index = 3
equip_index = 9
choice2_index = 19
esc_index = 17
cloth_index = 32
continue_index = 61
wait_index = -10
change_player_index = -11
#图片地址，当前位置说明，匹配概率，是否需要限定匹配范围，当前位置index，当前状态index(None表示不关心)
common_map = [
            ['./pic/leave_map2.png','是否离开副本',0.9,None,None,210,State.common_operation],
           ['./pic/set.png','setting界面',0.9,None,None,0,State.common_operation],
           ['./pic/init.png','init界面',0.9,None,None,212,State.common_operation],
           ['./pic/new_role.png','选择职业界面',0.9,None,None,200,State.common_operation],
           ['./pic/new_role2.png','新建角色界面2',0.9,[88,41],[347,451],1,State.common_operation],
           ['./pic/shenxiang_logo.png','神像职业界面',0.9,None,None,205,State.common_operation],
           ['./pic/confirm5.png','确定按键界面5',0.9,None,None,choice_index,State.common_operation],
           ['./pic/create_role2.png','选择样貌界面',0.9,None,None,choice_index,State.common_operation],
           ['./pic/choice_name.png','填写名字界面',0.9,[402,51],[791,600],2,State.common_operation],
           ['./pic/run.png','自动寻路中',0.8,[568,534],[651,558],6,State.common_operation],
           ['./pic/npc_talk.png','NPC讲话中',0.8,[422,496],[638,537],7,State.common_operation],
           ['./pic/equip.png','装备道具',0.9,[989,636],[1092,683],equip_index,State.common_operation],
           ['./pic/use.png','使用道具',0.9,[989,636],[1092,683],equip_index,State.common_operation],
           ['./pic/branch4_11.png','买药忽视按钮界面',0.9,None,None,continue_index,State.common_operation],
           ['./pic/talk_choice.png','对话选择',0.9,None,None,choice_index,State.common_operation],
           ['./pic/shiming.png','实名制按钮',0.9,None,None,choice_index,State.common_operation],
           ['./pic/shiming2.png','实名制信息填写',0.9,None,None,206,State.common_operation],
           ['./pic/die2.png','人物死亡',0.9,None,None,18,State.common_operation],
           ['./pic/die.png','人物死亡',0.9,None,None,18,State.common_operation],
           ['./pic/confirm2.png','退出视频按钮界面',0.9,None,None,choice_index,State.common_operation],
           ['./pic/view_video.png','观看视频',0.9,None,None,30,State.common_operation],
           ['./pic/banghui1_2.png','帮会仗剑，守卫吃东西任务',0.9,None,None,continue_index,State.branch],
           ['./pic/submit_fail.png','没有东西提交',0.9,None,None,esc_index,State.branch],
           ['./pic/branch5_23.png', '客途问州-没有药', 0.9, None, None,182 , State.branch],
           ['./pic/branch4_13.png', '说书见闻-没有物品提交', 0.9, None, None, 182, State.branch],
           ['./pic/confirm.png','确定按键界面',0.9,None,None,choice_index,State.common_operation],
           ['./pic/choice2_3.png','提交界面',0.9,None,None,choice_index,State.common_operation],
           ['./pic/question.png','回答问题界面',0.9,None,None,33,State.common_operation],
           ['./pic/roll.png','roll点界面',0.9,None,None,choice_index,State.common_operation],
           ['./pic/choice_mode.png','模式选择-选自动寻路',0.9,[579,97],[938,647],13,State.common_operation],
           ['./pic/13_6.png', '第13回主线，藏书阁查线索6', 0.9, None, None, choice_index, State.mainline_42],
           ['./pic/29_2.png', '第29回主线，回答2', 0.9, None, None, choice_index, State.mainline_42],
           ['./pic/29_4.png', '第29回主线，回答4', 0.9, None, None, choice_index, State.mainline_42],
           ['./pic/talk.png','对话界面',0.9,None,None,keyF_index,State.common_operation],
           ['./pic/known.png','已知晓按钮',0.9,None,None,choice_index,State.common_operation],
           #['./pic/esc.png','ESC离开按钮',0.9,None,None,choice_index],
           #['./pic/package.png','背包界面',0.9,None,None,esc_index,None],
           ['./pic/team.png','队伍信息界面',0.9,None,None,esc_index,State.common_operation],
           ['./pic/money.png','首冲界面',0.9,None,None,esc_index,State.common_operation],
           ['./pic/esc_6.png','退出创建视频界面',0.9,None,None,esc_index,State.common_operation],
           ['./pic/recharge_button.png','充值界面',0.9,None,None,choice_index ,State.common_operation],
           ['./pic/recharge2.png','充值界面2',0.9,None,None,esc_index ,State.common_operation],
           ['./pic/known2.png','中部已知晓界面',0.9,None,None,choice_index,State.common_operation],
           ['./pic/upgrade.png','经验溢出界面',0.9,None,None,46,State.common_operation],
           ['./pic/upgrade_skill.png','技能修为不够界面',0.9,None,None,47,State.common_operation],
           ['./pic/upgrade_skill2.png','技能升级对话界面',0.9,None,None,choice_index,State.common_operation],
           ['./pic/upgrade_skill4.png','血河技能升级对话界面',0.9,None,None,choice_index,State.common_operation],
           ['./pic/upgrade_skill5.png','铁衣技能升级对话界面',0.9,None,None,choice_index,State.common_operation],
           ['./pic/upgrade_skill6.png','碎梦技能升级对话界面',0.9,None,None,choice_index,State.common_operation],
           ['./pic/shenxiang_button.png','神像技能升级对话界面',0.9,None,None,choice_index,State.common_operation],
           ['./pic/suwen_skill.png','素问技能升级对话界面',0.9,None,None,choice_index,State.common_operation],
           ['./pic/upgrade_skill3.png','技能升级按钮界面',0.9,None,None,62,State.common_operation],
           ['./pic/confirm4.png','确定按钮',0.9,None,None,choice_index,State.common_operation],
           ['./pic/confirm3.png','确定选择按钮',0.9,None,None,choice_index,State.common_operation],
           ['./pic/accept.png','接受任务按钮',0.9,None,None,choice_index,State.common_operation],
           ['./pic/begin_fight.png', '准备打架按钮', 0.9, None, None, choice_index, State.common_operation],
           ['./pic/branch14_1.png','怪盗疑踪-接任务',0.9,None,None,choice_index,State.branch],
           ['./pic/shenhou_talk.png', '深喉令对话界面', 0.9, None, None, esc_index, State.common_operation],
           ['./pic/esc_5.png','垂虹洞天任务-离开战场',0.9,None,None,176,State.branch],
           ['./pic/branch2_2.png', '读信关闭按钮', 0.9, None, None, choice_index, State.common_operation],
           ['./pic/esc_2.png', '组队关闭界面', 0.9, None, None, esc_index, State.common_operation],
           ['./pic/esc_3.png', '任务关闭界面', 0.9, None, None, esc_index, State.common_operation],
           ['./pic/detail.png', '任务详情界面', 0.9, None, None, esc_index, State.common_operation],
           ['./pic/esc_4.png', '关闭地图界面', 0.9, None, None, esc_index, State.common_operation],
           ['./pic/map10.png', '关闭孤山地图界面', 0.9, None, None, esc_index,State.common_operation],
           ['./pic/hangzhou.png', '杭州加载界面', 0.9, None, None, wait_index, State.common_operation],
           ['./pic/hangzhou2.png', '杭州加载界面2', 0.9, None, None, wait_index, State.common_operation],
           ['./pic/no_branch_9.png','关闭获得卡片界面',0.9,None,None,esc_index,State.common_operation],
           ['./pic/make_face.png','捏脸',0.9,None,None,201,State.common_operation],
           ['./pic/create_role.png','确定创建角色',0.9,None,None,202,State.common_operation],
           ['./pic/free_point.png','更给为固定视角',0.9,None,None,203,State.common_operation],
           ['./pic/1_4.png', '第一回-击败黑衣人', 0.8, None, None, fight_index, State.common_operation],
          # ['./pic/yaoqing.png', '邀请按钮', 0.9, None, None, choice_index, State.branch],
        ]
fight_map = [
    ['./pic/qingming_map.png', '清明上河', 0.9, None, None, 100, None],
    ['./pic/wanxianglou.png', '万象楼', 0.9, None, None, 100, None],
    ['./pic/shenhou_map_2.png', '神候令-冰火湖心', 0.9, None, None, 100, None],
    ['./pic/shenhou_map_1.png', '神候令-枫林追击', 0.9, None, None, 100, None],
    ['./pic/shenhou_map_3.png', '神候令-围棋', 0.9, None, None, 100, None],
    ['./pic/shenhou_map_4.png', '神候令-虎口夺食', 0.9, None, None, 100, None],
    ['./pic/heidian.png', '神候令-怒打黑店', 0.9, None, None, 100, None],
    ['./pic/luofengshanzhuang.png', '落枫山庄', 0.9, None, None, 100, None],
    ['./pic/yunqitai.png', '云起台', 0.9, None, None, 100, None],
    ['./pic/mishi.png', '密室', 0.9, None, None, 100, None],
    ['./pic/shenhouling.png', '深喉令任务', 0.9, None, None,mainline_index , None],
    # ['./pic/esc_button.png', 'esc按钮', 0.9, None, None,esc_index , None],
]
useless_index = 111
yaosheng39_index = 120
exit_team_index = 121
yaosheng46_index = 122
fight_index2 = 1000
#1-25级mainline
mainline_map1 = [
    ['./pic/newteach_1.png', '第一回-新手教学1', 0.8, [493, 174], [767, 216], 8, State.mainline_0_25],
    ['./pic/newteach_2.png', '第一回-新手教学2', 0.8, [493, 174], [767, 216], 31, State.mainline_0_25],
    ['./pic/newteach_3.png', '第一回-铁手新手教学2', 0.8, [493, 174], [767, 216], 8, State.mainline_0_25],
    ['./pic/newteach_4.png', '第一回-碎梦新手教学', 0.8, [493, 174], [767, 216], 8, State.mainline_0_25],
    ['./pic/newteach_6.png', '第一回-素问新手教学', 0.8, [493, 174], [767, 216], 8, State.mainline_0_25],
    ['./pic/newteach_7.png', '第一回-神像新手教学', 0.8, [493, 174], [767, 216], 8, State.mainline_0_25],
    ['./pic/1_1.png', '第一回-追命表明来意', 0.8, [690, 411], [794, 505], keyF_index, State.mainline_0_25],
    ['./pic/1_2.png', '第一回-击败黑衣人头目', 0.8, None, None, fight_index, State.mainline_0_25],
    ['./pic/1_3.png', '第一回-教训高大胜', 0.95, [1012, 378], [1280, 461], fight_index, State.mainline_0_25],
    ['./pic/1_5.png', '第一回-教训家丁', 0.9, None, None, fight_index, State.mainline_0_25],
    ['./pic/1_6.png', '第一回-询问菇凉', 0.9, None, None, 171, State.mainline_0_25],
    ['./pic/choice2_1.png', '第二回-选择1', 0.9, None, None, choice_index, State.mainline_0_25],
    ['./pic/choice2_2.png', '第二回-杂货铺打听消息', 0.9, [967, 591], [1269, 638], esc_index, State.mainline_0_25],
    ['./pic/choice2_4.png', '第二回-下河捕鱼', 0.9, [673, 423], [751, 497], keyF_index, State.mainline_0_25],
    ['./pic/2_1.png', '第二回-打水', 0.9, None, None, 15, State.mainline_0_25],
    ['./pic/2_2.png', '第二回-打架', 0.9, None, None, fight_index, State.mainline_0_25],
    ['./pic/2_3.png', '第二回-婆婆伤势', 0.9, None, None, 171, State.mainline_0_25],
    ['./pic/2_4.png', '第二回-江湖有缘', 0.9, None, None, esc_index, State.mainline_0_25],
    ['./pic/choice3_1.png', '第三回-进入卧房', 0.9, None, None, choice2_index, State.mainline_0_25],
    ['./pic/3_1.png', '第三回-破梦-击飞落叶', 0.9, [1015, 380], [1237, 689], 20, State.mainline_0_25],
    ['./pic/3_2.png', '第三回-换衣服', 0.9, [1015, 380], [1237, 689], cloth_index, State.mainline_0_25],
    ['./pic/3_3.png', '第三回-铁手-旋风腿', 0.9, [1015, 380], [1237, 689], 20, State.mainline_0_25],
    ['./pic/3_4.png', '第三回- 碎梦-击落飞叶', 0.9, None, None, 20, State.mainline_0_25],
    ['./pic/3_5.png', '第三回- 神像-击落飞叶', 0.9, None, None, 20, State.mainline_0_25],
    ['./pic/3_6.png', '第三回- 素问-击落飞叶', 0.9, None, None, 177, State.mainline_0_25],
    ['./pic/5_1.png', '第五回-恳求师兄', 0.9, [673, 423], [751, 497], keyF_index, State.mainline_0_25],
    ['./pic/5_2.png', '第五回-前往京城', 0.9, [969, 626], [1237, 689], choice2_index, State.mainline_0_25],
    ['./pic/6_1.png', '第六回-牵马', 0.9, [490, 500], [877, 631], 21, State.mainline_0_25],
    ['./pic/6_2.png', '第六回-骑马', 0.9, [1000, 380], [1280, 548], 22, State.mainline_0_25],
    ['./pic/6_3.png', '第六回-无情姓名', 0.85, None, None, choice_index, State.mainline_0_25],
    ['./pic/6_4.png', '第六回-无情生肖(蛇)', 0.85, None, None, choice_index, State.mainline_0_25],
    ['./pic/6_5.png', '第六回-无情进入时间', 0.85, None, None, choice_index, State.mainline_0_25],
    ['./pic/6_6.png', '第六回-神侯府选择', 0.9, None, None, choice_index, State.mainline_0_25],
    ['./pic/6_8.png', '第六回-回答问题1', 0.9, None, None,211, State.mainline_0_25],
    ['./pic/6_9.png', '第六回-回答问题2', 0.9, None, None, 211, State.mainline_0_25],
    ['./pic/6_10.png', '第六回-回答问题3', 0.9, None, None, 211, State.mainline_0_25],
    ['./pic/chuihong_1.png','垂虹洞天任务-回答',0.9,None,None,choice_index,State.branch],
    ['./pic/chuihong_2.png','垂虹洞天任务-进水',0.9,None,None,174,State.branch],
    ['./pic/chuihong_3.png','垂虹洞天任务-开箱子',0.9,None,None,175,State.branch],
    ['./pic/chuihong_4.png','垂虹洞天任务-离开水洞',0.9,None,None,choice_index,State.branch],
    ['./pic/no_branch_1.png','垂虹洞天任务',0.9,None,None,mainline_index,State.branch],
    ['./pic/no_branch_2.png','药王谷-九灵任务',0.9,None,None,useless_index,State.branch],
    ['./pic/no_branch_7.png','素问-帮派任务',0.9,None,None,useless_index,State.branch],
    ['./pic/no_branch_6.png','白帝城-神像任务',0.9,None,None,useless_index,State.branch],
    ['./pic/no_branch_8.png','缔仙岛-碎梦任务',0.9,None,None,useless_index,State.branch],
    ['./pic/no_branch_3.png','加入帮会皆兄弟任务',0.9,None,None,useless_index,State.branch],
    ['./pic/no_branch_4.png','装备拆分和合成任务',0.9,None,None,useless_index,State.branch],
    ['./pic/qiyu.png','奇遇线索任务',0.9,None,None,useless_index,State.branch],
    ['./pic/no_branch_5.png','庄园任务',0.9,None,None,useless_index,State.branch],
    ['./pic/mainline_1.png', '第1回主线', 0.85, None, None, mainline_index, State.mainline_0_25],
    ['./pic/mainline_2.png', '第2回主线', 0.85, None, None, mainline_index, State.mainline_0_25],
    ['./pic/mainline_3.png', '第3回主线', 0.8, None, None, mainline_index, State.mainline_0_25],
    ['./pic/mainline_4.png', '第4回主线', 0.85, None, None, mainline_index, State.mainline_0_25],
    ['./pic/mainline_5.png', '第5回主线', 0.85, None, None, mainline_index, State.mainline_0_25],
    ['./pic/mainline_6.png', '第6回主线', 0.85, None, None, mainline_index, State.mainline_0_25],
    ['./pic/qingyashu.png','青崖书界面',0.9,None,None,esc_index,State.branch],
    ['./pic/7_4.png','第七回-主线等待升到30级',0.95,[950,340],[1250,710],continue_index,State.mainline_30_39],
    #['./pic/huapi.png','画皮妖僧主线',0.85,None,None,mainline_index,State.mainline_30_39],
]
#30-39级mainline  yaosheng39_index
#change_player_index
mainline_map2 = [
    ['./pic/7_4.png','第七回-主线等待升到30级',0.95,[950,340],[1250,710],continue_index,State.mainline_30_39],
    ['./pic/7_1.png', '第七回-教训何绍金', 0.9, [950, 340], [1250, 710], fight_index, State.mainline_30_39],
    ['./pic/7_2.png', '第七回-交房租', 0.9, None, None, choice_index, State.mainline_30_39],
    ['./pic/7_3.png', '第七回-坐下', 0.9, None, None, 35, State.mainline_30_39],
    ['./pic/8_1.png', '第八回-表演', 0.9, [950, 340], [1250, 710], 40, State.mainline_30_39],
    ['./pic/8_2.png', '第八回-表演完了', 0.9, None, None,171, State.mainline_30_39],
    ['./pic/9_1.png', '第九回-摆平守卫', 0.9, [950, 340], [1250, 710], fight_index, State.mainline_30_39],
    ['./pic/9_2.png', '第九回-搜屋子', 0.9, None, None, 36, State.mainline_30_39],
    ['./pic/9_3.png', '第九回-按机关', 0.9, [950, 340], [1250, 710], 37, State.mainline_30_39],
    ['./pic/9_4.png', '第九回-不速之客', 0.9, [950, 340], [1250, 710], fight_index, State.mainline_30_39],
    ['./pic/10_1.png', '第10回-换衣服', 0.9, [950, 340], [1250, 710], 45, State.mainline_30_39],
    ['./pic/upgrade_39.png', '主线-主线等待升到39级', 0.95, [950, 340], [1250, 710], continue_index, State.mainline_30_39],
     ['./pic/esc_1.png', '画皮妖僧主线39，点到李阿婆了', 0.9, None, None, esc_index, State.mainline_30_39], 
    ['./pic/yaosheng39_1.png', '画皮妖僧主线39，怒战野利广缘', 0.95, None, None, fight_index2, State.mainline_30_39],
    ['./pic/yaosheng39.png', '画皮妖僧主线39，野利广缘第一次', 0.95, None, None, fight_index, State.mainline_30_39],
    ['./pic/yaosheng39_2.png', '画皮妖僧主线39，野利广缘第二次', 0.95, None, None, fight_index, State.mainline_30_39],
    ['./pic/yaosheng39_8.png', '画皮妖僧主线39，3战野利广缘', 0.95, None, None, yaosheng39_index, State.mainline_30_39],
   ['./pic/yaosheng39_5.png', '画皮妖僧主线39，野利广缘第3次', 0.95, None, None, fight_index2, State.mainline_30_39],
    ['./pic/yaosheng39_6.png', '画皮妖僧主线39，野利广缘打完了', 0.9, None, None, exit_team_index, State.mainline_30_39],
     ['./pic/yaosheng39_7.png', '画皮妖僧主线39，回复朱月明', 0.9, None, None, choice_index, State.mainline_30_39],
    ['./pic/yaosheng39_3.png', '画皮妖僧主线39，野利广缘任务', 0.9, None, None, choice_index, State.mainline_30_39],
    ['./pic/upgrade_42.png', '主线需要升级到42级', 0.9, None, None, continue_index, State.upgrade_42],
    ['./pic/mainline_7.png', '第7回主线', 0.9, None, None, mainline_index, State.mainline_30_39],
    ['./pic/mainline_8.png', '第8回主线', 0.9, None, None, mainline_index, State.mainline_30_39],
    ['./pic/mainline_9.png', '第9回主线', 0.9, None, None, mainline_index, State.mainline_30_39],
    ['./pic/mainline_10.png', '第10回主线', 0.9, None, None, mainline_index, State.mainline_30_39],
   # ['./pic/huapi.png','画皮妖僧主线',0.85,None,None,mainline_index,State.mainline_30_39],
]
#yaosheng39_index
#42-45级mainline
mainline_map3 = [
            ['./pic/11_1.png','第11回主线，拼接图画',0.9,None,None,48,State.mainline_42],
           ['./pic/11_2.png','第11回主线，拼接图画2',0.9,None,None,49,State.mainline_42],
           ['./pic/11_3.png','第11回主线，找到怜幽',0.9,None,None,choice_index,State.mainline_42],
           ['./pic/12_1.png','第12回主线，使用望气技能',0.9,None,None,50,State.mainline_42],
           ['./pic/12_2.png','第12回主线，击杀刺客按钮',0.9,None,None,choice_index,State.mainline_42],
           ['./pic/12_3.png','第12回主线，击杀刺客',0.95,None,None,fight_index,State.mainline_42],
           ['./pic/12_4.png','第12回主线，击杀刺客按钮2',0.9,None,None,choice_index,State.mainline_42],
           ['./pic/12_5.png','第12回主线，击杀刺客2',0.95,None,None,fight_index,State.mainline_42],
           ['./pic/12_6.png','第12回主线，击杀婉儿',0.9,None,None,fight_index,State.mainline_42],
           ['./pic/12_7.png','第12回主线，击杀高家丁',0.9,None,None,fight_index,State.mainline_42],
           ['./pic/12_8.png','第12回主线，击杀高家爪牙',0.9,None,None,fight_index,State.mainline_42],
           ['./pic/12_9.png','第12回主线，绑定令牌',0.9,None,None,keyF_index,State.mainline_42],
           ['./pic/12_10.png','第12回主线，查看伤势',0.9,None,None,171,State.mainline_42],
           ['./pic/13_1.png','第13回主线，藏书阁查线索',0.95,None,None,choice_index,State.mainline_42],
           ['./pic/13_2.png','第13回主线，藏书阁查线索2',0.95,None,None,choice_index,State.mainline_42],
           ['./pic/13_3.png','第13回主线，藏书阁查线索3',0.95,None,None,choice_index,State.mainline_42],
           ['./pic/13_4.png','第13回主线，藏书阁查线索4',0.95,None,None,choice_index,State.mainline_42],
            ['./pic/13_5.png', '第13回主线，藏书阁查线索5', 0.9, None, None, choice_index, State.mainline_42],
               ['./pic/yaosheng46_2.png', '画皮妖僧46-击败妖僧', 0.9, None, None, fight_index, State.mainline_42],
             ['./pic/yaosheng46.png', '画皮妖僧46', 0.95, None, None, yaosheng46_index, State.mainline_42],
            ['./pic/upgrade_46.png','主线需要升级到46级',0.9,None,None,continue_index,State.upgrade_46],
         ['./pic/mainline_11.png', '第11回主线', 0.85, None, None, mainline_index, State.mainline_42],
         ['./pic/mainline_12.png', '第12回主线', 0.85, None, None, mainline_index, State.mainline_42],
         ['./pic/mainline_13.png', '第13回主线', 0.85, None, None, mainline_index, State.mainline_42],
    #['./pic/huapi.png', '画皮妖僧主线', 0.85, None, None, mainline_index, State.mainline_30_39],
]
#47-49mainline
mainline_map4 = [
    ['./pic/14_1.png', '第14回主线，打辽军', 0.95, None, None, fight_index, State.mainline_42],
    ['./pic/14_2.png', '第14回主线，打辽军2', 0.95, None, None, fight_index, State.mainline_42],
    ['./pic/14_3.png', '第14回主线，搜尸体', 0.9, None, None, 161, State.mainline_42],
    ['./pic/14_6.png', '第14回主线，诊治', 0.95, None, None, keyF_index, State.mainline_42],
    ['./pic/14_7.png', '第14回主线，穿衣服', 0.95, None, None, 69, State.mainline_42],
    ['./pic/14_8.png', '第14回主线，上床', 0.95, None, None, 71, State.mainline_42],
    ['./pic/14_9.png', '第14回主线，离开藏书阁', 0.95, None, None, esc_index, State.mainline_42],
    ['./pic/14_10.png', '第14回主线，感谢恩人', 0.95, None, None, 171, State.mainline_42],
    ['./pic/15_1.png', '第15回主线，选择1', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/15_2.png', '第15回主线，选择2', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/16_1.png', '第16回主线，杀宋军', 0.95, None, None, 162, State.mainline_42],
    ['./pic/16_2.png', '第16回主线，杀辽国男子', 0.95, None, None, fight_index, State.mainline_42],
    ['./pic/16_3.png', '第16回主线，坐下', 0.95, None, None, 72, State.mainline_42],
    ['./pic/16_6.png', '第16回主线，解开绳索', 0.95, None, None, 85, State.mainline_42],
    ['./pic/16_7.png', '第16回主线，进营房', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/16_8.png', '第16回主线，查看辽国女子', 0.95, None, None, 171, State.mainline_42],
    ['./pic/17_12.png', '第17回主线，深入追击辽军', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/16_5.png', '第17回主线，追击辽兵', 0.95, None, None, 83, State.mainline_42],
    ['./pic/17_1.png', '第17回主线，回答1', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/17_2.png', '第17回主线，打架', 0.95, None, None, 73, State.mainline_42],
    ['./pic/17_3.png', '第17回主线，上床', 0.95, None, None, 71, State.mainline_42],
    ['./pic/17_4.png', '第17回主线，敬酒', 0.95, None, None, keyF_index, State.mainline_42],
    ['./pic/17_5.png', '第17回主线，回答', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/17_6.png', '第17回主线，引狼', 0.95, None, None, 74, State.mainline_42],
    ['./pic/17_7.png', '第17回主线，回答2', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/17_8.png', '第17回主线，回答3', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/17_9.png', '第17回主线，回答4', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/17_10.png', '第17回主线，打铁疙瘩', 0.95, None, None, fight_index, State.mainline_42],
    ['./pic/17_11.png', '第17回主线，打宋军', 0.95, None, None, fight_index, State.mainline_42],
    ['./pic/17_14.png', '第17回主线，贴金疮药', 0.95, None, None, 86, State.mainline_42],
    ['./pic/17_15.png', '第17回主线，深入追击辽军2', 0.95, None, None, fight_index, State.mainline_42],
    ['./pic/17_16.png', '第17回主线，鲁熊疗伤', 0.95, None, None, keyF_index, State.mainline_42],
     ['./pic/yaosheng50_1.png', '画皮妖僧50', 0.95, None, None, 178, State.mainline_42],
    ['./pic/up_50.png','主线需要升级到50级',0.95,None,None,continue_index,State.upgrade_46],
    ['./pic/up_51.png','主线需要升级到51级',0.95,None,None,continue_index,State.upgrade_46],
    ['./pic/mainline_14.png', '第14回主线', 0.85, None, None, mainline_index, State.mainline_42],
    ['./pic/mainline_15.png', '第15回主线', 0.85, None, None, mainline_index, State.mainline_42],
    ['./pic/mainline_16.png', '第16回主线', 0.85, None, None, mainline_index, State.mainline_42],
    ['./pic/mainline_17.png', '第17回主线', 0.85, None, None, mainline_index, State.mainline_42],
   #['./pic/yaosheng50.png', '画皮妖僧50主线', 0.85, None, None, mainline_index, State.mainline_30_39],
]
#51-54mainline
mainline_map5 = [
    ['./pic/18_1.png', '第18回主线，回答', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/18_2.png', '第18回主线，回答2', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/18_3.png', '第18回主线，回答3', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/18_4.png', '第18回主线，打沈云山', 0.95, None, None, fight_index, State.mainline_42],
    ['./pic/18_5.png', '第18回主线，穿衣服', 0.95, None, None, 70, State.mainline_42],
    ['./pic/18_7.png', '第18回主线，易容', 0.95, None, None, keyF_index, State.mainline_42],
    ['./pic/18_8.png', '第18回主线，回答问题', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/18_9.png', '第18回主线，回答问题2', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/18_10.png', '第18回主线，回答问题3', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/18_12.png', '第18回主线，解密码锁', 0.9, None, None, 75, State.mainline_42],
    ['./pic/18_11.png', '第18回主线，回答问题4', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/18_13.png', '第18回主线，应对柳雁平', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/18_14.png', '第18回主线，回答5', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/18_15.png', '第18回主线，回答6', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/18_16.png', '第18回主线，回答7', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/18_18.png', '第18回主线，开钥匙', 0.95, None, None, keyF_index, State.mainline_42],
    ['./pic/18_19.png', '第18回主线，击杀狱卒', 0.95, None, None, fight_index, State.mainline_42],
    ['./pic/18_20.png', '第18回主线，生态开关', 0.95, None, None, 76, State.mainline_42],
    ['./pic/18_21.png', '第18回主线，听楚相玉讲话', 0.95, None, None, choice_index, State.mainline_42],
    ['./pic/18_22.png', '第18回主线，挡箭', 0.9, None, None, 77, State.mainline_42],
    ['./pic/18_23.png', '第18回主线，2层狱卒', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/18_24.png', '第18回主线，给乌云止血', 0.9, None, None, 78, State.mainline_42],
    ['./pic/18_25.png', '第18回主线，大牢找钥匙', 0.9, None, None, 88, State.mainline_42],
    ['./pic/18_27.png', '第18回主线，打田大错', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/18_28.png', '第18回主线，打四大天王', 0.9, None, None, 179, State.mainline_42],
    ['./pic/18_29.png', '第18回主线，深入大牢', 0.9, None, None, 185, State.mainline_42],
    # ['./pic/18_26.png','第18回主线，大牢找钥匙2',0.9,None,None,87,State.mainline_42],
    ['./pic/19_1.png', '第19回主线，教训秦时月', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/19_2.png', '第19回主线，击退辽军', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/19_3.png', '第19回主线，点火', 0.9, None, None, 79, State.mainline_42],
    ['./pic/19_4.png', '第19回主线，反弹', 0.9, None, None, 80, State.mainline_42],
    ['./pic/19_5.png', '第19回主线，击退辽军', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/19_6.png', '第19回主线，战胜中军护卫', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/19_7.png', '第19回主线，战胜辽军', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/19_8.png', '第19回主线，围堵聂其', 0.9, None, None,163 , State.mainline_42],
    ['./pic/19_9.png', '第19回主线，战胜辽军2', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/19_10.png', '第19回主线，战胜辽军3', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/19_11.png', '第19回主线，查看乌云伤势', 0.9, None, None, 171, State.mainline_42],
    ['./pic/20_1.png', '第20回主线，提交四逆汤', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/20_2.png', '第20回主线，摸白雪', 0.9, None, None, 164, State.mainline_42],
    ['./pic/20_3.png', '第20回主线，打神秘男子', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/21_1.png', '第21回主线，打咸鱼丑', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/21_2.png', '第21回主线，阻止官兵', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/21_3.png', '第21回主线，释放冷忽而', 0.9, None, None, keyF_index, State.mainline_42],
    ['./pic/21_4.png', '第21回主线，回答铁手', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/21_5.png', '第21回主线，回答2', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/21_6.png', '第21回主线，绑架冷忽而', 0.9, None, None, 90, State.mainline_42],
    ['./pic/yaosheng53.png', '画皮妖僧53', 0.95, None, None, 181, State.mainline_42],
    ['./pic/yaosheng53_2.png', '画皮妖僧53-打架', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/19_0.png','主线需要升级到54级',0.9,None,None,continue_index,State.upgrade_46],
    ['./pic/mainline_18.png', '第18回主线', 0.85, None, None, mainline_index, State.mainline_42],
    ['./pic/mainline_19.png', '第19回主线', 0.85, None, None, mainline_index, State.mainline_42],
    ['./pic/mainline_20.png', '第20回主线', 0.85, None, None, mainline_index, State.mainline_42],
    ['./pic/mainline_21.png', '第21回主线', 0.85, None, None, mainline_index, State.mainline_42],
    #['./pic/huapi.png', '画皮妖僧主线', 0.85, None, None, mainline_index, State.mainline_30_39],
]
#54之后的mainline
mainline_map6 = [
    ['./pic/22_1.png', '第22回主线，落座', 0.95, None, None, 81, State.mainline_42],
    ['./pic/22_2.png', '第22回主线，穿衣', 0.9, None, None, 82, State.mainline_42],
    ['./pic/22_4.png', '第22回主线，回答5', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/22_5.png', '第22回主线，回答6', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/22_7.png', '第22回主线，摸白雪', 0.9, None, None, keyF_index, State.mainline_42],
    ['./pic/22_8.png', '第22回主线，打架', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/22_9.png', '第25回主线，关门', 0.9, None, None, 186, State.mainline_42],
    ['./pic/22_10.png', '第25回主线，关闭裁缝', 0.9, None, None, 204, State.mainline_42],
    #['./pic/22_6.png', '第22回主线，打架', 0.98, None, None, fight_index, State.mainline_42],
    # ['./pic/22_3.png','第22回主线，穿衣2',0.9,None,None,choice_index,State.mainline_42],
    ['./pic/23_1.png', '第23回主线，打架', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/23_2.png', '第23回主线，回答问题', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/23_3.png', '第23回主线，回答问题2', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/23_4.png', '第23回主线，da护卫', 0.95, None, None, fight_index, State.mainline_42],
    ['./pic/23_5.png', '第23回主线，换衣服', 0.95, None, None, 170, State.mainline_42],
    ['./pic/23_8.png', '第23回主线，写之字1', 0.95, None, None, 184, State.mainline_42],
    ['./pic/23_10.png', '第23回主线，写之字2', 0.95, None, None, 197, State.mainline_42],
    ['./pic/23_9.png', '第23回主线，写之字3', 0.95, None, None, 195, State.mainline_42],
    ['./pic/23_11.png', '第23回主线，写之字4', 0.95, None, None, 198, State.mainline_42],
    ['./pic/24_1.png', '第24回主线，打架', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/24_2.png', '第24回主线，打架2', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/24_3.png', '第24回主线，打架3', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/24_4.png', '第24回主线，anzhang', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/24_5.png', '第24回主线，追出去', 0.9, None, None, 171, State.mainline_42],
    ['./pic/25_1.png', '第25回主线，推门', 0.9, None, None, 180, State.mainline_42],
    ['./pic/25_2.png', '第25回主线，回答', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/25_3.png', '第25回主线，打架', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/25_4.png', '第25回主线，关闭房门2', 0.9, None, None, 187, State.mainline_42],
    ['./pic/25_5.png', '第25回主线，拼图', 0.9, None, None, 188, State.mainline_42],
    ['./pic/25_6.png', '第25回主线，离开房间', 0.9, None, None, 189, State.mainline_42],
    ['./pic/25_7.png', '第25回主线，打家丁', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/25_8.png', '第25回主线，打谢主管', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/26_1.png', '第26回主线，棋阵', 0.9, None, None, 190, State.mainline_42],
    ['./pic/26_2.png', '第26回主线，准备打罐子', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/26_3.png', '第26回主线，打罐子', 0.9, None, None, 191, State.mainline_42],
    ['./pic/27_1.png', '第27回主线，回答问题', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/27_2.png', '第27回主线，回答问题2', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/27_3.png', '第27回主线，殴打陈三刀', 0.9, None, None, 130, State.mainline_42],
    ['./pic/27_4.png', '第27回主线，回答问题3', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/27_5.png', '第27回主线，坐下', 0.9, None, None, 192, State.mainline_42],
    ['./pic/27_6.png', '第27回主线，倒酒', 0.9, None, None, keyF_index, State.mainline_42],
    ['./pic/27_7.png', '第27回主线，回答问题4', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/27_8.png', '第27回主线，和顾惜朝打架', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/28_1.png', '第28回主线，回答', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/28_2.png', '第28回主线，打架', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/28_3.png', '第28回主线，打架2', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/28_4.png', '第28回主线，打架3', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/28_8.png', '第28回主线，靠近画舫', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/28_7.png', '第28回主线，击败第2艘船船上打手', 0.9, None, None, 196, State.mainline_42],
    ['./pic/28_5.png', '第28回主线，击败第一艘船船上打手', 0.9, None, None, 193, State.mainline_42],
    ['./pic/29_1.png', '第29回主线，回答', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/29_3.png', '第29回主线，回答3', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/29_5.png', '第29回主线，回答5', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/29_6.png', '第29回主线，回答6', 0.9, None, None, choice_index, State.mainline_42],
    ['./pic/29_7.png', '第29回主线，打完颜', 0.9, None, None, fight_index, State.mainline_42],
    ['./pic/29_8.png', '第29回主线，穿衣服', 0.9, None, None, 194, State.mainline_42],
    ['./pic/yaosheng56.png', '画皮妖僧56', 0.9, None, None, 183, State.mainline_42],
    ['./pic/mainline_22.png', '第22回主线', 0.85, None, None, mainline_index, State.mainline_42],
    ['./pic/mainline_23.png', '第23回主线', 0.85, None, None, mainline_index, State.mainline_42],
    ['./pic/mainline_24.png', '第24回主线', 0.85, None, None, mainline_index, State.mainline_42],
    ['./pic/mainline_25.png', '第25回主线', 0.85, None, None, mainline_index, State.mainline_42],
    ['./pic/mainline_26.png', '第26回主线', 0.85, None, None, mainline_index, State.mainline_42],
    ['./pic/mainline_27.png', '第27回主线', 0.85, None, None, mainline_index, State.mainline_42],
    ['./pic/mainline_28.png', '第28回主线', 0.85, None, None, mainline_index, State.mainline_42],
    ['./pic/mainline_29.png', '第29回主线', 0.85, None, None, mainline_index, State.mainline_42],
     ['./pic/mainline_30.png', '第30回主线', 0.85, None, None, mainline_index, State.mainline_42],
      ['./pic/mainline_31.png', '第31回主线', 0.85, None, None, mainline_index, State.mainline_42],
         ['./pic/mainline_32.png', '第32回主线', 0.85, None, None, mainline_index, State.mainline_42],
    #['./pic/huapi.png', '画皮妖僧主线', 0.85, None, None, mainline_index, State.mainline_30_39],
]

#获得当前位置 
previous_loc = [-1,-1,0,0,0]
same_times = [0,0,0,0,0]
def get_current_loc(imsrc,map_index,player_index = 0):
    global all_map
    global previous_loc
    mainline_map = all_map[map_index]
    for i in range(len(mainline_map)):
        #print('当前要查询的index:',i)
        if mainline_map[i][3] == None and mainline_map[i][4] == None:
            x,y,confidence = get_pic_location(mainline_map[i][0],imsrc)
        else:
            x,y,confidence = get_pic_location(mainline_map[i][0],imsrc[mainline_map[i][3][1]:min(757,mainline_map[i][4][1]+50),mainline_map[i][3][0]:min(1295,mainline_map[i][4][0]+50)])
        if x and y and confidence > mainline_map[i][2]:
            print('当前所在位置：',mainline_map[i][1],',匹配率：',confidence,',x和y坐标分别为:',x,',',y)
            if previous_loc[player_index] == map_index*10 + i:
                same_times[player_index] += 1
                if same_times[player_index] > 15:
                    same_times[player_index] = 0
                   # itchat.send('在同一个场景次数太多',toUserName='@e334bf0a0cbfbabc2835c0d39d15cea8873fc07e68782796f6bd5460a5df4d75')        
            return x,y,mainline_map[i][5],mainline_map[i][6]
    print('无法识别当前所在位置')
    same_times[player_index] = 0
    return None,None,None,None
    
#获得当前状态
is_jiuling = False
def fight(hwnd,index = 0,times=20):
    # 将两个16位的值连接成一个32位的地址坐标
    global is_jiuling
    if is_jiuling:
        click_position(hwnd,427,650,2)
        click_position(hwnd,470,650,2)
        click_position(hwnd,515,650,1)
    
    # 点击右键
    
    long_position = win32api.MAKELONG(640, 360)
    for i in range(times):
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONDOWN, 0, long_position)
        time.sleep(0.5)
        win32api.SendMessage(hwnd, win32con.WM_RBUTTONUP, 0, long_position)
        time.sleep(0.5)
    right_click_position(hwnd,640,360,1)
    '''
    for i in range(times):
        key_event(hwnd,'2')
    '''
#主线任务处理,返回0表示继续后面的任务判断，1表示直接continue
def mouse_absolute(x,y,x2,y2):
    windll.user32.SetCursorPos(x, y)    #鼠标移动到  
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)    #左键按下
    time.sleep(1)
    nx = int(x2*65535/win32api.GetSystemMetrics(0))
    ny = int(y2*65535/win32api.GetSystemMetrics(1))
    print(nx,ny)
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,nx,ny)   
    time.sleep(2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

def yaosheng_fight(hwd,target = './pic/yaosheng39_4.png'):
    #组队
    time.sleep(1)
    get_picture(hwd)
    imsrc = ac.imread('./test.png')
    #当前是入队，未跟随状态[0,140]-[58.226]
    x,y,confidence = get_pic_location(ac.imread('./pic/follow_button.png'),imsrc)
    if confidence and confidence>0.9:
        click_position(hwd, x-5, y-30, 15)
        click_position(hwd, x-5, y-30, 1)
        #fight(hwd,player_index)
    else:
        result = open_file(hwd,'t',ac.imread('./pic/make_team.png'),ac.imread('./pic/team.png'))
        time.sleep(1)
        #当前自己是队长，退出
        if result == 1:
            click_position(hwd, 1047, 509, 2)
            click_position(hwd, 564, 316, 2)
            result = open_file(hwd,'t',ac.imread('./pic/make_team.png'),ac.imread('./pic/team.png'))
            time.sleep(1)
            
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        #查找妖僧
        x,y,confidence = get_pic_location(ac.imread(target),imsrc)
        if confidence and confidence>0.9:
            click_position(hwd, x-8, y-30, 2)
            click_position(hwd, 982, 583, 2)
        close_file(hwd,'t',ac.imread('./pic/make_team.png'),ac.imread('./pic/make_team.png'))  
            
def mainline_operation(hwd,x,y,index,player_index = 0):
    global char_str
    global VK_CODE
    global fight_index
    global choice_index
    global keyF_index
    global esc_index
    global cloth_index
    global continue_index
    global yaosheng39_index
    global exit_team_index
    global shenhou_flag
    global qingming_flag
    global fight_index2
    global yaosheng46_index
    global wait_index

    if index == choice_index:
        click_position(hwd, max(10,x-8), max(10,y-30), 2)
    elif index == keyF_index:
        click_key(hwd, VK_CODE['f'])
        time.sleep(1)
    #需要战斗的场景
    elif index == fight_index:
        click_position(hwd, x-8,y-30, 5)
        fight(hwd,player_index)
    #通用主线(1076,386)
    elif index == mainline_index:
        click_position(hwd, max(x,1076), max(y,386), 5)
    elif index == useless_index:
        click_position(hwd, 1257, max(10,y-30), 0)
        click_position(hwd, 1257, max(10,y-30), 1)
    elif index == yaosheng39_index:
        yaosheng_fight(hwd,'./pic/yaosheng39_4.png')
    elif index == yaosheng46_index:
        yaosheng_fight(hwd,'./pic/yaosheng46_1.png')
    elif index == exit_team_index:
        time.sleep(1)
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        #当前是入队，未跟随状态[0,140]-[58.226]
        x1,y1,confidence = get_pic_location(ac.imread('./pic/follow_button.png'),imsrc)
        x2,y2,confidence2 = get_pic_location(ac.imread('./pic/cancel_button.png'),imsrc)
        if confidence or confidence2:    
            open_file(hwd,'t',ac.imread('./pic/in_team.png'),ac.imread('./pic/in_team.png'))
            click_position(hwd, 1046, 510, 2) 
        click_position(hwd, x-8, y-30, 1)
    elif index == wait_index:
        time.sleep(10)
    elif index == fight_index2:
        make_teamleader(hwd)
        time.sleep(2)
        click_position(hwd, x-8, y-30, 1)
    elif index == 1:
        click_position(hwd, 842, 626, 1)
        click_position(hwd, 1210, 633, 2)
        click_position(hwd, 1210, 633, 2)
        click_position(hwd, 1210, 633, 2)
    #副本内操作
    elif index == 100:
        time.sleep(1)
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        #当前是入队，未跟随状态[0,140]-[58.226]
        x,y,confidence = get_pic_location(ac.imread('./pic/follow_button.png'),imsrc)
        if confidence and confidence>0.9:
            click_position(hwd, x-5, y-30, 10)
            click_position(hwd, x-5, y-30, 1)
            fight(hwd,player_index)
    #setting
    elif index == 0:
        click_position(hwd, 652, 440, 1)
    #输入名字界面
    elif index == 2:
        click_position(hwd, 610, 633, 2)
        click_position(hwd, 968, 636, 1)
    # 自动寻路中,NPC讲话中
    elif index == 6 or index == 7:
        time.sleep(1)
        return 1
    #装备道具
    elif index == equip_index:
        click_position(hwd, 1041, 621, 1) 
    #寻路模式选择
    elif index == 13:
        click_position(hwd, 773, 425, 1)
    #杂货铺
    elif index == esc_index:
        click_key(hwd, VK_CODE['esc'])
    #死亡
    elif index == 18:
        click_position(hwd, x, max(10,y-40), 1)
    #充值界面
    elif index == 60:    
        click_position(hwd, 796, 225, 1)
    #跳过视频
    elif index == 30:
        click_key(hwd, VK_CODE['esc'])
        time.sleep(1)
    #回答问题界面
    elif index == 33:
        click_position(hwd, 543, 293, 1)
        click_position(hwd, x, y-35, 1)
    #技能升级界面
    elif index == 62:
       for i in range(5):
           click_position(hwd, 300, 120+i*70, 2)
           for j in range(8):
               click_position(hwd, 666, 125 + j*70, 1)
               click_key(hwd, VK_CODE['enter'])
       time.sleep(1)
       click_position(hwd, 1221, 680, 1)
       click_key(hwd, VK_CODE['esc'])
       time.sleep(1)
    # 第一回，新手教学1
    elif index == 8: 
        key_event(hwd,'1')
        time.sleep(1)
        key_event(hwd,'2')
        '''
        click_position(hwd, 430, 680, 1)
        click_position(hwd, 560, 280, 2)
        click_position(hwd, 480, 680, 2)
        click_position(hwd, 500, 200, 1)
        '''
    # 第一回，新手教学2
    elif index == 31: 
        click_position(hwd, 430, 632, 1)
    #第二回，打水
    elif index == 15: 
        click_position(hwd, 1076, 386, 3)
        time.sleep(7)
        click_position(hwd, 1076, 386, 4)
        click_position(hwd, 1071, 474, 8)
        click_key(hwd, VK_CODE['f'])
        time.sleep(4)        
    #对话选择2
    elif index == choice2_index:
        click_position(hwd, 1037, 612, 1)
    #第三回，击飞落叶
    elif index == 20:
        key_event(hwd,'4')
        time.sleep(1)
        key_event(hwd,'5')
    #第三回，换衣服
    elif index == cloth_index: 
        click_position(hwd, max(x,1076), max(y,386), 4)
        click_key(hwd, VK_CODE['F12'])
        time.sleep(2)
        click_position(hwd, 990, 235, 2)
        click_key(hwd, VK_CODE['esc'])
    #第六回，牵马
    elif index == 21:
        click_position(hwd, 717, 527, 1)
    #第六回，骑马
    elif index == 22:
        click_position(hwd, 976, 587, 1)
        click_position(hwd, 574, 644, 1)
    #第七回，搜屋子
    elif index == 35:
        wheel_move(hwd,-3600,640,320)
        click_position(hwd, x-10, y-30, 4)
        click_position(hwd, 634, 423, 1)    
    #第8回，表演
    elif index == 40: 
        fight(hwd,player_index)
    #第十回，换衣服
    elif index == 45:
        click_position(hwd, max(x,1076), max(y,386), 4)
        click_key(hwd, VK_CODE['F12'])
        time.sleep(2)
        click_position(hwd, 913, 232, 1)
        click_key(hwd, VK_CODE['esc'])
    #11回，拼接图画
    elif index == 48:
        mouse_press_to(hwd,826,500,353,578,2)
        mouse_press_to(hwd,865,312,547,447,2)
        mouse_press_to(hwd,726,428,527,562,2)
        click_position(hwd, 781, 572, 2)
    #11回，拼接图画2
    elif index == 49:
        #mouse_absolute(798,477,471,503)
        click_position(hwd, 1000, 417, 2)
        mouse_press_to(hwd,790,448,100,0,2)
        click_position(hwd, 775, 573, 2)
        '''
        windll.user32.SetCursorPos(798, 477)
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.5)
        windll.user32.SetCursorPos(471, 501)
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        '''
    #12回，使用望气技能,望气技能设置F4
    elif index == 50:
        click_position(hwd,542,650,1)
        time.sleep(1)
    #经验溢出界面
    elif index == 46:
        click_key(hwd, VK_CODE['esc'])
        time.sleep(1)
        click_key(hwd, VK_CODE['p'])
        time.sleep(1)
        for i in range(2):
            click_position(hwd, 544, 612, 1)
    #技能修为不够
    elif index == 47:
        click_position(hwd, 532, 299, 1)
        click_key(hwd, VK_CODE['enter'])
        time.sleep(1)
        time.sleep(random.uniform(3,5))
    #第9回，搜屋子
    elif index == 36:
        click_position(hwd, x, y-40, 2)
    #第9回，按机关
    elif index == 37:
        click_position(hwd,394,37,1)
        click_position(hwd,1085,420,4)
        click_position(hwd,689,283,1)
    #升级到42
    elif index == continue_index:
        #itchat.send('主线做完了',toUserName='@e334bf0a0cbfbabc2835c0d39d15cea8873fc07e68782796f6bd5460a5df4d75') 
        return 0
    #14回，穿衣服
    elif index == 69:
        click_position(hwd, max(x,1076), max(y,386), 4)
        click_key(hwd, VK_CODE['F12'])
        time.sleep(2)
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        x,y,confidence = get_pic_location(ac.imread('./pic/16_4.png'),imsrc)
        if confidence and confidence > 0.9:
            click_position(hwd, x-8, y-30, 1)
            click_key(hwd, VK_CODE['esc'])
            time.sleep(0.5)
    elif index == 70:
        click_position(hwd, max(x,1076), max(y,386), 4)
        click_key(hwd, VK_CODE['F12'])
        time.sleep(2)
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        x,y,confidence = get_pic_location(ac.imread('./pic/18_6.png'),imsrc)
        if confidence and confidence > 0.9:
            click_position(hwd, x-8, y-30, 1)
            click_key(hwd, VK_CODE['esc'])
            time.sleep(0.5)  
    #14回，上床
    elif index == 71:
        wheel_move(hwd,-3600,640,320) 
        time.sleep(1)
        click_position(hwd, x-10, y-30, 4)
        click_position(hwd, 710,290, 1)
    #16回，坐下
    elif index == 72:
        wheel_move(hwd,-2400,640,360)
        time.sleep(1)
        click_position(hwd, x-8, y-30, 5)
        click_position(hwd, 659, 333, 1)
    elif index == 73:
        time.sleep(1)
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        x,y,confidence = get_pic_location(ac.imread('./pic/17_13.png'),imsrc)
        if confidence and confidence > 0.9:
            print('找到敌人了')
            click_position(hwd, 430, 700, 1)
            click_position(hwd, x, y+60, 2)
            click_position(hwd, 430, 700, 1)
            click_position(hwd, x, y+30, 1)
    #17回,引狼
    elif index == 74:
        click_position(hwd, 430, 700, 1)
        click_position(hwd, 651, 363, 1)
    #18回，解锁
    elif index == 75:
        for i in range(7):
            click_position(hwd, 531, 323, 1)
        click_position(hwd, 605, 323, 1)
        click_position(hwd, 837, 358, 1)
    #18，开开关
    elif index == 76:
        click_position(hwd, x, max(10,y-35), 8)
        click_position(hwd, 562, 265, 1)
    #18，挡箭
    elif index == 77:
        goto_point(hwd,79,121,762,85,812,85,1025,70,'./pic/map3.png')
        time.sleep(3)
        for i in range(5):
           click_position(hwd, 422, 688, 3)
    #止血乌云
    elif index == 78:
        wheel_move(hwd,-2400,720,360)
        time.sleep(1)
        click_position(hwd, 619, 330, 1)
        click_key(hwd, VK_CODE['f'])
    #19回，点火
    elif index == 79:
        click_position(hwd, max(x,1076), max(y,386), 5)
        click_position(hwd, 430, 700, 1)
    #19回，反弹
    elif index == 80:
        click_position(hwd, 430, 700, 1)
    #22，落座
    elif index == 81:
        click_position(hwd, x-8, y-30, 6)
        wheel_move(hwd,-2400,640,360)
        time.sleep(1)
        click_position(hwd, 635, 340, 1)
    #22,换衣服
    elif index == 82:
        click_key(hwd, VK_CODE['F12'])
        time.sleep(2)
        mouse_move(hwd,394,326)
        time.sleep(1)
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        x,y,confidence = get_pic_location(ac.imread('./pic/22_3.png'),imsrc)
        if confidence and confidence > 0.95:
            click_position(hwd, x-8, max(10,y-30), 2)
            click_key(hwd, VK_CODE['esc'])
    elif index == 83:
        goto_point(hwd,544,545)
        time.sleep(45)
    
        for i in range(4):
            get_picture(hwd)
            imsrc = ac.imread('./test.png')
            x,y,confidence = get_pic_location(ac.imread('./pic/16_5.png'),imsrc)
            print('追击辽军，开始打架')
            if confidence and confidence > 0.9:  
                fight(hwd,player_index)
            else:
                break
    #16，解开绳索
    elif index == 85:
        goto_point(hwd,399,276)
        time.sleep(4)
        click_key(hwd, VK_CODE['f'])
        time.sleep(3)
        goto_point(hwd,403,276)
        time.sleep(2)
        for i in range(2):
            click_key(hwd, VK_CODE['f'])
            time.sleep(3)
        goto_point(hwd,404,275)
        time.sleep(2)
        click_key(hwd, VK_CODE['f'])
        time.sleep(2)
        goto_point(hwd,403,278)
        time.sleep(2)
        click_key(hwd, VK_CODE['f'])
        time.sleep(2)
    #17,贴金疮药
    elif index == 86:
        goto_point(hwd,388,469)
        time.sleep(2)
        click_position(hwd, 675, 370, 1)
        click_key(hwd, VK_CODE['f'])
        time.sleep(2)
        
        goto_point(hwd,383,472)
        time.sleep(2)
        click_position(hwd, 638, 343, 1)
        click_key(hwd, VK_CODE['f'])
        time.sleep(2)
        
        goto_point(hwd,385,471)
        time.sleep(2)
        click_position(hwd, 685, 310, 1)
        click_key(hwd, VK_CODE['f'])
        time.sleep(2)
        
        goto_point(hwd,384,475)
        time.sleep(2)
        click_position(hwd, 641, 346, 1)
        click_key(hwd, VK_CODE['f'])
        time.sleep(2)
        
        goto_point(hwd,386,474)
        time.sleep(2)
        click_position(hwd, 705, 332, 1)
        click_key(hwd, VK_CODE['f'])
        time.sleep(4)    
    #18，铁血大牢找钥匙
    elif index == 88:
        wheel_move(hwd,-2400,640,360)
        goto_point(hwd,137,111,762,85,812,85,1025,70,'./pic/map3.png')
        time.sleep(13)
        click_position(hwd, 620, 357, 2)
    elif index == 90:
        click_position(hwd, x, max(10,y-35), 1)
        click_key(hwd, VK_CODE['f'])
    elif index == 130:
        for i in range(8):
            click_position(hwd, 420, 690, 1)
            click_position(hwd, 470, 690, 1)
            click_position(hwd, 520, 690, 1)
    elif index == 161:
        goto_point(hwd,606,188)
        for i in range(3):
            click_key(hwd, VK_CODE['f'])
            time.sleep(6)
    elif index == 162:
        goto_point(hwd,397,278)
        time.sleep(3)
        fight(hwd,player_index)
    elif index == 163:
        click_position(hwd, x-8, y-30, 2)
        for i in range(20):
            click_key(hwd, VK_CODE['f'])
            time.sleep(0.5)
    elif index == 164:
        click_position(hwd, x-8, y-30, 2)
        click_key(hwd, VK_CODE['f'])
    elif index == 170:
        click_key(hwd, VK_CODE['F12'])
        time.sleep(2)
        mouse_move(hwd,394,326)
        time.sleep(1)
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        x,y,confidence = get_pic_location(ac.imread('./pic/23_6.png'),imsrc)
        if confidence and confidence > 0.96:
            click_position(hwd, x-8, max(10,y-30), 2)
            click_key(hwd, VK_CODE['esc'])
    #停止战斗，重新判断
    elif index == 171:
        for i in range(2):
            for i in range(4):
                right_click_position(hwd, 640, 360, 1)
            click_key(hwd, VK_CODE['f'])
            time.sleep(1)
            click_key(hwd, VK_CODE['f'])
            time.sleep(1)
        click_position(hwd, x-8, max(10,y-30), 3) 
    elif index == 174:
        click_position(hwd, x-8, max(10,y-30), 5)
        click_key(hwd, VK_CODE['f'])
    elif index == 175:
        points = [[115,88],[98,92],[81,80],[60,101],[62,121],[65,129],]
        for i in range(6):
            wheel_move(hwd,-2400,740,360)
            goto_point(hwd,points[i][0],points[i][1],759,86,814,86,1025,69,'./pic/map5.png')
            time.sleep(3)
            click_key(hwd, VK_CODE['f'])
            time.sleep(3)
            for j in range(4):
                click_key(hwd, VK_CODE['f'])
                time.sleep(3)
            for k in range(2):
                right_click_position(hwd, 640, 360, 1)
    elif index == 176:
        click_position(hwd, 1021, 63, 2)
        click_key(hwd, VK_CODE['enter'])
    elif index == 177:
        key_event(hwd,'5',5)
    elif index == 178:
        yaosheng_fight(hwd,'./pic/yaosheng50_2.png')
    elif index == 179:
        goto_point(hwd,76,152,762,85,812,85,1025,70,'./pic/map3.png')
        time.sleep(1)
        fight(hwd,player_index,40)
    elif index == 180:
        wheel_move(hwd,-2400,640,360)
        goto_point(hwd,112,197,762,85,812,85,1025,70,'./pic/map9.png')
        time.sleep(3)
        click_position(hwd, 626, 256, 2)
    elif index == 181:
        yaosheng_fight(hwd,'./pic/yaosheng53_1.png')
    elif index == 182:
        for i in range(3):
            click_key(hwd,VK_CODE['esc'])
            time.sleep(1)
    elif index == 183:
        yaosheng_fight(hwd,'./pic/yaosheng56_1.png')
    elif index == 184:
        click_position(hwd, 560, 549, 1)
        key_event(hwd,'w',1,0.5)
        key_event(hwd,'a',1.5,0.25)
        key_event(hwd,'d',0.5,0)
        key_event(hwd,'x',0.5,2.5)
        click_position(hwd, 696, 551, 1)
    elif index == 185:
        wheel_move(hwd,-2400,640,360)
        goto_point(hwd,212,188,762,85,812,85,1025,70,'./pic/map3.png')
        time.sleep(15)
    elif index == 186:
        click_position(hwd, 690, 280, 2)
    elif index == 187:
        wheel_move(hwd,-2400,640,360)
        goto_point(hwd,110,197,762,85,812,85,1025,70,'./pic/map9.png')
        time.sleep(2)
        click_position(hwd, 680, 276, 2)
    elif index == 188:
        click_position(hwd, 676, 194, 1)
        click_position(hwd, 895, 194, 1)
        click_position(hwd, 904, 341, 1)
        click_position(hwd, 686, 333, 1)
    elif index == 189:
        wheel_move(hwd,-2400,640,360)
        goto_point(hwd,110,197,762,85,812,85,1025,70,'./pic/map9.png')
        time.sleep(2)
        click_position(hwd, 680, 276, 3)
        goto_point(hwd,126,197,762,85,812,85,1025,70,'./pic/map9.png')
    #26回主线，湖心棋阵 todo
    elif index == 190:
        return 1
    #26,打罐子，黄、白、黑、红、白、红、红、绿。
    elif index == 191:
        wheel_move(hwd,-2400,640,360)
        goto_point(hwd,151,172,762,85,812,85,1025,70,'./pic/map10.png')
        time.sleep(2)
        click_position(hwd, 642, 350, 3)
        
        goto_point(hwd,152,171,762,85,812,85,1025,70,'./pic/map10.png')
        time.sleep(2)
        click_position(hwd, 642, 360, 3)
        
        goto_point(hwd,148,167,762,85,812,85,1025,70,'./pic/map10.png')
        time.sleep(2)
        click_position(hwd, 642, 350, 3)
        
        goto_point(hwd,150,167,762,85,812,85,1025,70,'./pic/map10.png')
        time.sleep(2)
        click_position(hwd, 642, 350, 3)
        
        goto_point(hwd,152,171,762,85,812,85,1025,70,'./pic/map10.png')
        time.sleep(2)
        click_position(hwd, 642, 350, 3)
        
        goto_point(hwd,150,167,762,85,812,85,1025,70,'./pic/map10.png')
        time.sleep(2)
        click_position(hwd, 642, 350, 3)
        
        goto_point(hwd,150,167,762,85,812,85,1025,70,'./pic/map10.png')
        time.sleep(2)
        click_position(hwd, 642, 350, 3)
        
        goto_point(hwd,152,169,762,85,812,85,1025,70,'./pic/map10.png')
        time.sleep(2)
        click_position(hwd, 642, 350, 5)
    elif index == 192:
        wheel_move(hwd,-2400,640,360)
        click_position(hwd, x-8, y-30, 3)
        click_position(hwd, 641, 352, 3)
    elif index == 193:
        goto_point(hwd,383,309,762,85,812,85,1025,70,'./pic/map_10.png')
        time.sleep(1)
        for i in range(6):
            key_event(hwd,'1')
            time.sleep(2)
    elif index == 194:
        click_position(hwd,x-8, y-30, 4)
        click_key(hwd, VK_CODE['F12'])
        time.sleep(2)
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        x,y,confidence = get_pic_location(ac.imread('./pic/29_9.png'),imsrc)
        if confidence and confidence > 0.95:
            click_position(hwd, x-8, y-30, 1)
            click_key(hwd, VK_CODE['esc'])
            time.sleep(0.5)
    elif index == 195:
        click_position(hwd, 560, 549, 1)
        key_event(hwd,'w',1.5,0.5)
        key_event(hwd,'a',1.25,0)
        key_event(hwd,'r',1,0)
        key_event(hwd,'z',1,2.5)
        click_position(hwd, 696, 551, 1)
    elif index == 196:
        goto_point(hwd,358,310,762,85,812,85,1025,70,'./pic/map_10.png')
        time.sleep(2)
        click_position(hwd, 540, 240, 1)
        key_event(hwd,'a')
        time.sleep(1)
        key_event(hwd,'w')
        click_position(hwd,540,146,1)
        key_event(hwd,'spacebar')
        time.sleep(0.5)
        for i in range(2):
            key_event(hwd,'1')
            time.sleep(2)
    elif index == 197:
        click_position(hwd, 560, 549, 1)
        key_event(hwd,'w',1.5,0.5)
        key_event(hwd,'a',2,0.25)
        key_event(hwd,'f',0.75,0.25)
        key_event(hwd,'z',1,2.5)
        click_position(hwd, 696, 551, 1)
    elif index == 198:
        click_position(hwd, 560, 549, 1)
        key_event(hwd,'w',2,0)
        key_event(hwd,'s',2,0)
        key_event(hwd,'r',0.75,0)
        key_event(hwd,'x',1,2.5)
        click_position(hwd, 696, 551, 1)
    elif index == change_player_index:
        change_player(hwd)
    elif index == 200:
        click_position(hwd, x-8, y-30, 4)
        click_position(hwd, 1200, 644, 2)
    elif index == 201:
        click_position(hwd, 667, 641, 2)
        click_position(hwd, x-8, y-30, 2)
    elif index == 202:
        click_position(hwd, x-8, y-30, 2)
        click_position(hwd, 666, 393, 3)
    elif index == 203:
        time.sleep(1)
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        x2,y2,confidence2 = get_pic_location(ac.imread('./pic/mainline_1.png'),imsrc)
        if confidence2 and confidence2 > 0.9:
            click_position(hwd, x-8, y-30, 2)
            get_picture(hwd)
            imsrc = ac.imread('./test.png')
            x,y,confidence = get_pic_location(ac.imread('./pic/stable_point.png'),imsrc)
            if confidence and confidence > 0.9:
                click_position(hwd, x-8, y-30, 2)
            else:
                click_position(hwd, 452, 212, 3)
            mouse_press_to(hwd,474,688,907,688,1)
            time.sleep(2)
            get_picture(hwd)
            imsrc = ac.imread('./test.png')
            x3,y3,confidence3 = get_pic_location(ac.imread('./pic/lock.png'),imsrc)
            if confidence3 and confidence3 > 0.9:
                click_position(hwd, x-8, y-30, 2)
        else:
            print('当前不是主线1，忽略掉')
            return 0
            
    elif index == 204:
        for i in range(2):
            click_key(hwd, VK_CODE['esc'])
            time.sleep(1)
    elif index == 205:
        click_position(hwd, 1198,642, 2)
    elif index == 206:
        #set_message(hwd,x-8,y+27,'吴霄',2,False)
        key_input(hwd,'吴霄')
        set_message(hwd,x-8,y+100,'500384199208190054',2,False)
        click_position(hwd, x-8, y+170, 2)
    elif index == 210:
        click_position(hwd, 708,315, 2)
    elif index == 211:
        for i in range(6):
           click_position(hwd, 636,290, 2) 
    elif index == 212:
        click_position(hwd, 822,655, 2)
        
        
    return 1
    
    
'''
def add_teammate(hwd):
    result = open_file(hwd,'t',ac.imread('./pic/make_team.png'),ac.imread('./pic/team.png'))
    time.sleep(1)
    if result == 0:
        click_position(hwd, 889, 582, 1)
    time.sleep(1)
    get_picture(hwd)
    imsrc = ac.imread('./test.png')
    x,y,confidence = get_pic_location(ac.imread('./pic/add_button.png'),imsrc)
    if confidence and confidence > 0.96:
        click_position(hwd, x-8, max(10,y-30), 2)   
'''    
#神候令任务
shenhou_idle = 9
shenhou_map = [
            ['./pic/confirm.png','神候令-确认按钮界面',0.95,None,None,choice_index,None],
            ['./pic/confirm4.png','神候令确认按钮界面2',0.95,None,None,choice_index,None],
            ['./pic/shenhou_over.png','青崖书-神候令完成界面',0.95,None,None,3,State.shenhou_over],
            ['./pic/shenhou_button.png','便捷组队界面，有神猴令队伍',0.95,None,None,choice_index,State.shenhou_remain],
            ['./pic/make_team.png','便捷组队界面, 当前无神猴队伍',0.95,None,None,6,State.teaming],
            ['./pic/follow_button.png','组队完成，未跟随',0.95,None,None,choice_index,State.follow],
            ['./pic/cancel_button.png','组队完成，跟随中',0.95,None,None,5,State.follow],
            ['./pic/task_wait.png','正在匹配，请等待',0.95,None,None,4,State.teaming],
            
        ]
#清明上河任务
qingming_map = [
            ['./pic/home_screen.png','主界面',0.95,[576,580],[702,693],0,State.idle],
            ['./pic/shenhou_over.png','青崖书-神候令完成界面',0.95,None,None,3,State.qingming_over],
            ['./pic/qingming_button.png','青崖书-清明上河按钮',0.95,None,None,1,State.qingming_remain],
            ['./pic/auto_team.png','便捷组队界面',0.95,None,None,2,State.teaming],
            ['./pic/follow_button.png','组队完成，点击跟随',0.95,None,None,choice_index,State.follow],
            ['./pic/task_wait.png','正在匹配，请等待',0.95,None,None,4,State.teaming],
        ]
#支线任务
branch_map1 = [
    ['./pic/branch4_5.png', '说书见闻-买汤界面', 0.9, None, None, 110, State.branch],
    ['./pic/yaopu.png', '说书见闻-药铺选择按钮', 0.9, None, None, choice_index, None],
    ['./pic/branch4_1.png', '说书见闻-打水', 0.9, None, None, 108, State.branch],
    ['./pic/branch4_2.png', '说书见闻-回答', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch4_3.png', '说书见闻-回答2', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch4_4.png', '说书见闻-杨济安买汤', 0.85, None, None, 109, State.branch],
    ['./pic/branch4_6.png', '说书见闻-打架', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch4_7.png', '说书见闻-打架2', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch4_8.png', '说书见闻-提交信笺', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch4_9.png', '说书见闻-查看墓碑', 0.9, None, None, 115, State.branch],
    ['./pic/branch4_12.png', '说书见闻-查看墓碑问题', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch20_1.png', '血河-职业支线-除草', 0.85, None, None, 154, State.branch],
    ['./pic/branch20_2.png', '血河-职业支线-回门派', 0.85, None, None, 155, State.branch],
    ['./pic/branch20_3.png', '血河-职业支线-打架', 0.85, None, None, fight_index, State.branch],
    ['./pic/branch20.png', '血河-职业支线', 0.85, None, None, mainline_index, State.branch],
    ['./pic/branch4.png', '说书见闻', 0.85, None, None, mainline_index, State.branch],
]
branch_map2 = [
    ['./pic/branch6_3.png', '当年明月在-回答问题', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch6_4.png', '当年明月在-打碎琴', 0.9, None, None, 116, State.branch],
    ['./pic/branch6_5.png', '当年明月在-回答2', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch6_6.png', '当年明月在-修补古筝', 0.95, None, None, 113, State.branch],
    ['./pic/branch6_7.png', '当年明月在-弹琴', 0.95, None, None, 114, State.branch],
    ['./pic/branch6_8.png', '当年明月在-回答问题3', 0.95, None, None, choice_index, State.branch],
    ['./pic/branch6_9.png', '当年明月在-保护山伯', 0.95, None, None, fight_index, State.branch],
    ['./pic/branch6_1.png', '当年明月在-开始任务', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch6_2.png', '当年明月在-坐下', 0.9, None, None, 112, State.branch],
    ['./pic/branch6_10.png', '当年明月在-进入任务', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch6.png','当年明月在',0.85,None,None,mainline_index,State.branch],
]
branch_map3 = [
    ['./pic/branch1_1.png','京华少年行,请教李师师',0.9,None,None,choice_index,State.branch],
    ['./pic/branch1_2.png','京华少年行,告辞王瑞',0.9,None,None,choice_index,State.branch],
    ['./pic/branch1_3.png','京华少年行,制服马',0.9,None,None,fight_index,State.branch],
    ['./pic/branch1_4.png','京华少年行,上塔',0.9,None,None,choice_index,State.branch],
    ['./pic/branch1_5.png','京华少年行,回答',0.9,None,None,choice_index,State.branch],
    ['./pic/branch1_6.png','京华少年行,回答2',0.9,None,None,choice_index,State.branch],
    ['./pic/branch1_7.png','京华少年行,乞丐',0.9,None,None,choice_index,State.branch],
    ['./pic/branch1_8.png','京华少年行,跪拜佛',0.9,None,None,100,State.branch],
    ['./pic/branch1_10.png','京华少年行,找小偷',0.9,None,None,101,State.branch],
    ['./pic/branch4_10.png','京华少年行-交画',0.9,None,None,choice_index,State.branch],
    ['./pic/branch14_2.png','怪盗疑踪-问题1',0.9,None,None,choice_index,State.branch],
    ['./pic/branch14_3.png','怪盗疑踪-问题2',0.9,None,None,choice_index,State.branch],
    ['./pic/branch14_4.png','怪盗疑踪-问题3',0.9,None,None,choice_index,State.branch],
    ['./pic/branch14_5.png','怪盗疑踪-问题4',0.9,None,None,choice_index,State.branch],
    ['./pic/branch14_6.png','怪盗疑踪-问题5',0.9,None,None,choice_index,State.branch],
    ['./pic/branch14_7.png','怪盗疑踪-进入巢穴',0.9,None,None,choice_index,State.branch],
    ['./pic/branch14_8.png','怪盗疑踪-准备进入巢穴',0.9,None,None,137,State.branch],
    ['./pic/branch14_9.png','怪盗疑踪-打架',0.9,None,None,fight_index,State.branch],
    ['./pic/branch14_10.png','怪盗疑踪-打架2',0.9,None,None,158,State.branch],
    ['./pic/branch14.png','怪盗疑踪',0.8,None,None,mainline_index,State.branch],
    ['./pic/branch1.png','京华少年行',0.8,None,None,mainline_index,State.branch],
]
branch_map4 = [
    ['./pic/branch2_1.png', '一生一世一双人,打架', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch2_3.png', '一生一世一双人,划船', 0.9, None, None, 102, State.branch],
    ['./pic/branch2_17.png', '一生一世一双人,如何应付曲和星', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch2_4.png', '一生一世一双人,打曲和星', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch2_5.png', '一生一世一双人,和曲和星对峙', 0.9, None, None, 103, State.branch],
    ['./pic/branch2_6.png', '一生一世一双人,上塔', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch2_7.png', '一生一世一双人,回答问题3', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch2_8.png', '一生一世一双人,回答问题4', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch2_9.png', '一生一世一双人,击败伊啸天', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch2_10.png', '一生一世一双人,买酒', 0.9, None, None, 104, State.branch],
    ['./pic/branch2_11.png', '一生一世一双人,去迎风崖', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch2_12.png', '一生一世一双人,去迎风崖按钮', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch2_13.png', '一生一世一双人,关闭图画', 0.9, None, None, 105, State.branch],
    ['./pic/branch2_14.png', '一生一世一双人,回答绿茶问题', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch2_15.png', '一生一世一双人,回答绿茶问题2', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch2_16.png', '一生一世一双人,打公子', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch2_18.png', '一生一世一双人,找帮手，汇合', 0.9, None, None, 137, State.branch],
    ['./pic/branch22_1.png', '饮者追命,回答', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch16_1.png','十二星宫录-回答',0.9,None,None,choice_index,State.branch],
    ['./pic/branch16_2.png','十二星宫录-回答2',0.9,None,None,choice_index,State.branch],
    ['./pic/branch2.png','一生一世一双人',0.85,None,None,mainline_index,State.branch],
    ['./pic/branch16.png','十二星宫录',0.85,None,None,mainline_index,State.branch],
    ['./pic/useless_1.png','饮者追命',0.9,None,None,mainline_index,State.branch],
]
branch_map5 = [
    ['./pic/branch7_1.png','牢狱风云-回答名字',0.9,None,None,choice_index,State.branch],
    ['./pic/branch7_6.png','牢狱风云-对周格使用洞悉技能',0.9,None,None,151,State.branch],
    ['./pic/branch7_7.png','牢狱风云-对卢彦使用洞悉技能',0.9,None,None,151,State.branch],
    ['./pic/branch7_4.png','牢狱风云-对伊真使用洞悉技能',0.9,None,None,151,State.branch],
    ['./pic/branch7_2.png','牢狱风云-使用洞悉技能',0.9,None,None,118,State.branch],
    ['./pic/branch7_5.png','牢狱风云-去值班房',0.9,None,None,143,State.branch],
    ['./pic/branch7_3.png','牢狱风云-打架',0.9,None,None,fight_index,State.branch],
    ['./pic/branch8_9.png','牢狱风云-捡东西',0.9,None,None,170,State.branch],
    ['./pic/branch8_1.png','老王寻亲-打架',0.95,None,None,fight_index,State.branch],
    ['./pic/branch8_2.png','老王寻亲-打架2',0.95,None,None,fight_index,State.branch],
    ['./pic/branch8_3.png','老王寻亲-给东西',0.95,None,None,choice_index,State.branch],
    ['./pic/branch8_4.png','老王寻亲-打架3',0.95,None,None,fight_index,State.branch],
    ['./pic/branch8_5.png','老王寻亲-回答',0.95,None,None,choice_index,State.branch],
    ['./pic/branch8_7.png','老王寻亲-骑上马',0.95,None,None,165,State.branch],
    ['./pic/banghui1_1.png','帮会仗剑，任务按钮',0.9,None,None,choice_index,State.branch],
    ['./pic/banghui1_7.png','帮会仗剑，完成任务按钮',0.9,None,None,choice_index,State.branch],
    ['./pic/banghui1_2.png','帮会仗剑，守卫吃东西任务',0.9,None,None,135,State.branch],
    ['./pic/banghui1_6.png','帮会仗剑， 回复雪姨',0.9,None,None,choice_index,State.branch],
    ['./pic/banghui1_20.png','帮会仗剑， 放弃间谍任务',0.9,None,None,136,State.branch],
    ['./pic/banghui1_8.png','帮会仗剑， 抓猫',0.9,None,None,136,State.branch],
    ['./pic/banghui1_9.png','帮会仗剑， 打扫落叶',0.9,None,None,136,State.branch],
    ['./pic/banghui1_21.png','帮会仗剑，玩家店铺按钮',0.9,None,None,choice_index,State.branch], 
    ['./pic/banghui1_12.png','帮会仗剑， 商会界面',0.9,None,None,140,State.branch],
    ['./pic/banghui1_10.png','帮会仗剑， 提交物品',0.9,None,None,139,State.branch],
    ['./pic/banghui1_11.png','帮会仗剑， 买东西',0.9,None,None,choice_index,State.branch], 
    ['./pic/banghui1_17.png','帮会仗剑， 和武海对话',0.9,None,None,choice_index,State.branch],
    ['./pic/banghui1_18.png','帮会仗剑， 武海选择按钮',0.9,None,None,choice_index,State.branch],
    ['./pic/banghui1_13.png','帮会仗剑， 打武海',0.95,None,None,fight_index,State.branch],
    ['./pic/banghui1_15.png','帮会仗剑， 保护高手',0.9,None,None,fight_index,State.branch],
    ['./pic/banghui1_16.png','帮会仗剑， 打间谍',0.9,None,None,fight_index,State.branch],
    ['./pic/banghui1_19.png','帮会仗剑， 任务按钮',0.9,None,None,choice_index,State.branch],
    ['./pic/banghui1_14.png','帮会仗剑， 任务失败',0.95,None,None,141,State.branch],
    ['./pic/banghui2_1.png','帮会快意恩仇,人物按钮',0.9,None,None,choice_index,State.branch],
    ['./pic/banghui2_5.png','帮会快意恩仇,换迷天服',0.9,None,None,168,State.branch],
    ['./pic/banghui2_7.png','帮会快意恩仇,打架中',0.9,None,None,136,State.branch],
    ['./pic/banghui2_2.png','帮会快意恩仇,完成任务',0.9,None,None,choice_index,State.branch],
    ['./pic/banghui2_3.png','帮会快意恩仇,接任务',0.9,None,None,keyF_index,State.branch],
    ['./pic/banghui2_8.png','帮会快意恩仇,接任务2',0.9,None,None,keyF_index,State.branch],
    ['./pic/banghui2_9.png','帮会快意恩仇,下马威',0.9,None,None,171,State.branch],
    ['./pic/banghui2_10.png','帮会快意恩仇,查看线索',0.9,None,None,172,State.branch],
    ['./pic/banghui2_12.png','帮会快意恩仇,教训敌人',0.9,None,None,fight_index,State.branch],
    ['./pic/banghui2_4.png','帮会快意恩仇,任务按钮',0.9,None,None,choice_index,State.branch],
    ['./pic/branch19_1.png','红颜如玉-打架',0.9,None,None,137,State.branch],
    ['./pic/branch19_2.png','红颜如玉-打架2',0.9,None,None,fight_index,State.branch],
    ['./pic/branch19_3.png','红颜如玉-打架3',0.9,None,None,fight_index,State.branch],
    ['./pic/branch19_4.png','红颜如玉-打架4',0.9,None,None,fight_index,State.branch],
    ['./pic/branch19_5.png','红颜如玉-回答1',0.9,None,None,choice_index,State.branch],
    ['./pic/branch19_6.png','红颜如玉-回答2',0.9,None,None,choice_index,State.branch],
    ['./pic/branch19_7.png','红颜如玉-回答3',0.9,None,None,choice_index,State.branch],
    ['./pic/branch19.png','红颜如玉',0.85,None,None,mainline_index,State.branch],
    ['./pic/branch7.png','牢狱风云',0.85,None,None,mainline_index,State.branch],
    ['./pic/branch8.png','老王寻亲',0.85,None,None,mainline_index,State.branch],
    ['./pic/banghui1.png','帮会仗剑',0.85,None,None,mainline_index,State.branch],
    ['./pic/banghui2.png','帮会快意恩仇',0.85,None,None,mainline_index,State.branch],
]
branch_map6 = [
    ['./pic/branch3_1.png', '鹧鸪天-给钱', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch3_2.png', '鹧鸪天-打架', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch3_3.png', '鹧鸪天-酒的位置', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch3_4.png', '鹧鸪天-打秦厉', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch3_5.png', '鹧鸪天-换琴', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch3_6.png', '鹧鸪天-递纸', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch3_7.png', '鹧鸪天-看书', 0.9, None, None, 119, State.branch],
    ['./pic/branch3_8.png', '鹧鸪天-不给信', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch5_1.png', '客途问州-回答', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch5_2.png', '客途问州-打辽兵', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch5_3.png', '客途问州-打辽兵2', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch5_12.png', '客途问州-打辽工3', 0.9, None, None, 162, State.branch],
    ['./pic/branch5_4.png', '客途问州-解绑', 0.9, None, None, 106, State.branch],
    ['./pic/branch5_5.png', '客途问州-打架2', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch5_6.png', '客途问州-打boss', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch5_7.png', '客途问州-打狱卒', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch5_11.png', '客途问州-坐下', 0.9, None, None, 117, State.branch],
    ['./pic/branch5_13.png', '客途问州-寻找钥匙', 0.9, None, None, 144, State.branch],
    ['./pic/branch5_14.png', '客途问州-解开密码', 0.9, None, None, 145, State.branch],
    ['./pic/branch5_15.png', '客途问州-保护母子', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch5_16.png', '客途问州-回答问题', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch5_17.png', '客途问州-找到薛三姑', 0.9, None, None, 147, State.branch],
    ['./pic/branch5_18.png', '客途问州-对暗号', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch5_19.png', '客途问州-回答三姑问题', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch5_20.png', '客途问州-疗伤', 0.9, None, None, 150, State.branch],
    ['./pic/branch5_21.png', '客途问州-击败狱卒', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch5_22.png', '客途问州-找到乔装人', 0.9, None, None, 153, State.branch],
    ['./pic/branch5_24.png', '客途问州-买药', 0.9, None, None,163 , State.branch],
    ['./pic/branch5_25.png', '客途问州-找人', 0.9, None, None,164 , State.branch],
    ['./pic/branch17_1.png', '事理为先-击败官兵', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch18_1.png', '情义江湖-任务', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch18_2.png', '情义江湖-打架', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch18_3.png', '情义江湖-打架2', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch21.png','锦书难出',0.85,None,None,mainline_index,State.branch],
    ['./pic/branch17.png','事理为先',0.85,None,None,mainline_index,State.branch],
    ['./pic/branch18.png','情义江湖',0.85,None,None,mainline_index,State.branch],
    ['./pic/branch3.png','鹧鸪天',0.85,None,None,mainline_index,State.branch],#一个戒指
    ['./pic/branch5.png','客途问州',0.85,None,None,mainline_index,State.branch],#5个化瘀膏
]
branch_map7 = [
    ['./pic/branch9_1.png', '雪泥鸿爪-打架', 0.95, None, None, fight_index, State.branch],
    ['./pic/branch9_2.png', '雪泥鸿爪-回答2', 0.95, None, None, choice_index, State.branch],
    ['./pic/branch9_3.png', '雪泥鸿爪-打架2', 0.95, None, None, fight_index, State.branch],
    ['./pic/branch9_4.png', '雪泥鸿爪-回答3', 0.95, None, None, choice_index, State.branch],
    ['./pic/branch9_5.png', '雪泥鸿爪-打架3', 0.95, None, None, fight_index, State.branch],
    ['./pic/branch9_6.png', '雪泥鸿爪-回答4', 0.95, None, None, choice_index, State.branch],
    ['./pic/branch9_7.png', '雪泥鸿爪-打架4', 0.95, None, None, fight_index, State.branch],
    ['./pic/branch9_8.png', '雪泥鸿爪-回答5', 0.95, None, None, choice_index, State.branch],
    ['./pic/branch9_9.png', '雪泥鸿爪-找鱼', 0.95, None, None, 156, State.branch],
    ['./pic/branch9_9.png', '雪泥鸿爪-离开石庙', 0.95, None, None, 157, State.branch],
    ['./pic/branch9_11.png', '雪泥鸿爪-打架6', 0.95, None, None, fight_index, State.branch],
    ['./pic/branch10_1.png', '雪泥鸿爪-回答问题', 0.95, None, None, choice_index, State.branch],
    ['./pic/branch11_1.png', '此地有西子-回答问题', 0.95, None, None, choice_index, State.branch],
    ['./pic/branch11_2.png', '此地有西子-回答问题2', 0.95, None, None, choice_index, State.branch],
    ['./pic/branch11_3.png', '此地有西子-打架', 0.95, None, None, fight_index, State.branch],
    ['./pic/branch11_4.png', '此地有西子-打架2', 0.95, None, None, fight_index, State.branch],
    ['./pic/branch11_5.png', '此地有西子-敲钟', 0.95, None, None, 148, State.branch],
    ['./pic/branch13_1.png', '焦骨牡丹-打壮汉', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch13_2.png', '焦骨牡丹-爬楼梯', 0.9, None, None, 149, State.branch],
    ['./pic/branch13_3.png', '焦骨牡丹-打卫兵', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch15_1.png', '玉咽雪-打架', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch15_2.png', '玉咽雪-回答', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch15_3.png', '玉咽雪-回答2', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch15_4.png', '玉咽雪-回答3', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch15_5.png', '玉咽雪-回答4', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch15_6.png', '玉咽雪-回答5', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch15_7.png', '玉咽雪-回答6', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch15_8.png', '玉咽雪-回答7', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch15_9.png', '玉咽雪-打架2', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch15_10.png', '玉咽雪-回答8', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch15_11.png', '玉咽雪-回答9', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch15_12.png', '玉咽雪-回答10', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch15_13.png', '玉咽雪-回答11', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch15_14.png', '玉咽雪-回答14', 0.9, None, None, choice_index, State.branch],
    ['./pic/branch15_15.png', '玉咽雪-打架3', 0.9, None, None, fight_index, State.branch],
    ['./pic/branch15_16.png', '玉咽雪-找人', 0.9, None, None,159 , State.branch],
    ['./pic/branch15_17.png', '玉咽雪-回答15', 0.9, None, None,choice_index, State.branch],
    ['./pic/branch15_18.png', '玉咽雪-打听消息', 0.9, None, None,160, State.branch],
    ['./pic/branch15_20.png', '玉咽雪-采茶1', 0.95, None, None,161, State.branch],
    ['./pic/branch15_21.png', '玉咽雪-采茶2', 0.95, None, None,166, State.branch],
    ['./pic/branch15_22.png', '玉咽雪-采茶3', 0.95, None, None,167, State.branch],
    ['./pic/branch15_23.png', '玉咽雪-买青风藤', 0.9, None, None,163, State.branch],
    ['./pic/branch15_24.png', '玉咽雪-回答16', 0.9, None, None,choice_index, State.branch],
    ['./pic/branch15.png', '玉咽雪', 0.85, None, None, mainline_index, State.branch],
    ['./pic/branch9.png', '雪泥鸿爪', 0.85, None, None, mainline_index, State.branch],
    ['./pic/branch11.png', '此地有西子', 0.85, None, None, mainline_index, State.branch],
    ['./pic/branch13.png', '焦骨牡丹', 0.85, None, None, mainline_index, State.branch],
]

def get_child_windows(parent):        
    '''     
    获得parent的所有子窗口句柄
     返回子窗口句柄列表
     '''     
    if not parent:         
        return None     
    hwndChildList = []     
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd),  hwndChildList)  
    print('所有子句柄:',hwndChildList)
    return hwndChildList

def goto_point(hwd,x,y,loc1x=940,loc1y=16,loc2x=986,loc2y=16,loc3x=1259,loc3y=16,map_name='./pic/map.png'):
    #win32gui.SetWindowPos(hwd, win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_SHOWWINDOW)
    win32gui.SetForegroundWindow(hwd)
    open_file(hwd,'m',ac.imread('./pic/map.png'),ac.imread(map_name))
    
    set_message(hwd,loc1x,loc1y,str(x),2,False)
    set_message(hwd,loc2x,loc2y,str(y),2,True)
    time.sleep(2)
    click_position(hwd,loc3x, loc3y, 2)
    close_file(hwd,'m',ac.imread('./pic/map.png'),ac.imread(map_name))
    
def make_teamleader(hwd):
    result = open_file(hwd,'t',ac.imread('./pic/make_team.png'),ac.imread('./pic/team.png'))
    time.sleep(2)
    if result == 0:
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        x3,y3,confidence3 = get_pic_location(ac.imread('./pic/create_team.png'),imsrc)
        if confidence3 and confidence3 > 0.9:
            click_position(hwd, x3-8, y3-30, 1)
    close_file(hwd,'t',ac.imread('./pic/make_team.png'),ac.imread('./pic/team.png'))

def branch_operation(hwd,x,y,index,player_index = 0,imsrc=0):
    if index == mainline_index:
        click_position(hwd, max(x,1042), max(y-10,380), 3)
    #选择界面
    elif index == choice_index:
        click_position(hwd, max(10,x-8), max(10,y-30), 1)
    #对话界面界面，按F键
    elif index == keyF_index:
        click_key(hwd, VK_CODE['f'])
    #需要战斗的场景
    elif index == fight_index:
        click_position(hwd, max(10,x-8), max(10,y-30), 5)
        fight(hwd,player_index)
    #跪拜佛主
    elif index == 100:
        wheel_move(hwd,-2400,640,360)
        goto_point(hwd,815,402)
        time.sleep(4)
        click_position(hwd, 674, 360, 2)
    #找出小偷
    elif index == 101: 
        goto_point(hwd,839,384)
    elif index == 102:
        for i in range(8):
            click_position(hwd, 430, 700, 2)
    elif index == 103:
        click_position(hwd, x, max(10,y+60),1)
    elif index == 104:
        click_position(hwd, x-8,y-30, 2)
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        x3,y3,confidence3 = get_pic_location(ac.imread('./pic/confirm.png'),imsrc)
        if confidence3 and confidence3 > 0.9:
            print('买酒，点击确认,x:',x3,",y:",y3)
            click_position(hwd, x3-8, y3-30, 1)
        click_key(hwd,VK_CODE['esc'])
        time.sleep(1)
        click_key(hwd,VK_CODE['esc'])
    elif index == 105:
        for i in range(4):
            mouse_press_to(hwd,253,108+100*i,1031,108+100*i,2)
    elif index == 106:
        click_position(hwd, x, max(10,y-30), 5)
        click_key(hwd,VK_CODE['f'])
        time.sleep(2)
        #fight(hwd,player_index,10)
    #打水
    elif index == 108:
        wheel_move(hwd,-2400,640,360)
        click_position(hwd, x, max(10,y-30), 2)
        click_position(hwd, 548,367, 2)
    #杨济安买药
    elif index == 109:
        click_position(hwd, x, max(10,y-30), 2)
        time.sleep(30)
    elif index == 110:
        click_position(hwd, x, max(10,y-30), 2)
        click_position(hwd, 654, 366, 2)
        click_position(hwd, 566, 444, 2)
        click_key(hwd,VK_CODE['esc'])
        time.sleep(2)
        click_key(hwd,VK_CODE['esc'])
        time.sleep(2)
        click_position(hwd, 1097, 387, 30)
    elif index == 112:
        click_position(hwd, max(10,x-10), max(10,y-30), 2)
        wheel_move(hwd,-3600,640,320)
        wheel_move(hwd,2400,640,320)
        time.sleep(1)
        click_position(hwd, 639, 484, 2)
    elif index == 113:
        open_file(hwd,'b',ac.imread('./pic/package.png'),ac.imread('./pic/package.png'))
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        x3,y3,confidence3 = get_pic_location(ac.imread('./pic/task_choice.png'),imsrc)
        if x3 != None:
            click_position(hwd,x3-10,y3-30,2)
            get_picture(hwd)
            imsrc = ac.imread('./test.png')
            x,y,confidence = get_pic_location(ac.imread('./pic/line.png'),imsrc)
            x2,y2,confidence2 = get_pic_location(ac.imread('./pic/wood.png'),imsrc)
        else:
            get_picture(hwd)
            imsrc = ac.imread('./test.png')
            x,y,confidence = get_pic_location(ac.imread('./pic/line.png'),imsrc)
            x2,y2,confidence2 = get_pic_location(ac.imread('./pic/wood.png'),imsrc)
        if x != None and x2 != None:
            right_click_position(hwd,x-10,y-30,2)
            click_position(hwd, x2-10, y2-30, 1)
        close_file(hwd,'b',ac.imread('./pic/package.png'),ac.imread('./pic/package.png'))
    elif index == 114:
        right_click_position(hwd,x-10,y-30,2)
        wheel_move(hwd,-3600,640,320)
        wheel_move(hwd,3600,640,320)
        time.sleep(1)
        click_position(hwd, 718, 551, 1)
    elif index == 115:
        wheel_move(hwd,-2400,640,320)
        click_position(hwd,x-10,y-30,2)
        goto_point(hwd,684,437)
        time.sleep(5)
        click_position(hwd,640,302,1)
        time.sleep(2)
    elif index == 116:
        right_click_position(hwd,x-10,y-30,2)
        click_key(hwd,VK_CODE['f'])
    elif index == 117:
        click_position(hwd, x-8, y-30, 3)
        wheel_move(hwd,-3600,640,320)
        time.sleep(3)
        wheel_move(hwd,3600,640,320)
        time.sleep(3)
        click_position(hwd, 736, 515, 1)
    elif index == 118:
        click_position(hwd, x-10, max(10,y-30), 2)
        click_position(hwd, 420, 687, 1)
        click_position(hwd, 620, 490, 4)
        click_key(hwd,VK_CODE['esc'])
    elif index == 119:
        click_position(hwd, x-10, max(10,y-30), 3)
        wheel_move(hwd,-2400,640,320)
        click_position(hwd, 645, 364, 3)
    elif index == 135:
        x,y,confidence = get_pic_location(ac.imread('./pic/banghui1_3.png'),imsrc)
        x2,y2,confidence2 = get_pic_location(ac.imread('./pic/banghui1_4.png'),imsrc)
        x3,y3,confidence3 = get_pic_location(ac.imread('./pic/banghui1_5.png'),imsrc)
        if confidence and confidence > 0.9:
            right_click_position(hwd,x-8,y-30,1)
            click_position(hwd, 580, 360, 1)
            click_position(hwd, 1024, 625, 2)
        if confidence2 and confidence2 > 0.9:
            right_click_position(hwd,x2-8,y2-30,1)
            click_position(hwd, 580, 360, 1)
            click_position(hwd, 1024, 625, 2)
        if confidence3 and confidence3 > 0.9:
            right_click_position(hwd,x3-8,y3-30,1)
            click_position(hwd, 580, 360, 1)
            click_position(hwd, 1024, 625, 2)
    #抓猫，不抓
    elif index == 136:
         time.sleep(1)
         get_picture(hwd)
         imsrc = ac.imread('./test.png')
         x,y,confidence = get_pic_location(ac.imread('./pic/cancel_task.png'),imsrc)
         if confidence and confidence > 0.9:
             click_position(hwd, x-8, y-30, 2)
             click_key(hwd,VK_CODE['enter'])
             time.sleep(1)
             click_key(hwd,VK_CODE['esc'])
             time.sleep(1)
             click_key(hwd,VK_CODE['esc'])
             time.sleep(3)
             #wheel_move(hwd,-2400,260,310)
             get_branch_task(hwd,3)
    elif index == 137:   
        make_teamleader(hwd)
        click_position(hwd, x-8, y-30, 7)
    elif index == 138:
        click_position(hwd, 1146, 394, 15)
        click_key(hwd,VK_CODE['esc'])
        time.sleep(1)
        off_length = [[0,30],[0,-30],[30,0],[-30,0]]
        for i in range(4):
            click_position(hwd, 1146, 394, 2)
            #long_position = win32api.MAKELONG(644+off_length[i][0],375+off_length[i][1])
            # 点击左键
            click_position(hwd, 644+off_length[i][0], 375+off_length[i][1], 2)
            #win32api.SendMessage(hwd, win32con.WM_MOUSEMOVE, win32con.MK_LBUTTON, long_position) 
            for j in range(3):
                key_event(hwd,'2',1)
            
    elif index == 139:
        click_key(hwd,VK_CODE['esc'])
        time.sleep(1)
        click_key(hwd,VK_CODE['esc'])
        
    elif index == 140:
        click_position(hwd, x+80, y+4, 1)
        click_position(hwd, x-8, y+364, 2)
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        x,y,confidence = get_pic_location(ac.imread('./pic/buy_button.png'),imsrc)
        if confidence and confidence > 0.9:
            click_position(hwd, x-8, y-30, 2)
            
        click_key(hwd,VK_CODE['enter'])
        time.sleep(1)
        click_key(hwd,VK_CODE['esc'])
        time.sleep(1)
        click_key(hwd,VK_CODE['esc'])
        time.sleep(1)
        click_position(hwd, 1177, 407, 6)
    #仗剑失败
    elif index == 141:
        click_position(hwd, 445, 594, 3)
        get_branch_task(hwd,3)
    elif index == 142:
        goto_point(hwd,228,289,759,88,817,88,1026,69,'./pic/map2.png')
        time.sleep(2)
        click_position(hwd, 754, 289, 2)
        click_position(hwd, 423, 688, 2)
        click_key(hwd,VK_CODE['esc'])
    elif index == 143:
        goto_point(hwd,232,249,759,88,817,88,1026,69,'./pic/map2.png')
        time.sleep(3)
        click_position(hwd, 627, 287, 2)
        goto_point(hwd,199,225,759,88,817,88,1026,69,'./pic/map2.png')
        time.sleep(20)
    elif index == 144:
        goto_point(hwd,188,219,759,88,817,88,1026,69,'./pic/map4.png')
        time.sleep(4)
        click_key(hwd,VK_CODE['f'])
        time.sleep(2)
    elif index == 145:
        click_position(hwd, x-8, y-30, 4)
        click_position(hwd, 902, 285, 3)
        for i in range(5):
            click_position(hwd, 521, 332,1)
        for j in range(2):
            click_position(hwd, 597, 332,1)
        time.sleep(1)
        click_position(hwd, 830, 369,1)   
    elif index == 147:
        wheel_move(hwd,-2400,640,360)
        time.sleep(2)
        click_position(hwd, x-177, y-30,1)
    elif index == 148:
        goto_point(hwd,805,826)
        time.sleep(3)
        for i in range(3):
            click_position(hwd, 678, 269,2)  
    elif index == 149:
        goto_point(hwd,745,446)
        time.sleep(2)
        click_key(hwd,VK_CODE['f'])
        time.sleep(5)
        click_position(hwd, 680, 317,2)  
        
    elif index == 150:
        click_position(hwd, x-8, y-30,1)
        click_key(hwd,VK_CODE['f'])
    elif index == 151:
        click_position(hwd, x-8, y-30,3)
        click_position(hwd, 424, 686,3)
    elif index == 153:
        wheel_move(hwd,-2400,640,360)
        goto_point(hwd,132,313)
        time.sleep(7)
        click_position(hwd, 693, 359,2)
        click_position(hwd, 537, 643,2)
        click_position(hwd, 420, 684,2)
        click_position(hwd, 537, 643,2)
    elif index == 154:
        goto_point(hwd,174,237)
        time.sleep(3)
        fight(hwd,player_index,3)
        
        goto_point(hwd,173,227)
        time.sleep(3)
        fight(hwd,player_index,3)
        goto_point(hwd,167,231)
        time.sleep(3)
        fight(hwd,player_index,3)
    elif index == 155:
        click_position(hwd, 496, 647,2)
    elif index == 156:
        goto_point(hwd,110,138,760,87,811,87,1026,70,'./pic/map6.png')
        time.sleep(3)
        click_position(hwd, 583, 283,2)
    elif index == 157:
        goto_point(hwd,960,348,760,87,811,87,1026,70,'./pic/map7.png')
        time.sleep(3)
        goto_point(hwd,964,310,760,87,811,87,1026,70,'./pic/map7.png')
        time.sleep(3)
    elif index == 158:
        goto_point(hwd,238,205,760,87,811,87,1026,70,'./pic/map8.png')
        fight(hwd,player_index,10)
        
        goto_point(hwd,235,220,760,87,811,87,1026,70,'./pic/map8.png')
        fight(hwd,player_index,10)
        
        goto_point(hwd,257,221,760,87,811,87,1026,70,'./pic/map8.png')
        fight(hwd,player_index,10)
        
        goto_point(hwd,259,206,760,87,811,87,1026,70,'./pic/map8.png')
        fight(hwd,player_index,10)
    elif index == 159:
        goto_point(hwd,521,1204)
        time.sleep(3)
        click_position(hwd, 631, 319,2)
    elif index == 160:
        goto_point(hwd,504,1215)
        time.sleep(3)
        click_key(hwd,VK_CODE['f'])
        time.sleep(2)
        click_position(hwd,1039,627,2)
        
        while True:
            time.sleep(2)
            get_picture(hwd)
            imsrc = ac.imread('./test.png')
            x,y,confidence = get_pic_location(ac.imread('./pic/talk.png'),imsrc)
            if confidence and confidence > 0.9:
                click_key(hwd,VK_CODE['f'])
            else:
                break
        
        goto_point(hwd,507,1213)
        time.sleep(3)
        click_key(hwd,VK_CODE['f'])
        time.sleep(2)
        click_position(hwd,1039,627,2)
        
        while True:
            time.sleep(2)
            get_picture(hwd)
            imsrc = ac.imread('./test.png')
            x,y,confidence = get_pic_location(ac.imread('./pic/talk.png'),imsrc)
            if confidence and confidence > 0.9:
                click_key(hwd,VK_CODE['f'])
            else:
                break
        
        goto_point(hwd,506,1208)
        time.sleep(3)
        click_key(hwd,VK_CODE['f'])
        time.sleep(2)
        click_position(hwd,1039,627,2)
        
        while True:
            time.sleep(2)
            get_picture(hwd)
            imsrc = ac.imread('./test.png')
            x,y,confidence = get_pic_location(ac.imread('./pic/talk.png'),imsrc)
            if confidence and confidence > 0.9:
                click_key(hwd,VK_CODE['f'])
            else:
                break
        
        goto_point(hwd,503,1205)
        time.sleep(3)
        click_key(hwd,VK_CODE['f'])
        time.sleep(2)
        click_position(hwd,1039,627,2)
        
        while True:
            time.sleep(2)
            get_picture(hwd)
            imsrc = ac.imread('./test.png')
            x,y,confidence = get_pic_location(ac.imread('./pic/talk.png'),imsrc)
            if confidence and confidence > 0.9:
                click_key(hwd,VK_CODE['f'])
            else:
                break
    elif index == 161:
        click_position(hwd, 560, 549, 1)
        key_event(hwd,'w',2,0)
        key_event(hwd,'x',2,0)
        key_event(hwd,'r',1,2.5)
        click_position(hwd, 696, 551, 1)
    elif index == 162:
        goto_point(hwd,155,294)
        fight(hwd,0,40)
        goto_point(hwd,127,303)
        time.sleep(2)
        fight(hwd,0,40)
        goto_point(hwd,108,309)
        time.sleep(2)
        fight(hwd,0,40)
        goto_point(hwd,113,283)
        time.sleep(2)
        fight(hwd,0,40)
    elif index == 163:
        time.sleep(1)
        #买药界面
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        x2,y2,confidence = get_pic_location(ac.imread('./pic/banghui1_12.png'),imsrc)
        if confidence and confidence > 0.9:
            print('客问途舟，开始买药')
            buy_goods(hwd,x2,y2,5)
        else:
            click_position(hwd, x-8, y-30, 2)
    elif index == 164:
        wheel_move(hwd,-2400,640,360)
        click_position(hwd, 1106, 235, 5)
    elif index == 165:
        click_position(hwd, x-8, y-30, 25)
        key_event(hwd,'1')
        time.sleep(1)
        goto_point(hwd,735,421)
        time.sleep(2)
        while True:
            time.sleep(1)
            get_picture(hwd)
            imsrc = ac.imread('./test.png')
            x2,y2,confidence = get_pic_location(ac.imread('./pic/branch8_8.png'),imsrc)
            if confidence and confidence > 0.9:
                click_key(hwd,VK_CODE['f'])
                for i in range(20):
                    key_event(hwd,'spacebar',0.25,0.25)
                    
                break
    elif index == 166:
        click_position(hwd, 560, 549, 1)
        key_event(hwd,'w',2,0)
        key_event(hwd,'a',2,0)
        key_event(hwd,'x',1,2.5)
        click_position(hwd, 696, 551, 1)
    elif index == 167:
        click_position(hwd, 560, 549, 1)
        key_event(hwd,'g',2,0)
        key_event(hwd,'q',1.5,0)
        key_event(hwd,'z',1,2.5)
        click_position(hwd, 696, 551, 1)
    elif index == 168:
        click_position(hwd, max(x,1076), max(y,386), 4)
        click_key(hwd, VK_CODE['F12'])
        time.sleep(2)
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        x,y,confidence = get_pic_location(ac.imread('./pic/banghui2_6.png'),imsrc)
        if confidence and confidence > 0.9:
            click_position(hwd, x-8, y-30, 1)
            click_key(hwd, VK_CODE['esc'])
            time.sleep(0.5)
    elif index == 170:
        point_list = [[197,226],[188,219],[195,232],[200,233],[205,233]]
        for i in range(len(point_list)):
            goto_point(hwd,point_list[i][0],point_list[i][1],759,88,817,88,1026,69,'./pic/map2.png')
            time.sleep(2)
            click_key(hwd, VK_CODE['f'])
            time.sleep(2)
            if i == 1:
                click_position(hwd, 580, 159, 3)
        
        time.sleep(2)
        open_file(hwd,'b',ac.imread('./pic/package.png'),ac.imread('./pic/package.png'))
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        x3,y3,confidence3 = get_pic_location(ac.imread('./pic/task_choice.png'),imsrc)
        if x3 != None:
            click_position(hwd,x3-10,y3-30,2)
            get_picture(hwd)
            imsrc = ac.imread('./test.png')
            #衣服
            x,y,confidence = get_pic_location(ac.imread('./pic/cloth.png'),imsrc)
            #狗肉
            x2,y2,confidence2 = get_pic_location(ac.imread('./pic/dog_food.png'),imsrc)
            #酒
            x3,y3,confidence3 = get_pic_location(ac.imread('./pic/wine.png'),imsrc)
            #棒子
            x4,y4,confidence4 = get_pic_location(ac.imread('./pic/bang.png'),imsrc)
            #蒙汗药
            
            
        else:
            get_picture(hwd)
            imsrc = ac.imread('./test.png')
            x,y,confidence = get_pic_location(ac.imread('./pic/line.png'),imsrc)
            x2,y2,confidence2 = get_pic_location(ac.imread('./pic/wood.png'),imsrc)
        #
    elif index == 171:
        time.sleep(1)
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        x,y,confidence = get_pic_location(ac.imread('./pic/cancel_task.png'),imsrc)
        if confidence and confidence > 0.9:
            click_position(hwd, x-8, y-30, 2)
            click_key(hwd,VK_CODE['enter'])
            time.sleep(1)
            click_key(hwd,VK_CODE['esc'])
            time.sleep(1)
            click_key(hwd,VK_CODE['esc'])
            time.sleep(3)
            #wheel_move(hwd,-2400,260,310)
            get_branch_task(hwd,5)
    elif index == 172:
        open_file(hwd,'b',ac.imread('./pic/package.png'),ac.imread('./pic/package.png'))
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        x3,y3,confidence3 = get_pic_location(ac.imread('./pic/task_choice.png'),imsrc)
        if x3 != None:
            click_position(hwd,x3-10,y3-30,2)
            get_picture(hwd)
            imsrc = ac.imread('./test.png')
            x,y,confidence = get_pic_location(ac.imread('./pic/banghui2_11.png'),imsrc)
        else:
            get_picture(hwd)
            imsrc = ac.imread('./test.png')
            x,y,confidence = get_pic_location(ac.imread('./pic/banghui2_11.png'),imsrc)
        if confidence and confidence >0.95:
            right_click_position(hwd,x-8,y-30,2)
            #click_position(hwd, x-8, y-30, 3)
        close_file(hwd,'b',ac.imread('./pic/package.png'),ac.imread('./pic/package.png'))
        time.sleep(1)
    else:
        return 0
    
    return 1

def buy_goods(hwd,x,y,number = 1):
    click_position(hwd, x+80, y+4, 1)
    click_position(hwd, x-8, y+364, 2)
    get_picture(hwd)
    imsrc = ac.imread('./test.png')
    x,y,confidence = get_pic_location(ac.imread('./pic/buy_button.png'),imsrc)
    if confidence and confidence > 0.9:
        for i in range(number):
            click_position(hwd, x-8, y-30, 2)
            click_key(hwd,VK_CODE['enter'])
            time.sleep(1)
            
    click_key(hwd,VK_CODE['esc'])
    time.sleep(1)
    click_key(hwd,VK_CODE['esc'])
    time.sleep(1)
    click_position(hwd, 1177, 407, 6)
branch_task_map = [
            ['./pic/task_25.png','说书雅集'],
            ['./pic/task_27.png','当年明月在'],
            ['./pic/task_35.png','京华少年行'],
            ['./pic/banghui_1.png','帮会仗剑风云'],
            ['./pic/task_42.png','一生一世一双人'],
            ['./pic/banghui_2.png','帮会快意恩仇'],
            ['./pic/task_36.png','怪盗疑踪'],
            ['./pic/task_44.png','玉咽雪'],
            ['./pic/task_46.png','客问途舟'],
            ['./pic/task_43.png','牢狱风云'],
            ['./pic/task_49.png','老王寻亲上'],
            ['./pic/task_51.png','此地有西子'],
            ['./pic/task_52.png','鹧鸪天'],
            ['./pic/task_54.png','事理为先'],
            ['./pic/task_54_1.png','情义江湖'],
            ['./pic/task_56.png','焦骨牡丹'],
        ]    
#返回是否执行continue指令的flag
def get_branch_task(hwd,task_index = -1):
    global branch_task_map
    open_file(hwd,'l',ac.imread('./pic/task_list.png'),ac.imread('./pic/task_list.png'))
    
    get_picture(hwd)
    imsrc = ac.imread('./test.png')
    x,y,confidence = get_pic_location(ac.imread('./pic/branch_list.png'),imsrc)
    if confidence and confidence > 0.9:
        click_position(hwd, x-8, y-30, 2)
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
    
    if task_index != -1:
        #wheel_move(hwd,)
        x2,y2,confidence = get_pic_location(branch_task_map[task_index][0],imsrc)
        if confidence and confidence > 0.9:
            print('添加特定新的支线任务:',branch_task_map[task_index][1])
            click_position(hwd, x2-8, y2-30, 2)
            get_picture(hwd)
            imsrc = ac.imread('./test.png')
            x3,y3,confidence = get_pic_location(ac.imread('./pic/branch_button.png'),imsrc)
            if confidence and confidence >0.9:
                click_position(hwd, x3-8, y3-30, 3)
                get_picture(hwd)
                imsrc = ac.imread('./test.png')
                x4,y4,confidence = get_pic_location(ac.imread('./pic/banghui1_19.png'),imsrc)
                if confidence and confidence >0.9:
                    click_position(hwd, x4-8, y4-30, 2)
                #close_file(hwd,'l',ac.imread('./pic/task_list.png'),ac.imread('./pic/task_list.png'))
                time.sleep(2)
            return 1
        else:
            '''
            get_picture(hwd)
            imsrc = ac.imread('./test.png')
            x4,y4,confidence4 = get_pic_location(ac.imread('./pic/banghui1_22.png'),imsrc)
            if confidence4 and confidence4 >0.9:
                mouse_press_to(hwd,x4-8,y4-30,x4-8,y4+30,2)
            time.sleep(1)
            get_branch_task(hwd,task_index)
            '''
            return 1
                
            
    else: 
        for i in range(len(branch_task_map)):
            x,y,confidence = get_pic_location(branch_task_map[i][0],imsrc)
            if confidence and confidence > 0.9:
                print('添加新的支线任务:',branch_task_map[i][1])
                click_position(hwd, x-8, y-30, 1)
                x,y,confidence = get_pic_location(ac.imread('./pic/get_task.png'),imsrc)
                if  confidence and confidence > 0.9:
                    click_position(hwd, x-8, y-30, 1)
                #close_file(hwd,'l',ac.imread('./pic/task_list.png'),ac.imread('./pic/task_list.png'))
                time.sleep(5)
                return 1
        
    #close_file(hwd,'l',ac.imread('./pic/task_list.png'),ac.imread('./pic/task_list.png'))
    return 0
        
    
def upgrade(hwnd):
    open_file(hwnd,'p',ac.imread('./pic/people.png'),ac.imread('./pic/people.png'))
    time.sleep(1)
    click_position(hwnd, 544,612, 2)
    get_picture(hwnd)
    imsrc = ac.imread('./test.png')
    x,y,confidence = get_pic_location(ac.imread('./pic/upgrade_skill.png'),imsrc)
    if x == None and y == None:
        click_key(hwnd, VK_CODE['p'])
        time.sleep(1)
def close_file(hwd,shortcut,imobj,imobj2):
    #按键直接找一遍
    get_picture(hwd)
    imsrc = ac.imread('./test.png')
    x,y,confidence = get_pic_location(imobj,imsrc) 
    if confidence != None and confidence > 0.9:
        print('当前界面打开，准备关闭。界面快捷键是:',shortcut)
        click_key(hwd,VK_CODE['esc'])
        return
    
    x,y,confidence = get_pic_location(imobj2,imsrc)
    if confidence != None and confidence > 0.9:
        print('当前界面打开，准备关闭。界面快捷键是:',shortcut)
        click_key(hwd,VK_CODE['esc'])
        return

    print('open_file():预期要关闭的界面未查询到，已经关闭')
    
def open_file(hwd,shortcut,imobj,imobj2):
    #按键直接找一遍
    click_key(hwd, VK_CODE[shortcut]) 
    time.sleep(1)
    get_picture(hwd)
    imsrc = ac.imread('./test.png')
    x,y,confidence = get_pic_location(imobj,imsrc) 
    if confidence != None and confidence > 0.9:
        print('当前界面打开，界面快捷键是:',shortcut)
        return 0
    
    x,y,confidence = get_pic_location(imobj2,imsrc)
    if confidence != None and confidence > 0.9:
        print('当前界面打开，界面快捷键是:',shortcut)
        return 1
    #按键再找一遍
    click_key(hwd, VK_CODE[shortcut]) 
    time.sleep(1)
    get_picture(hwd)
    imsrc = ac.imread('./test.png')
    x,y,confidence = get_pic_location(imobj,imsrc) 
    if confidence != None and confidence > 0.9:
        print('当前界面打开，界面快捷键是:',shortcut)
        return 0
    
    x,y,confidence = get_pic_location(imobj2,imsrc)
    if confidence != None and confidence > 0.9:
        print('当前界面打开，界面快捷键是:',shortcut)
        return 1
    
    print('open_file():找不到当前预期的界面')
    return -1
def is_shenhou_over(hwd):
    open_file(hwd,'j',ac.imread('./pic/qingyashu.png'),ac.imread('./pic/qingyashu2.png'))
    #当前是神猴完成界面，则退出
    time.sleep(1)
    get_picture(hwd)
    imsrc = ac.imread('./test.png')
    x,y,confidence = get_pic_location(ac.imread('./pic/shenhou_over.png'),imsrc) 
    if confidence != None and confidence > 0.9:
        print('神猴令完成')
        click_key(hwd, VK_CODE['j']) 
        return True
    
    click_key(hwd, VK_CODE['j']) 
    time.sleep(1)
    return False

def make_shenhou_team(hwd):
    while True:
        open_file(hwd,'t',ac.imread('./pic/make_team.png'),ac.imread('./pic/leader.png'))
        #寻找一级神猴令按钮
        print('已经打开便捷组队界面')
        time.sleep(2)
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        #当前已经在队伍了，退出
        x,y,confidence = get_pic_location(ac.imread('./pic/in_team.png'),imsrc)
        if confidence != None and confidence > 0.9:
            print('已经在队长队伍中，不用再组队了')
            return True
        #当前自己是队长，退出组队
        x,y,confidence = get_pic_location(ac.imread('./pic/leader.png'),imsrc)
        if confidence != None and confidence > 0.9:
            print('当前自己是队长，退出组队')
            click_position(hwd, 1055, 505, 1)
            return False
        
        #当前没在队伍，组队
        x,y,confidence = get_pic_location(ac.imread('./pic/shenhou_choice.png'),imsrc)
        if confidence != None and confidence > 0.9:
            click_position(hwd, x, max(10,y-35), 1)
            click_position(hwd, 991, 578, 1)
            print('神猴令已经点击自动匹配')
        else:
            print('神候令组队流程，没找到一级按钮界面')
        
        #验证当前是否在匹配中
        time.sleep(2)
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        x,y,confidence = get_pic_location(ac.imread('./pic/task_wait.png'),imsrc)
        if confidence != None and confidence > 0.9:
            print('当前在神候令匹配中')
            click_key(hwd, VK_CODE['t']) 
            return True
    
        
        
#第一个返回是否执行continue代码,第二个返回数组值表示神候令是否完成
def shenhou_task(hwd):
    #当前没在组队组队神猴令
    get_picture(hwd)
    imsrc = ac.imread('./test.png')
    #判断当前是否入队，没入队才入队
    x,y,confidence = get_pic_location(ac.imread('./pic/follow_button.png'),imsrc)
    x2,y2,confidence2 = get_pic_location(ac.imread('./pic/cancel_button.png'),imsrc)
    if confidence == None and confidence2 == None:
        print('开始神候令组队')
        result = make_shenhou_team(hwd)
        if result == False:
            print('神猴组队失败，重新开始流程')
        print('神猴令组队完成')
        
    #等待入队，跟随
    not_team_times = 0
    while True:
        time.sleep(4)
        print('等待神候令组队中')
        get_picture(hwd)
        imsrc = ac.imread('./test.png')
        #当前是入队，未跟随状态[0,140]-[58.226]
        x,y,confidence = get_pic_location(ac.imread('./pic/follow_button.png'),imsrc)
        if confidence != None and confidence > 0.9:
            print('当前在组队状态，未跟随')
            not_team_times = 0
            click_position(hwd, x, max(10,y-35), 1)
            #判断是否要按确认按钮
            get_picture(hwd)
            imsrc = ac.imread('./test.png')
            x,y,confidence = get_pic_location(ac.imread('./pic/confirm4.png'),imsrc)
            if confidence != None and confidence > 0.9:
                click_position(hwd, x, max(10,y-35), 1)
            time.sleep(5)
            
        else:
            #当前是入队，跟随状态
            x,y,confidence = get_pic_location(ac.imread('./pic/cancel_button.png'),imsrc)
            if confidence != None and confidence > 0.9:
                print('当前在组队状态，跟随中')
                not_team_times = 0
                time.sleep(5)
                #判断是否要按确认按钮
                get_picture(hwd)
                imsrc = ac.imread('./test.png')
                x,y,confidence = get_pic_location(ac.imread('./pic/confirm4.png'),imsrc)
                if confidence != None and confidence > 0.9:
                    click_position(hwd, x, max(10,y-35), 1)
                time.sleep(5)
                continue  
            #异常状态
            else:
                not_team_times += 1
                time.sleep(15)
                if not_team_times > 5:
                    print('脱离组队状态，重新判断神候令状态')
                    break
 
window_handle = 0
check_string = '逆水寒 角色ID'
check_string2 = 'Version'
def show_window_attr(hWnd):
    global window_handle
    global check_string
    if not hWnd:
        return False
    #中文系统默认title是gb2312的编码
    title = win32gui.GetWindowText(hWnd)
    clsname = win32gui.GetClassName(hWnd)
    if check_string in title:
        print('窗口句柄:%s ' % (hWnd))
        print('窗口标题:%s' % (title))
        print('窗口类名:%s' % (clsname))
        window_handle = hWnd
        return True
        #win32gui.SetBkMode(hWnd, win32con.TRANSPARENT)
    if check_string2 in title:
        print('登录界面窗口句柄:%s ' % (hWnd))
        print('登录界面窗口标题:%s' % (title))
        print('登录界面窗口类名:%s' % (clsname))
        window_handle = hWnd
        return True

    return False
def show_windows(hWndList):
    for h in hWndList:
        result = show_window_attr(h)
        if result:
            break
 
def demo_top_windows():
    #初始化相关数据结构
    global window_handle

    window_handle = 0
    hWndList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)
    show_windows(hWndList)
         
all_map = [common_map,mainline_map1,mainline_map2,mainline_map3,mainline_map4,mainline_map5,mainline_map6,
           branch_map1,branch_map2,branch_map3,branch_map4,branch_map5,branch_map6,branch_map7,fight_map,
           branch_task_map]

#前提，最低效，分辨率最低，望气技能设置为F4，攻击技能是F1,F2,1
player_point = [[322,655],[422,655],[522,655],[622,655],[722,655],[822,655]]
def change_player(hwd,nextplayer_index=5):
    global player_point
    global window_handle
    open_file(hwd,'esc',ac.imread('./pic/set.png'),ac.imread('./pic/set.png'))
    click_position(hwd, 715, 275, 10)
    print('等待选择新角色')
    #新建角色
    click_position(window_handle, player_point[nextplayer_index][0], player_point[nextplayer_index][1], 2)

def upgrade_fight_info(hwd,player_index):
    global shenhou_flag
    global qingming_flag
    open_file(hwd,'j',ac.imread('./pic/qingyashu.png'),ac.imread('./pic/qingyashu.png'))
    get_picture(hwd)
    imsrc = ac.imread('./test.png')
    x,y,confidence = get_pic_location(ac.imread('./pic/shenhou.png'),imsrc)
    x2,y2,confidence2 = get_pic_location(ac.imread('./pic/luofeng.png'),imsrc)
    if confidence != None and confidence > 0.95:
        print('深喉令没做')
        shenhou_flag = 0
    else:
        shenhou_flag = 1
    if confidence2 != None and confidence2 > 0.9:
        print('落风山庄没做')
        qingming_flag = 0
    else:
        qingming_flag = 1
        
#前提，最低效，分辨率最低，望气技能设置为F4，攻击技能是F1,F2,1
def main():
    '''
    主函数
    '''
    #最低特效，分辨率
    global window_handle
    global shenhou_flag
    global qingming_flag
    global esc_index
    global is_jiuling
    now_state = [0,0,0,0,0,0,0,0,0,0]

    fail_times = [0,0,0,0,0,0,0,0,0,0]
    last_map_index = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    demo_top_windows()
                    
    if window_handle == 0:
        print('未找到任何窗口句柄')
        return

    #初始化对应消息接收的微信
    '''
    itchat.auto_login(hotReload=True)
    friends_list = itchat.get_friends(update=True)
    name = itchat.search_friends(name=u'哈哈你')
    userName = name[0]["UserName"]
    print('微信名字:',userName)
    itchat.send('开始执行逆水寒自动化脚本',toUserName=userName)
    '''
    #read所有的imobj
    for i in range(len(all_map)):
        for j in range(len(all_map[i])):
            all_map[i][j][0] = ac.imread(all_map[i][j][0])
    
    #win32gui.SetWindowPos(hwnd_list[0], win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_SHOWWINDOW)
    #判断是不是九零
    get_picture(window_handle)
    imsrc = ac.imread('./test.png')
    x,y,confidence = get_pic_location(ac.imread('./pic/jiuling_logo.png'),imsrc)
    if confidence != None and confidence > 0.8:
        print('当前职业是九零')
        is_jiuling = True
    else:
        print('当前职业不是九零，confidence:',confidence)
    while True:
        i = 0
        my_hwnd = window_handle
        continue_flag = 0
        #刷新界面
        get_picture(my_hwnd)
        imsrc = ac.imread('./test.png')

        #做通用任务
        x,y,index,now_state[i]= get_current_loc(imsrc,0,i)
        if x and y :
            continue_flag = mainline_operation(my_hwnd,x,y,index,i)
            if continue_flag:
                fail_times[i] = 0
                continue
        #做上次主线的任务
        if last_map_index[i] >= 1 and last_map_index[i] <= 6:
            x, y, index, now_state[i] = get_current_loc(imsrc,last_map_index[i] , i)
            if x and y:
                continue_flag = mainline_operation(my_hwnd, x, y, index, i)
                if continue_flag:
                    fail_times[i] = 0
                    continue
        #做上次的支线任务
        if last_map_index[i] >= 7 and last_map_index[i] <= 13:
            x, y, index, now_state[i] = get_current_loc(imsrc,last_map_index[i] , i)
            if x and y:
                continue_flag = branch_operation(my_hwnd, x, y, index, i,imsrc)
                if continue_flag:
                    fail_times[i] = 0
                    continue

        #循环所有主线任务map
        for task_index in range(6):
            x,y,index,now_state[i] = get_current_loc(imsrc,1+task_index,i)
            if x and y :
                continue_flag = mainline_operation(my_hwnd,x,y,index,i)
                last_map_index[i] = 1+task_index
                break
        if continue_flag:
            fail_times[i] = 0
            continue

        #升级
        if imsrc[747,1285,0] == 165 and imsrc[747,1285,1] == 255 and imsrc[747,1285,2] == 166 and fail_times[i] >= 4:
            print('升级人物')
            upgrade(my_hwnd)
            continue
        #循环所有支线任务map
        for task_index in range(7):
            x,y,index,now_state[i] = get_current_loc(imsrc,7+task_index,i)
            if x and y :
                continue_flag = branch_operation(my_hwnd,x,y,index,i,imsrc)
                last_map_index[i] = 7+task_index
                break
            else:
                #选取一个任务，优先级从等级低的开始
                if fail_times[i] >= 5:
                    continue_flag = get_branch_task(my_hwnd)
                    break
        if continue_flag:
            #fail_times[i] = 0
            continue

        #在打架的地图
        x, y, index, now_state[i] = get_current_loc(imsrc, 14, i)
        if x and y:
            continue_flag = mainline_operation(my_hwnd, x, y, index, i)
            if index != esc_index:
                last_map_index[i] = 14
            if continue_flag:
                fail_times[i] = 0
                continue

        #未识别到有效操作
        print('未识别到主线有效操作流程,当前人物编号:',i,'失败次数:',fail_times[i])
        #time.sleep(random.uniform(1,2))
        mouse_move(my_hwnd,640,360)
        fail_times[i] += 1
        if fail_times[i] >= 6:
            print('失败次数超过上限，点击esc按钮')
            #itchat.send('逆水寒自动脚本失效了',toUserName=userName)
            fail_times[i] = 0
            for i in range(3):
                click_key(my_hwnd, VK_CODE['esc'])
                time.sleep(1)
            

if __name__ == '__main__':
    main()















