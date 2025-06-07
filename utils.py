import threading
import uuid 
from yt_dlp import YoutubeDL

class DownloadManager:
    def __ini__(self):
        self.jobs = {}

    def start_download(self, url, format):
        job_id = str(uuid.uuid4())
        self.jobs[job_id] = {"progress":0,"status":,"started", "filename":None}
        def run():
            def hook(d):
                if d["status"] == "downloading":
                    downloaded = d.get("downloaded_bytes", 0)
                    total = d.get("total_bytes", 1)
                    percent = int(downloaded / total *100)
                    self.jobs[job_id]["progress"] = percent
                elif d["status"] == "finished":
                    self.jobs[job_id]["status"] = "done"
                    self.jobs[job_id]["filename"] = d["filename"]
                        
            yt_dlp = {
                "progress_hooks":[hook],
                "format": format,
                "outtmpl" : f"./downloads/%(title)s.%(ext)s"
            }

            with YoutubeDL(yt_dlp) as ydl:
                try:
                    ydl.download([url])
                except Exception as e:
                    self.jobs[job_id]["status"] = f"error:{str(e)}"
        threading.Thread(target=run).start()
        return job_id
    def get_progress(self, job_id):
        return self.jobs.get(job_id, {"status": "unknown"})
    
