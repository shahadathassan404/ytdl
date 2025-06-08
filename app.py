import os
import yt_dlp as ydl
from flask import Flask, request, jsonify

app = Flask(__name__)

COOKIES_PATH = 'cookies.txt'

def get_video_details(url, cookies=None, formats=None):
    ydl_opts = {
        'noplaylist': True,
        'quiet': True,
        'cookies': cookies,
    }

    with ydl.YoutubeDL(ydl_opts) as ydl_instance:
        info_dict = ydl_instance.extract_info(url, download=False)

        video_details = {
            'title': info_dict.get('title', 'N/A'),
            'url': info_dict.get('url', 'N/A'),
            'thumbnail': info_dict.get('thumbnail', 'N/A'),
            'uploader': info_dict.get('uploader', 'N/A'),
            'duration': info_dict.get('duration', 'N/A'),
            'views': info_dict.get('view_count', 'N/A'),
            'like_count': info_dict.get('like_count', 'N/A'),
            'dislike_count': info_dict.get('dislike_count', 'N/A'),
        }

        formats_list = info_dict.get('formats', [])
        if formats:
            formats_filtered = [f for f in formats_list if any(fmt in f['format_id'] for fmt in formats)]
        else:
            formats_filtered = formats_list

        video_details['formats'] = [
            {'format_id': f"{f['format_id']}", 'quality': f.get('quality', 'N/A'), 'height': f.get('height', 'N/A'), 'url': f.get('url', 'N/A')}
            for f in formats_filtered
        ]
        
        return video_details

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

    formats = None
    if format_query:
        formats = format_query.split(',')

    try:
        details = get_video_details(url, cookies=COOKIES_PATH, formats=formats)
        details['developer'] = "S4NCHITT.t.me"
        return jsonify({'success': True, 'video_details': details})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
