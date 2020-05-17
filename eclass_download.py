# -*- coding: UTF-8 -*-
import wget
import requests
import os 
import os.path

url = 'https://smile.shec.edu.cn/resouces/cms/shjgbzw/pms/json/dataStudent.json?timestamp=1589680449457'

course = requests.get(url).json() 

chinese = course['data'][0]['grades']

#grade6 to grade9, index from 0
for i in range(5,9):
    gradedict = chinese[i]
    grade = gradedict['grade']
    videos = gradedict['videos']
    length = len(videos)
    for x in range(length-1,-1,-1):
        videoinfo = videos[x]
        name = videoinfo['name']
        path = grade + '/' + str(x-38) + '/' + name
        if not os.path.exists(path):
            os.makedirs(path)
        imgUrl = videoinfo['imgUrl']
        videoUrl = videoinfo['videoUrl']
        videoName = videoUrl.split('/')[-1:]

        if os.path.exists(path + '/' + videoName[0]):
            print('%s : %s exists , skip' % (grade, name))
            continue
        os.chdir(path)
        os.system('rm -rf *')
        print('begin downlaod %s %s' % (grade,name))
        wget.download(imgUrl)
        wget.download(videoUrl)
        print('\n end downlaod %s %s' % (grade,name))
