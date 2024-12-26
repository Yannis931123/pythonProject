"""
**当测试类内的每一个测试方法都调用了fixture，fixture只在该class下所有测试用例执行前执行一次
**测试类下面只有一些测试方法使用了fixture函数名，这样的话，fixture只在该class下第一个使用fixture函数的测试用例位置开始算，后面所有的测试用例执行前只执行一次。而该位置之前的测试用例就不管。
"""
import pytest


# fixture作用域 scope = 'class'
@pytest.fixture(scope='class')
def login():
    print("scope为class")


class TestLogin:
    def test_1(self, login):
        print("用例1")

    def test_2(self, login):
        print("用例2")

    def test_3(self, login):
        print("用例3")


if __name__ == '__main__':
    pytest.main()