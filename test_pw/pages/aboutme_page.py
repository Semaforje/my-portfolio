from playwright.sync_api import expect
from test_pw.pages.base_page import BasePage
from test_pw.tools.constants import *


class AboutMePage(BasePage):
    def __init__(self, page):
        self.page = page
        self.my_projects_button = page.get_by_role("link", name="My projects")
        super().__init__(page)


    def select_my_projects_button(self):
        self.my_projects_button.click()
        expect(self.page).to_have_title(PROJECTS_PAGE)




