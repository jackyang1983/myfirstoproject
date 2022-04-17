import pytest

# #测试类模块的fixture装饰器，每个测试模块运行一次
# @pytest.fixture(scope='module',autouse=False)
# def module_fixture():
#     print('\n这是测试模块的前置操作')
#     yield
#     print('\n这是测试模块的后置操作')
#
# #测试类级别的fixture装饰器，每个测试类运行一次
# @pytest.fixture(scope='class',autouse=False)
# def class_fixture():
#     print('\n这是测试类的前置操作')
#     yield
#     print('\n这是测试类的后置操作')

#测试方法级别的fixture装饰器，每个测试方法运行一次
@pytest.fixture(scope='function',autouse=False)
def all_fixture():
    print('\n这是全局的前置操作')
    yield
    print('\n这是全局的后置操作')
