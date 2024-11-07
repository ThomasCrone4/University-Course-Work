CSC1034: Practical 1
====================
Portfolio 1
===========

This package is build as a part of the CSC1034: Portfolio-1.

Type `python hello_world.py` to see some useful information.

# Argument Parsing

Scaling the panda, the function now takes scale as an argument.
By default, scale is set to 1. So the panda is normal size. However, if the function is called with a different
value of scale, the panda will change size proportionally
To implement this, I added scale as an argument of the walking panda function, as well as the cli function. 
I set the scale to be divided by 200, as the initial value of the pandas size was 0.005. So a scale of 1 would
produce the same sized panda

I also added "--moving" as a parameter to the function WalkingPanda and cli, which stops the panda from walking by not
calling the walking animation
I also added "--background" as a parameter to the function WalkingPanda and cli, which stops the background code 
from being ran
I also added "--rotate_speed" as a parameter to the function WalkingPanda, spinCameraTask and cli, which changes
the speed the camera rotates

# A multi media experience

I went on a website called pixabay and downloaded some ambient background music. Here is the link to the download:
https://pixabay.com/music/folk-village-background-music-village-music-no-copyright-203060/
I then downloaded the file, and added it into the walking_panda folder, and named the MP3 file "PandaMusic"
I then went to the site https://docs.panda3d.org/1.10/python/programming/audio/loading-playing-sounds-music
and read the panda3d directory. And it has the mySound function built into it.
I added the mySound function into the WalkingPanda function, so when the panda screen opens, the music starts playing