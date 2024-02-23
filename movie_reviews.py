from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json 
import collections
    
def tree():
    return collections.defaultdict(tree)

def crawling(desire_):
    with open("/amsal/review_list.json", "w", encoding='utf-8') as write_file:
        page_number = 1
        number = 1
        while(page_number!=desire_):
            driver.get("https://movie.naver.com//movie/bi/mi/pointWriteFormList.nhn?code=121048&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}".format(page_number)) 
            req = requests.get(driver.current_url)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')

            review_list = soup.select('body > div > div > div > ul > li > div > p')
            rating_list = soup.select('body > div > div > div.score_result > ul > li > div.star_score > em')
            date_list = soup.select('body > div > div > div.score_result > ul > li > div.score_reple > dl > dt')

            for a, b, c in zip(review_list,rating_list,date_list):
                data = tree()
                id = c.text.split()[0]
                date = c.text.split()[1] + " " + c.text.split()[2]
                data['no'] = number
                data['id'] = id
                data['review'] = str(a.text)
                data['rating'] = str(b.text)
                data['date'] = date
            
                data_list.append(data)
                number = number + 1
            page_number = page_number + 1
        json.dump(data_list, write_file, ensure_ascii=False, indent=3)

if __name__ == "__main__":
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    data_list = []
    crawling(3901)