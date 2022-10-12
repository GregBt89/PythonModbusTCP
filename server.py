import pandas as pd
from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep

DATA = pd.read_csv("data/2014JAN.csv", header=[0,1], chunksize=1, index_col=0)
SLEEP = 30 #seconds

scale = lambda x: int(x*10**3)

# Create an instance of ModbusServer
server = ModbusServer("0.0.0.0", 12345, no_block=True)

def streaming():
    incoming = next(DATA)["FD_083"]

    data = list(map(scale, incoming.values[0]))
    index = incoming.index.to_list()[0]
    
    date, time = index.split(' ')
    yr, mh, dy = date.split('.'); hr, me, sd = time.split('.')

    outgoing = list()
    outgoing = [int(yr), int(mh), int(dy), int(hr), int(me), int(sd)]
    outgoing.extend(data)
    return outgoing


try:
    print("Start server...")
    server.start()
    print("Server is online")
    while True:
        DataBank.set_words(0, streaming())
        sleep(SLEEP)
except:
    print("Shutdown server ...")
    server.stop()
    print("Server is offline")
