---
name: pfSense
description: Installing Pfsense
---
![cover](assets/cover.webp)


___


*This tutorial is based on original content by Florian BURNEL published on [IT-Connect](https://www.it-connect.fr/). License [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Major changes have been made to the author's original text to bring the tutorial up to date.*


___


![Image](assets/fr/027.webp)


## I. Presentation


pfSense is a free, open source operating system that transforms any computer, dedicated server or hardware appliance into a high-performance, highly configurable router and firewall. Based on FreeBSD and renowned for its stable, robust network architecture, pfSense has been setting the standard for open source firewalls for businesses, local authorities and demanding home users for over fifteen years.


Its main functions have evolved considerably over the years, and have been enhanced with each new version. To date, pfSense offers:



- Complete, centralized administration via a modern, intuitive and secure Interface web interface.
- High-performance stateful firewall with advanced NAT support (including NAT-T) and granular rule management.
- Native multi-WAN support, enabling aggregation or redundancy of Internet connections.
- Integrated DHCP server and relay.
- High availability thanks to CARP protocol for failover and the possibility of configuring pfSense clusters.
- Load balancing between several connections or servers.
- Full VPN support: IPsec, OpenVPN and WireGuard (replacing L2TP, now obsolete).
- Configurable captive portal for guest access control, especially in public or hotel environments.


pfSense also features an extensible package system that makes it easy to add advanced features such as a transparent proxy (Squid), URL filtering or IDS/IPS (Snort or Suricata) directly from the Interface web.


pfSense is distributed for 64-bit platforms only, in line with current FreeBSD recommendations. It can be installed on standard hardware (PCs, rack servers) or on low-power embedded platforms such as Netgate appliances or certain low-profile x86 boxes, which are far more powerful than older Alix boxes.


Finally, it's worth remembering that pfSense requires at least two physical network interfaces: one dedicated to the external zone (WAN) and one dedicated to the internal network (LAN). Depending on the complexity of your infrastructure (DMZ, VLAN, multiple WANs), several additional interfaces may be required to take full advantage of its capabilities.


## II. Download image


The latest stable version of pfSense, at the time of writing this tutorial, is 2.8 (released in June 2025). You can download the ISO image or the installation file adapted to your hardware environment directly from the official website:



- [Download pfSense](https://www.pfsense.org/download/)


The download portal allows you to select:



- Architecture (generally **AMD64** for all modern hardware).
- Image type (**Installer USB Memstick** for installation via USB stick, **ISO Installer** for burning or virtual editing).
- The nearest download mirror, to optimize transfer speed.


For those wishing to deploy pfSense in a virtualized environment (Proxmox, VMware ESXi, VirtualBox...), an **OVA** image is also available. This ready-to-use virtual machine greatly simplifies installation and initial configuration. Just make sure you adjust the allocated resources (CPU, RAM, network interfaces) according to the expected load and your network topology.


Before installation, we recommend checking the integrity of the downloaded file by verifying the **SHA256** provided on the official download page. This ensures that the image has not been altered or corrupted.


## III. Installation


In this example, the installation is performed on a virtual machine running VirtualBox. The procedure remains strictly identical on a physical machine or any other hypervisor, except for virtual device management.


### 1. Minimum hardware requirements


For a standard deployment, we recommend:



- 1 GB RAM** minimum (2 GB or more is recommended to enable additional packages or ZFS support).
- 8 GB disk space** (20 GB or more is preferable for more advanced configurations, especially if you're installing a proxy cache, IDS/IPS or detailed logs).
- At least two virtual network interfaces** (one for the WAN, one for the LAN). In VirtualBox, add them to the VM settings before startup.


### 2. Installer startup


Mount the downloaded ISO image as a virtual optical drive in VirtualBox, or insert the USB key if you're installing on a physical machine. On startup, a boot menu appears:


If you do not select any options, pfSense will automatically start up with the default options after a few seconds. Press the "**Enter**" key to initiate normal start-up.


![Image](assets/fr/027.webp)


When the main menu appears, quickly press the "**I**" button to initiate the installation.


![Image](assets/fr/001.webp)


### 3. Initial installer settings


The first screen lets you set a few regional parameters, such as display font and character encoding. These settings are useful in specific cases (non-standard keyboards, serial screens, oriental languages). For most installations, keep the default values and select "**Accept these Settings**".


![Image](assets/fr/002.webp)


### 4. Choice of installation mode


Select "**Quick/Easy Install**" to run an automated installation with the recommended options. This method deletes the selected disk and configures pfSense with the default partitioning.


![Image](assets/fr/003.webp)


A warning appears, indicating that all data on the disk will be deleted. Confirm with "**OK**".


The installer then copies the necessary files to disk. Depending on your hardware, this may take from a few seconds to a few minutes.


### 5. Core selection


When the installer prompts you to choose the kernel type, leave "**Standard Kernel**" selected. This generic kernel is perfectly suited to standard deployments, whether on a PC, server or VM.


### 6. End of installation and restart


Once installation is complete, select "**Reboot**" to reboot your machine on your new pfSense instance.


**Important note**: remove the ISO image or disconnect the installation USB key before rebooting, to avoid restarting the installation program the next time you boot.


## IV. Starting pfSense for the first time


On first start-up, pfSense must be configured to recognize and correctly assign its network interfaces (WAN, LAN, DMZ, VLANs, etc.). Careful identification of your network cards is essential to avoid any configuration errors that could deprive you of access to Interface web or render your firewall inoperative.


On launch, pfSense automatically detects and lists all available network interfaces, indicating the MAC address for each. This makes it easy to distinguish between them.


### 1. VLANs


The first question concerns the configuration of VLANs. At this stage, for a basic configuration, we won't be activating any VLANs. So press the "**N**" key to skip this step.


![Image](assets/fr/004.webp)


### 2. WAN and LAN interface assignment


pfSense then prompts you to define which Interface will be used for WAN (Internet access). You can choose between:



- Enter Interface name manually (recommended for virtual environments).
- Use automatic detection by pressing "**A**". This option is useful on a physical host, provided your network cables are connected and the links are active.


![Image](assets/fr/005.webp)


In this example, we manually configure the WAN. Enter the exact name of the Interface. For an Intel board, the name will often be "**em0**" under FreeBSD, but it may vary depending on the hardware. For example, a Realtek card will often be displayed as "**re0**".


![Image](assets/fr/006.webp)


Repeat the same operation to define the Interface LAN. Here, we use "**em1**".


pfSense confirms that the Interface LAN activates both firewall and NAT to protect your internal network and manage address translation.


If you have other physical interfaces, you can configure additional interfaces (DMZ, Wi-Fi, specific VLANs) at this stage. Each logical Interface requires a corresponding network card or virtual Interface. For initial configuration, we'll confine ourselves to WAN and LAN.


Once the assignments have been completed, pfSense displays a clear summary of the correspondences between physical interfaces and assigned roles. Confirm with "**Y**".


### 3. PfSense console


When this step is complete, the pfSense console main menu appears. It offers several useful options for direct administration, such as resetting the web password, rebooting, reloading the configuration or reassigning interfaces.


![Image](assets/fr/007.webp)


You'll also see a summary of current network settings, including the Interface LAN's default IP address, usually **192.168.1.1**. This is the address you'll need to enter in your browser to access the Interface administration web.


**Note**: If your internal network uses a different address range, select "**2)** Set Interface(s) IP Address" in the menu to assign an IP address suited to your environment.


By default, if your Interface WAN is connected to a DHCP-configured box or modem, pfSense will automatically retrieve a public IP address. You should therefore benefit from immediate Internet access by connecting a client to the pfSense Interface LAN.


## V. First access to Interface web


Once the initial start-up has been completed and the network interfaces configured, you can access pfSense's Interface web to finalize and fine-tune your configuration.


### 1. Initial connection


Connect a computer to the LAN port (or the virtual Interface LAN in your hypervisor) and assign it an IP address in the same range if necessary (by default, pfSense automatically distributes an address via DHCP on the LAN).


In your browser, go to the address indicated by the console (by default `https://192.168.1.1`). Note that pfSense requires HTTPS even for the first connection - so expect a self-signed certificate warning, which you can ignore by adding an exception.


The login screen appears. The default credentials are:


- User name:** `admin`
- Password:** `pfsense`


These identifiers will be modified during the initial configuration wizard.


## VI. Setup Wizard


On first connection, pfSense prompts you to follow its **Setup Wizard**. We strongly recommend that you use it to ensure that all essential parameters are correctly defined.


### 1. General parameters


You can:


- Specify a host name and a local domain (example: `pfsense` and `lan.local`).
- Define DNS servers and choose whether pfSense should use your ISP's DNS or an external service (Cloudflare, OpenDNS, Quad9...).


### 2. Time zone


Indicate your site's time zone so that logs and schedules are consistent (e.g. `Europe/Paris`).


### 3. WAN configuration


Configure the WAN connection:


- Defaults to **DHCP** (sufficient if you're behind a box).
- If you have a fixed IP, enter the parameters (static IP, mask, gateway, DNS) manually.
- If necessary, define a VLAN or PPPoE authentication (common with some ISPs).


### 4. LAN configuration


The wizard suggests changing the default LAN subnet. If you have a specific addressing plan, now's the time to adapt it.


### 5. Change administrator password


Secure your pfSense by immediately setting a strong password for the `admin` user.


## VII. Verification and updates


Before deploying your firewall, make sure you have the latest version of:



- Go to **System > Update**.
- Select the update channel (usually **Stable**).
- Check for updates and apply them.


It's a good idea to enable update notifications to keep you informed of security patches.


## VIII. Saving the configuration


Before making any major changes, implement a backup policy:



- Go to **Diagnostics > Backup & Restore**.
- Download a copy of the current configuration (`config.xml`).
- Keep it in a safe place (encrypted external media).


For mission-critical environments, consider automatic configuration backup on an external server or via a programmed script.


## IX. Best practices after installation


To end your deployment with peace of mind:



- Modify firewall rules**: by default, pfSense allows all outgoing traffic on the LAN and blocks incoming traffic on the WAN. Adjust these rules as required.
- Configure secure remote access**: if required, enable access to Interface web from the WAN only via VPN or with IP restrictions.
- Enable notifications**: configure an SMTP server to receive alerts (failures, updates, errors).
- Install useful extensions**: for example, IDS/IPS (Snort, Suricata), proxy (Squid), DNS filtering (pfBlockerNG).


Your pfSense firewall is now up and running, ready to protect your network. Thanks to its flexibility and active community, you have a powerful, scalable tool that can adapt to your future needs (multi-WAN, VLAN, site-to-site VPN, captive portal, etc.).


Consult the official documentation ([docs.netgate.com](https://docs.netgate.com/pfsense/en/latest/)) regularly to discover new features and make sure your configuration is up-to-date and secure.