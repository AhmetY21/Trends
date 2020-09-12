# import time
from selenium import webdriver


# from selenium.webdriver.common.keys import Keys

def down_trends(query1, son_bir, son_bes, start_date, end_date, geo1):
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory": 'C:\Kullanıcılar\Ahmet YÜKSEL\Desktop\Trends\down_trends'}
    chromeOptions.add_experimental_option("prefs", prefs)
    chromedriver = r'C:\Users\Ahmet YÜKSEL\Downloads\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
    base = "https://trends.google.com/trends/explore"
    driver.get(f"{base}")
    query = f"q={query1}"
    geo = f"geo={geo1}"
    if (son_bir == "1"):
        url = f"{base}?{query}&{geo}"
    elif son_bes == "1":
        url = f"{base}?date=today%205-y&{geo}&{query}"
    else:
        date = f"date={start_date}%20{end_date}"
        url = f"{base}?{date}&{geo}&{query}"

    driver.get(f"{base}")

    driver.get(url)

    driver.implicitly_wait(5)  # may need to implicitly wait longer on slow connections
    button = driver.find_element_by_class_name('export')
    button.click()

