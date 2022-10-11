from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TestSite:

    def setup_class(self):
        service = Service("./chromedriver")

        self.driver = Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("https://time.com/")
        pop_up_cross_button_element = self.driver.find_element(by=By.ID, value="close_icon")
        pop_up_cross_button_element.click()

    def test_page_title(self):
        page_title = self.driver.title
        expected_title = "TIME | Current & Breaking News | National & World Updates"
        assert page_title == expected_title

    def test_page_url(self):
        expected_url = "https://time.com/"
        assert self.driver.current_url == expected_url

    def teardown_class(self):
        self.driver.quit()