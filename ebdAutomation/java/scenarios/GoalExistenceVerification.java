package scenarios;

import com.agendaonline.prop.Props;
import pages.AdminPage;
import pages.NavigationFrame;

public class GoalExistenceVerification {
    private Props p = new Props();
    private NavigationFrame navigationFrame = new NavigationFrame();
    private AdminPage adminPage = new AdminPage();
    private AdminPage.GoalsPage goalsPage = new AdminPage.GoalsPage();

    public void goalExistenceVerification() throws InterruptedException {
        navigationFrame.getAdminButton().click();
        adminPage.getOpenGoalsButton().click();
        if(!goalsPage.isAnyGoalExists())
            goalsPage.createNewGoal(p.newGoalName(), p.newGoalDescription(), p.newGoalType());
    }
}
