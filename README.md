# Touch-Portal-SmartThings-Plugin
A SmartThings Plugin For Touch Portal

## Overview

This plugin is for controlling smart devices that are connected to SmartThings

## Features

* Lighting Control And States (Works)
* Switches And Dimmers Control And States (Works)
* Outlets And Plugs Control And States (Works)
* Thermostats Control And States (Needs Testing)
* Door Lock Control And States (Needs Testing)
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

## Plugin Settings
* Api Key: The Api Key Of Your SmartThings (https://account.smartthings.com/tokens) 
* State Update Delay: The Time It Takes For States To Update
* Enable Log: If You Want To Troubleshoot This Would Create A Log ("On" or "Off")
* Enable Auto Update: If You Want The Plugin To Search For A New Version Every Time It Starts ("On" or "Off")
* Status: Shows The Status Of the Plugin (Connected, Invalid Key, Plugin Is Off, Disconnected)



Any Donations are welcome at www.paypal.me/ElyOshri 
