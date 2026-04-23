import pytest

import StreamLab.youtube as youtube_module
from StreamLab import render_youtube_video
from StreamLab.custom_exception import InvalidURLException


class FakeHTML:
    def __init__(self, value):
        self.value = value


def test_render_youtube_video_displays_privacy_enhanced_embed(monkeypatch):
    captured = {}

    def fake_display(html):
        captured["html"] = html.value

    monkeypatch.setattr(youtube_module, "HTML", FakeHTML)
    monkeypatch.setattr(youtube_module, "display", fake_display)

    result = render_youtube_video(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        width=640,
        height=360,
    )

    assert result == "success"
    assert 'width="640"' in captured["html"]
    assert 'height="360"' in captured["html"]
    assert (
        'src="https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ"'
        in captured["html"]
    )


def test_render_youtube_video_rejects_invalid_url():
    with pytest.raises(InvalidURLException):
        render_youtube_video("https://example.com/not-youtube")
