import asyncio, json, random, requests, time, traceback, os
rng = random.SystemRandom
try:
    os.system('cls')
    OAuth = input("Go here and get a OAuth Token: https://developer.spotify.com/console/put-playlist-tracks/\nPaste your token here: ")
    OAuth = "Bearer {}".format(OAuth)
    os.system('cls')
    Playlist = input("Paste your playlist URL here: ")
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
            r=requests.request("PUT", url, data=json.dumps(payload), headers=headers)
            x = json.loads(r.text)
            time.sleep(0.25)
            if r.status_code == 403:
                os.system('cls')
                print("Error: {}".format(x['error']['message']))
                break
            os.system('cls')
            print("{} of {} songs randomised.".format(i,plc))
        except Exception as e:
            print("Error: {}\n{}".format(e, traceback.format_exc()))
            time.sleep(5)
            pass #prevents errors due to exceeding rate-limits
except Exception as e:
    print("Error: {}\n{}".format(e, traceback.format_exc()))
 
