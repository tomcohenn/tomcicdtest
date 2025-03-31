import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.dashboard #C18163
@allure.story("E2E Test for Suspicious Loading - Approve Notebook Suspicion")
@allure.description("Approve Notebook Suspicion and Loading Discharge Process For Suspicious Notebook")
def test_suspicious_loading_end_to_end_approve(f, add_allure_attach, page):
   f.functions.check_if_loading_number_exist(suspicious_loading_num,'suspicious_loading_num')
   # Dashboard
   f.workflow.navigation_to_loading_screen()

   # LoadingScreen
   f.functions.search_loading(suspicious_loading_num)
   f.workflow.navigation_from_loading_to_check_notebook_page(2, 2, 2)

   # CheckNotebookScreen
   f.functions.click_delete_notebook_if_enabled_suspicious()
   f.workflow.notebook_suspicion_approved_process()

   ##################################################################################################################################################################################
                                                                           # Testing
   #NotebookScreen
   f.functions.popup_answer_law()
   f.functions.assert_is_checkbox_checked(f.suspiciousLoadingNotebookPage.checkbox_notebook_suspicious_approved(2), expected_checked=True)
   f.functions.assert_is_checkbox_checked(f.suspiciousLoadingNotebookPage.checkbox_notebook_suspicious_denied(2), expected_checked=False)
   f.functions.assert_equal_to(f.suspiciousLoadingNotebookPage.txt_suspicious_notebook_status(2),"מחברת נבדקה", "the Notebook status is not 'מחברת נבדקה'")
   f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()

   #PortionScreen
   f.functions.assert_equal_to(f.suspiciousLoadingPortionPage.txt_table_sus_portion_status(2),"מנה תקינה ממתינה למשיכת תפוקה","the Portion status is not 'מנה תקינה ממתינה למשיכת תפוקה'")
   table_num_of_suspicion_approved_after = f.functions.number_to_int(f.suspiciousLoadingPortionPage.txt_table_num_of_suspicion_approved(2))
   f.functions.assert_equal_to(table_num_of_suspicion_approved_after,1, "Number of Suspicion Approved Notebooks is incorrect")
   f.breadcrumbs.btn_breadcrumbs_to_loadings_page().click()

   #LoadingScreen
   stat_num_of_checked_portions_after = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_num_of_checked_portions())
   stat_num_of_unchecked_portions_after = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_num_of_unchecked_portions()))
   stat_num_of_checked_notebooks_after = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_checked_notebooks()))
   stat_num_of_unchecked_notebooks_after = f.functions.extracting_value_from_statistics((f.loadingPage.txt_stat_unchecked_notebooks()))
   stat_num_of_suspicious_notebooks_after = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_suspicious_notebooks())
   f.functions.assert_equal_to(stat_num_of_checked_portions_after,1, "Statistics: Number of checked portions is incorrect")
   f.functions.assert_equal_to(stat_num_of_unchecked_portions_after,0, "Statistics: Number of unchecked portions is incorrect")
   f.functions.assert_equal_to(stat_num_of_checked_notebooks_after,1, "Statistics: Number of checked notebooks is incorrect")
   f.functions.assert_equal_to(stat_num_of_unchecked_notebooks_after,0, "Statistics: Number of unchecked notebooks is incorrect")
   f.functions.assert_equal_to(stat_num_of_suspicious_notebooks_after,1, "Statistics: Number of Suspicious notebooks is incorrect")

   soft_assert.assert_all()



