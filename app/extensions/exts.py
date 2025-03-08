from typing import Final

VIDEO_EXTS: Final = frozenset((".m4a", "mp3", ".wav", ".flac", ".mp4", ".mkv", ".flv", ".avi", ".wmv", ".ts", ".rmvb", ".webm", "wmv"))
EXTENDED_VIDEO_EXTS: Final = VIDEO_EXTS.union((".strm",))

SUBTITLE_EXTS: Final = frozenset(("lrc", ".ass", ".srt", ".ssa", ".sub"))

IMAGE_EXTS: Final = frozenset((".png", ".jpg"))

NFO_EXTS: Final = frozenset((".nfo",))
