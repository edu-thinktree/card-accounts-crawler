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
    # HTTP POST request: �α����� ���� POST url�� �Բ� ���۵� data�� �־�����.
    login_req = s.post('https://www.cardsales.or.kr/signin',
                       headers=headers, data=LOGIN_INFO)
    # � ����� ���ñ��?
    print(login_req.status_code)

    # �α����� ���� ������ ��� ����ݽô�.
    if login_req.status_code != 200:
        raise Exception('�α����� ���� �ʾҾ��! ���̵�� ��й�ȣ�� �ٽ��ѹ� Ȯ���� �ּ���.')

    post_dayApproval = s.get(
        'https://www.cardsales.or.kr/page/approval/day', headers=headers)

    # Soup���� ����� �ݽô�.
    dayApproval_soup = bs(post_dayApproval.text, 'html.parser')

    button = dayApproval_soup.find("button", {"id": "searchBtn"})

    print(dayApproval_soup)
