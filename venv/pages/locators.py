from selenium.webdriver.common.by import By




class BasePageLocators:
    LANGUAGE_CHANGE_BUTTON = (By.XPATH, "//*[contains(@class,'sc-14gaqg0-0 jGQJR')]")
    ENG_LANGUAGE_BUTTON = (By.XPATH, "//div[contains(@class, 'cmc-popover__dropdown')]//*[text()='English']")
    RUS_LANGUAGE_BUTTON = (By.XPATH, "//div[contains(@class, 'cmc-popover__dropdown')]//*[text()='Русский']")
    INFO_CRYPTOCURRENCIES = (By.XPATH, "//*[contains(@class, 'container')]/div/span[1]")
    INFO_CRYPTOCURRENCIES_LINK = (By.XPATH, "//*[contains(@class, 'container')]/div/span[1]/a")
    INFO_MARKET = (By.XPATH, "//*[contains(@class, 'container')]/div/span[2]")
    INFO_MARKET_LINK = (By.XPATH, "//*[contains(@class, 'container')]/div/span[2]/a")
    INFO_MARKET_CAP = (By.XPATH, "//*[contains(@class, 'container')]/div/span[3]")
    INFO_MARKET_CAP_LINK = (By.XPATH, "//*[contains(@class, 'container')]/div/span[3]/a")
    INFO_VOL = (By.XPATH, "//*[contains(@class, 'container')]/div/span[4]")
    INFO_VOL_LINK = (By.XPATH, "//*[contains(@class, 'container')]/div/span[4]/a")
    INFO_BTC = (By.XPATH, "//*[contains(@class, 'container')]/div/span[5]")
    INFO_BTC_LINK = (By.XPATH, "//*[contains(@class, 'container')]/div/span[5]/a")


class IndexPageLocators:
    ENG_TITLE = (By.XPATH, "//h1[contains(@class, 'sc-1m8sms1-1 bfHPLY')]")
    TABLE_HEADER_RANK = (By.XPATH, "//*[contains(@class, 'cmc-table--sort-by__rank')]/div[3]/div/table/thead/tr/th[1]")
    TABLE_HEADER_NAME = (By.XPATH, "//*[contains(@class, 'cmc-table--sort-by__rank')]/div[3]/div/table/thead/tr/th[2]")
    TABLE_HEADER_MARKET_CAP = (By.XPATH, "//*[contains(@class, 'cmc-table--sort-by__rank')]/div[3]/div/table/thead/tr/th[3]")
    TABLE_HEADER_PRICE = (By.XPATH, "//*[contains(@class, 'cmc-table--sort-by__rank')]/div[3]/div/table/thead/tr/th[4]")
    TABLE_HEADER_VOLUME = (By.XPATH, "//*[contains(@class, 'cmc-table--sort-by__rank')]/div[3]/div/table/thead/tr/th[5]")
    TABLE_HEADER_CIRCULATING_SUPPLY = (By.XPATH, "//*[contains(@class, 'cmc-table--sort-by__rank')]/div[3]/div/table/thead/tr/th[6]")
    TABLE_HEADER_CHANGE =  (By.XPATH, "//*[contains(@class, 'cmc-table--sort-by__rank')]/div[3]/div/table/thead/tr/th[7]")
    TABLE_HEADER_PRICE_GRAPH =  (By.XPATH, "//*[contains(@class, 'cmc-table--sort-by__rank')]/div[3]/div/table/thead/tr/th[8]")
    TABLE_ROW_MARKET_CAP = (By.XPATH, "//*[contains(@class, 'cmc-table--sort-by__rank')]/div[3]/div/table/tbody/tr[1]/td[3]")
    TABLE_ROW_PRICE = (By.XPATH, "//*[contains(@class, 'cmc-table--sort-by__rank')]/div[3]/div/table/tbody/tr[1]/td[4]")
    TABLE_ROW_VOLUME = (By.XPATH, "//*[contains(@class, 'cmc-table--sort-by__rank')]/div[3]/div/table/tbody/tr[1]/td[5]")
    TOTAL_MARKET_CAP = (By.XPATH, "//*[contains(@class, 'cmc-table-listing-footer sc-1jhjsq2-0 iInShT')]/strong")