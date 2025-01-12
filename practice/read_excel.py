import warnings
import pandas as pd
from openpyxl import Workbook

# 过滤忽略特定警告
warnings.filterwarnings("ignore", message="Workbook contains no default style, apply openpyxl's default")

# 读取Excel文件
opensource_excel = pd.read_excel(r'C:\Users\xyyxs\Downloads\opensource_cve_2024.xlsx')
# 打印数据
print(opensource_excel)

# 遍历每一行
# for index, row in df.iterrows():
#     # 获取每一行的所有列的值
#     data = row.tolist()
#     print(data)
# def test_function(data):
#     pass
#
#
# for index, row in df.iterrows():
#     # 获取每一行的所有列的值
#     data = row.tolist()
#
#     # 将数据带入到自动化脚本中
#     # 这里假设你的自动化脚本有一个名为test_function的函数，它接受一个列表作为参数
#     test_function(data)
