"""
方法：
parametrize(argnames, argvalues, indirect=False, ids=None, scope=None)
常用参数：
argnames：参数名
argvalues：参数对应值，类型必须为list

Tips:
如果只有一个参数，里面则是值的列表如：@pytest.mark.parametrize(“username”, [“yy”, “yy2”, “yy3”])
如果有多个参数例，则需要用元组来存放值，一个元组对应一组参数的值，如：@pytest.mark.parametrize(“name,pwd”, [(“yy1”, “123”), (“yy2”, “123”), (“yy3”, “123”)])
当参数个数大于一个时，格式为:[(param_value1,param_value2…),(param_value1,param_value2…)]
使用方法:
@pytest.mark.parametrize(argnames,argvalues)
️ 参数值为N个，测试方法就会运行N次
"""
import pytest


class Test_ABC:
    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    @pytest.mark.parametrize("a,b", [(1, 2), (0, 3), (3, 0), (1, 2)])  # 参数a,b均被赋予两个值，函数会运行两遍
    def test_a(self, a, b):  # 参数必须和parametrize里面的参数一致
        print("test data:a=%d,b=%d" % (a, b))
        assert a + b == 3
