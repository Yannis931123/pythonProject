import pandas as pd

# 读取Excel文件
df = pd.read_excel('your_file.xlsx', sheet_name=1)

# 遍历每一行
def test_function(data):
    pass


for index, row in df.iterrows():
    # 获取每一行的所有列的值
    data = row.tolist()

    # 将数据带入到自动化脚本中
    # 这里假设你的自动化脚本有一个名为test_function的函数，它接受一个列表作为参数
    test_function(data)
