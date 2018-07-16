package scenarios;

import com.agendaonline.prop.Props;
import pages.MyMeetingsPage;
import pages.NavigationFrame;
import pages.StartMeetingPage;
import utils.Utils;

public class StartMeeting {

    private StartMeetingPage startMeetingPage = new StartMeetingPage();
    private MyMeetingsPage myMeetingsPage = new MyMeetingsPage();
    private NavigationFrame navigationFrame = new NavigationFrame();
    private Utils u = new Utils();
    private Props p = new Props();

    public void startMeeting() throws InterruptedException {
        navigationFrame.getMyMeetingsButton().click();
        myMeetingsPage.selectMeetingWithLongWait(p.meetingName() + u.getStaticId(), p.statusPublished());
        startMeetingPage.getStartMeetingButton().click();
        startMeetingPage.getConfirmPublishMeetingPopupOkButton().click();
    }
}
