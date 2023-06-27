from pytube import YouTube
link='https://youtu.be/St0Jf_VmG_g'
youtube_1=YouTube(link)
print(youtube_1.title)
print(youtube_1.length)
videos=youtube_1.streams.all()
# videos=youtube_1.streams.filter(only_audio=True) for downlaoding audio only
vid=list(videos)
for i in vid:
    print(i)
strm=int(input("Enter number :- "))
videos[strm].download()
print("Downloaded!!")



