import allure
import pytest
from pytest_playwright.pytest_playwright import page
from helper.configuration_manager import ConfigurationManager
from helper.utils import *
from helper.soft_assert import soft_assert

@pytest.mark.regular_loading
@allure.story("Permissions for Regular Loading")
@allure.description("Checking Permissions for Regular Loading")
def test_verify_permissions_for_regular_loading(f, add_allure_attach, page):
   permissions = ConfigurationManager.get_permission()
   if permissions == "Senior Evaluator":
      print("Running commands for Senior Evaluator")
      #Dashboard
      f.functions.assert_element_exists(f.permissions.comp_personal_details(), "The Component - רכיב פרטים אישיים")
      f.functions.assert_element_exists(f.permissions.comp_total_evaluations_in_the_last_session(), "The Component - רכיב סהכ הערכות במועד האחרון")
      f.functions.assert_element_exists(f.permissions.comp_evaluation_status(), "The Component - סטטוס הערכות")
      # f.functions.element_exists_and_disabled_or_visible(f.permissions.comp_general_info_for_session(),"The Component - נתונים כלליים למועד")
      f.functions.assert_element_exists(f.permissions.comp_links(), "The Component - לינקים חשובים")
      f.workflow.navigation_to_loading_screen()

      #LoadingScreen
      f.functions.choose_filter_option("טעינה להערכה בכירה")
      f.functions.assert_element_exists(f.permissions.btn_loading_archive(), "The Button - מעבר לארכיון טעינות")
      f.functions.assert_element_exists(f.permissions.btn_loading_discharge(), "The Button - סיום בדיקה ושליחה למרבד")
      f.functions.table_choose_a_row(2).dblclick()

      #PortionScreen
      f.functions.assert_element_exists(f.permissions.btn_half_discharge_loading(), "The Button - פריקה חלקית")
      f.functions.assert_element_exists(f.permissions.btn_delete_all_evaluations(), "The Button - מחק כלל הערכות במנה in Portion screen")
      f.functions.assert_element_exists(f.permissions.btn_confirm_no_check(), "The Button - אשר אי בדיקה")
      f.functions.assert_element_exists(f.permissions.btn_cancel_no_check(), "The Button - בטל אי בדיקה")
      f.functions.table_choose_a_row(2).dblclick()

      #NotebookScreen
      f.functions.popup_answer_law()
      f.functions.assert_element_exists(f.permissions.btn_delete_notebook_evaluation(), "The Button - מחק בדיקת מחברת in Notebook Page")
      f.functions.assert_element_exists(f.permissions.btn_end_notebook_evaluation(), "The Button - סיים בדיקת מנה")
      f.functions.table_choose_a_row(2).dblclick()

      #CheckNotebookScreen
      f.functions.assert_element_exists(f.permissions.btn_delete_notebook_evaluation_check_notebook(), "The Button - מחק בדיקת מחברת in CheckNotebook Page")
      f.functions.assert_element_exists(f.permissions.btn_student_adaptations(), "The Button - התאמות לתלמיד")
      f.functions.assert_element_exists(f.permissions.btn_show_formats(), "The Button - הצג פורמטים")
      f.functions.assert_element_exists(f.permissions.btn_uncheck_notebook(), "The Button - אי בדיקת מחברת")
      f.functions.assert_element_exists(f.permissions.btn_suspicious_notebook(), "The Button - מחברת חשודה")
      f.functions.assert_element_exists(f.permissions.btn_save_and_end_notebook_test(), "The Button - שמור וסיים בדיקת מחברת")
      f.functions.assert_element_exists(f.permissions.btn_save_question_score(), "The Button - שמור - in Grade Component")

      soft_assert.assert_all()

   elif permissions == "Regular Evaluator":
      print("Running commands for Regular Evaluator")
      #Dashboard
      f.functions.assert_element_exists(f.permissions.comp_personal_details(), "The Component - רכיב פרטים אישיים")
      f.functions.assert_element_exists(f.permissions.comp_total_evaluations_in_the_last_session(), "The Component - רכיב סהכ הערכות במועד האחרון")
      f.functions.assert_element_exists(f.permissions.comp_evaluation_status(), "The Component - סטטוס הערכות")
      # f.functions.assert_element_exists(f.permissions.comp_general_info_for_session(),"The Component - נתונים כלליים למועד")
      f.functions.assert_element_exists(f.permissions.comp_links(), "The Component - לינקים חשובים")
      f.workflow.navigation_to_loading_screen()

      #LoadingScreen
      f.functions.choose_filter_option("טעינה להערכה")
      f.functions.assert_element_exists(f.permissions.btn_loading_archive(), "The Button - מעבר לארכיון טעינות")
      f.functions.assert_element_exists(f.permissions.btn_loading_discharge(), "The Button - סיום בדיקה ושליחה למרבד")
      f.functions.table_choose_a_row(2).dblclick()

      #PortionScreen
      f.functions.assert_element_exists(f.permissions.btn_half_discharge_loading(), "The Button - פריקה חלקית")
      f.functions.assert_element_exists(f.permissions.btn_delete_all_evaluations(), "The Button - מחק כלל הערכות במנה in Portion screen")
      f.functions.assert_element_exists(f.permissions.btn_confirm_no_check(), "The Button - אשר אי בדיקה")
      f.functions.assert_element_exists(f.permissions.btn_cancel_no_check(), "The Button - בטל אי בדיקה")
      f.functions.table_choose_a_row(2).dblclick()

      #NotebookScreen
      f.functions.popup_answer_law()
      f.functions.assert_element_exists(f.permissions.btn_delete_notebook_evaluation(), "The Button - מחק בדיקת מחברת in Notebook Page")
      f.functions.assert_element_exists(f.permissions.btn_end_notebook_evaluation(), "The Button - סיים בדיקת מנה")
      f.functions.table_choose_a_row(2).dblclick()

      #CheckNotebookScreen
      f.functions.assert_element_exists(f.permissions.btn_delete_notebook_evaluation_check_notebook(), "The Button - מחק בדיקת מחברת in CheckNotebook Page")
      f.functions.assert_element_exists(f.permissions.btn_student_adaptations(), "The Button - התאמות לתלמיד")
      f.functions.assert_element_exists(f.permissions.btn_show_formats(), "The Button - הצג פורמטים")
      f.functions.assert_element_exists(f.permissions.btn_uncheck_notebook(), "The Button - אי בדיקת מחברת")
      f.functions.assert_element_exists(f.permissions.btn_suspicious_notebook(), "The Button - מחברת חשודה")
      f.functions.assert_element_exists(f.permissions.btn_save_and_end_notebook_test(), "The Button - שמור וסיים בדיקת מחברת")
      f.functions.assert_element_exists(f.permissions.btn_save_question_score(), "The Button - שמור - in Grade Component")

      soft_assert.assert_all()