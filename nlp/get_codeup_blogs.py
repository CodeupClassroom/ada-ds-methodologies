import requests
from bs4 import BeautifulSoup

urls = [
        "https://codeup.com/why-san-antonio-has-more-than-tacos-to-offer/",
        "https://codeup.com/codeups-data-science-career-accelerator-is-here/",
        "https://codeup.com/data-science-vs-data-analytics-whats-the-difference/",
        "https://codeup.com/10-tips-to-crush-it-at-the-sa-tech-job-fair/",
        "https://codeup.com/competitor-bootcamps-are-closing-is-the-model-in-danger/",
    ]

def get_response(url):
    headers = {'User-Agent': 'Codeup Ada Data Science'}
    response = requests.get(url, headers=headers)
    return response

def get_codeup_blog_post(url):
    response = get_response(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find("h1").contents[0]
    content = soup.find("div", class_="mk-single-content").get_text()
    content = content.replace("\n", "")
    content = content.replace("\t", "")
    return {
        "title": title,
        "content": content
    }

# get all articles w/ list comprehension
def get_blog_articles():    
    return [get_codeup_blog_post(url) for url in urls]
