#用for-range输出1~100，用if-or-continue跳过7的倍数、含7的数字
#7的倍速：i%7==0
#个位含7：i%10=7
#十位含7：i//10==7或0<=i-70<10
for i in range(1,101):
	if i%7==0 or i%10==7 or i//10==7:
		continue
	else:
		print(i)
