import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    # Set up the WebDriver using WebDriver Manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    # Tear down (close the browser)
    driver.quit()

def test_google_search(driver):
    # Step 1: Open Google
    driver.get("https://www.google.com")
    driver.maximize_window()
    print("Opened Google.")

    # Step 2: Locate the search box, enter a query, and submit
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    print("Search query submitted.")

    # Step 3: Wait for the results page to load
    driver.implicitly_wait(3)

    # Step 4: Extract and print the titles of the search results
    search_results = driver.find_elements(By.CSS_SELECTOR, 'h3')
    print("Search results:")
    for index, result in enumerate(search_results):
        print(f"{index + 1}. {result.text}")

    # Assert that at least one result is found
    assert len(search_results) > 0, "No search results found."
