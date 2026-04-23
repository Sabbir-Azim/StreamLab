import re
from urllib.parse import parse_qs, urlparse

from IPython.display import HTML, display

from StreamLab.custom_exception import InvalidURLException
from StreamLab.logger import logger

YOUTUBE_VIDEO_ID_PATTERN = re.compile(r"^[0-9A-Za-z_-]{11}$")
YOUTUBE_HOSTS = {
    "youtube.com",
    "www.youtube.com",
    "m.youtube.com",
    "youtube-nocookie.com",
    "www.youtube-nocookie.com",
}


def _extract_video_id(url: str) -> str:
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname or ""
    path_parts = [part for part in parsed_url.path.split("/") if part]

    if hostname == "youtu.be" and path_parts:
        video_id = path_parts[0]
    elif hostname in YOUTUBE_HOSTS and parsed_url.path == "/watch":
        video_id = parse_qs(parsed_url.query).get("v", [""])[0]
    elif hostname in YOUTUBE_HOSTS and len(path_parts) >= 2:
        video_id = path_parts[1] if path_parts[0] in {"embed", "shorts"} else ""
    else:
        video_id = ""

    if not YOUTUBE_VIDEO_ID_PATTERN.match(video_id):
        raise InvalidURLException(f"Invalid YouTube URL: {url}")

    return video_id


def render_youtube_video(url: str, width: int = 780, height: int = 440):
    video_id = _extract_video_id(url)
    embed_url = f"https://www.youtube-nocookie.com/embed/{video_id}"
    iframe = f"""
        <iframe width="{width}" height="{height}"
        src="{embed_url}"
        title="YouTube video player"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        referrerpolicy="strict-origin-when-cross-origin"
        allowfullscreen>
        </iframe>
        """

    display(HTML(iframe))
    logger.info(f"Successfully rendered YouTube video for URL: {url}")

    return "success"
