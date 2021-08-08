from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from conduit_data import *
from webdriver_manager.chrome import ChromeDriverManager


class TestConduit(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://localhost:1667/#/")

    def teardown(self):
        self.driver.quit()

    # Test1 - oldal megjelenése és cookie-k elfogadása ok
    def test_home_page_appearances(self):
        assert self.driver.find_element_by_xpath("//h1").text == "conduit"
        accept_cookies_btn = self.driver.find_element_by_xpath('//div[@id="cookie-policy-panel"]//button[2]')
        accept_cookies_btn.click()


    # Test2 - regisztráció - rendben fut
    def test_registration(self):
        self.driver.find_element_by_xpath('//a[@href="#/register"]').click()
        self.driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys("Tester12@gmail.com")
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("Tester12@gmail.com")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Tester12@gmail.com")
        time.sleep(3)
        self.driver.find_element_by_xpath('//button').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]').click()
        time.sleep(3)
        element = WebDriverWait(
            self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, ('//a[normalize-space(text())="Your Feed"]')))
        )
        assert element.text == "Your Feed"

    # Test3 log in - ok
    def test_login(self):
        self.driver.find_element_by_xpath('//a[@href="#/login"]').click()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("Tester12@gmail.com")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Tester12@gmail.com")
        sign_in_btn = WebDriverWait(
            self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, ('//form/button')))
        )
        sign_in_btn.click()

        element = WebDriverWait(
            self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, ('//a[normalize-space(text())="Your Feed"]')))
        )
        assert element.text == "Your Feed"


    # # Test4 log out - ok
    # def test_logout(self):
    #     self.test_login()
    #     logout_btn = WebDriverWait(
    #         self.driver, 5).until(
    #         EC.visibility_of_element_located((By.XPATH, ('//i[@class="ion-android-exit"]')))
    #     )
    #     logout_btn.click()
    #
    #     sign_in_btn = WebDriverWait(
    #         self.driver, 5).until(
    #         EC.visibility_of_element_located((By.XPATH, ('//a[normalize-space(text())="Sign in"]')))
    #     )
    #     assert sign_in_btn.text == "Sign in"
    #



    # # Test5 create new article - ok
    # def test_create_new_article(self):
    #     self.test_login()
    #     time.sleep(3)
    #     self.driver.find_elements_by_xpath('//a[@class="nav-link"]')[0].click()
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys(
    #         "Chocolate lollipop oat cake")
    #     self.driver.find_elements_by_xpath('//form//input')[1].send_keys("About cakes")
    #     self.driver.find_element_by_xpath(
    #         '//form//textarea[@placeholder="Write your article (in markdown)"]').send_keys(
    #         "Powder donut liquorice I love I love powder sesame snaps jujubes. Gummies chocolate sweet roll. Icing I love powder I love danish cookie I love. Cake chocolate bar I love. Cupcake I love cheesecake pastry I love fruitcake candy croissant. Lollipop caramels I love bonbon. Gingerbread powder macaroon cookie. Sesame snaps tootsie roll bear claw I love. Brownie cake gingerbread carrot cake marshmallow I love halvah.")
    #     self.driver.find_elements_by_xpath('//form//input')[2].send_keys("bonbon")
    #     self.driver.find_element_by_xpath('//button[normalize-space(text()="Publish Article")]').click()
    #
    #     time.sleep(2)
    #     article_title = self.driver.find_element_by_xpath('//h1[text()="Chocolate lollipop oat cake"]')
    #     assert article_title.text == "Chocolate lollipop oat cake"
    #
    #
    #     delete_btn = WebDriverWait(
    #         self.driver, 5).until(
    #         EC.visibility_of_element_located((By.XPATH, ('//button[@class="btn btn-outline-danger btn-sm"]')))
    #     )
    #     delete_btn.click()


    # Test6 modify article
    # def test_modify_article(self):
    #     self.test_login()
    #     time.sleep(3)
    #     self.driver.find_elements_by_xpath('//a[@class="nav-link"]')[0].click()
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys(
    #         "Chocolate lollipop oat cake")
    #     self.driver.find_elements_by_xpath('//form//input')[1].send_keys("About cakes")
    #     self.driver.find_element_by_xpath(
    #         '//form//textarea[@placeholder="Write your article (in markdown)"]').send_keys(
    #         "Powder donut liquorice I love I love powder sesame snaps jujubes. Gummies chocolate sweet roll. Icing I love powder I love danish cookie I love. Cake chocolate bar I love. Cupcake I love cheesecake pastry I love fruitcake candy croissant. Lollipop caramels I love bonbon. Gingerbread powder macaroon cookie. Sesame snaps tootsie roll bear claw I love. Brownie cake gingerbread carrot cake marshmallow I love halvah.")
    #     self.driver.find_elements_by_xpath('//form//input')[2].send_keys("bonbon")
    #     self.driver.find_element_by_xpath('//button[normalize-space(text()="Publish Article")]').click()
    #
    #
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath('//span[normalize-space(text()=" Edit Article")]').click()
    #     self.driver.find_element_by_xpath('//a[@class="btn btn-sm btn-outline-secondary"]').click()
    #     time.sleep(2)
    #     # self.driver.find_element_by_xpath('//input[@class="form-control form-control-lg"]').send_keys(" modified")
    #     self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys(" modified")
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath('//button[normalize-space(text()="Publish Article")]').click()
    #
    #     time.sleep(2)
    #     article_title = self.driver.find_element_by_xpath('//h1[text()="Chocolate lollipop oat cake modified"]')
    #     assert article_title.text == "Chocolate lollipop oat cake modified"



    # Test7 delete article
    # def test_delete_article(self):
    #     self.test_login()
    #     time.sleep(3)
    #     self.driver.find_elements_by_xpath('//a[@class="nav-link"]')[0].click()
    #     time.sleep(5)
    #     self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys(
    #         "Chocolate lollipop oat cake")
    #     # self.driver.find_elements_by_xpath('//form//input')[1].send_keys("About cakes")
    #     # self.driver.find_element_by_xpath(
    #     #     '//form//textarea[@placeholder="Write your article (in markdown)"]').send_keys(
    #     #     "Powder donut liquorice I love I love powder sesame snaps jujubes. Gummies chocolate sweet roll. Icing I love powder I love danish cookie I love. Cake chocolate bar I love. Cupcake I love cheesecake pastry I love fruitcake candy croissant. Lollipop caramels I love bonbon. Gingerbread powder macaroon cookie. Sesame snaps tootsie roll bear claw I love. Brownie cake gingerbread carrot cake marshmallow I love halvah.")
    #     # self.driver.find_elements_by_xpath('//form//input')[2].send_keys("bonbon")
    #     self.driver.find_element_by_xpath('//button[normalize-space(text()="Publish Article")]').click()
    #
    #     delete_btn = WebDriverWait(
    #         self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, ('//button[@class="btn btn-outline-danger btn-sm"]')))
    # )
    #     delete_btn.click()
    #
    #
    #     self.driver.find_element_by_xpath('//a[@href="#/@Tester12@gmail.com/"]').click() # username-re cserélni
    #     time.sleep(3)
    #     article_title = self.driver.find_elements_by_xpath('//h1')[0]
    #     assert article_title.text != "Chocolate lollipop oat cake"

    # Test8 listing data - nem fut le - sárga
    # def test_listing_data(self):
    #     self.test_login()
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath('//a[@href="#/editor"]').click()
    #
    #     time.sleep(5)
    #     self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys("Chocolate lollipop oat cake")
    #     self.driver.find_elements_by_xpath('//form//input')[2].send_keys("bonbon")
    #     self.driver.find_element_by_xpath('//button[normalize-space(text()="Publish Article")]').click()
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath('//a[@href="#/@Tester12@gmail.com/"]').click()
    #     time.sleep(3)
    #     assert self.driver.find_element_by_xpath('//h4').text == "Tester12@gmail.com"
    #     assert self.driver.find_element_by_xpath('//a[@class="author router-link-exact-active router-link-active"]').text == "Tester12@gmail.com"
    #     # assert self.driver.find_element_by_xpath('//h1').text == "Chocolate lollipop oat cake"
    #     # assert self.driver.find_element_by_xpath('//a[@href="#/tag/bonbon"]').text == "bonbon"
    #
    #     print(self.driver.find_element_by_xpath('//h4').text)
    #     print(self.driver.find_element_by_xpath('//a[@class="author router-link-exact-active router-link-active"]').text)
    #     print(self.driver.find_element_by_xpath('//h1').text)
    #     print(self.driver.find_element_by_xpath('//a[@href="#/tag/bonbon"]').text)
    #
    #     delete_btn = WebDriverWait(
    #             self.driver, 10).until(
    #             EC.visibility_of_element_located((By.XPATH, ('//button[@class="btn btn-outline-danger btn-sm"]')))
    #     )
    #     delete_btn.click()

    # Test9 saving data
    def test_save_data(self):
        self.test_login()

        time.sleep(5)
        articles_preview = self.driver.find_elements_by_xpath('//div[@class="article-preview"]')

        with open("articles_preview.txt", "w") as txt1:
            for i in articles_preview:
                txt1.write(f"{i.text}")
            # print(i.text)

        with open("articles_preview.txt", "r") as txt1:
            txt2 = txt1.readlines()
            # print(txt2, end='')
            for line in txt2:
                print(line, end='')


        # Test10 pagination
        # Test10 ismételt és sorozatos adatbevitel





