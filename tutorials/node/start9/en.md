---
name: Start9

description: Tutorial about setting up a Start9 private server

---

![cover](assets/cover.webp)

![video](https://www.youtube.com/watch?v=DzikmY4S42Y)

*Here is a video tutorial from Southern Bitcoiner, a video guide that shows you how to setup and use a Start9 / StartOS personal server, and how to run a bitcoin node.*

## 1️⃣ Introduction

### What exactly is Start9?

Start9 is a company founded in 2020, best known for developing [**StartOS**,](https://github.com/Start9Labs/start-os) a Linux-based operating system designed for personal servers. It enables users to easily self-host a wide range of software services—such as Bitcoin and Lightning nodes, messaging apps, or password managers, while maintaining full control over their data and eliminating reliance on centralized tech platforms. StartOS features a user-friendly, browser-based interface, a curated Marketplace for installing services, and built-in privacy tools like Tor integration and system-wide HTTPS encryption. Start9 also provides hardware devices preloaded with the OS, though the software can be installed on compatible hardware or virtual machines (VMs).

### What options are available?

Start9 offers both prebuilt and DIY deployment options. The [**Server One**](https://store.start9.com/collections/servers/products/server-one) and [**Server Pure** ](https://store.start9.com/collections/servers/products/server-pure) are official hardware devices featuring high-performance components: the Server One uses an **AMD Ryzen 7 5825U** processor with configurable RAM (16GB–64GB) and storage (2TB–4TB NVMe SSD), while the Server Pure is equipped with an **Intel i7-10710U**, also offering configurable RAM and storage options. Both include **lifetime technical support** when purchased directly from Start9. For users preferring flexibility, StartOS can be installed for free on a wide range of existing hardware, including laptops, desktops, mini PCs, and single-board computers, or within VMs. 

![image](assets/en/01.webp)

### What are the differences to Umbrel?

StartOS and Umbrel both simplify self-hosted service installation but differ in architecture and features. Umbrel operates as an application layer on Debian/Ubuntu systems or VMs, whereas Start9 is a dedicated operating system requiring direct hardware or VM installation. Umbrel features a polished, macOS-inspired interface, while Start9 prioritizes a functional, minimal design. Umbrel offers a larger [selection of applications](https://apps.umbrel.com/), while the [Start9 Marketplace](https://marketplace.start9.com/) compensates with advanced technical capabilities. Start9 simplifies access to advanced settings through validated UI forms, reducing the need for command-line interaction. It also excels in backup management with one-click encrypted system backups, a feature Umbrel lacks natively. StartOS provides built-in monitoring tools and enforces HTTPS encryption for local network access, enhancing security. Umbrel uses unencrypted HTTP locally, though both platforms support secure remote access via Tor. Umbrel is suitable for users prioritizing a rich app ecosystem and a polished UI. Start9 is a strong choice for those who value security, configurability, backup reliability, and advanced service management without requiring command-line expertise. To learn more about Umbrel and the differences to Start9, please visit this course:  

[https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426](https://planb.network/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426)

## 2️⃣ DIY Prerequisites: Minimum & Recommended Specs

For basic use with minimal services, the **minimum specs** are: **1 vCPU core (2.0GHz+ boost), 4GB RAM, 64GB storage**, and an Ethernet port. That said, I’d recommend going well beyond that, especially if you're running a Bitcoin Node. Personally, I started with 1TB and quickly ran out of space. Better aim for **at least 2TB storage**, along with a **quad-core CPU (2.5GHz+)** and **8GB+ RAM**. It makes a huge difference in performance and longevity. If you want to dive deep, here is an up-to-date community thread about [Hardware Capable of Running StartOS](https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229).  

## 3️⃣ Download and Flashing the Firmware

To begin the setup, use a separate computer to visit the [Start9 website](https://start9.com/), and navigate to the documentation section by clicking `DOCS`. From there, access the `Flashing Guides` to find the appropriate version of StartOS. Two options are available: 

- StartOS (Raspberry Pi)
- StartOS (X86/ARM)

This tutorial covers the  `x86/ARM` option. 

The latest OS version can be downloaded from the [Github release page](https://github.com/Start9Labs/start-os/releases/latest). [Pre-release](https://github.com/Start9Labs/start-os/releases) versions are also available for users who wish to test new features. At the bottom of the page, under `Assets`, download the  `x86_64` or `x86_64-nonfree.iso`.  The `x86_64-nonfree.iso` image contains non-free (closed-source) software required for the Server One and most DIY hardware, particularly for graphics and network device support. 

Verifying the file's integrity by checking its SHA256 hash against the one listed on GitHub is recommended. For Linux, the command `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso` can be used, with other operating systems covered in the documentation.

After downloading and verifying the StartOS image, it must be flashed onto a USB drive. `BalenaEtcher` is a recommended software for this task. It is a free, open-source tool for writing OS image files to USB drives and SD cards, available for Windows, macOS, and Linux. Download the appropriate version from the official [Balena Etcher website](https://www.balena.io/etcher/) and run the installer. Connect the target USB drive or SD card, open Balena Etcher, and click `Flash from file` to select the downloaded OS image. Etcher will automatically detect connected drives; select the correct target if multiple are present. Click `Flash!` to begin writing the image. Etcher automatically validates the write process upon completion. Once finished, safely remove the drive and use it to boot the device.

![image](assets/en/19.webp)

## 4️⃣ Initial Setup

For the initial setup, refer to the Start9 [documentation](https://docs.start9.com/0.3.5.x/) page under `USER MANUAL` followed by `Getting Started - Initial Setup`.  This official guide should be consulted for the most current information.

Two options are presented: 

- Start Fresh 
- Recovery Options

For a new server installation, select `Start Fresh`. First, connect the server to power and an Ethernet cable. Ensure the computer used for setup is on the same local network. Remove the newly-flashed USB drive from the computer and insert it into the server. 

You can control the server remotely from any computer on the same network. Open a web browser and navigate to `http://start.local`. 

**Note**: If connection issues occur with this address, it is often due to home networks failing to resolve `.local` domain names. The problem can be resolved by accessing the server directly via its IP address. The IP can be found by logging into the router's admin interface (typically at `192.168.1.1` or a similar address), and locating the device in the DHCP clients or network map list. Then, enter the full IP address (e.g. `http://192.168.1.105`) in the browser. This bypasses DNS resolution. If issues persist, consult the  [Common Issues page](https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) or [reach out to their support.](https://start9.com/contact/)

The StartOS setup screen should appear. Click `Start Fresh` to begin the new server setup.

![image](assets/en/03.webp)

The next step is to select the storage drive where StartOS data will be stored.

![image](assets/en/04.webp)

Set a strong `Password` for the server. Record it as advised by Start9, then click `FINISH`.

![image](assets/en/05.webp)

A screen will show that StartOS is initializing and setting up the server. The next step is to `Download address info` as the `start.local` address is for setup purposes only and will not work afterward.

![image](assets/en/06.webp)

The configuration file contains two critical access addresses: one for the `local network (LAN)` and another for secure access via `Tor`. Both addresses should be saved in a secure password manager. The next step is to `Trust your Root CA`. Open a new browser tab and follow the instructions to trust the Root CA and log in. The Root CA certificate can also be downloaded by clicking `Download certificate` in the downloaded file.

## 5️⃣ Trust your Root CA

After downloading the certificate, the server's `Root CA`  must be trusted by the operating system. Click `View Instructions` and find the guidelines for the specific OS.

![image](assets/en/07.webp)

For a Linux system, the following commands are used. First, open a Terminal and install the necessary packages:

```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```

Navigate to the directory where the certificate was downloaded, typically `~/Downloads` . Execute these commands to add the certificate to the OS's trust store. Change to the downloads folder with `cd ~/Downloads`. Create the required directory with `sudo mkdir -p /usr/share/ca-certificates/start9`. Copy the certificate file, replacing  `your-filename.crt` with the actual filename, using `sudo cp "your-filename.crt" /usr/share/ca-certificates/start9/`. Register the certificate permanently by appending its path to the system configuration with `sudo bash -c "echo 'start9/your-filename.crt' >> /etc/ca-certificates.conf"`. Finally, rebuild the trust store with `sudo update-ca-certificates`. It is crucial to use the actual certificate filename and verify all paths before executing these commands. This process establishes permanent trust for the Start9 server's HTTPS connections.

A  successful installation will be indicated by an output stating `1 added`. Most applications will then be able to connect securely via `https`. If using Firefox, an additional [final step](https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff) is required. For Chrome or Brave, a different [final step](https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome) is needed to configure the browser to respect the Root CA. Test the connection by refreshing the page. If the issue persists, quit and reopen the browser before revisiting the page. 

![image](assets/en/08.webp)

## 6️⃣ Getting Started with StartOS

It should now be possible to log in using a secure HTTPS connection. Enter the `Password` to access the `Welcome Screen`. 

![image](assets/en/09.webp)

This screen provides useful shortcuts for getting started. The left sidebar contains the main menu items for navigation.

## 7️⃣ System

The Systems tab in StartOS provides access to core system functions for managing the personal server. It offers tools for system maintenance, security, diagnostics, and configuration without requiring command-line expertise.

The `Backups` section allows for the creation of full system backups, including services, configurations, and data, which can be restored later. This is essential for disaster recovery or migrating to new hardware. Backups can be stored on external drives and are encrypted using the master password.

The `Manage` section in the Systems tab allows for control over key system functions. Users can manually check for and apply StartOS updates, maintaining control over the system update process. It is possible to sideload custom or third-party services not available in the official marketplace. If the server is not connected via Ethernet, Wi-Fi settings can be configured from this section. Advanced users can enable SSH access for terminal-level system management.

![image](assets/en/10.webp)

The `Insights` section provides real-time monitoring of the server's performance and health, displaying CPU, RAM, and disk usage through graphs. It also shows system temperature, which is useful for devices like the Raspberry Pi that lack active cooling. Uptime and load average metrics help assess system stability, and live logs are available for troubleshooting service or system issues.

The `Support` section offers access to built-in FAQs, official documentation, and community support channels. Debug logs can be downloaded from this section to share with Start9 support for faster issue resolution.

![image](assets/en/11.webp)

## 8️⃣ Marketplace

The `Marketplace` is used to discover, install, and manage services on the personal server. It provides access to software such as Bitcoin Core, BTCPay Server, and electrs. StartOS supports multiple marketplaces, including the official Start9 Registry and community-run registries. These can be added by clicking `CHANGE` and switching to the `Community Registry`, which provides access to a broader range of services.

![image](assets/en/12.webp)

## 9️⃣ Installing a Bitcoin Full Node

Installing a Bitcoin full node on StartOS provides full sovereignty over the Bitcoin experience. It enables the validation of transactions and enhances privacy and security by removing reliance on external services that may log activity. Full control over transactions is gained, allowing them to be broadcast directly to the network. The default option is `Bitcoin Core`, which integrates natively with StartOS and allows for connection with wallets like Specter, Sparrow, or Electrum for a self-custody setup. An alternative, `Bitcoin Knots`, is also available through the Community Registry.

To install Bitcoin Core, navigate to the Marketplace. Under the default registry, find and install the Bitcoin Core service. After installation, a `Needs Config` prompt will appear, requiring settings to be completed before the service can run. This typically occurs after updates or fresh installations and prompts a review of `RPC settings`. Proceed with the default configuration and click `Save`. 

![image](assets/en/13.webp)

Once fully synchronized, your node can serve as a private backend for wallets like Sparrow, providing enhanced privacy and transaction validation. However, for users storing significant amounts, it is critical to understand the security trade-offs of this direct connection. When a wallet connects directly to Bitcoin Core, it can expose sensitive data, as Bitcoin Core stores public keys (xpubs) and wallet balances unencrypted on the host machine. A compromised system could allow an attacker to discover your holdings and target you.

To mitigate this risk and achieve a more robust security model, you can set up a Private Electrum Server. This server acts as an intermediary, indexing the blockchain without storing any wallet-specific information. By connecting your wallet to your own Electrum server instead of directly to Bitcoin Core, you prevent the wallet from accessing the node's sensitive data. 

![image](assets/en/14.webp)

## 🔟 Set up electrs

`electrs` (Electrum Rust Server) is a fast, efficient indexer that connects to your Bitcoin Core node and enables Electrum-compatible wallets to query transaction history and balances in real time. By running electrs on StartOS, you eliminate reliance on third-party Electrum servers, significantly improving privacy and security—your wallet queries go directly to your self-hosted node.

To set it up, first install the electrs service from the StartOS Marketplace. The system will require Bitcoin Core to be fully synced before proceeding. After installation, confirm the `Needs Config` settings with the recommended defaults and electrs begins indexing the blockchain, which may take up to a day depending on your hardware. 

![image](assets/en/15.webp)

Once complete, you can connect wallets like Sparrow or Specter. A successful connection allows your wallet to sync directly with your node, providing a secure, private, and self-hosted Bitcoin experience. 

## 1️⃣1️⃣ Connect Sparrow Wallet

To connect `Sparrow Wallet` to your StartOS node using the electrs implementation, first ensure Bitcoin Core is fully synced and electrs is installed and running. Open Sparrow Wallet on your device and navigate to `File` -> `Settings` -> `Server`. Then choose `Private Electrum Server`. In the URL field, enter the `Tor hostname` and `Port` for electrs, which you can find in StartOS under `Services` -> `electrs` -> `Properties` (typically ending in `.onion:50001`). 

![image](assets/en/16.webp)

Next, enable Tor by checking `Use Proxy`, setting the proxy address to `127.0.0.1` and port to `9050`. Click `Test Connection` and wait a few moments. A successful connection will display a confirmation message such as `Connected to electrs`. Once verified, close the settings and proceed to create or restore your wallet. This setup ensures your wallet queries your own node via electrs, providing full privacy and trustless operation.

![image](assets/en/17.webp)

## 🎯 Conclusion

StartOS by Start9 is a user-friendly, privacy-focused platform designed for self-hosting essential services like Bitcoin and Lightning nodes, wallets, and personal apps. It eliminates the need for command-line skills by offering a clean graphical interface, automated backups, health monitoring, and secure Tor access, making it ideal for non-technical users. Its modular architecture supports seamless integration with tools like electrs or Sparrow, giving you full control over your financial and digital sovereignty. With a strong focus on transparency, local control, and extensibility, StartOS empowers users to reclaim ownership from centralized platforms and run their own private, resilient infrastructure.