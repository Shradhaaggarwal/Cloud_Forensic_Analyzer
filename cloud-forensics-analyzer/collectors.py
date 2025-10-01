"""Data collectors for cloud forensic sources."""

from typing import List


def list_dropbox_files(path: str) -> List[str]:
    """Stub: return a list of file paths from Dropbox at `path`.

    Replace with actual Dropbox API calls and auth handling.
    """
    # TODO: implement Dropbox SDK integration
    return []


def collect_gdrive_files(folder_id: str) -> List[str]:
    """Stub: return a list of files from Google Drive folder.

    Replace with Google Drive API client usage.
    """
    # TODO: implement Google Drive API integration
    return []
