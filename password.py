import random
import string

# 确保每种类型都有至少一个字符
upper_case = random.choice(string.ascii_uppercase)
lower_case = random.choice(string.ascii_lowercase)
digit = random.choice(string.digits)
special_char = '_'

# 剩余的字符从所有字符中随机选择
remaining_length = 8 - 4
all_characters = string.ascii_letters + string.digits + '_'
remaining_chars = ''.join(random.choice(all_characters) for _ in range(remaining_length))

# 组合成密码
password = upper_case + lower_case + digit + special_char + remaining_chars
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

print(password)