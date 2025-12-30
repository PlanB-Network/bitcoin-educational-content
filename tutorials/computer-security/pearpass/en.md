---
name: PearPass
description: Regain control of your passwords with a local, peer-to-peer, cloud-free password manager
---

![cover](assets/cover.webp)


At a time when every individual manages dozens, even hundreds of online accounts, the security of logins has become a central issue in IT security. Social networks, messaging systems, professional services, financial platforms: each of these accesses relies on a secret, the compromise of which can have serious consequences for your life.


And yet, despite the growing number of attacks, bad practices remain widespread among the population: weak passwords, reused passwords, passwords stored in clear text or approximately memorized passwords. To solve these problems without making life more complicated on a daily basis, the solution is to use a password manager.


Dozens of password managers already exist, and Plan ₿ Academy offers a tutorial for most of them. But in this tutorial, I'd like to introduce you to one that clearly stands out from the rest in terms of how it works: **PearPass**.


**PearPass is an open-source, local-first, peer-to-peer password manager designed to give users total control over their data


![Image](assets/fr/01.webp)


## Why choose PearPass?


A password manager is a software program that generates, stores and organizes all your passwords in a secure manner. Rather than memorizing or reusing passwords, you have just one secret to protect: the master password, which encrypts your entire safe. This approach makes it possible to use unique, long, random passwords for each service, reducing both the risk of forgetting and compromise, while limiting the impact of any possible leak. Today, it's a basic IT tool that everyone should be using.


There are two main categories of password manager. On the one hand, there's local-only software, which is very secure since data is never stored on a central server, but not very practical, since it doesn't allow you to easily synchronize your credentials between several devices (computer, smartphone, tablet...). On the other hand, cloud-based password managers store your credentials on their servers and synchronize them across all your devices. Their main advantage is convenience, but they involve a compromise on security, since your passwords are stored on infrastructures you have no control over.


PearPass deliberately breaks with both models. It positions itself between local managers and cloud solutions: it enables synchronization of your passwords, while guaranteeing that they are never stored on remote servers. As a result, all your credentials are stored locally on your devices, and synchronization between multiple machines is exclusively peer-to-peer. This architecture eliminates the single points of failure associated with centralized databases: there are no servers to compromise, and no third-party infrastructure to access your credentials. Communications between your devices are end-to-end encrypted, ensuring that only the keys you hold allow access to data.


![Image](assets/fr/02.webp)


To make this possible, as its name suggests, PearPass relies on **Pears**, a peer-to-peer technology ecosystem dedicated to the creation and execution of serverless applications. Pears provides the execution environment, distribution mechanisms and network layers needed to run fully decentralized applications, capable of synchronizing directly between peers, without any central infrastructure. In the case of PearPass, Pears provides device discovery, encrypted connection establishment and password vault synchronization between your machines. This approach ensures that PearPass remains functional, resilient and independent of any external authority.


https://planb.academy/tutorials/computer-security/communication/pears-6d42b312-c69f-4504-8f71-b03b56c42fdd

Beyond this innovative architecture, PearPass is entirely open-source, and all its functions are free of charge. The software has also been independently audited by Secfault Security. In addition to its specific architecture, PearPass of course offers all the classic features expected of a good password manager, which we'll discover throughout this tutorial.


In short, where traditional password managers ask you to trust a company and its servers, PearPass adopts a logic of sovereignty: no cloud, no centralized accounts, no intermediaries. You retain exclusive control over your credentials, while benefiting from synchronization between your devices.


## How do I install PearPass?


PearPass is available on all platforms: Windows, Linux, macOS, Android, iOS and browser extensions. There's no need to install Pears on your machine: PearPass works on its own.


### Installation on Windows


On Windows, PearPass is supplied as a classic installer. Go to [the official download page](https://pass.pears.com/download), then click on the `Download Windows installer` button.


Once the file has been downloaded, open the installer and follow the steps indicated by the wizard. The application can then be accessed from the `Start Menu` or via a desktop shortcut.


![Image](assets/fr/03.webp)


### Installation on macOS


On macOS, PearPass is distributed as a disk image (`.dmg`). Go to [the official download page](https://pass.pears.com/download) and choose the version corresponding to your Mac's architecture (Intel or Apple Silicon). After downloading, open the `.dmg` file and launch the application from the `Applications` folder.


On first startup, macOS will display a security message indicating that the application has come from the Internet: simply confirm to continue.


### Installation on Linux


On Linux, PearPass is available in `.AppImage` format, which guarantees broad compatibility with most distributions without any specific dependencies. Download the `.AppImage` file from [the official download page](https://pass.pears.com/download), then launch it directly by double-clicking.


Depending on your environment, you may need to make the file executable via file properties (right-click) or with the `chmod +x` command. Once authorized, PearPass launches as a stand-alone application.


### Browser extension installation


PearPass offers a browser extension for automatic login and fast access to your safe while browsing the web. The extension is currently available for Google Chrome and compatible browsers. To install it, go to [the official download page](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).


![Image](assets/fr/04.webp)


Once added, you can pin it to the toolbar for quick access. Activating the extension then requires a link with the PearPass application installed locally on your computer (we'll come back to this later in the tutorial).


### Installation on iOS and Android


On iPhone and Android, simply download the application from your app store:


- [Google Play Store](https://play.google.com/store/apps/details?id=com.pears.pass);
- [App Store](https://apps.apple.com/us/app/pearpass/id6752954830).


![Image](assets/fr/05.webp)


In addition to these classic installation methods, it is also possible to download the software directly from GitHub repositories, for each :


- [Desktop](https://github.com/tetherto/pearpass-app-desktop);
- [Mobile](https://github.com/tetherto/pearpass-app-mobile);
- [Browser extension](https://github.com/tetherto/pearpass-app-browser-extension).


Once PearPass has been installed on one or more platforms, you can move on to the initial configuration. In this tutorial, we'll start by configuring the software on the desktop, then synchronize it with the browser extension and the mobile application.


## How do I create a PearPass safe?


When you first launch PearPass on your computer, the application guides you through two steps: setting your master password, and then creating your first safe.


### Set master password


When the application is first started up on the desktop, click on the `Skip` button and then `Continue` to go through the introduction screen and reach the master password configuration stage.


![Image](assets/fr/06.webp)


Next comes the important step of choosing your master password. As we saw in the introduction, this password is very important, as it gives you access to all your other passwords saved on the manager. Technically, it is used to derive the cryptographic keys used to encrypt your data.


The master password carries two main risks: loss and compromise. If you lose access to this password, you will no longer be able to access your login details. PearPass never keeps your master password: **If it's lost, your login details are permanently lost**. There is no recovery mechanism. Conversely, if this password is compromised and an attacker gains access to one of your devices, he or she will be able to access all your accounts.


To limit the risk of loss, you can make a physical backup of your master password, for example on paper, and keep it in a secure place. Ideally, seal this backup in an envelope so that you can periodically check that it has not been accessed. On the other hand, never make a digital backup of this password.


To reduce the risk of compromise, your master password must be strong. It should be as long as possible, include a wide variety of characters and be chosen in a truly random way. In 2025, minimum recommendations call for at least 13 characters including upper and lower case letters, numbers and symbols, provided the password is random. However, I would recommend a password of at least 20 characters, if not more, with all types of characters, to ensure a more lasting level of security.


Enter your master password in the field provided, confirm it a second time, then click on the `Continue` button.


![Image](assets/fr/07.webp)


You will then be redirected to the login screen: enter your master password to check that everything is working correctly.


![Image](assets/fr/08.webp)


### Create your first safe


Once you've logged in, PearPass will prompt you to create your first safe. A safe is an encrypted container in which your passwords, IDs, secure notes and other information are stored. Each safe is isolated and can be identified by a distinct name, allowing you to organize your data according to your uses (personal, professional, specific projects...).


Click on the `Create a new vault` button.


![Image](assets/fr/09.webp)


Choose a name for this vault, then click `Create a new vault` again to finalize creation.


![Image](assets/fr/10.webp)


Your safe is immediately ready for use. You can start adding passwords, logins or secure notes right away.


![Image](assets/fr/11.webp)


## How do I add a login to PearPass?


Once you've created your safe, you can start saving your items in it. PearPass supports the registration of many types of items:


- login to a site or service ;
- identity: your personal information to quickly fill in forms, but also to store identity documents directly in PearPass ;
- credit card: your credit card numbers for faster payment when shopping online;
- Wi-Fi: passwords for your Wi-Fi networks ;
- PassPhrase: secret phrase composed of several words (warning: I strongly advise against using it for wallet Bitcoin mnemonic phrases);
- note: creating secure notes ;
- custom: this feature allows you to create a custom element type, adapted to your specific needs.


Start by opening PearPass and logging in with your master password.


![Image](assets/fr/12.webp)


Select the safe in which you wish to save this identifier.


![Image](assets/fr/13.webp)


On the home page, click on the button to add a new item, depending on the type of information you wish to record. In my case, I want to add a login for my account on the Plan ₿ Academy website: so I click on the `Create a Login` button.


![Image](assets/fr/14.webp)


Once you've selected the type of item you wish to add, a form appears, allowing you to enter the information associated with the service in question. Depending on your needs, you can enter the service name, login, password and, if required, the website address and additional notes.


PearPass also features a password generator, allowing you to create a strong password directly from the form. To use it, click on the icon representing three small dots in the `Password` field, choose the desired length, then click on `Insert password`.


Once all the fields have been filled in, click on the `Save` button to save the identifier in the safe.


![Image](assets/fr/15.webp)


The identifier is now saved. It appears in the list of items in the selected safe, and can be viewed by clicking on it.


![Image](assets/fr/16.webp)


You can easily modify an element by clicking on it, then on the `Edit` button. You can also delete it by clicking on the three small dots at the top right of the interface, then on `Delete element`.


![Image](assets/fr/22.webp)


On mobile, the logic remains the same, although the interface has been adapted. After logging in, select the desired safe, tap on the `+` button, choose the type of item to be created, then fill in the necessary information.


![Image](assets/fr/17.webp)


## How to organize PearPass?


As we saw in the previous sections, PearPass lets you create several distinct vaults. This makes it possible to separate different uses and constitutes a first level of organization for your password manager. From the home page, you can easily switch from one vault to another by clicking on the arrow at the top left of the interface.


![Image](assets/fr/18.webp)


Another way of organizing your passwords, even within a vault, is to create folders. To do this, in the left-hand column of the interface, click on the `+` symbol next to `All Folders`, then enter the name of the folder you wish to create.


![Image](assets/fr/19.webp)


You can then store the identifiers of your choice, either directly when creating an item, or later by clicking on `Edit`. All you have to do is select the desired folder in the top left-hand corner of the form.


![Image](assets/fr/20.webp)


After opening an item, such as a login, you can click on the star icon at the top right of the interface to add it to your favorites. Favorites can be quickly found in a dedicated folder, in addition to their base folder.


![Image](assets/fr/21.webp)


Finally, there's a search bar at the top of the interface, so you can quickly find the item you're looking for, even if your vault contains many identifiers.


## How do I synchronize PearPass on my mobile?


Now that you have a working vault with items stored on your computer, you'll probably want to access your passwords from your smartphone or other device. PearPass allows you to synchronize your manager on multiple machines securely using Pears. Let's find out how.


To begin, on the source machine (your computer, for example), log in to your vault using your master password. Once on the home page, click on the `Add a Device` button, located at the bottom right of the interface.


![Image](assets/fr/23.webp)


PearPass then generates an invitation link, also available as a QR code, to synchronize the selected vault on the device of your choice.


![Image](assets/fr/24.webp)


If you'd like to synchronize on your mobile device, first install the application, then launch it. You will be asked to create a master password for your mobile manager. You can choose to use the same password as on your computer, or a different one. In all cases, follow the same recommendations: a strong, random password saved on a physical medium.


![Image](assets/fr/25.webp)


You can then activate biometric authentication if you wish, to avoid having to manually enter your master password every time you unlock your mobile.


![Image](assets/fr/26.webp)


Re-enter your master password, then click on the `Continue` button.


![Image](assets/fr/27.webp)


Select the `Load a vault` option, then click `Scan QR Code` and scan the invitation QR code displayed by PearPass on your source machine (the computer).


![Image](assets/fr/28.webp)


Your vaults on your computer and your mobile are now synchronized. Every ID added on one device will be securely stored and replicated on the other.


![Image](assets/fr/29.webp)


On cell phones, you can also activate automatic field filling. To do this, go to `Settings > Advanced`, then click on the `Set as Default` button in the `Autofill` section.


![Image](assets/fr/30.webp)


## How do I synchronize PearPass with the browser extension?


Having a password manager synchronized between your computer and your smartphone is already very practical, but integrating it directly into your browser is even more so. To do so, start by [adding the official PearPass extension to your browser](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).


![Image](assets/fr/31.webp)


From the PearPass software installed on your local machine, go to `Settings > Advanced`, then activate the `Activate browser extension` option.


![Image](assets/fr/32.webp)


PearPass generates a token pairing file. Copy it.


![Image](assets/fr/33.webp)


Then open the PearPass extension in your browser, paste in the token pairing, and click on the `Verify` button, followed by `Complete`.


![Image](assets/fr/34.webp)


Your password manager is now synchronized with the browser extension.


![Image](assets/fr/35.webp)


You can now use it to easily connect to your various web accounts.


![Image](assets/fr/36.webp)


Now you know how to use the PearPass password manager. Beyond this tool, day-to-day digital security depends on the correct use of appropriate solutions. If you'd like to learn how to set up a secure, stable and efficient personal digital environment, I invite you to discover our training course dedicated to this subject:


https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1