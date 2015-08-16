# -*- coding:UTF-8 -*-
__author__ = 'J3n5en'
import re
import urllib2
#############################################################
#             作者：J3n5en									#
#	用途：筛选存活的shell，并进行去重操作						#
#	使用说明：在同目录下放入保存shell的文本，并命名为shell.txt	#
#	注意：shell地址和密码之间只能用“ ”	，“|”,"-"分隔			#
#############################################################

def geturl(shell):
# 切割shell分离地址和密码
    shell_sed = re.split('\|| |-', shell)
    url = shell_sed[0]  #取出地址
    pwd = shell_sed[1]  #取出密码
    checkalive(url,pwd)

def checkalive(url,pwd):
    try:
        code = urllib2.urlopen(url, timeout = 15).getcode()
        if code == 200:
            # getseo(url)
            print url
            file = open('alive.txt', 'a')
            file.write(url+" "+pwd)
            file.close()
        else:
            pass
    except Exception,e:
        print url+" --------- " + str(e)

#先进行去重操作
obuff = []
for ln in open('shell.txt'):
    if ln in obuff:
        continue
    obuff.append(ln)
with open('shell_qc.txt', 'w') as handle:
    handle.writelines(obuff)
# 读取文件并取出每一行
shells = open("shell_qc.txt", "r")
for shell in shells:
    geturl(shell)
shells.close()        