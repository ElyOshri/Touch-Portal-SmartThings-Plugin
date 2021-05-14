import aiohttp, asyncio, pysmartthings, time, requests, socket, json, sys, webbrowser


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
    if settings[2]["Enable Log"] == 'On':
        currenttime = (time.strftime('[%I:%M:%S:%p] '))
        logfile = open('log.txt', 'a')
        logfile.write(currenttime + "%s" % (Serverinfo))
        logfile.write('\n')
        logfile.close()
    elif settings[2]["Enable Log"] == 'Off':
        print(Serverinfo)

#Todo: fix auto update
if settings[3]["Enable Auto Update"] == "On":
    WriteServerData(f"Checking for updates")
    try:
        CheckingUpdateFile = requests.get("https://api.github.com/repos/ElyOshri/Touch-Portal-SmartThings-Plugin/tags").json()
        if str(CheckingUpdateFile[0]['name']) != "v1.0":
            WriteServerData(f"Found a updated version: {CheckingUpdateFile[0]['name']}")
            WriteServerData("New version is availble please update")
            webbrowser.get().open_new_tab('https://github.com/ElyOshri/Touch-Portal-SmartThings-Plugin/releases')
        if str(CheckingUpdateFile[0]['name']) == "v1.0":
            WriteServerData(f"No new verison is available")
    except:
        WriteServerData("User Passed Update Check Rate Limit")




async def main():
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
        switchList = []
        switchLevelList = []
        colorHSList = []
        colorRGBList = []
        colorTempList = []
        thermostatModeList = []
        lockList = []
        windowList = []
        for x in devices:
            deviceList[x.label] = x
            await x.status.refresh()
            for i in x.capabilities:
                if i == "switch":
                    switchList.append(x.label)
                if i == "switchLevel":
                    switchLevelList.append(x.label)
                if i == "colorControl" and x.status.values['hue'] != None:
                    colorHSList.append(x.label)
                if i == "colorContorl" and x.status.values['color'] != None:
                    colorRGBList.append(x.label)
                if i == "colorTemperature":
                    colorTempList.append(x.label)
                if i == "thermostatMode":
                    thermostatModeList.append(x.label)
                if i == "lock":
                    lockList.append(x.label)
                if i == 'windowShade':
                    windowList.append(x.label)
        WriteServerData(deviceList)
        if switchList != []:
            s.sendall(('{"type":"choiceUpdate", "id":"TPPlugin.SmartThings.Actions.Data.SwitchList", "value":%s}\n' % switchList).encode())

        if switchLevelList != []:
            s.sendall(('{"type":"choiceUpdate", "id":"TPPlugin.SmartThings.Actions.Data.SwitchLevelList", "value":%s}\n' % switchLevelList).encode())

        if colorHSList != []:
            s.sendall(('{"type":"choiceUpdate", "id":"TPPlugin.SmartThings.Actions.Data.ColorHSList", "value":%s}\n' % colorHSList).encode())

        if colorRGBList != []:
            s.sendall(('{"type":"choiceUpdate", "id":"TPPlugin.SmartThings.Actions.Data.ColorRGBList", "value":%s}\n' % colorRGBList).encode())

        if colorTempList != []:
            s.sendall(('{"type":"choiceUpdate", "id":"TPPlugin.SmartThings.Actions.Data.ColorTempList", "value":%s}\n' % colorTempList).encode())

        if thermostatModeList != []:
            s.sendall(('{"type":"choiceUpdate", "id":"TPPlugin.SmartThings.Actions.Data.ThermostatList", "value":%s}\n' % thermostatModeList).encode())

        if lockList != []:
            s.sendall(('{"type":"choiceUpdate", "id":"TPPlugin.SmartThings.Actions.Data.LockList", "value":%s}\n' % lockList).encode())

        if windowList != []:
            s.sendall(('{"type":"choiceUpdate", "id":"TPPlugin.SmartThings.Actions.Data.WindowShadeList", "value":%s}\n' % windowList).encode())




        global sceneList
        scenes = await api.scenes()
        sceneList = {}
        scencName = []
        for x in scenes:
            sceneList[x.name] = x
            scencName.append(x.name)
        s.sendall(('{"type":"choiceUpdate", "id":"TPPlugin.SmartThings.Actions.SceneTigger.Data.SceneList", "value":%s}\n' % scencName).encode())



        Running = True

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
                WriteServerData(f"Shutdown TPSmartThingsPlugin-Main...")
                Running = False
                sys.exit()
            firstline = buffer[:buffer.find(b'\n')]
            print(firstline)
            WriteServerData(f"Reviced: {firstline}")
            d = firstline
            d = json.loads(d)
            if d['type'] == "closePlugin":
                WriteServerData(f"Shutdown TPSmartThingsPlugin-Main...")
                s.sendall(('{"type": "settingUpdate", "name": "Status:", "value": "Plugin Is Off"}\n').encode())
                Running = False
                sys.exit()
            if d['type'] == 'settings':
                settings[0]['Api Key'] = d['values'][0]['Api Key']
                settings[2]["Enable Log"] = d['values'][2]['Enable Log']
                settings[3]["Enable Auto Update"] = d['values'][3]['Enable Auto Update']

            if d['type'] != 'closePlugin' and Running and d['type'] != 'listChange' and d['type'] != "settings" and d[
                'type'] != "broadcast":
                try:
                    if d['data'][0]['value'] != "" and d['data'][1]['value'] != "":
                        try:
                            if d['actionId'] == 'TPPlugin.SmartThings.Actions.OnOFFTigger' and d['data'][0]['value'] == "ON":
                                WriteServerData("Turning On " +d['data'][1]['value'])
                                await deviceList[d['data'][1]['value']].switch_on()
                            elif d['actionId'] == 'TPPlugin.SmartThings.Actions.OnOFFTigger' and d['data'][0]['value'] == "OFF":
                                WriteServerData("Turning Off " +d['data'][1]['value'])
                                await deviceList[d['data'][1]['value']].switch_off()

                            if d['actionId'] == "TPPlugin.SmartThings.Actions.Bright" and d['data'][1]['id'] == "TPPlugin.SmartThings.Actions.DataBright":
                                WriteServerData("Changing " + d['data'][0]['value'] + "Brightness To " + d['data'][1]['value'])
                                await deviceList[d['data'][0]['value']].set_level(int(d['data'][1]['value']), 1)

                            if d['actionId'] == 'TPPlugin.SmartThings.Actions.Toggle' and d['data'][1]['id'] == 'TPPlugin.SmartThings.Actions.UnusedData':
                                WriteServerData("Toggling " + d['data'][0]['value'])
                                await deviceList[d['data'][0]['value']].status.refresh()
                                state = deviceList[d['data'][0]['value']].status.switch
                                if state:
                                    await deviceList[d['data'][0]['value']].switch_off()
                                elif not state:
                                    await deviceList[d['data'][0]['value']].switch_on()

                            if d['actionId'] == "TPPlugin.SmartThings.Actions.RGBColor" and d['data'][1]['id'] == "TPPlugin.SmartThings.Actions.DataRGB":
                                WriteServerData("Changing " + d['data'][0]['value'] + " RGB To " + d['data'][1]['value'])
                                await deviceList[d['data'][0]['value']].command("main", "colorControl", "setColor", [{"hex" : d['data'][1]['value']}])


                            if d['actionId'] == "TPPlugin.SmartThings.Actions.HSColor" and d['data'][1]['id'] == "TPPlugin.SmartThings.Actions.DataRGBHue":
                                WriteServerData("Changing " + d['data'][0]['value'] + " Hue To " + d['data'][1]['value'] + " And Saturation To " + d['data'][2]['value'])
                                await deviceList[d['data'][0]['value']].command("main", "colorControl", "setColor", [{"hue": float(d['data'][1]['value']) ,"saturation": float(d['data'][2]['value'])}])

                            if d['actionId'] == "TPPlugin.SmartThings.Actions.ExecuteScene" and d['data'][1]['id'] == 'TPPlugin.SmartThings.Actions.UnusedData':
                                WriteServerData("Executing "+d['data'][0]['value']+" Scene")
                                await sceneList[d['data'][0]['value']].execute()

                            if d['actionId'] == "TPPlugin.SmartThings.Actions.Temp" and d['data'][1]['id'] ==  "TPPlugin.SmartThings.Actions.DataTemp":
                                WriteServerData("Settings "+d['data'][0]['value']+" Color Temp To " + d['data'][1]['value'])
                                await deviceList[d['data'][0]['value']].command("main", "colorTemperature", "setColorTemperature", [int(d['data'][1]['value'])])

                            if d['actionId'] == "TPPlugin.SmartThings.Actions.Brightness_Down" and d['data'][1]['id'] == "TPPlugin.SmartThings.Actions.DataBrightDown":
                                WriteServerData("Brighness Down By "+d['data'][1]['value']+" To " + d['data'][0]['value'])
                                await  deviceList[d['data'][0]['value']].status.refresh()
                                state = deviceList[d['data'][0]['value']].status.level
                                if state <= int(d['data'][1]['value']):
                                    state += 1
                                await deviceList[d['data'][0]['value']].set_level(state - int(d['data'][1]['value']), 1)

                            if d['actionId'] == "TPPlugin.SmartThings.Actions.Brightness_Up" and d['data'][1]['id'] == "TPPlugin.SmartThings.Actions.DataBrightUp":
                                WriteServerData("Brighness Up By "+d['data'][1]['value']+" To " + d['data'][0]['value'])
                                await  deviceList[d['data'][0]['value']].status.refresh()
                                state = deviceList[d['data'][0]['value']].status.level
                                await deviceList[d['data'][0]['value']].set_level(state + int(d['data'][1]['value']), 1)

                            if d['actionId'] == "TPPlugin.SmartThings.Actions.ThermostatMode" and d['data'][1]['id'] == "TPPlugin.SmartThings.Actions.DataThermostatMode":
                                WriteServerData("Settings " +d['data'][0]['value']+ " Thermostat Mode To " +d['data'][1]['value'])
                                if d['data'][1]['value'] == "auto":
                                    await deviceList[d['data'][0]['value']].command("main", "thermostatMode", "auto")
                                elif d['data'][1]['value'] == "cool":
                                    await deviceList[d['data'][0]['value']].command("main", "thermostatMode", "cool")
                                elif d['data'][1]['value'] == "heat":
                                    await deviceList[d['data'][0]['value']].command("main", "thermostatMode", "hear")
                                elif d['data'][1]['value'] == "off":
                                    await deviceList[d['data'][0]['value']].command("main", "thermostatMode", "off")

                            if d['actionId'] == "TPPlugin.SmartThings.Actions.ThermostatSetpointHeat" and d['data'][1]['id'] == "TPPlugin.SmartThings.Actions.DataThermostatSetpointHeat":
                                WriteServerData("Setting Heating Temp To " + d['data'][1]['value'] + "On Device: " + d['data'][0]['value'])
                                await deviceList[d['data'][0]['value']].command("main", "thermostatHeatingSetpoint", "setHeatingSetpoint", [int(d['data'][1]['value'])])

                            if d['actionId'] == "TPPlugin.SmartThings.Actions.ThermostatSetpointCool" and d['data'][1]['id'] == "TPPlugin.SmartThings.Actions.DataThermostatSetpointCool":
                                WriteServerData("Setting Cooling Temp To " + d['data'][1]['value'] + "On Device: " + d['data'][0]['value'])
                                await deviceList[d['data'][0]['value']].command("main", "thermostatCoolingSetpoint", "setCoolingSetpoint", [int(d['data'][1]['value'])])

                            if d['actionId'] == "TPPlugin.SmartThings.Actions.Lock" and d['data'][1]['id'] == "TPPlugin.SmartThings.Actions.DataLock":
                                if d['data'][1]['value'] == "lock":
                                    WriteServerData("Locking " + d['data'][0]['value'])
                                    await deviceList[d['data'][0]['value']].command("main","lock","lock")
                                elif d['data'][1]['value'] == "unlock":
                                    WriteServerData("Unlocking " + d['data'][0]['value'])
                                    await deviceList[d['data'][0]['value']].command("main","lock","unlock")

                            if d['actionId'] == "TPPlugin.SmartThings.Actions.WindowShade" and d['data'][1]['id'] == "TPPlugin.SmartThings.Actions.DataWindowShade":
                                if d['data'][1]['value'] == "open":
                                    WriteServerData("Opening " + d['data'][0]['value'])
                                    await deviceList[d['data'][0]['value']].command("main","windowShade","open")
                                elif d['data'][1]['value'] == "close":
                                    WriteServerData("Closing " + d['data'][0]['value'])
                                    await deviceList[d['data'][0]['value']].command("main","windowShade","close")
                                elif d['data'][1]['value'] == "stop":
                                    WriteServerData("Stopping " + d['data'][0]['value'])
                                    await deviceList[d['data'][0]['value']].command("main", "windowShade", "presetPosition")


                        except:
                            WriteServerData("User inputted wrong values or passed connection rate limit")

                except KeyError:
                    WriteServerData('User did not input values')

asyncio.run(main())
