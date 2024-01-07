import cv2
import numpy as np
import textwrap
import re
import time

def parse_lrc(lrc_content):
    lrc_lines = lrc_content.split('\n')
    pattern = r'\[(\d{2}):(\d{2})\.(\d{2})\](.*)'
    parsed_lrc = []

    for line in lrc_lines:
        match = re.match(pattern, line)
        if match:
            minutes, seconds, centiseconds, lyric = match.groups()
            total_seconds = int(minutes) * 60 + int(seconds) + int(centiseconds) / 100
            parsed_lrc.append((total_seconds, lyric))

    return parsed_lrc

def wrap_text(text, font, max_width):
    lines = textwrap.wrap(text, width=max_width)
    return lines

def main(lrc_file_path):
    with open(lrc_file_path, 'r') as file:
        lrc_content = file.read()

    lyrics = parse_lrc(lrc_content)

    # Video properties
    fps = 24
    width, height = 640, 480
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (width, height))

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (255, 255, 255)
    line_type = 2
    max_line_length = 30

    current_index = 0
    current_time = 0
    frame_duration = 1 / fps

    while current_index < len(lyrics):
        start_time, lyric = lyrics[current_index]
        end_time = lyrics[current_index + 1][0] if current_index + 1 < len(lyrics) else start_time + 3  # 3 seconds for the last line
        wrapped_text = wrap_text(lyric, font, max_line_length)

        while current_time < end_time:
            if current_time >= start_time:
                frame = np.zeros((height, width, 3), np.uint8)
                y0, dy = 200, 40
                for i, line in enumerate(wrapped_text):
                    y = y0 + i*dy
                    cv2.putText(frame, line, (50, y), font, font_scale, font_color, line_type)
            else:
                frame = np.zeros((height, width, 3), np.uint8)  # Black frame for time before the start

            out.write(frame)
            current_time += frame_duration

        current_index += 1

    out.release()

if __name__ == "__main__":
    lrc_file_path = 'path_to_your_lrc_file.lrc'  # Replace with your LRC file path
    main(lrc_file_path)
