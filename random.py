import requests, os, random
while True:
    domain = "https://vid.puffyan.us/"
    apilink = domain+"api/v1/popular"
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
    }
    posts = requests.get(apilink, headers=headers)
    if posts.status_code == 200 and 'application/json' in posts.headers.get('Content-Type',''):
        posts = posts.json()
        a = random.randrange(0,len(posts))
        if posts:
            videoId = posts[a]["videoId"]
            print(videoId)
            if videoId:
                os.system("cmd /k start vlc http://riitube.rc24.xyz/video/wii/?q=" + str(videoId))
            else:
                print("No Videos!") 
        else:
            print("No Videos!")                
    else:
        print("Error")
