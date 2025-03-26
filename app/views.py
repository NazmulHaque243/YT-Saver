import yt_dlp
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return render(request, 'downloader/index.html')

def get_video_formats(request):
    """Fetch available resolutions with minimal processing."""
    url = request.GET.get("url")
    if not url:
        return JsonResponse({"error": "No URL provided"}, status=400)

    ydl_opts = {
        'quiet': True,
        'extract_flat': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            formats = [
                {
                    "format_id": f["format_id"],
                    "resolution": f.get("resolution", "audio"),
                    "ext": f["ext"],
                    "url": f["url"]  # Direct YouTube URL for client-side download
                }
                for f in info.get("formats", [])
                if f.get("resolution") or f["ext"] == "mp4"
            ]
            return JsonResponse({"formats": formats})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
