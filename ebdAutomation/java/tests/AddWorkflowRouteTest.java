package tests;

import com.agendaonline.prop.Props;
import com.codeborne.selenide.WebDriverRunner;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import scenarios.AddWorkflowRoute;
import scenarios.SignInWithCsba;
import utils.BrowserInstanceInitializer;

import static com.codeborne.selenide.Selenide.open;

public class AddWorkflowRouteTest {
    private Props p = new Props();
    private SignInWithCsba signInWithCsba = new SignInWithCsba();
    private AddWorkflowRoute addWorkflowRoute = new AddWorkflowRoute();
    private BrowserInstanceInitializer browser = new BrowserInstanceInitializer();

    @Test
    public void addWorkflowRouteTest() throws InterruptedException {
        signInWithCsba.signInWithCsba();
        addWorkflowRoute.addWorkflowRoute();
    }

    @Before
    public void before()
    {
        browser.initialize(p.browser());
        WebDriverRunner.getWebDriver().manage().window().maximize();
        open(p.agendaOnlineUrl());
    }

    @After
    public void after() {
        WebDriverRunner.getWebDriver().quit();
    }
}
