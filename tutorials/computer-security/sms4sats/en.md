---
name: SMS4Sats
description: Receive and send SMS anonymously by paying in Bitcoin Lightning
---

![cover](assets/cover.webp)


SMS verification has become a must for many online services. Whether it's to create an account on a platform, validate a registration or confirm an identity, websites almost systematically require a telephone number. This widespread practice poses a major problem for anyone wishing to preserve their privacy: your personal number becomes a permanent identifier, linking your various digital activities to your real identity and opening the door to unwanted commercial solicitations.


**SMS4Sats** responds to this problem by offering temporary telephone numbers for receiving and sending SMS messages. The service stands out for its no-registration model and exclusive Bitcoin payment via Lightning Network. For a few satoshis, you get a disposable number enabling you to validate a registration without ever revealing your personal number.


This tutorial guides you through the three SMS4Sats features: receive a verification SMS, send an anonymous SMS, and rent a temporary number for several hours.


## What is SMS4Sats?


SMS4Sats is an online service accessible at [sms4sats.com](https://sms4sats.com), enabling anonymous SMS management via payment in Bitcoin Lightning. The service offers three distinct functionalities: reception of single-use verification codes, sending of SMS to any number, and rental of temporary numbers for several hours.


### Philosophy and operating model


The project is designed to ensure maximum confidentiality and financial sovereignty. By requiring no account creation and accepting only Bitcoin Lightning payments, SMS4Sats completely eliminates the need to provide personal data. No email address, no credit card, no personal information is required. Only Lightning payment is required to access services.


The service supports over 400 sites and applications in around 120 countries, covering the majority of common verification needs. This extensive geographic coverage enables validation of registrations on a variety of platforms, from social networks to messaging services.


### Conditional payment model


SMS4Sats uses conditional Lightning invoices (hodl invoices) for its SMS reception functionality. This mechanism ensures that you are only charged if the SMS is actually received. If no message arrives within the allotted time (20 minutes maximum), the payment is automatically cancelled and the satoshis are returned to your wallet. This guarantee does not apply to sending and rental features, which are non-refundable.


## The three SMS4Sats features


The SMS4Sats interface is organized around three tabs corresponding to three distinct uses: **RECEIVE** to receive verification codes, **SEND** to send anonymous SMS, and **RENT** to rent a temporary number.


### Receive an SMS


The main feature allows you to obtain a temporary number to receive a unique verification code. Once the code has been received and used, the number is permanently deactivated.


### Send an SMS


This feature lets you send an SMS to any telephone number without revealing your identity. The recipient will receive the message from an anonymous number.


### Rent an act


For users who need to receive multiple SMS messages on a single number, SMS4Sats offers a temporary rental option. This option allows you to receive and send several messages during the rental period.


**Note on prices** : The prices shown in this tutorial are indicative. They vary according to the country of the number, the target service and current demand. For example, an SMS to Telegram France can cost between 1,500 and 5,000 satoshis, depending on conditions. Always check the exact amount of the Lightning invoice before paying.


## Receive a verification SMS


Let's look in detail at how to use SMS4Sats to receive a verification code, illustrated by the creation of a Telegram account.


### Step 1: Select country and service


Go to [sms4sats.com](https://sms4sats.com) and stay on the **RECEIVE** tab. Select the country of the desired number from the drop-down menu. If the target service of your subscription is listed, select it to optimize the chances of reception.


![Sélection du pays France et du service Telegram sur SMS4Sats](assets/fr/01.webp)


In this example, we select France as the country and Telegram as the target service. Click **NEXT** to proceed to the next step.


### Step 2: Pay the Lightning invoice


A Lightning invoice is displayed in the form of a QR code. The amount varies according to the country and service selected. Scan the QR code with your Lightning wallet or copy the invoice to pay manually.


![QR code de paiement Lightning avec garantie de remboursement](assets/fr/02.webp)


Note the important message: "No SMS Code = No Payment". If you do not receive an SMS, your payment will be automatically cancelled and refunded within a maximum of 20 minutes.


### Step 3: Get the temporary number


Once payment has been confirmed, the temporary phone number is immediately displayed. A counter shows the time remaining to receive the SMS.


![Numéro temporaire révélé avec timer d'attente](assets/fr/03.webp)


Copy this number (here +33 7 74 70 09 66) to use it on the service you wish to register for.


### Step 4: Use the number on the target service


Enter the temporary number on the application or website where you create your account. In our Telegram example, enter the number, confirm it and wait for the verification code.


![Processus d'inscription Telegram avec le numéro temporaire SMS4Sats](assets/fr/04.webp)


The process is identical to conventional registration: you enter the number, Telegram sends a verification code by SMS, and then you finalize account creation.


### Step 5: Retrieve the verification code


Return to the SMS4Sats interface. As soon as the SMS is received, the activation code is automatically displayed. Click on **COPY CODE** to copy it easily.


![Code de vérification reçu sur SMS4Sats](assets/fr/05.webp)


Enter this code on the target service to finalize your registration. The temporary number is then permanently deactivated.


## Send an anonymous SMS


SMS4Sats also lets you send SMS messages to any number without revealing your identity.


### Step 1: Writing the message


Click on the **SEND** tab. Enter the destination phone number with its international dialling code and write your message (maximum 1600 characters).


![Interface d'envoi de SMS avec numéro destinataire et message](assets/fr/06.webp)


Click **NEXT** to proceed to payment.


### Step 2: Pay and send


Pay the Lightning invoice displayed. Once payment has been confirmed, the SMS is sent immediately to the recipient.


![Confirmation d'envoi du SMS avec code de confirmation](assets/fr/07.webp)


A confirmation code is displayed to confirm that the message has been sent. The recipient will receive the SMS from an anonymous number.


## Rent a temporary number


For uses requiring several SMS messages on the same number, the RENT feature lets you rent a number for several hours.


### Rental configuration


Click on the **RENT** tab. Select country and duration.


![Interface de location de numéro avec avertissement de non-remboursement](assets/fr/08.webp)


**Important points to note:**


- Prices vary according to country and length of stay
- Rentals are non-refundable**, unlike single-use SMS messages
- Leased numbers generally do not work with Telegram
- This option is suitable for subscribing to several services in succession


Once you've clicked on **NEXT** and paid the Lightning invoice, you'll get a number that you can use for the duration of the rental period to receive and send SMS messages.


## Advantages and limitations


### Highlights


**No personal data required**: The no-registration model guarantees that no personal information is collected.


**Three additional functions**: Receive, send and rent cover most needs.


**Payment in Bitcoin only** : Lightning Network allows instant and pseudonymous transactions.


**Automatic reimbursement**: When receiving SMS messages, the hodl invoices system guarantees that you only pay if the SMS arrives.


### Constraints to consider


**Relative SMS channel security**: SMS codes are not a robust authentication method and should not be used for sensitive accounts.


**Variable compatibility**: Many sites detect and block virtual numbers. Several attempts may be necessary.


**Non-reusable numbers**: After single use, the number is recycled and cannot be recovered.


**Non-refundable rentals**: Unlike one-off SMS messages, rentals do not come with a money-back guarantee.


## Best practices


### Use Tor for more privacy


SMS4Sats is accessible via [Tor](sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion). This configuration masks your IP address when accessing the service.


### Avoid critical accounts


Never use a disposable number for your important accounts (bank, main email). If these platforms require you to revalidate your number at a later date, you will lose access to the account.


### Separate your digital identities


For pseudonymous accounts, combine the temporary number with a disposable email address and a browser isolated from your usual use.


### Choose a sturdy 2FA


Once your account has been created, activate stronger authentication solutions: TOTP application (Aegis, Ente Auth) or FIDO2 physical security key.


## Conclusion


SMS4Sats is a complete solution for confidential SMS management. Whether you want to receive a verification code, send an anonymous message or rent a temporary number, the service meets a wide range of confidentiality needs, thanks to payment in Bitcoin Lightning.


Bear in mind its limitations, however: the service does not guarantee absolute anonymity, and is not suitable for sensitive or long-term accounts. Used wisely and with an awareness of its limitations, SMS4Sats is a practical tool for regaining control over your telephone communications.


## Resources



- [SMS4Sats official website](https://sms4sats.com)
- [Service FAQ](https://sms4sats.com/faq)
- [Tor address](http://sms4sat6y7lkq4vscloomatwyj33cfeddukkvujo2hkdqtmyi465spid.onion)