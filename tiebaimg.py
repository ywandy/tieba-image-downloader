#!/usr/bin/python
#encoding:utf-8
import re
import urllib
import os


def geturl():
	urlinput = raw_input("你希望下载的贴吧地址:\n")
	return urlinput

def getpath():
	path = raw_input("你希望保存在当前目录的文件夹名，请输入一个不同于当前目录的文件夹名:\n")
        ispathexist = os.path.exists("./%s" % path)
	if not ispathexist:
		os.mkdir("./%s" % path)
	return path

def aboutme():
	print '百度贴吧一键下载所有图片工具\n该工具来源，由yyw开发'

def gethtmlpage(tiebaurl):
	print '正在解析网址\n %s' % tiebaurl
	webpage = urllib.urlopen(tiebaurl)
	html = webpage.read()
	return html

def downimg(htmldate,dirpath):
	reg = r'src="(.*\.jpg)" pic_ext'
	imgre = re.compile(reg)
	imgdownlist = re.findall(imgre,htmldate)
	x = 0
	for i in imgdownlist:
		urllib.urlretrieve(i, './%s/%d.jpg' %(dirpath,x))
		print '已经下载 %d.jpg  保存在当前目录的 %s文件夹' %(x,dirpath)
		x+=1
	return '所有图片下载完成'

aboutme()
userurl = geturl()
path = getpath()
html = gethtmlpage(userurl)
print downimg(html,path)


