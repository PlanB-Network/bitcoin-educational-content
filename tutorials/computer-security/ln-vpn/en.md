---
name: LN VPN

description: Set up your VPN
---

![image](assets/cover.webp)

LN VPN is a customizable VPN service that only accepts lightning payments. Today, I'll show you how to use it and leave fewer traces when browsing the interwebs.

There are many quality VPN service providers, and we have conducted a comprehensive review in this article (hyperlink). However, LN VPN stands out, and we couldn't miss the opportunity to introduce it to you.

Most VPN service providers like ProtonVPN and Mullvad offer the option to pay with bitcoins but require creating an account and purchasing a plan for a longer or shorter term, which may not fit everyone's budget.

LN VPN enables on-demand VPN usage for as short as one hour, thanks to its implementation of bitcoin payments via the lightning network. Instant and anonymous, lightning payments open up a world of possibilities for micropayments.

Note💡: **This guide describes how to use LN VPN from a Linux Ubuntu 22.04 LTS system.**

## Prerequisites: Wireguard

In simple terms, Wireguard is used to create a secure tunnel between your computer and the remote server through which you will browse the Internet. It is the IP address of this server that will appear as yours for the duration of the lease you will contract by following this guide.

Official Wireguard installation guide: https://www.wireguard.com/install/

```
Wireguard installation
          $ sudo apt-get update
          $ sudo apt install wireguard
```

## Prerequisites: Lightning Bitcoin Wallet

If you don't have a Lightning Bitcoin wallet yet, no worries, we have created a very simple guide for you here. (the LN tutorial section can help you)

## Step 1: Contract a Lease

From https://lnvpn.com, you will need to select the country of the VPN tunnel's exit IP and a duration. Once these parameters are set, click on Pay with lightning.

![image](assets/1.webp)

A lightning invoice will be displayed, and you just need to scan it with your lightning wallet.

Once the invoice is paid, you will need to wait for a few seconds to up to two minutes for your Wireguard configuration settings to be generated. If it takes a little longer, don't panic, we have done this procedure dozens of times, and sometimes it just takes a bit longer.
The following text has been translated into English while maintaining the same markdown layout as the original text:

The next screen will appear and you just have to click on "Download as File" to receive your config file, which will have a name that looks like lnvpn-xx-xx.conf where "xx" will correspond to the current date.
![image](assets/2.webp)

## Step 2: Activate the tunnel

First, you will need to rename the config file obtained in the previous step so that it can be automatically recognized by Wireguard.

Go to your download folder, either in a terminal window or with the file explorer, and rename the lnvpn-xx-xx.conf file to wg0.conf like this:

```
    $ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
    $ sudo wg-quick up ~/Downloads/wg0.conf
```

There you go! The tunnel is activated!

## Step 3: Verify

Use an online service like whatismyip to verify that your public IP address is now the one from the VPN you just activated.

## Step 4: Disable

When your lease expires, you will need to disable the connection to regain access to the internet. You can then repeat steps 1 to 3 whenever you want to establish a lease with LN VPN.

Disable the tunnel:

```
    $ sudo ip link delete dev wg0
```

There you have it! You now know how to use LN VPN, a unique VPN service!
