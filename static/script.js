function startDownload() {
      const url = document.getElementById("url").value.trim();
      if (!url) {
        document.getElementById("status").innerText = "Please enter a URL.";
        return;
      }
      const format = document.getElementById("format").value;

      document.getElementById("status").innerText = "Starting download...";
      document.getElementById("progressBar").value = 0;

      fetch("/download", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams({ url, format }),
      })
        .then((res) => res.json())
        .then((data) => pollProgress(data.job_id))
        .catch((err) => {
          console.error(err);
          document.getElementById("status").innerText = "❌ Error downloading video.";
        });
    }

    function pollProgress(job_id) {
      const progressBar = document.getElementById("progressBar");
      const interval = setInterval(() => {
        fetch(`/progress/${job_id}`)
          .then((res) => res.json())
          .then((data) => {
            progressBar.value = data.progress || 0;
            document.getElementById("status").innerText = `Status: ${data.status} | Progress: ${data.progress || 0}%`;
            if (data.status === "done") {
              clearInterval(interval);
              document.getElementById("status").innerText = "Download complete!";
              window.location.href = `downloaded/${job_id}`;
            }
            if (data.status.startsWith("error")) {
              clearInterval(interval);
              document.getElementById("status").innerText = "Error :( " + data.status;
            }
          });
      }, 1000);
    }