---
name: Tailscale
description: Advanced Tailscale tutorial
---
![cover](assets/cover.webp)


## 1. Introduction


Tailscale is a next-generation VPN that creates an encrypted mesh network between your devices. It lets you connect remote machines as if they were on the same local network, without complex configuration or port opening.


For self-hosting, Tailscale assigns each device a fixed private IP in a virtual network, offering stable access to your services even when your public IP changes. This means you can manage your servers remotely, without exposing your services directly to the Internet.


**Main applications:**


- Manage a personal server from the outside
- Manage Umbrel/Lightning nodes faster than Tor
- Secure access to a Raspberry Pi or NAS
- Connect to your services via SSH or HTTP without complex network configuration


This simplicity-focused approach enables self-hosters to access their services securely, avoiding the pitfalls of traditional VPNs.


## 2. How Tailscale works


Unlike traditional VPNs, which route all traffic through a central server, Tailscale creates a mesh network where devices communicate directly with each other. The central server only handles authentication and key distribution, without seeing user data.


![VPN traditionnel (hub-and-spoke)](assets/fr/01.webp)

*Figure 1: Traditional VPN with hub-and-spoke architecture where all traffic passes through a central server*


Based on WireGuard, each device generates its own cryptographic keys. The coordination server distributes the public keys to the nodes, which then establish end-to-end encrypted tunnels directly between themselves. To get through firewalls, Tailscale uses NAT traversal and, as a last resort, DERP relays that maintain encryption.


![VPN maillé (mesh)](assets/fr/02.webp)

*Figure 2: Tailscale mesh network where devices communicate directly with each other*


All communications are encrypted with WireGuard. Tailscale only sees metadata (connections) but never the content of exchanges. For greater sovereignty, Headscale enables the coordination server to be self-hosted.


**Security and confidentiality:** Thanks to WireGuard, all communications on Tailscale are end-to-end encrypted. Tailscale can't read your traffic - only your devices have the necessary private keys. The service only sees metadata: IP addresses, device names, connection timestamps and peer-to-peer connection logs (without content).


However, this architecture is dependent on Tailscale Inc. for network coordination. To eliminate this dependency, Headscale offers an open-source alternative that allows you to self-host the control server while using the official Tailscale clients, thus guaranteeing complete sovereignty over your network infrastructure, at the cost of a more technical configuration.


**For a detailed explanation of the inner workings of Tailscale, including control plane management, NAT traversal and DERP relays, we recommend the excellent article [How Tailscale Works](https://tailscale.com/blog/how-tailscale-works) on the official blog. This article explains in depth the technical concepts that make Tailscale so powerful.


## 3. Installing Tailscale


Tailscale runs on **most common** operating systems (Windows, macOS, Linux, iOS, Android). Installation is said to be "quick and easy" on all platforms. Let's start by taking a look at Interface and how to create an account, then move on to the installation procedures for different environments.


### 3.1 Tailscale account creation


Go to [https://tailscale.com/](https://tailscale.com/) and click on the "Get Started" button at the top right of the page.



![Page d'accueil Tailscale](assets/fr/03.webp)

*The Tailscale home page explains the concept and offers a free start*


To use Tailscale, you first need to create an account via an identity provider:


![Page de connexion Tailscale](assets/fr/04.webp)

*Choice of identity provider to connect to Tailscale (Google, Microsoft, GitHub, Apple, etc.)*


After logging in, Tailscale will ask you for some information about your intended use:


![Questionnaire d'utilisation](assets/fr/05.webp)

*Form to better understand your use case (personal or professional)*


Once you have created your account, you can install Tailscale on your devices:


![Ajout du premier appareil](assets/fr/07.webp)

*Tailscale lets you install the application on different systems*


### 3.2 Installation on different platforms



- On Windows and macOS:** Simply download the graphical application from the official Tailscale website and install it (.msi file on Windows, .dmg file on Mac). Once installed, the application launches a graphical Interface that lets you connect (via a browser) to your Tailscale account to authenticate the machine.


![Connexion d'un appareil macOS](assets/fr/08.webp)

*Connect a MacBook to the tailnet*


![Connexion réussie](assets/fr/09.webp)

*Confirmation that the device is connected to the Tailscale* network



- On Linux (Debian, Ubuntu, etc.):** You have several options. The simplest method is to run the official installation script: for example, on Debian/Ubuntu:


```bash
curl -fsSL https://tailscale.com/install.sh | sh
```


This script will add the official Tailscale repository and install the package. You can also [manually add the APT repository](https://pkgs.tailscale.com) or use regular Snap or apt packages. Once installed, daemon `tailscaled` will run in the background. You will then need to **authenticate the node** (see Interface CLI vs web below). On other distributions (Fedora, Arch...), the package is also available via the standard repositories or the universal install script. For a headless server, use CLI: for example `sudo tailscale up --auth-key <key>` if using a pre-generated authentication key, or simply `tailscale up` for an interactive login (which will provide a URL to visit to authenticate the device).



- On ARM-based systems (Raspberry Pi, etc.):** We're generally on Linux, so the same approach as above (script or package). Note that Tailscale supports ARM32/ARM64 architecture without any problems. Many users install Tailscale on Raspberry Pi OS via apt or on lightweight distributions (DietPi, etc.) to access their Pi everywhere.



- On iOS and Android:** Tailscale provides **official** mobile applications. Simply install *Tailscale* from the [App Store](https://apps.apple.com/us/app/tailscale/id1470499037?ls=1) (iOS) or the [Play Store](https://play.google.com/store/apps/details?id=com.tailscale.ipn) (Android).


![Installation sur iPhone](assets/fr/11.webp)

*Steps to install Tailscale on iPhone: welcome, privacy, notifications, VPN*


![Connexion sur iPhone](assets/fr/12.webp)

*Connect to tailnet, select account and validate on iPhone*


Once the app is installed, on first launch it will ask you to authenticate via the chosen provider (Google, Apple ID, Microsoft, etc., depending on what you're using for Tailscale) - it's the same procedure as on other platforms, usually a redirect to an OAuth web page. After that, the mobile app creates the VPN (on iOS you'll need to accept the VPN configuration add-on). The app can then run in the background, giving you access to your tailnet from anywhere. *Please note:* on mobile, you can only have **one active VPN at a time** - so make sure you don't have another VPN connected at the same time, or Tailscale won't be able to establish its own. On Android, you can set up a separate work profile if you want to isolate certain uses (e.g. a profile with Tailscale active for a given app).


### 3.3 Adding multiple devices and validation


Once your first device is connected, Tailscale prompts you to add other devices to your network:


![Ajout d'appareils supplémentaires](assets/fr/10.webp)

*Interface showing the first device connected and waiting for other devices*


Once you've added several devices, you can check that they can communicate with each other:


![Test de connectivité entre appareils](assets/fr/13.webp)

*Confirmation that devices can communicate with each other via ping*


Tailscale then suggests additional configurations to enhance your experience:


![Suggestions de configuration](assets/fr/14.webp)

*Suggestions for setting up DNS, sharing devices and managing access*


### 3.4 Administration dashboard


The web administration console lets you view and manage all your connected devices:


![Tableau de bord des machines](assets/fr/15.webp)

*List of connected devices with their characteristics and status*


**Interface Web vs Interface CLI:** Tailscale offers two complementary ways of interacting with the network: the **Interface web administration** and the **command-line client (CLI)**.



- Interface Web (Admin Console)**: accessible at [https://login.tailscale.com](https://login.tailscale.com), this web console is the central dashboard for your Tailscale network. It lists all devices (*Machines*), their online/offline status, their Tailscale IP addresses, and more. Here you can **manage devices** (rename, expire keys, authorize routes, disable a node), **manage users** (in an organizational context), and define security rules (ACLs). This is also where you configure global options such as MagicDNS, tags, or auth keys (pre-generate auth keys for automated device addition). Interface web is very handy for getting an overview and applying changes that will be propagated via the coordination server to all nodes. *Example:* Activating a **subnet route** or an **exit node** is done with a single click in the console, once the node in question has announced itself as such.



- Interface command line (CLI):** The `tailscale` command is available in CLI on every device where Tailscale is installed. This CLI allows you to do everything locally: connect (`tailscale up`), inspect status (`tailscale status` to see which peers are connected), debug (`tailscale ping <ip>`), and so on. Some features are even **exclusive to CLI** or more advanced, for example:



  - `tailscale up --advertise-routes=192.168.0.0/24` to advertise a subnet route,
  - `tailscale up --advertise-exit-node` to propose your machine as an exit node,
  - `tailscale set --accept-routes=true` (or `--exit-node=<IP>`) to consume a route or use an exit node,
  - `tailscale ip -4` to display the device's Tailscale IP,
  - `tailscale lock/unlock` (if using *tailnet-lock*, advanced security feature),
  - or `tailscale file send <node>` to use **Taildrop** (file transfer between devices).

CLI is very useful on servers without Interface graphics, and for scripting certain actions. **Differences in use:** Most basic configurations can be made either via the Web or via the CLI. For example, adding a device is done either by prompting via the console, or by running `tailscale up` on the device and validating via the web. Similarly, renaming a device can be done via the console or with `tailscale set --hostname`. **In summary**, the web console is ideal for global network administration (especially with multiple machines/users), while the CLI is handy for fine-grained control over a given machine, automation scripts, or use on a system without a GUI.


## 4. Using Tailscale on Umbrel


Umbrel is a popular self-hosting platform (notably used for Bitcoin/Lightning nodes and other self-hosted services, via its App Store). To install and configure Umbrel, we recommend you follow our dedicated tutorial:


https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Using Umbrel and Tailscale together is a particularly interesting use case, as Umbrel natively integrates an easy-to-deploy Tailscale module. Here's how Tailscale integrates with Umbrel and what it brings:


### 4.1 Umbrel installation and configuration



- Installing Tailscale on Umbrel:** Umbrel has an official Tailscale application in its App Store. Installation couldn't be simpler:


![Interface Umbrel avec l'application Tailscale](assets/fr/16.webp)

*Tailscale application page in the Umbrel App Store*


From the Interface Web Umbrel, open the App Store, search for **Tailscale** and click *Install*. A few seconds later, the application is installed on the Umbrel. When you open it, Umbrel displays a page allowing you to link your node to Tailscale.


![Écran de login Tailscale dans Umbrel](assets/fr/17.webp)

*Tailscale connection screen in Umbrel's Interface*


Just **click on "Log in "**, which will redirect you to the Tailscale authentication page:


![Page d'authentification Tailscale](assets/fr/18.webp)

*Connect to Tailscale via an identity provider*


You can authenticate via your Tailscale account (Google/GitHub/etc.) or enter your email. Typically, on Umbrel, Interface asks you to visit [https://login.tailscale.com](https://login.tailscale.com) and log in - this authenticates the Umbrel Tailscale app.


![Confirmation de connexion réussie](assets/fr/19.webp)

*Confirmation that the Umbrel device is connected to the Tailscale network*


Once done, your Umbrel is "in" your Tailscale network and appears on your console with a name (e.g. *umbrel*). You can then click on the IP address of your devices to copy it, retrieve the IPv6 address or your MagicDNS associated with your device.


![Console Tailscale avec appareils connectés](assets/fr/20.webp)

*Tailscale administration console showing several connected devices, including Umbrel*



### 4.2 Remote access to Umbrel services


Once Umbrel is connected to Tailscale, **you can access Interface Umbrel and the applications running on it, from anywhere, as if you were on the local network**. This is one of the main advantages over Tor.


Access is remarkably simple: instead of using `umbrel.local` (which only works on your local network), you use your Umbrel's Tailscale IP address (`http://100.x.y.z`) directly from any device connected to your tailnet. This works no matter where you are or what internet connection you're using (4G, public Wi-Fi, corporate network).


**Examples of Umbrel-hosted applications accessible via Tailscale:**



- Interface main Umbrel**: Access your Umbrel dashboard simply by typing `http://100.x.y.z` in your browser
- Bitcoin node**: Manage your Bitcoin node without latency, view synchronization and statistics
- Lightning Node**: Use ThunderHub, RTL or other Lightning management interfaces with immediate responsiveness
- Mempool**: View Bitcoin transactions and Mempool without Tor delays
- noStrudel**: Access your Nostr services hosted on Umbrel


**Connect external wallets to your Bitcoin or lightning nodes via Tailscale:**


Tailscale also enables your Bitcoin and Lightning wallets installed on other devices to connect directly to your Umbrel node:



- Sparrow wallet (Bitcoin)**: This external Wallet Bitcoin can connect directly to your Umbrel's Electrum server using the Tailscale IP address:


![Configuration Electrum dans Sparrow](assets/fr/21.webp)

*Configuring a private Electrum server in Sparrow wallet using Umbrel's Tailscale IP address*


![Liste des serveurs Electrum dans Sparrow](assets/fr/22.webp)

*List of Electrum server aliases in Sparrow with Umbrel Tailscale IP address*


Read our complete guide to configuring Sparrow wallet with your Bitcoin node:


https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d



- Zeus (Lightning)**: This Wallet mobile Lightning can connect to your Lightning node on Umbrel. Instead of configuring the endpoint as `.onion', simply set the Tailscale IP of your Umbrel and the Lightning API port. The connection will be instantaneous compared to Tor.


![Configuration Zeus avec IP Tailscale](assets/fr/23.webp)

*Configuring Zeus to connect to the Lightning node via the Tailscale* IP address


To configure Zeus with your Lightning node, see our detailed tutorial:


https://planb.network/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

To find out more about the Lightning Network and how it works on Umbrel, visit:


https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16



### 4.3 Advantages over Tor


Umbrel natively offers remote access via Tor (by providing `.onion` addresses for its web services). While Tor has the advantage of confidentiality (anonymity) and requires no registration, many users find **Tor slow and unstable** for everyday use (pages load slowly, timeouts, etc.) - *"Umbrel via Tor is so slow "* some complain.


Tailscale offers a generally **faster, low-latency** connection, as traffic passes directly (or via a fast relay) instead of bouncing through 3 Tor nodes. What's more, Tailscale provides a "local network" experience: private IPs are used, and applications can be mapped directly (e.g. SMB network drive on \100.x.y.z).


That said, Tor has the advantage of being decentralized and "out of the box" on Umbrel, whereas Tailscale involves trusting a third party (or hosting headscale). Tor is also useful for clientless access (from any Tor browser, you can consult the Umbrel UI, whereas Tailscale requires the client installed on the accessing device).


**To sum up**, for interactive use (Lightning wallets, frequent web interfaces), Tailscale offers appreciable comfort and speed compared with Tor, at the price of a slight external dependency. Many people choose to use *both*: Tailscale on a day-to-day basis, and Tor as a fallback or to share access with someone without inviting them into their VPN.


### 4.4 Safety


By using Tailscale with Umbrel, you avoid exposing Umbrel to the Internet. The Umbrel node is accessible only to your other authenticated devices in the tailnet, considerably reducing the attack surface (no port open to strangers, no risk of attack on the web service via the Internet).


Communications are encrypted (WireGuard) in addition to any encryption your services are already doing (e.g. even internal HTTP is in the tunnel). You can still apply Tailscale ACLs to, for example, prevent a particular tailnet device from accessing Umbrel if you want to partition the network. Umbrel itself doesn't see the difference - it thinks it's serving local.


---

To conclude this section, integrating Tailscale on Umbrel takes just a few clicks and **greatly improves the accessibility** of your self-hosted node. You'll be able to administer Umbrel and its services from anywhere, securely and efficiently, just as if you were at home. This is a particularly useful solution for real-time applications (Lightning) that suffer from Tor latency, or more generally for any self-host looking for a simple private connection. All without exposing a single port** on your box, and without complicated network configuration.


## 5. Advanced management and use cases


### 5.1 Tailscale advanced features


**Network management:** The administration console (login.tailscale.com) lets you manage your devices, view connections and configure access rules.


**MagicDNS:** Automatically resolves device names (e.g. `raspberrypi.tailnet.ts.net`) to avoid memorizing IP addresses.


**ACL and access control:** Define precisely who can access what in your network via JSON rules, ideal for isolating certain devices or restricting access to specific services.


**Device Sharing lets you invite someone to access a specific machine without giving them access to your entire network.


**Subnet Router:** A Tailscale machine can act as a gateway for an entire subnet, enabling access to non-Tailscale devices (IoT, printers, etc.) via a single configured machine.


**Exit Node:** Use a machine as an Internet gateway to exit with its IP. Useful for public Wi-Fi or to bypass geographic restrictions.


**Taildrop:** A secure alternative to AirDrop, allowing you to transfer files between your Tailscale devices, whatever their platform or location. Unlike AirDrop, which is limited to the Apple ecosystem and physical proximity, Taildrop works between all your devices (Windows, Mac, Linux, Android, iOS), even if they're in different countries. Files are transferred directly between devices with end-to-end encryption, without passing through a central server. Use the command line `tailscale file cp` or the graphical Interface application depending on your system.


### 5.2 Comparison with other solutions


**Vs OpenVPN:** Tailscale is much simpler to configure (no ports to open, no certificate management) but involves dependence on a third-party service. OpenVPN is fully controllable, but requires more expertise.


**As a direct competitor, ZeroTier operates at Layer 2 (Ethernet), enabling broadcast/multicast, while Tailscale operates at Layer 3 (IP). ZeroTier offers greater network flexibility, while Tailscale favors simplicity of use.


**Vs Tor:** Tor offers anonymity that Tailscale doesn't, but is much slower. Tor is decentralized and doesn't require an account, while Tailscale is faster and offers a LAN-like experience.


**Vs WireGuard manual:** Tailscale automates all the key and connection management that WireGuard raw requires you to handle manually. It's essentially WireGuard + a simplified management layer.


In conclusion, Tailscale positions itself as a modern, simplicity-oriented solution, ideal for personal use and small teams. For purists of total control, Headscale offers a self-hosting alternative.


## 6. Conclusion


**Tailscale benefits:** Tailscale offers several advantages for self-hosting:



- Simplicity and performance** - Quick installation on all platforms without complex network configuration. Traffic follows the most direct path between your machines (P2P mesh), with the performance of the WireGuard protocol and no central server to limit throughput.
- Security and flexibility** - End-to-end encryption, reduced attack surface, and advanced features (ACL, SSO/MFA authentication). Works even behind NATs or on the move, with subnet routers and exit nodes to adapt the network to your needs.


**Limits:** Also keep in mind:



- External dependency** - In its standard version, the service relies on the Tailscale Inc. infrastructure. This dependency can be bypassed via Headscale (self-hosting alternative).
- Other constraints** - Partially closed source code, limitations of the free version for certain advanced uses, no support for Layer 2 (broadcast/multicast), and need for Internet access to establish connections.


**Tailscale is ideal for individual self-hosts and small teams, developers needing access to dispersed resources, VPN beginners and mobile users. For companies requiring total control, other solutions such as Headscale or WireGuard directly may be preferable.


**Explore Headscale for full self-hosting, API and DevOps integrations (Terraform), or alternatives like Innernet (similar but fully self-hosted) and Netmaker.


Tailscale is an essential tool for self-hosting, thanks to its simplicity and efficiency, making your private infrastructure as accessible as if it were in the cloud, while keeping control at home.


## 7. Useful resources


### Official documentation



- Tailscale Documentation Center**: [docs.tailscale.com](https://docs.tailscale.com) - Full English documentation, installation guides, tutorials and technical references.
- How Tailscale works**: [How Tailscale Works](https://tailscale.com/blog/how-tailscale-works) - Detailed article explaining the inner workings of Tailscale.
- Changelog**: [tailscale.com/changelog](https://tailscale.com/changelog) - Tracking updates and new features.


### Practical guides



- Homelab** tutorials: [tailscale.com/kb/1310/homelab](https://tailscale.com/kb/1310/homelab) - Specific guides for self-hosting.
- Configuring an Exit Node**: [tailscale.com/kb/1103/exit-nodes](https://tailscale.com/kb/1103/exit-nodes) - Detailed guide to configuring Exit Nodes.
- Use Taildrop**: [tailscale.com/kb/1106/taildrop](https://tailscale.com/kb/1106/taildrop) - Transfer files between Tailscale devices.


### Comparisons



- Tailscale vs. other solutions**: [tailscale.com/compare](https://tailscale.com/compare) - Detailed comparisons with other VPN and network solutions (ZeroTier, OpenVPN, etc.).


### Community



- Reddit**: [r/Tailscale](https://www.reddit.com/r/tailscale/) - Discussions, questions and feedback.
- GitHub**: [github.com/tailscale/tailscale](https://github.com/tailscale/tailscale) - Customer source code, where to track development and report problems.
- Discord**: [discord.gg/tailscale](https://discord.gg/tailscale) - Community of users and developers.


Tailscale regularly provides new content and features. Check out their [official blog](https://tailscale.com/blog/) for the latest news and case studies.