package scenarios;

import pages.AdminPage;
import pages.NavigationFrame;

public class AddWorkflowRoute {
    private NavigationFrame navigationFrame = new NavigationFrame();
    private AdminPage.WorkflowRoutesPage workflowRoutesPage = new AdminPage.WorkflowRoutesPage();
    private AdminPage adminPage = new AdminPage();

    public void addWorkflowRoute() throws InterruptedException {
        navigationFrame.getAdminButton().click();
        adminPage.getWorkflowRoutesButton().click();
        workflowRoutesPage.addNewWorkflowRoute();
    }
}
