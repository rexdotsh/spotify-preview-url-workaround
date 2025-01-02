import re
from typing import Optional

import requests


def get_spotify_preview_url(spotify_track_id: str) -> Optional[str]:
    """
    Get the preview URL for a Spotify track using the embed page workaround.

    Args:
        spotify_track_id (str): The Spotify track ID

    Returns:
        Optional[str]: The preview URL if found, else None
    """
    try:
        embed_url = f"https://open.spotify.com/embed/track/{spotify_track_id}"
        response = requests.get(embed_url)
        response.raise_for_status()

        html = response.text
        match = re.search(r'"audioPreview":\s*{\s*"url":\s*"([^"]+)"', html)
        return match.group(1) if match else None

    except Exception as e:
        print(f"Failed to fetch Spotify preview URL: {e}")
        return None


# example usage:
# preview_url = get_spotify_preview_url('1301WleyT98MSxVHPZCA6M')
