import re
from playwright.sync_api import Page, expect
from test_pw.tools.constants import *


class BasePage(Page):
    def __init__(self, page):
        self.page = page
        self.logo = page.locator("a.navbar-brand")
        self.home_link = page.locator("#home_link")
        self.about_link = page.get_by_role("link", name="About")
        self.projects_link = page.get_by_role("link", name="Projects")
        self.github_link = page.get_by_role("link", name="GitHub")
        self.linkedin_link = page.get_by_role("link", name="LinkedIn")
        self.resume_link = page.get_by_role("link", name="Resume")

    def select_logo(self):
        self.logo.click()
        expect(self.page).to_have_title(HOME_PAGE)

    def select_home_link(self):
        self.home_link.click()
        expect(self.page).to_have_title(HOME_PAGE)

    def select_about_link(self):
        self.about_link.click()
        expect(self.page).to_have_title(ABOUT_ME_PAGE)

    def select_projects_link(self):
        self.projects_link.click()
        expect(self.page).to_have_title(PROJECTS_PAGE)

    def select_github_link(self, context):
        with context.expect_page() as new_page_info:
            self.github_link.click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        expect(new_page).to_have_title(GITHUB_PAGE)


    def select_linkedin_link(self, context):
        with context.expect_page() as new_page_info:
            self.linkedin_link.click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        self.page.wait_for_timeout(120000)
        expect(new_page).to_have_title(LINKEDIN_PAGE)

    def select_resume_link(self, context):
        with context.expect_page() as new_page_info:
            self.resume_link.click()
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        expect(new_page).to_have_url(RESUME_PAGE_URL)
