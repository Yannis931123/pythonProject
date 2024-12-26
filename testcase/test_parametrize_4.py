"""
方法：
parametrize(argnames, argvalues, indirect=False, ids=None, scope=None)
常用参数：
argnames：参数名
argvalues：参数对应值，类型必须为list

“笛卡尔积”，多个参数化装饰器

一个函数或一个类可以装饰多个 @pytest.mark.parametrize
这种方式，最终生成的用例数是 n*m，比如上面的代码就是：参数a的数据有 3 个，参数b的数据有 2 个，所以最终的用例数有 3*2=6 条
当参数化装饰器有很多个的时候，用例数都等于 nnnn…
"""
import pytest

# 笛卡尔积，组合数据
data_1 = [1, 2, 3]
data_2 = ['a', 'b', 'c', 'd']


@pytest.mark.parametrize('a', data_1)
@pytest.mark.parametrize('b', data_2)
def test_parametrize_1(a, b):
    print(f'笛卡尔积 测试数据为 ： {a}，{b}')
