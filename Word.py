import random
import nltk
from nltk.corpus import words

# 下载nltk的words数据集（如果尚未下载）
# nltk.download('words')

# 获取所有单词
all_words = words.words()

# 过滤出8个字母以上的单词
long_words = [word for word in all_words if len(word) >= 10]

# 随机选择一个单词
random_word = random.choice(long_words).capitalize()

print(random_word)