# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import js2xml
from lxml import etree
import socket
import time
import logging
import logging.handlers
import os

def catchtheweb(url):

	#爬这个url
	req = urllib2.Request(url)
	#超时退出（万一超过这个时间还没读取到网站及退出这个爬虫）
	socket.setdefaulttimeout(10.0)
	#从这下面都是获取界面的html
	res_data = urllib2.urlopen(req)
	res = res_data.read()
	soup = BeautifulSoup(res, 'lxml')
	src = soup.select('body script')[2].string
	src_text = js2xml.parse(src,  debug=False)
	src_tree = js2xml.pretty_print(src_text)
	selector = etree.HTML(src_tree)
	#到这一步已经把界面的html获取了，而且变为了可读形式
	#这里是解析读到的可读形式html
	content = selector.xpath("//property[@name = 'data']/array/array/number")
	return content
def catchtheweb1(url):

	#爬这个url
	req = urllib2.Request(url)
	#超时退出（万一超过这个时间还没读取到网站及退出这个爬虫）
	socket.setdefaulttimeout(10.0)
	#从这下面都是获取界面的html
	res_data = urllib2.urlopen(req)
	res = res_data.read()
	soup = BeautifulSoup(res, 'lxml')
	src = soup.select('body script')[3].string
	src_text = js2xml.parse(src,  debug=False)
	src_tree = js2xml.pretty_print(src_text)
	selector = etree.HTML(src_tree)
	#到这一步已经把界面的html获取了，而且变为了可读形式
	#这里是解析读到的可读形式html
	content = selector.xpath("//property[@name = 'data']/array/array/number")
	return content
def writejson(content,json_url):
	text1 = open(json_url,'w')
	text1.write('[')
	k = len(content)
	for i in xrange(len(content)):
		#这一步就把需要的数据打印了
		val_list1 = str(content[i].attrib)
		val_list2 = val_list1.replace("'", '"')
		text1.write(val_list2)
		
		if i != k-1:
			text1.write(',')
	
	text1.write(']')
	#print 12345
	text1.close()
#循环无限次
for i in range(9999999):
	module_path = '/usr/txjson/'
	LOG_FILE = module_path+'/log.log'
	handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler 
	fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s' 
	formatter = logging.Formatter(fmt)   # 实例化formatter
	handler.setFormatter(formatter)      # 为handler添加formatter
	logger1 = logging.getLogger('logging')
	
	logger1.addHandler(handler)
	logger1.setLevel(logging.INFO)
	try:
		url = "http://tongxiang.haiwensoft.com/stationchart/Temp.aspx?stationId=58456&el=TURFPVH"
		content = catchtheweb(url)
		logger1.info("obtain json_temp success")
	except:
		logger1.error("obtain json_temp error",exc_info=1)
	
	json_url = module_path+'json_temp.json'
	try:
		writejson(content,json_url)
		logger1.info('write json_temp success')
	except:
		logger1.error("write json_temp success error",exc_info=1)
	time.sleep(15)
	try:
		url1 = "http://tongxiang.haiwensoft.com/stationchart/Wind.aspx?stationId=58456&el=TURFPVH"
		content1 = catchtheweb1(url1)
		logger1.info("obtain json_wind success")
	except:
		logger1.error("obtain json_wind error",exc_info=1)
	json_url1 = module_path+'json_wind.json'
	try:
		writejson(content1,json_url1)
		logger1.info('write json_wind success')
	except:
		logger1.error("write json_wind success error",exc_info=1)
	time.sleep(15)
	try:
		url2 = "http://tongxiang.haiwensoft.com/stationchart/Rainfall.aspx?stationId=58456&el=TURFPVH"
		content2 = catchtheweb1(url2)
		logger1.info("obtain json_rainfall success")
	except:
		logger1.error("obtain json_rainfall error",exc_info=1)
	json_url2 = module_path+'json_rainfall.json'
	try:
		writejson(content2,json_url2)
		logger1.info('write json_rainfall success')
	except:
		logger1.error("write json_rainfall success error",exc_info=1)
	time.sleep(15)
	try:
		url3 = "http://tongxiang.haiwensoft.com/stationchart/Visib.aspx?stationId=58456&el=TURFPVH"
		content3 = catchtheweb(url3)
		logger1.info("obtain json_visib success")
	except:
		logger1.error("obtain json_visib error",exc_info=1)
	json_url3 = module_path+'json_visib.json'
	try:
		writejson(content3,json_url3)
		logger1.info('write json_visib success')
	except:
		logger1.error("write json_visib success error",exc_info=1)
	time.sleep(15)
	try:
		url4 = "http://tongxiang.haiwensoft.com/stationchart/Pressure.aspx?stationId=58456&el=TURFPVH"
		content4 = catchtheweb(url4)
		logger1.info("obtain json_pressure success")
	except:
		logger1.error("obtain json_pressure error",exc_info=1)
	json_url4 = module_path+'json_pressure.json'
	try:
		writejson(content4,json_url4)
		logger1.info('write json_pressure success')
	except:
		logger1.error("write json_pressure success error",exc_info=1)
	time.sleep(15)
	try:
		url5 = "http://tongxiang.haiwensoft.com/stationchart/RelHumidity.aspx?stationId=58456&el=TURFPVH"
		content5 = catchtheweb(url5)
		logger1.info("obtain json_relHumidity success")
	except:
		logger1.error("obtain json_relHumidity error",exc_info=1)
	json_url5 = module_path+'json_relHumidity.json'
	try:
		writejson(content5,json_url5)
		logger1.info('write json_relHumidity success')
	except:
		logger1.error("write json_relHumidity success error",exc_info=1)
	time.sleep(3520)






