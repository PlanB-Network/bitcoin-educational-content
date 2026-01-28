---
name: DietPi
description: Lightweight operating system optimized for underperforming machines. With a preference for self-hosting
---

![cover](assets/cover.webp)


In non-technical circles, brands such as `Odroid`, `Raspberry Pi`, `Orange Pi` or `Radxa`, are little known. But one only has to look out into tech circles, to find that **SBC** computers--built on a single motherboard, often microscopic in size compared to commonly used computers--become indispensable, as support for any personal project.


These are computers produced in a wide variety of models. They preferably host Linux distributions, often adapted to run smoothly on these underpowered machines.


**DietPi is no exception**: it is a Debian-based operating system, optimized to be as light as possible and make even the least performing `SBC` very fast. Switched from Debian12 Bookworm to Debian13 Trixie just as this tutorial was being written, it now also supports open source `RISC-V` processor-based SBCs. DietPi is a pleasant discovery that deserves further study.


## Strengths


This is not the "usual duplicate" of Debian for small Raspberry-type boards. DietPi is:


- Optimized for speed and lightness**: a [comparison with other Debian distributions for SBC](https://dietpi.com/blog/?p=888), DietPi is lighter in everything. The DietPi ISO image weighs less than 1 GB, by far the smallest among those dedicated to older models of Raspberry or Orange PI (for example). The demand for RAM and CPU resources is very low, so that it always gets the best out of boards, even older ones.
- Built-in automations and installers**: A suite of dedicated commands helps users monitor system resources as well as automate tasks to install and launch programs, update versions, make backups, and check all logs.
- A strong, experimentation-oriented community**: [tutorials](https://dietpi.com/forum/c/community-tutorials/8) and projects from the DietPi community, are ideal for getting inspired by software you can install with one click, thanks to DietPi.


**Squeezing every bit out of your SBC has never been easier**.


## Automations for self-hosting

Want to experiment with your own server to run advanced networking solutions, or tools to evolve your Bitcoin expertise? DietPi may be the solution you've been looking for. Although many people know how to manage their own infrastructure and run perfectly configured and protected servers, DietPi is a suitable step for those who want to start from scratch.


Instead of manually performing all the complex tasks such a task requires, DietPi allows you to build them with a `wizard` and its own command line. Here you can experiment with your own personal cloud, _smart home_ device management, automated backups and crontab, as well as more advanced solutions.


![img](assets/en/01.webp)


## Installation


### Download


DietPi offers a countless set of ISO images, to burn the operating system to many different devices. Some are only supported: the ISO for Raspberry PI5 is still in testing, for example, but you can definitely find the one suitable for your board.


For this guide I chose to install it on a thin client, so the choice went to _PC/VM_ and then to _Native PC_. There are two ISO images for these devices, which differ in the generation of the bootloader. The machine used in the tutorial is quite old, so the choice went to the _BIOS/CSM_ version. If you have a newer machine, the correct version might be the `UEFI`.


![img](assets/en/02.webp)


You will land on the page that contains the `image of the installer`, the `sha256` and the `Signatures`.


![img](assets/en/03.webp)


Prepare a directory in the `home` of your daily computer, so you can download the necessary files, with `wget`.


![img](assets/en/04.webp)


The developer's public key required a minimum of research, but you can find it at this link: https://github.com/MichaIng.gpg.


![img](assets/en/05.webp)


Check the contents of the directory with `ls -la` and import the MichaIng key into your keyring, with `gpg --import`.


### Verification and flash


Finally, the part I recommend most: ascertain the authenticity of the operating system you have downloaded and are about to install on your SBC.


![img](assets/en/06.webp)


If you also got the `Good signature` result and the same Hash control with the sha256sum command, you can proceed to flash the ISO to a USB stick. Use apps like Whale Etcher to do this.


![img](assets/en/07.webp)


## DietPi Installation


![img](assets/en/09.webp)


Transfer the flash drive to the device that will host DietPi and begin the installation of the lime green operating system. In this exercise we are using a thin client with 16 GB of RAM, a 128 GB SSD for the operating system, and a second 1 TB data disk. The installation took less than 30 minutes, but if you will be using a Raspberry, for example, the resources may be less and take longer. You will be shown the progress during the installation.


![img](assets/en/08.webp)


Being designed for Raspberries and the like, the true nature of DietPi is the so-called `headless` installation, without a graphical environment and with native `shsh' access. In the guide instead you will see a graphical environment, LXDE to be precise.


During this step you will also be asked to decide which web browser you want to use by default, between Chromium and Firefox. Both work well; there are no particular contraindications to either, other than your personal preference.


Towards the end, the installer may ask you if you want to install any programs already, but here **I advise you not to pre-load anything**. You should know that after this step, you will be asked to change the default passwords of the two users, for security reasons. Most importantly you will be required to **set the `Global Software Password (GSP)`**, which will ensure access to the various software in a controlled manner. **If you download any software during OS installation, without the `GSP` set, they will remain virtually inaccessible**. You will have to uninstall and re-install them again after setting the `Global Software Password`: therefore, **don't put anything in so as to avoid double work**. (The inconvenience is probable, not 100% certain).


The installation ends with a request to activate DietPi-Survey, an automated data collection service used to support the development of the operating system. According to the website, data collection is activated when you download any of the software from the automation provided by DietPi, or when you upgrade to the next release. Everyone has the option to opt in (_Opt IN_) or opt out (_Opt OUT_).


![img](assets/en/23.webp)


Upon completion of the installation and subsequent reboot, DietPi shows up on the screen as you set it up. For the tutorial, as mentioned, I chose the `LXDE` graphical environment. On the desktop I found the shortcut to start `htop` and the open terminal.


![img](assets/en/10.webp)


### "Tools" from operating system


Forget most of the programs you use on your Linux distribution-DietPi is so optimized, you've left out quite a few. You'd basically have to install a lot of commands manually, but if you're just trying it out, resist the temptation and try putting DietPi's automations under test.


It is definitely the terminal that is the first useful tool for getting started with your new operating system, and it opens automatically each time you turn it on.


![img](assets/en/11.webp)


On the terminal screen, you will find listed a series of commands preceded by `dietpi-` representing the [tools](https://dietpi.com/docs/dietpi_tools/) of this operating system:


- `dietpi-launcher`: to access the operating system, file manager, etc
- `dietpi-Software`: which represents the tool with which you can install all the software already available in the suite
- `dietpi-config`: to access system configurations, even the most advanced ones.


![img](assets/en/14.webp)


### Backup


Backing up a server is a routine that the system administrator should anticipate from the first start-up.


With DietPi there is the `dietpi-Backup` command, which I recommend you explore to find the ideal solution: it allows you to set up a regular backup, incremental or not depending on the applications used, and all the options to customize the routine.


![img](assets/en/22.webp)


Select the destination of the backup, for example another disk, by starting `dietpi-Drive_Manager` to mount the destination drive and use it for this function.


## Configuration


Self-hosting is an advisable experience for everyone, whether curious or simply enthusiastic. However, pulling up and configuring a server involves some not inconsiderable technological challenges. This is where **the simplicity of DietPi** comes in, allowing you to configure a system tailored to your needs in a few simple steps.


![img](assets/en/24.webp)


Basic and advanced settings, all at your fingertips in the one interface available with the command:


```dietpi-config

sudo dietpi-config

```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```

sudo dietpi-software

```