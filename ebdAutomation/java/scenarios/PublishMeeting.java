package scenarios;

import com.agendaonline.prop.Props;
import pages.MyMeetingsPage;
import pages.PublishMeetingPage;
import utils.Utils;

public class PublishMeeting {
    private PublishMeetingPage publishMeetingPage = new PublishMeetingPage();
    private MyMeetingsPage myMeetingsPage = new MyMeetingsPage();
    private Utils u = new Utils();
    private Props p = new Props();

    public void publishMeeting() throws InterruptedException {
        myMeetingsPage.selectMeeting(p.meetingName() + u.getStaticId(), "");
        publishMeetingPage.getPublishMeetingButton().click();
        publishMeetingPage.getConfirmPublishMeetingPopupOkButton().click();
    }
}
