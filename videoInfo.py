#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Encoding: UTF-8

from pymediainfo import MediaInfo
from pprint import pprint as pp
from pathlib import Path

def videoInfo(path, file, verbose):

    media_info = MediaInfo.parse(file)
    for track in media_info.tracks:
        if track.track_type == "Video":
        
            print("Contains a video track")
                
            sortByResolution(file, track, path, verbose)
            
"""
            print("Bit rate: {t.bit_rate}, Frame rate: {t.frame_rate}, "
                "Format: {t.format}".format(t=track)
            )
            print("Duration (raw value):", track.duration)
            print("Duration (other values:")
            pprint(track.other_duration)
        elif track.track_type == "Audio":
            print("Track data:")
            pprint(track.to_data())
"""

def createDir(path, name, verbose):
    fullPath = Path(path, name)
    
    if (fullPath).is_dir():
        
        if verbose:
            print("Directory %s already exist" % fullPath)
            
    else:
            
        if verbose:
            print("Creating directory %s ..." % fullPath)
            
        fullPath.mkdir(parents=True, exist_ok=True)
        
def sortByResolution(file, track, path, verbose):
    
    width = track.width
    height = track.height
    
    print("Resolution: {}x{}".format(width, height))
        
    if width >= 7680 and height >= 4320:
        print("Is a 4320p video")
        sort(file, path, "4320p", verbose)
    elif width >= 3840 and height >= 2160:
        print("Is a 2160p video")
        sort(file, path, "2160p", verbose)
    elif width >= 2560 and height >= 1440:
        print("Is a 1440p video")
        sort(file, path, "1440p", verbose)
    elif width >= 1920 and height >= 1080:
        print("Is a 1080p video")
        sort(file, path, "1080p", verbose)
    elif width >= 1280 and height >= 720:
        print("Is a 720p video")
        sort(file, path, "720p", verbose)
    elif width >= 720 and height >= 480:
        print("Is a 480p video")
        sort(file, path, "480p", verbose)
    elif width >= 480 and height >= 360:
        print("Is a 360p video")
        sort(file, path, "360p", verbose)
    elif width >= 352 and height >= 288:
        print("Is a 288p video")
        sort(file, path, "288p", verbose)
    elif width >= 320 and height >= 240:
        print("Is a 240p video")
        sort(file, path, "240p", verbose)
    elif width >= 176 and height >= 144:
        print("Is a 144p video")
        sort(file, path, "144p", verbose)
    elif width >= 160 and height >= 120:
        print("Is a 120p video")
        sort(file, path, "120p", verbose)
    elif width >= 128 and height >= 96:
        print("Is a 96p video")
        sort(file, path, "96p", verbose)
    else:
        print("Sorting by bitrate")
        bitRate = int(track.bit_rate)
        print("Bit rate: %s kbps" % (bitRate / 1024))
#        sort(file, path, "h{}".format(height) , verbose)
        
def sort(file, path, dir, verbose):
    
        createDir(path, dir, verbose)
        
        fileName = Path(file).name
        
        if verbose:
            print("Moving %s to %s/%s" % (fileName, path, dir))
            
        newPath = Path(path, dir, fileName)
        
        file.rename(newPath)