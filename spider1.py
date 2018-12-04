#-*- coding:utf-8 -*-
# coding: utf-8  
# http://jgsb.agri.gov.cn/flexapps/hqApp.swf数据抓取  
#http://wms.zjemc.org.cn/wms/messagebroker/amfWms
import urllib2  
import uuid  
import pyamf  
import time
import json
from pyamf import remoting  
from pyamf.flex import messaging
import logging
import logging.handlers
def spider1():
	msg = messaging.RemotingMessage(
	messageId=str(uuid.uuid1()).upper(),  
	clientId=str(uuid.uuid1()).upper(),  
	operation='getHourlyDataForAllSites',
	destination='GisCommonDataUtil',  
	timeToLive=0,
	timestamp=0,
	body = [],
	source = None
	)
	# 第一个是查询参数，第二个是页数，第三个是控制每页显示的数量（默认每页只显示15条）  
	#msg.body = [HqPara()]
	msg.headers['DSEndpoint'] = None
	msg.headers['DSId'] = str(uuid.uuid1()).upper()  
	# 按AMF协议编码数据  
	req = remoting.Request('null', body=(msg,))
	env = remoting.Envelope(amfVersion=pyamf.AMF3)
	env.bodies = [('/1', req)]  
	data = bytes(remoting.encode(env).read())  
	# 提交请求  
	
	#url = 'http://wms.zjemc.org.cn/wms/messagebroker/amfWms'  
	url = 'http://aqi.zjemc.org.cn/aqi/messagebroker/amf'  
	req = urllib2.Request(url, data, headers={'Content-Type': 'application/x-amf'})  
	# 解析返回数据  
	opener = urllib2.build_opener()  
	
	# 解码AMF协议返回的数据  
	resp = remoting.decode(opener.open(req).read())
	result = str(resp.bodies)
	#print result
	number1_a = result.find("u'\u4e4c\u9547'") #乌镇
	result_1 =result[number1_a:]
	number1_b = result_1.find("},")
	number1_c = result_1.find("u'airIndexLevel': {")
	result_1_f = result_1[number1_b+2:number1_c-2]
	result_1_i = result[:number1_a]
	number1_d = result_1_i.rfind("u'avgHour1O3'")
	number1_f = result_1_i.rfind("u'avgHour24SliderPm25'")
	result_1_j = result_1_i[number1_d:number1_f-1]
	result_1_k = result_1_j+result_1_f
	result_1_h = result_1_k.split(',')


	number2_a = result.find("u'\u632f\u4e1c\u65b0\u516d\u4e2d\u7ad9'") #振东新六中站
	result_2 =result[number2_a:]
	number2_b = result_2.find("},")
	number2_c = result_2.find("u'airIndexLevel': {")
	result_2_f = result_2[number2_b+2:number2_c-2]
	result_2_i = result[:number2_a]
	number2_d = result_2_i.rfind("u'avgHour1O3'")
	number2_f = result_2_i.rfind("u'avgHour24SliderPm25'")
	result_2_j = result_2_i[number2_d:number2_f-1]
	result_2_k = result_2_j+result_2_f
	result_2_h = result_2_k.split(',')

	number3_a = result.find("u'\u679c\u56ed\u6865\u6c34\u5382'") #果园桥水厂
	result_3 =result[number3_a:]
	number3_b = result_3.find("},")
	number3_c = result_3.find("u'airIndexLevel': {")
	result_3_f = result_3[number3_b+2:number3_c-2]
	result_3_i = result[:number3_a]
	number3_d = result_3_i.rfind("u'avgHour1O3'")
	number3_f = result_3_i.rfind("u'avgHour24SliderPm25'")
	result_3_j = result_3_i[number3_d:number3_f-1]
	result_3_k = result_3_j+result_3_f
	result_3_h = result_3_k.split(',')
	
	result_total = [{'name':'乌镇','value':result_1_h},{'name':'振东新六中站','value':result_2_h},{'name':'果园桥水厂','value':result_3_h}]
	return result_total
for kk in range(9999999):
	module_path = '/usr/txjson/'
	#module_path = 'F:/tongxiang_spider/'
	LOG_FILE = module_path+'/spider1.log'
	handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler 
	fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s' 
	formatter = logging.Formatter(fmt)   # 实例化formatter
	handler.setFormatter(formatter)      # 为handler添加formatter
	logger = logging.getLogger('logging')
	logger.addHandler(handler)
	logger.setLevel(logging.INFO)
	json_url1 = module_path+'json_aqi1.json'
	text1 = open(json_url1,'w')
	try:
		result_total = spider1()
		logger.info('spider1没错 成功')
	except:
		logger.error('spider1有错 失败',exc_info=1)
	data_json = json.dumps(result_total,ensure_ascii=False)
	text1.write(data_json)
	text1.close()
	
	json_url1 = open(module_path+'/json_aqi1.json','r')
	lines_url = ''
	try:
		lines_url = json_url1.read().splitlines()
	except:
		logger.error('读取 失败',exc_info=1)
	json_url1.close()
	if lines_url:
		json_url = open(module_path+'/json_aqi.json','w')
		for eachline in lines_url:
			json_url.write(eachline)
			json_url.write('\n')
		json_url.close()
	time.sleep(900)
