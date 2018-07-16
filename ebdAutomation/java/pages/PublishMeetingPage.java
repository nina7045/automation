package pages;

import com.codeborne.selenide.SelenideElement;
import utils.Utils;
import utils.Wait;

import static com.codeborne.selenide.Selenide.$;

public class PublishMeetingPage {

    private SelenideElement publishMeetingButton = $("#actionButton1");
    private SelenideElement confirmPublishMeetingPopupOkButton = $(".accent.style-scope.submit-action.x-scope.paper-button-0");
    private Wait wait = new Wait();

    public SelenideElement getPublishMeetingButton() throws InterruptedException {
        wait.waitForComplexElement(publishMeetingButton);
        wait.waitForPageLoadingSpinner();
        return publishMeetingButton;
    }

    public SelenideElement getConfirmPublishMeetingPopupOkButton() throws InterruptedException {
        wait.waitForPageLoadingSpinner();
        return confirmPublishMeetingPopupOkButton;
    }
}
