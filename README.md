
# **YT-DLP API**

![YT-DLP API Logo](https://via.placeholder.com/150)

Welcome to the **YT-DLP API**! This API allows you to retrieve video details and various download/streaming formats from YouTube using **yt-dlp**. It supports retrieving **video details**, **audio formats**, and **video formats** such as `mp4`, `mp3`, `1080p`, `720p`, and more!

This project is hosted on [Vercel](https://vercel.com/), making it highly scalable and always available.

## **Table of Contents**

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Request Formats](#request-formats)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)
- [Developer Info](#developer-info)

## **Features**

- 🎥 **Video Details**: Retrieve title, uploader, views, likes, duration, and more.
- 🎶 **Audio Formats**: Get all available audio formats like `mp3`, `aac`, and more.
- 🎬 **Video Formats**: Access multiple video formats such as `mp4`, `1080p`, `720p`, `4k`, etc.
- 🌐 **Public API**: Easily accessible for anyone to integrate with their own projects.
- 🚀 **Fast and Scalable**: Hosted on Vercel for optimal performance.

## **Installation**

You can deploy this API by cloning this repository or using the Vercel CLI:

1. Clone the repository:
   ```bash
   git clone https://github.com/shahadathassan404/ytdl.git
   cd ytdl
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## **Usage**

### **Request Formats**

- **All audio formats** (`mp3`, `aac`, etc.) with video details:

  ```
  /?url=https://www.youtube.com/watch?v=video_id&format=mp3
  ```

- **All video formats** (`mp4`, `1080p`, etc.) with video details:

  ```
  /?url=https://www.youtube.com/watch?v=video_id&format=mp4
  ```

- **Specific format** (e.g., `720p`):

  ```
  /?url=https://www.youtube.com/watch?v=video_id&format=720p
  ```

- **Using video ID instead of URL**:

  ```
  /?id=video_id&format=mp3
  ```

## **API Documentation**

### **Endpoints**

- **GET /**:
  - **Parameters**:
    - `url` (string): The URL of the YouTube video.
    - `id` (string): The YouTube video ID (if URL is not provided).
    - `format` (string): A comma-separated list of formats (e.g., `mp4,1080p`).
  
  - **Response**: Returns JSON with video details and selected formats.

### **Sample Request**

```bash
curl "https://ytdlp-api-psi.vercel.app/?url=https://www.youtube.com/watch?v=video_id&format=mp4,1080p"
```

### **Sample Response**

```json
{
    "success": true,
    "video_details": {
        "title": "Example Video Title",
        "url": "https://example.com/streaming_url",
        "thumbnail": "https://example.com/thumbnail.jpg",
        "uploader": "Uploader Name",
        "duration": 3600,
        "views": 1000000,
        "like_count": 10000,
        "dislike_count": 500,
        "formats": [
            {
                "format_id": "22",
                "quality": "HD",
                "height": 1080,
                "url": "https://example.com/video_1080p.mp4"
            },
            {
                "format_id": "18",
                "quality": "SD",
                "height": 480,
                "url": "https://example.com/video_480p.mp4"
            }
        ]
    },
    "developer": "PikachuFromBd.t.me"
}
```

## **Contributing**

We welcome contributions to enhance this API! Please fork the repository and submit a pull request with your improvements.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push the branch (`git push origin feature-branch`).
5. Submit a pull request.

## **License**

MIT License. See [LICENSE](LICENSE) for more details.

## **Developer Info**

- 👨‍💻 **Developer**: [Shahadat Hassan](https://shahadathassan.xyz) 
- 💬 **Telegram**: [PikachuFromBd](https://t.me/PikachuFromBd) ![Telegram](https://img.shields.io/badge/Telegram-%40PikachuFromBd-blue)
- 🌐 **Website**: [Shahadat Hassan](https://shahadathassan.xyz)
- 📫 **Contact**: [Telegram](https://t.me/PikachuFromBd)

## **Badges**

![License](https://img.shields.io/badge/license-MIT-blue)
![Vercel](https://img.shields.io/badge/deployed_on-Vercel-brightgreen)
![Python](https://img.shields.io/badge/python-3.9-blue)
![Repo Size](https://img.shields.io/github/repo-size/shahadathassan404/ytdl)
![Stars](https://img.shields.io/github/stars/shahadathassan404/ytdl?style=social)
