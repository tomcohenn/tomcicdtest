import re
import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.configuration_manager import ConfigurationManager
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.regular_loading
@allure.story("Delete Notebook Grade - Senior Loading")
@allure.description("Deleting the notebook's Grade using the 'Delete Notebook Check' button")
def test_senior_delete_notebook_grade(f, add_allure_attach, page):
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(senior_loading_num)
    f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

    #CheckNotebookScreen
    f.functions.questions_numbers_finish_popup()
    f.functions.click_delete_notebook_if_enable()
    total_gap = f.checkNotebookPage.btn_senior_total_gap()
    f.functions.process_api_data(f.functions.fetch_api_data_senior)
    f.workflow.delete_notebook_test()
    total_gap_after = f.checkNotebookPage.btn_senior_total_gap()
    assert total_gap == total_gap_after


