from synapse.switchboard import *

@setHook(HOOK_STARTUP)
def startupEvent():
    uniConnect(DS_TRANSPARENT, DS_STDIO) #From DS_TRANSPARENT to DS_STDIO
    
@setHook(HOOK_STDIN)    
def stdinEvent(data):
    print data
