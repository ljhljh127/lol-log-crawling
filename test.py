import time,os,shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

name="퀸은오늘도달린다"
game=int(input('최근 몇 게임의 전적을 출력할까요?'))
 ##메인 웹페이지 연결
driver = webdriver.Chrome(f"{os.getcwd()}/chromedriver.exe")
driver.implicitly_wait(100)
driver.get("https://fow.kr/")
element= driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/form/div/input[2]')
element.send_keys(f"{name}")
element.submit()
solorank=driver.find_element(By.XPATH,'/html/body/div[5]/div[1]/div[1]/div[16]/a[2]/span')
solorank.click()
print(name+f"님의 최근{game}번 게임 전적입니다(최신순)\n")
for i in range(1,game+1):
    gr=driver.find_element(By.XPATH,f'/html/body/div[5]/div[1]/div[1]/div[18]/table[2]/tbody/tr[{i}]/td[1]')
    grc=driver.find_element(By.XPATH,f'/html/body/div[5]/div[1]/div[1]/div[18]/table[2]/tbody/tr[{i}]/td[2]/div/div/b')
    grs=driver.find_element(By.XPATH,f'/html/body/div[5]/div[1]/div[1]/div[18]/table[2]/tbody/tr[{i}]/td[4]/font/b')
    print(f"최근 전적 {i}번 결과:"+gr.text+"\n플레이 한 챔피언:"+grc.text+"\n"+grs.text+"\n")

driver.close()