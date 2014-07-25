#-*- coding: utf-8 -*
import os
import sys
import getopt
import re

def isValid(keyword,filefullname,resulttype):
	if keyword == None and resulttype == None:
		return True
	filename = os.path.splitext(filefullname)[0]
	filetype = os.path.splitext(filefullname)[1]
	if keyword == None and resulttype != None:
		if filetype == '.%s'%resulttype:
			return True
		else:
			return False
	elif keyword != None and resulttype == None:
		if keyword in filename:
			return True
		else:
			return False
	elif keyword != None and resulttype != None:
		if keyword in filename and filetype == '.%s'%resulttype:
			return True
		else:
			return False
			

def Search(keyword,filetype,dirname,regStr):
	re_search = re.compile(regStr)
	#result = open('/Users/liumiao/result.txt','w')
	totalcount = 0
	successcount = 0
	for root, dirs, fileList in os.walk(dirname):
	 	for f in fileList:
			if isValid(keyword,f,filetype):
				totalcount += 1
				filepath = os.path.join(root, f);
				with open (filepath,'r') as f:
					classname = re.findall(regStr,f.read())
					if len(classname)>0:
							#result.write(classname[0]+'\n')
						successcount += 1
						print filepath
	#result.close()
	print '%d success'%successcount
	
#   查找包含指定字符串的文件，可以指定文件名称，文件类型，查找文件夹，是否完全匹配:
#   -m 是否完全匹配 -f:文件名称 -t:文件类型名 -d:搜索文件夹路径 -k:指定字符串

RegStr = raw_input('请输入关键词:') or '.*'
Keyword =  raw_input('请输入文件名(部分或完整,回车可跳过):') or None
Type =  raw_input('请输入文件类型(回车可跳过):') or None
Dirname = raw_input('请输入搜索路径(跳过表示用户目录):') or '.'
isMatch = raw_input('是否完全匹配关键词(y/n):') or 'y'

if isMatch != 'y':
	RegStr = '(?i)'+RegStr

Search(Keyword,Type,Dirname,RegStr)

