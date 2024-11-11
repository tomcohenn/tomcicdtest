import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.suspicious_loading
@pytest.mark.regular_evaluator
@allure.story("Error Handling Test for Suspicious Loading - Regular Evaluator")
@allure.description("Error Handling Checking Process")
def test_suspicious_loading_error_handling(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(suspicious_loading_error_num,'suspicious_loading_error_num')
   f.functions.wait_for_networkidle()
   f.workflow.navigation_to_loading_screen()
   f.functions.search_loading(suspicious_loading_error_num)

   f.workflow.navigation_from_loading_to_CheckNotebookPage(2,2,2)

   ###########################################################################################################################################
                                                                    # Testing

   f.workflow.assert_and_validate_popup_and_error_messages_suspicious_loading()
   soft_assert.assert_all()