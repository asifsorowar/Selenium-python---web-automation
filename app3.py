# automation with selenium.
# asifsorowar
# code - 3
# page navigating and  clicking elements

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://www.youtube.com')

# code - 1
# try:
#     youtubeLibrary = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, 'Library'))
#     )
#     youtubeLibrary.click()
# except:
#     driver.quit()
# finally:
#     time.sleep(5)
#     driver.quit()


# code - 2
# try:
#     search = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//input[@id="search"]'))
#     )
#     search.send_keys('i love bangladesh')
#     search.send_keys(Keys.RETURN)

#     contents = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'contents'))
#     )
#     videoCards = contents.find_elements_by_tag_name('ytd-video-renderer')
#     videoCards[0].click()
# except:
#     driver.quit()
# finally:
#     time.sleep(5)
#     driver.quit()


# code - 3
try:
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@id="search"]'))
    )
    search.send_keys('i love bangladesh')
    search.send_keys(Keys.RETURN)

    contents = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'contents'))
    )
    videoCards = contents.find_elements_by_tag_name('ytd-video-renderer')
    for index, videoCard in enumerate(videoCards):
        if (index > 3):
            break

        time.sleep(2)
        videoCard.click()
        time.sleep(2)
        driver.back()

except:
    driver.quit()
finally:
    driver.quit()
