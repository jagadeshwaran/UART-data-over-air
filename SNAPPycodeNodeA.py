from synapse.switchboard import *

@setHook(HOOK_STARTUP)
def startupEvent():
    initUart(1, 9600) # <= put your desired baudrate here!
    flowControl(1, False) # <= set flow control False as it is not needed
    uniConnect(DS_TRANSPARENT, DS_STDIO) #From DS_TRANSPARENT to DS_STDIO
    
@setHook(HOOK_STDIN)    
def stdinEvent(data):
    print data
