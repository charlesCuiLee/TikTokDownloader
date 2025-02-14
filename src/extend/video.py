from types import SimpleNamespace

__all__ = ["VideoDownloader"]


class VideoDownloader:
    COOKIE = False

    @staticmethod
    def deal(data: dict | SimpleNamespace, *args, **kwargs) -> str:
        return data["downloads"]
