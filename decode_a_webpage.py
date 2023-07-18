import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/' #Declares website
r = requests.get(url) #gets HTML
r_html = r.text #html as text

soup = BeautifulSoup(r_html, features= 'html.parser') #constructor
x = soup.find_all('a') #gets all <a> tags from HTML
count = 0

x = list(x) #sets x as list 
HTMLsubtitles = [''] #creates 'empty' list 
subtitles = ['']

for i in range(13,50): 
    HTMLsubtitles.append(x[i]) #adds html code for each subtitle to list
    
for line in HTMLsubtitles: #adds subtitles to list 
    subtitles.append(str(line))
    # print(str(line))
    for i in line: 
        subtitles.append(str(i))
print(subtitles)
