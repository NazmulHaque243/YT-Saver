from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View
from pytube import YouTube
import re



class home(View):
    def __init__(self,url=None):
        self.url = url
    def get(self,request):
        return render(request,'home.html')
    

    def post(self,request):
        # for fetching the video
        if request.POST.get('fetch-vid'):
            self.url = request.POST.get('given_url')
            video = YouTube(self.url)
            info=video.vid_info
            info2=video.streaming_data
            vidTitle,vidThumbnail = re.sub(r"(\W+)(\d+)", "",video.title),video.thumbnail_url
            if "streamingData" in info:
                format=info["streamingData"]
                context = {'vidTitle':re.sub(r"\|","_",vidTitle).lstrip(),'vidThumbnail':vidThumbnail,'stream':format['formats'],
                            'url':self.url}
                return render(request,'home.html',context)
            else:
                context = {'vidTitle':re.sub(r"\|","_",vidTitle).lstrip(),'vidThumbnail':vidThumbnail,'stream':info2['formats'],
                            'url':self.url}
                return render(request,'home.html',context)


        # for downloading the video
        elif request.POST.get('download-vid'):
            self.url = request.POST.get('given_url')
            video = YouTube(self.url)
            stream = [x for x in video.streams.filter(progressive=True)]
            video_qual = video.streams[int(request.POST.get('download-vid')) - 1]
            video_qual.download(output_path='../../Downloads')
            return redirect('home')

        return render(request,'home.html')