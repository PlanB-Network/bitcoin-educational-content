---
name: Bitchat
description: Decentralized, Internet-free messaging for free communication
---

![cover](assets/cover.webp)

![video](https://youtu.be/WfzcKAzgB9s)

*This video tutorial from BTC Sessions walks you through the process of setting up and using Bitchat!*

Bitchat emerged from a rapid prototyping effort where [@jack](https://primal.net/jack) developed the initial concept during a weekend coding session. [@calle](https://primal.net/calle) joined the project shortly afterward to co-develop the Android implementation. Jack currently leads the development of the iOS version, while calle oversees the Android version with the support of many other contributors. 

## Introduction: Chat Freely, Without the Grid

Imagine sending messages when the internet goes down, during a natural disaster, or in places where communication is restricted. Bitchat makes this possible. It’s a decentralized, peer-to-peer messaging app that skips central servers, letting devices talk directly to each other, entirely offline using Bluetooth and mesh networking. Designed with privacy and resilience in mind, Bitchat is ideal for use in areas where traditional connectivity is unreliable or unavailable—such as during disaster scenarios, in remote locations, or for those looking to avoid surveillance. At its core, Bitchat uses cryptography to ensure every message is end-to-end encrypted, verified, and tamper-proof. 

In this tutorial, we’ll show how Bitchat works and how you can use it for truly private, offline-ready communication.

## 🚀 Key Features

Bitchat enables offline messaging through these [features](https://github.com/permissionlesstech/bitchat-android?tab=readme-ov-file#features): 

- **Cross-Platform Compatible**: Full protocol compatibility between iOS and Android.
- **Decentralized Mesh Network**: Automatic peer discovery and multi-hop message relay over Bluetooth Low Energy (BLE)
- **End-to-End Encryption**: X25519 key exchange + AES-256-GCM for private messages
- **Channel-Based Chats**: Topic-based group messaging with optional password protection
- **Store & Forward**: Messages cached for offline peers and delivered when they reconnect
- **Privacy First**: No accounts, no phone numbers, no persistent identifiers
- IRC-Style Commands: Familiar `/join, /msg, /who` style interface.
- **Message Retention**: Optional channel-wide message saving controlled by channel owners
- **Emergency Wipe**: Triple-tap logo to instantly clear all data
- **Modern Android UI**: Jetpack Compose with Material Design 3
- **Dark/Light Themes**: Terminal-inspired aesthetic matching iOS version
- **Battery Optimization**: Adaptive scanning and power management

## 1️⃣ How Bitchat Works - simply

Bitchat lets you message nearby phones directly via Bluetooth (`BLE` as follows), with no internet or cell signal needed. When you start a chat, the phones perform a secure handshake to create a unique, temporary encryption key for your conversation. Every message is protected with end-to-end encryption, and a new key is used for each one to ensure past messages remain safe even if your phone is compromised later. Finally, the app splits messages into small pieces and mixes them with random dummy data to hide your messaging activity. For direct device-to-device chats, it only works within a range of up to ~100m. It's like passing encrypted notes in a crowded room—devices whisper directly to each other, shredding the keys after every message.

Bitchat also allows you to join location-based chat rooms using the Nostr protocol and `#geohashes`. A geohash is a short code, like `#u33d`, that represents a specific geographic area, from a single neighborhood, up to an entire city or region. You can `teleport` into any geohash chat room around the world simply by entering its tag. Your messages are sent through a decentralized network of relays, which protects your exact location. Furthermore, each time you join a geohash room, you are given a new, temporary identity, adding an extra layer of privacy to your location-based conversations.

For more accurate technical details, please refer to the [official Whitepaper](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md).

## 2️⃣ Installation & Setup

### Where to Get Bitchat

You can install Bitchat through:

- [Apple App Store](https://apps.apple.com/us/app/bitchat-mesh/id6748219622) (for iOS devices)
- [Google Play Store](https://play.google.com/store/apps/details?id=com.bitchat.droid) (for Android devices)

Android users also have alternative options:

- Download the APK directly from [GitHub Releases](https://github.com/permissionlesstech/bitchat-android/releases) page or
- Install through the Nostr-compatible [Zapstore](https://zapstore.dev/apps/naddr1qvzqqqr7pvpzq7xwd748yfjrsu5yuerm56fcn9tntmyv04w95etn0e23xrczvvraqqgkxmmd9e3xjarrdpshgtnywfhkjeqxtfkcr)

![image](assets/en/01.webp)

**Note**: _This tutorial focuses primarily on the Android implementation. The iOS version may differ._

### Setup Process

After installation, open Bitchat to see this initial permissions screen. Here's what you need to do:

1. **Grant these required permissions:**
   - **Bluetooth access** (to discover nearby Bitchat users)
   - **Precise location** (Android requires this for Bluetooth functionality)
   - **Notifications** (to receive private message alerts)
2. **Disable battery optimization**:
   - This allows Bitchat to run in the background
   - Maintains mesh network connections continuously

Tap on `Grant Permissions` , follow the `prompts` and `Disable Battery Optimization` to move to the next screen. 

![image](assets/en/02.webp) 

Welcome to Bitchat's main screen. Let's get oriented:

### Settings

First things first. The settings menu can be opened by tapping the `Bitchat logo`.  The following options are available: 

- Set the  `appearance` (system/light/dark).
- enable `Proof of work` to geohash for spam deterrence (optional) 
- Turn on `Tor` to enhance privacy.

![image](assets/en/16.webp) 

### Set Your Identity

Tap the `bitchat/anonXXXX` field at the top to choose your username. This is how others will see you in both Bluetooth and internet modes. For example, you could change "anon2022" to a username of your choice.

![image](assets/en/03.webp) 

### Select Network Channels

Use the `#location channels` menu (right of username) to switch between connection types:

- **BLE Mesh***: Default Bluetooth mode (no internet, from 10 to 50 meters range)
- **#geohashes**: Internet-enabled geographic communities using [Nostr protocol](https://nostr.com/) 

When you select `#geohashes` mode, Bitchat integrates with the Nostr protocol to enable geographic communities. Your messages are published to `decentralized Nostr relays` rather than Bitchat's peer-to-peer network, allowing broader but location-filtered conversations. Crucially, your Bitchat identity keys cryptographically sign all Nostr events to maintain authentication, while geohash tags (like `#u4pruyd` for a neighborhood) filter messages to your chosen precision level. This means you can participate in local discussions without revealing exact coordinates, though internet access is required.

![image](assets/en/04.webp) 

### Monitor Peers
licence: CC-BY-SA-V4
The peer counter shows users:

- Nearby (BLE Mesh) or
- In your geohash zone (#geohashes)

![image](assets/en/05.webp) 

## 3️⃣ Global Chat & Private Messages

Bitchat provides two distinct communication modes to suit different needs:

- **Public Channels:** For open conversations with others. You can connect either through the local BLE mesh network for nearby users or via a global #geohash for internet-enabled, location-based communities.
- **Private Messages:** For secure, one-on-one conversations. These establish a direct, encrypted connection to keep your exchanges confidential.

Understanding both modes will help you navigate your conversations.

### Public Channels: The Community Hub

The `#location channels` menu (top-right) controls your public visibility. Selecting `mesh` connects you to all nearby users via BLE mesh, typically devices within 10-50 meters. This creates an open forum where messages broadcast to everyone in range, ideal for event announcements or local alerts. 

For broader geographic reach, choose any `#geohash` tag to join internet-powered communities filtered by location. These channels use Nostr protocol relays, allowing communication across cities or regions while maintaining location-based relevance. Your messages appear live to others in the same channel, with new participants automatically seeing recent message history upon joining.

![image](assets/en/06.webp) 

### Private conversations: Secure & Encrypted

To start a private conversation, single-tap directly on any `username` displayed in `Peers Overview.` You can also tap on the `star icon` to mark this user as a favorite, which will keep them visible in your contact list even when they are offline.

![image](assets/en/07.webp) 

Bitchat automatically initiates its `security handshake` when you start a private chat. Devices exchange ephemeral keys to create an encrypted tunnel specifically for your conversation. This process ensures that all your messages and shared files remain confidential thanks to continuous end-to-end encryption. Private messages support text and file sharing. 

![image](assets/en/08.webp)  

## 4️⃣ Additional features

You can access the actions panel instantly by typing `/` anywhere in Bitchat. This reveals a command menu for quick actions.

- **Manage connections**: `Block users` or `Unblock peers`
- **Channel controls**: `Show channels` or `Join/create channel`
- **Social interactions**: `Send warm hug`  or `slap with trout` 🎣
- **Chat maintenance**: `Clear chat messages`
- **Privacy tools**: `See who's online` or `Send private message`

Commands execute immediately - like `/block Satoshi` to silence critics or `/hug Hal` to spread positivity 🫂. 

![image](assets/en/09.webp)  

## 5️⃣ Creating a channel

Channels in Bitchat enable organized communication around topics, locations, or communities. To create your own, follow this workflow:

### Step 1: Create a channel

To create a channel, type `/j` or `/join` followed by the `channel name` in any chat (e.g. `/j <channelname>`). After creation a new `icon ⧉` appears indicating the new channel. Other users can join by typing the same command (e.g. `/j bitchat_tutorial`). 

![image](assets/en/10.webp)  

### Step 2: Configure settings

In addition to the default commands, the following settings are available within a channel:

- `/save` to save messages locally 
- `/transfer` to transfer channel ownership and
- `/pass` to change the channel password.

For private communities, this command enables password protection, requiring approved members to enter a custom password before joining.

## 6️⃣ Panic Mode

Now, let's talk about that `panic mode`: triple-tapping the `Bitchat logo` initiates a complete wipe of all local messages and data within the app. This is your ultimate privacy safeguard, perfect for situations requiring immediate discretion.

**Important reminder:** _Panic mode is permanent. Once activated, data cannot be recovered. Use with caution._

![image](assets/en/11.webp)  

## 7️⃣  Geohashes

Geohash channels enable targeted conversations based on `geographic locations` rather than traditional network connections. This feature transforms bitchat into a location-aware communication tool, ideal for local coordination, community building, and location-specific discussions.

### How `#geohashes` work

The system divides the world into grid squares using the [Geohash system](https://en.wikipedia.org/wiki/Geohash), where each character in the hash represents greater precision:

- **Level 4** (e.g., `u33d`): Covers approximately 25km × 25km - ideal for city-wide discussions
- **Level 6** (e.g., `u33d8z`): Covers about 1.2 km × 1.2 km - neighborhood precision
- **Level 8** (e.g., `u33d8z1k`): Covers roughly 150 m × 150 m - street-segment accuracy

Precision selection balances privacy with utility: higher levels create more exclusive zones but reveal your location more precisely.

### Joining `#geohash` channels

1. Access the `#location channels` menu.
2. Select your desired precision level and enter the `#geohash` (e.g. #u33d)
3. Tap the `Teleport` button to join the `#location channel`. 

![image](assets/en/12.webp)  

Alternatively, you can tap the `map icon` to use the map view to determine the precision level and tap `select` to join the `#location channel`. 

![image](assets/en/13.webp)  

**Important reminder**: _#geohash functionality requires an active internet connection - unlike BLE mesh which operates offline via Bluetooth._

## 8️⃣ Heatmaps

Heatmaps are a cool way to discover Bitchat events and channels around the world. [Bitmap](https://bitmap.lat/) visualises and tracks anonymous, location-based messages across the Nostr network, displaying ephemeral Nostr events. Take a look and join location-specific channels and chats.  

![image](assets/en/15.webp)  

## 🎯 Conclusion

Bitchat enables secure, decentralized communication for scenarios where traditional messaging fails. It's able to operate without internet infrastructure using BLE mesh networking, making it suitable for protests, disaster zones, and remote areas where connectivity is limited or censored. The app ensures privacy through ephemeral key encryption, geohash-based location channels, and a panic mode data erasure.

The app is still in its early stages of development, but it is already showing promise. Users should expect occasional bugs and report issues via [GitHub](https://github.com/permissionlesstech/bitchat-android/issues). Improvements are planned, including `ecash` integration for private in-app transactions using Cashu protocol.

![image](assets/en/14.webp)  

## 📚 Bitchat Resources

[Github](https://github.com/permissionlesstech) | [Website ](https://bitchat.free/)| [Whitepaper](https://github.com/permissionlesstech/bitchat/blob/main/WHITEPAPER.md)
