#In order ror this example-code to work, make sure you have a
#card with at least one folder, containing at least two mp3:s.
#The folders should be named 01, 02 etc and files should be named
#001.mp3, 002.mp3 etc.
from utime import sleep_ms, sleep
from picodfplayer import DFPlayer


#Constants. Change these if DFPlayer is connected to other pins.
UART_INSTANCE=0
TX_PIN = 16
RX_PIN=17
BUSY_PIN=1

#Create player instance
player=DFPlayer(UART_INSTANCE, TX_PIN, RX_PIN, BUSY_PIN)


#Check if player is busy.
print('Playing', player.queryBusy())
#Play the first song (001.mp3) from the first folder (01)

player.playTrack(1,1)
#Wait 5 seconds...
sleep(5)

#Pause
player.pause()

#Wait 2 seconds...
sleep(2)

#Resume
player.resume()

#Wait 5 seconds
sleep(5)

#Next Track
player.nextTrack()
