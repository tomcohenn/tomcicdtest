import allure
import pytest
from pytest_playwright.pytest_playwright import page

from helper.soft_assert import soft_assert
from helper.utils import *


@pytest.mark.senior_loading #C22664
@allure.story("Set Suspicious Notebook Test for Senior Loading")
@allure.description("Set Suspicious Notebook Process and Loading Discharge For Senior Notebook")
def test_senior_loading_set_suspicious_notebook(f, add_allure_attach, page):
    f.functions.check_if_loading_number_exist(senior_loading_num, 'senior_loading_num')
    # Dashboard
    f.workflow.navigation_to_loading_screen()

    # LoadingScreen
    f.functions.search_loading(senior_loading_num)
    f.workflow.navigation_from_loading_to_check_notebook_page(2, 2, 2)

    #CheckNotebookScreen
    f.functions.questions_numbers_finish_popup()
    f.functions.click_delete_notebook_if_enabled()
    f.workflow.flow_set_suspicious_notebook()
    f.workflow.senior_notebook_checking_process()

    #################################################################################################################################################
                                                                #Testing
    #NotebookScreen
    f.functions.popup_answer_law()
    f.functions.assert_is_checkbox_checked(f.notebookPage.checkbox_notebook_suspicious_evaluation(2), expected_checked=True)
    f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()

    #PortionScreen
    table_num_of_notebooks_in_suspicious_after = f.functions.number_to_int(f.portionPage.txt_table_num_of_suspicious_notebooks(2))
    f.functions.assert_equal_to(table_num_of_notebooks_in_suspicious_after,1, "Number of notebooks in Suspicious is incorrect")
    f.breadcrumbs.btn_breadcrumbs_to_loadings_page().click()

    #LoadingScreen
    stat_num_of_suspicious_notebooks_after = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_suspicious_notebooks())
    f.functions.assert_equal_to(stat_num_of_suspicious_notebooks_after,1, "Statistics: Number of Suspicious notebooks is incorrect")

    soft_assert.assert_all()


