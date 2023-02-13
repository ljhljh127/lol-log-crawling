---

### 전체적인 설명

[OP.GG](http://OP.GG) 기반으로 파이선 Selenium을 이용하여 크롤링하여 최근 게임의 승패 여부와 KDA를 표시하여 준다.

Docker를 이용하여 크롤링에 필요한 환경을 구축 할 수 있다.

---

### 도커파일에 대한 설명

도커파일은 다음과 같이 이루어져 있다.

```docker
FROM ubuntu
LABEL maintainer="Lee.J.H"
RUN apt-get update\
    && apt-get upgrade -y\
    && apt-get install wget python3 python3-pip -y \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb\
    && apt -y install ./google-chrome-stable_current_amd64.deb\
    && pip install selenium \
    && pip install webdriver-manager

Copy ./test.py
```

1. **FROM** 명령어로 ubuntu 기반의 이미지를 지정하였다.
2. **LABEL** 명령어로 이미지의 메타데이터를 지정하였으며 maintainer를 지정하는데 사용하였다.
3. ******RUN****** 명령어로 **ubuntu** 이미지로부터의 쉘 스크립트를 실행하게 된다.

 먼저 **apt-get update**와 **apt-get upgrade**를 통하여 새로운 버전을 확인 및 최신화 시킨다.

 다음으로 크롤링에 필요한 파일들을 다운받아준다.

- **wget 패키지(링크 기반으로 파일을 다운 받을 수 있게 해줌)**
- **python3 패키지**
- **python3-pip 패키지(파이썬 패키지 라이브러리 관리→패키지 import할 외부 패키지 가져 오는데 이용)**
1. 다운받은 **wget**을 이용하여 리눅스 최신 버전의 크롬을 다운 받아준다.
2. 다운받은 크롬을 설치한다.
3. 파이썬 패키지 관리자를 이용하여 selenium과 크롬 웹드라이버 매니저를 받아준다.
4. 데스크탑의 test.py코드를 도커 이미지로 복사한다.

---

### 도커파일은 다음과 같이 실행한다.

**docker run -it --name (컨테이너명) testimage2 python3 test.py**

실행결과

![image](https://user-images.githubusercontent.com/43638794/218352951-3af9ef7d-a35f-4ecf-bc26-0445e2b875d7.png)
