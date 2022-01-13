#!/usr/bin/env python
# coding: utf-8

# Automatic Streaming Highlights Module for Desktop App

import os
import time
import numpy as np # for numerical operations
from moviepy.editor import VideoFileClip, concatenate, ipython_display

def get_automatic_highlights(videoFileName): 

    # Expecting videoFileName as:
    # videoFileName = "streaming2p3.mp4" 

    # Function returns a video containing the automatic highlights

    curDir = os.getcwd()
    print(curDir)

    start = time.time()

    clip = VideoFileClip(videoFileName)
    cut = lambda i: clip.audio.subclip(i,i+1).to_soundarray(fps=22000)
    volume = lambda array: np.sqrt(((1.0*array)**2).mean())
    volumes = [volume(cut(i)) for i in range(0,int(clip.duration-1))]

    end = time.time()

    _duration = end - start 

    print(f'Time of the algorithm: {round(_duration,2)} seconds.')

    # From [1]:
    # It is much clearer if we compute the average volumes over periods of 10 seconds:
    averaged_volumes = np.array([sum(volumes[i:i+10])/10 
                                for i in range(len(volumes)-10)])

    # Modified comments from [[1]](http://zulko.github.io/blog/2014/07/04/automatic-soccer-highlights-compilations-with-python/):
    # 
    # As we can see in the above graph, there are some higher peaks that give us the loudest times of the recorded videogame, 
    # but other peaks may also indicate interesting events. In the next lines, we select the times of the 10% highest peaks:

    increases = np.diff(averaged_volumes)[:-1]>=0
    decreases = np.diff(averaged_volumes)[1:]<=0
    peaks_times = (increases * decreases).nonzero()[0]
    peaks_vols = averaged_volumes[peaks_times]
    peaks_times = peaks_times[peaks_vols>np.percentile(peaks_vols,90)] # Can change the 90 to 80 or 70 to include more highlights.

    final_times=[peaks_times[0]]
    for t in peaks_times:
        if (t - final_times[-1]) < 60:
            if averaged_volumes[t] > averaged_volumes[final_times[-1]]:
                final_times[-1] = t
        else:
            final_times.append(t)

    print(final_times)

    start = time.time()
    final = concatenate([clip.subclip(max(t-5,0),min(t+5, clip.duration))
                        for t in final_times])

    # highlightVideoName = 'streaming2p3_cuts.mp4' # Uncomment this line and comment the below one if you want to manually insert
                                                # your outputVideoName

    highlightVideoName = videoFileName.split('.mp4')[0]+"_automatic_highlights.mp4" 

    final.to_videofile(highlightVideoName) # Low quality is the default
    end = time.time()

    _duration = end - start 

    print(f'Time of the algorithm: {round(_duration,2)} seconds.')
