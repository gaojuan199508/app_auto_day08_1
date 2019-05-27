import allure


class Test_002:

    def test_add_png(self):
        with open("C:\\Users\\Lenovo\\Desktop\\AppAuto08\\scripts\\Snipaste_2019-05-25_17-33-34.png", "rb") as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)
