from selenium import webdriver
from bs4 import BeautifulSoup
# assign the driver
driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url = 'http://stats.nba.com/players/list/'
# go get me the html page
driver.get(url)
# create my soup
soup = BeautifulSoup(driver.page_source, 'lxml')
div = soup.find('div', class_="stats-player-list players-list")
# print contents of the div
for a in div.find_all('a'):
	print a.text
# shut 'em down
driver.quit()
#double check  local folder names and dependencies if you have any trouble! Happy scraping!
