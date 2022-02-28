#scraping using beautiful soup
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/#country"
html_page = requests.get(url).text
soup = BeautifulSoup(html_page,'html_parser')
get_table = soup.find("table",id="main_table_countries_today")
get_table_data = get_table.tbody.find_all("tr")

dic{}
for i in range(len(get_table_data)):
	try:
		key = get_table_data[i].find_all("a", href = True)[0].string
	except:
		key = geT_table_data[i].find_all("td")[0].string
	values = [j.string for j in get_table_data[i].find_all("td")]
	dic[key] = values
live_data = pd.DataFrame(dic).drop([14,15,16,17,18,19,20,21]).iloc[2:,1:].T
live_data.columns = ["Total Cases","New Cases", "Total Deaths", "New Deaths", "Total Recovered", "New Recovered", "Active", "Serious Critical", "Tot Cases/1M pop",
		     "Deaths /1M pop", "Total Test", "Tests /1M pop]
print(live_data)
