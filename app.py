import os
import yt_dlp as ydl
from flask import Flask, request, jsonify

app = Flask(__name__)

COOKIES_PATH = os.path.join(os.path.dirname(__file__), 'cookies.txt')

def get_video_details(url, cookies=None, formats=None):
    ydl_opts = {
        'quiet': True,
        'noplaylist': True,
        'cookies': cookies,
        'skip_download': True,
    }

    with ydl.YoutubeDL(ydl_opts) as ydl_instance:
        info_dict = ydl_instance.extract_info(url, download=False)

        formats_list = info_dict.get('formats', [])
        if formats:
            formats_filtered = [f for f in formats_list if any(fmt in f['format_id'] for fmt in formats)]
        else:
            formats_filtered = formats_list

        return {
            'title': info_dict.get('title', 'N/A'),
            'url': info_dict.get('url', 'N/A'),
            'thumbnail': info_dict.get('thumbnail', 'N/A'),
            'uploader': info_dict.get('uploader', 'N/A'),
            'duration': info_dict.get('duration', 'N/A'),
            'views': info_dict.get('view_count', 'N/A'),
            'like_count': info_dict.get('like_count', 'N/A'),
            'formats': [
                {
                    'format_id': f.get('format_id'),
                    'quality': f.get('quality', 'N/A'),
                    'height': f.get('height', 'N/A'),
                    'url': f.get('url')
                } for f in formats_filtered
            ]
        }

@app.route('/', methods=['GET'])
def video_details():
    url = request.args.get('url')
    video_id = request.args.get('id')
    format_query = request.args.get('format')

    if not url and not video_id:
        return jsonify({'error': 'Either "url" or "id" is required'}), 400

    if video_id:
        url = f"https://www.youtube.com/watch?v={video_id}"

    if not os.path.exists(COOKIES_PATH):
        return jsonify({'error': 'Cookies file not found'}), 400

    formats = format_query.split(',') if format_query else None

    try:
        details = get_video_details(url, cookies=COOKIES_PATH, formats=formats)
        details['developer'] = "S4NCHITT.t.me"
        return jsonify({'success': True, 'video_details': details})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7860)
