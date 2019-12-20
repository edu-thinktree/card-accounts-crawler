# -*- coding: euc-kr -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
timeout = 10


def login2(driver):
    # ���̵�/��й�ȣ�� �Է����ش�.
    driver.find_element_by_name('userId').send_keys('jaurim73')
    driver.find_element_by_name('userPass').send_keys('5569')

    # �α��� ��ư�� ��������.
    try:
        element_login = EC.element_to_be_clickable(
            (By.XPATH, "//input[@type='image']"))
        WebDriverWait(driver, timeout).until(element_login)
        driver.find_element_by_xpath("//input[@type='image']").click()
        print("�α����� ���������� �̷�������ϴ�.")
    except TimeoutException:
        print(
            "�α��� ���� - �������� �ε��ϱ� ���� ���ð��� ������ ")
        driver.quit()


def login(driver, id, password):
    # ���̵�/��й�ȣ�� �Է����ش�.
    # j_username
    driver.find_element_by_id('j_username').send_keys(id)
    driver.find_element_by_id('j_password').send_keys(password)

    # �α��� ��ư�� ��������.
    try:
        element_login = EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="goLogin"]'))
        WebDriverWait(driver, timeout).until(element_login)
        driver.find_element_by_xpath('//*[@id="goLogin"]').click()
        print("�α����� ���������� �̷�������ϴ�.")
    except TimeoutException:
        print(
            "�α��� ���� - �������� �ε��ϱ� ���� ���ð��� ������ ")
        driver.quit()
