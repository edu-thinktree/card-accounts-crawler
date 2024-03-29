# 베이스 이미지로 ubuntu:16.04 사용 
FROM ubuntu:16.04

# 메인테이너 정보 (옵션)
MAINTAINER eshell "eshell@naver.com"

# 환경변수 설정 (옵션)
# ENV PATH /usr/local/bin:$PATH
ENV LANG C.UTF-8

# 기본 패키지들 설치 및 Python 3.6 설치
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:fkrull/deadsnakes
RUN apt-get update

# python 설치
RUN apt-get install -y --no-install-recommends python3 python3-pip python3-dev 

# pip 업그레이드
RUN python3 -m pip install pip --upgrade

# wget 설치
RUN apt-get install -y wget

# Set up the Chrome PPA
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Update the package list and install chrome
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable 

# python3 setuptools 설치
RUN apt-get install -y python3-setuptools
Run pip install --upgrade pip setuptools wheel requests

WORKDIR /app

ADD requirements.txt    /app/
RUN pip install -r requirements.txt

ADD ./chromedriver          /app/chromedriver
ADD ./_crawling.py          /app/
ADD ./parser.py              /app/