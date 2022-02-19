from toplist_spider import *
from random_spider import *
from latest_spider import *

def select_mode():
    '''提供用户选择爬虫模式的功能'''
    
    print('请输入数字，1代表模式一，2代表模式2，3代表模式3.')
    res = eval(input('请选择爬虫的模式：'))
    
    if res == 1 :
        print('启动模式1')
        latest_list_spider()
    elif res == 2:
        print('启动模式2')
        top_list_spider()
    elif res == 3:
        print('启动模式3')
        random_list_spider()
    else:
        print('无效输入！')
        
    return