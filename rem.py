import os, time
from twython import Twython
from os import environ
from io import BytesIO
import requests
from pybooru import Danbooru

while True:
    #TAKE IMAGES FROM DANBOORU

    client = Danbooru('danbooru')
    artists = client.post_list(tags=['rating:safe rem_(re:zero)'], limit=[1], random=["true"])

    for artist in artists:
        source = artist['source']
        url = artist['file_url']
        print (source)
        print (url)

    #AUTH TO TWITTER
    consumer_key = ''
    consumer_secret =  ''
    access_token =  ''
    access_token_secret = ''
    twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
    auth = twitter.get_authentication_tokens

    #PROCESS IMAGE TO DOWNLOAD
    response = requests.get(url)
    photo = BytesIO(response.content)
    response = twitter.upload_media(media=photo)
    twitter.update_status(status=f'Source: {source}', media_ids=[response['media_id']])

    time.sleep(10800)


