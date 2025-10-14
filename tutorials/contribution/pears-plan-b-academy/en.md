---
name: Pears - Plan ₿ Academy
description: How to install and use the Plan ₿ Academy app on Pears?
---

![cover](assets/cover.webp)

As you probably know, Plan ₿ Academy is the largest educational database dedicated to Bitcoin, bringing together courses, tutorials, and thousands of open-source resources. Originally, Plan ₿ Academy was a website. But what would happen if you could no longer access it normally—for instance, in the event of censorship?

In this tutorial, we will learn how to run the **Plan ₿ Academy** platform in a truly censorship-resistant way thanks to **Pears**, a peer-to-peer (P2P) technology developed by **Holepunch** and supported by **Tether**. The goal is simple: to make it possible to distribute and use web applications without relying on any centralized infrastructure (no servers, no hosts, no intermediaries). In other words, even if a cloud provider shuts down or a country blocks a domain, the application continues to live among the network’s peers. This approach ensures that our educational platform, Plan ₿ Academy, remains accessible worldwide with no single point of failure.

## 1. What is Pears?

Pears is both a runtime environment, a development tool, and a deployment platform for peer-to-peer applications. This open-source tool allows you to build, share, and run software without servers or infrastructure—directly between users. In practical terms, instead of hosting an application on a central server, each user becomes a node in the network, sharing part of the application and its data with other peers. The entire system forms a distributed network where every instance cooperates to keep the service available.

![Image](assets/fr/01.webp)

This approach relies on a set of modular software components developed by Holepunch:

* **Hypercore**: a distributed log ensuring data consistency and integrity without a central database.
* **Hyperbee**: an index layer built on top of Hypercore that allows efficient data organization and traversal.
* **Hyperdrive**: a distributed file system used to store and synchronize application files among peers.
* **Hyperswarm** and **HyperDHT**: network layers that enable peer discovery and connections across the globe without a central server.
* **Secretstream**: an end-to-end encryption protocol securing exchanges between peers.

By combining these components, Pears makes it possible to create autonomous, encrypted, and distributed applications where every user actively contributes to the network. This decentralized architecture eliminates infrastructure costs, censorship risks, and SPOFs (Single Points of Failure).

## 2. Origin and Philosophy of the Project

Pears is developed by Holepunch, a company founded by Mathias Buus and Paolo Ardoino (CEO of Tether and CTO of Bitfinex), with the mission of extending peer-to-peer logic beyond Bitcoin. Their ambition is to build the “*Internet of peers*,” where each application can operate without permission, without servers, and without intermediaries. Holepunch is already behind **Keet**, a fully P2P video-conferencing and messaging application.

https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

## 3. How to Install Pears on Linux (Debian)

Installing Pears on Debian is relatively simple but requires a few prerequisites, which we will detail in this section.

*If you are using Windows, you can skip directly to step 4.*

### 3.1. Update the System

Before anything else, make sure your system is up to date.

```bash
sudo apt update && sudo apt upgrade -y
```

![Image](assets/fr/02.webp)

### 3.2. Install Dependencies

Pears depends on certain system libraries, including `libatomic1`, which is used by the Bare JavaScript runtime engine. Install it with the following command:

```bash
sudo apt install -y libatomic1 curl git
```

![Image](assets/fr/03.webp)

### 3.3. Install Node.js and npm via NVM

Pears is distributed through *npm*, the *Node.js* package manager. Although Pears does not directly depend on *Node.js* to run, it is required for installation. The recommended way to install *Node.js* on Linux is via *NVM* (Node Version Manager), which allows you to manage multiple Node versions side by side.

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```

![Image](assets/fr/04.webp)

Then reload your terminal to activate *NVM*:

```bash
source ~/.bashrc
```

![Image](assets/fr/05.webp)

Check that *NVM* is properly installed:

```bash
nvm --version
```

![Image](assets/fr/06.webp)

Next, install a stable version of *Node.js* (for example, the current LTS version):

```bash
nvm install --lts
```

![Image](assets/fr/07.webp)

Verify your *Node.js* and *npm* installations:

```bash
node -v
npm -v
```

![Image](assets/fr/08.webp)

### 3.4. Install Pears with npm

Once *npm* is available, you can globally install the Pears CLI on your system. This will allow you to use the `pear` command from any directory.

```bash
npm install -g pear
```

![Image](assets/fr/09.webp)

### 3.5. Initialize Pears

After installation, simply run the following command in your terminal:

```bash
pear
```

At first launch, Pears connects to the peer-to-peer network to download the necessary components. This process requires no central server: the files are retrieved directly from other peers.

![Image](assets/fr/10.webp)

Once the download is complete, relaunch the command to confirm everything works:

```bash
pear
```

![Image](assets/fr/11.webp)

If everything was installed correctly, the Pears help menu will appear, listing all available commands.

### 3.6. Test Pears with Keet

To ensure Pears is fully operational, you can launch an existing P2P application available on the network, such as Keet, the open-source messaging and video-conferencing app by Holepunch.

```bash
pear run pear://keet
```

This command loads the Keet application directly from the Pears network, without using any central server. If Keet launches successfully, it means your Pears installation is fully functional.

![Image](assets/fr/12.webp)

Your Linux system is now ready to run and host peer-to-peer applications using Pears.

## 4. How to Install Pears on Windows

Installing Pears on Windows is just as simple as on Linux but requires a few specific tools.

*If you are using Linux, you can skip directly to step 5.*

### 4.1. Open PowerShell as Administrator

First, launch PowerShell with administrator privileges:

* Click on the Start menu
* Type “PowerShell”
* Right-click on "*Windows PowerShell*"
* Select "*Run as administrator*"

![Image](assets/fr/15.webp)

### 4.2. Download NVS

Pears is installed via *npm*, the *Node.js* package manager. On Windows, the method recommended by Holepunch is to use *NVS* (*Node Version Switcher*), which is more stable than *NVM* on this operating system.

In PowerShell, run the following command to install the latest version of *NVS*:

```PowerShell
winget install jasongin.nvs
```

![Image](assets/fr/16.webp)

### 4.3. Install Node.js

After installation, restart PowerShell, then enter the following command:

```powershell
nvs
```

You should see a list of available *Node.js* versions. Select the first one by pressing the `a` key on your keyboard.

![Image](assets/fr/17.webp)

*Node.js* is now installed.

![Image](assets/fr/18.webp)

### 4.4. Verify the Installations

Make sure *Node.js* and *npm* are accessible:

```powershell
node -v
npm -v
```

Both commands should return a version number.

![Image](assets/fr/19.webp)

### 4.5. Install Pears with npm

Once *Node.js* and *npm* are available, install **Pears CLI** globally on your system:

```powershell
npm install -g pear
```

This will install the `pear` binary in your global *npm* directory.

![Image](assets/fr/20.webp)

### 4.6. Verify and Initialize Pears

Once the installation is complete, run:

```powershell
pear
```

At first launch, Pears will automatically download the necessary components from the peer-to-peer network. This process may take a few moments.

![Image](assets/fr/21.webp)

If everything went well, you should see the Pears CLI help menu with the list of available subcommands (run, seed, info...).

### 4.7. Test Pears with Keet

To verify that Pears is fully operational, you can launch an existing P2P application available on the network, such as Keet, the open-source messaging and video-conferencing software developed by Holepunch.

```bash
pear run pear://keet
```

This command loads the Keet application directly from the Pears network, without relying on any central server. If Keet launches successfully, it means your Pears installation is working perfectly.

![Image](assets/fr/22.webp)

Your Windows system is now ready to run and host peer-to-peer applications with Pears.

## 5. How to Use Plan ₿ Academy on Pears

Once Pears is installed and running properly, you can directly launch the **Plan ₿ Academy** platform through the P2P network. Simply execute the following command in your terminal (the same command works for both Linux and Windows):

```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```

![Image](assets/fr/13.webp)

Once the loading is complete, Plan ₿ Academy will open within your Pears environment, ready to be used just like on the original website, but without relying on any centralized server.

![Image](assets/fr/14.webp)
