from test_pw.pages.home_page import HomePage
from playwright.sync_api import Page, BrowserContext


def test_navbar_logo_link(page: Page):
    page = HomePage(page)
    page.open_home_page()
    page.select_logo()


def test_navbar_home_link(page: Page):
    page = HomePage(page)
    page.open_home_page()
    page.select_home_link()


def test_navbar_about_link(page: Page):
    page = HomePage(page)
    page.open_home_page()
    page.select_about_link()


def test_navbar_projects_link(page: Page):
    page = HomePage(page)
    page.open_home_page()
    page.select_projects_link()


def test_navbar_github_link(page: Page, context: BrowserContext):   # context fixture is used to handle new tabs
    page = HomePage(page)
    page.open_home_page()
    page.select_github_link(context)


def test_navbar_linkedin_link(page: Page, context: BrowserContext):
    page = HomePage(page)
    page.open_home_page()
    page.select_linkedin_link(context)


# TODO Check how to verify that the PDF is opened in new tab
# def test_navbar_resume_link(page: Page, context: BrowserContext):
#     page = HomePage(page)
#     page.open_home_page()
#     page.select_resume_link(context)