import aiohttp, asyncio, pysmartthings, time, requests, socket, json, sys, webbrowser, threading


TPHOST = '127.0.0.1'
TPPORT = 12136

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.connect((TPHOST, TPPORT))
s.sendall(b'{"type":"pair","id":"TPSmartThings"}\n')
data = s.recv(1024)
print(repr(data))
settings = (json.loads(data.decode('utf-8')))["settings"]

token = settings[0]['Api Key']

def WriteServerData(Serverinfo):
    '''
    This Function makes it eazier for write a log without repeating it
    '''
    if settings[2]["Enable Log"] == 'On':
        currenttime = (time.strftime('[%I:%M:%S:%p] '))
        logfile = open('log.txt', 'a')
        logfile.write(currenttime + "%s" % (Serverinfo))
        logfile.write('\n')
        logfile.close()
    elif settings[2]["Enable Log"] == 'Off':
        print(Serverinfo)

global Running

async def updateStates():
    async with aiohttp.ClientSession() as session:
        global api
        api = pysmartthings.SmartThings(session, token)
        global deviceList
        try:
            devices = await api.devices()
            s.sendall(('{"type": "settingUpdate", "name": "Status:", "value":Connected}\n').encode())
        except:
            s.sendall(('{"type": "settingUpdate", "name": "Status:", "value": "Invalid Key"}\n').encode())
            WriteServerData("Invalid Key Please Enter A Valid Key And Restart The Plugin")
            sys.exit()
        deviceList = {}
        deviceName = []
        for x in devices:
            deviceList[x.label] = x
            deviceName.append(x.label)
            await x.status.refresh()

            if x.status.values['switch'] != None:
                s.sendall(('{"type":"createState", "id":"%s", "desc":"SmartThings %s ON or OFF", "defaultValue":"0"}\n' % ("TPPlugin.SmartThings.device." + x.label + ".power", str(x.label))).encode())
                WriteServerData("Creating Power State For " + x.label)

            if x.status.values['level'] != None:
                s.sendall(('{"type":"createState", "id":"%s", "desc":"SmartThings %s Brightness", "defaultValue":"0"}\n' % ("TPPlugin.SmartThings.device." + x.label + ".CurrentBrightness", str(x.label))).encode())
                WriteServerData("Creating Brightness State For " + x.label)

            if x.status.values['color'] != None:
                s.sendall(('{"type":"createState", "id":"%s", "desc":"SmartThings %s Color", "defaultValue":"0"}\n' % ("TPPlugin.SmartThings.device." + x.label + ".Color", str(x.label))).encode())
                WriteServerData("Creating Color State For " + x.label)

            if x.status.values['hue'] != None:
                s.sendall(('{"type":"createState", "id":"%s", "desc":"SmartThings %s Hue", "defaultValue":"0"}\n' % ("TPPlugin.SmartThings.device." + x.label + ".Hue", str(x.label))).encode())
                WriteServerData("Creating Hue State For " + x.label)

            if x.status.values['saturation'] != None:
                s.sendall(('{"type":"createState", "id":"%s", "desc":"SmartThings %s Saturation", "defaultValue":"0"}\n' % ("TPPlugin.SmartThings.device." + x.label + ".Saturation", str(x.label))).encode())
                WriteServerData("Creating Saturation State For " + x.label)

            if x.status.values['colorTemperature'] != None:
                s.sendall(('{"type":"createState", "id":"%s", "desc":"SmartThings %s Color Temperature", "defaultValue":"0"}\n' % ("TPPlugin.SmartThings.device." + x.label + ".colorTemp", str(x.label))).encode())
                WriteServerData("Creating Color Temperature State For " + x.label)

            if x.status.values['temperature'] != None:
                s.sendall(('{"type":"createState", "id":"%s", "desc":"SmartThings %s Thermostat Temperature", "defaultValue":"0"}\n' % ("TPPlugin.SmartThings.device." + x.label + ".thermostatTemp", str(x.label))).encode())
                WriteServerData("Creating Temperature State For " + x.label)

            if x.status.values['thermostatMode'] != None:
                s.sendall(('{"type":"createState", "id":"%s", "desc":"SmartThings %s Thermostat Mode", "defaultValue":"0"}\n' % ("TPPlugin.SmartThings.device." + x.label + ".thermostatMode", str(x.label))).encode())
                WriteServerData("Creating Thermostat Mode State For " + x.label)

            if x.status.values["thermostatSetpoint"] != None:
                s.sendall(('{"type":"createState", "id":"%s", "desc":"SmartThings %s Thermostat Setpoint", "defaultValue":"0"}\n' % ("TPPlugin.SmartThings.device." + x.label + ".thermostatSetpoint", str(x.label))).encode())
                WriteServerData("Creating Thermostat Setpoint State For " + x.label)

            if x.status.values['motion'] != None:
                s.sendall(('{"type":"createState", "id":"%s", "desc":"SmartThings %s Motion Sensor", "defaultValue":"0"}\n' % ("TPPlugin.SmartThings.device." + x.label + ".motionSensor", str(x.label))).encode())
                WriteServerData("Creating Motion Sensor State For " + x.label)

            if x.status.values['contact'] != None:
                s.sendall(('{"type":"createState", "id":"%s", "desc":"SmartThings %s Contact Sensor", "defaultValue":"0"}\n' % ("TPPlugin.SmartThings.device." + x.label + ".contactSensor", str(x.label))).encode())
                WriteServerData("Creating Contact Sensor State For " + x.label)

            if x.status.values['presence'] != None:
                s.sendall(('{"type":"createState", "id":"%s", "desc":"SmartThings %s Presence Sensor", "defaultValue":"0"}\n' % ("TPPlugin.SmartThings.device." + x.label + ".presenceSensor", str(x.label))).encode())
                WriteServerData("Creating Presence Sensor State For " + x.label)

            if x.status.values['lock'] != None:
                s.sendall(('{"type":"createState", "id":"%s", "desc":"SmartThings %s Lock", "defaultValue":"0"}\n' % ("TPPlugin.SmartThings.device." + x.label + ".lock", str(x.label))).encode())
                WriteServerData("Creating Lock State For " + x.label)

            if x.status.values['windowShade'] != None:
                s.sendall(('{"type":"createState", "id":"%s", "desc":"SmartThings %s Window Shade", "defaultValue":"0"}\n' % ("TPPlugin.SmartThings.device." + x.label + ".windowShade", str(x.label))).encode())
                WriteServerData("Creating Window Shade State For " + x.label)






        oldStates = []
        while Running:
            states = []
            for x in deviceList:
                await deviceList[x].status.refresh()
                states.append(deviceList[x].status.values)

            if states != oldStates:
                oldStates = states
                for x in deviceList:
                    if deviceList[x].status.values['switch'] != None:
                        s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("TPPlugin.SmartThings.device." + x + ".power", deviceList[x].status.values['switch'])).encode())

                    if deviceList[x].status.values['level'] != None:
                        s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("TPPlugin.SmartThings.device." + x + ".CurrentBrightness", deviceList[x].status.level)).encode())

                    if deviceList[x].status.values['color'] != None:
                        s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("TPPlugin.SmartThings.device." + x + ".Color", "#ff" + deviceList[x].status.values['color'][1:255])).encode())

                    if deviceList[x].status.values['hue'] != None:
                        s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("TPPlugin.SmartThings.device." + x + ".Hue", round(float(deviceList[x].status.values['hue']), 1))).encode())

                    if deviceList[x].status.values['saturation'] != None:
                        s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("TPPlugin.SmartThings.device." + x + ".Saturation", round(float(deviceList[x].status.values['saturation']), 1))).encode())

                    if deviceList[x].status.values['colorTemperature'] != None:
                        s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("TPPlugin.SmartThings.device." + x + ".colorTemp", deviceList[x].status.values['colorTemperature'])).encode())

                    if deviceList[x].status.values['temperature'] != None:
                        s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("TPPlugin.SmartThings.device." + x + ".thermostatTemp", deviceList[x].status.values['temperature'])).encode())

                    if deviceList[x].status.values['thermostatMode'] != None:
                        s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("TPPlugin.SmartThings.device." + x + ".thermostatMode", deviceList[x].status.values['thermostatMode'])).encode())

                    if deviceList[x].status.values['thermostatSetpoint'] != None:
                        s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("TPPlugin.SmartThings.device." + x + ".thermostatSetpoint", deviceList[x].status.values['thermostatSetpoint'])).encode())

                    if deviceList[x].status.values['motion'] != None:
                        s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("TPPlugin.SmartThings.device." + x + ".motionSensor", deviceList[x].status.values['motion'])).encode())

                    if deviceList[x].status.values['contact'] != None:
                        s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("TPPlugin.SmartThings.device." + x + ".contactSensor", deviceList[x].status.values['contact'])).encode())

                    if deviceList[x].status.values['presence'] != None:
                        s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("TPPlugin.SmartThings.device." + x + ".presenceSensor", deviceList[x].status.values['presence'])).encode())

                    if deviceList[x].status.values['lock'] != None:
                        s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("TPPlugin.SmartThings.device." + x + ".lock", deviceList[x].status.values['lock'])).encode())

                    if deviceList[x].status.values['windowShade'] != None:
                        s.sendall(('{"type":"stateUpdate", "id":"%s", "value":"%s"}\n' % ("TPPlugin.SmartThings.device." + x + ".windowShade", deviceList[x].status.values['windowShade'])).encode())






            await asyncio.sleep(int(settings[1]["State Update Delay"]))
        sys.exit()

def TpConnection():
    global Running
    while Running:
        try:
            buffer = bytearray()
            while True:
                data = s.recv(1)
                if data != b'\n':
                    buffer.extend(data)
                else:
                    break
        except ConnectionResetError:
            WriteServerData(f"Shutdown TPSmartThingsPlugin-States...")
            Running = False
            break
        firstline = buffer[:buffer.find(b'\n')]
        print(firstline)
        WriteServerData(f"Reviced: {firstline}")
        d = firstline
        d = json.loads(d)

        if d['type'] == "closePlugin":
            WriteServerData(f"Shutdown TPSmartThingsPlugin-States...")
            s.sendall(('{"type": "settingUpdate", "name": "Status:", "value": "Plugin Is Off"}\n').encode())
            Running = False
            break

        if d['type'] == 'settings':
            settings[0]['Api Key'] = d['values'][0]['Api Key']
            settings[1]["State Update Delay"] = d['values'][1]['State Update Delay']
            settings[2]["Enable Log"] = d['values'][2]['Enable Log']
    sys.exit()

Running = True
t1 = threading.Thread(target=TpConnection,args=())
t1.start()
asyncio.run(updateStates())