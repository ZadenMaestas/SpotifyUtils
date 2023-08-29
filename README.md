# Spotify Playlist Manager

A Python application for managing your Spotify playlists, including archiving collaborative playlists and saving playlist tracks to text files.

## Getting Started

### Prerequisites

- Python 3.x
- [Spotipy](https://github.com/plamere/spotipy) library

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/spotify-playlist-manager.git
   ```

2. Install the required Spotipy library:

   ```bash
   pip install spotipy
   ```

3. Edit the `main.py` file with your Spotify Developer credentials and the desired redirect URI.

4. Run the application:

   ```bash
   python main.py
   ```

## Usage

### Authentication

The application uses the Spotify OAuth 2.0 flow for authentication.

### Commands

1. **Get Playlist as Text File**: Save the tracks of a selected playlist as a text file.

2. **Archive Collaborative Playlist as Text File**: Archive the tracks of a selected collaborative playlist with added-by information.

3. **I'm excited about this project and always thinking about what more to add**, some next features I want to add are YouTube playlist conversion both from and to spotify but YouTube API is horrid from my first encounters so don't expect that too soon. As well as YouTube DL integration, and liked song archival
## Contributing

Contributions are welcome! Open issues or pull requests for improvements or new features.

## License

This project is licensed under the MIT License.
```
Copyright 2023 Zaden Maestas

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```