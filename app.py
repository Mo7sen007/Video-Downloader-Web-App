from flask import Flask, send_from_directory, request, jsonify
import yt_dlp
import os

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/download", methods=["POST"])
def download():
    url =request.form["url"]
    selected_format = request.form["format"]
    output_dir = os.path.join(os.getcwd(), "download")
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {"outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),"format": selected_format}
    if selected_format == "mp3":
        ydl_opts.update({
            "format" : "bestaudio/best",
            "postprocessors": [{
                "key" : "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality":"192",
            }]
        })
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        #mp3 case handle
        if selected_format == "mp3":
            filename = os.path.splitext(filename)[0] + ".mp3"

        basename = os.path.basename(filename)


    return send_from_directory(output_dir, basename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
