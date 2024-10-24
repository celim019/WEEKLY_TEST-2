import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to the CSV file
csv_file_path = '/mnt/data/online_shopping.csv'

# Set up the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Open the target website
driver.get('https://example-online-shopping-site.com')

# Wait for the page to load
time.sleep(3)

# Read the CSV file
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        # Example fields: Adjust the locators and row keys based on the actual website and CSV structure
        search_box = driver.find_element(By.NAME, 'search')  # Name of search box
        search_box.clear()
        search_box.send_keys(row['Product Name'])
        search_box.send_keys(Keys.RETURN)
        
        time.sleep(2)  # Wait for the page to load search results
        
        # Add additional actions to select items, fill in details, etc.
        # For example, click the first product in search results
        product = driver.find_element(By.CSS_SELECTOR, 'div.product-item a')
        product.click()
        
        time.sleep(2)  # Wait for the product page to load
        
        # Example: Add to cart
        add_to_cart_button = driver.find_element(By.ID, 'add-to-cart')
        add_to_cart_button.click()
        
        time.sleep(2)  # Wait for the item to be added to the cart
        
        # Navigate back to search for the next item
        driver.back()
        time.sleep(2)

# Close the browser
driver.quit()
