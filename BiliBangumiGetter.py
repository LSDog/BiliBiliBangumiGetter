import requests
import sys
import time

#这里是要爬的md号，拼到后面 https://www.bilibili.com/bangumi/media/md908 访问就是 DOUBLE-J
md_start = 2708481
md_end = 30000000

def getInfo(mediaId) -> dict:
    try:

        response = requests.get(f'http://api.bilibili.com/pgc/review/user?media_id=' + str(mediaId))
        response.raise_for_status()
        if response.status_code != 200:
            print('\a请求失败')
            sys.exit(1)

        inf = response.json()
        inf = inf['result']['media']

        return inf

    except requests.RequestException or ValueError as e:
        print(e)
    except KeyError as e:
        return None


if __name__ == "__main__":

    noneCount = 0
    
    f = open("MediaList.txt", encoding='utf-8', mode="a")

    for i in range(md_start, md_end):

        inf = getInfo(i)

        if inf == None:
            noneCount += 1
            print(str(i) + ' None')
            continue

        if inf['type_name'] == '番剧':
            if noneCount > 5:
                print('none count: ', noneCount)
            noneCount = 0
            result = str(inf['media_id'])+'\t'+inf['title']+'\t\t\t\t'+inf['share_url']
            print(result)
            f.write(result+"\n")
            f.flush()
        else:
            if noneCount > 5:
                print('none count: ', noneCount)
            noneCount = 0
            print(str(i) + ' Not a anime')
        
        #time.sleep(0.2)
        

f.flush()
f.close()