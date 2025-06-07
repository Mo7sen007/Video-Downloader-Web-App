from flask import Flask, send_file, send_from_directory, request, jsonify
import os
from utils import DownloadManager

manager = DownloadManager()

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/download", methods=["POST"])
def download():
    url =request.form["url"]
    selected_format = request.form["format"]
    job_id = manager.start_download(url, selected_format)
    return jsonify({"job_id": job_id})        #mp3 case handle

    #return send_from_directory(output_dir, basename, as_attachment=True)

@app.route("/progress/<job_id>")
def progress(job_id):
    return jsonify(manager.get_progress(job_id))

@app.route("/downloaded/<job_id>")
def downloaded(job_id):
    job = manager.get_progress(job_id)
    if job["status"] != "done" or not job["filename"]:
        return abort(404, description = "File not ready")
    directory = os.path.dirname(job["filename"])
    filename = os.path.basename(job["filename"])
    filepath = os.path.join(directory,filename)
    return send_file(filepath, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
