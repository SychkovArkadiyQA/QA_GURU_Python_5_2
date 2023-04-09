import pytest
from selene import browser
from selene import be, have
@pytest.fixture
def browser_open():
    browser.open('https://google.com')
    browser.driver.maximize_window()
    yield
    print('Тест завершен')

def test_search_google_5_1(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_search_google_5_2(browser_open):
    browser.element('[name="q"]').should(be.blank).type('4578654398ghjfekghj').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print('Поиск не дал результатов')
