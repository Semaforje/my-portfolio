from test_pw.pages.home_page import HomePage
from test_pw.pages.aboutme_page import AboutMePage
from test_pw.pages.projects_page import ProjectsPage
from test_pw.pages.project_details_page import ProjectDetailsPage
from playwright.sync_api import Page


def test_view_project_details(page: Page):
    test_page = HomePage(page)
    test_page.open_home_page()
    test_page.select_learn_more_button()
    test_page = AboutMePage(page)
    test_page.select_my_projects_button()
    test_page = ProjectsPage(page)
    test_page.select_nth_project(1)
    test_page = ProjectDetailsPage(page)
    test_page.select_back_to_projects_button()
    test_page = ProjectsPage(page)
    test_page.select_nth_project(2)
    test_page = ProjectDetailsPage(page)
    test_page.select_back_to_projects_button()
