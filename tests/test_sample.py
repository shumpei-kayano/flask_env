import pytest

def test_func1():
    assert 1 == 1
    
def test_func2():
    assert 2 == 2
    
# @pytest.fictureを追加する
# @pytest.fixture
# def app_data():
#     return 3

# フィクスチャのk数を引数で指定すると関数の実行結果が渡される
def test_func3(app_data):
    assert app_data == 3