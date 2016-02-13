#!/bin/sh
youtube-dl -f 22 $1
ffmpeg -i outputlate-yZwoMROzlB4.mp4 -vf fps=1 out%d.jpg
./pics2file