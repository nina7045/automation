package pages;

import com.codeborne.selenide.SelenideElement;
import utils.Utils;
import utils.Wait;

import javax.rmi.CORBA.Util;

import static com.codeborne.selenide.Selenide.$;

public class DashboardPage {
    private Wait wait = new Wait();
    private SelenideElement dashboardTitle = $(".awi-master-page.x-scope.paper-toolbar-0");

    public SelenideElement getDashboardTitle() {
        wait.waitForElement(dashboardTitle);
        return dashboardTitle;
    }
}
