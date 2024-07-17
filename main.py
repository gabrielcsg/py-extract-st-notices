'''
    
    Data: 2024-07-06
    Created by: Gabriel Castro.
    Github: https://github.com/gabrielcsg

'''

from bs4 import BeautifulSoup
import pandas as pd
import re
import requests

DATE_PATTERN = r'\d{2}/\d{2}/\d{4}'


def extract_items(content_list):
    items_formatted = []
    for row in content_list.find_all("li"):
        category = row.find("div").text.strip()
        title = row.find("h2").text.strip()
        description = row.find("p").text.strip().split(" \n\n")[0]
        link = base_url + row.find("p").find("span").find("a").attrs['href']

        dates = row.find_all("span", attrs={"class": "details"})[0].text
        published_at = re.search(DATE_PATTERN, dates.split(",")[0]).group()
        updated_at = re.search(DATE_PATTERN, dates.split(",")[1]).group()

        items_formatted.append({
            "category": category,
            "title": title,
            "description": description,
            "link": link,
            "published_at": published_at,
            "updated_at": updated_at,

        })

    return items_formatted


print("-> Initializing extraction...")
base_url = "https://serratalhada.pe.gov.br"
notices_url = f"{base_url}/transparencia/publicacoes/index/processos-seletivos"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(notices_url, headers=headers)

notices_list = []

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    pages = soup.find_all(
        "div", attrs={"class": "paginator"})[0].find("p").text.split(" ")[-1]
    list = soup.find_all(name="ul", attrs={"id": "posts-list"})[0]

    notices_list = extract_items(list)

    for page in range(2, int(pages)+1):
        url = f"{notices_url}?page={page}"
        new_page_response = requests.get(url, headers=headers)

        if new_page_response.status_code == 200:
            soup = BeautifulSoup(new_page_response.content, 'html.parser')
            new_page_list = soup.find_all(
                name="ul", attrs={"id": "posts-list"})[0]

            page_list = extract_items(new_page_list)
            notices_list = notices_list + page_list

print(f"-> Completed extraction with {len(notices_list)} items.")


# Load
notices_df = pd.DataFrame(notices_list, index=False)
notices_dt = notices_df.sort_values("updated_at", ascending=False)
notices_df.to_excel("editais-serra-talhada.xlsx", encoding='utf-8')
print("File 'editais-serra-talhada.xlsx' generated successfully!")
