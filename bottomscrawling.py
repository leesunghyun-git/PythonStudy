import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import oracledb as db

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

list_tabs = [51]  # 예시: bags

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

for a in list_tabs:
    genders = ["men","women","kids"]
    for TYPE in genders:
        url = f"https://kream.co.kr/search?tab={a}&gender={TYPE}"
        driver.get(url)
        time.sleep(2)

        # 조금씩 스크롤하면서 500개 수집
        scroll_pause_time = 0.5
        collected_urls = set()
        last_height = driver.execute_script("return document.body.scrollHeight")

        while len(collected_urls) < 700:
            items = driver.find_elements(By.CSS_SELECTOR, "a.item_inner")
            for item in items:
                collected_urls.add(item.get_attribute("href"))
            if len(collected_urls) >= 700:
                break
            driver.execute_script("window.scrollBy(0, 700);")  # 조금씩 스크롤
            time.sleep(scroll_pause_time)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                same_count=0
                same_count += 1
                if same_count >= 5:  # 5번 연속으로 변화 없으면 종료
                    break
            else:
                same_count = 0  # 다시 로딩되면 초기화
            last_height = new_height

        # 최대 500개만 선택
        item_urls = list(collected_urls)[:700]
        print(len(item_urls))
        for url in item_urls:
            driver.get(url)
            time.sleep(1)
            try:
                detail = driver.find_elements(By.CSS_SELECTOR,'div.product_info')
                RELEASE_PRICE = detail[0].text if len(detail) > 0 else ""   # 출시가
                SKU = detail[1].text if len(detail) > 1 else ""  # 제품번호
                RELEASE_DATE = detail[2].text if len(detail) > 2 else "" # 출시일
                COLOR = detail[3].text if len(detail) > 3 else "" # 대표 색
            except:
                RELEASE_PRICE = SKU = RELEASE_DATE = COLOR = "" # 예외처리 -> null

            try:
                IMG = driver.find_element(By.CSS_SELECTOR,'img.image.full_width[alt*="대표 이미지"]').get_attribute("src") # 이미지
            except:
                IMG = ""

            try:
                RT_PRICE = int(driver.find_element(By.CSS_SELECTOR,'span.price-info').text.replace(",","")) # 최근 거래가
            except:
                RT_PRICE = 0

            try:
                NAME_KOR = driver.find_element(By.CSS_SELECTOR,'p.sub-title').text # 한국이름
            except:
                NAME_KOR = ""

            try:
                NAME_ENG = driver.find_element(By.CSS_SELECTOR,'p.title').text #영어 이름
            except:
                NAME_ENG = ""

            try:
                BRAND = driver.find_element(By.CSS_SELECTOR,'p.title-text').text # 브랜드
            except:
                BRAND = ""

            try:
                VARIANCE = driver.find_element(By.CSS_SELECTOR,'div.fluctuation').text #판매가 등폭
            except:
                VARIANCE = ""

            try:
                nowprices = driver.find_elements(By.CSS_SELECTOR,'div.price span.amount em.num')
                IM_SELL = int(nowprices[0].text.replace(",","")) if len(nowprices) > 0 else 0 # 현재 판매가
                IM_BUY = int(nowprices[1].text.replace(",","")) if len(nowprices) > 1 else 0 # 현재 구매가
            except:
                IM_SELL = IM_BUY = 0

            try:
                BOOKMARK = parse_bookmark(driver.find_element(By.CSS_SELECTOR,'span[class="wish_count_num"]').text) # 구독
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

conn.commit()
driver.quit()