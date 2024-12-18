# num1=input("input num1:")
# num2=input("input num2:")
# num3=input("input num3:")
# def getMax():
#     if(num1>num2 and num1>num3):
#         return num1
#     if (num2 > num1 and num2 > num3):
#         return num2
#     if (num3 > num1 and num3 > num2):
#         return num3
# print(getMax())

#
# def getMax():
#     # 从键盘接收三个整数
#     num1 = int(input("请输入第一个整数: "))
#     num2 = int(input("请输入第二个整数: "))
#     num3 = int(input("请输入第三个整数: "))
#
#     # 比较这三个数，返回最大值
#     max_num = max(num1, num2, num3)
#
#     return max_num
#
#
# # 调用函数并打印结果
# max_value = getMax()
# print("三个数中的最大值是:", max_value)

# sum=map(lambda x:x+1,[1,2,3,4,5])
# result=filter(lambda x:x%2,list(sum))
# print(list(result))

import click


@click.command()
@click.option('--name', prompt='请输入你的名字')
def greet(name):
    print(f"你好，{name}！")


if __name__ == '__main__':
    greet()
