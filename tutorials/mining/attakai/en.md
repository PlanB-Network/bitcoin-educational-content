---
name: Attakaï

description: transforming an S9 into a home heating system
---

![cover](assets/cover.webp)

# Attakai - making home mining possible and accessible!

The "Attakaï" initiative explores Bitcoin mining using the generated heat. The guide offers solutions to make miners suitable for use as radiators in homes, providing more comfort and energy savings. Bitcoin automatically adjusts the mining difficulty and rewards miners for their work. However, the concentration of hashrate can pose risks to network neutrality. "Attakaï" provides a practical guide for retrofitting miners economically, allowing participants to reduce their electricity bills and be rewarded with sats without KYC.

## Introduction

"Attakaï," which means "ideal temperature" in Japanese, is the name of the initiative aimed at discovering bitcoin mining through the reuse of heat launched by @ajelexBTC and @BlobOnChain with Découvre Bitcoin. This ASIC retrofitting guide will serve as a basis for learning more about mining, its operation, recent history, and the underlying economy.

### Why reuse the heat from an ASIC?

It is important to understand the relationship between energy and heat production in an electrical system.

For an investment of 1 kW of electrical energy, an electric radiator produces 1 kW of heat, neither more nor less. New radiators are not more efficient than traditional radiators. Their advantage lies in their ability to distribute heat continuously and evenly in a room, providing more comfort compared to traditional radiators that alternate between high heating power and no heating, thus generating regular temperature variations and discomfort.

A computer, or more broadly an electronic board, does not consume energy to perform calculations; it simply needs energy to flow through its components to function. Energy consumption is due to the electrical resistance of the components, which produces losses and thus generates heat, which is known as the Joule effect.
Some companies have come up with the idea of ​​pooling the need for computing power and heating needs through radiator/servers. The idea is to distribute a company's servers into small units that could be placed in homes or offices. However, this idea encounters several problems. The need for servers is not related to the need for heating, and companies cannot use the computing capacity of their servers flexibly. There are also limits to the bandwidth that individuals can possess. All these constraints prevent the company from making these expensive installations profitable or providing a stable online server offering without data centers capable of taking over when heating is not needed.

> The heat from your computer is not wasted if you need to heat your home. If you use electric heating where you live, then the heat from your computer is not wasted. It costs the same if you generate this heat with your computer. If you have a cheaper heating system than electric, then the waste is only in the cost difference. If it's summer and you use air conditioning, then it's double.
> Bitcoin mining should take place where it is cheaper. Maybe it will be where the climate is cold and where heating is electric, where mining would become free.

_As Satoshi Nakamoto said on August 8, 2010._

Bitcoin and its proof of work stand out because they automatically adjust the mining difficulty based on the amount of computing done by the entire network, this amount is called the hashrate and is expressed in hashes per second. Today it is estimated at 280 Exahashes per second, or 280 billion billion hashes per second. This hashrate represents work and therefore an amount of energy expended. The higher the hashrate, the higher the difficulty increases, and vice versa. Thus, a Bitcoin miner can be activated or deactivated at any time without any impact on the network, unlike radiator/servers that would need to remain stable to offer their service. The miner is rewarded for the work done relative to the work of others, no matter how small this participation may be.

In summary, an electric radiator and a Bitcoin miner both produce 1 kW of heat for 1 kW of electricity consumed. However, the miner also receives bitcoins as a reward. Regardless of the price of electricity, the price of bitcoin, or the competition of mining activity on the Bitcoin network, it is economically more advantageous to heat with a miner rather than an electric radiator.

![Video presentation](https://youtu.be/gKoh44UCSnE)

### The added value for Bitcoin

We will not go into the details of mining operation here (resources available on the academy if needed). What is important to understand is how mining contributes to the decentralization of Bitcoin. Several existing technologies have been ingeniously combined to bring Nakamoto's consensus to life. This consensus economically rewards honest actors for their participation in the operation of the Bitcoin network, while discouraging dishonest actors. This is one of the key points that allows the network to exist sustainably.

Honest actors, those who mine according to the rules, are all competing with each other to obtain the largest possible share of the reward for producing new blocks. This economic incentive naturally leads to a form of centralization as companies choose to specialize in this lucrative activity by reducing their costs through economies of scale. These industrial actors have an advantageous position for purchasing and maintaining machines, as well as negotiating bulk electricity rates.

> At first, most users would run network nodes, but as the network grew beyond a certain point, it would be left more and more to specialists with server farms of specialized hardware. A server farm would only need to run one node on the network and the rest of the LAN connects with that one node.

_As Satoshi Nakamoto stated on November 2, 2008_

Certain entities hold a considerable percentage of the total hashrate in large mining farms. We can observe the recent cold wave in the United States where a significant portion of the hashrate was taken offline to redirect energy to households with an exceptional need for electricity. For several days, miners were economically incentivized to turn off their farms, and thus we can see this exceptional weather on the Bitcoin hashrate curve.

This issue could become problematic and pose a significant risk to the neutrality of the network. An actor possessing more than 51% of the hashrate could more easily censor transactions if they wished. That is why it is important to distribute the hashrate among multiple actors rather than centralized entities that could be more easily seized by a government, for example.

**If miners are spread across thousands, or even millions, of households around the world, it becomes very complicated for a state to take control of them.**

'At the factory, a miner is not suitable to be used as a radiator in a housing, due to two main problems: excessive noise and lack of adjustment. However, these problems can be easily solved through simple modifications made to the hardware and software, allowing for a much quieter miner that can be configured and automated like modern electric heaters.

**Attakaï is an educational initiative that teaches you how to retrofit the Antminer S9 in the most cost-effective way possible.**

This is an excellent opportunity to learn by practicing. In addition to reducing your electricity bill, you are rewarded for your participation with free KYC sats.

## Chapter 1: Buying Guide for a Used ASIC

In this section, we will discuss best practices for purchasing a used Bitmain Antminer S9, the machine on which this radiator retrofitting tutorial will be based. This guide also applies to other ASIC models as it is a general buying guide for used mining hardware.

The Antminer S9 is a device offered by Bitmain since May 2016. It consumes 1323W of electricity and produces 13.5 TH/s. Although it is considered old, it remains an excellent option for starting mining. Since it has been produced in large quantities, it is easy to find spare parts abundantly in many regions of the world. It can generally be acquired peer-to-peer on sites such as Ebay or LeBonCoin, as professional resellers no longer offer it due to its lower competitiveness compared to newer machines. It is less efficient than ASICs like the Antminer S19, introduced since March 2020, but this makes it an affordable used hardware and more suitable for the modifications we will make.

The Antminer S9 comes in several variations (i, j) that bring minor modifications to the first-generation hardware. We do not believe that this should influence your purchasing decision, and this guide will work for all these variations.

The price of ASICs varies depending on many factors such as the price of bitcoin, network difficulty, machine efficiency, and electricity cost. Therefore, it is difficult to give an accurate estimate for purchasing a used machine. In February 2023, the expected price in France generally ranges between €100 and €200, but these prices are subject to change rapidly.

![image](assets/guide-achat/1.webp)

The Antminer S9 is composed of the following parts:

- 3 hashboards where the chips that produce the hashing power are located

![image](assets/guide-achat/2.webp)'

- A control board that includes a slot for an SD card, an Ethernet port, and connectors for hashboards and fans. This is the brain of your ASIC.
  ![image](assets/guide-achat/3.webp)

- 3 data cables that connect the hashboards to the control board.

![image](assets/guide-achat/4.webp)

- The power supply that operates on 220V and can be plugged in like a regular household appliance.

![image](assets/guide-achat/5.webp)

- 2 120mm fans.

![image](assets/guide-achat/6.webp)

- A male C13 cable.

![image](assets/guide-achat/7.webp)

When buying a used machine, it is important to check that all parts are included and functional. During the exchange, you should ask the seller to turn on the machine to verify its proper functioning. It is important to check that the device turns on correctly, and then check the internet connectivity by connecting an Ethernet cable and accessing the Bitmain connection interface via a web browser on the same local network. You can find this IP address by connecting to your internet router interface and looking for connected devices. This address should have the following format: 192.168.x.x

![image](assets/guide-achat/8.webp)

Also, check that the default credentials work (username: root, password: root). If the default credentials do not work, you will need to perform a machine reset.

![image](assets/guide-achat/9.webp)

Once connected, you should be able to see the status of each hashboard on the dashboard. If the miner is connected to a pool, you should see all the hashboards functioning. It is important to note that miners make a lot of noise, which is normal. Also, make sure the fans are functioning properly.

You can then remove the previous owner's mining pool to set up your own later. If desired, you can also inspect the hashboards by disassembling the machine. However, this step is more complex and requires more time and certain tools. If you want to proceed with this disassembly, you can refer to the next part of this tutorial that details how to do it. It is important to note that miners collect a lot of dust and require regular maintenance. You can observe this dust accumulation and the quality of maintenance by disassembling the machine.
After reviewing all these points, you can purchase your machine with a high degree of confidence. If in doubt, reach out to the community, and if you need equipment to complete this tutorial, feel free to send us a message.
To summarize this guide in one sentence:

> Don't trust, verify.

## Chapter 2: Buying Guide for Modification Parts

![image](assets/piece/1.webp)

### How to transform your Antminer S9 into a silent and connected heater?

If you own an Antminer S9, you probably know how loud and bulky it can be. However, it is possible to transform it into a silent and connected heater by following a few simple steps. In this article, we will present the necessary equipment for making the modifications, while a later article will explain in detail the steps to follow to make these changes.

### 1. Replace the fans

The original fans of the Antminer S9 are too loud to use it as a heater. The solution is to replace them with quieter fans. Our team has tested several models from the Noctua brand and selected the Noctua NF-A14 iPPC-2000 PWM as the best compromise. Be sure to choose the 12V version of the fans. This 140mm fan can produce up to 1300W of heat while maintaining a theoretical noise level of 31 dB. To mount these 140mm fans, you will need a 140mm to 120mm adapter, which you can find on the DécouvreBitcoin store. We will also add 140mm protective grilles.

![image](assets/piece/1.webp)
![image](assets/piece/2.webp)
![image](assets/piece/3.webp)

The power supply fan is also quite noisy and needs to be replaced. We recommend the Noctua NF-A6x25 PWM. Note that the connectors of the Noctua fans are not the same as the original ones, so you will need a connector adapter to connect them. Two should be enough. Again, make sure to choose the 12V version of the fan.

![image](assets/piece/4.webp)
![image](assets/piece/5.webp)

### 2. Add a WIFI/Ethernet bridge

Instead of using an Ethernet cable, you can connect your Antminer to WIFI by adding a WIFI/Ethernet bridge. We have selected the vonets vap11g-300 because it easily allows you to retrieve the WIFI signal from your Internet box and transmit it to your Antminer via Ethernet without creating a subnet. If you have electrical skills, you can power it directly with the Antminer's power supply without the need to add a USB charger. For this, you will need a female 5.5mmx2.1mm jack.

![image](assets/piece/6.webp)
![image](assets/piece/7.webp)

### 3. Optional: Add a smart plug

If you want to turn on/off your Antminer from your smartphone and monitor its power consumption, you can add a smart plug. We tested the ANTELA plug in the 16A version, compatible with the smartlife application. This smart plug allows you to check the daily and monthly power consumption and connects directly to your Internet box via WIFI.
![image](assets/piece/8.webp)

**List of equipment and links:**

- 2X 3D adapter piece 140mm to 120mm
- 2X NF-A14 iPPC-2000 PWM [link](https://www.amazon.fr/Noctua-nf-polarized-A14-industrialppc-PWM-2000/dp/B00KESSUDW)
- 2X 140mm fan grilles [link](https://www.amazon.fr/dp/B06XD4FTSQ)
- Noctua NF-A6x25 PWM [link](https://www.amazon.fr/Noctua-nf-a6-25-PWM-Ventilateur-Marron/dp/B00VXTANZ4)
- Electrician's sugar 2.5mm2 [link](https://www.amazon.fr/Legrand-LEG98433-Borne-raccordement-Nylbloc/dp/B00BBHXLYS)
- Vonets vap11g-300 [link](https://www.amazon.fr/Vonets-VAP11G-300-Bridge-convertit-Ethernet/dp/B014SK2H6W)

## Chapter 3 - TUTORIAL: How to Turn a Miner into a Heater?

If you are a skilled DIYer and looking to turn a miner into a heater, this tutorial is for you. We want to warn you that modifying an electronic device can pose electrical and fire risks. It is essential to take all necessary precautions to avoid any damage or injury.
Out of the factory, a miner is not really usable as a radiator in a home because it is too noisy and not adjustable. However, it is possible to make simple modifications to solve these problems.

**Note:** It is essential to have previously installed Braiins OS+ on your miner or any other software that can reduce the performance of your machine. This measure is crucial because, in order to reduce noise, we will install **less powerful fans that can dissipate less heat**.

### Required Materials

- 2 pieces 3D adapter 140mm to 120mm
- 2 Noctua NF-A14 iPPC-2000 PWM fans
- 2 140mm fan grilles
- 1 Noctua NF-A6x25 PWM fan
- 2.5mm² electrician's sugar
- Vonets VAP11G-300
- Optional: ANTELA smart plug

### Replacing the Fans

We will start by replacing the power supply fan.

**Note**: First and foremost, before starting, make sure you have unplugged your miner to avoid any risk of electrocution.

![image](assets/hardware/1.webp)

We will start by replacing the power supply fan.

First, remove the 6 screws on the side of the case that hold it closed. Once the screws are removed, gently open the case to remove the plastic cover that protects the components.

![image](assets/hardware/2.webp)
![image](assets/hardware/3.webp)'
Next, it is time to remove the original fan, taking care not to damage the other components. To do this, remove the screws holding it in place and gently peel off the white glue surrounding the connector. It is important to proceed delicately to avoid damaging the wires or connectors.
![image](assets/hardware/4.webp)

Once the original fan is removed, you will notice that the connectors of the new Noctua fan do not match those of the original fan. Indeed, the new fan has 3 wires, including a yellow wire that allows for speed control. However, this wire will not be used in this specific case. To connect the new fan, it is recommended to use a special adapter. However, it is important to note that this adapter can sometimes be difficult to find.

![image](assets/hardware/5.webp)

If you do not have this adapter, you can still proceed to connect the new fan using a wire nut. To do this, you will need to cut the cables of the old and new fan.

![image](assets/hardware/6.webp)
![image](assets/hardware/7.webp)

On the new fan, use a cutter and carefully cut the contours of the main sheath at 1cm without cutting the sheaths of the cables below.

![image](assets/hardware/8.webp)

Then, by pulling the main sheath downwards, cut the sheaths of the red and black cables in the same way as before. And cut the yellow cable flush.

![image](assets/hardware/9.webp)

On the old fan, it is more delicate to cut the main sheath without damaging the sheaths of the red and black wires. For this, we used a needle that we slid between the main sheath and the red and black wires.

![image](assets/hardware/10.webp)
![image](assets/hardware/11.webp)

Once the red and black wires are exposed, cut the sheaths carefully to avoid damaging the electrical wires.

![image](assets/hardware/12.webp)

Then, connect the cables with a wire nut, the black wire with the black and the red wire with the red. You can also add electrical tape.

![image](assets/hardware/13.webp)
![image](assets/hardware/14.webp)

Once the connection is made, it is time to install the new Noctua fan with the grille and the old screws, the new screws that are in the box will be reused later. Make sure to place it with the correct orientation. You will notice an arrow on one side of the fan, indicating the direction of the airflow. It is important to place the fan so that this arrow points towards the inside of the case. Then, reconnect the fan.
![image](assets/hardware/15.webp)
![image](assets/hardware/16.webp)

**Optional:** If you are skilled in electricity, you can directly add a female 5.5mm jack connector to the 12V power output, which will allow you to directly power the Vonet Wi-Fi bridge. However, if you are unsure of your electrical skills, it is best to use the USB connector with a smartphone charger to avoid any risk of short circuit or electrical damage.

![image](assets/hardware/17.webp)

Once the connections are made, make sure to place the plastic cover over the plastic casing and not inside.

![image](assets/hardware/18.webp)

Finally, put the casing cover back in place and screw the 6 screws on the sides to hold everything securely in place. And there you have it, your power supply casing is now equipped with a new fan.

### Replacement of the 2 main fans

1. First, unplug the fans and unscrew them.
   ![image](assets/hardware/19.webp)

2. The connectors of the new Noctua fans do not match the original ones, but don't panic! Take out your cutter and carefully cut the small plastic tabs so that the connectors fit perfectly with your miner.

![image](assets/hardware/20.webp)
![image](assets/hardware/21.webp)

3. It's time to install the 3D parts!
   Attach them on both sides of the miner using the screws that you removed from the fans. Screw until the screw head goes into the 3D part and it is securely held in place. Be careful not to tighten too much, as you could deform the part and one of the screws may touch a capacitor! Then carefully cut the small plastic tabs so that the connectors fit perfectly with your miner.

![image](assets/hardware/22.webp)

4. Now let's move on to the fans.
   Attach them to the 3D parts using the screws provided in the box. Pay attention to the direction of air flow, the arrows on the sides of the fans will indicate the direction to follow. Go from the Ethernet port side to the other side. See photo below.

![image](assets/hardware/23.webp)
![image](assets/hardware/24.webp)
![image](assets/hardware/25.webp)

5. Last step: plug in the fans and attach the grilles on top with the unused screws from the fan box. You only have 4, but 2 per grille in opposite corners will be enough. You can also look for other similar screws in a hardware store if needed.

![image](assets/hardware/26.webp)
![image](assets/hardware/27.webp)

While waiting to be able to offer a sexier casing for your new heater, you can attach the case and the power supply together with electrician's cable ties.

![image](assets/hardware/28.webp)

And for the finishing touch, connect the Vonet bridge to the Ethernet port on its power supply. If you haven't done so already, you can follow this tutorial to set up your bridge.

![image](assets/hardware/29.webp)

And there you have it, congratulations! You have just replaced the entire mechanical part of your miner. You should now hear much less noise.

## Chapter 4 - Software Modification - Resetting an Antminer S9

**Article series proposed by BlobOnChain & Ajelex - 15/02/2023**

### Reset via the "Reset" button

This method can be applied within 10 minutes after starting the miner.

After turning on the miner for 2 minutes, please press the "Reset" button for 5 seconds, then release it. The miner will be restored to factory settings within 4 minutes and will automatically restart (there is no need to turn it off).

![image](assets/software/1.webp)

Restore via web side

Log in to the user interface of your miner, click on "Upgrade" >> "Perform a reset", then click "OK" in the pop-up window.

### Original operating system

For this part, we will assume that the machine is working, running, and its original operating system is installed. We will briefly see the interface of the original operating system offered by Bitmain.

First, connect to your machine through your local network:

![image](assets/software/2.webp)

Once on the login page, you will need to log in to the ASIC using the default credentials:

- username: root
- password: root

**How to reset if the default password doesn't work?**

The main operating system is relatively basic. With the 4 tabs: System, Miner Configuration, Miner Status, Network. In the Miner Configuration tab, you can configure up to 3 mining pools.

![image](assets/software/3.webp)

In the Miner Status tab, you can observe various information about the live operation of the ASIC. The hashrate expressed in GH/s, more detailed information about the pool, as well as details about the status of each hashboard and the fan speed in rotations/minute.

![image](assets/software/4.webp)

### Braiins OS+

Now, we will study the software for ASICs Braiins OS+ (https://braiins.com/os/plus). The software is developed by the company [Braiins](https://braiins.com/), which is the parent company of the mining pool Braiins Pool (https://braiins.com/pool). This mining pool currently has 4.39% of the global hashrate at the time of writing these lines. The Prague-based company was formerly known as Slushpool and is the first mining pool that started in November 2010. [Here](https://mempool.space/mining/pool/braiinspool) you shall find updated hashrate and pool dominance stats.

Today, the company, with its various activities, offers profitability study tools for mining (https://insights.braiins.com/en), mining farm management solutions in parallel with its pool activity, and its optimization software for ASICs. It also offers mining using the new Stratum V2 protocol (https://braiins.com/bitcoin-mining-stack-upgrade).

We will therefore study in more detail the operation of Bitmain devices, which are currently the only compatible models:

- S19, S19 Pro, S19j, S19j Pro, T19,

- 17, S17 Pro, S17+, S17e, T17, T17+, T17e & S9 [i, j]

The Braiins OS software can be easily installed on all the machines mentioned above. It will allow for more precise control of a machine by allowing overclocking or underclocking. It also allows fine-tuning of the frequency of each chip through an automatic optimization feature called autotuning. Since each hashing chip is slightly different due to its manufacturing process, the software tests the optimal frequency for each chip to achieve maximum efficiency (W/THs). The software claims to achieve performance that can be 25% higher than the original. According to our measurements, it is possible to achieve these figures.

## Installation of Braiins OS+

There are several ways to install Braiins OS+ on an ASIC. You can refer to this guide as well as the official documentation from Braiins and video tutorials.
Installing Braiins OS+ directly on the memory of the Antminer

Learn how to easily install Braiins OS+ directly on the memory of your Antminer using BOS toolbox, replacing the original operating system, through the detailed steps below. If you want to keep the original OS in parallel, you can install Braiins OS+ on an SD card.

1. Power on your Antminer and connect it to your internet box.
2. Download BOS toolbox Windows / Linux.
3. Unzip the downloaded file and open the bos-toolbox.bat file, choose the language, and after a moment you will see this window:
   ![image](assets/software/5.webp)
4. Bos toolbox will allow you to easily find the IP address of your Antminer and install Braiins OS+. If you already know the IP address of your machine, you can skip to step 8. Otherwise, go to the scan tab.
   ![image](assets/software/6.webp)
5. Usually, on home networks, the IP address range is between 192.168.1.1 and 192.168.1.255, so enter "192.168.1.0/24" in the IP range field. If your network is different, please change these addresses. Then click on "Start".
6. Attention, if the Antminer has a password, the detection will not work. If that's the case, the simplest solution is to perform a factory reset.
7. You should see all the Antminers on your network, here the IP address is 192.168.1.37.
   ![image](assets/software/7.webp)
8. Click on Back, then go to the install tab, enter the previously found IP address in the Miner(s) field and "admin" (or "root") in the Password field, which is the default password, then click on "Start".
   If the installation does not work with "admin" or "root" as the password, it may be necessary to perform a factory reset and try again.
   ![image](assets/software/8.webp)
9. After a few moments, your Antminer will restart and you will be able to access the Braiins OS+ interface at the IP address in question, here 192.168.1.37, directly in the address bar of your browser. The default username is "root" and there is no default password.
   ![image](assets/software/9.webp)
   ![image](assets/software/10.webp)

Installing Braiins OS+ on an SD card is the second method, it uses the original interface of your Antminer. This method works for machines with an operating system dating from before 2019.

### Antminer Interface

1. Download the new operating system to be installed.
2. As in the previous section, connect to your machine through your local network.
3. Go to the System tab and then Upgrade.
4. Load the file you downloaded and flash the image.

![image](assets/software/11.webp)

### Micro SD Card

A second method allows you to use a micro SD card. This method only works with machines with an operating system dating from after 2019.

1. Download the new operating system to be installed.
2. Flash the downloaded image onto a micro SD card. For this, you can use Etcher. Simply copying the file to the micro SD card will not work.
3. If you own an Antminer S9 and its variations (S9i, S9j), you will need to adjust jumpers to force your ASIC to boot from the file on the micro SD card instead of the NAND. If you have a different model, you can skip to part 4. The jumpers are located on the control board on the top part of the ASIC, near the Ethernet port. You will need to remove it by sliding it backwards. Once the jumper position is modified as shown in the images below BOOT FROM SD, you can reinsert the control board and reconnect the S9.
   ![image](assets/software/12.webp)
   ![image](assets/software/13.webp)
4. Insert the micro SD card into the ASIC.
5. Start the ASIC. If the automatic installation version was used, the new operating system will be installed automatically. The installation is complete when both LEDs light up at the same time. You can restart the ASIC and remove the micro SD card. If the other version was downloaded, you will need to leave the micro SD card inside the ASIC.

For more information on installation, you can visit this section of the Braiins website.

## The Interface

You will need to connect to your ASIC in a similar way. Using the local IP address of your device on your network through a browser.

The default credentials are the same as the original operating system.

- username: root
- password: root

You will then be greeted by the Brains OS+ Dashboard.

### Dashboard

![image](assets/software/14.webp)

On this first page, you can observe the real-time performance of your machine.

- Three real-time graphs that show the temperature, hashrate, and overall status of your machine.
- On the right, the real hashrate, average chip temperature, estimated efficiency in W/THs, and power consumption.
- Below, the fan speed in percentage of maximum speed and the number of rotations per minute.

![image](assets/software/15.webp)

- Further down, you will find a detailed view of each hashboard. The average temperature of the board and the chips it contains, voltage, and frequency.
- Details on the active mining pools in Pools.
- The status of autotuning in Tuner Status.
- On the right, details on the shares transmitted to the pool.

### Configuration

![image](assets/software/16.webp)

### System

![image](assets/software/17.webp)

### Quick actions

![image](assets/software/18.webp)

Configuring a pool

One can imagine a mining pool as an agricultural cooperative. Farmers pool their production together to reduce the variance of supply and demand and thus obtain more stable income for their operation. A mining pool works in the same way, and the raw material pooled together are hashes. In fact, the discovery of a single valid hash allows the creation of a block and thus winning the coinbase or the reward, currently 6.25 BTC plus the transaction fees included in the block. If you mine alone, you will only be rewarded when you find a block. Being in competition against all other miners on the planet, you would have very little chance of winning this big lottery and you would still have to pay the fees associated with using your miner without any guarantee of success. Mining pools address this issue by pooling the computing power of several (thousands) of miners and sharing their rewards based on the percentage of participation in the pool's hashrate when a block is found. To visualize your chances of mining a block alone, you can use this tool. By entering the information of an Antminer S9, we can see that the chances of finding a hash that allows the creation of a block are 1 in 24,777,849 for each block or 1 in 172,068 per day. On average (with a constant hashrate and difficulty), it would take 471 years to find a block.

However, since everything in Bitcoin is probability, it sometimes happens that solo miners are rewarded for taking this risk: Solo Bitcoin Miner Solves Block With Hash Rate of Just 10 TH/s, Beating Extremely Unlikely Odds – Decrypt

If you like to gamble, you can try it, but our guide will not focus in that direction. Instead, we will concentrate on the mining pool that best suits our needs to create a heating system.
The considerations to have when choosing a mining pool are the operation of the pool's rewards, which can be different, as well as the minimum amount before being able to withdraw the rewards to an address. For example, Braiins, which offers the software we are talking about here, also offers a pool. This pool has a reward system called "Score" which encourages miners to mine for long periods of time. Participation includes an activity time factor which is expressed with a "scoring hashrate". In our case, where we want a heating system that can be turned on for only a few minutes, this is not the ideal reward system. We prefer a reward system that gives us an equal reward for each participation. In addition, the minimum withdrawal amount for Braiins Pool is 100,000 sats and On-Chain. So we lose some sats in transaction fees and a portion of our reward can be locked if we do not mine enough during the winter.

The reward model that interests us is PPS, which stands for "pay-per-share". This means that the miner will receive a reward for each valid share. There is also a variant of this system, FPPS (Full Pay Per Share), which not only divides the coinbase reward, but also the transaction fees included in the block. The mining pools we recommend for connecting your mining/heating are Linecoin Pool (FPPS) and Nicehash (PPS).

- Nicehash: The advantage of Nicehash is that withdrawal can be done using Lightning with minimal fees. In addition, the minimum withdrawal amount is 2000 sats. The disadvantage is that Nicehash uses its hashrate for the most profitable blockchain, without really giving control to the user, so it may not necessarily participate in the Bitcoin hashrate.

- Linecoin: The advantage of Linecoin is the number of features offered, such as a detailed dashboard, the ability to make withdrawals with a Paynym (BIP 47) for better privacy protection, and the integration of a Telegram bot as well as directly configurable automations in the mobile application. This pool only mines Bitcoin blocks, but the minimum amount to withdraw remains high at 100,000 sats. We will examine the interface of one of these pools in more detail in a future article.

To configure a pool in Braiins 0S+, you will need to create an account in one of the pools of your choice. Here we will take the example of Linecoin:

![image](assets/software/19.webp)

Once your account is created, click on Connect To Pool

Then copy the Stratum address as well as your username:

![image](assets/software/20.webp)

You can now return to the Braiins OS+ interface to enter these credentials. For the password, you can leave the field blank.

![image](assets/software/21.webp)

### Overclocking and Underclocking

Overclocking and autotuning both involve adjusting frequencies on hashing cards to improve ASIC performance. The difference between the two lies in the complexity of these frequency settings.

**Overclocking** is a simple adjustment that involves increasing the frequency on hashing cards to increase the machine's hash rate. Underclocking, on the other hand, involves decreasing the clock frequency of an integrated circuit below its nominal frequency. By reducing the clock frequency of an ASIC through underclocking, the heat generated by the hardware is also reduced. This allows for a decrease in the speed of the fans needed to cool the ASIC, as they do not have to work as hard to maintain an appropriate temperature. By reducing fan speed, the noise generated by the ASIC is also reduced. This can be particularly useful for users who use ASICs at home and are looking to minimize the noise disturbances caused by mining hardware.

It is important to note that underclocking can result in a reduction in ASIC performance, so it is important to find a good balance between performance and noise.

Braiins OS+ supports overclocking, underclocking of ASICs, and autotuning. It allows users to adjust the clock frequency of their hardware flexibly to maximize performance or save energy according to their preferences.

### Autotuning

Before 2018, miners had two ways to gain an advantage in their activity: finding electricity at a reasonable cost and buying more efficient hardware. However, in 2018, a new advancement was discovered in the field of mining software and firmware, called AsicBoost. This technique allows miners to reduce their costs by approximately 13% by modifying the firmware running on their devices.
Today, there is a new advancement in the software and firmware mining sector called autotuning, which offers an even greater advantage than AsicBoost. ASICs are composed of many small computer chips that perform hashing. These chips are made of silicon, the same element widely used in semiconductors and other microelectronic components. The key understanding here is that not all silicon chips are identical - each one can vary slightly in its electrical properties. Hardware manufacturers know this and publish the performance specifications of their mining machines based on the lower limit of their tolerances. In other words, manufacturers know the frequency that works best for average chips and they use this frequency uniformly for all the chips in the machine.

This puts an upper limit on the hash rate that a machine can have. Autotuning is a process in which algorithms evaluate the optimal frequencies for chip-by-chip hashing, instead of treating the entire machine as a single unit. This means that a higher-quality chip that can perform more hashes per second will get a higher frequency, and a lower-quality chip that can perform relatively fewer hashes will get a lower frequency. Chip-level autotuning is essentially a way to optimize the performance of an ASIC through the software and firmware running on it.

The end result is a higher hash rate per watt of electricity, which means larger profit margins for miners. The reason why machines are not distributed with this type of software is that machine variance is undesirable, as customers want to know exactly what they are getting, and it is therefore a bad idea for manufacturers to sell a product that does not have consistent and predictable performance from one machine to another. Additionally, chip-level autotuning requires considerable development resources, as it is complex to implement. Manufacturers already spend a lot of resources developing their own firmwares. There are software solutions that allow for autotuning, such as Braiins OS+. In addition to improving ASIC performance by up to 20%.

This guide has been created by DecouvreBitcoin, more info on MIN201 - credit Jim and Ajelex
