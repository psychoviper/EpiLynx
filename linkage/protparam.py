import requests
from bs4 import BeautifulSoup


def fetch_instability(seq):
    url='https://web.expasy.org/cgi-bin/protparam/protparam'
    payload={
        'sequence': seq
    }
    response = requests.post(url, data=payload)

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    instability_tag = soup.find('strong', string='Instability index:')
    if instability_tag:
        instability_text = instability_tag.next_sibling
        if instability_text:
            instability_value = instability_text.split()[8]  # Should extract "108.68" from "108.68 This classifies the protein as unstable."
            print(f'Instability Index: {instability_value}')
            return instability_value
        else:
            print('Instability index value not found.')
            return 100000
    else:
        print('Instability index tag not found.')
        return 100000