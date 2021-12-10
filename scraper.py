import requests
from bs4 import BeautifulSoup as bs

### FUNCTIONS
def get_names(url, element_type, class_search_term, multiple_pages=False):
    """Function to get page or pages and find the names of UFRF professors - may refactor later to be reusable"""
    if multiple_pages:
        page_number = 1
        page = requests.get(f'{url}{page_number}')
        pages = []

        while page.status_code == 200:
            print(f'{url}{page_number}')
            print(f'Page {page_number} added')
            pages.append(page)
            page_number += 1
            page = requests.get(f'{url}{page_number}')

        print(f'Could not find page {page_number}')

    else:
        page = requests.get(url)
        pages = [page]

    names=[]

    for p in pages:
        soup = bs(p.content, "html.parser")
        results = soup.find_all(element_type, class_=class_search_term)
        for result in results:
            names.append(result.text)
    return names

def get_years(start, end, url, element_type, class_search_term, multiple_pages=False):
    """Uses get_names to get multiple years worth of UFRF professors"""
    all_names = []
    while start <= end:
        print(start)
        if not multiple_pages:
            regular_url = f'{url}{start}'
            for item in get_names(regular_url, element_type, class_search_term, multiple_pages):
                all_names.append(item)
        else:
            multi_page_url = f'{url}{start}/page/'
            for item in get_names(multi_page_url, element_type, class_search_term, multiple_pages):
                all_names.append(item)
        start += 1
    return all_names


### MAIN PROGRAM

# Variables
url = "https://ufrfprofessors.research.ufl.edu/category/"
search_type = "h3"
search_name = "limoking-blog-title"

# Get results
results = get_years(2017, 2020, url, search_type, search_name, True)
print(results)

# Write results
if results:
    print("Writing results to file")
    with open("results.txt", "w+") as myfile:
        for result in results:
            myfile.write(f'{result} \n\n')
            

        

