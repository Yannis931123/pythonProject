"""
scope = “module”：与class相同，只从.py文件开始引用fixture的位置生效
"""
import pytest

# fixture scope = 'module'
@pytest.fixture(scope='module')
def login():
    print("fixture范围为module")

def test_01():
    print("用例01")

def test_02(login):
    print("用例02")

class TestLogin():
    def test_1(self):
        print("用例1")

    def test_2(self):
        print("用例2")

    def test_3(self):
        print("用例3")


if __name__ == '__main__':
    pytest.main()