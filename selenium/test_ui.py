from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_home_page():

    options = Options()

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("http://localhost:5000")

        assert "DevOps Security Demo" in driver.title

        assert "DevOps Testing & Security Demo" in driver.page_source

    finally:
        driver.quit()
