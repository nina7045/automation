package pages;

import com.agendaonline.prop.Props;
import com.codeborne.selenide.SelenideElement;
import utils.SearchItemEngine;
import utils.Wait;

import static com.codeborne.selenide.Selenide.$;

public class MyTasksPage {
    private Wait wait = new Wait();
    private SearchItemEngine searchItemEngine = new SearchItemEngine();
    private String taskPath = "iron-list#list awi-grid-row[index='";
    private SelenideElement youHaveNewMessagePopupCloseButton = $(".dialog-medium.style-scope.step-comment.x-scope.paper-dialog-0").find(".style-scope.step-comment.x-scope.paper-icon-button-0");
    private SelenideElement postItemButton = $("#actionButton1");
    private SelenideElement confirmPostItemPopupOkButton = $(".accent.style-scope.submit-action.x-scope.paper-button-0");
    private SelenideElement publishMeetingButton = $("#actionButton0");
    private SelenideElement confirmPublishMeetingPopupOkButton = $(".accent.style-scope.submit-action.x-scope.paper-button-0");
    private SelenideElement closeMeetingButton = $("#actionButton1");
    private SelenideElement amountOfItems = $(".total-items.style-scope.awi-grid-footer");

    public void selectAgendaItemTask(String agendaItemName, String dataName) throws InterruptedException {
        searchItemEngine.selectItem(agendaItemName, dataName, amountOfItems, taskPath, false);
    }

    public void selectMeetingTask(String meetingTitle, String dataName) throws InterruptedException {
        searchItemEngine.selectItem(meetingTitle, dataName, amountOfItems, taskPath, false);
    }

    public SelenideElement getYouHaveNewMessagePopupCloseButton() throws InterruptedException {
        wait.waitForComplexElement(youHaveNewMessagePopupCloseButton);
        return youHaveNewMessagePopupCloseButton;
    }

    public SelenideElement getPostItemButton() throws InterruptedException {
        wait.waitForElement(postItemButton);
        wait.waitForPageLoadingSpinner();
        return postItemButton;
    }

    public SelenideElement getConfirmPostItemPopupOkButton() throws InterruptedException {
        wait.waitForComplexElement(confirmPostItemPopupOkButton);
        wait.waitForPageLoadingSpinner();
        return confirmPostItemPopupOkButton;
    }

    public SelenideElement getPublishMeetingButton() {
        return publishMeetingButton;
    }

    public SelenideElement getConfirmPublishMeetingPopupOkButton() throws InterruptedException {
        wait.waitForPageLoadingSpinner();
        return confirmPublishMeetingPopupOkButton;
    }

    public SelenideElement getCloseMeetingButton() throws InterruptedException {
        wait.waitForComplexElement(closeMeetingButton);
        wait.waitForPageLoadingSpinner();
        return closeMeetingButton;
    }

}
