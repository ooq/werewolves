#-*- coding:utf-8 –*-
import random
import sys

roles = ["狼人","狼人","狼人","狼人","平民","平民","平民","平民","预言家","女巫","猎人","守卫","法官"]
random.shuffle(roles)

# for role in roles:
# 	print role

for i in range(len(roles)):
	x = raw_input("按两次回车将显示" + str(i+1) + "号玩家身份")
	x = raw_input("再按一次回车将显示" + str(i+1) + "号玩家身份")
	print str(i+1) + "号玩家为:" + roles[i]
	x = raw_input(str(i+1) + "号玩家，请按回车隐藏你的身份")
	sys.stdout.write("\033[F                                          ")
	sys.stdout.write("\033[F身份已隐藏                                 \n")
	print ""

for i in range(5):
	x = raw_input("再按" + str(5-i) + "回车将显示所有人身份（法官操作）")

for i in range(len(roles)):
	print str(i+1) + "号玩家为:" + roles[i]