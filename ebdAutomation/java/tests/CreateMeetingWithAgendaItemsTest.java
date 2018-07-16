package tests;

import com.agendaonline.prop.Props;
import com.codeborne.selenide.WebDriverRunner;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import scenarios.GoalExistenceVerification;
import scenarios.SignInWithCsba;
import scenarios.StartNewAgendaItem;
import scenarios.StartNewMeeting;
import utils.BrowserInstanceInitializer;
import org.apache.log4j.Logger;
import utils.Utils;

import static com.codeborne.selenide.Selenide.open;

public class CreateMeetingWithAgendaItemsTest {
    private Props p = new Props();
    private Utils u = new Utils();
    private StartNewAgendaItem startNewAgendaItems[] = new StartNewAgendaItem[p.amountOfAgendaItems()];
    private SignInWithCsba signInWithCsba = new SignInWithCsba();
    private GoalExistenceVerification goalExistenceVerification = new GoalExistenceVerification();
    private BrowserInstanceInitializer browser = new BrowserInstanceInitializer();
    private StartNewMeeting startNewMeeting = new StartNewMeeting(p.meetingName(), p.meetingStartDate(), p.openSessionStartTime(), p.closedSessionStartTime(), p.meetingLocation(), p.workflowRouteNoApprovalOption(), p.closeMeetingAttendanceGroupOption());
    final static Logger logger = Logger.getLogger(CreateMeetingWithAgendaItemsTest.class);

    @Test
    public void createMeetingWithAgendaItems() throws InterruptedException {

        signInWithCsba.signInWithCsba();

        goalExistenceVerification.goalExistenceVerification();

        initializeNewAgendaItems();

        startNewMeeting.startNewMeeting();

        for(int i = 0; i < p.amountOfAgendaItems(); i++) {
            logger.info("Creating agenda item #" + i + " without attachment");
            startNewAgendaItems[i].startNewAgendaItem();
        }

        startNewMeeting.publishMeeting();
    }

    @Test
    public void createAgendaItemsInExistingMeetingTest() throws InterruptedException {

        signInWithCsba.signInWithCsba();

        initializeAgendaItemsForExistingMeeting();

        for(int i = 0; i < p.existingMeetingAmountOfAgendaItems(); i++) {
            logger.info("Creating agenda item #" + i + " without attachment");
            startNewAgendaItems[i].startNewAgendaItem();
        }
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

    private void initializeNewAgendaItems()
    {
        for(int i = 0; i < p.amountOfAgendaItems(); i++) {
            startNewAgendaItems[i] = i < p.amountOfAgendaItems()/2 ?
                    new StartNewAgendaItem(p.agendaItemName(), p.meetingName() + u.getStaticId(), p.workflowRouteNoApprovalOption(), false, false, true, false, false, true, p.goalOption(), p.quickSummary(), true)
                    :
                    new StartNewAgendaItem(p.agendaItemName(), p.meetingName() + u.getStaticId(), p.workflowRouteNoApprovalOption(), true, true, false, false, false, false, p.goalOption(), p.quickSummary(), false);
        }
    }

    private void initializeAgendaItemsForExistingMeeting()
    {
        for(int i = 0; i < p.existingMeetingAmountOfAgendaItems(); i++) {
            startNewAgendaItems[i] = i < p.existingMeetingAmountOfAgendaItems()/2 ?
                    new StartNewAgendaItem(p.agendaItemName(), p.existingMeetingName(), p.workflowRouteNoApprovalOption(), false, false, true, false, false, true, p.goalOption(), p.quickSummary(), true)
                    :
                    new StartNewAgendaItem(p.agendaItemName(), p.existingMeetingName(), p.workflowRouteNoApprovalOption(), true, true, false, false, false, false, p.goalOption(), p.quickSummary(), false);
        }
    }

}
