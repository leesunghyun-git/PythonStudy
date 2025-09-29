import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import oracledb as db
conn = db.connect(
    user="hr",
    password="happy",
    dsn="localhost:1521/XE"
)
cur=conn.cursor()
ct_dict = {50:"tops",51:"bottoms",63:"bags"}
seq_dict = {50:"tops_id_seq.nextval",51:"bts_id_seq.nextval",63:"bags_id_seq.nextval"}
type_dict = {"men":"남자","women":"여자","kids":"키즈"}
ctn_dict={50:2,51:3,63:4}
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
list = [63]
def parse_bookmark(s):
    s = s.strip()  # 앞뒤 공백 제거
    if "만" in s:
        # '1.7만' -> 1.7 * 10000
        num = float(s.replace("만", "")) * 10000
    else:
        # 그냥 숫자
        num = float(s.replace(",", ""))
    return int(num)
for a in list:
    sex = ["men","women","kids"]
    for TYPE in sex:
        url = "https://kream.co.kr/search?tab="+str(a)+"&gender="+TYPE
        driver.get(url)

         # 페이지 전체 높이  

        # 조금씩 스크롤
        scroll_pause_time = 0.4
        scroll_step = 500   # px 단위

        current_position = 0
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            items = driver.find_elements(By.CSS_SELECTOR, "a.item_inner")
            new_height = driver.execute_script("return document.body.scrollHeight")
            if len(items) >= 500:
                break
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        
        item_urls = [item.get_attribute("href") for item in items]
        for url in item_urls:
            print(url)
            driver.get(url)
            time.sleep(5)
            detail = driver.find_elements(By.CSS_SELECTOR,'div.product_info')
        
            RELEASE_PRICE=detail[0].text
            SKU=detail[1].text
            RELEASE_DATE=detail[2].text
            COLOR=detail[3].text

            
            IMG=driver.find_element(By.CSS_SELECTOR,'img.image.full_width[alt*="대표 이미지"]').get_attribute("src")
            RT_PRICE=int(driver.find_element(By.CSS_SELECTOR,'span.price-info').text.replace(",",""))
            NAME_KOR=driver.find_element(By.CSS_SELECTOR,'p.sub-title').text
            NAME_ENG=driver.find_element(By.CSS_SELECTOR,'p.title').text
            BRAND=driver.find_element(By.CSS_SELECTOR,'p.title-text').text
            VARIANCE=driver.find_element(By.CSS_SELECTOR,'div.fluctuation').text
            nowprices=driver.find_elements(By.CSS_SELECTOR,'div.price span.amount em.num')
            IM_SELL=int(nowprices[0].text.replace(",",""))
            IM_BUY=int(nowprices[1].text.replace(",",""))
            BOOKMARK=parse_bookmark(driver.find_element(By.CSS_SELECTOR,'span[class="wish_count_num"]').text)
            data = (NAME_KOR, NAME_ENG, IMG, BRAND, SKU, COLOR, TYPE, VARIANCE, RELEASE_DATE, RELEASE_PRICE, RT_PRICE, IM_SELL, IM_BUY, BOOKMARK, ctn_dict[a])
            sql = "INSERT INTO "+ct_dict[a]+"(GOODS_ID,NAME_KOR,NAME_ENG,IMG,BRAND,SKU,COLOR,TYPE,VARIANCE,RELEASE_DATE,RELEASE_PRICE,RT_PRICE,IM_SELL,IM_BUY,BOOKMARK,CATEGORY_ID) VALUES("+seq_dict[a]+",:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15)"
            cur.execute(sql,data)
            
conn.commit()

