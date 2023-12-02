# Youtube Web Scraper

This is a tool for scraping youtube channels.

# Installing

First, clone this repository using
```
git clone https://github.com/levycamoes/youtube-web-scraper.git
```
Install the requirements:
```
pip install -r requirements.txt
```
Now you should be ready to scrape!

# Getting Started
After installing all the requirements, you can run the "web_scraper_channel.py" file to get the following data from the selected channel as a CSV file:
* Title of the videos;
* Number of views;
* Link to the video;
* Number of videos displayed to public.

# Scraping

This project uses Selenium 4.15.2 to make requests from a YouTube channel link. First, you need to update the channel URL. To do so, just change the URL on the first string as below:

![screenshot youtube scraper](https://github.com/levycamoes/youtube-web-scraper/assets/98728758/d54730a1-1304-4173-bfa7-fde57ae0346a)

# Example

Scraping the channel "music by bebop," we have:
```
url = "https://www.youtube.com/@musicbybebop/videos"
driver = webdriver.Chrome()
driver.get(url)
```
The program should open an in-browser Chrome page that displays the video page of the channel.
After loading the page, we call the Scroll() function, which scrolls through all the publicly displayed videos of the channel. After scanning the videos, the page closes.
For data visualization, the program creates a pandas DataFrame and a CSV file containing all the channel data.
The output should be a CSV file named "youtube_videos_details.csv" that looks like this:

![image](https://github.com/levycamoes/youtube-web-scraper/assets/98728758/ad096515-6de0-4668-952f-ba6b195b6ecb)

Using proper software, you can improve your CSV data visualization.

# License

This project is under the [MIT](./LICENSE) license. 
