from pytube import YouTube
import os

print("Enter Link: ")
url = input()

destination = os.getcwd()

try:
    #object creation using YouTube which was imported in the beginning
    yt = YouTube(url)
except:
    print("Connection Error")

# Show list of all the available streams
list = yt.streams.filter(progressive=True, subtype='mp4').order_by('resolution').desc().all()
list = str(list).split(',')
size = len(list)
for x in range (0, size):
	temp = list[x]
	pos = temp.index('res')
	print(x,'. ', list[x][pos+5:pos+4+5])

print("Enter Index: ")
index = int(input())

i = list[index].index("itag")
itag = list[index][i+6:i+8]

try:
	yt.streams.get_by_itag(int(itag)).download(destination)
	print("Download Successful")
except:
	print("Connection Error")
