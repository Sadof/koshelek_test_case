import pytest
from pages.index_page import IndexPage
from time import sleep

INDEXPAGE_URL = 'https://coinmarketcap.com/'


@pytest.mark.smoke
class TestIndexPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.index_page = IndexPage(self.browser, INDEXPAGE_URL)
        self.index_page.open()

    def test_open_index_page(self):
        self.index_page.is_it_eng_index_page()

    def test_info_bar_end(self):
        self.index_page.info_bar_eng()

    def test_info_bar_eng_rus_eng(self):
        self.index_page.click_language_button()
        self.index_page.click_rus_lang()
        self.index_page.click_language_button()
        self.index_page.click_eng_lang()
        self.index_page.info_bar_eng()

    def test_click_change_language_button(self):
        self.index_page.click_language_button()
        self.index_page.is_lang_buttons_presented()

    def test_change_to_rus_lang(self):
        self.index_page.click_language_button()
        self.index_page.click_rus_lang()
        self.index_page.is_it_rus_index_page()

    def test_info_bar_rus(self):
        self.index_page.click_language_button()
        self.index_page.click_rus_lang()
        self.index_page.info_bar_rus()

    def test_table_header_eng(self):
        self.index_page.table_header_eng()

    def test_table_header_rus(self):
        self.index_page.click_language_button()
        self.index_page.click_rus_lang()
        self.index_page.table_header_rus()

    def test_total_market_eng(self):
        self.index_page.total_market_eng()

    def test_total_market_rus(self):
        self.index_page.click_language_button()
        self.index_page.click_rus_lang()
        self.index_page.total_market_rus()

    def test_table_row_eng(self):
        self.index_page.table_row_eng()

    def test_table_row_rus(self):
        self.index_page.click_language_button()
        self.index_page.click_rus_lang()
        self.index_page.table_row_rus()

