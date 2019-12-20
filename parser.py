from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

TEST_URL = 'https://www.cardsales.or.kr/signin'


service = webdriver.chrome.service.Service('chromedriver/chromedriver')
service.start()
options = webdriver.ChromeOptions()

options.add_argument('headless')
options.add_argument('window-size=2500x1080')
options.add_argument("disable-gpu")
options.add_argument('--no-sandbox')
options.add_argument("--disable-setuid-sandbox")
# 시험지 3~4장 출력 후 멈춤 현상 - 크롬에서 /tmp 디렉토리를 대신 사용한다. 메모리 대신 디스크가 사용됨으로 실행 속도가 느려질 수 있다.
options.add_argument('--disable-dev-shm-usage')
options.add_argument("lang=ko_KR")  # 한국어!

# options.add_argument(
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36")


options = options.to_capabilities()
# 유의: chromedriver를 위에서 받아준
# chromdriver(windows는 chromedriver.exe)의 절대경로로 바꿔주세요!


driver = webdriver.Remote(service.service_url, options)


driver.get(TEST_URL)
driver.implicitly_wait(3)
driver.get(TEST_URL)


# 플러그인 있는 걸로 속이기
# driver.execute_script(
#     "Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")
# lanuages 속성을 업데이트해주기
# driver.execute_script(
#     "Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
# 그래픽카드가 있는 척
# driver.execute_script(
#     "const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")

driver.implicitly_wait(3)

# 화면 스크린 샷
driver.get_screenshot_as_file('card_main.png')
# user_agent = driver.find_element_by_css_selector('#user-agent').text
# plugins_length = driver.find_element_by_css_selector('#plugins-length').text
# languages = driver.find_element_by_css_selector('#languages').text
# webgl_vendor = driver.find_element_by_css_selector('#webgl-vendor').text
# webgl_renderer = driver.find_element_by_css_selector('#webgl-renderer').text

# print('User-Agent: ', user_agent)
# print('Plugin length: ', plugins_length)
# print('languages: ', languages)
# print('WebGL Vendor: ', webgl_vendor)
# print('WebGL Renderer: ', webgl_renderer)

driver.quit()
