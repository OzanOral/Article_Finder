from exceptiongroup import catch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from config import query_with_FA_Title as query

def make_search(driver, title):
    driver.get("https://pubmed.ncbi.nlm.nih.gov")
    assert "PubMed" in driver.title
    elem = driver.find_element(By.ID, "id_term")
    elem.clear()
    elem.send_keys(title)
    elem.send_keys(Keys.RETURN)
    time.sleep(5)
    print(driver.title)

def split_query(each):
    splited_text = each.split("AND")
    title = splited_text[0][1:-8]
    fa = splited_text[1][1:-9]
    fa_surname = fa.split(" ")[-1]
    return title,fa_surname

def gather_info(driver):
    article_doi = driver.find_element(By.CLASS_NAME,"id-link").text
    article_journal = driver.find_element(By.ID, "full-view-journal-trigger").text
    journal_date = driver.find_element(By.CLASS_NAME,"cit").text
    first_author = driver.find_element(By.CLASS_NAME,"full-name").text
    return article_doi, article_journal, journal_date, first_author


driver = webdriver.Firefox()

for each in query:
    title, fa_surname = split_query(each)
    make_search(driver, title)
    article_doi, article_journal, journal_date, first_author = " "," "," "," "
    try:
        print(driver.find_element(By.XPATH,"/html/body/main/div[9]/div[2]/div[2]/div[1]/div[1]/h3/span"))
    except:
        pass
    try: 
        authors_list = driver.find_elements(By.CLASS_NAME, "full-name")
        for author in authors_list:
            if fa_surname in author.text:
                article_doi, article_journal, journal_date, first_author = gather_info(driver)
                  
        with open('NewVersion/Results_Selenium.txt', 'a') as f:
            f.write(title + "\t" + first_author + "\t" + article_journal + "\t" + journal_date + "\t" + article_doi + "\n")
    except:
        with open('NewVersion/Results_Selenium.txt', 'a') as f:
            f.write(title + "\t" + driver.current_url + "\n")
    
driver.close()

"""
        if driver.find_element(By.CLASS_NAME,"publication-type").text == "Comment":
            driver.find_element(By.CLASS_NAME,"docsum-title").click()
            time.sleep(5)
            article_doi = driver.find_element(By.CLASS_NAME,"id-link").text
            article_journal = driver.find_element(By.ID, "full-view-journal-trigger").text
            journal_date = driver.find_element(By.CLASS_NAME,"cit").text
            first_author = driver.find_element(By.CLASS_NAME,"full-name").text  


"""