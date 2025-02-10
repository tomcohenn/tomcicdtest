import allure
import pytest
from pytest_playwright.pytest_playwright import page

from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.mismatch_loading
@allure.story("Error Handling Test for MisMatch loading")
@allure.description("Mismatch Notebook Error Handling Checking Process")
def test_mismatch_loading_error_handling(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(misMatch_loading_num,'misMatch_loading_num')
   #Dashboard
   f.workflow.navigation_to_loading_screen()

   #LoadingScreen
   f.functions.search_loading(misMatch_loading_num)
   f.workflow.navigation_from_loading_to_check_notebook_page(2, 2, 2)

   ###########################################################################################################################################
                                                                    # Testing

   f.workflow.assert_and_validate_popup_and_error_messages_mismatch_loading()
   soft_assert.assert_all()
