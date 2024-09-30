import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from anticaptchaofficial.recaptchav2proxyless import *

class AdvancedScraperBot:
    def __init__(self, base_url, vpn_config=None):
        self.base_url = base_url
        self.vpn_config = vpn_config
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.setup_driver()

    def setup_driver(self):
        chrome_options = Options()
        if self.vpn_config:
            chrome_options.add_argument(f'--proxy-server={self.vpn_config["proxy"]}')
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)

    def fetch_page(self, url):
        self.driver.get(url)
        self.handle_captcha()
        return self.driver.page_source

    def handle_captcha(self):
        try:
            captcha_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "g-recaptcha"))
            )
            if captcha_element:
                site_key = captcha_element.get_attribute("data-sitekey")
                solver = recaptchaV2Proxyless()
                solver.set_verbose(1)
                solver.set_key(#Anticapchaapikey)
                solver.set_website_url(self.driver.current_url)
                solver.set_website_key(site_key)

                response = solver.solve_and_return_solution()
                if response != 0:
                    self.driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{response}";')
                    submit_button = self.driver.find_element_by_css_selector("input[type='submit']")
                    submit_button.click()
                else:
                    print("Failed to solve CAPTCHA")
        except:
            print("No CAPTCHA found or unable to solve")

    def parse_page(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        # Implement your parsing logic here
        # For example, let's extract all paragraph texts
        paragraphs = soup.find_all('p')
        return [p.text for p in paragraphs]

    def save_to_csv(self, data, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Content'])  # Header
            for item in data:
                writer.writerow([item])

    def run(self, num_pages=1):
        all_data = []
        for i in range(num_pages):
            url = f"{self.base_url}/page/{i+1}"
            html = self.fetch_page(url)
            data = self.parse_page(html)
            all_data.extend(data)
            print(f"Scraped page {i+1}")
            sleep(random.uniform(1, 3))  # Random delay between requests
        
        self.save_to_csv(all_data, 'scraped_data.csv')
        print("Scraping completed. Data saved to scraped_data.csv")
        self.driver.quit()

# Usage example
if __name__ == "__main__":
    vpn_config = {
        "proxy": "#httpsyourproxy"
    }
    bot = AdvancedScraperBot("https://example.com", vpn_config)
    bot.run(num_pages=5)
