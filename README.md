# LRC to Video Converter

## Overview
This script converts LRC (Lyric) files into videos displaying the lyrics synchronized with the timing specified in the LRC file. It's a perfect tool for creating karaoke-style videos or simple lyric videos for any song.

## Features
- Parses LRC files and extracts timing and lyrics.
- Generates a video with synchronized lyrics.
- Customizable video properties like frame rate, dimensions, and font settings.

## Prerequisites
To run this script, you need to have Python installed on your system along with the following libraries:
- OpenCV (`cv2`)
- NumPy (`numpy`)

## Installation
1. Clone the repository:
`git clone https://github.com/CarlosATeixeira/LRC_to_text_renderer`

2. Install the required Python libraries:
`pip install opencv-python numpy`

## Usage
1. Prepare your LRC file with the lyrics and timings.
2. Place the LRC file in an accessible directory.
3. Run the script with the path to your LRC file:
`python main.py 'path_to_your_lrc_file.lrc'`

Replace `script_name.py` with the name of your script and `'path_to_your_lrc_file.lrc'` with the path to your LRC file.
4. The script will generate a video file named `output_video.mp4` in the same directory.

## Customization
You can customize the following video properties in the script:
- Frame rate (`fps`)
- Video dimensions (`width`, `height`)
- Font style, scale, and color
- Maximum line length for text wrapping

## Contributing
Feel free to fork the repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
