from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json 
import collections

def tree():
    return collections.defaultdict(tree)

driver = webdriver.Chrome('/usr/local/bin/chromedriver')


def rating_list_crawler(desired_):
    page_number = 660
    while(page_number != desired_):
        
        for i in range(1, 11):
            driver.get("https://movie.naver.com//movie/bi/mi/pointWriteFormList.nhn?code=121048&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={}".format(page_number)) 

            f = open("amsal/rate/{}.txt".format(((page_number-1)*10)+i), "w")
            
            req = requests.get(driver.current_url)
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')  
            css_select = "body > div > div > div.score_result > ul > li:nth-child({}) > div.score_reple > dl > dt > em:nth-child(1) > a > span".format(i)
            user_name_list = soup.select('body > div > div > div.score_result > ul > li > div.score_reple > dl > dt > em > a > span')
            user_name = user_name_list[i-1].text
            driver.find_element_by_css_selector(css_select).click()
            user_req = requests.get(driver.current_url)
            user_html = user_req.text
            user_soup = BeautifulSoup(user_html, 'html.parser')  
            
            data_list = []
            table = user_soup.find('table', attrs={'class':'list_netizen'})
            table_body = table.find('tbody')

            rows = table_body.find_all('tr')
            for row in rows:
                points = row.find_all('td', attrs={'class':'point'})
                i=0
                for a in points:
                    data_list.append(a.text)
            data_modi =""
            for i in data_list:
                data_modi = data_modi + i + " " 
            print(data_modi)
            f.write(str(data_modi))
        page_number += 1 

if __name__ == "__main__":
    rating_list_crawler(3901)