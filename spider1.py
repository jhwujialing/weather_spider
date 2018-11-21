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
	result_1_h = result_1_f.split(',')
	

	number2_a = result.find("u'\u632f\u4e1c\u65b0\u516d\u4e2d\u7ad9'") #振东新六中站
	result_2 =result[number2_a:]
	number2_b = result_2.find("},")
	number2_c = result_2.find("u'airIndexLevel': {")
	result_2_f = result_2[number2_b+2:number2_c-2]
	result_2_h = result_2_f.split(',')

	number3_a = result.find("u'\u679c\u56ed\u6865\u6c34\u5382'") #果园桥水厂
	result_3 =result[number3_a:]
	number3_b = result_3.find("},")
	number3_c = result_3.find("u'airIndexLevel': {")
	result_3_f = result_3[number3_b+2:number3_c-2]
	result_3_h = result_3_f.split(',')
	
	result_total = [{'name':'乌镇','value':result_1_h},{'name':'振东新六中站','value':result_2_h},{'name':'果园桥水厂','value':result_3_h}]
	print resp
	return result_total
for kk in range(9999999):
	module_path = '/usr/txjson/'
	#module_path = 'F:/tongxiang_spider/'
	json_url = module_path+'json_aqi.json'
	text1 = open(json_url,'w')
	result_total = spider1()
	data_json = json.dumps(result_total,ensure_ascii=False)
	text1.write(data_json)
	text1.close()
	time.sleep(900)