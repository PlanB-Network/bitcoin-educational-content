---
name: Voltz
description: The all-in-one Lightning wallet for your business.
---

![cover](assets/cover.webp)


The idea for the Voltz platform came from a group of bitcoiners who wanted to provide their own bitcoin wallet service. The result was a complete infrastructure for accepting bitcoin at retail. In this tutorial, we take you on a tour of Voltz and the bitcoin integration possibilities the platform has to offer.


## Getting started with Voltz


Beyond being a custodial Lightning wallet that lets you send, receive and pay daily, Voltz is a complete platform that provides numerous extensions for integrating bitcoin as a point of sale or marketplace in your business.


Go to the [Voltz] platform (https://www.lnvoltz.xyz/en) and create an account by clicking on the "Try now" button.


![voltz](assets/fr/01.webp)


![login](assets/fr/02.webp)


⚠️ It's important to set a strong alphanumeric password to increase your chances against brute-force attacks, and check that you are indeed on the official Voltz website to fill in your login details to guard against phishing.


The Voltz interface is very similar to that of the LnBits platform.


https://planb.academy/tutorials/business/others/lnbits-cdfe1e38-069a-4df9-a86b-ce01ef28f4c2

Voltz is in fact built on a LnBits server; check out our tutorial to learn how to mount your own LnBits servers and build your solutions on them.


https://planb.academy/tutorials/business/others/lnbits-server-6a406046-3cef-4a64-a82b-8d8f0f82a192

The platform allows you to efficiently manage multiple wallets. By default, when you sign up, you automatically have a Lightning wallet. However, you can add other wallets.


![wallets](assets/fr/03.webp)


### Portability


Voltz is not limited to a web interface: in the **Mobile Access** section, you can connect your active Voltz wallet to applications such as Zeus or Blue Wallet.


https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90

To do this, you need to install and activate the **LndHub** extension on the platform.


![lndhub](assets/fr/04.webp)


Select your active Voltz wallet and, depending on the rights you wish to grant, scan the appropriate QR code.


- The invoice QR code only allows you to read your wallet history and generate new invoices.
- The admin QR code allows you to view the history, generate invoices and also pay Lightning invoices.


![qrs](assets/fr/05.webp)


In this tutorial, we connect our Voltz wallet to the Blue Wallet application.


![connect](assets/fr/06.webp)


Once our wallet is connected, all actions carried out will be synchronized between Blue Wallet and Voltz. For example, when you generate an invoice on Blue Wallet, you also have a history on Voltz.


![sync](assets/fr/07.webp)


In the **Portfolio configuration** section, you'll find minimal parameters such as the customization of the wallet name and the currency in which you wish to receive your payments.


![config](assets/fr/08.webp)


### Extensions


One of the special features of the Voltz platform is its modularity, allowing you to activate the extensions you need. The list of extensions can be found in the **Extensions** menu.


![extensions](assets/fr/09.webp)


Among these extensions is the TPoS, a point-of-sale terminal you can use to keep an inventory and collect payments from your customers.


![tpos](assets/fr/10.webp)


From the Point of Sale terminal, you can :


- Get a web page you can share with your customers and partners;
- Manage product inventory;
- Generate Lightning invoices;
- Cash payments via Bolt cards.


The extension is available as a free version and as a paid version for more advanced features. To create a POS terminal, click on the **Open** button below the extension logo, then click on **New POS**.


![new_tpos](assets/fr/11.webp)


Define the name of your point of sale, then connect your Voltz wallet to your terminal to collect payments. You can activate gratuities by checking the **Activate gratuities** box. Also activate the invoice printing option if you wish to issue receipts to your customers (this functionality is still under development, so there may be malfunctions).


The point-of-sale terminal also includes tax configuration when you want to apply your country's tax directly to your products.


![tpos](assets/fr/12.webp)


Once your POS terminal has been created, you can add pre-configured products and services to ensure a smooth payment and accounting experience for you and your customers.


![product](assets/fr/13.webp)


Create your products by defining their name, adding an image and setting a selling price.  You can categorize your products for easier tracking. You can apply taxes directly to a specific product. If the product has no tax applied, the tax configured at the point-of-sale terminal creation stage will be applied automatically.


![products](assets/fr/14.webp)


You can automatically import your product list from a JSON format by clicking on the **Import/Export** button.


![exports](assets/fr/15.webp)


Access the checkout area via the link by clicking on the **New Tab** icon, or share your POS platform via QR code with your customers by clicking on the **QR code** icon.


![lien](assets/fr/16.webp)


![qr](assets/fr/17.webp)


Your customers can consult your catalog and make their payment from this interface.


![pos](assets/fr/18.webp)


![chose](assets/fr/19.webp)


![pay](assets/fr/20.webp)


![checkout](assets/fr/21.webp)


In the group of available extensions, you'll also find tools like the **Invoice** and **Payment Link** extensions, which let you generate invoices with specific products to collect isolated payments without going through the POS terminal.


## Keep track of your payments


In the **Payments** menu, Voltz gives you an overview of payments to your various wallets.

You can track your payments by :


- Status.
- The label: for example **TPOS** for point-of-sale payments and **lnhub** via the mobile connection in Zeus and Blue Wallet wallets.
- The collection wallet.
- Total incoming and outgoing payments.
- A well-defined period.


![payments](assets/fr/22.webp)


## More options


Voltz is also an infrastructure on which you can build your own solutions. In the **Extensions** section, you'll find a guide to developing your own extensions within the Voltz and LnBits ecosystem.


![build](assets/fr/23.webp)


In the event that you want to develop solutions outside the ecosystem but still use their infrastructure, in the **URL of node** section, you'll find API keys and documentation information with an example of what you can do with this data.


You can create Lightning invoices from your applications using your Voltz wallet, pay Lightning invoices, decode and verify invoices.


![keys](assets/fr/24.webp)


You now have a good grasp of Voltz. If you enjoyed this tutorial, we're sure you'll learn more about the best methods and tools for integrating bitcoin into your business with our course: Bitcoin for businesses.


https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a