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
			

def Search(keyword,filetype,dirname):
	re_search = re.compile(r'.*? : BaseViewController')
	result = open('/Users/liumiao/result.txt','w')
	totalcount = 0
	successcount = 0
	for root, dirs, fileList in os.walk(dirname):
	 	for f in fileList:
			if isValid(keyword,f,filetype):
				totalcount += 1
				filepath = os.path.join(root, f);
				print filepath
				with open (filepath,'r') as f:
					for line in f.readlines(): 
						classname = re.match(r'@interface (.*?)\s?:\s?BaseViewController',line)
						if classname:
							result.write(classname.group(1)+'\n')
							successcount += 1
	result.close()
	print '%d success'%successcount
	print '%d files total found cotains keyword %s of type %s in %s'%(totalcount,keyword,filetype,dirname)



opts, args = getopt.getopt(sys.argv[1:], "hk:t:d:")

Keyword =  None
Type =  None
Dirname = '.'
for op, value in opts:
    if op == "-k":
        Keyword = value
    elif op == "-t":
        Type = value
    elif op == "-d":
        Dirname = value
    elif op == "-h":
    	sys.exit()

Search(Keyword,Type,Dirname)

