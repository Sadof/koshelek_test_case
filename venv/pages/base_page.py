from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from .locators import BasePageLocators as BPL
from time import sleep



class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.timeout = 5

    def open(self):
        self.browser.get(self.url)
        # sleep(self.timeout)

    def click_language_button(self):
        self.browser.find_element(*BPL.LANGUAGE_CHANGE_BUTTON).click()

    def is_lang_buttons_presented(self):
        assert self.is_element_present(*BPL.ENG_LANGUAGE_BUTTON)
        assert self.is_element_present(*BPL.RUS_LANGUAGE_BUTTON)

    def click_eng_lang(self):
        self.browser.find_element(*BPL.ENG_LANGUAGE_BUTTON).click()
        sleep(self.timeout)
        
    def click_rus_lang(self):
        self.browser.find_element(*BPL.RUS_LANGUAGE_BUTTON).click()
        sleep(self.timeout)

    def info_bar_eng(self):
        assert "Cryptocurrencies" in self.browser.find_element(*BPL.INFO_CRYPTOCURRENCIES).text
        assert "Markets" in self.browser.find_element(*BPL.INFO_MARKET).text
        assert "Market Cap" in self.browser.find_element(*BPL.INFO_MARKET_CAP).text
        assert "$" == self.browser.find_element(*BPL.INFO_MARKET_CAP_LINK).text[0],\
            self.browser.find_element(*BPL.INFO_MARKET_CAP_LINK).text[0]
        assert "24h Vol" in self.browser.find_element(*BPL.INFO_VOL).text
        assert "BTC Dominance" in self.browser.find_element(*BPL.INFO_BTC).text

    def info_bar_rus(self):
        assert "Криптовалюты" in self.browser.find_element(*BPL.INFO_CRYPTOCURRENCIES).text
        assert "Рынки" in self.browser.find_element(*BPL.INFO_MARKET).text
        assert "Рыночная капитализация" in self.browser.find_element(*BPL.INFO_MARKET_CAP).text
        assert "₽" == self.browser.find_element(*BPL.INFO_MARKET_CAP_LINK).text[0], \
        self.browser.find_element(*BPL.INFO_MARKET_CAP_LINK).text[0]
        assert "Объем за 24ч" in self.browser.find_element(*BPL.INFO_VOL).text
        assert "₽" == self.browser.find_element(*BPL.INFO_VOL_LINK).text[0], \
            self.browser.find_element(*BPL.INFO_VOL_LINK).text[0]
        assert "Доминирование BTC" in self.browser.find_element(*BPL.INFO_BTC).text



    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable((how, what)))
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False