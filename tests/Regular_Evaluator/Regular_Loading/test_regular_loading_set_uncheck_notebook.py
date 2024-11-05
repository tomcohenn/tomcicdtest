import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.utils import *
from helper.soft_assert import soft_assert
from pages.loading_page import LoadingPage


@pytest.mark.regular_evaluator2
@allure.story("בדיקת אי בדיקה למחברת הערכה רגילה - מעריך רגיל")
@allure.description("תהליך אי בדיקה למחברת")
def test_regular_loading_set_uncheck_notebook(f, add_allure_attach, page):
    f.functions.wait_for_networkidle()

    # Dashboard
    f.workflow.navigation_to_loading_screen()
    f.functions.search_loading(regular_loading_number_E2E_set_uncheck_notebook)

    #LoadingScreen
    f.functions.table_choose_a_row(2).click()
    stat_num_of_nocheck_portions_before = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_num_of_nocheck_portions())
    stat_num_of_nocheck_notebooks_before = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_nocheck_notebooks())
    f.functions.table_choose_a_row(2).dblclick()

    #PortionScreen
    f.functions.table_choose_a_row(2).dblclick()

    #NotebookScreen
    f.functions.popup_answer_law()
    f.functions.table_choose_a_row(2).dblclick()

    #CheckNotebookScreen
    f.workflow.flow_set_uncheck_notebook()
    f.functions.popup_answer_law()

    ######################################################################################################################################################
                                                                # Testing

    #NotebookScreen
    f.functions.table_choose_a_row(2).click()
    notebook_status = f.notebookPage.txt_table_notebook_status(2).strip()
    f.functions.assert_equal_to(notebook_status,f.workflow.uncheck_reason,"The Notebook Status is not equal to the uncheck reason")
    f.breadcrumbs.btn_breadcrumbs_to_loadings_page().click()

    #LoadingScreen
    stat_num_of_nocheck_portions_after = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_num_of_nocheck_portions())
    stat_num_of_nocheck_notebooks_after = f.functions.extracting_value_from_statistics(f.loadingPage.txt_stat_nocheck_notebooks())
    f.functions.assert_equal_to(stat_num_of_nocheck_notebooks_before+1,stat_num_of_nocheck_notebooks_after, "Statistics: Number of uncheck portions is incorrect")
    f.functions.assert_equal_to(stat_num_of_nocheck_portions_before+1,stat_num_of_nocheck_portions_after, "Statistics: Number of uncheck notebooks is incorrect")

    # f.workflow.loading_discharge_and_navigate_to_archive()
    #ArchiveScreen
    # f.functions.search_loading(regular_loading_number_E2E_set_uncheck_notebook)
    # soft_assert.check(f.functions.table_choose_a_row(2).is_visible(),"The loading didn't appear in the archives")

    soft_assert.assert_all()

