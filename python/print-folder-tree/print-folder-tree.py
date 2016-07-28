"""
print folder tree.

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

"""
#!/usr/local/bin/py

import os
tapChar="─"
tap=4
def myPrint(fileName,tapSize=0):
	if tapSize==0:
		print(os.path.split(fileName)[1])
		return
	print("├{}{}".format(tapChar*(tapSize-tap), os.path.split(fileName)[1]))

def getContent(pathName,tapSize=0):
	#print("path name {}".format(pathName))
	if os.path.isdir(pathName):
		pathContent = os.listdir(pathName)
		pathContent = [x for x in pathContent if not x.startswith((".","~"))]
		for ele in pathContent:
			myPrint(os.path.join(pathName,ele),tapSize)
			getContent(os.path.join(pathName,ele), tapSize+tap)

targetFolder="/Users/bokix/Desktop/"
#os.chdir(targetFolder)
myPrint(targetFolder)
getContent(targetFolder,tap)




