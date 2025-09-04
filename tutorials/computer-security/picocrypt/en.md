---
name: Picocrypt
description: An open source tool to encrypt your data
---
![cover](assets/cover.webp)


___


*This tutorial is based on original content by Florian BURNEL published on [IT-Connect](https://www.it-connect.fr/). License [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Changes have been made to the original content.*


___


## I. Presentation


In this tutorial, we'll be taking a look at Picocrypt, a simple, lightweight and effective encryption software for encrypting data with a high level of security.


Suitable for **encrypting files**, you can use it to protect **data on your computer, on a USB stick**, but also data stored in the Cloud. For example, you can encrypt data and store it on **Microsoft OneDrive, Google Drive, iCloud or Dropbox**, although for this purpose I prefer another piece of software that will be presented in a future article.


You can also use it when you need to **share data with a third party**: thanks to Picocrypt and the decryption key, they'll be able to decrypt the data on their machine. So if your account or computer is compromised, your data is protected.


To follow the Picocrypt project, there is only one address:



- [Picocrypt on GitHub](https://github.com/Picocrypt/Picocrypt)


Totally **free and open source**, PicoCrypt is available for **Windows,** **Linux** and **macOS**. On Windows, you can install it on your own machine or use the portable version.


## II. Picocrypt, open source encryption software


Picocrypt** encryption software presents itself as **an alternative** to other well-known solutions such as **VeraCrypt** and **Cryptomator** (*designed to encrypt data on Cloud environments*), or **AxCrypt**. By the way, on Picocrypt's official GitHub, you can find a comparison with some competitors:


|                | Picocrypt                                                                          | VeraCrypt   | 7-Zip GUI | BitLocker  | Cryptomator |
| -------------- | ---------------------------------------------------------------------------------- | ----------- | --------- | ---------- | ----------- |
| Free           | ✅ Yes                                                                              | ✅ Yes       | ✅ Yes     | ✅ Bundled  | ✅ Yes       |
| Open Source    | ✅ GPLv3                                                                            | ✅ Multi     | ✅ LGPL    | ❌ No       | ✅ GPLv3     |
| Cross-Platform | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ❌ No       | ✅ Yes       |
| Size           | ✅ 3 MiB                                                                            | ❌ 20 MiB    | ✅ 2 MiB   | ✅ N/A      | ❌ 50 MiB    |
| Portable       | ✅ Yes                                                                              | ✅ Yes       | ❌ No      | ✅ Yes      | ❌ No        |
| Permissions    | ✅ None                                                                             | ❌ Admin     | ❌ Admin   | ❌ Admin    | ❌ Admin     |
| Ease-Of-Use    | ✅ Easy                                                                             | ❌ Hard      | ✅ Easy    | ✅ Easy     | 🟧 Medium   |
| Cipher         | ✅ XChaCha20                                                                        | ✅ AES-256   | ✅ AES-256 | 🟧 AES-128 | ✅ AES-256   |
| Key Derivation | ✅ Argon2                                                                           | 🟧 PBKDF2   | ❌ SHA-256 | ❓ Unknown  | ✅ Scrypt    |
| Data Integrity | ✅ Always                                                                           | ❌ No        | ❌ No      | ❓ Unknown  | ✅ Always    |
| Deniability    | ✅ Supported                                                                        | ✅ Supported | ❌ No      | ❌ No       | ❌ No        |
| Reed-Solomon   | ✅ Yes                                                                              | ❌ No        | ❌ No      | ❌ No       | ❌ No        |
| Compression    | ✅ Yes                                                                              | ❌ No        | ✅ Yes     | ✅ Yes      | ❌ No        |
| Telemetry      | ✅ None                                                                             | ✅ None      | ✅ None    | ❓ Unknown  | ✅ None      |
| Audited        | ✅ [Yes](https://github.com/Picocrypt/storage/blob/main/Picocrypt.Audit.Report.pdf) | ✅ Yes       | ❌ No      | ❓ Unknown  | ✅ Yes       |

Source: [Github.com](https://github.com/Picocrypt/Picocrypt)


Picocrypt is **very lightweight**, weighing in at just **3 MB**, and doesn't need to be installed: it's a **portable application** with the advantage of not requiring administrator rights! However, it does not neglect security, since it relies on **robust and reliable algorithms**:



- XChaCha20** encryption algorithm
- Key bypass function **Argon2**


Over and above the advantages just mentioned, what really appeals is **its ease of use**!


It only needs one thing: **a code audit**, but that's planned, as you can see from the comparison table above (last line). But since it's open source, there's nothing to stop you taking a look at its source code.


Even though it's compared to BitLocker in the table above, **in my opinion BitLocker and Picocrypt are intended for different uses**: BitLocker for encrypting a complete volume (that of Windows, for example) and Picocrypt for encrypting a tree structure or "Drive"-type storage space.


## III. Using Picocrypt


For this demonstration, a Windows 11 machine will be used.


### A. Encrypting data with Picocrypt


First of all, you need to download Picocrypt.exe from the official GitHub ([see this page](https://github.com/Picocrypt/Picocrypt/releases)).


Open the application to display its minimalist Interface on the screen. To encrypt data, be it **a file, several files or a folder**, simply **drag and drop it into Picocrypt's Interface**. This will select the data to be encrypted.


![Image](assets/fr/020.webp)


Then, for data encryption, you have access to several options, including the encryption key. It can be **a strong password** or **an encryption key in the form of a key file**, or **both**. If we take the example of a password, you have the choice between creating your own password, or generating a password with Picocrypt.


This password must be strong, as it can be used to decrypt the data. Enter it under "**Password**" and "**Confirm Password**", then click on "**Encrypt**" to encrypt the data! Before that, you can click on the "**Change**" button next to "**Save output as**" to specify the output directory.


**Note**: to use a key in file format, click on "**Create**" to the right of "**Keyfiles**" to create a key. Then select it by clicking on "**Edit**" and dragging and dropping the key file onto the appropriate area.


![Image](assets/fr/019.webp)


The two selected files are **encrypted and grouped together** in the file "**Encrypted.zip.pcv**", since **PCV** is the extension used by Picocrypt. This ZIP file is unreadable thanks to encryption. To prevent selected files from being grouped together in a single encrypted ZIP file, you need to check the "**Recursively**" option, so that there are as many encrypted files as there are files to be encrypted.


To access our data, we need to decrypt it using Picocrypt.


![Image](assets/fr/023.webp)


Before we talk about data decryption, here's some information about some of the options available:



- Paranoid mode**: use the highest security level offered by Picocrypt. The tool will use several cascading encryption algorithms (XChaCha20 and Serpent) and HMAC-SHA3 instead of BLAKE2b for data authentication.
- Reed-Solomon**: implement *Reed-Solomon* error correction codes to facilitate error correction on corrupted data. This allows you to support a corruption level of around 3% of your file.
- Split into chunks** or **divide into several parts**: if you're encrypting a large file, you can ask Picocrypt to split it into several parts. This may make the file easier to transfer.
- Compress Files** or **Compress files**: compress files to reduce the size of encrypted files.
- Deleted files** or **Fichiers supprimés**: delete source files to keep only the encrypted version


### B. Decrypting data with Picocrypt


If you need to decrypt the data, it's no more complicated than encrypting it. Simply open Picocrypt and **drag and drop the PCV file to be decrypted**. Then enter the password and/or select the key file before clicking on "**Decrypt**".


![Image](assets/fr/021.webp)


The unencrypted version of the "Encrypted.zip" ZIP archive now allows me to recover my two files in clear text!


![Image](assets/fr/022.webp)


## IV. Conclusion


**You've been warned: Picocrypt is very easy to use, and it works! Although the Interface is minimalist, it incorporates some very useful options for customizing encryption! And since it's available in a portable version, you can take it with you wherever you go, so you can decrypt your data with confidence**


Be sure to use strong passwords to protect data, and if you use a key file, you must remember to back it up, otherwise you'll no longer be able to decrypt the PCV container generated by Picocrypt. Finally, you should know that there is also [a CLI version](https://github.com/Picocrypt/CLI) (with fewer features) that lets you run Picocrypt from the command line: here again, Picocrypt opens the door to new possibilities.


https://planb.network/tutorials/computer-security/data/veracrypt-d5ed4c83-7c1c-4181-95ea-963fdf2d83c5