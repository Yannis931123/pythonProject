# pytest 会默认读取 conftest.py里面的所有 fixture
# conftest.py 文件名称是固定的，不能改动
# conftest.py 只对同一个 package 下的所有测试用例生效
# 不同目录可以有自己的 conftest.py，一个项目中可以有多个 conftest.py
# 测试用例文件中不需要手动 import conftest.py，pytest 会自动查找