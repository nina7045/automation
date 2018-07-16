package tests;

import com.agendaonline.prop.Props;
import com.codeborne.selenide.WebDriverRunner;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import scenarios.CloseMeeting;
import scenarios.PublishMeeting;
import scenarios.StartMeeting;
import utils.BrowserInstanceInitializer;

import static com.codeborne.selenide.Selenide.open;

public class ConductedMeetingTest {
    private Props p = new Props();
    private CreateMeetingWithAgendaItemsTest createMeetingWithAgendaItemsTest = new CreateMeetingWithAgendaItemsTest();
    private CloseMeeting closeMeeting = new CloseMeeting();
    private PublishMeeting publishMeeting = new PublishMeeting();
    private StartMeeting startMeeting = new StartMeeting();
    private BrowserInstanceInitializer browser = new BrowserInstanceInitializer();

    @Test
    public void conductedMeetingTest() throws InterruptedException {

        createMeetingWithAgendaItemsTest.createMeetingWithAgendaItems();
        closeMeeting.closeMeeting();
        publishMeeting.publishMeeting();
        startMeeting.startMeeting();
    }

    @Before
    public void before()
    {
        browser.initialize(p.browser());
        WebDriverRunner.getWebDriver().manage().window().maximize();
        open(p.agendaOnlineUrl());
    }

    @After
    public void after() {
        WebDriverRunner.getWebDriver().quit();
    }
}
