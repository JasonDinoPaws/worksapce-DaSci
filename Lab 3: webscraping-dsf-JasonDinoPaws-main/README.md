# Lab 3: Webscraping
For this lab, complete the following three challenges. You will need the `requests` library and the `BeautifulSoup` library. You may want to use regular expressions. Your programs should be in a Jupyter Notebook with proper titles and comments.

## Part 1: Link Scraper
For any website, print out the all of the other websites it links to. Exclude the original sites(for example other pages within the same site) from the list. When you list the websites, only include the subdomain, second level domain and the top level domain. 
![Pasted image 20240201081822](https://github.com/gormes-EPIC/webscraping/assets/134316348/a9cedb13-a58d-4497-ad4d-57dfe24aaadd)

## Part 2: Weather
Get the current weather using [AccuWeather]( https://www.accuweather.com/en/us/englewood/80110/daily-weather-forecast/332230). Write a program to print out the high and low temperature for the next three days. Each line should include the date and the highs/lows. If there is a 'Wintercast' banner for the day, print out the expected snowfall as well.

## Part 3: Recipes
Create a program to remove the backstory from recipe websites. For simplicity, choose one website, for example [simplyrecipes.com](https://www.simplyrecipes.com/). For a recipe, your program needs to print out the title of the recipe, the total time, the serving size, a list of ingredients, and numbered steps.
