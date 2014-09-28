import facebook3
from json import dumps

def printj(json_object):
    print(dumps(json_object, indent=4))

## You can obtain a fresh access token here
## https://developers.facebook.com/tools/explorer/
## The one here will not work

token = "CAACEdEose0cBABCiExhM1qAXJKEPyb03z1LkGvD0ZCUpnQHTdT1xalRPv1C8iKObvgNakaxzFVbJVXrDVmq6roMhJ0hVepbb3SU5axK8Xem7VFNIpfALza81ujM0JZBYBWHw386wYLrtkygM90PgG7m8hzuTAZBkyUgEn7OrU4wcP58keHc53ndiwqVgETfyIvqvdcVKisk2fSseJmM29EEaeYsnnkZD"

graph = facebook3.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")

printj(profile)

printj(friends)




