import config
import requests
import shutil
import os
from bs4 import BeautifulSoup as soup

def download(urls, title, chapter, dir):
	# For every line in the file
	for url in urls:
	    # Split on the rightmost / and take everything on the right side of that
	    url = url.rstrip('\r\n')
	    name = url.rsplit('/', 1)[-1]

	    # if a chapter exists
	    if chapter:
	    	filename = os.path.join(dir, title, chapter, name)
	    	# Combine the name and the downloads directory to get the local filename
	    else:
	    	filename = os.path.join(dir, title, name)
	    # ensure the directory exists
	    directory = os.path.dirname(filename)
	    if not os.path.exists(directory):
	    	os.makedirs(directory)
	    # Download the file if it does not exist
	    if not os.path.isfile(filename):
	    	response = requests.get(url, headers=config.headers)
	    	with open(filename, 'wb') as outfile: outfile.write(response.content)


def getLinks(url):
	response = requests.get(url, headers=config.headers)
	page_soup = soup(response.content, "html.parser")
	links = page_soup.findAll('img')
	# storylinks are images to be downloaded
	storylinks = []
	chapter = ''
	title = ''
	for link in links:
		# find the filename (everything after the last /)
		filename = link['src'].rsplit('/', 1)[-1]
		# remove the extension
		filename = os.path.splitext(filename)[0]
		# for the specific site being scraped
		# all relevant images only contain numbers
		if filename.isdigit():
			# for all numeric filenames, append to
			storylinks.append(link['src'])
			# grab the chapter name
			# note: this really only needs to be done once
			# but this is file gauranteed to have the chapter url
			chapter = link['src'].rsplit('/', 2)[-2]
			# grab the title
			title = link['src'].rsplit('/', 3)[-3]
	# if there are no chapters, then the url is formatted as
	# http://domain.com/title/page_num.extension
	# handle accordingly
	if "chap" in chapter.lower():
		return title, chapter, storylinks
	else:
		title = chapter
		return title, '', storylinks

def getAllChapters(url):
	chapters = []
	response = requests.get(url, headers=config.headers)
	page_soup = soup(response.content, "html.parser")
	chapter_list = page_soup.find("div", class_="chapter-list")
	possible_chapters = chapter_list.findChildren("a", href=True)
	for possible_chapter in possible_chapters:
		chapters.append(possible_chapter['href'])
	return(chapters)

def getSeries(url, directory):
	chapters = getAllChapters(url)
	for chapter in chapters:
		title, current_chapter, urls = getLinks(chapter)
		print("Title: " + title + " Chap : " + current_chapter)
		download(urls, title, current_chapter, directory)

if __name__ == "__main__":
	getSeries(config.url, config.download_dir)
