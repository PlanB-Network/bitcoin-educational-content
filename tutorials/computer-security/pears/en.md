---
name: Pears
description: How do I install and use applications on Pears?
---

![cover](assets/cover.webp)


In this tutorial, we'll learn how to run applications on **Pears**, a peer-to-peer (P2P) technology developed by **Holepunch** and supported by **Tether**. The aim is simple: to make it possible to distribute and use web applications without relying on any centralized infrastructure (no servers, no hosts, no intermediaries). In other words, even if a cloud provider closes down or a country blocks a domain, the application lives on among network peers.


## 1. What is Pears?


Pears is a runtime environment, development tool and deployment platform for peer-to-peer applications. This open-source tool makes it possible to build, share and run software without a server or infrastructure, directly between users. In concrete terms, this means that instead of hosting an application on a central server, each user becomes a network node, sharing part of the application and data with other peers. The whole system forms a distributed network, with each instance cooperating to keep the service accessible.


![Image](assets/fr/01.webp)


This approach is based on a set of modular software bricks developed by Holepunch:


- Hypercore**: a distributed log that guarantees data consistency and security without a central database.
- Hyperbee**: an indexer on top of Hypercore, for efficient data organization and browsing.
- Hyperdrive**: a distributed file system used to store and synchronize application files between peers.
- Hyperswarm** and **HyperDHT**: network layers that enable discovery and connection between peers worldwide, without a central server.
- Secretstream**: an E2E encryption protocol to secure exchanges between two peers.


By combining these components, Pears makes it possible to create autonomous, encrypted and distributed applications, where each user actively participates in the network. This decentralized architecture eliminates infrastructure costs, censorship risks and SPOFs (*Single Point of Failure*).


## 2. Origin and philosophy of the project


Pears is being developed by Holepunch, a company founded by Mathias Buus and Paolo Ardoino (CEO of Tether and CTO of Bitfinex), with the mission of extending peer-to-peer logic beyond Bitcoin. Their ambition is to build the "Peer-to-Peer Internet", where every application can run without authorization, without servers, and without intermediaries. Holepunch is already behind **Keet**, a fully P2P video conferencing and messaging application.


*This Pears installation tutorial is divided into several sections depending on your operating system. Go directly to the section corresponding to your environment to follow the appropriate instructions :*


- Linux (Debian)** → Part **3**
- Windows** → Part **4**
- macOS** → Part **5**


## 3. How to install Pears on Linux (Debian)


Installing Pears on a Debian system is relatively straightforward, but requires a few prerequisites, which we'll detail in this section.


### 3.1. update the system


First and foremost, it's important to make sure your system is up to date.


```bash
sudo apt update && sudo apt upgrade -y
```


![Image](assets/fr/02.webp)


### 3.2. install dependencies


Pears relies on certain system libraries, notably `libatomic1`, used by the Bare JavaScript runtime. Install it with the following command:


```bash
sudo apt install -y libatomic1 curl git
```


![Image](assets/fr/03.webp)


### 3.3. install Node.js and npm via NVM


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


### 3.4 Installing Pears with npm


Once *npm* is available, you can install Pears CLI globally on your system. This will allow you to run the `pear` command from any directory.


```bash
npm install -g pear
```


![Image](assets/fr/09.webp)


### 3.5. Initialize Pears


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


### 3.6. Testing Pears with Keet


To check that Pears is fully operational, you can launch a P2P application already available on the network, such as Keet, Holepunch's open-source messaging and videoconferencing software.


```bash
pear run pear://keet
```


This command loads the Keet application directly from the Pears network, without passing through a central server. If Keet launches correctly, your Pears installation is fully functional.


![Image](assets/fr/12.webp)


Your Linux system is now ready to run and host peer-to-peer applications with Pears.


## 4. How to install Pears on Windows


Installing Pears on Windows is just as easy as on Linux, but requires a few special tools.


*If you're using Linux, you can skip to step 6.*


### 4.1. open PowerShell in administrator mode


First of all, run PowerShell with administrator rights :


- Click on the Start menu;
- Type PowerShell ;
- Right-click on "*Windows PowerShell*" ;
- Select "*Run as administrator*".


![Image](assets/fr/15.webp)


### 4.2. download NVS


Pears is installed via *npm*, the *Node.js* package manager. On Windows, the method recommended by Holepunch is to use *NVS* (*Node Version Switcher*), which is more stable than *NVM* on this system.


In PowerShell, run the following command to install the latest version of *NVS* :


```PowerShell
winget install jasongin.nvs
```


![Image](assets/fr/16.webp)


### 4.3. install Node.js


After installation, restart PowerShell and enter the following command:


```powershell
nvs
```


You should see a list of available *Node.js* versions. Select the first one by pressing the `a` key on your keyboard.


![Image](assets/fr/17.webp)


*Node.js* is installed.


![Image](assets/fr/18.webp)


### 4.4. Check installations


Make sure *Node.js* and *npm* are accessible:


```powershell
node -v
npm -v
```


Both commands must return a version number.


![Image](assets/fr/19.webp)


### 4.5. Installing Pears with npm


Once *Node.js* and *npm* are available, install **Pears CLI** globally on your system:


```powershell
npm install -g pear
```


This will install the `pear` binary in your global *npm* directory.


![Image](assets/fr/20.webp)


### 4.6. Check and initialize Pears


Once installation is complete, run :


```powershell
pear
```


On first launch, Pears will automatically download the necessary components from the peer-to-peer network. This process may take a few moments.


![Image](assets/fr/21.webp)


If all has gone well, you should see the CLI Pears help screen with a list of available sub-commands (run, seed, info...).


### 4.7. Testing Pears with Keet


To check that Pears is fully operational, you can launch a P2P application already available on the network, such as Keet, Holepunch's open-source messaging and videoconferencing software.


```bash
pear run pear://keet
```


This command loads the Keet application directly from the Pears network, without passing through a central server. If Keet launches correctly, your Pears installation is fully functional.


![Image](assets/fr/22.webp)


Your Windows system is now ready to run and host peer-to-peer applications with Pears.


## 5. How do I install Pears on macOS?


Installing Pears on macOS is similar to installing it on Linux, but requires a few adjustments specific to the Apple environment. Let's discover these steps together.


*If you're using Linux or Windows and have already installed Pears, you can proceed directly to **step 6**.*


### 5.1. Check system requirements


Before installing, please ensure that *Xcode Command Line Tools* is present on your system. This package provides the necessary compilation tools for _Node.js_ and its dependencies.


To do this, open a terminal with the keyboard shortcut `Cmd + Space bar`, then type `Terminal` and press the `Enter` key. You can then enter this command in the terminal to launch the installation:


```bash
xcode-select --install
```


If the tools are already installed on your system, macOS will inform you.


### 5.2. install NVM


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


### 5.3. install Node.js and npm


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


### 5.4 Installing Pears with npm


Once *npm* is available, you can install Pears CLI globally on your system. This will allow you to run the `pear` command from any directory.


```bash
npm install -g pear
```


### 5.5. Initialize Pears


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


### 5.6. Testing Pears with Keet


To check that Pears is fully operational, you can launch a P2P application already available on the network, such as Keet, Holepunch's open-source messaging and videoconferencing software.


```bash
pear run pear://keet
```


This command loads the Keet application directly from the Pears network, without passing through a central server. If Keet launches correctly, your Pears installation is fully functional.


Your macOS system is now ready to run and host peer-to-peer applications with Pears.


## 6. How do I use an application on Pears?


Once Pears is up and running, you can run the application of your choice directly with the following command:


```bash
pear run pear://[KEY]
```


Simply replace `[KEY]` with the application key you wish to use.


![Image](assets/fr/13.webp)


To learn how to run our Plan ₿ Academy platform on Pears, check out this comprehensive tutorial :


https://planb.academy/tutorials/contribution/others/pears-plan-b-academy-77f0ae28-28fc-4465-a9f1-1c6654711770

And to find out how to use the Keet messaging application you've just launched on Pears, check out this tutorial :


https://planb.academy/tutorials/computer-security/communication/keet-efdb759d-5e94-4bbf-b28c-5fa8669c809b