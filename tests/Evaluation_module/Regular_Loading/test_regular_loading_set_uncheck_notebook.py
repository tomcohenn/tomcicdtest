import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert
from pages.loading_page import LoadingPage

@pytest.mark.regular_loading
@allure.story("Set Uncheck Notebook Test for Regular Loading")
@allure.description("Set Uncheck Notebook Process and Loading Discharge For Regular Notebook")
def test_regular_loading_set_uncheck_notebook(f, add_allure_attach, page):
    f.functions.check_if_loading_number_exist(regular_loading_num, 'regular_loading_num')
    # Dashboard
    f.workflow.navigation_to_loading_screen()

    # LoadingScreen
    f.functions.search_loading(regular_loading_num)
    f.workflow.navigation_from_loading_to_check_notebook_page(2, 2, 2)

    #CheckNotebookScreen
    f.functions.click_delete_notebook_if_enable()
    f.workflow.flow_set_uncheck_notebook_and_save()

    ######################################################################################################################################################
                                                                # Testing
    #NotebookScreen
    f.functions.popup_answer_law()
    notebook_status = f.notebookPage.txt_table_notebook_status(2).strip()
    f.functions.assert_equal_to(notebook_status,f.workflow.uncheck_reason,"The Notebook Status is not equal to the Uncheck reason")
    f.breadcrumbs.btn_breadcrumbs_to_portions_page().click()

    # PortionScreen
    table_num_of_checked_notebooks_after = f.functions.number_to_int(f.portionPage.txt_table_num_of_checked_notebooks(2))
    f.functions.assert_equal_to(table_num_of_checked_notebooks_after,1, "Number of checked Notebooks is incorrect")
    f.functions.assert_equal_to(f.portionPage.txt_table_portion_status(2), "מנה עם שאלון לא מתאים","the Portion status is not 'מנה עם שאלון לא מתאים'")
    f.breadcrumbs.btn_breadcrumbs_to_loadings_page().click()

    #LoadingScreen
    stat_num_of_nocheck_portions_after = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_num_of_nocheck_portions())
    stat_num_of_nocheck_notebooks_after = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_nocheck_notebooks())
    f.functions.assert_equal_to(stat_num_of_nocheck_notebooks_after,1, "Statistics: Number of uncheck portions is incorrect")
    f.functions.assert_equal_to(stat_num_of_nocheck_portions_after,1, "Statistics: Number of uncheck notebooks is incorrect")

    soft_assert.assert_all()

