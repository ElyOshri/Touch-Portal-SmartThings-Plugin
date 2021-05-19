
# Touch-Portal-SmartThings-Plugin
A SmartThings Plugin For Touch Portal

[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/ElyOshri/Touch-Portal-SmartThings-Plugin?include_prereleases&label=Release)](https://github.com/ElyOshri/Touch-Portal-SmartThings-Plugin/releases/tag/v1.0)
[![Downloads](https://img.shields.io/github/downloads/ElyOshri/Touch-Portal-SmartThings-Plugin/total?label=Downloads)](https://github.com/ElyOshri/Touch-Portal-SmartThings-Plugin/releases)
[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://www.paypal.me/ElyOshri1)



## Overview

This plugin is for controlling smart devices that are connected to SmartThings

## Features

* Lighting Control And States 
* Switches And Dimmers Control And States
* Outlets And Plugs Control And States 
* Thermostats Control And States (Nest Devices Are Not Supported)
* Door Lock Control And States
* Window Shade Control And States 
* Sensors States

## Installation Guide

Go to the releases:
https://github.com/ElyOshri/Touch-Portal-SmartThings-Plugin/releases

Get the latest version and there will be a TPP file you can download. From Touch Portal go to Import Plugin. Once you have done that add your SmartThings Api key which you can get from here: https://account.smartthings.com/tokens and enter it into the SmartThings plugin settings and restart the plugin.

After that you will have a list of new actions you can choose from. Also States are available for supported devices. You can see them from the Dynamic Text Updater, or you can add an option for "On Plugin State Change" then select the corresponding state and "Changes to". 

For Device ON or OFF state you need to use "on" or "off".

For RGB background color change or text color change you can use "When Plug-in State changes" and set it to "does not change to" and it the text you need to put "0" for it to work.


* Note: To add devices or scenes to the plugin after adding them to the app you need to restart the plugin.

* Note: Not all devices are not supported yet (please contact me to add the devices you want), the plugin should only allow you to do actions on the devices that support that type of action and the same is for States. (if your device doesn't show up in an action list or a state is created for it that means that it isn't supported)

## Troubleshooting - Windows

* If the plugin isn't working please go to ``%appdata%\TouchPortal\plugins\SmartThings`` and make sure that both exes are there like in this picture below, if they are missing (either one or both of them) please make sure that your anti-virus hasn't flagged them as malware (Most Anti Viruses Do That Because The Plugin Is Written In Python)
 
 ![image](https://user-images.githubusercontent.com/79017393/114606833-749dcb80-9ca4-11eb-853a-efd40a762be9.png)
 
 * If that isn't the case I will be happy to help with anything you need in the ``SmartThings`` channel on Touch Portal's discord server (https://discord.com/invite/MgxQb8r)

## Troubleshooting - MacOS

* If the plugin isn't working please go to `Documents/TouchPortal/plugins/SmartThings` and check the two log files if they say: `Permission denied`. open the Terminal and run these two commends:
* `cd Documents/TouchPortal/plugins/SmartThings` 
* `chmod 777 SmartThings_Plugin*` 
* Another problem could be that your anti virus flagged the two Unix executables that are in `Documents/TouchPortal/plugins/SmartThings` and are shown in the picture below, if one of them is missing check your anti virus and make sure that either of them didn't get flagged as malware and try to reinstall the plugin. (Most Anti Viruses Do That Because The Plugin Is Written In Python)

![image](https://user-images.githubusercontent.com/79017393/118855602-98c17d80-b8de-11eb-99dc-8221a37888ab.png)

* If that isn't the case I will be happy to help with anything you need in the ``SmartThings`` channel on Touch Portal's discord server (https://discord.com/invite/MgxQb8r)

## Possible State Values

* Switch - `on` or `off`
* Brightness - `0 - 100`
* Color - `#00000000 - #FFFFFFFF`
* Hue - `0 - 100`
* Saturation - `0 - 100`
* Color Temperature - `1 - 30000` (depending on the device)
* Thermostat Temperature - `-460 - 10000` (depending on chosen unit `C` or `F`)
* Thermostat Mode -  `auto`, `cool`, `eco`, `rush hour`, `emergency heat`, `heat`, `off`
* Thermostat Setpoint - `-460 - 10000` (depending on chosen unit `C` or `F`)
* Motion Sensor - `active` or `inactive`
* Contact Sensor - `closed` or `open`
* Presence Sensor - `present` or `not present`
* Lock - `locked`, `unlocked`, `unlocked with timeout`, `unknown`
* Window Shade - `closed`, `closing`, `open`, `opening`, `partially open`, `unknown`

## Plugin Settings
* Api Key: The Api Key Of Your SmartThings (https://account.smartthings.com/tokens) 
* State Update Delay: The Time It Takes For States To Update
* Enable Log: If You Want To Troubleshoot This Would Create A Log ("On" or "Off")
* Enable Auto Update: If You Want The Plugin To Search For A New Version Every Time It Starts ("On" or "Off")
* Status: Shows The Status Of the Plugin (Connected, Invalid Key, Plugin Is Off, Disconnected)



Any Donations Are Welcome At www.paypal.me/ElyOshri1 
