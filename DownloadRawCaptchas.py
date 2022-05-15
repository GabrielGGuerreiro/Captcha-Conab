import requests
from bs4 import BeautifulSoup

for i in range(0,300):
    html = requests.get('https://sisdep.conab.gov.br/precosiagroweb/', allow_redirects=True)
    soup = BeautifulSoup(html.text)
    img = soup.select_one('img[src*="captcha.php"]')
    captchaURL = 'https://sisdep.conab.gov.br'+ img['src']
    r = requests.get(captchaURL, allow_redirects=True)
    open(fr'Captcha-Conab\RawCaptchas\captcha-{i}.png', 'wb').write(r.content)