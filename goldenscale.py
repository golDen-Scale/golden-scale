#!/usr/bin/env python
# 作者：golDen-Scale
# 版本：1.0
# License: MIT License


import os
import re
import io
import ssl
import json
import argparse
import string
import logging
import time
import requests
import urllib
import urllib.parse
import scrapy
import beautifulsoup4
import threading
import builtwith
from selenium import webdriver
from collections import defaultdict

# 定义爬取结果的数据结构
class Result:
    def __init__(self, source, url, where):
        self.source = source
        self.url = url
        self.where = where

# 全局变量，用于存储 HTTP 请求的头部信息
headers = {}


# 定义一个带默认值的字典
class SyncMap:
    def __init__(self):
        self._data = defaultdict(lambda: None)

    def Load(self, key):
        return self._data[key]

    def Store(self, key, value):
        self._data[key] = value

    def Delete(self, key):
        del self._data[key]

# 创建一个 SyncMap 的实例
sm = SyncMap()

# 主动扫描
def main():



    # 创建解析器对象
    parser = argparse.ArgumentParser(description='Website crawler options')

    # 添加命令行参数
    parser.add_argument('-i', '--inside', action='store_true', help='Only crawl inside path')
    parser.add_argument('-t', '--threads', type=int, default=8, help='Number of threads to utilise.')
    parser.add_argument('-d', '--depth', type=int, default=2, help='Depth to crawl.')
    parser.add_argument('--size', type=int, default=-1, help='Page size limit, in KB.')
    parser.add_argument('--insecure', action='store_true', help='Disable TLS verification.')
    parser.add_argument('--subs', action='store_true', help='Include subdomains for crawling.')
    parser.add_argument('--json', action='store_true', help='Output as JSON.')
    parser.add_argument('-s', '--showSource', action='store_true', help='Show the source of URL based on where it was found. E.g. href, form, script, etc.')
    parser.add_argument('-w', '--showWhere', action='store_true', help='Show at which link the URL is found.')
    parser.add_argument('-h', '--rawHeaders', default='', help='Custom headers separated by two semi-colons. E.g. -h "Cookie: foo=bar;;Referer: http://example.com/"')
    parser.add_argument('-u', '--unique', action='store_true', help='Show only unique urls.')
    parser.add_argument('--proxy', default='', help='Proxy URL. E.g. --proxy http://127.0.0.1:8080')
    parser.add_argument('--timeout', type=int, default=-1, help='Maximum time to crawl each URL from stdin, in seconds.')
    parser.add_argument('--dr', action='store_true', help='Disable following HTTP redirects.')

    # 解析命令行参数
    args = parser.parse_args()

    # 打印解析结果
    print("inside:", args.inside)
    print("threads:", args.threads)
    print("depth:", args.depth)
    print("size:", args.size)
    print("insecure:", args.insecure)
    print("subs:", args.subs)
    print("json:", args.json)
    print("showSource:", args.showSource)
    print("showWhere:", args.showWhere)
    print("rawHeaders:", args.rawHeaders)
    print("unique:", args.unique)
    print("proxy:", args.proxy)
    print("timeout:", args.timeout)
    print("disableRedirects:", args.dr)











# 定义一个全局变量用于存储已经处理过的 URL
processed_urls = set()

# 检查给定的 URL 是否是唯一的
def isUnique(url):
    # 如果 URL 已经存在于 processed_urls 中，返回 False
    if url in processed_urls:
        return False
    # 如果 URL 不存在于 processed_urls 中，将其添加，并返回 True
    processed_urls.add(url)
    return True








if __name__ == "__main__":
    main()