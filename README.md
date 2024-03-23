# Article_Finder - PubMed and Google Scholar Search Automation 


This project automates the process of searching for scientific articles on PubMed and Google Scholar, extracting relevant information, and compiling it into a text file. It uses Selenium for web scraping and the SerpAPI to query Google Scholar, aiming to assist researchers in gathering data for literature reviews or meta-analyses.


Getting Started
These instructions will guide you on setting up your local machine to run the script and how to customize it for your research needs.

Prerequisites
Python 3.x
Selenium
SerpApi

Output
The output will be saved in a file named githubversion_results.txt in the root directory. Each line of the file contains tab-separated values of the following information:

Title from SerpAPI
Document type
Link to the article
Summary
Author
Number of times cited
Author match indicator
Article DOI
Journal name
Publication date
First author according to PubMed
PubMed ID (PMID)
Customizing the Script
You can customize the script by editing the queries in the config.py file or by modifying the main_script.py to adjust which information is collected and how it's processed.

Troubleshooting
Ensure your Chrome WebDriver version matches your Chrome browser's version.
Verify that your SerpAPI key is valid and has not exceeded its request limit.
Contributing
Contributions to improve the script or extend its capabilities are welcome. Please feel free to fork the repository and submit pull requests.

License
This project is licensed under the MIT License - see the LICENSE file for details.
