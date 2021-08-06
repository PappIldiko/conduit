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

    # # # Test1 - oldal megjelenése ok
    # def test_home_page_appearances(self):
    #     assert self.driver.find_element_by_xpath("//h1").text == "conduit"

    # Test1 - cookie-k

    # # Test2 - regisztráció - rendben fut
    # def test_registration(self):
    #     random_number = str(random.randint(1000, 2000))
    #     username = random_number + "Teszteles"
    #     email = username + "@gmail.com"
    #
    #     self.driver.maximize_window()
    #     self.driver.find_element_by_xpath('//a[@href="#/register"]').click()
    #     self.driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys(username)
    #     self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys(email)
    #     self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys(username)
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath('//button').click()
    #     element = WebDriverWait(
    #         self.driver, 5).until(
    #         EC.visibility_of_element_located((By.XPATH, ('//div[text()="Your registration was successful!"]')))
    #     )
    #     assert element.text == "Your registration was successful!"

    # # Test3 log in - ok
    # def test_login(self):
    #     conduit_registration(self.driver)
    #     self.driver.find_element_by_xpath('//a[@href="#/login"]').click()
    #     self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("Ildiko123@gmail.com")
    #     self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Ildiko123@gmail.com")
    #     # time.sleep(5)
    #     # self.driver.find_element_by_xpath('//form/button').click()
    #     elem = WebDriverWait(
    #         self.driver, 5).until(
    #         EC.visibility_of_element_located((By.XPATH, ('//form/button')))
    #     )
    #     elem.click()
    #
    #     element = WebDriverWait(
    #         self.driver, 5).until(
    #         EC.visibility_of_element_located((By.XPATH, ('//a[normalize-space(text())="Your Feed"]')))
    #     )
    #     assert element.text == "Your Feed"


    # # Test4 log out - ok
    # def test_logout(self):
    #     conduit_registration(self.driver)
    #     element = WebDriverWait(
    #         self.driver, 14).until(
    #         EC.visibility_of_element_located((By.XPATH, ('//i[@class="ion-android-exit"]')))
    #     )
    #     element.click()
    #     time.sleep(2)
    #
    #     elem = WebDriverWait(
    #         self.driver, 5).until(
    #         EC.visibility_of_element_located((By.XPATH, ('//a[normalize-space(text())="Sign in"]')))
    #     )
    #     assert elem.text == "Sign in"


        # self.driver.find_element_by_xpath('//a[@active-class="active"]').click() ('//ul/li[5]')


    #
    # # Test4 create and delete new article - ez nem kell
    # def test_create_delete_new_article(self):
    #     conduit_registration(self.driver)
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
    #     element = WebDriverWait(
    #         self.driver, 5).until(
    #         EC.visibility_of_element_located((By.XPATH, ('//button[@class="btn btn-outline-danger btn-sm"]')))
    #     )
    #     element.click()

    # Test5 create new article - ok
    # def test_create_new_article(self):
    #     conduit_registration(self.driver)
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
    #     element = WebDriverWait(
    #         self.driver, 5).until(
    #         EC.visibility_of_element_located((By.XPATH, ('//button[@class="btn btn-outline-danger btn-sm"]')))
    #     )
    #     element.click()

    # Test6 modify article
    def test_modify_article(self):
        conduit_registration(self.driver)
        time.sleep(3)
        self.driver.find_elements_by_xpath('//a[@class="nav-link"]')[0].click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys(
            "Chocolate lollipop oat cake")
        self.driver.find_elements_by_xpath('//form//input')[1].send_keys("About cakes")
        self.driver.find_element_by_xpath(
            '//form//textarea[@placeholder="Write your article (in markdown)"]').send_keys(
            "Powder donut liquorice I love I love powder sesame snaps jujubes. Gummies chocolate sweet roll. Icing I love powder I love danish cookie I love. Cake chocolate bar I love. Cupcake I love cheesecake pastry I love fruitcake candy croissant. Lollipop caramels I love bonbon. Gingerbread powder macaroon cookie. Sesame snaps tootsie roll bear claw I love. Brownie cake gingerbread carrot cake marshmallow I love halvah.")
        self.driver.find_elements_by_xpath('//form//input')[2].send_keys("bonbon")
        self.driver.find_element_by_xpath('//button[normalize-space(text()="Publish Article")]').click()


        time.sleep(2)
        self.driver.find_element_by_xpath('//span[normalize-space(text()=" Edit Article")]').click()
        self.driver.find_element_by_xpath('//a[@class="btn btn-sm btn-outline-secondary"]').click()
        time.sleep(2)
        # self.driver.find_element_by_xpath('//input[@class="form-control form-control-lg"]').send_keys(" modified")
        self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys(" modified")
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[normalize-space(text()="Publish Article")]').click()


    # Test7 delete article
    def test_delete_article(self):
        conduit_registration(self.driver)
        time.sleep(3)
        self.driver.find_elements_by_xpath('//a[@class="nav-link"]')[0].click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys(
            "Chocolate lollipop oat cake")
        self.driver.find_elements_by_xpath('//form//input')[1].send_keys("About cakes")
        self.driver.find_element_by_xpath(
            '//form//textarea[@placeholder="Write your article (in markdown)"]').send_keys(
            "Powder donut liquorice I love I love powder sesame snaps jujubes. Gummies chocolate sweet roll. Icing I love powder I love danish cookie I love. Cake chocolate bar I love. Cupcake I love cheesecake pastry I love fruitcake candy croissant. Lollipop caramels I love bonbon. Gingerbread powder macaroon cookie. Sesame snaps tootsie roll bear claw I love. Brownie cake gingerbread carrot cake marshmallow I love halvah.")
        self.driver.find_elements_by_xpath('//form//input')[2].send_keys("bonbon")
        self.driver.find_element_by_xpath('//button[normalize-space(text()="Publish Article")]').click()

        element = WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, ('//button[@class="btn btn-outline-danger btn-sm"]')))
    )
        element.click()
