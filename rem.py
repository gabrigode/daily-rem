import os, time
from twython import Twython, TwythonError
from os import environ
from io import BytesIO
import requests
from pybooru import Danbooru

#TWITTER API AUTH
consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']
twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
auth = twitter.get_authentication_tokens

def danbooru():
    client = Danbooru('danbooru')
    danbooru = client.post_list(tags=['rating:safe rem_(re:zero)'], limit=[1], random=["true"])

    for danbooru in danbooru:
        source = danbooru['source']
        artist = danbooru['tag_string_artist']
        url = danbooru['file_url']
        print (source)
        print (url)
        print (artist)
        return (url, artist, source)

def sendTwitter():
    (url, artist, source) = danbooru()
    response = requests.get(url)
    photo = BytesIO(response.content)
    response = twitter.upload_media(media=photo)
    twitter.update_status(status=f'Artist: {artist} \nSource: {source}', media_ids=[response['media_id']])

def favTwitter():
    i = 0
    search_results = twitter.cursor(twitter.search, count=100, q='rem re:zero')
    for result in search_results:
        if i>100:
            break
        else:
            try:
                i = i + 1
                id_tweet = result['id']
                twitter.create_favorite(id=id_tweet)
            except TwythonError as e:
                print (e)
                print ("A error has ocurred while trying to favorite one of the tweets. Probably already favorited")
                break

while True:
    sendTwitter()
    favTwitter()
    time.sleep(3600)