# Setup
from serpapi import GoogleSearch
from config import API_KEY, query_with_FA_Title as query_year
from datetime import datetime


# Queries
titles = query_year[:5]
start_time = datetime.now().strftime("%H:%M:%S")
print("Current Time =", start_time)


# Search for each query
for title in titles:
    # Parameters for the SerpApi request
    params = {
        "api_key": API_KEY,
        "engine": "google_scholar",
        "q": title
    }

    # Default values for variables to be extracted
    doc_type, link, summary, author, inline_links, total = "NaN", "NaN", "NaN", "NaN", "No info", 0

    # Perform the Google Scholar search
    search = GoogleSearch(params)
    results = search.get_dict()
    first_query = results["organic_results"][0] if "organic_results" in results else {}

    # Extract information from the first result
    title = first_query.get("title", "NaN")
    doc_type = first_query.get("type", doc_type)
    link = first_query.get("link", link)
    
    publication_info = first_query.get("publication_info", {})
    summary = publication_info.get("summary", "NaN")
    author = publication_info.get("authors", [{}])[0].get("name", "NaN")

    # Check if there are inline links
    inline_links = "1" if "inline_links" in first_query else "No info"
    total = first_query.get("inline_links", {}).get("cited_by", {}).get("total", "NaN")

    # Record the information
    f_result = f"{title}\t {doc_type}\t {link}\t {summary}\t {author}\t {inline_links}\t {total}\n"
    print(f_result)
    
    # Write the information to a file
    if "Alexander" in summary:
        with open('Results_Selenium.txt', 'a') as f:
            f.write(f_result)


finish_time = datetime.now().strftime("%H:%M:%S")
print(f"Current Time= {finish_time}")