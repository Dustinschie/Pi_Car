#!/bin/bash

#	make stream directory in /tmp/
	mkdir /tmp/stream

#	start the Camera
raspistill --nopreview -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 10 -t 9999999 -th 0:0:0 &

#	Start MJPG-Streamer
LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -i "input_file.so -f /tmp/stream -n pic.jpg" -o "output_http.so -w /usr/local/www"

