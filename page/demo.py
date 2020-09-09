from poium import Page, CSSElement
from selenium import webdriver


class BaiduIndexPage(Page):
    search_input = CSSElement('#kw')
    search_button = CSSElement('#su')



driver = webdriver.Chrome()

page = BaiduIndexPage(driver)
page.get("https://www.baidu.com")

page.search_input.set_text("poium")
page.search_button.click()

driver.quit()