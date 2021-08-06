import time


def conduit_registration(driver):

    driver.find_element_by_xpath('//a[@href="#/register"]').click()
    driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys("Tester11@gmail.com")
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("Tester11@gmail.com")
    driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Tester11@gmail.com")
    time.sleep(3)
    driver.find_element_by_xpath('//button').click()
    time.sleep(3)
    driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]').click()
