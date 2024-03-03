import re
from playwright.sync_api import expect
from test_pw.pages.base_page import BasePage
from test_pw.tools.constants import *


class ProjectsPage(BasePage):
    def __init__(self, page):
        self.page = page
        self.all_projects = page.locator("div.card")
        super().__init__(page)

    def select_nth_project(self, number):
        self.all_projects.locator("nth=" + str(number-1)).click()
        expect(self.page).to_have_title(re.compile("Denys Neplokhov"))





