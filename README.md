# Spotify Preview URL Workaround

A simple utility to extract preview URLs for Spotify tracks. This provides an alternative method to access preview audio when the official API's `preview_url` field returns `null`.

## The Problem

The Spotify API often returns `preview_url` as `null` for many tracks, even when preview audio is actually available. As of November 27, 2024, Spotify [officially announced](https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api) that "30-second preview URLs, in multi-get responses (`SimpleTrack` object)" are intentionally being removed for new API applications.

This affects multiple endpoints including:

- `/v1/tracks/{id}`
- `/v1/me/player/currently-playing`
- `/v1/me/player/recently-played`

## The Solution

This workaround, [originally discovered on Stack Overflow](https://stackoverflow.com/questions/79237053/android-spotify-api-preview-url-for-tracks-is-suddenly-being-returned-as-null), extracts the preview URL directly from Spotify's embed player HTML. While not an official solution, it provides a reliable way to access preview URLs despite the API changes.

## Installation

### Python

```bash
pip install requests
```

### TypeScript

No additional dependencies required if you have `fetch` available in your environment.

## Usage

### Python

```python
from spotify_preview import get_spotify_preview_url

# Pass a Spotify track ID
preview_url = get_spotify_preview_url('1301WleyT98MSxVHPZCA6M')
if preview_url:
    print(f"Preview URL: {preview_url}")
```

### TypeScript

```typescript
import { getSpotifyPreviewUrl } from "./spotify-preview";

// Pass a Spotify track ID
const previewUrl = await getSpotifyPreviewUrl("1301WleyT98MSxVHPZCA6M");
if (previewUrl) {
  console.log(`Preview URL: ${previewUrl}`);
}
```

## Notes

- The track ID can be found in the Spotify URL for any track (e.g., `https://open.spotify.com/track/1301WleyT98MSxVHPZCA6M`)
- No API key or authentication is required as this uses the public embed player

## License

MIT
