import requests
from bs4 import BeautifulSoup
import utils 

def crawl_index_page():
    url = "https://www.psu.edu"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract content from the homepage
    content = soup.get_text()

    #Print Content
    print(content)

    # Save to index.txt file
    utils.save_to_file('C:/Users/Zeel Prajapati/Project/PennState/Data/psu_website/index.txt', content)
    
if __name__ == "__main__":
    crawl_index_page()