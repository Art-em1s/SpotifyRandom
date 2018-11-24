import asyncio, json, random, requests, time, traceback, os
rng = random.SystemRandom
try:
    print("Go here and get a OAuth Token: https://developer.spotify.com/console/put-playlist-tracks/")
    print("Paste your token here: ")
    OAuth = input()
    OAuth = "Bearer {}".format(OAuth)
    print("Paste your playlist URL here: ")
    Playlist = input()
    Playlist = Playlist.split("/")[6].split("?")[0]
    try:
        url = "https://api.spotify.com/v1/playlists/{}".format(Playlist)
        querystring = {"market":"GB"}
        headers = {'Accept': "application/json",'Content-Type': "application/json",'Authorization': OAuth}
        r=requests.request("GET", url, headers=headers, params=querystring).json()
        plc=int(r["tracks"]["total"])
    except:
        print("Incorrect playlist/token information, check them and try again")
        quit()
    for i in range(plc):
        try:
            url = "https://api.spotify.com/v1/playlists/{}/tracks".format(Playlist)
            x=rng().randrange(1, plc)
            payload = {"range_start":0,"range_length":1,"insert_before":x}
            headers = {'Accept': "application/json",'Content-Type': "application/json",'Authorization': OAuth}
            a=requests.request("PUT", url, data=json.dumps(payload), headers=headers).json()
            time.sleep(0.2)
            os.system('cls')
            print("{}/{}".format(i,plc))
        except Exception as e:
            print("Error: {}\n{}".format(e, traceback.format_exc()))
            pass #prevents errors due to exceeding rate-limits
except Exception as e:
    print("Error: {}\n{}".format(e, traceback.format_exc()))
 
    