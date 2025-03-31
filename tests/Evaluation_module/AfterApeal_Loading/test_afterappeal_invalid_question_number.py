import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *


@pytest.mark.afterappeal_loading #C20994
@allure.story("Invalid Question number for AfterAppeal Loading")
@allure.description("Invalid Question number for AfterAppeal Loading - Expecting to get an Error")
def test_afterappeal_invalid_question_number(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(appeal_loading_num, 'appeal_loading_num')
   #Dashboard
   f.workflow.navigation_to_loading_screen()

   #LoadingScreen
   f.functions.search_loading(appeal_loading_num)
   f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

   #CheckNotebookScreen
   f.functions.click_delete_notebook_if_enabled()
   f.workflow.assert_invalid_question_number_error()
