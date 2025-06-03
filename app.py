from flask import Flask, send_from_directory, request, jsonify
import yt_dlp
import os

app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    return send_from_directory("static", "index.html")

@app.route("/download", methods=["POST"])
def download():
    data = request.get_json()
    url = data["url"]
    output_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {"outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s")}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
    return jsonify({"title": info.get("title", "Unknown")})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
