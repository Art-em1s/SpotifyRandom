import asyncio, json, random, requests, time, traceback
from auth import OAuth, Playlist
rng = random.SystemRandom

try:
    url = "https://api.spotify.com/v1/playlists/{}".format(Playlist)
    querystring = {"market":"GB"}
    headers = {'Accept': "application/json",'Content-Type': "application/json",'Authorization': OAuth}
    r=requests.request("GET", url, headers=headers, params=querystring).json()
    playlist_length = int(r["tracks"]["total"])
    while True:
        try:
            url = "https://api.spotify.com/v1/playlists/{}tracks".format(Playlist)
            x=rng().randrange(0, 32)
            a=int(playlist_length/10)
            y=rng().randrange(0, a)
            payload = {"range_start":0,"range_length":y,"insert_before":x}
            headers = {'Accept': "application/json",'Content-Type': "application/json",'Authorization': OAuth}
            requests.request("PUT", url, data=payload, headers=headers)
            time.sleep(5)
        except:
            pass #prevents errors due to exceeding rate-limits
except Exception as e:
    print("Error: {}\n{}".format(e, traceback.format_exc()))
 
    