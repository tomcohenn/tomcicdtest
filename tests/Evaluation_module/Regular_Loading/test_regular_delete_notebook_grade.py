import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.soft_assert import soft_assert
from helper.utils import *


@pytest.mark.regular_loading #C20694
@allure.story("Delete Notebook Grade - Regular Loading")
@allure.description("Deleting the notebook's Grade using the 'Delete Notebook Check' button")
def test_regular_delete_notebook_grade(f, add_allure_attach, page):
    f.functions.check_if_loading_number_exist(regular_loading_num, 'regular_loading_num')
    #Dashboard
    f.workflow.navigation_to_loading_screen()

    #LoadingScreen
    f.functions.search_loading(regular_loading_num)
    f.workflow.navigation_from_loading_to_check_notebook_page(2,2,2)

    #CheckNotebookScreen
    f.functions.click_delete_notebook_if_enabled()
    f.workflow.answer_one_question("1")
    f.workflow.delete_notebook_test()
    f.workflow.assert_check_notebook_score_deleted()
    f.breadcrumbs.btn_breadcrumbs_to_notebooks_page().click()

    # NotebookPage
    f.functions.popup_answer_law()
    table_notebook_grade_after = f.functions.number_to_int(f.notebookPage.txt_table_notebook_grade(2))
    f.functions.assert_equal_to(table_notebook_grade_after, 0, "The Notebook grade is incorrect")

    soft_assert.assert_all()
