
'''
├─cdr
│  ├─cdr_audit
│  ├─ts_file
│  └─xdr
├─codelite
│  ├─dmws
│  │  └─example
│  ├─dmws_test
│  ├─taws
│  │  ├─3rd_md5
│  │  ├─3rd_xml

'''

import os
def makeResult(fileName):
	if os.isdir(fileName):
		pass

def getContent(pathName):
	#print("path name {}".format(pathName))
	if os.path.isdir(pathName):
		pathContent = os.listdir(pathName)
		pathContent = [x for x in pathContent if not x.startswith((".","~"))]
		#print("content of path:{}".format(pathContent))
		for ele in pathContent:
			getContent(os.path.join(pathName,ele))
	else:
		print(os.path.basename(pathName))

os.chdir("XC")

getContent(os.getcwd())

手上



