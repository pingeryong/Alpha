# 打印九九乘法口诀表
# 变化
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}\t".format(i,j,i*j),end="")
        print()