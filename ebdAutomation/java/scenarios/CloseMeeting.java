package scenarios;

import com.agendaonline.prop.Props;
import com.codeborne.selenide.WebDriverRunner;
import pages.MeetingInDevelopmentPage;
import pages.MyMeetingsPage;
import pages.MyTasksPage;
import pages.NavigationFrame;
import utils.Utils;

public class CloseMeeting {
    private NavigationFrame navigationFrame = new NavigationFrame();
    private MyMeetingsPage myMeetingsPage = new MyMeetingsPage();
    private MeetingInDevelopmentPage meetingInDevelopmentPage = new MeetingInDevelopmentPage();
    private MyTasksPage myTasksPage = new MyTasksPage();

    private Props p = new Props();
    private Utils u = new Utils();

    public void closeMeeting() throws InterruptedException {

        navigationFrame.getMyMeetingsButton().click();
        myMeetingsPage.selectMeeting(p.meetingName() + u.getStaticId(), p.statusInDevelopment());
        Thread.sleep(5000);
        meetingInDevelopmentPage.selectAttendanceGroup(p.closeMeetingAttendanceGroupOption());
        myTasksPage.getCloseMeetingButton().click();
        myTasksPage.getConfirmPublishMeetingPopupOkButton().click();
        navigationFrame.getMyMeetingsButton().click();
    }

}
