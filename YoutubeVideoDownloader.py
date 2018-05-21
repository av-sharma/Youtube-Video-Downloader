from pytube import YouTube

print("Enter Link: ")
link = input()

print("Enter Destination: ")
destination = input()

yt = YouTube(link)

# Currently it downloads only the best available quality
yt.streams.first().download(destination)
#print(yt.streams.filter(progressive=True).all())
	
print("Download Successful")