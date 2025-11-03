---
name: Alias Vault
description: Powerful tool to manage passwords, two-factor authentication and aliases (with built-in email server) - Also self hosted!
---

![cover](assets/cover.webp)


Online privacy and security is a topic that anyone, regardless of his or her business, should pay close attention to.


These issues are, moreover, part of a world in constant turmoil: more and more developers are participating in the topic, bringing implementations to established solutions and new products.


This is the case with **Leendert de Borst** and his `Alias Vault`, a revolutionary tool (the first of its kind) that allows you to manage and store passwords, use password records to authenticate to web services, administer two-factor authentication, but most importantly generate real _aliases_, all in a single interface.


**But Alias Vault doesn't stop there**.


## Key Features


Alias Vault works in the cloud on the developer's servers or self-hosted in its own infrastructure, an option for which Docker files and image are available to install with a scipt. In addition to the web interface, extensions are available for all popular browsers, as well as mobile apps for iOS and Android; the latter can also be downloaded from F-Droid, bypassing the official Google store.


In one interface Alias Vault is:


- Free and open source**
- Password Manager**, to store all complex passwords. Using the browser extension, the password manager completes logins to websites
- 2FA**, to support two-factor authentication
- Alias manager with embedded email server**: Alias Vault does not create aliases that forward email to a user's mailbox; rather, it creates actual alter-egos, complete with first name, last name, gender, username, password, and birthday (if this information is required).


An extensive and thorough documentation is part of the package, which will accompany newcomers to the discovery of this powerful tool.


## No personal data!


It starts, as always, from the [aliasvault.net](aliasvault.net) website. As mentioned, Alias Vault can be used on one's own server, or from the developer's cloud to get acquainted with it before moving to the self-hosted solution.


The site has really eye-catching and well-maintained graphics, but the good stuff comes if you start getting your hands on it: **create your account**.


![img](assets/en/01.webp)


To your enormous surprise you will find that Alias Vault does not ask for personal information: all you need to create the account is any nickname, a word familiar to you, as long as it is available. Agree to the Terms of Service, choose the word, and continue.


![img](assets/en/02.webp)


Set the **`master password`** now, which is the most important piece of information in your entire new system. With this one password, in fact, you will be the only one who can access/recover the account, as it will keep your `vault` encrypted on the server that will host your information.


![img](assets/en/03.webp)


Fact: You have created your own password manager and alias manager, but without giving your own working, private email address.


![img](assets/en/04.webp)


Alias Vault welcomes you to a safe, new, personal but also empty space. And now we begin to populate it a bit.


If you already have a password manager, you can import the file from the one you are using, to evaluate the differences with other provider, or perhaps eliminate the alias manager so you can manage everything in one application.


![img](assets/en/05.webp)


Alias Vault is extremely simple: you have one main page, which is the `Home`, with two menus:


- `Credentials`: which allows you to create and then manage identities and aliases
- `Email`: an inbox where you can check incoming messages for aliases you have generated.


![img](assets/en/06.webp)


It is the creation of a first `alias` that we are interested in doing, so go to the top right of the page and click _+New Alias_.


![img](assets/en/07.webp)


Initially the menu looks minimal, as per the philosophy of Alias Vault. To discover the features of this function, click on _Create via advanced mode_.


![img](assets/en/08.webp)


The top part of the first screen, you can use it to import password credentials that you already use for services you have a subscription with, or that you use most often online.


If you have enabled two-factor authentication on any (or all) of the above services, with Alias Vault you can also manage this additional layer of security by importing the `secret key`. Alias Vault will create the `TOTP` required for access.


![img](assets/en/09.webp)


**Caution**: In the space reserved for the email address, Alias Vault proposes its own domain by default; in order to use the correct address you previously created accounts with, click on _Enter custom domain_, so you can set the correct domain after `@`.


![img](assets/en/14.webp)


The bottom part of this screen is the most fun. Click on _Generate Random Alias_ and Alias Vault will create separate identities for you for different needs, each with its own mailbox, very robust level passwords, supplemented with other details such as gender, date of birth, and a suitable nickname.


![img](assets/en/10.webp)


From an apposite menu, you can change the settings that affect password generation, such as choosing only lowercase letters and eliminating characters that may be ambiguous.


![img](assets/en/11.webp)


You can use the alias email suggested by Alias Vault, or change domains if you click on the corresponding drop-down menu.


![img](assets/en/12.webp)


Before you use this email for a login service, you can test its functionality by sending a message from an address of your own to the newly created mailbox.


![img](assets/en/13.webp)


**⚠️ WARNING**: Receipt of emails is possible thanks to Alias Vault's built-in server, but this only allows you to receive emails and not to reply, or use the email box with the "conventional" functions of an `alias` service. It thus differs greatly from Simple Login, Addy and other platforms that are dedicated exclusively to this type of service. For the example of Simple Login you can view the dedicated tutorial:


https://planb.academy/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41

To delete an alias you have created as a test, all you have to do is log into your `Home`, then `Credentials` and click on the identity you want to delete. The _Delete_ command will appear in the upper right-hand corner for you to proceed.


![img](assets/en/16.webp)


## Browser extension


Depending on what your needs are, you can resort to the browser extension, which can be found on the most widely used browsers.


![img](assets/en/15.webp)


It installs as you already did with all the other extensions, so I won't dwell on that detail.


The browser extension is there to make it easier to log in to online services, or to create new aliases as needed: if the service is stored among your Alias Vault records, the auto-fill does what is needed.


![img](assets/en/17.webp)


The only caution is to verify that Alias Vault is active. In fact, the application has a default setting whereby it pauses after a period of inactivity. This is a very useful feature, **when you have to step away from your computer, for example, and prevent someone else from accessing your accounts**. A streamlined procedure will allow you to log in again by entering the `master password`, if the previous session is still in the cache. The time for logging out is one of the parameters you can customize, shortening or lengthening it according to your preferences.


## Mobile App


Like all self-respecting apps of this kind, Alias Vault has a version for mobile devices, in both Android and iOS environments. For Android, you can download the app from [F-Droid](https://f-droid.org/packages/net.aliasvault.app/).


At the time of this writing (late August 2025), the mobile app considers `auto-fill` an experimental feature, not working except with very few sites. Until it is fully implemented, using Alias Vault on mobile requires copy/paste of data.


Once you download the app from the store, to login you will simply enter the user and `master password` created on the web app.


![img](assets/en/18.webp)


When opening your `vault`, you will be asked if you want to enable biometrically controlled access, an additional layer of security to prevent someone else from accessing your passwords if they happen to be holding your phone.


![img](assets/en/19.webp)


If you decide to set up biometric checking, go ahead. If you skip the step and change your mind, you can also configure it later from the _Settings_ menu.


Once you have completed logging in, you will find the data you have already created synchronized again.


![img](assets/en/20.webp)


The mobile app can be routed to the link to the`vault` hosted on its own server.


![img](assets/en/22.webp)


And it is precisely the self-hosted version that we will address, briefly, in the next section.


## Self-Hosting: full control over your data


Alias Vault, to be fair, is not the first `password manager` that allows you to deploy the service on your infrastructure. There are others, but some either have limitations or are partially closed source.


The opportunity is unique: **end dependence on external service providers or clouds, but use your own local server to guard and manage the passwords, aliases, and extremely sensitive information associated with it all**. With Alias Vault you can also have the email service point to your own email server for added confidentiality.


It is time to turn to [documentation](https://docs.aliasvault.net/installation/), to find out how to proceed to self-host Alias Vault.


![img](assets/en/23.webp)


Alias Vault runs on Docker Compose, so minimal experience with Linux and Docker is required. You can start with the basic installation and then complete with more advanced solutions.


Your server must be running on a 64-bit machine, with a Linux distribution, 1 GB of RAM and at least 16 GB of storage; the version of Docker (CE) must be at least 20.10 or higher, while Docker Compose requires a release from 2.0 and up.


I decided to try Alias Vault with a thin client, on which DietPi is installed as a distribution, a Debian Bookworm base, optimized to the essentials and already running `Docker` and `Docker Compose`.


First, in order to have some order, create a directory in your home, open the `terminal` and paste the command to run the installation script.


```bash
curl -L -o install.sh https://github.com/lanedirt/AliasVault/releases/latest/download/install.sh
```


![img](assets/en/24.webp)


![img](assets/en/25.webp)


When the installation is complete, you will find your credentials for access:

```
Admin Panel: https://localhost/admin
Username: admin
Password: yyy0xyx1yxy2zxx4
```


Check the contents of the directory after installation.


![img](assets/en/29.webp)


To launch Alias Vault use the command:


``` Launch-Alias-Vault

./install.sh start

```

Alias Vault adesso gira sul tuo server personale.

![img](assets/en/30.webp)

Apri un browser e digita l'url: ti comparirà la pagina per fare login come `Admin` di Alias Vault.

![img](assets/en/26.webp)

Il più è fatto! Hai davanti a te il pannello per amministrare Alias Vault in maniera personalizzata.

![img](assets/en/27.webp)

Da questa interfaccia, potrai controllare quanti e quali utenti stanno utilizzando il servizio, limitarne l'uso, cancellare gli utenti (azione irreversibile) e soprattutto controllare tutti i `log`.

Se si tratta di una nuova installazione, non avrai altri utenti oltre ad `admin`; per crearne di nuovi, apri un'altra `tab` del browser e digita:

```

localhost/user/start

```

![img](assets/en/28.webp)

Da qui in poi, tutto procede come abbiamo visto in precedenza nella guida, con la differenza che adesso stai usando Alias Vault sul tuo server. Se la tua macchina è adeguatamente configurata e protetta, questo è un modo elegante e sicuro di gestire un tuo password e alias manager, senza servizi di terze parti.

Per fermare Alias Vault, torna al terminale e digita:

``` Stop-Alias-Vault
./install.sh stop

```


![img](assets/en/31.webp)


## Considerations on encryption and security


![img](assets/en/32.webp)


According to what Lanedirt states on the site, in the documentation, and on Github, with Alias Vault **all the information (components) you place on Alias Vault, remain tightly bound to the device, encrypted and inaccessible to anyone who does not know the `master password`**.


The `master password` is thus the fundamental element of the whole `vault`. After it is entered, it is processed with the `Argon2id` algorithm, a Hard-memory key derivation function, to prevent the secret from leaving the device.


Everything remains hidden even from the cloud or hosting service manager. In fact, from the admin panel you cannot access user details, you can only know if they have created aliases, received emails, and little else.


All stored contents are encrypted and decrypted by cryptographic keys derived from the `master password`. **Only encrypted data is stored on the server, nothing appears in plain text**. If a user forgets or loses his `master password`, the account linked to it is irreversibly lost, as the server cannot access the plaintext contents.


For the self-hosted version there is the script to reset the `master password`, but this does not prevent data loss.


![img](assets/en/33.webp)


Since Alias Vault is in the _Beta_ stage, you may have difficulty accessing it if you change/update the master password. I suggest you choose it robust and complex from the beginning so that you can experiment with the service and eventually decide whether to use it. If you have difficulty accessing the cloud following the password update, please contact Alias Vault support.


For a complete understanding of the architecture and security adopted by Alias Vault, I strongly recommend that you consult [this page](https://docs.aliasvault.net/architecture/), which contains details of the cryptography underlying its operation.


## Roadmap

The developers' intentions are to make Alias Vault mature and stable by the end of 2025, so as to define its future usage characteristics.


Alias Vault is and will always remain open source and free, but probably not unlimitedly as in beta. Some paid features are in the process of being implemented, as they have already been announced.


There are team/family plans and support for hardware keys, the latter for authentication with FIDO2 or WebAuth.


## Who needs Alias Vault


**A tool like this is ideal for anyone who puts online privacy first**.


Your identity is, in all likelihood, at the heart of the business you conduct online and must be safeguarded by all means to put **that** data away from services, companies and brokers willing to do anything to get their hands on your online behavior.


Alias Vault gives you back complete control over your credentials, mitigating or eliminating altogether the need to rely on third parties to guard and encrypt your most sensitive data.


Alias Vault's architecture and cryptographic facility are ideal for sovereign individuals, small and medium-sized businesses, development teams, and all **open source** application enthusiasts. If you fall into any of these categories: have fun discovering Alias Vault.