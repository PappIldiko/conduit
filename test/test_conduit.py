from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager
import csv


class TestConduit(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://localhost:1667/#/")

    def teardown(self):
        self.driver.quit()

    # Test1 - oldal megjelenése - a 'conduit' szó megjelenése, majd a cookie-k elfogadása
    # gomb megkeresése megkattintása
    def test_home_page_appearances(self):
        assert self.driver.find_element_by_xpath("//h1").text == "conduit"
        accept_cookies_btn = self.driver.find_element_by_xpath('//div[@id="cookie-policy-panel"]//button[2]')
        accept_cookies_btn.click()

    # Test2 - regisztráció - regisztráció gombra kattintás, adatok kitöltése, Sign up gombra kattintás, Welcome pop up
    # ablak ok gombjára kattintás, Your Feed fül elem megjelenése igazolja a regisztráció létrejöttét
    def test_registration(self):
        self.driver.find_element_by_xpath('//a[@href="#/register"]').click()
        self.driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys("Tester15@gmail.com")
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("Tester15@gmail.com")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Tester15@gmail.com")
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

    # Test3 bejelentkezés - a főoldalon a Sign in gombra kattintás, belépési adatok beírása a megkeresett mezőkbe,
    # a Sign in gombra kattintás, Your Feed fül elem megjelenése igazolja a belépés megtörténtét
    def test_login(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//a[@href="#/login"]').click()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("Tester15@gmail.com")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Tester15@gmail.com")
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

    # Test4 - kijelentkezés - a login függvény meghívása, a kilépés gomb kattintása, a Sign in gomb megjelenés
    # a kilépés tényét igazolja
    def test_logout(self):
        self.test_login()
        logout_btn = WebDriverWait(
            self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, ('//i[@class="ion-android-exit"]')))
        )
        logout_btn.click()

        sign_in_btn = WebDriverWait(
            self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, ('//a[normalize-space(text())="Sign in"]')))
        )
        assert sign_in_btn.text == "Sign in"

    # Test5 - új cikk létrehozása -  a login függvény meghívása, a New article gomb kattintása, a megjelenő 4 mezőbe
    # adatok küldése, kitöltése után a Publish Article gomb megnyomása, a cikk oldalán a cikk címének megjelenése
    # igazolja a cikk létrejöttét, végül  a cikk törlése
    def test_create_new_article(self):
        self.test_login()
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
        article_title = self.driver.find_element_by_xpath('//h1[text()="Chocolate lollipop oat cake"]')
        assert article_title.text == "Chocolate lollipop oat cake"

    # Test6 - cikk módosítása - belépés, cikk létrehozása, az Edit Article gombra kattintás, a cikk címébe a
    # "modified" szó beírása és a Publish Article gombbal a változtatás mentése, végül a cikk aloldalán megjelenő
    # módosított cím ellenőrzése
    def test_modify_article(self):
        self.test_create_new_article()

        time.sleep(3)
        self.driver.find_element_by_xpath('//span[normalize-space(text()=" Edit Article")]').click()
        self.driver.find_element_by_xpath('//a[@class="btn btn-sm btn-outline-secondary"]').click()
        time.sleep(2)
        # self.driver.find_element_by_xpath('//input[@class="form-control form-control-lg"]').send_keys(" modified")
        self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys(" modified")
        time.sleep(3)
        self.driver.find_element_by_xpath('//button[normalize-space(text()="Publish Article")]').click()

        time.sleep(5)
        article_title = self.driver.find_element_by_xpath('//h1[text()="Chocolate lollipop oat cake modified"]')
        assert article_title.text == "Chocolate lollipop oat cake modified"

    # Test7 - cikk törlése - belépés után a New Article gombra kattintás, új cikk létrehozása, majd törlés után
    # annak ellenőrzése, hogy a megjelenő My Articles listában egyik cikknek a címe sem egyezik a létrehozott cikk
    # címével // a cikk aloldalán nem jelenik meg a delete gomb
    def test_delete_article(self):
        self.test_create_new_article()

        delete_btn = WebDriverWait(
            self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, ('//button[@class="btn btn-outline-danger btn-sm"]')))
        )
        delete_btn.click()

        time.sleep(3)
        self.driver.find_element_by_xpath('//a[@href="#/@Tester15@gmail.com/"]').click()
        time.sleep(3)
        article_title = self.driver.find_elements_by_xpath('//h1')[-1]
        # assert "Chocolate lollipop oat cake" not in article_titles
        assert article_title != "Chocolate lollipop oat cake"

    # Test8 - adatok kilistázása - belépés után a lorem cimkére kattintás, a lorem cimkével rendelkező cikkek
    # kilistázódnak, ezután összehasonlítom a kapott lista hosszát (1-et kivonva belőle a conduit h1-es elem miatt) az
    # olyan lorem cimkét tartalmazó lista hosszával, amik megtalálhatók a kilistázott cikkek között
    def test_listing_data(self):
        self.test_login()
        time.sleep(5)
        self.driver.find_element_by_xpath('//a[@href="#/tag/lorem"]').click()
        time.sleep(5)
        listed_articles = self.driver.find_elements_by_tag_name('h1')
        # for i in listed_articles:
        #     if i.text == 'conduit':
        #         continue
        #     title = i.text

        articles_with_lorem_tag = self.driver.find_elements_by_xpath(
            '//div[@class="article-preview"]//a[@href="#/tag/lorem"]')
        assert len(listed_articles) - 1 == len(articles_with_lorem_tag)

    # Test9 - adatok kimentése - belépés után létrehozom a Global Feedben található cikkek listáját, a listában
    # található cikkek felületen megjelenő adatait beleiratom egy articles_preview nevű text fájlba, ezután a txt fájl
    # tartalmát soronként kiolvasom, leellenőrzöm, hogy az első sor testuser1-e
    def test_saving_data(self):
        self.test_login()
        time.sleep(5)
        articles_preview = self.driver.find_elements_by_xpath('//div[@class="article-preview"]')

        with open("articles_preview.txt", "w") as txt1:
            for i in articles_preview:
                txt1.write(f"{i.text}")

        with open("articles_preview.txt", "r") as txt1:
            txt2 = txt1.readlines()
            # print(txt2, end='')
            for line in txt2:
                print(line, end='')
                # assert line[1] == "testuser1"

    # Test10 - lapozás - belépés után létrehozok egy listát, amelyben a page-link osztálynevű lapozó gombok vannak,
    # a lista elemein for ciklussal végigmegyek, majd megkeresem az utosló lapozó gombot, ami a lenti attribútumokkal
    # rendelkezik, ellenőrzöm, hogy a gomb szövege 2-e
    def test_pagination(self):
        self.test_login()
        time.sleep(3)

        page_numbers = self.driver.find_elements_by_class_name("page-link")
        for i in page_numbers:
            i.click()

        time.sleep(3)
        last_page_number = self.driver.find_element_by_xpath(
            '//li[@class="page-item active" and @data-test="page-link-2"]')
        assert last_page_number.text == "2"

    # Test11 - ismételt és sorozatos adatbevitel - belépés után az első cikket megkeressük a Global Feedben és
    # rákattintunk, létrehozunk egy num nevű változót 0 értékkel, egy for ciklusban a komment mezőbe egymás után 5 db
    # kommentet létrehozunk, különböző szövegekkel, amiket leellenőrzünk, majd töröljük a létrehozott kommenteket / 1es és 3as bennemarad
    def test_sequential_data_input_from_csv(self):
        self.test_login()
        time.sleep(3)

        self.driver.find_elements_by_xpath('//h1')[1].click()
        time.sleep(3)

        with open('./test/comments.csv', 'r', encoding="UTF-8") as c_file:
            file_table = csv.reader(c_file, delimiter=',')
            for row in file_table:
                self.driver.find_element_by_xpath('//textarea').send_keys(row)
                self.driver.find_element_by_xpath('//button[text()="Post Comment"]').click()
                time.sleep(3)

        assert self.driver.find_elements_by_xpath('//p[@class="card-text"]')[0].text == "Comment5"

    # Test12 - ismételt és sorozatos adatbevitel - belépés után az első cikket megkeressük a Global Feedben és
    # rákattintunk, létrehozunk egy num nevű változót 0 értékkel, egy for ciklusban a komment mezőbe egymás után 5 db
    # kommentet létrehozunk, különböző szövegekkel, amiket leellenőrzünk, majd töröljük a létrehozott kommenteket / 1es és 3as bennemarad
    def test_sequential_data_input(self):
        self.test_login()
        time.sleep(3)

        self.driver.find_elements_by_xpath('//h1')[1].click()
        time.sleep(3)

        num = 0
        for i in range(5):
            self.driver.find_element_by_xpath('//textarea').send_keys(f"Comment {num}")
            self.driver.find_element_by_xpath('//button[text()="Post Comment"]').click()
            time.sleep(3)
            assert self.driver.find_element_by_xpath('//p[@class="card-text"]').text == (f"Comment {num}")
            num += 1
