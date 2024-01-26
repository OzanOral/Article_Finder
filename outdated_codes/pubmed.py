import requests
import xml.etree.ElementTree as ET

def get_pubmed_records():
    # Define the database and query parameters
    db = 'pubmed'
    query = 'KRAS+Mutation+Is+Present+in+a+Small+Subset+of+Primary+Urinary+Bladder+Adenocarcinomas'

    # Base URL for NCBI E-utilities
    base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'

    # ESearch URL assembly
    esearch_url = f'{base}esearch.fcgi?db={db}&term={query}&usehistory=y'

    # Post the ESearch URL and get the output
    esearch_output = requests.get(esearch_url).text

    # Parse WebEnv and QueryKey
    root = ET.fromstring(esearch_output)
    web_env = root.findtext('WebEnv')
    query_key = root.findtext('QueryKey')

    # ESummary URL assembly and posting
    esummary_url = f'{base}esummary.fcgi?db={db}&query_key={query_key}&WebEnv={web_env}'
    docsums = requests.get(esummary_url).text
    print(docsums)

    # EFetch URL assembly and posting
    efetch_url = f'{base}efetch.fcgi?db={db}&query_key={query_key}&WebEnv={web_env}&rettype=abstract&retmode=text'
    data = requests.get(efetch_url).text
    print(data)

# Call the function to get PubMed records
get_pubmed_records()