from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
import pandas as pd

url = "https://www.youtube.com/channel/videos"
driver = webdriver.Chrome()
driver.get(url)

def scroll():
    SCROLL_PAUSE_TIME = 4

    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, arguments[0]);", last_height)

        time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def get_titles():
    scroll()
    try:
        titles = driver.find_elements(By.ID, "video-title")
    except:
        return ""
    return titles

def get_views():
    try:
        views = driver.find_elements(By.XPATH,'//*[@id="metadata-line"]/span[1]')
    except:
        return ""
    return views

def get_video():
    try:
        video = driver.find_elements(By.ID, "video-title-link")
    except:
        return ""
    return video

def create_df():
    titles = get_titles()
    views = get_views()
    video = get_video()

    data = []
    urls = [] # Aqui ficam armazenadas as URLS de TODOS os vídeos do canal.

    for i, j, k in zip(titles, views, video):
        data.append([i.text, j.text, k.get_attribute("href")])
        urls.append(k.get_attribute("href"))

    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns = ["Title", "Views", "Url"])
    df.to_csv('youtube_videos_details.csv')

def main():
    get_titles()
    get_views()
    get_titles()
    create_df()

main()
driver.quit()