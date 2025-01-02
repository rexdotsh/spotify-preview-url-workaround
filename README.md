# Spotify Preview URL Workaround

A simple utility to extract preview URLs for Spotify tracks, working around a current bug in the Spotify API where `preview_url` is being returned as `null`.

## The Problem

As of early 2024, the Spotify API has a bug where the `preview_url` field is being returned as `null` for many tracks, even when preview audio is actually available. This affects multiple endpoints including:

- `/v1/tracks/{id}`
- `/v1/me/player/currently-playing`
- `/v1/me/player/recently-played`

## The Solution

This workaround, [originally discovered on Stack Overflow](https://stackoverflow.com/questions/79237053/android-spotify-api-preview-url-for-tracks-is-suddenly-being-returned-as-null), extracts the preview URL directly from Spotify's embed player HTML. While not an official solution, it provides a reliable way to access preview URLs until the API issue is resolved.

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
