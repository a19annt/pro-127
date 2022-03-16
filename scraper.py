from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv


Start_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome(executable_path=r"C:\Users\Rajesh sharma\Desktop\Whitehat\python\projects\pro-127\chromedriver.exe")
browser.get(Start_URL)
time.sleep(10)

def scrape():
    headers = ["Name", "Distance", "Mass", "Radius"]
    brightest_star = []
    for i in range(0, 198):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for table_tag in soup.find_all("table", attrs={"class", "wikitable sortable jquery-tablesorter"}):
            td_tags = table_tag.find_all("td")
            temp_list = []
            for index, td_tag in enumerate(td_tags):
                if index == 0:
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
            brightest_star.append(temp_list)
    with open("data.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(brightest_star)
        
scrape()