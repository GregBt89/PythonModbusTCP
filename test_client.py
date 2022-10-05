from pyModbusTCP.client import ModbusClient
from time import sleep

client = ModbusClient(host="10.30.244.10", port=12345, debug=False)

try:
    print("Open client connection ...")
    client.open()
    print("OPEN")
    while True:
        for i in range(6):
            print(f"Value of Register {i} : " + str(client.read_holding_registers(i)[0]))
        for i in range(6, 18):
            print(f"Value of Register {i} : " + str(client.read_holding_registers(i)[0]/10**3))
        sleep(5)

except:
    print("Close client connection ...")
    client.close()
    print("CLOSED")