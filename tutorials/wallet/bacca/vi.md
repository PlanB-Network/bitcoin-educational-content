---
name: Bacca
description: Configuring a Ledger without Ledger Live software
---
![cover](assets/cover.webp)

If you use a Ledger, you've probably found that you have to go through Ledger Live software, at least for the initial device configuration, to check its authenticity and install the Bitcoin application on it. However, after this configuration, many bitcoiners prefer to use specialized Bitcoin wallet management software such as Sparrow or Liana rather than Ledger Live. Although Ledger produces excellent hardware wallets that quickly include the latest Bitcoin features, their software is not necessarily adapted to the specific needs of bitcoiners. Indeed, Ledger Live includes many features designed for altcoins, while the options dedicated to Bitcoin wallet management are limited. But the problem with Sparrow and Liana (for the moment), is that they don't allow you to install the Bitcoin application on the Ledger.

To bypass the need to use Ledger Live during the initial configuration of your Ledger, you can use the Bacca tool, (or "Ledger Installer"). This software allows you to install and update the Bitcoin application, verify the authenticity of your Ledger, and even later update the device's firmware. Bacca was created by Antoine Poinsot (Darosior), Bitcoin Core developer at Chaincode Labs, co-founder [of Revault and Liana](https://wizardsardine.com/), and Pythcoiner.

In this tutorial, I'll show you how to use this tool, so you can do without Ledger Live software for good, and still enjoy Ledger devices. It works on all devices: Nano S Classic, Nano S Plus, Nano X, Flex and Stax.

---
*Please note that this tool is fairly new, and its developers specify that it is still **in the testing phase**. They recommend using it for test purposes only, and not for a device intended to host a real Bitcoin wallet, although it is possible to do so. In this regard, I recommend that you follow the recommendations of the developers of this tool, which are specified [on the README of their GitHub repository](https://github.com/darosior/ledger_installer).*

---
## Prerequisites

On your computer, you will need two tools to use Bacca:


- Git ;
- Rust.

If you've already installed them, you can skip this step.

**Linux:**

On a Linux distribution, Git is generally preinstalled. To check whether Git is installed on your system, you can type the following command in the terminal :

```bash
git --version
```

If you don't have Git installed on your system, here's the command to install it on a Debian :

```bash
sudo apt install git
```

Finally, to install your Rust development environment, use the command :

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

**Windows:**

To install Git, go to [the project's official website](https://git-scm.com/). Download the software and follow the installation instructions.

![BACCA](assets/fr/01.webp)

Proceed in the same way to install Rust from [the official website](https://www.rust-lang.org/tools/install).

![BACCA](assets/fr/02.webp)

**MacOS:**

If Git is not already installed on your system, open a terminal and run the following command to install it:

```bash
git --version
```

If Git is not installed on your system, a window will open offering you to install Xcode, which includes Git. Simply follow the on-screen instructions to proceed with the installation.

To install Rust, run the following command:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## Bacca installation

Open a terminal and go to the folder where you want to save the software, then run the following command:

```bash
git clone https://github.com/darosior/ledger_installer.git
```

Navigate to the software directory:

```bash
cd ledger_installer
```

Then use Cargo to compile the project and run the Bacca GUI:

```bash
cargo run -p ledger_manager_gui
```

You now have access to the software interface.

![BACCA](assets/fr/03.webp)

## Configuring the Ledger

Before you start, if your Ledger is new, make sure you have set up the PIN code and saved the recovery phrase. You don't need Ledger Live for these initial steps. Simply connect your Ledger via the USB cable to power it. If you're not sure how to proceed with these two steps, you can refer to the beginning of the tutorial specific to your model:

https://planb.network/tutorials/wallet/hardware/ledger-c6fc7d82-91e7-4c74-bad7-cbff7fea7a88

https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a

## Using Bacca

Connect your Ledger to your computer and unlock it using the PIN code you have set. Bacca should automatically detect your Ledger.

![BACCA](assets/fr/04.webp)

To confirm the authenticity of your Ledger, click on the "*Check*" button. You will need to authorize the connection on your Ledger device to continue.

![BACCA](assets/fr/05.webp)

Bacca will then inform you if your Ledger is genuine. If it isn't, this indicates either that the device has been compromised, or that it's a counterfeit. In this case, stop using it immediately.

![BACCA](assets/fr/06.webp)

In the "*Apps*" menu, you can consult the list of applications already installed on your Ledger.

![BACCA](assets/fr/07.webp)

To install the Bitcoin application, click on "*Install*", then authorize installation on your Ledger.

![BACCA](assets/fr/08.webp)

The application is well installed.

![BACCA](assets/fr/09.webp)

If you don't have the latest version of the Bitcoin application installed, Bacca will display an "*Update*" button instead of the "*Latest*" indication. Simply click on this button to update the application.

![BACCA](assets/fr/10.webp)

Now that your Ledger is correctly configured with the latest version of the Bitcoin application, you're ready to import and use your wallet on management software such as Sparrow or Liana, without having to go through Ledger Live!

If you found this tutorial useful, I'd be grateful if you'd leave a green thumb below. Feel free to share this article on your social networks. Thank you very much!

I also recommend you take a look at this tutorial on GnuPG, which explains how to check the integrity and authenticity of your software before installing it. This is an important practice, especially when installing portfolio management software such as Liana or Sparrow :

https://planb.network/tutorials/others/general/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

