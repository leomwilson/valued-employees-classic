from pypresence import Presence
import time, os

screen: int = 0 # 0 = log
log: str = 'Initializing the game...\n'

def update():
    os.system('clear || cls') # clear the console, compatible with *NIX and Windows
    if(screen == 0):
        print(log)

update()

try:
    rpc = Presence('565398225016586251')
    rpc.connect()
    rpc.update(state='Test', details='Classic')
    log += 'Discord Rich Presence initialized\n'
    update()
except:
    # The user doesn't have Discord running
    log += 'Discord Rich Presence\n'
    update()

while(True):
    time.sleep(60)