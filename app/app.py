# from flask import Flask, render_template
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

# app = Flask(__name__)

# def get_lazada_data():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")  # Chạy trình duyệt ẩn nếu cần
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)

#     url = "https://www.lazada.vn/catalog/?q=điện%20thoại"
#     driver.get(url)

#     products = driver.find_elements(By.CSS_SELECTOR, ".Bm3ON")
#     data = []

#     for product in products[:10]:  # Giới hạn lấy 10 sản phẩm
#         try:
#             title = product.find_element(By.CSS_SELECTOR, ".RfADt").text
#             price = product.find_element(By.CSS_SELECTOR, ".ooOxS").text
#             img = product.find_element(By.CSS_SELECTOR, "img").get_attribute("src")
#             link = product.find_element(By.TAG_NAME, "a").get_attribute("href")
#             data.append({"title": title, "price": price, "img": img, "link": link})
#         except:
#             continue

#     driver.quit()
#     return data

# @app.route("/")
# def home():
#     products = get_lazada_data()
#     return render_template("index.html", products=products)

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template
# from db import get_db_connection

# app = Flask(__name__)

# def get_products():
#     conn = get_db_connection()
#     with conn.cursor() as cursor:
#         cursor.execute("SELECT name, price FROM products")
#         products = cursor.fetchall()
#     conn.close()
#     return products

# @app.route("/")
# def index():
#     products = get_products()
#     return render_template("index.html", products=products)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)


from flask import Flask, render_template
from db import get_db_connection

app = Flask(__name__)

def get_products():
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT name, price FROM products")  # Chỉ lấy name và price
        products = cursor.fetchall()
    conn.close()
    return products

@app.route("/")
def index():
    products = get_products()
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
