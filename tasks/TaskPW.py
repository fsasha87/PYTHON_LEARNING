# 1\ pCLI: pip install pytest-playwright => playwright install
# 2\ from playwright.sync_api import Page, expect
# def_test_1(page:Page): page.goto(url)    page.locator("").click()  expect(page.locator(""))).to_be_visible() assert (locator).inner_text()==
# 3\ pytest.ini:   [pytest]    addopts = --headed --slowmo 300
# 4\ conftest.py:  @pytest.fixture(scope="function"/"session", autouse=True) def foo(page): print("A") yield  print('B')
# 5\ from psa import sync_playwright  @pytest.fixture def setup(): with (sync_playwright() as pw): br = pw.chromium.launch(headless=False)
# c = br.new_context(viewport={"width": 1920, "height": 1080})  page = c.new_page()  page.goto("...")  yield page  c.close()  br.close()
# 6\ def test_01(setup): page = setup  page.locator("").click()  expect(page).to_have_title("")  expect(page.locator("")).to_be_visible()


from playwright.sync_api import Page, expect
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='function', autouse=True)
def before_func():
    print("Before")
    yield
    print("\nAfter")


@pytest.fixture(scope='session', autouse=True)
def before_session():
    print("Before session")
    yield
    print("After session")


@pytest.fixture(scope='function')
def setup_function():
    with (sync_playwright() as playwright_instance):
        browser = playwright_instance.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        page.goto("https://www.wikipedia.org")
        yield page
        context.close()
        browser.close()


def test_01(setup_function):
    page = setup_function
    page.locator("a#js-link-box-en").click()
    expect(page).to_have_title("Wikipedia, the free encyclopedia")
    page.locator("//input[@type='search']").fill("Ukraine")
    page.locator("//button[text()='Search']").click()
    expect(page.locator("//div[@class='fn org country-name']")).to_be_visible()
    assert (page.locator("//div[@class='fn org country-name']").inner_text() == "Ukraine")



#  PO: 1\ BasePage: init(self,page)
#  2\ HomePage: init(self, page:Page): super().__init__(page)  self.btn=page.locator("")
#  3\ def_check_title(self):expect(self.page).to_have_title("")  return self
#  4\ def_check_btn(self):expect(self.btn).to_be_visible()  return self
#  5\ def_click(self): self.btn.click() return OtherPage(self.page)
#  6\ @pytest.fixture() def setup:...
#  7\ def_test1(setup):  page=setup  HomePage(page).check_title().check_btn().click_btn()


class BasePage:
    def __init__(self,  page):
        self.page = page


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.eng_lang_link = page.locator("a#js-link-box-en")

    def click_eng_lang(self):
        self.eng_lang_link.click()
        return MainPage(self.page)


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.search_field = page.locator("//input[@type='search']")
        self.search_btn = page.locator("//button[text()='Search']")

    def enter_to_search_field(self):
        self.search_field.fill("Ukraine")
        self.search_btn.click()
        return UkrainePage(self.page)

    def check_title(self):
        expect(self.page).to_have_title("Wikipedia, the free encyclopedia")
        return self

    def is_search_field_visible(self):
        expect(self.search_field).to_be_visible()
        return self


class UkrainePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.country_name = page.locator("//div[@class='fn org country-name']")

    def is_country_name_visible(self):
        expect(self.country_name).to_be_visible()
        return self

    def check_country_name(self):
        return self.country_name.inner_text()


def test02(setup_function):
    page = setup_function
    country = (HomePage(page)
               .click_eng_lang()
               .check_title()
               .is_search_field_visible()
               .enter_to_search_field()
               .is_country_name_visible()
               .check_country_name())
    assert country == "Ukraine"


#  pip install requests  import requests def_test1():resp=requests.get(url)  print(response.json()) assert resp.status_code==200
import requests


def test_get_request():
    url = "https://greencity.greencity.cx.ua/languages/codes"

    headers = {
        'accept': '*/*',
        'Content-Type': 'application/json'
    }

    # response = requests.get(url=url, headers=headers)
    response = requests.get(url)
    print(response.json())  # response body
    print(response.status_code)
    assert response.status_code == 200

# import logging logging.basicConfig(filename='app.log', filemode='w', format='[%(asctime)s]-%(levelname)s-%(filename)s-[LINE:%(lineno)s]-%(message)s', level=logging.INFO)  logging.info("smth print")
import logging
logging.basicConfig(filename='app.log', filemode='w', format='[%(asctime)s]-%(levelname)s-%(filename)s-[LINE:%(lineno)s]-%(message)s', level=logging.INFO)
logging.info("smth print")
