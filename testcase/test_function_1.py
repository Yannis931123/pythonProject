"""
#场景一：做为参数传入
#函数级 每一个函数或方法都会调用
"""

import pytest


# fixture函数(类中) 作为多个参数传入
@pytest.fixture()
def login():
    print("打开浏览器")
    a = "account"
    return a

@pytest.fixture()
def logout():
    print("关闭浏览器")


class TestLogin:
    # 传入lonin fixture
    def test_001(self, login):
        print("001传入了loging fixture")
        assert login == "account"

    # 传入logout fixture
    def test_002(self, logout):
        print("002传入了logout fixture")

    def test_003(self, login, logout):
        print("003传入了两个fixture")

    def test_004(self):
        print("004未传入仍何fixture哦")


if __name__ == '__main__':
    pytest.main()

"""
从运行结果可以看出，fixture做为参数传入时，会在执行函数之前执行该fixture函数。再将值传入测试函数做为参数使用，这个场景多用于登录
"""