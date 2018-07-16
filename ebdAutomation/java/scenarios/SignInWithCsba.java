package scenarios;

import com.agendaonline.prop.Props;
import com.codeborne.selenide.WebDriverRunner;
import pages.SignInPage;
import utils.Utils;
import utils.Wait;

import javax.rmi.CORBA.Util;

public class SignInWithCsba {
    private SignInPage signInPage = new SignInPage();
    private Props p = new Props();
    private Wait wait = new Wait();

    public void signInWithCsba() throws InterruptedException {
        wait.waitForComplexElement(signInPage.getCsbaEmailField());
        wait.waitForPageLoadingSpinner();
        signInPage.getCsbaEmailField().val(p.csbaUser1Email());
        signInPage.getCsbaPassField().val(p.csbaUser1Pass());
        signInPage.getCsbaLoginButton().click();
        signInPage.getOrganizationSubscription().click();
    }
}
