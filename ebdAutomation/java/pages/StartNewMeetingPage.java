package pages;

import com.codeborne.selenide.Condition;
import com.codeborne.selenide.ElementsCollection;
import com.codeborne.selenide.SelenideElement;
import org.openqa.selenium.Keys;
import utils.Utils;
import utils.Wait;

import static com.codeborne.selenide.Selenide.$;
import static com.codeborne.selenide.Selenide.$$;

public class StartNewMeetingPage {
    private Wait wait = new Wait();

    private SelenideElement meetingNameField = $("awi-textbox[binding='Meeting.MeetingTitle'] input");
    private SelenideElement meetingDateField = $("awi-datepicker[binding='Meeting.MeetingDate'] input");
    private SelenideElement openSessionBeginsField = $("awi-time-picker[binding='Meeting.OpenSessionStartTime'] input");
    private SelenideElement closedSessionsBeginsField = $("awi-time-picker[binding='Meeting.ClosedSessionStartTime'] input");
    private SelenideElement locationField = $("awi-textbox[binding='Meeting.MeetingLocation'] input");
    private SelenideElement agendaWorkflowRouteField = $("awi-user-route-select #userRoutesCombobox");
    private ElementsCollection agendaWorkflowRouteOptions = $$("awi-combobox-item");
    private SelenideElement attendanceGroupField = $("awi-combobox[binding='Meeting.MeetingAG']");
    private ElementsCollection attendanceGroupOptions = $$("awi-combobox-item");
    private SelenideElement openMeetingButton = $("#actionButton1");
    private SelenideElement openMeetingNotesField = $(".dialog-content.style-scope.submit-action").find("#textarea");
    private SelenideElement openMeetingPopupCancelButton = $(".buttons.style-scope.submit-action").find(".style-scope.submit-action.x-scope.paper-button-0");
    private SelenideElement openMeetingPopupOkButton = $(".accent.style-scope.submit-action.x-scope.paper-button-0");

    ///////////////////////////////////////////////////////////////
    //Preliminary Information Text Editor
    private String preliminaryInformationControls = "awi-editor[binding='Meeting.AgendaHeaderText'] ";
    private SelenideElement preliminaryInformationEditorFrame = $(preliminaryInformationControls + "iframe");
    private SelenideElement preliminaryInformationBulletedListButton = $(preliminaryInformationControls + ".cke_button__bulletedlist");
    private SelenideElement preliminaryInformationCenterTextAlignButton = $(preliminaryInformationControls + ".cke_button__justifycenter");
    private SelenideElement preliminaryInformationRightTextAlignButton = $(preliminaryInformationControls + ".cke_button__justifyright");
    private SelenideElement preliminaryInformationLeftTextAlignButton = $(preliminaryInformationControls + ".cke_button__justifyleft");
    private SelenideElement preliminaryInformationTableButton = $(preliminaryInformationControls + ".cke_button__table");
    private SelenideElement preliminaryInformationUndoButton = $(preliminaryInformationControls + ".cke_button__undo");
    private SelenideElement preliminaryInformationRedoButton = $(preliminaryInformationControls + ".cke_button__redo");
    private SelenideElement preliminaryInformationInputArea = $(".cke_editable");

    ///////////////////////////////////////////////////////////////
    //Closing Information Text Editor
    private String closingInformationControls = "awi-editor[binding='Meeting.AgendaFooterText'] ";
    private SelenideElement closingInformationEditorFrame = $(closingInformationControls + "iframe");
    private SelenideElement closingInformationNumberedList = $(closingInformationControls + ".cke_button__numberedlist");
    private SelenideElement closingInformationCenterTextAlignButton = $(closingInformationControls + ".cke_button__justifycenter");
    private SelenideElement closingInformationRightTextAlignButton = $(closingInformationControls + ".cke_button__justifyright");
    private SelenideElement closingInformationLeftTextAlignButton = $(closingInformationControls + ".cke_button__justifyleft");
    private SelenideElement closingInformationTableButton = $(closingInformationControls + ".cke_button__table");
    private SelenideElement closingInformationUndoButton = $(closingInformationControls + ".cke_button__undo");
    private SelenideElement closingInformationRedoButton = $(closingInformationControls + ".cke_button__redo");
    private SelenideElement closingInformationInputArea = $(".cke_editable");

    //////////////////////////////////////////////////////////////
    private ElementsCollection tablePopupsList = $$(".cke_editor_editor_dialog");
    private SelenideElement preliminaryInformationTablePopupOkButton = tablePopupsList.get(0).find(".cke_dialog_ui_button_ok");
    private SelenideElement closingInformationTablePopupOkButton = tablePopupsList.get(1).find(".cke_dialog_ui_button_ok");;

    /////////////////////////////////////////////////////////////////

    public SelenideElement getMeetingNameField() throws InterruptedException {
        wait.waitForComplexElement(meetingNameField);
        return meetingNameField;
    }

    public SelenideElement getMeetingDateField()
    {
        return meetingDateField;
    }

    public SelenideElement getOpenSessionBeginsField() {
        return openSessionBeginsField;
    }

    public SelenideElement getClosedSessionsBeginsField() {
        return closedSessionsBeginsField;
    }

    public SelenideElement getLocationField() {
        return locationField;
    }


    public void selectAgendaWorkflowRouteOption(String option) throws InterruptedException {
        wait.waitForComplexElement(agendaWorkflowRouteField);
        agendaWorkflowRouteField.click();
        agendaWorkflowRouteOptions.find(Condition.text(option)).click();
    }

    public void selectRandomAgendaWorkflowRouteOption()
    {
        agendaWorkflowRouteField.click();
        agendaWorkflowRouteField.append("" + Keys.ARROW_DOWN).click();
    }

    public void selectAttendanceGroupOption(String option)
    {
        attendanceGroupField.click();
        attendanceGroupOptions.find(Condition.text(option));
    }

    public void selectRandomAttendanceGroupOption()
    {
        attendanceGroupField.click();
        attendanceGroupField.append("" + Keys.ARROW_DOWN + Keys.ENTER);
    }

    //////////////////////////////////////////////////////////////
    public SelenideElement getPreliminaryInfoBulletedListButton() {
        return preliminaryInformationBulletedListButton;
    }

    public SelenideElement getPreliminaryInfoEditorFrame() {
        return preliminaryInformationEditorFrame;
    }

    public SelenideElement getPreliminaryInfoInputArea()
    {
        return preliminaryInformationInputArea;
    }

    public SelenideElement getPreliminaryInfoCenterTextAlignButton() {
        return preliminaryInformationCenterTextAlignButton;
    }

    public SelenideElement getPreliminaryInfoRightTextAlignButton() {
        return preliminaryInformationRightTextAlignButton;
    }

    public SelenideElement getPreliminaryInfoLeftTextAlignButton() {
        return preliminaryInformationLeftTextAlignButton;
    }

    public SelenideElement getPreliminaryInfoTableButton(){
        return preliminaryInformationTableButton;
    }

    public SelenideElement getPreliminaryInfoTablePopupOkButton()
    {
        return preliminaryInformationTablePopupOkButton;
    }

    public SelenideElement getPreliminaryInfoUndoButton(){
        return preliminaryInformationUndoButton;
    }

    public SelenideElement getPreliminaryInfoRedoButton()
    {
        return preliminaryInformationRedoButton;
    }

    ////////////////////////////////////////////////////////////////////

    public SelenideElement getClosingInfoNumberedList()
    {
        return closingInformationNumberedList;
    }

    public SelenideElement getClosingInfoEditorFrame()
    {
        return closingInformationEditorFrame;
    }

    public SelenideElement getClosingInfoInputArea()
    {
        return closingInformationInputArea;
    }

    public SelenideElement getClosingInfoCenterTextAlignButton()
    {
        return closingInformationCenterTextAlignButton;
    }

    public SelenideElement getClosingInfoRightTextAlignButton()
    {
        return closingInformationRightTextAlignButton;
    }

    public SelenideElement getClosingInfoLeftTextAlignButton()
    {
        return closingInformationLeftTextAlignButton;
    }

    public SelenideElement getClosingInfoTableButton()
    {
        return closingInformationTableButton;
    }

    public SelenideElement getClosingInfoTablePopupOkButton()
    {
        return closingInformationTablePopupOkButton;
    }

    public SelenideElement getClosingInfoUndoButton()
    {
        return closingInformationUndoButton;
    }

    public SelenideElement getClosingInfoRedoButton()
    {
        return closingInformationRedoButton;
    }

    public SelenideElement getOpenMeetingButton() {
        return openMeetingButton;
    }

    public SelenideElement getOpenMeetingNotesField() {
        return openMeetingNotesField;
    }

    public SelenideElement getOpenMeetingPopupCancelButton() {
        return openMeetingPopupCancelButton;
    }

    public SelenideElement getOpenMeetingPopupOkButton()
    {
        return openMeetingPopupOkButton;
    }
}
