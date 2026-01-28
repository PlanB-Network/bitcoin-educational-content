---
name: COLDCARD - Co-Sign
description: Discover the Co-Sign feature and use it on your COLDCARD
---

![cover](assets/cover.webp)

*NB: This tutorial is aimed at people who already have some experience with multisignature wallets, Coinkite devices, and software such as Sparrow wallet or Nunchuk.*


![video](https://youtu.be/MjMPDUWWegw)



**Why ColdCard Co-Sign?


This feature lets you add **spending conditions** to your ColdCard (Q or Mk4) device in the manner of a Hardware Security Module (HSM), to protect your funds while retaining considerable flexibility and control over them.


Spending conditions can be, for example:



- Limits on magnitude**: cap the amount of bitcoins you can spend in a single transaction.
- Velocity limits:** decide how many transactions you can carry out per unit of time (per hour, day, week, etc.), requiring a minimum number of blocks between them.
- Pre-approved addresses:** Only allow bitcoins to be sent to pre-approved addresses.
- Two-factor authentication:** Requires confirmation from a third-party 2FA mobile application (TOTP [RFC 6238](https://www.rfc-editor.org/rfc/rfc6238)) on an NFC-enabled smartphone/tablet with internet access.


**How it works


By adding a second seed to your ColdCard Mk4 or Q device, called the "Spending Policy Key", which we'll refer to throughout this tutorial as the "C Key".

In addition to this additional seed, you'll be asked to supply at least one additional key (XPUB), which we'll call a "Backup Key", in order to create a Wallet Multisig 2-on-N.


In summary, we're going to create a Wallet Multisig, and your ColdCard device will contain 2 of the private keys needed to spend the funds, the device's seed master and the "Spending Policy Key".


Each time the "C Key" is asked to sign, the specified spending conditions will apply, and the ColdCard will only sign if the transaction complies with them.


If you wish to dispense with these spending conditions, you can do so:


- by signing with one of the backup keys and the seed hand, or 2 backup keys depending on the size of your Multisig.
- by entering the "Spending Policy Key" or "C Key" in the "Co-Sign" menu. **The latter cannot be consulted directly on the device, otherwise anyone could cancel the spending conditions configured.**



## Configuring ColdCard Co-Sign


![video](https://youtu.be/MjMPDUWWegw)


### 1- Activate functionality


First of all, make sure your device has at least the latest firmware version:


- Mk4: v5.4.2
- Q: v1.3.2Q



On your Mk4 or ColdCardQ, go to *Advanced Tools > ColdCard Co-Signing*.


![Co-Sign](assets/fr/01.webp)


*In the following tutorial, screenshots will be taken on a ColdCardQ for convenience, but the steps and menus are identical between the Mk4 and the Q.*


A summary of the functionality is displayed.

The terminology used to designate the keys, which we'll be using again in the 2-on-3 multi-signature Wallet we're about to create, is:


Key A = Coldcard master seed

Key B = Backup Key

Key C = Spending Policy Key


Click **"ENTER "**.


![Co-Sign](assets/fr/02.webp)


The next step is to decide which private key will act as the "Spending Policy Key" or "Key C".


We can see that we have several options open to us:



- Or press **"ENTER "** to generate a new seed sentence of 12 words.



- Either click on **"(1) "** to import an existing 12-word seed, or choose **"(2) "** to import an existing 24-word seed.



- Or press **"(6) "** to import a seed from your device's vault.


For the purposes of this tutorial, we've decided to import an existing 12-word seed by pressing **"(1) "**. This can be any seed BIP39 you already own, and for which you obviously have a backup.


Use your keyboard to enter the 12 words of your seed. For this example, we'll choose the seed valid phrase beef x 12. Then press **"ENTER "**.

*NB: if you do not have a backup of this seed, you will no longer be able to modify the "Co-Sign" settings on your device, in order to change your spending conditions*


The "Co-Sign" feature is now activated on the device. Next we'll need to choose our spending conditions, then complete the creation of the multi-signature Wallet.


![Co-Sign](assets/fr/03.webp)


### 2- Choose the spending conditions or "*spending policies*"


Here we specify the spending conditions that must be met when the **"C Key "** or **"Spending Policy Key**" signs a transaction.


In the **"Co-Signing "** menu, click on **"Spending Policy**".


You can then choose the maximum magnitude, i.e. the maximum number of satoshis that can be spent in a single transaction.


For this example, we'll choose a maximum magnitude of **21212** satoshis. Click on **"ENTER "** to confirm.



![Co-Sign](assets/fr/04.webp)


We then choose to set the maximum velocity, i.e. the number of transactions the device will be able to sign per unit of time. For this tutorial, we'll choose unlimited velocity, i.e. no limit on the number of transactions.



![Co-Sign](assets/fr/05.webp)


### 3- Create Wallet Multisig 2-on-N


We still need to choose the third key for our Wallet Multisig, i.e. the **"Backup Key "** (Key B), in addition to the device's **master seed** (Key A) and the **"Spending Policy Key "** (Key C).


Our "B Key" will have to be imported either via SD card, or via QR code in the case of ColdCardQ.

To do this, we'll need a second ColdCard Mk4 or Q device, on which our "Key B" is used.


On this second device containing your **"Backup Key "**, say a ColdCard Mk4 for this example, go from the main menu to **"Settings "**, then, **"Multisig Wallet"**, and finally **"Export Xpub "**.

(If your second device is a ColdCardQ, you'll have the option of exporting your Xpub via QR code, of course).




![Co-Sign](assets/fr/06.webp)




On the next screen, insert an SD card and click on the **"validate "** button at bottom right. Then click on **"(1) "** to save the file on the SD card.


The file will contain the public key fingerprint (*fingerprint*) in its name, and will take the form `ccxp-0F056943.json`.



![Co-Sign](assets/fr/07.webp)


Then insert the SD card into the "initial" ColdCardQ to import our "Backup Key" (key B).

In the "ColdCard Co-Signing" menu, choose "Build 2-of-N", then on the next screen click **"ENTER "**, then again **"ENTER "** to import the "Backup Key" from the SD card.


![Co-Sign](assets/fr/08.webp)


On the next screen, leave "Account Number" blank (unless you know exactly what you're doing) and click **"ENTER "** again.


![Co-Sign](assets/fr/09.webp)


At last, we're ready to use our new Wallet Multisig 2-sur-3, composed as follows:


Key A= Coldcard Q master seed

Key B= Backup Key (just imported from a second Coldcard device)

Key C= Spending Policy Key (if used to sign, imposes predefined spending conditions)


## Co-Sign with Sparrow wallet


If necessary, refer to the tutorials below to familiarize yourself with the Sparrow wallet software:


https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

https://planb.academy/tutorials/wallet/desktop/sparrow-multisig-5860333b-6dd8-4aaa-8ab6-89ebc6276f1f

### 1- Export Wallet Multisig 2-sur-3 to Sparrow wallet


We now need to export our Wallet Multisig to Sparrow so that we can place our first satoshis there.


From the main menu of your ColdCardQ, select **"Settings "**, then **"Multisig Wallets "**.

The set of multisig wallets known to your ColdCard is now displayed, with the number of keys involved here "2/3" (2-sur3). Choose the Multisig **"ColdCard Co-Sign "** we've just created, then click on **"ColdCard Export "**.


![Co-Sign](assets/fr/10.webp)



Finally, choose the method that will allow you to export Wallet to Sparrow. In our case, we'll choose SD card, and so click on **"(1) "** after inserting an SD card in slot A of the device.


![Co-Sign](assets/fr/11.webp)


Then in Sparrow wallet, select "Import Wallet".


![Co-Sign](assets/fr/12.webp)


Then click on **"Import File "**. Then choose the file **"export-Coldcard_Co-sign.txt "** on your SD card.


![Co-Sign](assets/fr/13.webp)


Give your Wallet a name as it will appear in Sparrow, and choose a password to encrypt your Wallet (or not).


![Co-Sign](assets/fr/14.webp)


![Co-Sign](assets/fr/15.webp)


We're now ready to receive our first satoshis and test the spending conditions we've applied to our Wallet.


![Co-Sign](assets/fr/16.webp)


### 2- Testing predefined spending policies


As a reminder, we had decided on a maximum magnitude of 21212 satoshis for our Wallet Multisig. This meant that each time the Spending Policiy Key (Key C) signed a transaction, the latter would only be valid if the amount spent was less than or equal to 21212 satoshis.


Let's test it.

First, let's click on the "Receive" tab in Sparrow and drop a few Satss onto Wallet, which we'll use throughout this tutorial.


![Co-Sign](assets/fr/17.webp)


![Co-Sign](assets/fr/18.webp)


Then let's try to spend more than the 21212 allowed satoshis by simulating a 50,000 Sats transaction.


![Co-Sign](assets/fr/19.webp)


![Co-Sign](assets/fr/20.webp)


![Co-Sign](assets/fr/21.webp)


![Co-Sign](assets/fr/22.webp)


After scanning the QR code representing the *unsigned* transaction with our ColdCardQ to import the transaction, this is what we're shown on the screen. A warning message tells us that the spending conditions have not been met. If we sign the transaction anyway, then only one of the 2 keys (the seed master on the device, but not "Key C") will sign.



![Co-Sign](assets/fr/23.webp)


Here, after importing our transaction into Sparrow, we can see that only one of the signatures has been applied to the transaction.


![Co-Sign](assets/fr/24.webp)



Now let's repeat the experiment, but for a transaction of 21,000 satoshis, i.e. less than the maximum magnitude (21212 Sats) we set for this Wallet.



![Co-Sign](assets/fr/25.webp)


![Co-Sign](assets/fr/26.webp)


![Co-Sign](assets/fr/27.webp)


![Co-Sign](assets/fr/28.webp)


Let's try signing this transaction with our ColdCardQ.


No problem this time, no warning message appears, and when we import the signed transaction into Sparrow wallet, this time the 2 signatures have been applied, making the transaction valid and ready for distribution.



![Co-Sign](assets/fr/29.webp)



![Co-Sign](assets/fr/30.webp)





## Co-Sign with Nunchuk


https://planb.academy/tutorials/wallet/mobile/nunchuk-6cbcb406-ec84-478f-afac-bb4da366a6fa

### 1- Web 2FA & Whitelisted addresses


In this paragraph, we'll use our Wallet Multisig Co-Sign with Nunchuk, and take the opportunity to apply new spending conditions to see how it goes.


Go to *Avanced Tools > ColdCard Co-Signing*.

We are asked to enter our "Spending Policy Key", in order to access the menu allowing us to change the spending conditions. In our case, we enter 12 x "beef".


We've decided to keep a magnitude of 21212 Sats, and a maximum "Limit Velocity" for practical reasons related to this tutorial. On the other hand, we're going to use the **"Whitelist Addresses "** menu to impose the addresses on which our funds can be spent.



![Co-Sign](assets/fr/31.webp)



Scan the QR codes associated with the addresses (we'll choose 2) you wish to add to your whitelist, then click **"ENTER "**. After validating your addresses by pressing **"ENTER "** successively, we see that limits on Magnitude and beneficiary addresses have been applied.


![Co-Sign](assets/fr/32.webp)


Finally, to get a complete picture of the possibilities offered by "Co-Sign", let's activate the "Web 2FA" option.

This feature lets you use a TOTP RFC-6238-compliant application such as Google Authenticator / Ente Auth / Proton Authenticator / Authy 2FA / or Aegis Authenticator, to add an extra layer of security.


https://planb.academy/tutorials/computer-security/authentication/ente-auth-1928e65a-3b43-40f3-9efd-457ee2d79bb9

https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc

In concrete terms, before signing a transaction, you'll need to bring your NFC-enabled, internet-connected device close to your Coldcard. This will automatically take you to a coldcard.com web page, where you'll be asked to enter the 6-digit code for your application. If you enter the right code, the web page will show you either a QR code to scan for the ColdCardQ, or an 8-digit code to enter on your Mk4, to authorize your device to sign.




![Co-Sign](assets/fr/33.webp)


After scanning the QR code displayed in your dual authentication application, and adding your ColdCard Co-Sign (CCC) account, you will be asked to verify that everything is in order by entering your 2FA code.


Type your ColdCard into the back of your NFC device.


![Co-Sign](assets/fr/34.webp)


On the web page that opens, enter the 2FA code of your favorite application. Then scan the QR code displayed with your ColdCardQ (or enter the 8-digit code displayed in your Mk4).


![Co-Sign](assets/fr/35.webp)



We have now imposed a limit on magnitude (21212 Sats), destination addresses and double authentication.


![Co-Sign](assets/fr/36.webp)


### 2- Export Wallet Multisig 2-on-3 to Nunchuk


Let's export Wallet Multisig 2-on-3 into Nunchuk this time, as we did with Sparrow previously.

Go to *Settings > Multisig Wallets > 2/3: ColdCard Co-sign > ColdCard Export*.


![Co-Sign](assets/fr/10.webp)


This time choose the NFC option for export by clicking on the ColdcardQ button of the same name **"NFC "**.


![Co-Sign](assets/fr/37.webp)


In Nunchuk, if you're opening the application for the first time, click on **"Recover existing Wallet"**.


![Co-Sign](assets/fr/38.webp)


If you already have a Wallet in the application, click on the **"+"** at top right, then **"Recover existing Wallet"**.


![Co-Sign](assets/fr/39.webp)



Then choose **"Recover Wallet from COLDCARD "** then **"Multisig Wallet"**.


![Co-Sign](assets/fr/40.webp)


Finally, tap the back of your smartphone to the screen of your ColdCardQ to import the Wallet via NFC.


![Co-Sign](assets/fr/41.webp)


Our account and the satoshis previously deposited via Sparrow wallet are back.


![Co-Sign](assets/fr/42.webp)


### 3- Testing predefined spending policies


Let's now try to make a transaction that violates the 2 spending conditions we've set. **We'll try to spend more than 21212 Sats to an address that hasn't been approved.** Let's try to send 22 222 Sats to a random address.


![Co-Sign](assets/fr/43.webp)


Once the transaction has been created, click on the 3 small dots in the top right-hand corner to export it to your ColdCard.


![Co-Sign](assets/fr/44.webp)


Then choose **"Export via BBQR "**, and scan the QR code displayed with your ColdCardQ.


![Co-Sign](assets/fr/45.webp)


Your ColdcardQ then displays a warning which, as you scroll to the bottom of the screen, clarifies that the transaction violates the spending conditions, as expected.


**Note that the device does not tell us what spending conditions are involved, to prevent a potential attacker from trying to circumvent the restrictions.**



![Co-Sign](assets/fr/46.webp)


If you still validate by pressing **"ENTER "**, the QR code representing the signed transaction appears. If you import it on Nunchuk, you can see that only one signature has been applied.


![Co-Sign](assets/fr/47.webp)


![Co-Sign](assets/fr/48.webp)





Let's perform exactly the same operation, but this time with a transaction that respects the magnitude limit (21212 Sats), and spends the satoshis to one of the 2 addresses we've preconfigured.


We send the Nunchuk 12121 Sats to one of our 2 addresses. Then we export the transaction to our ColdCard as previously done.


![Co-Sign](assets/fr/49.webp)



After importing the unsigned transaction into our ColdCardQ, let's see what we're shown this time.


A warning is always present, but this time, scrolling to the bottom of the screen, we see that it's a matter of validating the transaction via 2FA. The device asks us to bring our ColdcardQ close to our Internet-connected NFC terminal (smartphone or tablet), which we do.


![Co-Sign](assets/fr/50.webp)


A web page opens on our smartphone, asking us to enter our 2FA code, which we do thanks to Proton Authenticator.


![Co-Sign](assets/fr/51.webp)




Then scan the QR code that appears on the web page, to authorize your ColdCard to sign the transaction.

The transaction is now signed by the 2 keys and therefore valid.


If "Push Tx" is enabled on your ColdCardQ, you can broadcast the transaction directly to the network with a simple tap on the back of your smartphone.


![Co-Sign](assets/fr/52.webp)



If you don't have "Push tx" activated, press the "QR" button on your ColdCardQ to display the signed transaction as a QR code, and import it onto Nunchuk, in the same way as in the previous example.


![Co-Sign](assets/fr/53.webp)


This time we notice that 2 signatures have been applied, so the transaction is ready to be broadcast on the Bitcoin network.


![Co-Sign](assets/fr/54.webp)



We've come to the end of this tutorial, which will give you an overview of the possibilities offered by the Co-Sign functionality integrated into Coinkite's ColdCardQ and Mk4 devices, as well as its use through wallets such as Sparrow and Nunchuk.