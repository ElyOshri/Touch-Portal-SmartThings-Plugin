# Touch-Portal-SmartThings-Plugin
A SmartThings Plugin For Touch Portal

## Overview

This plugin is for controlling smart devices that are connected to SmartThings

## Features

* Lighting Control And States (Works)
* Switches And Dimmers Control And States (Works)
* Outlets And Plugs Control And States (Works)
* Thermostats Control And States (Needs Testing)(Nest Devices Are Not Supported)
* Door Lock Control And States (Works)
* Sensors States (Needs Testing)

## Installation Guide

Go to the releases:
https://github.com/ElyOshri/Touch-Portal-SmartThings-Plugin/releases

Get the latest version and there will be a TPP file you can download. From Touch Portal go to Import Plugin. Once you have done that add your SmartThings Api key which you can get from here: https://account.smartthings.com/tokens and enter it into the SmartThings plugin settings and restart the plugin.

After that you will have a list of new actions you can choose from. Also States are available for supported devices. You can see them from the Dynamic Text Updater, or you can add an option for "On Plugin State Change" then select the corresponding state and "Changes to". 

For Device ON or OFF state you need to use "on" or "off".

For RGB background color change or text color change you can use "When Plug-in State changes" and set it to "does not change to" and it the text you need to put "0" for it to work.


* Note: To add devices or scenes to the plugin after adding them to the app you need to restart the plugin.

* Note: Not all devices are not supported yet (please contact me to add the devices you want), the plugin should only allow you to do actions on the devices that support that type of action and the same is for States. (if your device doesn't show up in an action list or a state is created for it that means that it isn't supported)

## Troubleshooting

* If the plugin isn't working please go to ``%appdata%\TouchPortal\plugins\SmartThings`` and make sure that both exes are there like in this picture below, if they are missing (either one or both of them) please make sure that your anti-virus hasn't flagged them as malware (Most Anti Viruses Do That Because The Plugin Is Written In Python)
* ![image](https://user-images.githubusercontent.com/79017393/114606833-749dcb80-9ca4-11eb-853a-efd40a762be9.png)

* If that isn't the case I will be happy to help with anything you need in the ``SmartThings`` channel on Touch Portals discord server (https://discord.com/invite/MgxQb8r)



## Plugin Settings
* Api Key: The Api Key Of Your SmartThings (https://account.smartthings.com/tokens) 
* State Update Delay: The Time It Takes For States To Update
* Enable Log: If You Want To Troubleshoot This Would Create A Log ("On" or "Off")
* Enable Auto Update: If You Want The Plugin To Search For A New Version Every Time It Starts ("On" or "Off")
* Status: Shows The Status Of the Plugin (Connected, Invalid Key, Plugin Is Off, Disconnected)



Any Donations Are Welcome At www.paypal.me/ElyOshri 
