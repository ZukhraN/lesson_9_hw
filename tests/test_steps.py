import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s



def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")
        browser.driver.maximize_window()

    with allure.step("Ищем репозиторий"):
        s(".search-input-container").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем issues-tab"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие issue с номером 76"):
        s(by.partial_text("#76")).should(be.visible)


def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    check_issue_76("#76")

@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")
    browser.driver.maximize_window()


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".search-input-container").click()
    s("#query-builder-test").send_keys(repo)
    s("#query-builder-test").submit()

@allure.step("Переходим по ссылке репозитория")
def go_to_repository(repo):
    s(by.link_text(repo)).click()

@allure.step("Открываем issues-tab")
def open_issue_tab():
    s("#issues-tab").click()

@allure.step("Проверяем наличие issue с номером 76")
def check_issue_76(number):
    s(by.partial_text(number)).should(be.visible)