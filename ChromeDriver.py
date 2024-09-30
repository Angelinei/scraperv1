from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Automatically download and set up ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open Google.com
driver.get("https://www.google.com")

# Close the browser
driver.quit()
