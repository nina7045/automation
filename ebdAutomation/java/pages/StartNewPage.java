package pages;

import com.codeborne.selenide.Condition;
import com.codeborne.selenide.ElementsCollection;
import com.codeborne.selenide.SelenideElement;
import utils.Utils;
import utils.Wait;

import static com.codeborne.selenide.Selenide.$;
import static com.codeborne.selenide.Selenide.$$;

public class StartNewPage {
    private Wait wait = new Wait();
    private SelenideElement startNewTitle = $(".awi-master-page.x-scope.paper-toolbar-0");
    private ElementsCollection agendaManagementList = $$(".links-list.layout.vertical.style-scope.workflow-category > ul > li");
    private SelenideElement confirmServiceRequestTitle = $(".title.style-scope.awi-master-page");
    private SelenideElement confirmServiceRequestNextButton  = $("#confirmServiceRequestConfirmBtn");

    public SelenideElement getStartNewTitle() {

        return startNewTitle;
    }

    public SelenideElement getAgendaManagementList(String option) throws InterruptedException {

        wait.waitForPageLoadingSpinner();
        return agendaManagementList.find(Condition.text(option));
    }

    public SelenideElement getConfirmServiceRequestTitle() {
        return confirmServiceRequestTitle;
    }

    public SelenideElement getConfirmServiceRequestNextButton() throws InterruptedException {
        wait.waitForComplexElement(confirmServiceRequestNextButton);
        wait.waitForPageLoadingSpinner();
        return confirmServiceRequestNextButton;
    }
}
