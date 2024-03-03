from playwright.sync_api import expect
from test_pw.pages.base_page import BasePage
from test_pw.tools.constants import *


class ProjectDetailsPage(BasePage):
    def __init__(self, page):
        self.page = page
        self.back_to_projects_button = page.get_by_role("link", name="Back to projects")
        super().__init__(page)


    def select_back_to_projects_button(self):
        self.back_to_projects_button.click()


