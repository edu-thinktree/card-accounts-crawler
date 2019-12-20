### 실행

도커이미지 만들기

```
docker build -t card_accounts .
```

도커이미지 실행

```
docker run --rm --volume=$(pwd):/app/ card_accounts python3 paser.py <사용자 아이디> <비밀번호> 2019 12 12
```
