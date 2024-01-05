import allure
from allure_commons.types import Severity



def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="Testing")
    pass

def test_no_labels():
    pass

@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "zukhran")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com",name="Testing")
def test_decorator_labels():
    pass

