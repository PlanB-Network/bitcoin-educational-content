---
name: Bitcoin Core Node (linux)
description: Running your own node with Bitcoin Core
---

![cover](assets/cover.webp)

# Running your own node with Bitcoin Core

Introduction to Bitcoin and the concept of a node, complemented by a comprehensive installation guide on Linux.

One of the most exciting propositions of Bitcoin is the ability to run the program oneself, and thus participate at a granular level in the network and the verification of the public transaction ledger.

Bitcoin, an open-source project, has been publicly distributed and available for free since 2009. Nearly 15 years after its inception, Bitcoin is now a robust and unstoppable digital monetary network, benefiting from a powerful organic network effect. For their efforts and vision, Satoshi Nakamoto deserves our gratitude. By the way, we host the Bitcoin whitepaper here on Agora 256 (note: also on the university).

## Becoming your own bank

Running your own node has become essential for adherents to the Bitcoin axiom. Without asking anyone's permission, it is possible to download the blockchain from the beginning and thus verify all transactions from A to Z according to the Bitcoin protocol.

The program also includes its own wallet. Thus, we have control over the transactions we send to the rest of the network, without any intermediary or third party. You are your own bank.

The rest of this article is therefore a guide to installing Bitcoin Core — the most widely used Bitcoin software version — specifically on Debian-compatible Linux distributions such as Ubuntu and Pop!/\_OS. Follow this guide to take one step closer to your individual sovereignty.

## Bitcoin Core Installation Guide for Debian/Ubuntu

**Prerequisites**
- Minimum 6GB of data storage (pruned node) — 1TB of data storage (full node)
- Allow at least 24 hours for the completion of the Initial Block Download (IBD). This operation is mandatory even for a pruned node.
- Allow ~600GB of bandwidth for the IBD, even for a pruned node.

**Note:💡** the following commands are predefined for Bitcoin Core version 24.1.

## Downloading and Verifying Files

1. Download bitcoin-24.1-x86_64-linux-gnu.tar.gz, as well as the SHA256SUMS and SHA256SUMS.asc files. (https://bitcoincore.org/bin/bitcoin-core-24.1/bitcoin-24.1-x86_64-linux-gnu.tar.gz)
2. Open a terminal in the directory where the downloaded files are located. E.g., cd ~/Downloads/.
3. Verify that the checksum of the version file is listed in the checksum file using the command sha256sum --ignore-missing --check SHA256SUMS.
4. The output of this command should include the name of the downloaded version file followed by "OK". Example: bitcoin-24.0.1-x86_64-linux-gnu.tar.gz: OK.
5. Install git using the command sudo install git. Then, clone the repository containing the PGP keys of Bitcoin Core signers using the command git clone https://github.com/bitcoin-core/guix.sigs.
6. Import the PGP keys of all signers using the command gpg --import guix.sigs/builder-keys//\*
7. Verify that the checksum file is signed with the PGP keys of the signers using the command gpg --verify SHA256SUMS.asc.

Each signature will return a line starting with: gpg: Good signature and another line ending with Primary key fingerprint: 133E AC17 9436 F14A 5CF1 B794 860F EB80 4E66 9320 (example of Pieter Wuille's PGP key fingerprint).

**Note💡:** it is not necessary for all signer keys to return an "OK". In fact, only one may be necessary. It is up to the user to determine their own validation threshold for PGP verification.

You can ignore the messages WARNING:
- `This key is not certified with a trusted signature!`
- `There is no indication that the signature belongs to the owner.`

## Installation of the Bitcoin Core graphical interface

1. In the terminal, still in the directory where the Bitcoin Core version file is located, use the command tar xzf bitcoin-24.1-x86_64-linux-gnu.tar.gz to extract the files contained in the archive.

2. Install the previously extracted files using the command sudo install -m 0755 -o root -g root -t /usr/local/bin bitcoin-24.1/bin//\*

3. Install the necessary dependencies using the command sudo apt-get install libqt5gui5 libqt5core5a libqt5dbus5 qttools5-dev qttools5-dev-tools qtwayland5 libqrencode-dev

4. Start bitcoin-qt (Bitcoin Core graphical interface) using the command bitcoin-qt.

5. To choose a pruned node, check Limit blockchain storage and configure the data limit to be stored:

![welcome](assets/1.webp)

## Conclusion of Part 1: Installation Guide

Once Bitcoin Core is installed, it is recommended to keep it running as much as possible to contribute to the Bitcoin network by verifying transactions and transmitting new blocks to other peers.

However, running and synchronizing your node intermittently, even just to validate received and sent transactions, remains a good practice.

![Creation wallet](assets/2.webp)

# Configuring Tor for a Bitcoin Core Node

**Note💡:** this guide is designed for Bitcoin Core 24.0.1 on Ubuntu/Debian compatible Linux distributions.

## Installing and configuring Tor for Bitcoin Core

First, we need to install the Tor service (The Onion Router), a network used for anonymous communication, which will allow us to anonymize our interactions with the Bitcoin network. For an introduction to online privacy protection tools, including Tor, refer to our article on this topic.

To install Tor, open a terminal and enter sudo apt -y install tor. Once the installation is complete, the service will normally be automatically launched in the background. Check that it is running correctly with the command sudo systemctl status tor. The response should show Active: active (exited). Press Ctrl+C to exit this function.

**Tip:** in any case, you can use the following commands in the terminal to start, stop, or restart Tor:
```
sudo systemctl start tor
sudo systemctl stop tor
sudo systemctl restart tor
```

Next, let's launch the Bitcoin Core graphical interface with the command bitcoin-qt. Then, enable the software's automated feature to route our connections through a Tor proxy: Settings > Network, and from there we can check Connect through SOCKS5 proxy (default proxy) as well as Use a separate SOCKS5 proxy to reach peers via Tor onion services.

![option](assets/3.webp)

Bitcoin Core automatically detects if Tor is installed and, if so, will by default create outbound connections to other nodes also using Tor, in addition to connections to nodes using IPv4/IPv6 networks (clearnet).

**Note💡:** to change the display language to French, go to the Display tab in Settings.

## Advanced Tor Configuration (optional)

It is possible to configure Bitcoin Core to only use the Tor network to connect with peers, thus optimizing our anonymity through our node. Since there is no built-in functionality for this in the graphical interface, we will need to manually create a configuration file. Go to Settings, then Options.

![option 2](assets/4.webp)

Here, click on Open configuration file. Once in the bitcoin.conf text file, simply add a line onlynet=onion and save the file. You need to restart Bitcoin Core for this command to take effect.
We will then configure the Tor service so that Bitcoin Core can receive incoming connections via a proxy, allowing other nodes on the network to use our node to download blockchain data without compromising the security of our machine.

In the terminal, enter sudo nano /etc/tor/torrc to access the Tor service configuration file. In this file, look for the line #ControlPort 9051 and remove the # to enable it. Now add two new lines to the file: HiddenServiceDir /var/lib/tor/bitcoin-service/ and HiddenServicePort 8333 127.0.0.1:8334. To exit the file while saving it, press Ctrl+X > Y > Enter. Back in the terminal, restart Tor by entering the command sudo systemctl restart tor.

With this configuration, Bitcoin Core will be able to establish incoming and outgoing connections with other nodes on the network only through the Tor network (Onion). To confirm this, click on the Window tab, then Peers.

![Nodes Window](assets/5.webp)

## Additional Resources

Ultimately, using only the Tor network (onlynet=onion) could make you vulnerable to a Sybil attack. That's why some recommend maintaining a multi-network configuration to mitigate this type of risk. Furthermore, all IPv4/IPv6 connections will be routed through the Tor proxy once it is configured, as previously indicated.

Alternatively, to remain solely on the Tor network and mitigate the risk of a Sybil attack, you can add the address of another trusted node to your bitcoin.conf file by adding the line addnode=trusted_address.onion. You can add this line multiple times if you want to connect to multiple trusted nodes.

To view the logs of your Bitcoin node specifically related to its interaction with Tor, add debug=tor to your bitcoin.conf file. You will now have relevant Tor information in your debug log, which you can view in the Information window with the Debug File button. It is also possible to view these logs directly in the terminal with the command bitcoind -debug=tor.

**Tip💡:** here are some interesting links:
- Wiki page explaining Tor and its relationship with Bitcoin
- Bitcoin Core configuration file generator by Jameson Lopp
- Tor configuration guide by Jon Atack

As always, if you have any questions, feel free to share them with the Agora256 community. We learn together to be better tomorrow than we are today!
