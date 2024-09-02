import os.path
import time
import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup():
    # Configure Chrome options to automatically allow camera, microphone, and location permissions
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.geolocation": 1
    })

    # serv = Service("C:\\Users\\b.rakesh\\Driver\\chromedriver-win64/chromedriver.exe")
    serv = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=serv, options=opt)

    yield driver  # Provide the fixture value to tests
    # time.sleep(1)
    # Teardown - close the browser session
    driver.quit()

