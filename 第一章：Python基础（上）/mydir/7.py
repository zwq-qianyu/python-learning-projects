#定义一个计算指定数值累加的函数
def sum(m):
    '''
    这是一个计算指定数值的累加函数
    参数一个，int类型，表示要累加的数值
    返回值是一个累加结果 int类型
    '''
    total=0
    for i in range(0,m+1):
        total+=i
    #print(total) #直接输出结果
    return total #返回结果

a = sum(10)
print("sum of 10: ",a)

print("sum of 50: ",sum(50))
print("sum of 100: ",sum(100))
help(sum)
