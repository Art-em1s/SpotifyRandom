import asyncio, json, random, requests, time, traceback
from auth import OAuth, Playlist
rng = random.SystemRandom

try:
    url = "https://api.spotify.com/v1/playlists/{}".format(Playlist)
    querystring = {"market":"GB"}
    headers = {'Accept': "application/json",'Content-Type': "application/json",'Authorization': OAuth}
    r=requests.request("GET", url, headers=headers, params=querystring).json()
    plc=int(r["tracks"]["total"])
    for i in range(plc):
        try:
            url = "https://api.spotify.com/v1/playlists/{}/tracks".format(Playlist)
            x=rng().randrange(1, plc)
            payload = {"range_start":0,"range_length":1,"insert_before":x}
            headers = {'Accept': "application/json",'Content-Type': "application/json",'Authorization': OAuth}
            a=requests.request("PUT", url, data=json.dumps(payload), headers=headers).json()
            time.sleep(0.2)
        except Exception as e:
            print("Error: {}\n{}".format(e, traceback.format_exc()))
            pass #prevents errors due to exceeding rate-limits
except Exception as e:
    print("Error: {}\n{}".format(e, traceback.format_exc()))
 
    