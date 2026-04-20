import pandas as pd
import os
import requests
from datetime import datetime

def generate_yml():
    csv_url = os.getenv('CSV_URL')
    df = pd.read_csv(csv_url)
    
    date_now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    
    yml = f'<?xml version="1.0" encoding="UTF-8"?>\n'
    yml += f'<yml_catalog date="{date_now}">\n'
    yml += f'  <shop>\n'
    yml += f'    <name>Alamat Domiki</name>\n'
    yml += f'    <company>Alamat Domiki</company>\n'
    yml += f'    <url>https://alamatdomiki.ru</url>\n'
    yml += f'    <currencies><currency id="RUR" rate="1"/></currencies>\n'
    yml += f'    <categories><category id="1">Аренда домиков</category></categories>\n'
    yml += f'    <offers>\n'
    
    for _, row in df.iterrows():
        yml += f'      <offer id="{row["id"]}">\n'
        yml += f'        <name>{row["name"]}</name>\n'
        yml += f'        <url>{row["url"]}</url>\n'
        yml += f'        <price>{row["price"]}</price>\n'
        yml += f'        <currencyId>RUR</currencyId>\n'
        yml += f'        <categoryId>1</categoryId>\n'
        yml += f'        <picture>{row["picture"]}</picture>\n'
        yml += f'        <description>{row["description"]}</description>\n'
        yml += f'      </offer>\n'
        
    yml += f'    </offers>\n  </shop>\n</yml_catalog>'
    
    os.makedirs('public', exist_ok=True)
    with open('public/yandex-feed.xml', 'w', encoding='utf-8') as f:
        f.write(yml)

if __name__ == "__main__":
    generate_yml()
