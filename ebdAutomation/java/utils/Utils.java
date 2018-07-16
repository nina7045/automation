package utils;

import com.codeborne.selenide.SelenideElement;
import com.codeborne.selenide.WebDriverRunner;
import org.openqa.selenium.JavascriptExecutor;
import java.util.Random;

public class Utils {
    private static Random random = new Random();

    private static final int rnd = random.nextInt(100000);
    private static final int rnd2 = random.nextInt(100000);

    public void scrollTo(SelenideElement e)
    {
        ((JavascriptExecutor) WebDriverRunner.getWebDriver()).executeScript("arguments[0].scrollIntoView(true);", e);
    }

    public void switchToFrame(SelenideElement e)
    {
        WebDriverRunner.getWebDriver().switchTo().frame(e);
    }

    public void switchToDefaultContent()
    {
        WebDriverRunner.getWebDriver().switchTo().defaultContent();
    }

    public int getId()
    {
        return random.nextInt(100000);
    }

    public int getStaticId()
    {
        return rnd;
    }

    public int getStaticId2()
    {
        return rnd2;
    }
}
