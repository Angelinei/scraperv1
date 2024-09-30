# scraperv1
Scraper web v1 code source with Anti-Captcha, VPN Proxy - Personnal Project #NonCommercial

This scraper is a first version for a personal project. 1 main problem here : GDPR, heres why you really need to consider it as a school project. I need to work more on this aspect because an Anti-Captcha (https://anti-captcha.com/) API is integrated - I didn't let mine - as other elements because it's for you to configure (vpn proxy - OpenVPN as I work on Windows - for example or URL concerned - really basic version but perfect to start as a newbie like me)

Disclaimer : I'm workin' on Windows I let you the file (you need to do first in the terminal pip install selenium and webdriver-manager : 

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Automatically download and set up ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

#Open Google.com - Exemple
driver.get("https://www.google.com")

#Close the browser
driver.quit()

So adapt to the OS you working with

Enjoy and I'm open for feedbacks :)
