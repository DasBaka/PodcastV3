import requests

PodcastJSON = '{'

# Define the URL of the website you want to scrape
#url = 'https://podcasts.watchnebula.com/thesojournrss/f3c64bd07d894cac8a197e66abad7c25'


# Send an HTTP GET request to the URL
#response = requests.get(url)

# Check if the request was successful (status code 200)
#if response.status_code == 200:
    # Print the HTML source code
    #print(response.text)
#    print('success')
#else:
#    print('Failed to retrieve the webpage. Status code:', response.status_code)

path='C:/dev/PodcastV3/rss/rss.xml'
#path='C:/dev/PodcastV3/rss/leer.txt'
file = open(path, "r", buffering=-1, encoding="utf8", errors=None, newline=None, closefd=True, opener=None)
rss = file.read()
#rss ='1<title>a</title>'
file.close
#print(rss)
tags = ['title','description']
n = 0
while n < len(tags):
  PodcastJSON+='\n"'
  PodcastJSON+=tags[n]
  PodcastJSON+='":"'
  posStart = rss.find('<'+tags[n]+'>')
  posEnd = rss.find('</'+tags[n]+'>')
  i = 0
  while i<posEnd-posStart-len(tags[n])-2:
    PodcastJSON += rss[posStart+2+i+len(tags[n])]
    i+=1
  PodcastJSON+='"'
  n+=1
    
PodcastJSON+='\n}'

#print(posStart)
#print(posEnd)
print(PodcastJSON)