package pages;

import com.codeborne.selenide.SelenideElement;
import org.openqa.selenium.Keys;
import utils.Utils;
import utils.Wait;

import static com.codeborne.selenide.Selenide.$;

public class MeetingInDevelopmentPage {

    private SelenideElement attendanceGroupField = $("awi-combobox[binding='Meeting.MeetingAG'] input");
    private Wait wait = new Wait();

    public void selectAttendanceGroup(String option) throws InterruptedException {
        Thread.sleep(5000);
        wait.waitForPageLoadingSpinner();
        attendanceGroupField.val(option);
        Thread.sleep(500);
        attendanceGroupField.append("" + Keys.ARROW_DOWN + Keys.ENTER);
    }
}
