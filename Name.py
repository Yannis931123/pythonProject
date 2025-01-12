import random
import nltk
from nltk.corpus import names

# 下载nltk的names数据集（如果尚未下载）
nltk.download('names')

# 获取所有英文名
all_names = names.words()

# 过滤出长度大于5个字母的名字
long_names = [name for name in all_names if len(name) > 5]

# 随机选择5个名字
random_names = [name.capitalize() for name in random.sample(long_names, 5)]

for name in random_names:
    print(name)
