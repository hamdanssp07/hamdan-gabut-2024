import os
import sys
import requests

# Meminta pengguna untuk memasukkan Video ID
AngivLink = input('Video ID Fx 7136376173239520539 -> ')

# URL target
url = "https://homedecoratione.com/v4.php"

# Header untuk permintaan HTTP
hat = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-length': '52',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'PHPSESSID=c1a15a17a74a3c4fa17d859ce3e3cc90; n=1',
    'origin': 'https://homedecoratione.com',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

# Data payload
date = {
    '0429a': 'tok_free',
    'af49f': 'views',
    '9a898': AngivLink  # Nilai dari AngivLink yang dimasukkan oleh pengguna
}

# Loop tak terbatas
while True:
    tiktoker = requests.post(url, data=date, headers=hat)
    print("Succesfully Booted the Video Response ->", tiktoker)
