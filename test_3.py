import pytest


class Test_Demo():
    @pytest.mark.demo
    def test_demo(self):
        a = 5
        b = -1
        assert a != b
        print("标签为demo的测试⽤例")

    @pytest.mark.smoke
    def test_smoke(self):
        a = 2
        b = -1
        assert a != b
        print("标签为smoke的个测试⽤例")

    @pytest.mark.qwe
    @pytest.mark.asd
    def test_add_02(self):
        b = 1 + 2
        assert 0 == b  # 失败用例
        print("标签为qwe和asd的测试用例")
