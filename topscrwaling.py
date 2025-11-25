import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import oracledb as db

def crwaling(a):
    # Oracle 연결
    conn = db.connect(
        user="hr",
        password="happy",
        dsn="localhost:1521/XE"
    )
    cur = conn.cursor()

    # 테이블/시퀀스/카테고리 매핑
    ct_dict = {50:"tops",51:"bottoms",63:"bags"}
    seq_dict = {50:"tops_id_seq.nextval",51:"bts_id_seq.nextval",63:"bags_id_seq.nextval"}
    ctn_dict = {50:2,51:3,63:4}

    # 크롬 드라이버
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    def parse_bookmark(s):
        """북마크 문자열을 숫자로 변환"""
        try:
            s = s.strip()
            if "만" in s:
                num = float(s.replace("만", "")) * 10000
            else:
                num = float(s.replace(",", ""))
            return int(num)
        except:
            return 0

    genders = ["men","women","kids"]
    for TYPE in genders:
        url = f"https://kream.co.kr/search?tab={a}&gender={TYPE}"
        driver.get(url)
        time.sleep(2)

        # 스크롤하면서 아이템 수집
        scroll_pause_time = 0.7
        collected_elements = set()
        last_height = driver.execute_script("return document.body.scrollHeight")
        same_count = 0

        while len(collected_elements) < 100:
            items = driver.find_elements(By.CSS_SELECTOR, "a.item_inner")
            for item in items:
                collected_elements.add(item)
            if len(collected_elements) >= 100:
                break
            driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(scroll_pause_time)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                same_count += 1
                if same_count >= 5:
                    break
            else:
                same_count = 0
            last_height = new_height

        # 최대 100개 아이템 선택
        item_elements = list(collected_elements)[:100]
        i=1
        for item in item_elements:
            try:
                
                print(i)
                # 새 탭에서 클릭
                driver.execute_script("window.open(arguments[0].href);", item)
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(5)

                # 상세페이지 데이터 수집
                try:
                    detail = driver.find_elements(By.CSS_SELECTOR,'div.product_info')
                    RELEASE_PRICE = detail[0].text if len(detail) > 0 else ""   
                    SKU = detail[1].text if len(detail) > 1 else ""  
                    RELEASE_DATE = detail[2].text if len(detail) > 2 else "" 
                    COLOR = detail[3].text if len(detail) > 3 else "" 
                except:
                    RELEASE_PRICE = SKU = RELEASE_DATE = COLOR = "" 

                try:
                    IMG = driver.find_element(By.CSS_SELECTOR,'img.image.full_width[alt*="대표 이미지"]').get_attribute("src")
                except:
                    IMG = ""
                try:
                    RT_PRICE = int(driver.find_element(By.CSS_SELECTOR,'span.price-info').text.replace(",",""))
                except:
                    RT_PRICE = 0
                try:
                    NAME_KOR = driver.find_element(By.CSS_SELECTOR,'p.sub-title').text
                except:
                    NAME_KOR = ""
                try:
                    NAME_ENG = driver.find_element(By.CSS_SELECTOR,'p.title').text
                except:
                    NAME_ENG = ""
                try:
                    BRAND = driver.find_element(By.CSS_SELECTOR,'p.title-text').text
                except:
                    BRAND = ""
                try:
                    VARIANCE = driver.find_element(By.CSS_SELECTOR,'div.fluctuation').text
                except:
                    VARIANCE = ""
                try:
                    nowprices = driver.find_elements(By.CSS_SELECTOR,'div.price span.amount em.num')
                    IM_SELL = int(nowprices[0].text.replace(",","")) if len(nowprices) > 0 else 0
                    IM_BUY = int(nowprices[1].text.replace(",","")) if len(nowprices) > 1 else 0
                except:
                    IM_SELL = IM_BUY = 0
                try:
                    BOOKMARK = parse_bookmark(driver.find_element(By.CSS_SELECTOR,'span[class="wish_count_num"]').text)
                except:
                    BOOKMARK = 0

                # 데이터 INSERT
                data = (NAME_KOR, NAME_ENG, IMG, BRAND, SKU, COLOR, TYPE, VARIANCE, RELEASE_DATE,
                        RELEASE_PRICE, RT_PRICE, IM_SELL, IM_BUY, BOOKMARK, ctn_dict[a])
                sql = "INSERT INTO "+ct_dict[a]+" (GOODS_ID,NAME_KOR,NAME_ENG,IMG,BRAND,SKU,COLOR,TYPE,VARIANCE,RELEASE_DATE,RELEASE_PRICE,RT_PRICE,IM_SELL,IM_BUY,BOOKMARK,CATEGORY_ID) VALUES( "+seq_dict[a]+", :1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15)"
                try:
                    cur.execute(sql, data)
                except Exception as e:
                    print(f"INSERT 실패: {e}")
                i+=1

            finally:
                # 탭 닫고 메인 탭으로
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

    conn.commit()
    driver.quit()

crwaling(50)
crwaling(51)
crwaling(63)
