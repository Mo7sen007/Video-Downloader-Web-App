import threading
import uuid 
from yt_dlp import YoutubeDL
import os


output_dir = os.path.join(os.getcwd(),"downloads")
os.makedirs(output_dir, exist_ok=True)
class DownloadManager:
    def __init__(self):
        self.jobs = {}

    def start_download(self, url, format):
        job_id = str(uuid.uuid4())
        self.jobs[job_id] = {"progress":0,"status":"started", "filename":None}
        def run():
            def hook(d):
                if d["status"] == "downloading":
                    downloaded = d.get("downloaded_bytes", 0)
                    total = d.get("total_bytes", 1)
                    percent = int(downloaded / total *100)
                    self.jobs[job_id]["progress"] = percent
                    #elif d["status"] == "finished":
                    #self.jobs[job_id]["status"] = "done"
                    #self.jobs[job_id]["filename"] = d["filename"]
                        
            ydl_opts = {
                "progress_hooks":[hook],
                "format": format,
                "outtmpl" : os.path.join(output_dir,"%(title)s.%(ext)s")
            }
            if format =="mp3":
                ydl_opts.update({
                    "format" : "bestaudio/best",
                    "postprocessors" : [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec" : "mp3",
                        "preferredquality" : "192",
                    }]
                })
            with YoutubeDL(ydl_opts) as ydl:
                try:
                    #ydl.download([url])
                    info = ydl.extract_info(url, download = True)
                    filename = ydl.prepare_filename(info)
                    if format == "mp3":
                        filename = os.path.splitext(filename)[0] + ".mp3"
                    self.jobs[job_id]["filename"] = filename
                    self.jobs[job_id]["status"] = "done"
                except Exception as e:
                    self.jobs[job_id]["status"] = f"error:{str(e)}"
        threading.Thread(target=run).start()
        return job_id
    def get_progress(self, job_id):
        return self.jobs.get(job_id, {"status": "unknown"})
    
