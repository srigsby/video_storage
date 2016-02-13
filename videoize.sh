#!/bin/sh
./file2pics.py $1
ffmpeg -r 1 -start_number 0 -i test%d.jpg -c:v huffyuv video.avi
# ffmpeg -r 1 -start_number 0 -i test%d.jpg -c:v libx264 -preset ultrafast -qp 0 output.mkv
# rm *.jpg