import time
import random
import agent_pool
from classify_img import *

from bs4 import BeautifulSoup
from multiprocessing import Process, Queue
from concurrent.futures import ThreadPoolExecutor
from math import ceil
import os, sys

# 防止程序出现连接错误
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.ssl_ import create_urllib3_context
CIPHERS = (
            'ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
            'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES:!aNULL:'
            '!eNULL:!MD5'
          )
class DESAdapter(HTTPAdapter):
    """
    A TransportAdapter that re-enables 3DES support in Requests.
    """

    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=CIPHERS)
        kwargs['ssl_context'] = context
        return super(DESAdapter, self).init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=CIPHERS)
        kwargs['ssl_context'] = context
        return super(DESAdapter, self).proxy_manager_for(*args, **kwargs)


def get_img_src(num, q, q_name):
    page = ceil(num / 24) # 取大于或者等于num / 24的最大整数
    n = 1
    url = 'https://wallhaven.cc/latest'

    # 爬取数量过多时自动启用第三方代理
    if num > 500:
        agent = agent_pool.spider_ip()
        proxy = {
            'http':'http://' + agent,
            'https': 'https://' + agent
        }
   
    thumb_href_list = []
    for page_num in range(page):
        page_num += 1
        params = {
        'page': f'{page_num}'
        }
        if num > 500:
            resp = requests.get(url, params=params, proxies=proxy)
        else:
            resp = requests.get(url, params=params)
        resp.encoding = 'utf-8'
        latest_list_page = BeautifulSoup(resp.text, "html.parser")
        thumb_href_list_plus = latest_list_page.find_all('a', attrs={'class':'preview'})
        thumb_href_list = thumb_href_list + thumb_href_list_plus
    thumb_href_list = thumb_href_list[:num] 
    for thumb_href in thumb_href_list:
        href = thumb_href.get('href')

        # 得到每一张图片的href
        # 用href去请求
        if num > 500:
            resp_next = requests.get(href, proxies=proxy)
        else:
            resp_next = requests.get(href)

        #防止请求过于频繁
        random_num = random.randint(3, 10)
        time.sleep(random_num)

        # 设置编码
        resp_next.encoding = 'utf-8'

        resp_next_page = BeautifulSoup(resp_next.text, "html.parser")
        # 初始化BeautifulSoup对象
        wallpaper_href = resp_next_page.find('img', attrs={'id':'wallpaper'})
        wallpaper_href_url = wallpaper_href.get('src')
        
        q.put(wallpaper_href_url)
        q_name.put(n)
        n += 1
        
    q.put('over')
        
    return

def download(url, n):
    img_reps = requests.get(url)
    os.chdir(sys.path[0])
    with open(f'../wallpaper/{n}.png', mode='wb') as f:
        f.write(img_reps.content)
    return

def download_img(q, q_name):
    with ThreadPoolExecutor(10) as t:
        while(1):            
            url = q.get() # 如果没数据则阻塞
            if url == 'over':
                break
            n = q_name.get()
            t.submit(download, url, n)
    
    return

def spider(num):
    q = Queue()
    q_name = Queue()
    p1 = Process(target=get_img_src, args=(num, q, q_name,))
    p2 = Process(target=download_img, args=(q, q_name,))
    
    p1.start()
    p2.start()

    # 等待p2进程执行完成后再执行主进程
    # 防止分类时图片还没下载完毕
    p2.join()
    classify_img() # 自动分类

def latest_list_spider():
    print('请输入想要爬取图片的数量:')
    num = eval(input())
    if isinstance(num, int):
        if num <= 500:
            spider(num)
        else:
            print('提示：爬取数量较多，将自动启用第三方代理伪装，这会稍微降低爬取速度。')
            spider(num)
    else:
        print('请输入数字！')

    return