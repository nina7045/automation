package utils;

import com.codeborne.selenide.SelenideElement;
import com.codeborne.selenide.WebDriverRunner;

import org.apache.log4j.Logger;

import static com.codeborne.selenide.Selenide.$;

public class SearchItemEngine {
    private Utils u = new Utils();
    private Wait wait = new Wait();
    final static Logger logger = Logger.getLogger(SearchItemEngine.class);
    private String _itemPathBodySelector;
    private SelenideElement itemPath(String index) { return $(_itemPathBodySelector + index + "']"); }

    public void selectItem(String itemName, String dataName2, SelenideElement amountSelector, String itemPathBodySelector, boolean longWaitNeeded) throws InterruptedException
    {
        wait.waitForPageLoadingSpinner();
        wait.waitForComplexElement(amountSelector);
        _itemPathBodySelector = itemPathBodySelector;

        int amount = Integer.parseInt(amountSelector.getText().replaceAll("\\D+","")); // getting total amount of items int the list

        logger.info("Amount of items in the list: " + amount);
        logger.info("=>=>=>=>=>=>=> " + dataName2 + "\nSearching for " + itemName + " in the list");

        int ms = 30000; // amount of seconds to wait for long wait
        int n = longWaitNeeded ? 20 : 5; // amount of iterations for search

        for(int i = 0; i < n; i++)
        {
            logger.info("Attempt " + i);
            if (itemSearchEngine(itemName, dataName2, amount)) {
                break;
            }
            else
            {
                if(longWaitNeeded)
                {
                    logger.info("Item is not visible yet, waiting for " + ms + " seconds more");
                    Thread.sleep(ms);
                }
            }

            WebDriverRunner.getWebDriver().navigate().refresh();
            wait.waitForPageLoadingSpinner();
        }
    }

    private boolean itemSearchEngine(String itemName, String itemData, int amount)
    {
        for (int i = 0; i < amount-1; i++)
        {
            SelenideElement item = itemPath(i + "");
            u.scrollTo(item);
            if (item.getText().toLowerCase().contains(itemName.toLowerCase())
                    &&
                item.getText().toLowerCase().contains(itemData.toLowerCase()))
            {
                logger.info("Item has been FOUND, opening...");
                item.click();
                return true;
            }
        }
        return false;
    }
}
