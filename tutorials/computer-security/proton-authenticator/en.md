---
name: Proton Authenticator
description: How can I use Proton Authenticator to secure my accounts with 2FA?
---
![cover](assets/cover.webp)


Two-factor authentication (2FA) adds an extra security barrier to your accounts by requiring, in addition to your password, additional proof that only you have it. Enabling 2FA drastically reduces the risk of hacking, even if your password is compromised through phishing or a data leak. Without 2FA, an attacker would only need your password to access your accounts; with 2FA, he would also need your second factor, thwarting most account theft attempts.


Various types of 2FA exist. SMS codes are better than nothing, but remain vulnerable to SIM swapping attacks and interception. We do not recommend SMS as a primary 2FA. Authentication applications (TOTP) generate temporary codes locally on your device, making them much harder to intercept. Physical security keys offer the best security, but require dedicated hardware.


Proton Authenticator is a TOTP authenticator. It's Proton's response to the limitations of existing applications: many are proprietary, contain ad trackers and don't offer encrypted backup. Proton Authenticator sets itself apart by providing an open source application, free of ads and trackers, with end-to-end encrypted backup.


## Introducing Proton Authenticator


Proton Authenticator is a mobile and desktop TOTP authentication application developed by Proton, renowned for its privacy-focused services. Like all Proton products, the application is open source and has undergone independent security audits. It is available free of charge on all platforms (Android, iOS, Windows, macOS, Linux).


Proton Authenticator offers the following key features:



- Generation of TOTP** codes for your 2FA accounts, compatible with most sites using Google Authenticator, Authy, etc.



- Optional encrypted cloud backup**: you can link the application to your Proton account to back up and synchronize your codes with end-to-end encryption. If you lose your device, simply reconnect a new one to restore all your codes.



- Multi-device synchronization**: by logging into Proton in the app, your 2FA codes automatically synchronize between multiple devices via end-to-end encryption. On iOS, an alternative is synchronization via iCloud.



- Local locking by password or biometrics**: the application offers PIN and/or fingerprint/Face ID locking. So even if someone physically accesses your unlocked phone, they won't be able to open Proton Authenticator.



- No data collection or trackers**: Proton is committed to collecting no personal data via the application. There is no hidden advertising or behavioral analysis.



- Easy import/export**: one of Proton Authenticator's strong points is its import wizard for existing accounts, compatible with other applications (Google Authenticator, Authy, Aegis, etc.). You can also export your codes to a file if required.


In short, Proton Authenticator aims to be an uncompromising 2FA solution: secure, private, flexible.


## Installation


Proton Authenticator is available free of charge on all platforms. To download the application, go to the official page: [https://proton.me/fr/authenticator/download](https://proton.me/fr/authenticator/download)


![PROTON AUTHENTICATOR](assets/fr/01.webp)


*Official Proton Authenticator page showing the application's main features and Interface*


On this page, you'll find download links for all operating systems: Android, iOS, Windows, macOS and Linux. Simply click on the operating system of your choice and follow the standard installation steps.


In this tutorial, we'll show you how to install and configure it on macOS, and then we'll look at how to install the app on iOS and synchronize your codes between the two devices.


### Installation on macOS


Once you've downloaded and installed the application, launch Proton Authenticator. On first launch, the application guides you through a few initial configuration screens:


![PROTON AUTHENTICATOR](assets/fr/02.webp)


*Proton Authenticator welcome screen with "Security in every code" message and "Get started "* button


### Initial import


If Proton Authenticator detects that you were previously using another 2FA application, an import wizard may appear. It supports direct import from certain applications (Google Authenticator, 2FAS, Authy, Aegis, etc.). Alternatively, you can skip this step and add your accounts manually later.


![PROTON AUTHENTICATOR](assets/fr/03.webp)


*Import wizard for transferring codes from other authentication applications*


![PROTON AUTHENTICATOR](assets/fr/04.webp)


*Compatible import applications: 2FAS, Aegis Authenticator, Authy, Bitwarden Authenticator, Ente Auth and Google Authenticator*


### Local application protection


Set an unlock PIN, or enable biometric unlocking (Touch ID) if available. This step is crucial to prevent anyone using your Mac from gaining free access to your 2FA codes.


![PROTON AUTHENTICATOR](assets/fr/05.webp)


*Touch ID configuration screen with "Protect your data" message and "Activate Touch ID "* button


### Synchronization options


The application also lets you activate iCloud synchronization to back up your data securely between your Apple devices.


![PROTON AUTHENTICATOR](assets/fr/06.webp)


*ICloud synchronization option with the message "Back up your data securely with encrypted iCloud synchronization "*


Once these steps have been completed, Proton Authenticator is ready for use.


![PROTON AUTHENTICATOR](assets/fr/07.webp)


*Interface main empty Proton Authenticator with "Create a new code" and "Import codes "* options


## Add a 2FA account with ProtonMail


We'll now look at how to add your first 2FA code, using ProtonMail as an example. This method works identically for all services that support two-factor authentication.


### Enable 2FA on ProtonMail


First of all, you can consult our guide to ProtonMail for more information:


https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2

Log in to your ProtonMail account and go to the security settings. Look for the "Two-factor authentication" option and activate it.


![PROTON AUTHENTICATOR](assets/fr/08.webp)


*ProtonMail settings page with the "Authenticator app" option in the "Two-factor authentication "* section


Click on the button to activate the authenticator and ProtonMail will prompt you to choose an authentication application.


![PROTON AUTHENTICATOR](assets/fr/09.webp)


*ProtonMail 2FA configuration window with "Cancel" and "Next "* buttons


ProtonMail will then display a QR code for you to scan with your authentication application.


![PROTON AUTHENTICATOR](assets/fr/10.webp)


*ProtonMail QR code to scan with your authentication application, with "Enter key manually instead" option available*


If you prefer to enter the key manually, click on "Enter key manually instead" to see the secret key.


![PROTON AUTHENTICATOR](assets/fr/11.webp)


*Manual entry of 2FA information: Key, Interval (30) and Digits (6)*


### Scan the QR code with Proton Authenticator


In Proton Authenticator on macOS, click on "Create a new code". The application offers you several options: **Scan a QR code** or **Enter the key manually**.


Use your Mac's camera to scan the QR code displayed on the ProtonMail screen. Once you've scanned the QR code, you'll be taken to the new code configuration screen.


![PROTON AUTHENTICATOR](assets/fr/12.webp)


*New entry creation window with Title (ProtonMail), Secret, Sender (Proton), digit parameters and interval fields*


Proton Authenticator will automatically fill in the information. You can customize the name if you wish, then click "Save".


![PROTON AUTHENTICATOR](assets/fr/13.webp)


*TOTP code generated for ProtonMail (848 812) with remaining time displayed*


### Validate configuration


ProtonMail will ask you to enter a 6-digit code generated by Proton Authenticator to confirm that the 2FA is working correctly.


![PROTON AUTHENTICATOR](assets/fr/14.webp)


*ProtonMail validation screen asking you to enter the 6-digit code (848812)*


Copy the code from the application (by clicking on it) and paste it into ProtonMail to complete the activation.


Once validated, ProtonMail will ask you to download your recovery codes. It's vital to save them carefully.


![PROTON AUTHENTICATOR](assets/fr/15.webp)


*ProtonMail recovery codes screen with list of rescue codes and "Download "* button


### Emergency codes


When adding an account, keep the recovery codes provided by the service. Most sites offer static, single-use recovery codes to store in a safe place. Keep these backup codes outside Proton Authenticator so that you can access your account if you lose access to the 2FA application.


## IOS installation and code import


Now that you've set up Proton Authenticator on macOS, you may also want to use it on your iPhone or iPad. Here's how to get your 2FA codes on multiple devices.


### Download the application on iOS


Go to the App Store and search for "Proton Authenticator". Download and install the application on your iOS device.


![PROTON AUTHENTICATOR](assets/fr/16.webp)


*Installation process on iOS: welcome screen, import wizard, selection of compatible applications, and final "Import codes from Proton Authenticator "* screen


### Method 1: Export/Import via JSON file


If you don't use automatic synchronization (iCloud or Proton account), you'll need to manually transfer your codes from your Mac to your iPhone:


**Step 1 - Export from macOS** :


On your Mac, open Proton Authenticator and go to Settings (gear icon). In the menu, click on "Export".


![PROTON AUTHENTICATOR](assets/fr/17.webp)


*Proton Authenticator settings menu on macOS with the "Export" option visible*


![PROTON AUTHENTICATOR](assets/fr/18.webp)


*Export window with file name "Proton_Authenticator_backup_2025" and "Save "* button


Save the JSON file on your Mac. You can send it by secure email or save it in iCloud Drive for access from your iPhone.


**Step 2 - Import on iOS** :


On your iPhone, install Proton Authenticator and during configuration, choose to import codes. Select "Proton Authenticator" from the list and import the JSON file.


![PROTON AUTHENTICATOR](assets/fr/19.webp)


*Import process on iOS: JSON file localization, import confirmation, and configuration screens with Face ID and iCloud options*


### Method 2: Automatic synchronization


**Via Proton account (for multi-platform synchronization)** :


If you haven't yet set up a Proton account and wish to synchronize between different operating systems, the application will prompt you to create or connect a Proton account.


![PROTON AUTHENTICATOR](assets/fr/20.webp)


*Device synchronization screen asking you to create a free Proton account or connect to an existing account*


**Via iCloud (for Apple ecosystem only)** :

If you only use Apple devices, you can choose iCloud synchronization in the application settings. This method will automatically and securely synchronize your codes between all your Apple devices, without the need for a Proton account.


## Encrypted backup and restore


One of Proton Authenticator's key features is its end-to-end back-up of 2FA codes, ensuring that a loss or change of device doesn't mean you have to start all over again.


### End-to-end encryption


When it comes to encrypted cloud backup with Proton Authenticator, your TOTP secrets are encrypted locally on your device before being sent to the Proton server. Decryption is only possible by you, on your devices connected to your Proton account. Proton AG does not have the key to read your registered codes.


On iOS, if you opt for iCloud rather than the Proton account, your data is encrypted to Apple standards. Local backup on Android lets you encrypt the backup file with a password of your choice.


### Restoration in case of loss


If your phone is lost, stolen or you change handset :


**With Proton backup enabled**: Install Proton Authenticator on the new device. During initial setup, log in to the same Proton account. Immediately, the application will synchronize and download all your 2FA codes from the encrypted backup.


**With iCloud backup (iOS)**: Connect the new iPhone/iPad with the same Apple ID and make sure to activate iCloud Keychain. After installing Proton Authenticator, connect to iCloud. Your codes should sync via iCloud and appear.


**No cloud backup**: You'll need to import your accounts manually. If you had exported a backup file, use the Import function in Proton Authenticator. In the worst-case scenario, if you had no backup, you'll need to use the backup codes for each service, or contact support.


Proton Authenticator lets you export your accounts at any time, either as an encrypted file or as a multi-account QR code. These options give you added assurance.


## Best practices


Using a 2FA authenticator greatly enhances your security, but certain best practices must be observed:


### Save your emergency codes


When you activate 2FA on a service, you are often given a list of recovery codes. Keep them off your phone (on paper, in an encrypted password manager, etc.). In the event of total loss of your authenticator, these static codes will save you.


### Don't mix up your passwords and 2FA codes


It's tempting to use a password manager that also stores TOTPs. However, keeping the password and 2FA code in the same place creates a single point of failure and weakens dual authentication. For maximum security, many experts recommend separating the two factors: passwords in a secure manager, and 2FA codes in a separate application such as Proton Authenticator. However, using an integrated manager is still better than having no 2FA at all.


### Activate several 2FA methods


Ideally, use more than one second factor on your critical accounts. Don't hesitate to add a physical security key if the service allows it. See our tutorial on Yubikey physical keys for more information:


https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Likewise, keep printed emergency codes on hand.


### Stay discreet and protect your device


Don't let anyone search your unlocked phone. With Proton Authenticator, your codes are protected by PIN/biometrics - don't divulge this PIN. Similarly, beware of phishing: even with 2FA, if you give a code to a fraudulent site in real time, it could be used by an attacker.


### Updates and audits


Keep Proton Authenticator up to date (updates correct possible flaws). As the code is open, the community carries out informal audits, and Proton publishes the results of formal audits.


## Comparison with other applications


How does Proton Authenticator stack up against other authentication applications? Here's a comparative summary:


**Proton Authenticator**: Open source, optional E2EE encrypted cloud backup, multi-device synchronization, local locking, no tracking, available on mobile and desktop.


**Google Authenticator**: Proprietary, backup via Google account since 2023 but without end-to-end encryption (keys can be seen by Google), multi-device synchronization added in 2023, no application lock by default, contains Google trackers.


**Aegis Authenticator**: Open source, local backup only, no cloud synchronization, code/biometric lock, no tracking, Android only.


**Authy**: Proprietary, password-encrypted cloud backup but closed code, multi-device synchronization, PIN lock/fingerprint, collects phone number, desktop application discontinued in March 2024.


You will find our guide to Authy below:


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

Proton Authenticator is one of the most comprehensive and secure solutions available: open source, multi-device encrypted synchronization, no commercial follow-up.


## Resources and support


### Official documentation


- Official website**: [proton.me/authenticator](https://proton.me/authenticator) - Product presentation and downloads
- Download page**: [proton.me/en/authenticator/download](https://proton.me/fr/authenticator/download) - Links for all OSes
- Proton support**: [proton.me/support/two-factor-authentication-2fa](https://proton.me/support/two-factor-authentication-2fa) - Official 2FA activation guide
- Proton blog**: [proton.me/blog/authenticator-app](https://proton.me/blog/authenticator-app) - Announcement and detailed features


### Source code and transparency


- GitHub Proton Authenticator** : [github.com/ProtonMail/proton-authenticator](https://github.com/ProtonMail/proton-authenticator) - Open source code
- Security audits**: [proton.me/community/security-audits](https://proton.me/community/security-audits) - Independent audit reports


### Recommended safety tests

After configuration, test your setup:


- [Have I Been Pwned](https://haveibeenpwned.com/) - Check if your accounts have been compromised
- [2FA Directory](https://2fa.directory/) - List of services supporting 2FA


### Communities and discussions


- Reddit r/Proton** : [reddit.com/r/ProtonMail](https://reddit.com/r/ProtonMail) - Official Proton community
- Privacy Guides Forum** : [discuss.privacyguides.net](https://discuss.privacyguides.net) - Technical discussions on privacy issues
- Reddit r/privacy**: [reddit.com/r/privacy](https://reddit.com/r/privacy) - General privacy tips


### Other


- [Have I Been Pwned](https://haveibeenpwned.com/) - Check if your accounts have been compromised
- [2FA Directory](https://2fa.directory/) - List of services supporting 2FA