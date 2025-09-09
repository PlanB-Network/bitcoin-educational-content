---
name: Aegis Authenticator
description: How can you use Aegis Authenticator to secure your accounts with dual authentication?
---

![cover](assets/cover.webp)


Today, two-factor authentication (2FA) is essential for securing online accounts. In addition to the password, it adds a second factor (often a 6-digit code) that expires after 30 seconds, making it considerably more difficult for hackers. Using a dedicated TOTP (*Time-based One-Time Password*) application is safer than SMS, which can be hijacked by SIM swapping attacks.


However, not all authentication applications are created equal. Many proprietary solutions (Google Authenticator, Authy, etc.) pose problems: they are proprietary and closed-source (impossible to audit their security), sometimes integrate advertising trackers, don't offer encrypted back-up of your codes, and can even prevent exporting your accounts to lock you into their ecosystem.


Aegis Authenticator, on the other hand, presents itself as a free and ethical alternative to these applications. Aegis is a free, secure, open-source application for managing your two-step verification tokens on Android. Its development focuses on essential features that other apps don't offer, including robust encryption of local data and the possibility of secure backups. All in all, Aegis offers a local, auditable dual authentication solution, ideal for anyone wishing to retain total control over their 2FA codes.


## Introducing Aegis Authenticator


Aegis Authenticator is an open-source 2FA application for Android, released under the GPL v3 license. It stands out for its "privacy by design" philosophy: the application works entirely offline and requires no connection to a remote service. As a result, your tokens remain stored locally on your device, in a secure safe to which you alone hold the key.


### Key features


**Encrypted vault:** all your OTP codes are stored in an AES-256 encrypted vault (GCM mode), protected by a user-defined master password. You can unlock this vault via password or biometric data (fingerprint, facial recognition) for added convenience. In the absence of a password, the data would be unencrypted - so we strongly recommend that you set one.


**Advanced organization:** Aegis keeps your many 2FA accounts well organized. You can sort your entries alphabetically or in the order of your choice, group them by category (e.g. Personal, Work, Social) for easy retrieval, and assign each entry a personalized icon. A search bar is included to instantly find a service or account by name.


**Encrypted local backups:** To ensure you never lose access to your accounts, Aegis offers automatic backups of your safe. These are encrypted (via a password) and can be saved in the location of your choice (internal storage, cloud folder, etc.). The application can also export your account database manually, in encrypted or unencrypted format as required. Importing accounts from other 2FA applications is just as easy (Aegis supports import from Authy, Google Authenticator, FreeOTP, andOTP, etc.).


**Security and privacy:** the application is completely offline by default. It requires no network permissions - which means it transmits no data to the outside world, and features no ad trackers or behavioral analysis modules. Aegis doesn't display ads, and doesn't require a user account: as soon as it's installed, it's up and running without registration. As its source code is public on GitHub, the community can audit it freely, guaranteeing the absence of malicious or hidden functionalities.


**Modern Interface:** Aegis adopts a neat Material Design, with dark theme support (including an AMOLED mode) and even an optional tile view to display your codes as grids. Interface is uncluttered, with no frills, and prevents screen capture of codes as a security measure.


## Installation


As Aegis Authenticator is open source, its developers favor privacy-friendly distribution channels. There are two main ways to install it:


### Via F-Droid (recommended)


The safest and easiest way is through F-Droid, the free alternative store. If F-Droid is not yet installed on your phone, start by downloading it from the official website [F-Droid.org](https://f-droid.org). Then :



- Open F-Droid and make sure you've updated your repositories to get the latest list of applications
- Search for "Aegis Authenticator" in F-Droid. The official application should appear (publisher: Beem Development)
- Start installation by pressing Install. As Aegis is one of the applications verified by F-Droid, you benefit from a reliable and secure download


Installing via F-Droid offers the advantage of receiving automatic application updates as soon as they are released. What's more, F-Droid guarantees that the application is free of unwanted proprietary components.


### Via GitHub (signed APK)


If you prefer to install the application without going through a store, you can download the official APK directly from the project's GitHub page. On the Aegis repository ([github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis)), go to the Releases section where stable versions are published.



- Download the latest APK version
- Before installing the APK, make sure you have authorized the installation of applications from unknown sources on your device (in Android Settings)
- The APK provided on GitHub is signed by the developer with the same key as on F-Droid


After manual installation, the application will function identically. Please note that updates will not be automatic: you'll need to check GitHub periodically for new versions.


### Google Play Store vs F-Droid


Aegis Authenticator is available on both the Google Play Store and F-Droid, giving you the choice of installation method:


**Google Play Store:**


- ✅ Automatic updates integrated into the Android system
- ✅ Simple, familiar installation
- ✅ Same signed APK as on other channels


**F-Droid (recommended) :**


- ✅ Free and open source store
- ✅ Reproducible and verifiable construction
- ✅ No Google service required
- ✅ Respect for the free software philosophy


The choice between these two options depends on your preferences regarding the Google ecosystem. If you prefer simplicity, the Play Store is ideal. If you want a more privacy-friendly approach, independent of Google services, F-Droid is the better choice.


## First configuration


When Aegis is launched for the first time, an initial configuration procedure is proposed to secure your 2FA code safe:


![Configuration initiale Aegis](assets/fr/01.webp)


*Initial Aegis configuration process: welcome screen, security choices, master password definition and finalization*


### Set a master password


Aegis will first ask you to choose a master password. This password will be used to encrypt all your authentication tokens stored in the vault. We strongly recommend that you set a strong, unique password that only you will know.


**⚠️ Warning:** don't forget this password - if you lose it, your encrypted 2FA codes will become inaccessible (there is no backdoor). Aegis will ask you to enter the password twice for confirmation.


### Enable biometric unlocking (optional)


If your Android device is equipped with a fingerprint reader or other biometric sensor, Aegis will prompt you to activate biometric unlocking. This option is optional but very practical: it lets you quickly unlock the application with your fingerprint or face, rather than typing the password each time.


Note that biometrics are an added convenience: your master password is still required if the biometrics are changed or the device is restarted.


### Discover application settings


Once you're inside the application (the main Interface is initially empty), familiarize yourself with the available configuration options. Access the settings via the drop-down menu at the top right of the screen (three vertical dots), then select "Settings".


![Interface principale et paramètres](assets/fr/02.webp)


*Interface main Aegis empty at start, access to parameters menu and overview of available options*


The Aegis settings menu groups together several important sections:



- Appearance**: Customize theme (light, dark, AMOLED), language and other visual settings
- Behavior**: Configure application behavior when interacting with the list of entries
- Icon packs**: manage and import icon packs to customize the look and feel of your accounts
- Security**: Settings for encryption, biometric unlocking, automatic locking and other security parameters
- Backups**: Configure automatic backups to a location of your choice
- Import & Export**: Import backups from other authentication applications and manually export your Aegis vault
- Audit log**: Detailed log of all significant events in the application


This clear organization lets you configure Aegis according to your preferences and security needs.


## Add a 2FA account


With Aegis configured, let's move on to the essentials: adding your two-factor accounts. The process is simple, and Aegis offers several methods for integrating your authentication codes.


### The three available addition methods


From the main Aegis Interface, press the **+** button at bottom right to access the add options. You have three options:



- Scan QR code**: Scan directly the QR code displayed by the web service
- Scan image**: Scan a QR code from an image saved on your device
- Enter manually**: Enter 2FA account information manually


### Practical example: configuring Bitwarden


Let's take the concrete example of 2FA activation on Bitwarden to illustrate the process:


![Exemple avec Bitwarden](assets/fr/04.webp)


*Example of 2FA activation on Bitwarden: Interface web with authentication options and Aegis recommendation*



- Logging in and accessing settings**: Log in to your Bitwarden account and access the settings, "Security" tab
- Providers section**: Go to the "Providers" section and click on "Manage" in the "Authenticator app" section


![Configuration 2FA avec QR code](assets/fr/05.webp)


*Complete process for adding an account: QR code displayed by the service, secret key visible and verification code entered*



- Scan QR code**: A popup window opens with the QR code and secret key
- In Aegis**: Use "Scan QR code" to capture information automatically
- Verification**: Enter the 6-digit code generated by Aegis in the "Verification code" field
- Activation**: Click on "Turn on" to finalize activation


### Add details manually


If you prefer or are unable to scan the QR code, use the "Enter manually" option. The form allows you to enter :


![Ajout d'un compte 2FA](assets/fr/03.webp)


*Process for adding a new 2FA account: empty Interface, add options, manual entry form and account successfully added*



- Name** : Service name (e.g. Bitwarden, GitHub...)
- Issuer** : The issuer (often identical to the name)
- Group**: Optional, to organize your accounts by category
- Note** : Personal remarks on this account
- Secret** : The secret key supplied by the service (masked by default)
- Advanced**: Advanced parameters (algorithm, period, number of digits)


Once the account has been added, it appears in your list with its current code and a time indicator showing the time remaining before renewal.


### Universal compatibility


Aegis is compatible with all services using the TOTP and HOTP standards, including virtually all sites offering 2FA: social networks, banks, password managers, crypto platforms, etc.


### Entrance organization


Once you've added several accounts, you'll appreciate Aegis' organizational tools:



- Custom sorting:** By default, accounts are listed in alphabetical order, but you can change the order manually
- Groups and categories:** Create groups to separate your personal accounts from your business accounts, or group them by type of service (banking, e-mail, social networks, etc.)
- Customized icons:** Aegis tries to automatically assign an appropriate icon if available, otherwise you can choose from many generic icons or import an image
- Quick search:** The search bar at the top lets you type a few letters to instantly filter out matching entries


By touching an entry, the OTP code is displayed in full size (if it was hidden) and you can copy it to the clipboard with a long press - handy for pasting it into the application you want to connect.


## Security and backups


With security at the heart of Aegis, it's important to understand how your 2FA codes are protected, and how to ensure their persistence in the event of a problem.


### Security architecture


**Robust encryption**: All your codes are stored in an encrypted safe using the **AES-256 algorithm in GCM mode**, combined with your master password. Key derivation is based on **scrypt**, offering enhanced protection against brute-force attacks.


**Secure unlocking** : The master password is required to decrypt your data. Biometrics (optional) uses the **Android Secure Keystore** and TEE (Trusted Execution Environment) to protect the encryption key.


**Minimal permissions**: Aegis operates offline by default, requiring only access to the camera (QR scan), biometrics and vibrator. No data is collected or shared.


### Backup options


Aegis offers several backup strategies to suit different security and convenience needs:


![Configuration des sauvegardes](assets/fr/06.webp)


*Interface complete with added account, backup alert, automatic backup settings and backup strategies*


**1. Automatic local backups**


- Configure a destination folder of your choice
- Customizable frequency (after each change, daily, etc.)
- Password-protected encrypted files (.aesvault)
- Compatible with synchronized folders (Nextcloud, Dropbox, etc.)


![Sélection du dossier de sauvegarde](assets/fr/07.webp)


*Backup folder selection process: file explorer, destination folder and access authorization*


**2. Android** cloud backups


- Optional integration with Android backup system
- Available only for encrypted safes (security preserved)
- Transparent backup with other Android data
- Automatic restore on device changeover


**3. Manual** exports


- Export on demand via **Settings > Import & Export**
- Choice of encrypted (recommended) or clear format
- Useful for migrations or occasional backups


### Good safety practices



- Keep several backup versions** to prevent corruption
- Regularly test** your backups by attempting a restore
- Store your service-provided recovery codes separately**
- Your master password** is still required even with cloud backups
- Secure your master password**: use a unique, strong password stored in a password manager
- Keep your application up to date** with the latest security patches
- Activate auto-lock** in settings to secure access to the application
- Disable screenshots** (default option) to prevent your codes from being intercepted
- Use biometrics sparingly**: prefer passwords for critical accesses


## Comparison with other applications


How does Aegis stack up against other popular authentication applications?


### Aegis vs Google Authenticator


**Aegis :**


- ✅ Open source and auditable
- ✅ Local encrypted backup
- ✅ Advanced organization (groups, icons, search)
- ✅ No data collection
- ❌ Android only


**Google Authenticator :**


- ✅ Available on Android and iOS
- ✅ Cloud synchronization (since 2023)
- ❌ Closed source code
- ❌ Limited functionality
- ❌ Potential Google data collection


### Aegis vs Authy


**Aegis :**


- ✅ Open source
- ✅ No account required
- ✅ Code export possible
- ✅ Total data control
- ❌ No native multi-device sync


**Authy :**


- ✅ Multi-device synchronization
- ✅ Available on Android and iOS
- ❌ Closed source code
- ❌ Requires a phone number
- ❌ Unable to export codes
- ❌ Desktop applications removed in March 2024


Aegis excels for Android users who value transparency, local security and complete control over their data. Alternatives like Authy are better suited if you absolutely need automatic multi-device synchronization.



## Conclusion


Aegis Authenticator is an excellent solution for those looking for a privacy-friendly, secure and transparent 2FA application. Its open-source approach, combined with robust encryption and a neat Interface, makes it a first-rate choice for securing your online accounts.


Although limited to Android and lacking native cloud synchronization, Aegis more than makes up for these limitations with its "privacy by design" philosophy and total data control. For users concerned about their digital privacy, Aegis offers a credible and powerful alternative to the market's dominant proprietary solutions.


The security of your online accounts doesn't have to depend on the goodwill of commercial companies. With Aegis, you keep control of your authentication codes, in a digital safe to which you alone hold the key.


## Resources


### Official websites


- Official website**: [getaegis.app](https://getaegis.app/) - Application presentation and download
- Source code**: [github.com/beemdevelopment/Aegis](https://github.com/beemdevelopment/Aegis) - Official GitHub repository
- F-Droid** : [f-droid.org/packages/com.beemdevelopment.aegis](https://f-droid.org/packages/com.beemdevelopment.aegis/) - Installation via the free store


### Technical documentation


- Vault documentation**: [Vault design](https://github.com/beemdevelopment/Aegis/blob/master/docs/vault.md) - Technical description of encryption and secure architecture
- Official FAQ**: [getaegis.app/#faq](https://getaegis.app/#faq) - Answers to frequently asked questions
- Project wiki**: [github.com/beemdevelopment/Aegis/wiki](https://github.com/beemdevelopment/Aegis/wiki) - Full user documentation