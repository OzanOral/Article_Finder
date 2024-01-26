from exceptiongroup import catch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from config import query_with_FA_Title as query

def split_query(each):
    splited_text = each.split("AND")
    title = splited_text[0][1:-8]
    fa = splited_text[1][1:-9]
    fa_surname = fa.split(" ")[-1]
    return title,fa_surname

driver = webdriver.Firefox()
for each in query:
    title, first_author_surname = split_query(each)
    driver.get("https://pubmed.ncbi.nlm.nih.gov")
    assert "PubMed" in driver.title
    elem = driver.find_element(By.ID, "id_term")
    elem.clear()
    elem.send_keys(title)
    elem.send_keys(Keys.RETURN)
    time.sleep(5)
    print(driver.title)


    
"""
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
print(f"Current Time= {finish_time}")"""