import requests
from bs4 import BeautifulSoup
from multiprocessing import Process, Queue
from concurrent.futures import ThreadPoolExecutor
from lxml import etree
import redis

def get_ip_data():
    url = 'https://www.kuaidaili.com/free/inha/'

    ip_list = []
    port_list = []

    for page in range(5):
        page += 1
        url = url + str(page) + '/'
        resp = requests.get(url)
        resp.encoding = 'utf-8'
        et = etree.HTML(resp.text)
        tem_ip_list = et.xpath('//td[@data-title="IP"]/text()')
        tem_port_list = et.xpath('//td[@data-title="PORT"]/text()')
        ip_list += tem_ip_list
        port_list += tem_port_list

    data_list = []
    for i in range(0,len(ip_list)):
        data_list.append(ip_list[i]+':'+port_list[i])

    for ip_and_port in data_list:
        yield ip_and_port

def check_ip(conn):
    url = 'https://www.baidu.com'
    
    while 1:
        try:
            ip = conn.srandmember('proxy')
            ip = ip.decode("utf-8")
            proxy_ip = ip
            proxy = {
                'http': 'http://' + proxy_ip,
                'https': 'https://' + proxy_ip
            }

            # 5秒内无法连接到服务器，则此ip数据作废
            resp = requests.get(url, proxies=proxy, timeout=5)

            # 一旦此ip可用
            # 即运行到此处没有抛出错误
            # 则立即使用此ip进行伪装
            return proxy_ip
        except:
            # 报错之后转到异常处理，删除失效的ip数据
            conn.srem('proxy', ip)

            # 进入死循环检查ip可用性

def redis_ip_data(ip_data, conn):
    # 建立ip数据库
    conn.sadd('proxy', ip_data)

def spider_ip():
    '''这个函数的作用是返回一个可用的IP地址'''

    # 爬取ip数据，生成生成器
    gen = get_ip_data()
    # 连接数据库
    conn = redis.Redis(host='localhost', port=6379)
    for ip_data in gen:
        # 从生成器中逐一取出ip数据
        # 压入数据库中
        redis_ip_data(ip_data, conn)

    # 检查数据库中ip的可用性
    proxy_ip = check_ip(conn)
    return proxy_ip