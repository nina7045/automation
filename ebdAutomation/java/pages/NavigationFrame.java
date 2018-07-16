package pages;

import com.codeborne.selenide.SelenideElement;
import utils.Utils;
import utils.Wait;

import static com.codeborne.selenide.Selenide.$;

public class NavigationFrame {
    private Wait wait = new Wait();
    private SelenideElement dashboardButton = $("#drawer sidebar-menu-item[label='Dashboard'] a");
    private SelenideElement myTasksButton = $("#drawer sidebar-menu-item[label='My Tasks'] a");
    private SelenideElement startNewButton = $("#drawer sidebar-menu-item[label='Start New'] a");
    private SelenideElement myMeetingsButton = $("#drawer sidebar-menu-item[label='My Meetings'] a");
    private SelenideElement adminButton = $("#drawer sidebar-menu-item[label='Admin'] a");
    private SelenideElement logoutButton = $("#drawer sidebar-menu-item[label='Log out'] a");

    public SelenideElement getStartNewButton() throws InterruptedException {
        wait.waitForPageLoadingSpinner();
        return startNewButton;
    }

    public SelenideElement getDashboardButton() throws InterruptedException {
        wait.waitForPageLoadingSpinner();
        return dashboardButton;
    }

    public SelenideElement getMyTasksButton() throws InterruptedException {
        wait.waitForPageLoadingSpinner();
        return myTasksButton;
    }

    public SelenideElement getMyMeetingsButton() throws InterruptedException {
        wait.waitForPageLoadingSpinner();
        return myMeetingsButton;
    }

    public SelenideElement getAdminButton() throws InterruptedException {
        wait.waitForPageLoadingSpinner();
        return adminButton;
    }

    public SelenideElement getLogoutButton() throws InterruptedException {
        wait.waitForPageLoadingSpinner();
        return logoutButton;
    }
}
