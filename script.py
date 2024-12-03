from selenium import webdriver 

search_string = input("input url or string to search for:") 

search_string = search_string.replace(' ', '+') 

browser = webdriver.Chrome('chromedriver') 

for i in range(1): 
	matched_elements = browser.get("https://www.google.com/search?q=" +
									search_string + "&start=" + str(i)) 
