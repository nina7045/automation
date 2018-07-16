package scenarios;
import com.agendaonline.prop.Props;
import com.codeborne.selenide.ex.ElementNotFound;
import org.apache.log4j.Logger;
import pages.*;
import utils.Utils;

import java.io.File;

public class StartNewAgendaItem {
    ///////////////////////////////////////////////////////
    private Props p = new Props();
    private Utils u = new Utils();
    private NavigationFrame navigationFrame = new NavigationFrame();
    private StartNewPage startNewPage = new StartNewPage();
    private StartNewAgendaItemPage startNewAgendaItemPage = new StartNewAgendaItemPage();
    private MyTasksPage myTasksPage = new MyTasksPage();
    final static Logger logger = Logger.getLogger(StartNewAgendaItem.class);
    ///////////////////////////////////////////////////////
    private String agendaItemName;
    private String meetingName;
    private String workflowRoute;
    private String goalsOptions;
    private String quickSummaryData;
    private boolean actionItem;
    private boolean consentItem;
    private boolean closedExecSessionItem;
    private boolean proceduralItem;
    private boolean informationalItem;
    private boolean discussionItem;
    private boolean fileToUpload;
    ///////////////////////////////////////////////////////
    public StartNewAgendaItem(String _agendaItemName, String _meetingName, String _workflowRoute, boolean _actionItem, boolean _consentItem, boolean _closedExecSessionItem, boolean _proceduralItem, boolean _informationalItem, boolean _discussionItem,String _goalsOption, String _quickSummaryData, boolean fileToUpload)
    {
        agendaItemName = _agendaItemName + u.getId();
        meetingName = _meetingName;
        workflowRoute = _workflowRoute;
        goalsOptions = _goalsOption;
        quickSummaryData = _quickSummaryData;
        actionItem = _actionItem;
        consentItem = _consentItem;
        closedExecSessionItem = _closedExecSessionItem;
        proceduralItem = _proceduralItem;
        informationalItem = _informationalItem;
        discussionItem = _discussionItem;
        this.fileToUpload = fileToUpload;
    }
    ///////////////////////////////////////////////////////
    public void startNewAgendaItem() throws InterruptedException {
        navigationFrame.getStartNewButton().click();
        startNewPage.getStartNewTitle().getText().equals(p.startNewTitle());
        startNewPage.getAgendaManagementList(p.agendaManagementAgendaItemOption()).click();
        startNewPage.getConfirmServiceRequestTitle().getText().equals(p.confirmServiceRequestTitle());
        startNewPage.getConfirmServiceRequestNextButton().click();

        Thread.sleep(10000);

        startNewAgendaItemPage.getAgendaItemNameField().append(agendaItemName);
        System.out.println(agendaItemName);
        startNewAgendaItemPage.selectChooseMeetingOption(meetingName);
        startNewAgendaItemPage.selectAgendaItemWorkflowRouteOption(workflowRoute);
        if(actionItem) startNewAgendaItemPage.getActionItemCheckbox().click();
        if(consentItem) startNewAgendaItemPage.getConsentItemCheckbox().click();
        if(closedExecSessionItem){
            startNewAgendaItemPage.getClosedOrExecutedSessionItemCheckbox().click();
            startNewAgendaItemPage.selectReasonForClosedExecSessionOption(p.reasonForClosedExecSessionOption());
        }
        if(proceduralItem) startNewAgendaItemPage.getProceduralItemCheckbox().click();
        if(informationalItem) startNewAgendaItemPage.getInformationalItemCheckbox().click();
        if(discussionItem) startNewAgendaItemPage.getDiscussionItemCheckbox().click();
        startNewAgendaItemPage.selectRandomAgendaItemGoalsOption();


        u.switchToFrame(startNewAgendaItemPage.getQuickSummaryAbstractEditorFrame());
        startNewAgendaItemPage.getQuickSummaryAbstractInputArea().append(quickSummaryData);
        u.switchToDefaultContent();


        if(fileToUpload) {
            startNewAgendaItemPage.getAgendaItemAttachmentsAddButton().click();
            startNewAgendaItemPage.getAgendaItemAttachmentsPopupNameField().val(p.attachmentName1());
            startNewAgendaItemPage.getAgendaItemAttachmentsPopupUploadField().uploadFile(new File(p.attachmentPdfFileName1()));
            startNewAgendaItemPage.getAgendaItemAttachmentsPopupSaveAndAddMoreButton().click();
            startNewAgendaItemPage.getAgendaItemAttachmentsPopupNameField().val(p.attachmentName2());
            startNewAgendaItemPage.getAgendaItemAttachmentsPopupUploadField().uploadFile(new File(p.attachmentPdfFileName2()));
            startNewAgendaItemPage.getAgendaItemAttachmentsPopupSaveButton().click();
        }

        startNewAgendaItemPage.getAddToAgendaButton().click();
        startNewAgendaItemPage.getSendToWorkFlowOkButton().click();
    }

    public void postAgendaItem() throws InterruptedException
    {
            navigationFrame.getMyTasksButton().click();
            myTasksPage.selectAgendaItemTask(agendaItemName, "");
            myTasksPage.getPostItemButton().click();
            myTasksPage.getConfirmPostItemPopupOkButton().click();
    }
}
