import uuid

# 生成一个随机的UUID
unique_id = uuid.uuid4()

# 打印UUID（默认格式）
print("生成的UUID是:", unique_id)

# 打印UUID的字符串表示
print("UUID的字符串表示是:", str(unique_id))

# 打印UUID的十六进制表示
print("UUID的十六进制表示是:", unique_id.hex)