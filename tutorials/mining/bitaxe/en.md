---
name: Setting Up a BitAxe
Description: How to set up a BitAxe?
---

### Introduction

BitAxe is an open-source project created by Skot and [available on GitHub](https://github.com/skot/bitaxe) that allows for cost-effective mining experimentation.

It has reverse-engineered the workings of the famous Antminer S19 by Bitmain, the market leader in ASICs, the specialized machines for bitcoin mining. Now, it's possible to use these powerful chips in new open-source projects. Unlike the Nerdminer, BitAxe has sufficient computing power to be connected to a mining pool, which will allow you to regularly earn some satoshis. The Nerdminer, on the other hand, can only be connected to what’s called a solopool, which functions like a lottery ticket: you have a slim chance of winning the full block reward.

There are several versions of BitAxe, with different chips and performances:

| Bitaxe Model Series      | ASIC Chip | Used On                     | Expected Hash Rate          | Ideal For                                                                                                  |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Series 100)  | 1 x BM1397| Antminer Series 17          | 400 GH/s (up to 450 GH/s)   | Bitcoin mining beginners, offering a solid hash rate with moderate power consumption.                      |
| Bitaxe Ultra (Series 200)| 1 x BM1366| Antminer S19 XP and S19k Pro| 500 GH/s (up to 550 GH/s)   | Serious miners aiming to balance efficiency and higher hash rate.                                          |
| Bitaxe Hex (Series 300)  | 6 x BM1366| Antminer S19k Pro and S19 XP| 3.0 TH/s (up to 3.3 TH/s)   | Miners seeking scalability and high performance without sacrificing efficiency.                             |
| Bitaxe Supra (Series 400)| 1 x BM1368| Antminer S21                | 600 GH/s (up to 700 GH/s)   | Serious enthusiasts seeking the highest hash rates and efficiency.                                         |

In this tutorial, we will be using a BitAxe Ultra 204 equipped with a BM1366 chip, used for the Antminer S19XP. This one is already assembled and flashed by the retailer.

### [The list of retailers is available on this page](https://bitaxe.org/legit.html)

![signup](assets/2.webp)

Generally, the power supply is sold with it. If not, you will need to purchase a power supply with a 5V jack cable and at least 4A.

![signup](assets/1.webp)

### Configuration
When you first plug in your BitAxe, it will attempt to connect to a Wi-Fi network by default. After five attempts, it will display the name of its own Wi-Fi network so you can connect to it and configure it.
To do this, you can use any computer or smartphone. Go to your Wi-Fi settings, search for new networks, and you will see a Wi-Fi called Bitaxe_XXXX. Here, it is `Bitaxe_A859`. Connect to this Wi-Fi network, and a window will automatically open.

![signup](assets/3.webp)

In this window, click on the three small horizontal bars at the top left, then on `Settings`.

![signup](assets/4.webp)

You will need to manually enter your Wi-Fi network information, as there is no automatic discovery system.

![signup](assets/5.webp)

Therefore, indicate the SSID of the Wi-Fi, that is, the name of your network, the password, as well as the information of the mining pool you have chosen. Be careful, here the URL of the pool is not presented in the same way. For example, for Braiins, the pool URL provided is: `stratum+tcp://eu.stratum.braiins.com:3333`.

![signup](assets/6.webp)

As you can see on the screen, you need to remove the `stratum+tcp://` and `:3333` parts, leaving only `eu.stratum.braiins.com`. Then, in the `Port` field, enter the 4 digits at the end of the URL given by the pool, but without the `:`. Here, it is therefore `3333`.

In this tutorial, we are using the Braiins mining pool, but you are free to choose another one. You can find our tutorials on mining pools [on the PlanB Network website](https://planb.network/en/tutorials/mining).

Next, in `User`, enter your identifier and then the `Password`, usually, it is `"x"` or `"Anything123"`.

The `Core Voltage` setting should be left at `1200` by default, and for `Frequency`, also leave the default value initially. It will be possible to adjust this setting later to obtain more computing power. However, it is important to ensure that the chip's temperature does not exceed 65-70°C, as the BitAxe does not have a system to reduce performance in case of overheating. If the temperature exceeds 65°C too much, it could damage your BitAxe.

![signup](assets/7.webp)

Once you have correctly entered all the settings, click the `Save` button at the bottom, then restart your BitAxe simply by unplugging it and plugging it back in.
If you have entered your information correctly, the device should quickly connect to your Wi-Fi, then to the mining pool, and start to display some information on its small screen. It will probably take a few minutes for it to appear on the mining pool's dashboard.
### Dashboard and Screen

Three different displays will scroll through. On the third page, you will see the `IP` information, which is the IP address that allows you to connect to the dashboard. Here, the address is `192.168.1.19`.

![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)

To access the dashboard, simply enter this address into your internet browser.

On the dashboard, you will find all the information displayed on the small screen, which we will now look at in detail.

![signup](assets/11.webp)

| BitAxe Screen | Dashboard                                   | Description                                                                                                                                                                                                               |
| ------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gh            | Hashrate                                    | The current computing power, expressed in GigaHash/s                                                                                                                                                                      |
| W/THs         | Efficiency                                  | This is the efficiency of your BitAxe expressed in W/THs. It's the ratio between the electrical power consumed and the computing power produced.                                                                          |
| A/R           | Shares                                      | Quantity of `Shares` sent by your BitAxe to the pool, representing the amount of work provided.                                                                                                                          |
| UT            | Uptime                                      | Time since your BitAxe has been operating without interruption (available in the left menu under `Logs`).                                                                                                                |
| BD            | Best Difficulty                             | Maximum difficulty reached since the last restart. For comparison, the current network difficulty is about 85T.                                                                                                          |
| FAN           | FAN in the `Heat` box                       | Fan rotation speed, expressed in rotations per minute.                                                                                                                                                                    |
| Temp          | ASIC temperature in the `Heat` box          | Chip temperature, which should not exceed 65°C.                                                                                                                                                                           |
| Pwr           | Power                                       | Power in watts consumed. However, this information does not take into account the screen, the fan, or the power supply. For example, when it displays 11.7W, the total consumption is actually 15.8W.                    |
| mV mA         | Input Voltage Input Current                 | Voltage and current consumed by the machine. The power in watts is equal to the voltage multiplied by the current.                                                                                                        |
| FH            | Free Heap Memory (left menu -> `Logs`)      | The available memory.                                                                                                                                                                                                     |
| vCore         | ASIC Voltage (in the Performance box)       | Voltage measured on the ASIC chip.                                                                                                                                                                                        |
| IP            | NA                                          | IP Address.                                                                                                                                                                                                               |
| V2.1.0       | Version (left menu -> `Logs`)               | Firmware version.                                                                                                                                                                                                         |
You can change the Wi-Fi or pool settings at any time without any problem.  
Depending on the ventilation and the temperature of your room, you may need to increase or might have to decrease the performance so that the temperature does not exceed 65°C. If you increase the performance, you will earn more satoshis, but your BitAxe will also consume more electricity!