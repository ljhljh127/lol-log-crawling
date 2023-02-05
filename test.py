import time,os,shutil
from selenium import webdriver
from selenium.webdriver.common.by import By

name=input("소환사 이름을 입력해 주세요")
game=int(input('최근 몇 게임의 전적을 출력할까요?'))
 ##메인 웹페이지 연결
driver = webdriver.Chrome(f"{os.getcwd()}/chromedriver.exe")
driver.implicitly_wait(100)
driver.get("https://www.op.gg/")
element= driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/form/div[2]/input')
element.send_keys(f"{name}")
element.submit()
excep1=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/h2')
if name.isalnum():
    if excep1.text=="OP.GG에 등록되지 않은 소환사입니다. 오타를 확인 후 다시 검색해주세요.":
        print("사용자 이름이 존재하지 않습니다.")
        driver.close()
    else:
        print(name+f"님의 최근{game}번 게임 전적입니다(최신순)\n")
        for i in range(1,game+1):
            gt=driver.find_element(By.XPATH,f'/html/body/div[1]/div[6]/div[2]/div[3]/li[{i}]/div/div[1]/div/div[1]/div[1]')
            gr=driver.find_element(By.XPATH,f'/html/body/div[1]/div[6]/div[2]/div[3]/li[{i}]/div/div[1]/div/div[1]/div[4]')
            gs=driver.find_element(By.XPATH,f'/html/body/div[1]/div[6]/div[2]/div[3]/li[{i}]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]')
            print(f"{i}번째 게임의 결과\n게임타입:"+gt.text+"\n결과:"+gr.text+"\n"+gs.text+"\n\n")
        driver.close()
else:
    print("이름에 특수문자가 존재합니다.")