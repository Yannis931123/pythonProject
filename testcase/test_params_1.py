"""
fixtrue的params和ids的使用
"""
import pytest

@pytest.fixture(params=[1, 2,{'a':'1','b':'2'},(4,5,5)],ids=['one','two','three','four'])
def demo(request): # request是固定写法
    return request.param

def test_demo(demo):
    print("{}".format(demo))
