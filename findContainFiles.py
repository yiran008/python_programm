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
	result = open('/Users/liumiao/result.txt','w')
	totalcount = 0
	successcount = 0
	for root, dirs, fileList in os.walk(dirname):
	 	for f in fileList:
			if isValid(keyword,f,filetype):
				totalcount += 1
				filepath = os.path.join(root, f);
				with open (filepath,'r') as f:
					for line in f.readlines(): 
						classname = re.findall(regStr,line)
						if len(classname)>0:
							result.write(classname[0]+'\n')
							successcount += 1
							print filepath
	result.close()
	print '%d success'%successcount
	
#   查找包含指定字符串的文件，可以指定文件名称，文件类型，查找文件夹，是否完全匹配:
#   -m 是否完全匹配 -f:文件名称 -t:文件类型名 -d:搜索文件夹路径 -k:指定字符串

opts, args = getopt.getopt(sys.argv[1:], "hmf:t:d:k:")

Keyword =  None
Type =  None
RegStr = '.*'
Dirname = '.'
isMatch = False
for op, value in opts:
    if op == "-f":
        Keyword = value
    elif op == "-t":
        Type = value
    elif op == "-d":
        Dirname = value
    elif op == "-k":
        RegStr = value
    elif op == "-m":
    	isMatch = True
    elif op == "-h":
    	sys.exit()

if isMatch == False:
	RegStr = '(?i)'+RegStr
Search(Keyword,Type,Dirname,RegStr)

