package utils;

import com.agendaonline.prop.Props;
import com.codeborne.selenide.WebDriverRunner;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.safari.SafariDriver;

public class BrowserInstanceInitializer {

    public void initialize(String browser)
    {
        Props p = new Props();

        switch(browser)
        {
            case "chrome":
                System.setProperty("webdriver.chrome.driver", p.chromeDriverPath());
                WebDriverRunner.setWebDriver(new ChromeDriver());
                break;
            case "firefox":
                System.setProperty("webdriver.gecko.driver", p.firefoxDriverPath());
                WebDriverRunner.setWebDriver(new FirefoxDriver());
                break;
            case "safari":
                System.setProperty("webdriver.safari.driver", p.safariDriverPath());
                WebDriverRunner.setWebDriver(new SafariDriver());
                break;
            default:
                System.setProperty("webdriver.chrome.driver", p.chromeDriverPath());
                WebDriverRunner.setWebDriver(new ChromeDriver());
                break;
        }
    }

}
