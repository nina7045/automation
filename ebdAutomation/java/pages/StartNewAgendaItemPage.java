package pages;

import com.codeborne.selenide.Condition;
import com.codeborne.selenide.ElementsCollection;
import com.codeborne.selenide.SelenideElement;
import com.codeborne.selenide.WebDriverRunner;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.interactions.Actions;
import utils.Utils;
import utils.Wait;

import java.security.Key;

import static com.codeborne.selenide.Selenide.$;
import static com.codeborne.selenide.Selenide.$$;

public class StartNewAgendaItemPage {
    private Utils u = new Utils();
    private Wait wait = new Wait();

    private SelenideElement agendaItemNameField = $("awi-textbox[binding='AgendaItem.ItemTitle'] input");
    private SelenideElement chooseMeetingField = $("awi-combobox[display-field='Wido.Meeting.MeetingTitle'] .flex-container input");
    private ElementsCollection chooseMeetingListOfOptions = $$("awi-combobox-item");
    private SelenideElement agendaItemWorkflowRouteField = $("awi-user-route-select .flex-container input");
    private ElementsCollection agendaItemWorkflowRouteOptions = $$("awi-combobox-item");
    private SelenideElement previewAgendaItemButton = $(".preview-button");
    private SelenideElement previewAgendaItemSaveButton = $(".accent.style-scope.awi-agenda-preview.x-scope.paper-button-0");

    private SelenideElement actionItemCheckbox = $("awi-checkbox[binding='AgendaItem.isAction']").find("paper-checkbox[aria-checked]");
    private SelenideElement consentItemCheckbox = $("awi-checkbox[binding='AgendaItem.isConsent']").find("paper-checkbox[aria-checked]");
    private SelenideElement closedOrExecutedSessionItemCheckbox = $("awi-checkbox[label='Closed/Exec Session Item']").find("paper-checkbox[aria-checked]");
    private SelenideElement proceduralItemCheckbox = $("awi-checkbox[label='Procedural Item']").find("paper-checkbox[aria-checked]");
    private SelenideElement informationalItemCheckbox = $("awi-checkbox[label='Informational Item']").find("paper-checkbox[aria-checked]");
    private SelenideElement discussionItemCheckbox = $("awi-checkbox[label='Discussion Item']").find("paper-checkbox[aria-checked]");
    private SelenideElement reasonForClosedExecSessionField = $("awi-combobox[binding='AgendaItem.ClosedSessionReasonID'] .flex-container input");
    private ElementsCollection reasonForClosedExecSessionList = $$("awi-combobox-item");

    private SelenideElement agendaItemGoalsField = $("awi-tags[binding='Goals'] .flex-container input");
    private ElementsCollection agendaItemGoalsList = $$("awi-combobox-item");

    private SelenideElement agendaItemAttachmentsAddButton = $("#addButton");
    private SelenideElement agendaItemAttachmentsPopupNameField = $("awi-textbox[binding='AttachmentName'] input");

    private SelenideElement agendaItemAttachmentsPopupUploadField = $("awi-document[binding='AttachmentDoc'] input");
    private SelenideElement agendaItemAttachmentsPopupSaveButton = $("awi-grid[binding='AgendaItem.ItemDocs']").find(".accent.style-scope.awi-grid-add-modal");
    private SelenideElement agendaItemAttachmentsPopupSaveAndAddMoreButton = $("#saveAndAdd");

    private SelenideElement addToAgendaButton = $("#actionButton0");
    private SelenideElement sendToWorkflowButton = $("#actionButton1");

    private SelenideElement sendToWorkflowNotesField = $(".dialog-content.style-scope.submit-action #textarea");
    private SelenideElement sendToWorkFlowOkButton = $(".accent.style-scope.submit-action.x-scope.paper-button-0");

    private ElementsCollection agendaPreviewItemsSrcList = $$("#scrollable items-node .panes-node-key.style-scope.items-pane");
    private ElementsCollection agendaPreviewItemsTrgtList = $$(".dialog-content.style-scope.awi-agenda-preview .flex.layout.vertical.panes-drop-container.style-scope.items-pane");
    private ElementsCollection amountOfOptionsInTheMeetingList = $$("awi-meeting-select awi-combobox-overlay awi-combobox-item");
    private SelenideElement closeMeetingListDropdown = $("awi-meeting-select iron-icon.iron-icon-3");

    /////////////////////////////////////////////////////////////////////////
    //Quick Summary Abstract
    private SelenideElement quickSummaryAbstractEditorFrame = $("awi-editor[binding='AgendaItem.Abstract'] iframe");
    private SelenideElement quickSummaryAbstractInputArea = $(".cke_editable");

    ////////////////////////////////////////////////////////////////////////

    public SelenideElement getAgendaItemNameField() throws InterruptedException {
        wait.waitForPageLoadingSpinner();
        return agendaItemNameField;
    }


    public void selectChooseMeetingOption(String option) throws InterruptedException {

        chooseMeetingField.click();
        if(amountOfOptionsInTheMeetingList.size() == 0) {
            closeMeetingListDropdown.click();
            Thread.sleep(3000);
            chooseMeetingField.click();
            Thread.sleep(500);
        }
        chooseMeetingField.append(option);
        Thread.sleep(500);
        chooseMeetingListOfOptions.find(Condition.text(option)).click();

    }

    public void selectChooseRandomMeetingOption()
    {
        chooseMeetingField.click();
        chooseMeetingListOfOptions.iterator().next().click();
    }

    public void selectAgendaItemWorkflowRouteOption(String option) throws InterruptedException {
        agendaItemWorkflowRouteField.click();
        Thread.sleep(500);
        agendaItemWorkflowRouteOptions.find(Condition.text(option)).click();
    }

    public void selectRandomAgendaItemWorkflowRouteOption()
    {
        agendaItemWorkflowRouteField.click();
        agendaItemWorkflowRouteField.append("" + Keys.ARROW_DOWN + Keys.ENTER);
    }

    public SelenideElement getPreviewAgendaItemButton() {
        return previewAgendaItemButton;
    }

    public SelenideElement getPreviewAgendaItemSaveButton()
    {
        return previewAgendaItemSaveButton;
    }

    public SelenideElement getActionItemCheckbox() {
        return actionItemCheckbox;
    }

    public SelenideElement getConsentItemCheckbox() {
        return consentItemCheckbox;
    }

    public SelenideElement getClosedOrExecutedSessionItemCheckbox() {
        return closedOrExecutedSessionItemCheckbox;
    }

    public void selectReasonForClosedExecSessionOption(String option)
    {
        reasonForClosedExecSessionField.click();
        reasonForClosedExecSessionList.find(Condition.text(option)).click();
    }

    public SelenideElement getProceduralItemCheckbox() {
        return proceduralItemCheckbox;
    }

    public SelenideElement getInformationalItemCheckbox() {
        return informationalItemCheckbox;
    }

    public SelenideElement getDiscussionItemCheckbox() {
        return discussionItemCheckbox;
    }

    public void selectAgendaItemGoalsOption(String option)
    {
        agendaItemGoalsField.click();
        agendaItemGoalsList.find(Condition.text(option)).click();
    }

    public void selectRandomAgendaItemGoalsOption()
    {
        agendaItemGoalsField.click();
        agendaItemGoalsField.append("" + Keys.ARROW_DOWN + Keys.ENTER);
    }

    public SelenideElement getQuickSummaryAbstractEditorFrame() {
        return quickSummaryAbstractEditorFrame;
    }

    public SelenideElement getQuickSummaryAbstractInputArea() {
        return quickSummaryAbstractInputArea;
    }

    public SelenideElement getAgendaItemAttachmentsAddButton() {
        return agendaItemAttachmentsAddButton;
    }

    public SelenideElement getAgendaItemAttachmentsPopupNameField() {
        return agendaItemAttachmentsPopupNameField;
    }

    public SelenideElement getAgendaItemAttachmentsPopupUploadField() {
        return agendaItemAttachmentsPopupUploadField;
    }

    public SelenideElement getAgendaItemAttachmentsPopupSaveButton() throws InterruptedException {
        wait.waitForPageLoadingSpinner();
        return agendaItemAttachmentsPopupSaveButton;
    }

    public SelenideElement getSendToWorkflowButton()
    {
        wait.waitForElement(sendToWorkflowButton);
        return sendToWorkflowButton;
    }

    public SelenideElement getSendToWorkflowNotesField() {
        wait.waitForElement(sendToWorkflowNotesField);
        return sendToWorkflowNotesField;
    }

    public SelenideElement getSendToWorkFlowOkButton() {
        return sendToWorkFlowOkButton;
    }

    public SelenideElement getAgendaItemAttachmentsPopupSaveAndAddMoreButton() throws InterruptedException {
        wait.waitForPageLoadingSpinner();
        return agendaItemAttachmentsPopupSaveAndAddMoreButton;
    }

    public SelenideElement getAddToAgendaButton() {
        if(addToAgendaButton.getText().equalsIgnoreCase("add to agenda"))
            return addToAgendaButton;
        if(sendToWorkflowButton.getText().equalsIgnoreCase("add to agenda"))
            return sendToWorkflowButton;
        return null;
    }
}


