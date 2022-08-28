from machine import UART, Pin
from utime import sleep_ms, sleep

#Constants

class DFPlayer():
    UART_BAUD_RATE=9600
    UART_BITS=8
    UART_PARITY=None
    UART_STOP=1
    
    START_BYTE = 0x7E
    VERSION_BYTE = 0xFF
    COMMAND_LENGTH = 0x06
    ACKNOWLEDGE = 0x01
    END_BYTE = 0xEF
    COMMAND_LATENCY =   500


    def __init__(self, uartInstance, txPin, rxPin, busyPin):
        self.playerBusy=Pin(busyPin, Pin.IN, Pin.PULL_UP)
        self.uart = UART(uartInstance, baudrate=self.UART_BAUD_RATE, tx=Pin(txPin), rx=Pin(rxPin), bits=self.UART_BITS, parity=self.UART_PARITY, stop=self.UART_STOP)

    def split(self, num):
        return num >> 8, num & 0xFF

    def sendcmd(self, command, parameter1, parameter2):
        checksum = -(self.VERSION_BYTE + self.COMMAND_LENGTH + command + self.ACKNOWLEDGE + parameter1 + parameter2)
        highByte, lowByte = self.split(checksum)
        toSend = bytes([b & 0xFF for b in [self.START_BYTE, self.VERSION_BYTE, self.COMMAND_LENGTH, command, self.ACKNOWLEDGE,parameter1, parameter2, highByte, lowByte, self.END_BYTE]])
        #print(toSend)
        self.uart.write(toSend)

    def queryBusy(self):
        return not self.playerBusy.value()
        
    #Common DFPlayer control commands
    def nextTrack(self):
        self.sendcmd(0x01, 0x00, 0x00)

    def prevTrack(self):
        self.sendcmd(0x02, 0x00, 0x00)

    def increaseVolume(self):
        self.sendcmd(0x04, 0x00, 0x00)

    def decreaseVolume(self):
        self.sendcmd(0x05, 0x00, 0x00)

    def setVolume(self, volume):
        #Volume can be between 0-30
        self.sendcmd(0x06, 0x00, volume)

    def setEQ(self, eq):
        #eq can be o-5
        #0=Normal
        #1=Pop
        #2=Rock
        #3=Jazz
        #4=Classic
        #5=Base

        self.sendcmd(0x07, 0x00, eq)

    def setPlaybackMode(self, mode):
        #Mode can be 0-3
        #0=Repeat
        #1=Folder Repeat
        #2=Single Repeat
        #3=Random
        self.sendcmd(0x08, 0x00, mode)

    def setPlaybackSource(self, source):
        #Source can be 0-4
        #0=U
        #1=TF
        #2=AUX
        #3=SLEEP
        #4=FLASH
        self.sendcmd(0x09, 0x00, source)

    def standby(self):
        self.sendcmd(0x0A, 0x00, 0x00)

    def normalWorking(self):
        self.sendcmd(0x0B, 0x00, 0x00)

    def reset(self):
        self.sendcmd(0x0C, 0x00, 0x00)

    def resume(self):
        print('play')
        self.sendcmd(0x0D, 0x00, 0x00)

    def pause(self):
        print('pause')
        self.sendcmd(0x0E, 0x00, 0x00)

    def playTrack(self, folder, file):
        self.sendcmd(0x0F, folder, file)

    #Query System Parameters
    def init(self, params):
        self.sendcmd(0x3F, 0x00, params)



