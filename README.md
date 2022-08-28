# PicoDFPlayer
MicroPython Driver for the DFPlayer (and clones) MP3 Player on Raspberry Pi Pico

This driver implements the serial UART communication protocol that the DFPlayer use and adds shorthand functions for the most common features for controlling the DFPlayer such as play a track, change volume, next/previous track, volume controls etc.

It is also possible to directly send commands to the DFPlayer through the driver, for instance if you want to handle the return values and/or use features that are not implemented as shorthand features.

