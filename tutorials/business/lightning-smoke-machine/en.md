---
name: Lightning Smoke Machine
description: Trigger a smoke machine with a Lightning payment via ESP32.
---

![cover-lightning-smoke-machine](assets/cover.webp)


## Introduction


Transforms a classic smoke machine into a device payable in Bitcoin via Lightning Network. Each payment automatically triggers a jet of smoke!



- Level: Intermediate
- Estimated time: 2-3 hours
- Use cases: Bitcoin events, artistic performances, Lightning demos, automated stage effects


## Prerequisites


### Knowledge



 - Basic electronics (wiring, relays)
 - Welding (or use of Dupont connectors)
 - Network configuration (WiFi, WebSocket)


### Accounts required



- BTCPay Server: Functional instance (self-hosted or hosted)
- Blink Wallet : Account + access API


### Access



- Admin access to BTCPay Server
- WiFi connection for ESP32


## Materials required


### Hardware - Electronic components



- 1 Microcontroller - ESP32-WROOM-32

*The ESP32-WROOM-32 is a compact, low-cost WiFi/Bluetooth microcontroller for connecting electronic devices to the Internet and controlling them remotely*


![ESP32](assets/fr/1.webp)



- 1 Relay module - 5V with optocoupler

*A relay is like a switch that the ESP32 can operate to turn the smoke machine on or off*


![relay](assets/fr/2.webp)



- ~10 Dupont cables - Male/Male and Male/Female


![dupont-cables](assets/fr/3.webp)



- 1 Power supply for ESP32 - 5V USB or Li-Po battery


![battery](assets/fr/4.webp)



- 1 micro-USB cable - connection between ESP32 and power supply


![micro-usb-cables](assets/fr/5.webp)



- 1 220V fog machine with 12V battery remote control


![remote-and-smoke-machine](assets/fr/6.webp)



- 1 bottle of liquid compatible with your smoke machine


### Hardware - Tools



- Soldering iron + tin (if soldering)
- Screwdriver
- Multimeter (recommended)


### Software



- Firmware BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- WebSerial-compatible web browser (Chrome/Edge/Brave)
- BTCPay Server configured. For more information on creating a BTCPay Server instance, visit this tutorial: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


## System architecture


![architecture-lightning-smoke-machine](assets/fr/7.webp)


---


**⚠️** **SAFETY WARNING - READ BEFORE CONTINUING** **⚠️**


This project involves a fog machine connected to a **220V mains supply**. Improper operation can result in **fatal electrocution** or **fire**.


**Non-negotiable rules:**


1. **ALWAYS disconnect the smoke machine from the mains** before opening the remote control or tampering with the wiring

2. **Remove the battery from the remote control** before handling (risk of short-circuit and damage to components)

3. **Check that all your connections are isolated** before reconnecting anything

4. **Never reconnect the 220V** until the remote control box has been closed and secured


If you're not comfortable with this kind of handling, take someone with you who is.


---

## PART 1: Hardware assembly


### Step 1: Preparing the remote control


Objective: Connect the relay to the ON/OFF button on the remote control

1. Open remote control


    - Identify ON/OFF button
    - Unscrew the case to open the remote control

2. Locate connections


 - Locate the + and - terminals of the
 - Test continuity with a multimeter (optional)


![smoke-machine-remote](assets/fr/8.webp)


3. Button wiring (solder or connectors)


    - Solder a black cable to the - terminal of the button
    - Solder a red cable to the common + terminal


![smoke-machine-remote](assets/fr/9.webp)


### Step 2: Connecting to the relay module


**Reminder: Relay terminology



| **Terminal**         | **Description**           | **Function**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit open by default | Closes when the relay is activated |
| NC (Normally Closed) | Circuit closed by default  | Opens when the relay is activated  |
| COM (Common)         | Central terminal          | Switches between NO and NC              |

**Wiring from remote control to relay module:**


- Black wire from ON/OFF button **→** NO (Normally Open)
- Red wire (common) **→** COM (Common)


**Logic:**

When the ESP32 activates the relay, it connects COM and NO, which is exactly the same as pressing the remote control button.

When the ESP32 cuts the relay, COM and NO separate, which is equivalent to releasing the button.


![remote-relay](assets/fr/10.webp)


### Step 3: Connecting the ESP32 to the relay module


**Wiring diagram:**



| **ESP32** | **→** | **Relay Module** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |

**Verification:**


- VCC and GND well connected (polarity)
- GPIO 21 used for control signal
- No visible short circuit


![relay-esp32](assets/fr/11.webp)


**Checkpoint Hardware**

Before switching to the software, check :


- Correctly wired remote control
- Relay module connected to ESP32
- No bare wires touching other components
- 220V always disconnected


![relay-esp32](assets/fr/12.webp)




---


## PART 2: Software configuration


We'll use *Blink* as an example, but *BTCPay Server* also offers *Strike, Breez and Boltz* if you prefer another option.


### Step 1: Plugins, Installation *BitcoinSwitch* + *Blink


1 - Go to your *BTCPay Server* instance with an admin account


2 - Create your first blind


3 - On the left-hand side of *BTCPay Server*, scroll to the bottom and go to *"Manage Plugins "*


![btcpay-plugins](assets/fr/13.webp)


4 - We're going to install the *BitcoinSwitch* plugins as well as *Blink*


![btcpay-plugins](assets/fr/14.webp)


5 - Scroll down the list of plugins and click on *"Install "* : *BitcoinSwitch and Blink* (or the available wallet of your choice)


![btcpay-plugins](assets/fr/15.webp)


6 - Once the installation is complete, restart *BTCPay Server* and wait 1 minute for the instance to restart


![btcpay-plugins](assets/fr/16.webp)


7 - When you return to *"Manage plugins "*, check that both plugins have been installed


![btcpay-plugins](assets/fr/17.webp)


### Step 2: Backend : *BTCPay Server + Blink* configuration


**1 - Create a wallet *Blink***


- Visit https://www.blink.sv
- Create your account. Please refer to the tutorial :


[https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)


**2 - Generate a API key *Blink***


- Access the API interface: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** and log in with the same account you used to create your wallet *Blink*


![blink-api](assets/fr/18.webp)



   - Once connected, go to the *API Keys* tab


![blink-api](assets/fr/19.webp)



   - Click on *" + "* in the top right-hand corner to access your API Key configuration


![blink-api](assets/fr/20.webp)



   - Give your API Key a name and leave the default settings. Then, in the third step, make a note of your API Key - you'll only see it once: `blink_mZ5KxxxxxxxxxxxxxNbmX`


![blink-api](assets/fr/21.webp)



   - Once created, it should appear in your active API Key list.


![blink-api](assets/fr/22.webp)


**3 - Connect *Blink* to *BTCPay Server***


- Open your *BTCPay Server*
- Navigate to : *Wallet* **→** *Lightning*


![btcpay-server](assets/fr/23.webp)



- Click on *Use a custom node*
- Paste the following connection string:


```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```


**⚠️** **Important** :


- Do not modify the first part: `type=blink;server=https://api.blink.sv/graphql`;
- Replace only :
    - api-key= *by your API Blink* key
    - wallet-id= *by your wallet Blink* ID
- Then click on *Test connection*, then *Save*


![btcpay-server](assets/fr/24.webp)



 - Check that the connection is established (green status)


![btcpay-server](assets/fr/25.webp)


**4 - Create a Point of Sale (PoS)**


- In BTCPay Server, go to the *Plugins* tab and click on *Point of sale*


![btcpay-server](assets/fr/26.webp)



- Give your PoS a name and click on *Create*


![btcpay-server](assets/fr/27.webp)



- PoS configuration :
    - Choose a point of sale style = *Print display*
    - Currency = *SATS*
    - Click on *SAVE*


![btcpay-server](assets/fr/28.webp)



- Product configuration :
    - Delete all default products
    - Then click on *add item*


![btcpay-server](assets/fr/29.webp)


![btcpay-server](assets/fr/30.webp)



- Configure the product:
    - Title : *smoke-machine*
    - Price : *10 sats*
    - Bitcoin GPIO switch : 21
    - Bitcoin switch duration (in milliseconds) : 5000
    - Click on *Close* and then *Save* to save the new product


![btcpay-server](assets/fr/31.webp)


### Step 3: Firmware: Flashing the ESP32


**1 - Go to flash site


- Go to : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)


![bitcoinswitch-lnbits](assets/fr/32.webp)


**2 - Flash the BitcoinSwitch firmware**


- Connect the ESP32 to your computer with your USB/Micro-USB cable
- Then click on *Connect to Device*
- A window opens, select the USB port on your ESP32, then click on *Connect*


![bitcoinswitch-lnbits](assets/fr/33.webp)



- Once your ESP32 is connected, we'll flash the BitcoinSwitch firmware. In the *T-Display* section, click on *Upload Firmware* for the latest version available (currently: *bitcoinSwitch T-Display v1.0.1*)


![bitcoinswitch-lnbits](assets/fr/34.webp)



- Wait for the upload, the process is complete when the logs show *"Leaving... "*

![bitcoinswitch-lnbits](assets/fr/35.webp)



- Unplug the ESP32


**3 - Check BitcoinSwitch firmware installation


- Reload page: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- Reconnect the ESP32 to your computer with your USB/Micro-USB cable
- Then click on *Connect to device
- Select the USB port on your ESP32, then click on *Connect* as described above
- Once connected, press the **RESET** button on the ESP32
- Check in the logs that the last lines show :


```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```


(This is normal, it means that there is no config yet, but that the firmware has been installed)


![bitcoinswitch-lnbits](assets/fr/36.webp)


**4 - Generate WebSocket LNURL** URL


Expected final format :


```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```


Generation steps :


- Open yourBTCPay Server instance, then go to the PoS we created later.
- Then click on "View" to open your PoS in the browser


![btcpay-server-https](assets/fr/37.webp)



- Copy the URL of the page, for example :


![btcpay-server-https](assets/fr/38.webp)


Let's unpack this URL:


```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



- `XXXXv` → the domain of your BTCPay Server instance
- `46XXXXXXXXXXXXXXXXXXXXwFB` → your PoS unique identifier
- `/pos` → indicates a Point of Sale


Transform it:


- Replace `https://` with `wss://`
- Add `/bitcoinswitch` at the end


Result:


```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```


Keep this URL for future configuration, as it will enable your ESP32 to communicate in real time with BTCPay Server. The WebSocket protocol (`wss://`) establishes a permanent connection between the two: as soon as a Lightning payment is confirmed on your PoS, BTCPay instantly sends the information to the ESP32, which can then trigger your smoke machine.


**5 - Configuring WiFi and WebSocket


- Return to the page: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) with your ESP32 connected
- Go to *Configure Device* → *Wifi Settings*


Inform :


- WiFi SSID: the name of your WiFi network
- WiFi Password: your WiFi password


![bitcoinswitch-lnbits](assets/fr/39.webp)



- In the *LNbits Device URL* section, paste the WebSocket URL created in the previous step
- Click on *Upload config*


![bitcoinswitch-lnbits](assets/fr/40.webp)



- Wait for the upload to complete; the logs should display the parameters you've just entered (SSID, password and WebSocket URL)


![bitcoinswitch-lnbits](assets/fr/41.webp)



- Wait while ESP32 establishes the WebSocket connection. You should see :


```
WiFi connection established!

[WebSocket] Connected to url: ...
```


![bitcoinswitch-lnbits](assets/fr/42.webp)



- You can now disconnect the ESP32


---
## Checkpoint Software


Before the final test, check :



- Blink connected to BTCPay
- PoS created with at least 1 item
- ESP32 flashed with BitcoinSwitch
- WiFi configured on ESP32
- WebSocket URL correct
- Error-free ESP32 logs


---

## Testing and debugging


### Complete final test


1. Plug in the smoke machine (220V) and switch it on

2. Power the ESP32 (battery or USB)

3. Open your BTCPay PoS in your browser

4. Scan "smoke-machine" item

5. Pay with a wallet Lightning (Blink or other wallet)

6. Observe:


 - Relay clicks (audible sound and relay LED lights up)
 - The smoke machine is activated
 - Smoke generated!


### Fairness problems and solutions



| **Problem**                        | **Probable Cause**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 does not connect            | Missing USB driver             | Install [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relay does not click                | Wrong GPIO wiring            | Check GPIO 21 → IN                                                                        |
| Smoke machine does not respond         | Remote control improperly wired         | Check NO/NC/COM                                                                           |
| WebSocket timeout                   | Incorrect URL                  | Check wss:// and /bitcoinswitch                                                            |
| WiFi does not connect             | SSID/Password incorrect            | Re-flash WiFi config                                                                    |
| Payment received but nothing happens | ESP32 not connected to WebSocket | Check RESET logs                                                                      |

## Resources


### Useful links



- BitcoinSwitch Firmware: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- BTCPay Server Docs : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 Pinout : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)


### Community & Support



- BTCPay Server** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Official Mattermost
- BTCPay Server Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - Official Telegram, active community
- BitcoinSwitch (firmware bugs)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)


### Source code



- BitcoinSwitch firmware source code: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)


---

**⚡** Stack sats, make smoke, have fun, stay humble! **⚡**