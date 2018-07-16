package pages;

import com.codeborne.selenide.SelenideElement;
import utils.SearchItemEngine;

import static com.codeborne.selenide.Selenide.$;

public class MyMeetingsPage {
    private SearchItemEngine searchItemEngine = new SearchItemEngine();
    private String taskPath = "iron-list#list awi-grid-row[index='";
    private SelenideElement amountOfItems = $(".total-items.style-scope.awi-grid-footer");

    public void selectMeeting(String meetingTitle, String status) throws InterruptedException {
        searchItemEngine.selectItem(meetingTitle, status, amountOfItems, taskPath, false);
    }

    public void selectMeetingWithLongWait(String meetingTitle, String status) throws InterruptedException {

        searchItemEngine.selectItem(meetingTitle, status, amountOfItems, taskPath, true);
    }
}
