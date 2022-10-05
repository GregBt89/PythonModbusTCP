from pyModbusTCP.client import ModbusClient
from time import sleep

client = ModbusClient(host="127.0.0.1", port=12345)

client.open()
print(client.read_holding_registers(0))
client.close()


try:
    print("Open client connection ...")
    client.open()
    print("OPEN")
    state = [0]
    while True:
        print("Value of Register 1 : " + str(client.read_holding_registers(0)[0]))
        sleep(0.5)
except:
    print("Close client connection ...")
    client.close()
    print("CLOSED")