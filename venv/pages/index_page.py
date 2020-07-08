from selenium import webdriver
from .base_page import BasePage
from .locators import IndexPageLocators as IPL


INDEXPAGE_URL = 'https://coinmarketcap.com/'
INDEXPAGE_RUS_URL = "https://coinmarketcap.com/ru/"

class IndexPage(BasePage):

    def is_it_eng_index_page(self):
        assert self.browser.current_url == INDEXPAGE_URL
        assert "Top 100 Cryptocurrencies by Market Capitalization" in self.browser.find_element(*IPL.ENG_TITLE).text

    def is_it_rus_index_page(self):
        assert self.browser.current_url == INDEXPAGE_RUS_URL
        assert "Топ-100 Криптовалюты по рыночной капитализации" in self.browser.find_element(*IPL.ENG_TITLE).text

    def table_header_eng(self):
        assert "Name" in self.browser.find_element(*IPL.TABLE_HEADER_NAME).text, \
            self.browser.find_element(*IPL.TABLE_HEADER_NAME).text
        assert "Market Cap" in self.browser.find_element(*IPL.TABLE_HEADER_MARKET_CAP).text
        assert "Price" in self.browser.find_element(*IPL.TABLE_HEADER_PRICE).text
        assert "Volume (24h)" in self.browser.find_element(*IPL.TABLE_HEADER_VOLUME).text
        assert "Circulating Supply" in self.browser.find_element(*IPL.TABLE_HEADER_CIRCULATING_SUPPLY).text
        assert "Change (24h)" in self.browser.find_element(*IPL.TABLE_HEADER_CHANGE).text
        assert "Price Graph (7d)" in self.browser.find_element(*IPL.TABLE_HEADER_PRICE_GRAPH).text

    def table_header_rus(self):
        assert "Наименование" in self.browser.find_element(*IPL.TABLE_HEADER_NAME).text, \
            self.browser.find_element(*IPL.TABLE_HEADER_NAME).text
        assert "Рыночная капитализация" in self.browser.find_element(*IPL.TABLE_HEADER_MARKET_CAP).text
        assert "Цена" in self.browser.find_element(*IPL.TABLE_HEADER_PRICE).text
        assert "Объем (за 24ч)" in self.browser.find_element(*IPL.TABLE_HEADER_VOLUME).text
        assert "Циркулирующее предложение" in self.browser.find_element(*IPL.TABLE_HEADER_CIRCULATING_SUPPLY).text
        assert "Изменение (за 24ч)" in self.browser.find_element(*IPL.TABLE_HEADER_CHANGE).text
        assert "График цен (за 7д)" in self.browser.find_element(*IPL.TABLE_HEADER_PRICE_GRAPH).text

    def total_market_eng(self):
        assert "Total Market Cap: $" in self.browser.find_element(*IPL.TOTAL_MARKET_CAP).text ,\
            self.browser.find_element(*IPL.TOTAL_MARKET_CAP).text

    def total_market_rus(self):
        assert "Общая рыночная капитализация: ₽" in self.browser.find_element(*IPL.TOTAL_MARKET_CAP).text ,\
            self.browser.find_element(*IPL.TOTAL_MARKET_CAP).text

    def table_row(self):
        table = self.browser.find_element(*IPL.TABLE_ROW)
        print([elem.text for elem in table])
        # assert "756775685856" in row.text, self.browser.find_element(*IPL.TABLE_ROW).text

    def table_row_price_eng(self):
        assert "$" in self.browser.find_element(*IPL.TABLE_ROW_PRICE).text[0]

    def table_row_market_cap_eng(self):
        assert "$" in self.browser.find_element(*IPL.TABLE_ROW_MARKET_CAP).text[0]

    def table_row_volume_eng(self):
        assert "$" in self.browser.find_element(*IPL.TABLE_ROW_VOLUME).text[0]

    def table_row_eng(self):
        self.table_row_price_eng()
        self.table_row_market_cap_eng()
        self.table_row_volume_eng()

    def table_row_price_rus(self):
        assert "₽" in self.browser.find_element(*IPL.TABLE_ROW_PRICE).text[0]

    def table_row_market_cap_rus(self):
        assert "₽" in self.browser.find_element(*IPL.TABLE_ROW_MARKET_CAP).text[0]

    def table_row_volume_rus(self):
        assert "₽" in self.browser.find_element(*IPL.TABLE_ROW_VOLUME).text[0]

    def table_row_rus(self):
        self.table_row_price_rus()
        self.table_row_market_cap_rus()
        self.table_row_volume_rus()
