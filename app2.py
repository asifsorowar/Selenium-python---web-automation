# automation with selenium.
# asifsorowar
# code - 2
# in this app2.py we can print all video title in youtube.com containers [locating elements from html]


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://www.youtube.com')


# selenium will wait for 10 sec to find or match element.
# if not find, then the driver will quit in except
try:
    contents = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'contents'))
    )

    videoCards = contents.find_elements_by_tag_name('ytd-rich-item-renderer')
    for videoCard in videoCards:
        videoTitle = videoCard.find_element_by_id(
            'video-title-link')

        print(videoTitle.text)

finally:
    driver.quit()
