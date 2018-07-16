package utils;

import com.codeborne.selenide.Condition;
import com.codeborne.selenide.SelenideElement;

import static com.codeborne.selenide.Selenide.$;

public class Wait {
    private SelenideElement pageLoadingSpinner = $("#backdrop");

    public void waitForPageLoadingSpinner() throws InterruptedException {
        Thread.sleep(100);
        while(pageLoadingSpinner.isDisplayed()) {
            Thread.sleep(500);
        }
    }

    public void waitForElement(SelenideElement locator)
    {
        locator.waitUntil(Condition.visible, 8000);
    }

    public void waitForComplexElement(SelenideElement selector) throws InterruptedException {
        Thread.sleep(3000);

        if(!(selector.exists() && !selector.isEnabled() && !selector.isDisplayed()))
            Thread.sleep(1000);
    }
}
