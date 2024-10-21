import requests
import pickle
from bs4 import BeautifulSoup
from Countries import all_countries

dictionary = {}
countries_with_data = []
for country in all_countries:
    country = '-'.join(country[1].split(',')[0].split())
    URL = f"https://www.16personalities.com/country-profiles/{country}"
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    try:
        page = s.get(URL)
    except:
        continue
    soup = BeautifulSoup(page.content, "html.parser")


    title = soup.find("title")
    if "Oops!" in title.text:    
        continue
    
    print(country)
    countries_with_data.append(country)
    country_elements = soup.find("div", class_="country-individual")
    pupolation = "".join(country_elements.find("div", class_="info-panel").find_all("div", class_="demographics")[0].find_all("span")[1].text.split(","))
    respondent = "".join(country_elements.find("div", class_="info-panel").find_all("div", class_="demographics")[1].find_all("span")[1].text.split(","))
    top_personaliy = (eval(str(country_elements.find("div", class_="panel types").find("country-profiles-top-ten-list")).split("[")[1].split("]")[0]))


    dictionary[country] = {
        "pupolation": pupolation,
        "respondent": respondent,
        "top_personaliy": top_personaliy
    }

dictionary["countries"] = countries_with_data
Country_file = open('Countries_Data_Mined', 'wb') 
pickle.dump(dictionary, Country_file) 
Country_file.close() 

