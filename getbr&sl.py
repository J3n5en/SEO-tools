# -*- coding:UTF-8 -*-
__author__ = 'J3n5en'
import re
import urllib2
#############################################################
#             			作者：J3n5en							#
#	用途：获取shell地址的百度权重和百度收录情况					#
#	使用说明：在同目录下放入保存shell的文本，并命名为alive.txt	#
#	注意：shell地址和密码之间只能用“ ”	，“|”,"-"分隔			#
#############################################################
def geturl(shell):
# 切割shell分离地址和密码
    shell_sed = re.split('\|| |-', shell)
    url = shell_sed[0]  #取出地址
    pwd = shell_sed[1]  #取出密码
    pwd = pwd.strip('\n')
    getseo(url,pwd)
def getseo(url,pwd):
	try:
		br = urllib2.urlopen("http://www.j3n5en.com/api/br&url="+url).read()
		# sl = urllib2.urlopen("http://www.j3n5en.com/api/br&url="+url).read()
		print (url+" "+pwd+"  百度权重："+br)
			# +"  百度收录："+sl)
		file = open('seo.txt', 'a')
		file.write(url+" "+pwd+"  百度权重："+br+"\n")
			# "  百度收录："+sl+"\n")
		file.close()
	except Exception,e:
		print url+" --------- " + str(e)
#先进行去重操作
obuff = []
for ln in open('alive.txt'):
    if ln in obuff:
        continue
    obuff.append(ln)
with open('alive_qc.txt', 'w') as handle:
    handle.writelines(obuff)
# 读取文件并取出每一行
shells = open("alive_qc.txt", "r")
for shell in shells:
    geturl(shell)
shells.close()    