from bs4 import BeautifulSoup
from flask import jsonify
import requests
from lxml import html

def get_data():
    url = "https://guvenilirgida.tarimorman.gov.tr/GuvenilirGida/GKD/DataTablesList"

    payload = "draw=1&columns%5B0%5D%5Bdata%5D=DuyuruTarihi&columns%5B0%5D%5Bname%5D=DuyuruTarihi&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=FirmaAdi&columns%5B1%5D%5Bname%5D=FirmaAdi&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=Marka&columns%5B2%5D%5Bname%5D=Marka&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=UrunAdi&columns%5B3%5D%5Bname%5D=UrunAdi&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=Uygunsuzluk&columns%5B4%5D%5Bname%5D=Uygunsuzluk&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=PartiSeriNo&columns%5B5%5D%5Bname%5D=PartiSeriNo&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=FirmaIlce&columns%5B6%5D%5Bname%5D=FirmaIlce&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=FirmaIl&columns%5B7%5D%5Bname%5D=FirmaIl&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=UrunGrupAdi&columns%5B8%5D%5Bname%5D=UrunGrupAdi&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=desc&start=0&length=200&search%5Bvalue%5D=&search%5Bregex%5D=false&KamuoyuDuyuruAra.IdariYaptirimYasalDayanakIdler=2%2C20&KamuoyuDuyuruAra.IdariYaptirimYasalDayanakId=&SiteYayinDurumu=True&KamuoyuDuyuruAra.DuyuruTarihi=&_KamuoyuDuyuruAra_UrunGrupId=&KamuoyuDuyuruAra.UrunGrupId=&Order%5B0%5D%5Bcolumn%5D=DuyuruTarihi&Order%5B0%5D%5Bdir%5D=desc"
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-GB,en;q=0.9,ru;q=0.8,tr;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'Dil479=1; __RequestVerificationToken=xs1acMR4IIcy9jjjBAerrso9Z4GZTpjQ-kIEVvxN_5TEwzN6aw8rjl73xAgTFtM61mnwlelN6V1KBs9DZO9axgHhzZM1; TS01fe2271=016f66f15eef6d4df18587cdc84957fef82236c1cfe3f5ba122b0e7853b120e45993d81e3b1167470e9a0cf9cfb0b50f847d4c6d76801fb0e0e815cecaf986102d6f3cf87c16515f6f50ccd614fbc74d7312f3bfb3; Dil479=1; TS01fe2271=016f66f15e94bd99c98a769beff314cdd3270f0187e8e7a018c6d81315c2326983eaab890cd42dbd656b175449b536876b868a1e1167ab958e5d6c3b35e01eb21b0d5a6580',
        'Origin': 'https://guvenilirgida.tarimorman.gov.tr',
        'Pragma': 'no-cache',
        'Referer': 'https://guvenilirgida.tarimorman.gov.tr/GuvenilirGida/gkd/SagligiTehlikeyeDusurecek?siteYayinDurumu=True',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return response.content


def get_data2():
    url = "https://www.tarimorman.gov.tr/GKGM/Link/40/Gidada-Dogru-Bilgi"

    response = requests.get(url)
    response.encoding = 'utf-8'  

    soup = BeautifulSoup(response.content, 'html.parser')
    accordion_groups = soup.find_all('div', class_='acc-group')

    results = []
    for accordion in accordion_groups:
        for heading in accordion.find_all('div', id=lambda x: x and x.startswith('heading')):
            title = heading.get_text(strip=True)
            content_div = heading.find_next_sibling('div', class_='collapse')
            content = content_div.find('div', class_='content').get_text(strip=True)

            content = content.replace('\u200b', '').strip()
            content = content.replace('\u011f', 'ğ').replace('\u00e7', 'ç').replace('\u0131', 'ı')
            content = content.replace('\u00f6', 'ö').replace('\u00fc', 'ü').replace('\u015f', 'ş')
            content = content.replace('\u0130', 'İ').replace('\u00c7', 'Ç').replace('\u011e', 'Ğ')

            results.append({'title': title, 'content': content})

    for item in results:
        print(f"Title: {item['title']}\nContent: {item['content']}\n")

    return jsonify(results)

