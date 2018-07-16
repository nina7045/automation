package pages;

import com.codeborne.selenide.SelenideElement;
import utils.Wait;

import static com.codeborne.selenide.Selenide.$;

public class StartMeetingPage {

    private SelenideElement startMeetingButton = $("#actionButton2");
    private SelenideElement confirmPublishMeetingPopupOkButton = $(".accent.style-scope.submit-action.x-scope.paper-button-0");
    private Wait wait = new Wait();

    public SelenideElement getStartMeetingButton() throws InterruptedException {
        wait.waitForComplexElement(startMeetingButton);
        wait.waitForPageLoadingSpinner();
        return startMeetingButton;
    }

    public SelenideElement getConfirmPublishMeetingPopupOkButton() throws InterruptedException {
        wait.waitForPageLoadingSpinner();
        return confirmPublishMeetingPopupOkButton;
    }
}
