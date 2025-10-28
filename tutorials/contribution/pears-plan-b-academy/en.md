---
name: Plan ₿ Academy - Pears App
description: How to install and use the Plan ₿ Academy application on Pears?
---

![cover](assets/cover.webp)

You probably already know that Plan ₿ Academy is the largest educational database dedicated to Bitcoin, bringing together courses, tutorials, and thousands of open-source resources. Originally, Plan ₿ Academy was a website. But what would happen if you could no longer access it normally, for example in the event of censorship?

In this tutorial, we will learn how to run the **Plan ₿ Academy** platform in a truly censorship-resistant way using **Pears**, a peer-to-peer (P2P) technology developed by **Holepunch** and supported by **Tether**.

Pears is the software that allows us to run the Plan ₿ Academy platform without relying on a centralized website. In this tutorial, we will install Pears on your computer in order to access Plan ₿ Academy through Pears.

The goal of Pears is simple: to make it possible to distribute and use web applications without depending on any centralized infrastructure (no servers, no hosts, no intermediaries). In other words, even if a cloud provider shuts down or a country blocks a domain, the application continues to live among the network’s peers. This approach allows our educational platform, Plan ₿ Academy, to remain accessible worldwide, without a single point of failure.

---

**TL;DR:**

* Install Pears;

* Run the following command to launch the Plan ₿ Academy app:

```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```

---

## 1. Install Pears

### 1.1. What is Pears?

Pears is at once a runtime environment, a development tool, and a deployment platform for peer-to-peer applications. This open-source tool allows you to build, share, and run software without servers or infrastructure, directly between users. In practical terms, this means that instead of hosting an application on a central server, each user becomes a node in the network: they share part of the application and data with other peers. The entire system forms a distributed network where each instance cooperates to keep the service accessible.

![Image](assets/fr/01.webp)

This approach is based on a set of modular software components developed by Holepunch:

* **Hypercore**: a distributed log that ensures data consistency and security without a central database.
* **Hyperbee**: an index built on top of Hypercore that allows data to be organized and queried efficiently.
* **Hyperdrive**: a distributed file system used to store and synchronize application files among peers.
* **Hyperswarm** and **HyperDHT**: network layers that enable peer discovery and connections worldwide without a central server.
* **Secretstream**: an end-to-end encryption protocol that secures communication between peers.

By combining these components, Pears enables the creation of autonomous, encrypted, and distributed applications, where every user actively participates in the network. This decentralized architecture eliminates infrastructure costs, censorship risks, and SPOFs (*Single Points of Failure*).

Pears is developed by Holepunch, a company founded by Mathias Buus and Paolo Ardoino (CEO of Tether and CTO of Bitfinex), with the mission of extending peer-to-peer logic beyond Bitcoin. Their ambition is to build the “*Internet of peers*,” where every application can operate without permission, without servers, and without intermediaries. Holepunch is already behind **Keet**, a fully P2P video conferencing and messaging app.

https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*This Pears installation tutorial is divided into multiple sections depending on your operating system. Go directly to the one corresponding to your environment to follow the appropriate instructions:*

* **Linux (Debian)** → Section **1.2**
* **Windows** → Section **1.3**
* **macOS** → Section **1.4**

### 1.2. How to install Pears on Linux (Debian)?

Installing Pears on Debian is relatively simple but requires a few prerequisites, which we will detail in this section.

#### 1.2.1. Update the system

Before anything else, it’s important to make sure your system is up to date.

```bash
sudo apt update && sudo apt upgrade -y
```

![Image](assets/fr/02.webp)

#### 1.2.2. Install dependencies

Pears relies on some system libraries, including `libatomic1`, used by the Bare JavaScript runtime engine. Install it with the following command:

```bash
sudo apt install -y libatomic1 curl git
```

![Image](assets/fr/03.webp)

#### 1.2.3. Install Node.js and npm via NVM

Pears is distributed through *npm*, the *Node.js* package manager. Although Pears doesn’t directly depend on *Node.js* to run, it is required for installation. The recommended way to install *Node.js* on Linux is through *NVM* (*Node Version Manager*), which allows you to manage multiple versions of Node side by side.

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```

![Image](assets/fr/04.webp)

Then, reload your terminal to activate *NVM*:

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

Verify that *Node.js* and *npm* are properly installed:

```bash
node -v
npm -v
```

![Image](assets/fr/08.webp)

#### 1.2.4. Install Pears with npm

Once *npm* is available, you can globally install the Pears CLI on your system. This allows you to run the `pear` command from any directory.

```bash
npm install -g pear
```

![Image](assets/fr/09.webp)

#### 1.2.5. Initialize Pears

After installation, simply run the following command in your terminal:

```bash
pear
```

At first launch, Pears will connect to the peer-to-peer network to download the necessary components. This process doesn’t rely on any central server — the files are retrieved directly from other peers.

![Image](assets/fr/10.webp)

Once the download is complete, run the command again to confirm everything works:

```bash
pear
```

![Image](assets/fr/11.webp)

If everything is correctly installed, the Pears help menu will appear with a list of available commands.

#### 1.2.6. Test Pears with Keet

To verify that Pears is fully operational, you can launch an existing P2P application available on the network, such as Keet, the open-source messaging and video conferencing software developed by Holepunch.

```bash
pear run pear://keet
```

This command loads the Keet application directly from the Pears network, without using a central server. If Keet launches correctly, it means your Pears installation is fully functional.

![Image](assets/fr/12.webp)

Your Linux system is now ready to run and host peer-to-peer applications with Pears.

### 1.3. How to Install Pears on Windows

Installing Pears on Windows is just as simple as on Linux but requires a few specific tools.

*If you’re using Linux and have already installed Pears, you can skip directly to **Step 2**.*

#### 1.3.1. Open PowerShell as Administrator

First, launch PowerShell with administrator privileges:

* Click on the Start menu;
* Type “PowerShell”;
* Right-click on "*Windows PowerShell*";
* Select "*Run as administrator*".

![Image](assets/fr/15.webp)

#### 1.3.2. Download NVS

Pears is installed via *npm*, the *Node.js* package manager. On Windows, the method recommended by Holepunch is to use *NVS* (*Node Version Switcher*), which is more stable than *NVM* on this system.

In PowerShell, run the following command to install the latest version of *NVS*:

```PowerShell
winget install jasongin.nvs
```

![Image](assets/fr/16.webp)

#### 1.3.3. Install Node.js

After installation, restart PowerShell, then enter the following command:

```powershell
nvs
```

You should see a list of available *Node.js* versions. Select the first one by pressing the `a` key on your keyboard.

![Image](assets/fr/17.webp)

*Node.js* is now installed.

![Image](assets/fr/18.webp)

#### 1.3.4. Verify Installations

Make sure *Node.js* and *npm* are accessible:

```powershell
node -v
npm -v
```

Both commands should return a version number.

![Image](assets/fr/19.webp)

#### 1.3.5. Install Pears with npm

Once *Node.js* and *npm* are available, install **Pears CLI** globally on your system:

```powershell
npm install -g pear
```

This installs the `pear` binary in your global *npm* directory.

![Image](assets/fr/20.webp)

#### 1.3.6. Verify and Initialize Pears

Once installation is complete, run:

```powershell
pear
```

At first launch, Pears will automatically download the required components from the peer-to-peer network. This process may take a few moments.

![Image](assets/fr/21.webp)

If everything went well, you should see the Pears CLI help menu with the list of available subcommands (run, seed, info...).

#### 1.3.7. Test Pears with Keet

To verify that Pears is fully operational, you can launch an existing P2P application available on the network, such as Keet — the open-source messaging and video conferencing software developed by Holepunch.

```bash
pear run pear://keet
```

This command loads the Keet application directly from the Pears network, without using any central server. If Keet launches successfully, it means your Pears installation is fully functional.

![Image](assets/fr/22.webp)

Your Windows system is now ready to run and host peer-to-peer applications with Pears.

### 1.4. How to Install Pears on macOS

Installing Pears on macOS is similar to Linux but requires a few adjustments specific to Apple’s environment. Let’s go through these steps together.

*If you’re using Linux or Windows and have already installed Pears, you can skip directly to **Step 2**.*

#### 1.4.1. Check System Prerequisites

Before installation, make sure *Xcode Command Line Tools* are installed on your system. This package provides the necessary build tools for *Node.js* and its dependencies.

To do this, open a terminal using the shortcut `Cmd + Space bar`, type `Terminal`, and press `Enter`. Then, run the following command in the terminal to install it:

```bash
xcode-select --install
```

If the tools are already installed on your system, macOS will notify you.

#### 1.4.2. Install NVM

Pears is distributed via *npm*, the *Node.js* package manager. Although Pears doesn’t directly depend on *Node.js* to function, it’s required for installation. The recommended method for installing *Node.js* on macOS is *NVM* (*Node Version Manager*), which allows you to manage multiple Node versions simultaneously.

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```

Then reload your terminal to activate *NVM*:

```bash
source ~/.zshrc
```

If you use *bash* instead of *zsh*, run:

```bash
source ~/.bashrc
```

Next, check that *NVM* is installed correctly:

```bash
nvm --version
```

Your terminal should display the installed *NVM* version.

#### 1.4.3. Install Node.js and npm

Next, install a stable version of *Node.js* (for example, the current LTS version):

```bash
nvm install --lts
```

Once the installation is complete, verify the installed versions:

```bash
node -v
npm -v
```

Both commands should return a version number.

#### 1.4.4. Install Pears with npm

Once *npm* is available, you can globally install the Pears CLI on your system. This will allow you to execute the `pear` command from any directory.

```bash
npm install -g pear
```

#### 1.4.5. Initialize Pears

After installation, simply run the following command in your terminal:

```bash
pear
```

At first launch, Pears connects to the peer-to-peer network to download the necessary components. This process doesn’t require any central server — files are retrieved directly from other peers.

Once the download is complete, rerun the command to verify that everything works:

```bash
pear
```

If everything is correctly installed, the Pears help menu will appear with the list of available commands.

#### 1.4.6. Test Pears with Keet

To verify that Pears is fully operational, you can launch a P2P application already available on the network, such as Keet, the open-source messaging and video conferencing software from Holepunch.

```bash
pear run pear://keet
```

This command loads the Keet app directly from the Pears network, without using a central server. If Keet launches successfully, it means your Pears installation is fully functional.

Your macOS system is now ready to run and host peer-to-peer applications with Pears.

## 2. How to Use Plan ₿ Academy on Pears

Once Pears is installed and running, you can directly launch the **Plan ₿ Academy** platform through the P2P network. Simply run the following command in your terminal (the same command works on Linux, Windows, and macOS):

```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```

![Image](assets/fr/13.webp)

Once loading is complete, Plan ₿ Academy will open within your Pears environment, ready to be used just like the original website — but without any dependence on a central server.

![Image](assets/fr/14.webp)

## 3. How to Seed Plan ₿ Academy on Pears

In the Pears network, to *seed* an application means to redistribute it to other peers from your own machine. In practice, when you seed Plan ₿ Academy, your computer becomes a data source that allows other users to download the application without relying on a central server.

This mechanism strengthens the resilience and censorship resistance of our application on the Pears network. The more peers seed an application, the more available and decentralized it becomes, even if some original nodes go offline.

To help distribute Plan ₿ Academy, simply run the following command:

```bash
pear seed pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```

As long as this command remains active, your device will participate in distributing the application’s files. If you close the terminal, the sharing process stops.

To continue seeding after a restart, you can run the command in the background or create a system service — for example, a systemd service on Linux, a LaunchAgent on macOS, or a scheduled task on Windows. These methods ensure that the Plan ₿ Academy application automatically resumes seeding at system startup.

Thank you for contributing to the decentralized distribution of Plan ₿ Academy on Pears and helping make Bitcoin education truly censorship-resistant!
