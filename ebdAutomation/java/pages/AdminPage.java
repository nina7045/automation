package pages;

import com.agendaonline.prop.Props;
import com.codeborne.selenide.Condition;
import com.codeborne.selenide.ElementsCollection;
import com.codeborne.selenide.SelenideElement;
import org.openqa.selenium.Keys;
import utils.SearchItemEngine;
import utils.Utils;
import utils.Wait;

import static com.codeborne.selenide.Selenide.$;
import static com.codeborne.selenide.Selenide.$$;

public class AdminPage {
    private Wait wait = new Wait();
    private ElementsCollection sections = $$("li.style-scope.admin-list a");

    public SelenideElement getOpenGoalsButton() throws InterruptedException {
        wait.waitForComplexElement(sections.get(0));
        return sections.find(Condition.text("Open Goals Page"));
    }

    public SelenideElement getWorkflowRoutesButton() throws InterruptedException {
        wait.waitForElement(sections.get(0));
        wait.waitForPageLoadingSpinner();
        return sections.find(Condition.text("Open Workflow Routes Page"));
    }

    public static class GoalsPage {
        private Wait wait = new Wait();
        private SelenideElement amountOfGoalItems = $(".total-items");
        private SelenideElement goalNameField = $$("awi-textbox#goalName input").get(1);
        private SelenideElement goalDescriptionField = $$("textarea#textarea.style-scope.iron-autogrow-textarea").get(1);
        private SelenideElement goalTypeField = $(".add-goal-modal.awi-combobox-0 input");
        private SelenideElement addGoalButton = $(".grid-button.accent");
        private SelenideElement saveGoalButton = $(".accent.style-scope.add-goal-modal");

        public boolean isAnyGoalExists()
        {
            int amount = Integer.parseInt(amountOfGoalItems.getText().replaceAll("\\D+",""));
            return amount == 0;
        }

        public void createNewGoal(String goalName, String description, String goalType) throws InterruptedException {
            addGoalButton.click();
            wait.waitForElement(goalNameField);
            goalNameField.append(goalName);
            goalDescriptionField.append(description);
            goalTypeField.append(goalType + Keys.ARROW_DOWN + Keys.ENTER);
            saveGoalButton.click();
        }
    }

    public static class WorkflowRoutesPage {
        private SelenideElement addButton = $(".grid-button.accent.paper-button-0");
        private SelenideElement governingBodyField = $("awi-combobox#userTeamsCombobox input");
        private SelenideElement workflowRouteNameField = $("awi-textbox#userRouteName input");
        private SelenideElement updateWorkflowRouteNameField = $("awi-textbox#updateUserRouteName input");
        private SelenideElement approversField = $(".add-approval-route-modal vaadin-combo-box#usersCombobox input");
        private SelenideElement saveAddNewWorkflowRouteButton = $(".accent.add-approval-route-modal");
        private SelenideElement deleteSelectedApprovalButton = $("paper-toolbar paper-button.add-approval-route-modal");
        private SelenideElement selectedApproversCheckbox = $$("#usersGrid awi-grid-row").get(0).find("#checkboxContainer");
        private SelenideElement updateWorkflowRouteButton = $(".accent.edit-approval-route-modal");
        private Utils u = new Utils();
        private Props p = new Props();
        private SearchItemEngine searchItemEngine = new SearchItemEngine();
        private String itemPath = "iron-list#list awi-grid-row[index='";
        private SelenideElement amountOfItems = $(".item-container .total-items.style-scope.awi-grid-footer");


        public void addNewWorkflowRoute() throws InterruptedException {
            addButton.click();
            governingBodyField.val(p.governingBody());
            Thread.sleep(500);
            governingBodyField.append("" + Keys.ARROW_DOWN + Keys.ENTER);

            workflowRouteNameField.val(p.workflowRouteName() + u.getStaticId());
            Thread.sleep(2000);
            approversField.click();
            approversField.append("" + Keys.ARROW_DOWN + Keys.ENTER);
            approversField.click();
            approversField.append("" + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER);
            Thread.sleep(2000);
            selectedApproversCheckbox.click();
            deleteSelectedApprovalButton.click();

            saveAddNewWorkflowRouteButton.click();
            Thread.sleep(3000);
            searchItemEngine.selectItem(p.governingBody(),p.workflowRouteName() + u.getStaticId(), amountOfItems, itemPath, false);
            updateWorkflowRouteNameField.val(p.workflowRouteName() + u.getStaticId2());
            updateWorkflowRouteButton.click();
            searchItemEngine.selectItem(p.governingBody(),p.workflowRouteName() + u.getStaticId2(), amountOfItems, itemPath, false);

        }
    }
}
