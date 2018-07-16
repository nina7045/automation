package scenarios;

import com.agendaonline.prop.Props;
import org.openqa.selenium.Keys;
import pages.*;
import utils.Utils;

public class StartNewMeeting {
    ////////////////////////////////////////////
    private Props p = new Props();
    private Utils u = new Utils();
    private DashboardPage dashboardPage = new DashboardPage();
    private NavigationFrame navigationFrame = new NavigationFrame();
    private StartNewPage startNewPage = new StartNewPage();
    private StartNewMeetingPage startNewMeetingPage = new StartNewMeetingPage();
    private MyTasksPage myTasksPage = new MyTasksPage();
    private MyMeetingsPage myMeetingsPage = new MyMeetingsPage();
    ////////////////////////////////////////////
    private String preliminaryInfoInputText1 = "Prelliminary text is placed here. First." + Keys.ENTER + "This should be the second line." + Keys.ENTER + "This is the third one.";
    private String preliminaryInfoInputText2 = "#" + Keys.ARROW_RIGHT + Keys.ARROW_RIGHT + "Name" + Keys.ARROW_DOWN + "1" + Keys.ARROW_RIGHT + "First";
    private String closingInfoInputText1 = "Closing information text is placed here." + Keys.ENTER + "This should be the second line." + Keys.ENTER + "This is the third one.";
    private String closingInfoInputText2 = "#" + Keys.ARROW_RIGHT + Keys.ARROW_RIGHT + "Name" + Keys.ARROW_DOWN + "1" + Keys.ARROW_RIGHT + "First";
    ////////////////////////////////////////////
    private String meetingTitle;
    private String meetingDate;
    private String openSessionBegins;
    private String closedSessionBegins;
    private String location;
    private String agendaApprovalRoute;
    private String attendanceGroup;

    public StartNewMeeting(String _meetingTitle, String _meetingDate, String _openSessionBegins, String _closedSessionBegins, String _location, String _agendaApprovalRoute, String _attendanceGroup)
    {
        meetingTitle = _meetingTitle + u.getStaticId();
        meetingDate = _meetingDate;
        openSessionBegins = _openSessionBegins;
        closedSessionBegins = _closedSessionBegins;
        location = _location;
        agendaApprovalRoute = _agendaApprovalRoute;
        attendanceGroup = _attendanceGroup;
    }

    public void startNewMeeting() throws InterruptedException {

        navigationFrame.getStartNewButton().click();
        startNewPage.getAgendaManagementList(p.agendaManagementMeetingOption()).click();
        startNewPage.getConfirmServiceRequestNextButton().click();
        startNewMeetingPage.getMeetingNameField().val(meetingTitle);
        Thread.sleep(10000);
        System.out.println(meetingTitle);
        startNewMeetingPage.getMeetingDateField().val(meetingDate);
        startNewMeetingPage.getOpenSessionBeginsField().val(openSessionBegins);
        startNewMeetingPage.getClosedSessionsBeginsField().val(closedSessionBegins);
        startNewMeetingPage.getLocationField().val(location);
        startNewMeetingPage.selectAgendaWorkflowRouteOption(p.workflowRouteNoApprovalOption());
        startNewMeetingPage.selectAttendanceGroupOption(p.closeMeetingAttendanceGroupOption());
        //////////////////////////////////////////////////////////////////////
        startNewMeetingPage.getPreliminaryInfoBulletedListButton().click();
        u.switchToFrame(startNewMeetingPage.getPreliminaryInfoEditorFrame());
        startNewMeetingPage.getPreliminaryInfoInputArea().append(preliminaryInfoInputText1);
        u.switchToDefaultContent();
        startNewMeetingPage.getPreliminaryInfoCenterTextAlignButton().click();
        startNewMeetingPage.getPreliminaryInfoRightTextAlignButton().click();
        startNewMeetingPage.getPreliminaryInfoLeftTextAlignButton().click();
        startNewMeetingPage.getPreliminaryInfoTableButton().click();
        startNewMeetingPage.getPreliminaryInfoTablePopupOkButton().click();
        u.switchToFrame(startNewMeetingPage.getPreliminaryInfoEditorFrame());
        startNewMeetingPage.getPreliminaryInfoInputArea().append(preliminaryInfoInputText2);
        u.switchToDefaultContent();
        startNewMeetingPage.getPreliminaryInfoUndoButton().click();
        startNewMeetingPage.getPreliminaryInfoRedoButton().click();
        startNewMeetingPage.getClosingInfoNumberedList().click();
        u.switchToFrame(startNewMeetingPage.getClosingInfoEditorFrame());
        startNewMeetingPage.getClosingInfoInputArea().append(closingInfoInputText1);
        u.switchToDefaultContent();
        startNewMeetingPage.getClosingInfoCenterTextAlignButton().click();
        startNewMeetingPage.getClosingInfoRightTextAlignButton().click();
        startNewMeetingPage.getClosingInfoLeftTextAlignButton().click();
        startNewMeetingPage.getClosingInfoTableButton().click();
        startNewMeetingPage.getClosingInfoTablePopupOkButton().click();
        u.switchToFrame(startNewMeetingPage.getClosingInfoEditorFrame());
        startNewMeetingPage.getClosingInfoInputArea().append(closingInfoInputText2);
        u.switchToDefaultContent();
        startNewMeetingPage.getClosingInfoUndoButton().click();
        startNewMeetingPage.getClosingInfoRedoButton().click();
        ////////////////////////////////////////////////////////////////////
        startNewMeetingPage.getOpenMeetingButton().click();
        startNewMeetingPage.getOpenMeetingPopupOkButton().click();
    }

    public void publishMeeting() throws InterruptedException {
        navigationFrame.getMyTasksButton().click();
        myTasksPage.selectMeetingTask(meetingTitle,"Meeting");
        myTasksPage.getCloseMeetingButton().click();
        myTasksPage.getConfirmPublishMeetingPopupOkButton().click();
        navigationFrame.getMyMeetingsButton().click();
    }
}
