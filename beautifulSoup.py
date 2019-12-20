import sys
import requests
from bs4 import BeautifulSoup as bs

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}


userID = sys.argv[1]
password = sys.argv[2]
# year = sys.argv[3]
# month = sys.argv[4]
# day = sys.argv[5]

LOGIN_INFO = {
    'userId': userID,
    'userPass': password
}

with requests.Session() as s:
    # HTTP POST request: 로그인을 위해 POST url와 함께 전송될 data를 넣어주자.
    login_req = s.post('https://www.cardsales.or.kr/signin',
                       headers=headers, data=LOGIN_INFO)
    # 어떤 결과가 나올까요?
    print(login_req.status_code)

    # 로그인이 되지 않으면 경고를 띄워줍시다.
    if login_req.status_code != 200:
        raise Exception('로그인이 되지 않았어요! 아이디와 비밀번호를 다시한번 확인해 주세요.')

    post_dayApproval = s.get(
        'https://www.cardsales.or.kr/page/approval/day', headers=headers)

    # Soup으로 만들어 줍시다.
    dayApproval_soup = bs(post_dayApproval.text, 'html.parser')

    button = dayApproval_soup.find("button", {"id": "searchBtn"})

    print(dayApproval_soup)
