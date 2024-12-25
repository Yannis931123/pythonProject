# import random
#
# # 生成100以内的5个随机正整数
# random_integers = [random.randint(1, 100) for _ in range(5)]
#
# # 由大到小排序
# sorted_integers = sorted(random_integers, reverse=True)
#
# print("生成的随机整数:", random_integers)
# print("排序后的整数:", sorted_integers)

import random

# # 生成100以内的5个随机正整数
# random_integers = [random.randint(1, 10) for _ in range(5)]
#
# # 对生成的随机整数进行排序
# sorted_integers = sorted(random_integers)
#
# # 输出结果
# print("生成的随机整数:", random_integers)
# print("排序后的整数:", sorted_integers)

import random

# 生成100以内5个不重复的正整数
random_integers = random.sample(range(500000, 1000000), 9)

# 由小到大排序
sorted_integers = sorted(random_integers)

print(sorted_integers)