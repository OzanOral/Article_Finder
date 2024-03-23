from exceptiongroup import catch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime
from config import query_with_FA_Title as query
from config import API_KEY
from serpapi import GoogleSearch

driver = webdriver.Chrome()

def make_search(driver, title):
    driver.get("https://pubmed.ncbi.nlm.nih.gov")
    elem = driver.find_element(By.ID, "id_term")
    elem.clear()
    elem.send_keys(title)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)

def split_query(each):
    splited_text = each.split("AND")
    title = splited_text[0][1:-8]
    fa = splited_text[1][1:-9]
    fa_surname = fa.split(" ")[-1]
    return title,fa_surname

def gather_info(driver):
    try:
        article_doi = driver.find_element(By.CLASS_NAME,"id-link").text
        article_journal = driver.find_element(By.ID, "full-view-journal-trigger").text
        journal_date = driver.find_element(By.CLASS_NAME,"cit").text
        first_author = driver.find_element(By.CLASS_NAME,"full-name").text
        pubmed_id = driver.find_element(By.CLASS_NAME,"current-id").text
    except:
        pubmed_id = driver.find_element(By.CLASS_NAME,"current-id").text
        article_doi, article_journal, journal_date, first_author = "NaN", "NaN", "NaN", "NaN"
    return article_doi, article_journal, journal_date, first_author, pubmed_id

def gather_info_serpapi(search):
    title_result, doc_type, link, summary, author, cited_by, author_match= "NaN", "NaN", "NaN", "NaN", "NaN", 0, 0
    results = search.get_dict()
    first_query = results["organic_results"][0] if "organic_results" in results else {}
    title_result = first_query.get("title", "NaN")
    doc_type = first_query.get("type", "NaN")
    link = first_query.get("link", "NaN")
    publication_info = first_query.get("publication_info", {})
    summary = publication_info.get("summary", "NaN")
    author = publication_info.get("authors", [{}])[0].get("name", "NaN")
    if first_author.lower() in author.lower():
        author_match = 1
    cited_by = first_query.get("inline_links", {}).get("cited_by", {}).get("total", "NaN")
    return title_result, doc_type, link, summary, author, cited_by, author_match

result_list=[]
for each in query:

    title, first_author = split_query(each)
    make_search(driver, title)
    if "search results" not in driver.title.lower():
        author_list = driver.find_element(By.CLASS_NAME, "authors-list").text.lower()
    else:
        author_list = []
    
    article_doi, article_journal, journal_date, first_author_pubmed, pmid = "NaN",  "NaN",  "NaN",  "NaN",  "NaN"
    if first_author.lower() not in author_list:
        docsums = driver.find_elements(By.CLASS_NAME,"docsum-content")
        for docsum in docsums:
            if first_author.lower() in docsum.text.lower():
                a = docsum.text
                b = a.find("PMID")
                pmid = a[b:b+15]
                break
    else:
        article_doi, article_journal, journal_date, first_author_pubmed,pmid = gather_info(driver)


    params = {
        "api_key": API_KEY,
        "engine": "google_scholar",
        "q": title
    }

    search = GoogleSearch(params)
    title_serpapi, doc_type, link, summary, author, cited_by, author_match = gather_info_serpapi(search)

    f_result = f"{title_serpapi}\t {doc_type}\t {link}\t {summary}\t {author}\t {cited_by}\t {author_match}\t {article_doi}\t {article_journal}\t {journal_date}\t {first_author_pubmed}\t {pmid}\n"
    result = {
    "title_serpapi": title_serpapi,
    "doc_type": doc_type,
    "link": link,
    "summary": summary,
    "author": author,
    "cited_by": cited_by,
    "author_match": author_match,
    "article_doi": article_doi,
    "article_journal": article_journal,
    "journal_date": journal_date,
    "first_author_pubmed": first_author_pubmed,
    "pmid": pmid
}
    result_list.append(result)
    with open('githubversion_results.txt', 'a') as f:
       f.write(f_result)
f.close()



 
