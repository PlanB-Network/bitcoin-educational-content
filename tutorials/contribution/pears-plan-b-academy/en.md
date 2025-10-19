---
name: Map ₿ Academy - Pears App
description: How do I install and use the Plan ₿ Academy application on Pears?
---

![cover](assets/cover.webp)


As you probably know, Plan ₿ Academy is the largest educational database dedicated to Bitcoin, bringing together courses, tutorials and thousands of resources published under an open license. Originally, Plan ₿ Academy was a website. But what would happen if you could no longer access it normally, for example in the event of censorship?


In this tutorial, we'll learn how to run the **Plan ₿ Academy** platform in a truly incensurable way thanks to **Pears**, a peer-to-peer (P2P) technology developed by **Holepunch** and supported by **Tether**.


Pears is the software that will enable us to run the Plan ₿ Academy platform without relying on a centralized website. In this tutorial, we'll install Pears on your computer to access Plan ₿ Academy via Pears.


Pears' objective is simple: to make it possible to distribute and use web applications without relying on any centralized infrastructure (no servers, no hosts, no intermediaries). In other words, even if a cloud provider closes down or a country blocks a domain, the application lives on among the network's peers. It's this approach that enables our educational platform Plan ₿ Academy to remain accessible anywhere in the world, with no single point of failure.


---

**TL;DR :**



- Install Pears ;



- Run the following command to launch the Plan ₿ Academy application:


```shell
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


---

## 1. Install Pears


### 1.1 What is Pears?


Pears is a runtime environment, development tool and deployment platform for peer-to-peer applications. This open-source tool makes it possible to build, share and run software without a server or infrastructure, directly between users. In concrete terms, this means that instead of hosting an application on a central server, each user becomes a network node, sharing part of the application and data with other peers. The whole system forms a distributed network, with each instance cooperating to keep the service accessible.


![Image](assets/fr/01.webp)


This approach is based on a set of modular software bricks developed by Holepunch:


- Hypercore**: a distributed log that guarantees data consistency and security without a central database.
- Hyperbee**: an indexer on top of Hypercore, for efficient data organization and browsing.
- Hyperdrive**: a distributed file system used to store and synchronize application files between peers.
- Hyperswarm** and **HyperDHT**: network layers that enable discovery and connection between peers worldwide, without a central server.
- Secretstream**: an E2E encryption protocol to secure exchanges between two peers.


By combining these components, Pears makes it possible to create autonomous, encrypted and distributed applications, where each user actively participates in the network. This decentralized architecture eliminates infrastructure costs, censorship risks and SPOFs (*Single Point of Failure*).


Pears is being developed by Holepunch, a company founded by Mathias Buus and Paolo Ardoino (CEO of Tether and CTO of Bitfinex), with the mission of extending peer-to-peer logic beyond Bitcoin. Their ambition is to build the "Peer-to-Peer Internet", where every application can run without authorization, without servers, and without intermediaries. Holepunch is already behind **Keet**, a fully P2P video-conferencing and messaging application.


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b

*This Pears installation tutorial is divided into several sections depending on your operating system. Go directly to the section corresponding to your environment to follow the appropriate instructions :*


- Linux (Debian)** → Part **1.2.**
- Windows** → Part **1.3.**
- macOS** → Part **1.4.**



### 1.2 - How do I install Pears on Linux (Debian)?


Installing Pears on a Debian system is relatively straightforward, but requires a few prerequisites, which we'll explain in detail in this section.


#### 1.2.1. Updating the system


First and foremost, it's important to make sure your system is up to date.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


#### 1.2.2 Installing dependencies


Pears relies on a number of system libraries, including `libatomic1`, used by the Bare JavaScript runtime. Install it with the following command:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


#### 1.2.3 Installing Node.js and npm via NVM


Pears is distributed via *npm*, the *Node.js* package manager. Although Pears does not depend directly on *Node.js* to function, it is necessary for installation. The recommended method for installing *Node.js* on Linux is *NVM* (*Node Version Manager*), which allows you to manage several versions of Node in parallel.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


![Image](assets/fr/04.webp)


Then reload your terminal to activate *NVM* :


```bash
source ~/.bashrc
```


![Image](assets/fr/05.webp)


Check that *NVM* is installed:


```bash
nvm --version
```


![Image](assets/fr/06.webp)


Then install a stable version of *Node.js* (e.g. the current LTS):


```bash
nvm install --lts
```


![Image](assets/fr/07.webp)


Check *Node.js* and *npm* installations:


```bash
node -v
npm -v
```


![Image](assets/fr/08.webp)


#### 1.2.4 Installing Pears with npm


Once *npm* is available, you can install Pears CLI globally on your system. This will allow you to run the `pear` command from any directory.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


#### 1.2.5. Initialize Pears


After installation, simply run the following command in your terminal:


```bash
pear
```


On first start-up, Pears will connect to the peer-to-peer network to download the necessary components. This process requires no central server: files are obtained directly from other peers.


![Image](assets/fr/10.webp)


Once the download is complete, run the command again to check that everything is working:


```bash
pear
```


![Image](assets/fr/11.webp)


If everything is correctly installed, Pears Help will be displayed with a list of available commands.


#### 1.2.6. Testing Pears with Keet


To check that Pears is fully operational, you can launch a P2P application already available on the network, such as Keet, Holepunch's open-source messaging and videoconferencing software.


```bash
pear run pear://keet
```


This command loads the Keet application directly from the Pears network, without passing through a central server. If Keet launches correctly, your Pears installation is fully functional.


![Image](assets/fr/12.webp)


Your Linux system is now ready to run and host peer-to-peer applications with Pears.


### 1.3 - How do I install Pears on Windows?


Installing Pears on Windows is just as easy as on Linux, but requires a few special tools.


*If you're using Linux and have already installed Pears, you can proceed directly to step 2


#### 1.3.1. Open PowerShell in administrator mode


First of all, run PowerShell with administrator rights :


- Click on the Start menu;
- Type PowerShell ;
- Right-click on "*Windows PowerShell*" ;
- Select "*Run as administrator*".


![Image](assets/fr/15.webp)


#### 1.3.2. Download NVS


Pears is installed via *npm*, the *Node.js* package manager. On Windows, the method recommended by Holepunch is to use *NVS* (*Node Version Switcher*), which is more stable than *NVM* on this system.


In PowerShell, run the following command to install the latest version of *NVS* :


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


#### 1.3.3. Installing Node.js


After installation, restart PowerShell and enter the following command:


```powershell
nvs
```


You should see a list of available *Node.js* versions. Select the first one by pressing the `a` key on your keyboard.


![Image](assets/fr/17.webp)


*Node.js* is installed.


![Image](assets/fr/18.webp)


#### 1.3.4. Check installations


Make sure *Node.js* and *npm* are accessible:


```powershell
node -v
npm -v
```


Both commands must return a version number.


![Image](assets/fr/19.webp)


#### 1.3.5. Installing Pears with npm


Once *Node.js* and *npm* are available, install **Pears CLI** globally on your system:


```powershell
npm install -g pear
```


This will install the `pear` binary in your global *npm* directory.


![Image](assets/fr/20.webp)


#### 1.3.6. Check and initialize Pears


Once installation is complete, run :


```powershell
pear
```


On first launch, Pears will automatically download the necessary components from the peer-to-peer network. This process may take a few moments.


![Image](assets/fr/21.webp)


If all has gone well, you should see the CLI Pears help screen with a list of available sub-commands (run, seed, info...).


#### 1.3.7. Testing Pears with Keet


To check that Pears is fully operational, you can launch a P2P application already available on the network, such as Keet, Holepunch's open-source messaging and videoconferencing software.


```bash
pear run pear://keet
```


This command loads the Keet application directly from the Pears network, without passing through a central server. If Keet launches correctly, your Pears installation is fully functional.


![Image](assets/fr/22.webp)


Your Windows system is now ready to run and host peer-to-peer applications with Pears.


### 1.4. How to install Pears on macOS?


Installing Pears on macOS is similar to installing it on Linux, but requires a few adjustments specific to the Apple environment. Let's discover these steps together.


*If you are using Linux or Windows and have already installed Pears, you can proceed directly to step 2


#### 1.4.1. Check system requirements


Before installing, please ensure that *Xcode Command Line Tools* is present on your system. This package provides the necessary compilation tools for _Node.js_ and its dependencies.


To do this, open a terminal with the keyboard shortcut `Cmd + Space bar`, then type `Terminal` and press the `Enter` key. You can then enter this command in the terminal to launch the installation:


```bash
xcode-select --install
```


If the tools are already installed on your system, macOS will inform you.


#### 1.4.2. Installing NVM


Pears is distributed via *npm*, the *Node.js* package manager. Although Pears does not depend directly on *Node.js* to function, it is necessary for installation. The recommended method for installing *Node.js* on macOS is *NVM* (*Node Version Manager*), which allows you to manage several versions of Node in parallel.


```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```


Then reload your terminal to activate *NVM* :


```bash
source ~/.zshrc
```


If you use *bash* rather than *zsh*, run :


```bash
source ~/.bashrc
```


Then check that *NVM* is installed:


```bash
nvm --version
```


The terminal should return the version of *NVM* installed on your system.


#### 1.4.3 Installing Node.js and npm


Then install a stable version of *Node.js* (e.g. the current LTS):


```bash
nvm install --lts
```


Once installation is complete, check the installed versions:


```bash
node -v
npm -v
```


Both commands must return a version number.


#### 1.4.4 Installing Pears with npm


Once *npm* is available, you can install Pears CLI globally on your system. This will allow you to run the `pear` command from any directory.


```bash
npm install -g pear
```


#### 1.4.5. Initialize Pears


After installation, simply run the following command in your terminal:


```bash
pear
```


On first start-up, Pears will connect to the peer-to-peer network to download the necessary components. This process requires no central server: files are obtained directly from other peers.


Once the download is complete, run the command again to check that everything is working:


```bash
pear
```


If everything is correctly installed, Pears Help will be displayed with a list of available commands.


#### 1.4.6. Testing Pears with Keet


To check that Pears is fully operational, you can launch a P2P application already available on the network, such as Keet, Holepunch's open-source messaging and videoconferencing software.


```bash
pear run pear://keet
```


This command loads the Keet application directly from the Pears network, without passing through a central server. If Keet launches correctly, your Pears installation is fully functional.


Your macOS system is now ready to run and host peer-to-peer applications with Pears.


## 2. How do I use Plan ₿ Academy on Pears?


Once Pears is installed and running, you can directly run the **Plan ₿ Academy** platform via the P2P network. Simply execute the following command in your terminal (it's the same command for Linux, Windows and macOS):


```bash
pear run pear://k9cawqdsan3bkobkigesuyfeqjcasi49ikjaru5cipap835t7nwy
```


![Image](assets/fr/13.webp)


Once uploaded, Plan ₿ Academy will open in your Pears environment, ready to be used as on the original website, but without any dependency on a central server.


![Image](assets/fr/14.webp)