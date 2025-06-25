import requests
from bs4 import BeautifulSoup

def get_vix_value():
    url = 'https://fred.stlouisfed.org/series/VIXCLS'  # URL of the page containing the VIX in FRED / dayly update
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Looking for the VIX value in the page
        vix_value = soup.find('span', {'class': 'series-meta-observation-value'})
        if vix_value:
            return vix_value.text.strip()
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    vix_value = get_vix_value()
    if vix_value:
        print(f"VIX: {vix_value}")
    else:
        print("No se pudo obtener el valor del VIX")