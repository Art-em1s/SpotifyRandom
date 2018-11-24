import asyncio, json, random, requests, time, traceback
from auth import OAuth, Playlist
rng = random.SystemRandom

try:
    url = "https://api.spotify.com/v1/playlists/{}".format(Playlist)
    querystring = {"market":"GB"}
    headers = {'Accept': "application/json",'Content-Type': "application/json",'Authorization': OAuth}
    r=requests.request("GET", url, headers=headers, params=querystring).json()
    while True:
        try:
            url = "https://api.spotify.com/v1/playlists/{}/tracks".format(Playlist)
            x=rng().randrange(0, int(r["tracks"]["total"]/10))
            y=rng().randrange(0, 64)
            payload = {"range_start":1,"range_length":y,"insert_before":x}
            headers = {'Accept': "application/json",'Content-Type': "application/json",'Authorization': OAuth}
            a=requests.request("PUT", url, data=json.dumps(payload), headers=headers).json()
            print("{} songs moved to {}-{}".format(x, y, y+x))
            time.sleep(5)
        except Exception as e:
            print("Error: {}\n{}".format(e, traceback.format_exc()))
            pass #prevents errors due to exceeding rate-limits
except Exception as e:
    print("Error: {}\n{}".format(e, traceback.format_exc()))
 
    