import serial
import time
import collections
import matplotlib.pyplot as plt # type: ignore
import matplotlib.animation as animation # type: ignore
from matplotlib.lines import Line2D # type: ignore
import numpy as np # type: ignore
import pymongo # type: ignore

#Remplazar el enlace de secuencia con la conexion de desarrollo de MongoDB.
conn_str= "mongodb://localhost:27017/"

#Pon 5 segundos de espera de conexion
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

try:
    print(client.server_info())
except Exception:
    print("Incapaz de conectar con el servidor.")

def getSerialData(self,Samples,numData,serialConnection,lines):
    for i in range(numData):
        value = float(serialConnection.readline().strip())
        data[i].append(value)
        lines[i].set_data(range(Samples),data[i])

serialPort= 'COM3'
baudRate = 9600

try:
    serialConnection = serial.Serial(serialPort, baudRate)
except:
    print("Imposible conectar con el puerto")

Samples = 50
sampleTimes = 150
numData = 4

xmin = 0
xmax = Samples
ymin = [0, 0, -50, 0]
ymax =[6, 6, 50, 100]
lines = []
data = []

for i in range(numData):
    data.append(collections.deque([0] * Samples, maxlen=Samples))
    lines.append(Line2D([], [], color='blue'))

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1, xlim=(xmin, xmax), ylim=(ymin[0], ymax[0]))
ax1.title.set_text('Primera trazada')
ax1.set_xlabel("Samples")
ax1.set_ylabel("Volts")
ax1.add_line(lines[0])

ax2 = fig.add_subplot(2, 2, 2, xlim=(xmin, xmax), ylim=(ymin[1], ymax[1]))
ax2.title.set_text('Segunda trazada')
ax2.set_xlabel("Samples")
ax2.set_ylabel("Volts")
ax2.add_line(lines[1])

ax3 = fig.add_subplot(2, 2, 3, xlim=(xmin, xmax), ylim=(ymin[2], ymax[2]))
ax3.title.set_text('Tercera trazada')
ax3.set_xlabel("Samples")
ax3.set_ylabel("Temperature")
ax3.add_line(lines[2])

ax4 = fig.add_subplot(2, 2, 4, xlim=(xmin, xmax), ylim=(ymin[3], ymax[3]))
ax4.title.set_text('Cuarta trazada')
ax4.set_xlabel("Samples")
ax4.set_ylabel("Humidity")
ax4.add_line(lines[3])

anim= animation.FuncAnimation(fig,getSerialData, fargs=(Samples, numData, serialConnection, lines), interval=sampleTimes)
plt.show()

serialConnection.close()