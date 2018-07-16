package pages;

import com.agendaonline.prop.Props;
import com.codeborne.selenide.SelenideElement;
import utils.Wait;

import static com.codeborne.selenide.Selenide.$;

public class SignInPage {
    private Props p = new Props();
    private Wait wait = new Wait();
    private SelenideElement signinWithCsbaButton = $("paper-button.button-csba.csba-page-welcome");
    private SelenideElement organizationSubscription = $("paper-item[name='" + p.oraganizationSubscription() + "']");
    private SelenideElement csbaEmailField = $("#Username");
    private SelenideElement csbaPassField = $("#Password");
    private SelenideElement csbaLoginButton = $(".btn-primary");

    public SelenideElement getSignInWithCsbaButton()
    {
        return signinWithCsbaButton;
    }

    public SelenideElement getOrganizationSubscription() throws InterruptedException {
        wait.waitForComplexElement(organizationSubscription);
        return organizationSubscription;
    }

    public SelenideElement getCsbaEmailField() {
        return csbaEmailField;
    }

    public SelenideElement getCsbaPassField() {
        return csbaPassField;
    }

    public SelenideElement getCsbaLoginButton() {
        return csbaLoginButton;
    }
}
