from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def scrape_prairie_learn_data():
    options = Options()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-infobars')
    options.add_argument('--incognito')

    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    wait = WebDriverWait(driver, 10)

    driver.get("https://us.prairielearn.com/pl/login")
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "University of Illinois Urbana-Champaign (UIUC)"))).click()
    time.sleep(random.uniform(4, 6))
    wait.until(EC.presence_of_element_located((By.NAME, "loginfmt"))).send_keys("[email]") # replace with actual email
    time.sleep(random.uniform(2, 3))
    driver.find_element(By.ID, "idSIButton9").click()
    time.sleep(random.uniform(4, 6))
    wait.until(EC.presence_of_element_located((By.NAME, "passwd"))).send_keys("[password]")  # replace with actual password
    time.sleep(random.uniform(2, 4))
    driver.find_element(By.ID, "idSIButton9").click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table[aria-label='Courses'] tbody tr td")))

    table = driver.find_element(By.CSS_SELECTOR, "table[aria-label='Courses']")
    rows = table.find_elements(By.TAG_NAME, "tr")

    courses = []
    links = []
    for row in rows:
        link_element = row.find_element(By.TAG_NAME, "a")
        course_name = link_element.text.strip().split(':')[0]
        course_link = link_element.get_attribute("href")
        courses.append(course_name)
        links.append(course_link)

    assignments = {}
    for course in courses:
        assignments[course] = []
    
    for i in range(len(links)):
        time.sleep(2)
        c, l = courses[i], links[i]
        driver.get(l)
        time.sleep(2)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-sm.table-hover[aria-label='Assessments']")))
        time.sleep(2)
        tab = driver.find_element(By.CSS_SELECTOR, ".table.table-sm.table-hover[aria-label='Assessments']")
        trs = tab.find_elements(By.TAG_NAME, "tr")
        for tr in trs:
            tds = tr.find_elements(By.TAG_NAME, "td")
            if tds:
                try:
                    span = tds[0].find_element(By.TAG_NAME, "span")
                    code = span.text

                    try:
                        a = tds[1].find_element(By.TAG_NAME, "a")
                        link = a.get_attribute('href')
                        name = a.text.strip()
                    except NoSuchElementException:
                        link = None
                        name = "No link available"

                    due = tds[2].text.strip()

                    if len(due) > 10 and "100%" in due:
                        assignments.setdefault(c, []).append((code, link, name, due))
                except Exception as e:
                    print(f"Error processing assignment in course {c}: {e}")

    driver.quit()
    return assignments
