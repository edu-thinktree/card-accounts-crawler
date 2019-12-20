# -*- coding: euc-kr -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
timeout = 10


def login2(driver):
    # 아이디/비밀번호를 입력해준다.
    driver.find_element_by_name('userId').send_keys('jaurim73')
    driver.find_element_by_name('userPass').send_keys('5569')

    # 로그인 버튼을 눌러주자.
    try:
        element_login = EC.element_to_be_clickable(
            (By.XPATH, "//input[@type='image']"))
        WebDriverWait(driver, timeout).until(element_login)
        driver.find_element_by_xpath("//input[@type='image']").click()
        print("로그인이 성공적으로 이루어졌습니다.")
    except TimeoutException:
        print(
            "로그인 실패 - 페이지를 로드하기 위한 대기시간이 지났음 ")
        driver.quit()


def login(driver, id, password):
    # 아이디/비밀번호를 입력해준다.
    # j_username
    driver.find_element_by_id('j_username').send_keys(id)
    driver.find_element_by_id('j_password').send_keys(password)

    # 로그인 버튼을 눌러주자.
    try:
        element_login = EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="goLogin"]'))
        WebDriverWait(driver, timeout).until(element_login)
        driver.find_element_by_xpath('//*[@id="goLogin"]').click()
        print("로그인이 성공적으로 이루어졌습니다.")
    except TimeoutException:
        print(
            "로그인 실패 - 페이지를 로드하기 위한 대기시간이 지났음 ")
        driver.quit()
