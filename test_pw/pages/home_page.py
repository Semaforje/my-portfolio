from playwright.sync_api import expect
from test_pw.pages.base_page import BasePage
from test_pw.tools.constants import *


class HomePage(BasePage):
    def __init__(self, page):
        self.page = page
        self.learn_more_button = page.get_by_text("Learn more")
        super().__init__(page)

    def open_home_page(self):
        self.page.goto(URL)
        expect(self.page).to_have_title(HOME_PAGE)

    def select_learn_more_button(self):
        self.learn_more_button.click()
        expect(self.page).to_have_title(ABOUT_ME_PAGE)




