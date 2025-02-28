from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from db import get_db_connection

def scrape_lazada():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Chạy trình duyệt ẩn
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    url = "https://www.lazada.vn/catalog/?q=điện%20thoại"
    driver.get(url)
    time.sleep(3)

    products = driver.find_elements(By.CSS_SELECTOR, ".Bm3ON")
    data = []

    for product in products[:10]:  # Giới hạn lấy 10 sản phẩm
        try:
            title = product.find_element(By.CSS_SELECTOR, ".RfADt").text
            price = product.find_element(By.CSS_SELECTOR, ".ooOxS").text
            data.append({"name": title, "price": price})
        except:
            continue

    driver.quit()
    return data

def save_to_db(data):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        for product in data:
            cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", 
                           (product["name"], product["price"]))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    products = scrape_lazada()
    save_to_db(products)
