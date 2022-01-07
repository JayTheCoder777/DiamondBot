import requests
r =requests.get('https://api.mcsrvstat.us/2/216.49.241.192')
import json
from random import randint
# parse x:
y = r.json()
#return('The server is up! \nPlayers online: '+str(test.r.json()['players']['list']))

# the result is a Python dictionary:
print(y["online"])
print(r.text)
#return('The server is up! \nPlayers online: '+str(test.r.json()['players']['list']))
def respond():
  global r
  r =requests.get('https://api.mcsrvstat.us/2/216.49.241.192')
  response = ('The server is up! \n')
  '''if r.json()['players']['online']==0:
    response.join('No one is online.')
  else:
    response = response+'Players online: '
    for i in range(0,r.json()['players']['online']):
      response = response+r.json()['players']['list'][i]+'
  '''
  print(response)
  return(response)

print(respond())