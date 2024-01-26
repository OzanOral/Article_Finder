from exceptiongroup import catch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from config import all_titles_reviewed as query

start_time = datetime.now().strftime("%H:%M:%S")
print("Current Time =", start_time)

driver = webdriver.Firefox()
for each in query:
    driver.get("https://pubmed.ncbi.nlm.nih.gov")
    assert "PubMed" in driver.title
    elem = driver.find_element(By.ID, "id_term")
    elem.clear()
    elem.send_keys(each)
    elem.send_keys(Keys.RETURN)
    time.sleep(5)
    print(driver.title)
    try:
        if "Search" in driver.title:
            driver.find_element(By.CLASS_NAME,"docsum-title").click()
    except:
        pass
    try: 
        article_doi = driver.find_element(By.CLASS_NAME,"id-link").text
        article_journal = driver.find_element(By.ID, "full-view-journal-trigger").text
        journal_date = driver.find_element(By.CLASS_NAME,"cit").text
        first_author = driver.find_element(By.CLASS_NAME,"full-name").text

        if driver.find_element(By.CLASS_NAME,"publication-type").text == "Comment":
            driver.find_element(By.CLASS_NAME,"docsum-title").click()
            time.sleep(5)
            article_doi = driver.find_element(By.CLASS_NAME,"id-link").text
            article_journal = driver.find_element(By.ID, "full-view-journal-trigger").text
            journal_date = driver.find_element(By.CLASS_NAME,"cit").text
            first_author = driver.find_element(By.CLASS_NAME,"full-name").text

        with open('try.txt', 'a') as f:
            f.write(each + "\t" + first_author + "\t" + article_journal + "\t" + journal_date + "\t" + article_doi + "\n")
    except:
        with open('try.txt', 'a') as f:
            f.write(each + "\t" + driver.current_url + "\n")
    
driver.close()

finish_time = datetime.now().strftime("%H:%M:%S")
print(f"Current Time= {finish_time}")