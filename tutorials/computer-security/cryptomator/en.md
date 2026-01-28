---
name: Cryptomator
description: Encrypt your files in the cloud
---
![cover](assets/cover.webp)


___


*This tutorial is based on original content by Florian BURNEL published on [IT-Connect](https://www.it-connect.fr/). License [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Changes may have been made to the original text.*


___


## I. Presentation


In this tutorial, we'll use the Cryptomator application to encrypt data stored in the Cloud, whether on Microsoft OneDrive, Google Drive, Dropbox, Box or even iCloud.


Encrypting the data you store on online storage solutions like Drive is the best way to protect your files and your privacy. Thanks to encryption, you're the only one who can decrypt and read your data, even if it's stored on a server in the USA or another country around the world.


In this demonstration, a Windows 11 22H2 machine with OneDrive will be used, but the procedure is identical on other versions of Windows and other storage services. All you need to do is install the synchronization client and add your account. This will enable Cryptomator to store its data in the vault.


![Image](assets/fr/020.webp)


Cryptomator is an alternative to other applications, notably Picocrypt presented in another article, which looks different, but is equally simple to use. Cryptomator is also **open source**, RGPD compliant, and will **encrypt data with the AES-256 bit encryption algorithm**. In contrast, Picocrypt relies on the faster XChaCha20 algorithm (also 256-bit).


https://planb.academy/tutorials/computer-security/data/picocrypt-98c213bd-9ace-425b-b012-bea71ce6b38f

The Cryptomator application is available on **Windows** (exe / msi), **Linux**, **macOS,** but also **Android** and **iOS**. By the way, all applications are free of charge, except for the Android application, which you have to pay for (14.99 euros).


On your machine, **Cryptomator will create a folder within which it will create a safe**. Within the vault, which may be stored on your OneDrive, Google Drive or similar, your data will be encrypted. So, if you store all your data in the safe hosted on your Drive storage space, it will be protected (because it's encrypted).


**Note**: in this article, online storage services are used as an example, but Cryptomator can be used to encrypt data on a local disk, an external disk or even a NAS. There are no restrictions, in fact.


## II. Installing Cryptomator


To get started, you need to **download** and **install** **Cryptomator**. Once the download is complete, a few clicks are all it takes to complete the installation. Like [Rclone](https://www.it-connect.fr/rclone-un-outil-gratuit-pour-synchroniser-vos-donnees-dans-le-cloud/), Cryptomator will rely on WinFsp to **mount a virtual drive on your Windows machine**.



- [Download Cryptomator from the official website](https://cryptomator.org/downloads/)


![Image](assets/fr/025.webp)


## III. Using Cryptomator on Windows


### A. Create a new safe


To create a new safe, click on the "**Add**" button and select "**New safe...**". Your existing and known safes on this machine will then appear in Interface, on the left. **A safe created on machine A can be opened and modified on machine B**, provided it is equipped with Cryptomator (and the encryption key is known).


![Image](assets/fr/015.webp)


Start by giving the vault a name, e.g. "**IT-Connect**". This will create a directory named "**IT-Connect**" in my OneDrive.


![Image](assets/fr/011.webp)


In the next step, Cryptomator is likely to **detect the "Drive "** present on your machine: Google Drive, OneDrive, Dropbox, etc.... To enable you to select the provider directly. I tried this on two different Windows 11 machines, with several Drives, and it wasn't detected. It's not a problem, just define a "**Custom location**" and select the root of your storage space. For example: **C:\Users\<Username>\OneDrive**.


![Image](assets/fr/018.webp)


Next, you can adjust an option under expert settings.


![Image](assets/fr/021.webp)


Next, you need to define **a password corresponding to the encryption key**. This password will enable you to **unlock your Cryptomator safe** and access its data. **If you lose it, you lose access to your data**. Finally, you still have the option of **creating a backup key** by checking the "**Yes, better safe than sorry**" option, much in the same spirit as the [BitLocker] recovery key (https://www.it-connect.fr/comment-activer-bitlocker-sur-windows-11-pour-chiffrer-son-disque/). This is advisable, but don't store this backup key at the root of your OneDrive!


Click on "**Create a safe**".


![Image](assets/fr/019.webp)


Copy the recovery key and store it in your favorite password manager. Click on "**Next**".


![Image](assets/fr/013.webp)


That's it, your new trunk is created and ready to use!


![Image](assets/fr/014.webp)


### B. Access figures


To access a safe and its data, either to **read existing data or add new data**, you need to **unlock** it. Cryptomator lists known safes: the IT-Connect safe appears, so simply select it and click on "**Unlock**".


![Image](assets/fr/016.webp)


You must enter your password to unlock the safe. Then click on "**Release drive**".


![Image](assets/fr/022.webp)


**Your safe is mounted on the Windows machine as a virtual drive.** This drive, which here inherits the letter E, gives you access to your data (in plain text, as the safe is unlocked).


![Image](assets/fr/017.webp)


On the OneDrive side, we can't browse the Cryptomator vault directly. We can't see the data (neither the file names nor the contents). This means you don't need to add data to your Cryptomator vault via the usual OneDrive shortcut. **You must add your data using Cryptomator's virtual drive.**


![Image](assets/fr/012.webp)


### C. Trunk options


The safe's settings are accessed via the "**Encrypted volume options**" button (when locked) and will enable automatic locking in the event of inactivity, just as you can do with your password safe. The "**Unlock encrypted volume on startup**" option, as its name suggests, unlocks the drive without any intervention on your part, and mounts the virtual drive. For security reasons, it is best to avoid activating this option.


Via the "**Mounting**" tab you can also decide to mount it read-only or assign a specific letter.


![Image](assets/fr/024.webp)


In addition, in the Cryptomator settings, you can **enable automatic application startup**.


## IV. Conclusion


With **Cryptomator**, you can **create an encrypted safe** in just a few minutes to protect the data you wish to store on OneDrive and consorts. It's very easy to use when it comes to "pairing" it with a Drive: for this purpose, it has my preference over Picocrypt.