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

def this_is_spider(module_path):
	msg = messaging.RemotingMessage(messageId=str(uuid.uuid1()).upper(),  
		clientId=str(uuid.uuid1()).upper(),  
		operation='getAllShowHourData',
		destination='GISCommonDataUtilForWms',  
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
	url = 'http://wms.zjemc.org.cn/wms/messagebroker/amfWms'  
	req = urllib2.Request(url, data, headers={'Content-Type': 'application/x-amf'})  
	# 解析返回数据  
	opener = urllib2.build_opener()  

	# 解码AMF协议返回的数据  
	resp = remoting.decode(opener.open(req).read())
	result = str(resp.bodies)
	number1_a = result.find("u'\u8bf8\u5bb6'") #诸家
	result_1 =result[number1_a:]
	number1_b = result_1.find('}')
	result_1_f = result_1[:number1_b]
	number1_c = result_1_f.find('[')
	number1_d = result_1_f.find(']')
	result_1_g = result_1_f[number1_c+1:number1_d]
	result_1_h = result_1_g.split(',')

	number2_a = result.find("u'\u5357\u661f\u6865\u6e2f'") #南星桥港
	result_2 =result[number2_a:]
	number2_b = result_2.find('}')
	result_2_f = result_2[:number2_b]
	number2_c = result_2_f.find('[')
	number2_d = result_2_f.find(']')
	result_2_g = result_2_f[number2_c+1:number2_d]
	result_2_h = result_2_g.split(',')

	number3_a = result.find("u'\u5927\u9ebb'") #大麻
	result_3 =result[number3_a:]
	number3_b = result_3.find('}')
	result_3_f = result_3[:number3_b]
	number3_c = result_3_f.find('[')
	number3_d = result_3_f.find(']')
	result_3_g = result_3_f[number3_c+1:number3_d]
	result_3_h = result_3_g.split(',')

	number4_a = result.find("u'\u8054\u5408\u6865'") #联合桥
	result_4 =result[number4_a:]
	number4_b = result_4.find('}')
	result_4_f = result_4[:number4_b]
	number4_c = result_4_f.find('[')
	number4_d = result_4_f.find(']')
	result_4_g = result_4_f[number4_c+1:number4_d]
	result_4_h = result_4_g.split(',')

	number5_a = result.find("u'\u665a\u6751'") #晚村
	result_5 =result[number5_a:]
	number5_b = result_5.find('}')
	result_5_f = result_5[:number5_b]
	number5_c = result_5_f.find('[')
	number5_d = result_5_f.find(']')
	result_5_g = result_5_f[number5_c+1:number5_d]
	result_5_h = result_5_g.split(',')

	number6_a = result.find("u'\u4e4c\u9547'") #乌镇
	result_6 =result[number6_a:]
	number6_b = result_6.find('}')
	result_6_f = result_6[:number6_b]
	number6_c = result_6_f.find('[')
	number6_d = result_6_f.find(']')
	result_6_g = result_6_f[number6_c+1:number6_d]
	result_6_h = result_6_g.split(',')

	number7_a = result.find("u'\u4e4c\u9547\u5317'") #乌镇北
	result_7 =result[number7_a:]
	number7_b = result_7.find('}')
	result_7_f = result_7[:number7_b]
	number7_c = result_7_f.find('[')
	number7_d = result_7_f.find(']')
	result_7_g = result_7_f[number7_c+1:number7_d]
	result_7_h = result_7_g.split(',')

	number8_a = result.find("u'\u65b0\u584d\u5927\u901a'") #新塍大通
	result_8 =result[number8_a:]
	number8_b = result_8.find('}')
	result_8_f = result_8[:number8_b]
	number8_c = result_8_f.find('[')
	number8_d = result_8_f.find(']')
	result_8_g = result_8_f[number8_c+1:number8_d]
	result_8_h = result_8_g.split(',')

	number9_a = result.find("u'\u676d\u7533\u516c\u8def\u6865'") #杭申公路桥
	result_9 =result[number9_a:]
	number9_b = result_9.find('}')
	result_9_f = result_9[:number9_b]
	number9_c = result_9_f.find('[')
	number9_d = result_9_f.find(']')
	result_9_g = result_9_f[number9_c+1:number9_d]
	result_9_h = result_9_g.split(',')
	result_total = [{'name':'南星桥港','value':result_2_h},{'name':'大麻','value':result_3_h},{'name':'联合桥','value':result_4_h},{'name':'晚村','value':result_5_h},{'name':'乌镇','value':result_6_h},{'name':'乌镇北','value':result_7_h},{'name':'新塍大通','value':result_8_h},{'name':'杭申公路桥','value':result_9_h}]
	json_url1 = module_path+'json_szsj1.json'
	text1 = open(json_url1,'w')
	data_json = json.dumps(result_total,ensure_ascii=False)
	text1.write(data_json)
	text1.close()
	
for kk in range(9999999):
	module_path = '/usr/txjson/'
	#module_path = 'F:/tongxiang_spider/'
	LOG_FILE = module_path+'/spider.log'
	handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler 
	fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s' 
	formatter = logging.Formatter(fmt)   # 实例化formatter
	handler.setFormatter(formatter)      # 为handler添加formatter
	logger = logging.getLogger('logging')
	logger.addHandler(handler)
	logger.setLevel(logging.INFO)
	try:
		this_is_spider(module_path)
		logger.info('spider没错 成功')
	except:
		logger.error('spider有错 失败',exc_info=1)
	json_url2 = open(module_path+'/json_szsj1.json','r')
	lines_url = ''
	try:
		lines_url = json_url2.read().splitlines()
	except:
		logger.error('读取 失败',exc_info=1)
	json_url2.close()
	if lines_url:
		json_url = open(module_path+'/json_szsj.json','w')
		for eachline in lines_url:
			json_url.write(eachline)
			json_url.write('\n')
		json_url.close()
	time.sleep(7200)
