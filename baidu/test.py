#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests,json


def saveImage(imgUrl,imgName='default.jpg'):
	response=requests.get(imgUrl,stream=True)
	image=response.content
	dst='/Users/yeshiyuan/leanpython/learnPython3/baidu/baidu_img/'
	path=dst+imgName
	print('save the file:'+path+'\n')
	with open(path,'wb') as img:
		img.write(image)
	img.close()
def run(rj):
	for line in rj['newslist']:
		title=line['title']
		picUrl=line['picUrl']
		saveImage(picUrl,imgName=title+'.jpg')


url='http://apis.baidu.com/txapi/mvtp/meinv'

headers={'apikey':'5a3416fa2be673902c50fe01188d7780'}

params={'num':'10'}

r=requests.get(url,params=params,headers=headers)

# print(r.content)

print(r.__class__)

rj=r.json()

print(rj.__class__)

run(rj)











url_1 = "http://www.tngou.net/tnfs/api/list"
# url_2 = "http://www.tngou.net/tnfs/api/classify"
src_header = "http://tnfs.tngou.net/image"
headers = {'apikey':'5a3416fa2be673902c50fe01188d7780'}
params_1 = {
    'page':3,
    'rows':20,
    'id':6      #需根据classify结果才能知道
}
r = requests.get(url_1)
r = r.json()
# 保存图片到本地路径
def saveImage(imgUrl,imgName= 'default.jpg'):
    response = requests.get(imgUrl,stream = True)
    image = response.content
    dst = "/Users/yeshiyuan/leanpython/learnPython3/baidu/baidu_img_two/"
    path = dst+imgName
    print('save the file:'+path+'\n') 
    with open(path,'wb') as img:
        img.write(image)
    img.close()
# 开始
def run():
    for line in r['tngou']:
        title = line['title']
        img = line['img']
        src_path = src_header+img
        saveImage(src_path,title+'.jpg')
run()




