---
name: BTCPay Server
description: Accepting BTC payments without intermediaries
---

![cover](assets/cover.webp)


![video](https://youtu.be/KqsM-n-e4aY)


BTCPay Server is a free, open-source software package created by Nicolas Dorier that enables bitcoin payments to be accepted without intermediaries. Designed to offer autonomy and financial sovereignty, it installs on its own server and provides complete transaction management, from invoicing to validation of on-chain or Lightning Network payments, and accounting. It integrates easily with e-commerce sites (WooComerce, Shopify, etc.) or can be used as a payment terminal for physical stores (*POS*).


BTCPay Server is without doubt the most advanced solution for merchants wishing to accept bitcoin. It is the most comprehensive and robust software in terms of security, sovereignty and confidentiality. On the other hand, it is also the most complex to install and maintain. There are also simpler alternatives: some are entirely custodial, like OpenNode, while others offer an interesting compromise between ease of use and sovereignty, like Swiss Bitcoin Pay :


https://planb.academy/tutorials/business/point-of-sale/swiss-bitcoin-pay-2-a78b057e-ed11-47ac-860c-71019fcb451a

The aim of this tutorial is to guide you step-by-step through the installation, configuration and use of BTCPay Server, so that you can deploy a secure, independent payment infrastructure in line with the Bitcoin ethos.


## BTCPay Server features


Centralized Bitcoin point-of-sale solutions, such as *OpenNode* for example, offer ease of use, but rely on a third-party company since they cannot be self-hosted and are, in most cases, proprietary. While they make it easier to set up payments, they involve commission charges and expose their users to more risks than a solution like BTCPay Server, both in terms of custody of funds and confidentiality.


BTCPay Server is aimed at online or physical merchants, associations and non-profit organizations wishing to receive donations in bitcoins. It is also an ideal solution for project owners and developers seeking direct support from their community.


The special features of BTCPay Server include :


- its **complete autonomy**,
- the absence of a **KYC** procedure,
- full control of funds**,
- the **elimination of platform fees**.


By becoming your own payment processor, you eliminate any dependence on a centralized third party between you and your customers. You can accept payments directly in bitcoins and generate payment invoices. This ensures that neither you nor your company can be banned by anyone else. You play the role of both bank and payment processor, without having to pay commissions to an intermediary for each transaction.


Transaction fees for **on-chain** remain, but can be reduced by using the **Liquid** or **Lightning** network.


In addition :


- Fully customizable interface and invoices;
- Native **Tor** support for enhanced confidentiality;
- Support for **crowdfunding**, **POS** and **payment buttons**;
- Compatible with many currencies ;
- Bitcoin direct and peer-to-peer payments ;
- Complete control over your private keys;
- Enhanced privacy ;
- Enhanced security ;
- Self-hosted software ;
- Support for **SegWit** and **Lightning network** ;
- Internal, node-based portfolio, with integration of hardware portfolios.


## Installing and configuring BTCPay Server


### Choosing your hosting mode


BTCPay Server can be installed in a number of different ways. Depending on your needs and resources, there are three main options:


- BTCPay Server hosted by a third party**: you use a platform that hosts the service for you. It's simple, but usually not free.
- BTCPay Server self-hosted on a cloud server** (e.g. via [btcpayprovider](https://btcpayprovider.com/), [Bitcoin People](http://bitcoinpeople.it/) or any other provider). This is the recommended solution for most novice merchants.
- BTCPay Server installed on your own hardware (locally)** : on a computer, mini-PC or Umbrel. This method is more technical, but offers total independence.


https://planb.academy/tutorials/business/point-of-sale/btcpay-server-umbrel-68e1c535-4322-4507-a69c-9dfcbc36dfd1

For a start-up merchant, **deployment on a cloud server** is the best compromise between autonomy, simplicity and security, without having to manage the entire technical infrastructure.


BTCPay Server can be deployed rapidly from a number of hosting providers. Among them, **Voltage** stands out as a benchmark solution for users requiring a **reliable**, **professional** and **sovereign** infrastructure.


### Create a BTCPay Server instance on Voltage


**Voltage** is a turnkey Bitcoin and Lightning hosting platform that lets you instantly deploy your own BTCPay Server, without complex configuration or server maintenance.


Visit the [official Voltage website](https://voltage.cloud).


![capture](assets/fr/03.webp)


Create a **user account** with a valid e-mail address and a strong password.


![capture](assets/fr/04.webp)


Voltage offers a **free 7-day trial**. Please note that after our 7-day free trial, you will be invited to sign up for a fixed subscription of **$25 per month** to continue **keeping your nodes active**.


Once you've created your Voltage account and logged in for the first time, you'll be redirected to the home page, which has two main sections:


- An **Infrastructure** section for managing Lightning nodes, Bitcoin Core, BTCPay Server and other Bitcoin services in the cloud;
- and a **Payments** section that lets you access Voltage's API Lightning to integrate Bitcoin payments into customized applications.


To deploy your **BTCPay Server** instance, click on **Access infrastructure**. This is where you can create, manage and monitor all your services, including your Bitcoin node and BTCPay Server.


#### Create a group


Before you can deploy a service, the platform will prompt you to **create a group**. A **group** (workspace) is a workspace that groups together all your Bitcoin and Lightning services (e.g. a node, a BTCPay Server, an explorer, etc.). It's a bit like a folder containing your various projects.


![capture](assets/fr/05.webp)


For the purposes of this tutorial, the group we've created will be called **Genesis**. You can add a profile picture if you wish. Once this is done, click on the **Create** button. You can invite other users to join the group, and even change the group name if you wish.


On the group home page, several options appear:


- Lightning Nodes** : to deploy a complete Lightning node (LND) ;
- Bitcoin Core Nodes** : to launch a complete Bitcoin node ;
- BTCPay Server** : to host a ready-to-use BTCPay instance;
- Nostr Accounts**: to manage Nostr identities.


Activate **double authentication (2FA)** to secure your account and services (the button is visible in red if deactivated).


![capture](assets/fr/06.webp)


Click on **BTCPay Server** among the options, then on **Launch a BTCPay Store**.


![capture](assets/fr/07.webp)


Voltage will then ask you to **create and configure your BTCPay Server instance** by choosing a **service name** (1) and enabling Lightning payments (2).


You'll need a Lightning node if you decide to accept Lightning payments.


If you don't already have a Bitcoin or Lightning node, Voltage will suggest you create one automatically.


Click on **Create a Lightning node** (3) .


![capture](assets/fr/08.webp)


Once on the node creation interface, you'll be asked to choose between the **standard** and **professional** layouts.


You can create a real node (**Mainnet**) or a test node (**Testnet**). Then click on the **Continue** button.


![capture](assets/fr/09.webp)


For this tutorial, let's use the standard plan. Enter the **node name**, a **password** and press the **Create** button.


![capture](assets/fr/10.webp)


After a few moments, your node will be operational and you'll be able to open a free channel with a reception capacity of 500,000 sats.


![capture](assets/fr/11.webp)


A little further down on the right, you'll find all the information you need about your knot!


![capture](assets/fr/12.webp)


Now that we've got our Lightning node up and running, let's get back to installing our BTCPay server. You can now click on the **Create BTCPay** button.


![capture](assets/fr/13.webp)


A page will open with your default login details, along with a message prompting you to change your initial password. Once you've done this, click on the **Login Now** button to access your interface.


![capture](assets/fr/14.webp)


That's it! Your BTCPay server is ready to use. You'll be redirected directly to your BTCPay server's login page.


![capture](assets/fr/15.webp)


Once you have logged in, configure your first **store**:



- Give it a **name**.



- Choose the **default currency** (EUR, USD, CFA, etc.).



- Select a **exchange rate provider** (e.g. CoinGecko).


![capture](assets/fr/16.webp)


You will then be redirected to your store's dashboard. On the dashboard interface, you'll notice that the **Create your shop** button is marked in green, as this step has already been completed.


![capture](assets/fr/17.webp)


A little further down we have the **Configure wallet** and **Configure Lightning node** buttons. In our case, we've already connected to a Lightning node running on voltage. So we won't have to do it here.


Let's move on to configuring a portfolio. Click on the **Configure a portfolio** button.


Since we're just getting started with BTCPay Server, let's connect an existing wallet. So press **Connect an existing portfolio**.


![capture](assets/fr/18.webp)


You must then choose your **import method**. Among the available options, select **Enter extended public key**.


![capture](assets/fr/19.webp)


By linking an existing wallet, you can receive your payments **directly on this external wallet**, without the BTCPay server having access to your private key. So, even if the server were hacked or the public key (`xpub`) compromised, an attacker could view your transaction history, but would be **impossible to access your funds**.


Once you click on the **Enter extended public key** button, you will be **redirected** to the page where you must provide this key.


Now let's retrieve the **extended public key**.


### Connecting a Bitcoin wallet


To receive your payments, you need to connect a Bitcoin wallet to your store. To do this, you have several options:



- Hardware portfolio** (Ledger, Trezor, Coldcard...) ;



- Software portfolio** (Blockstream App, Ashigaru, Electrum, Sparrow...)



- BTCPay Server** internal wallet (not recommended, as it's less secure and exposes your funds more in the event of server hacking).


In this tutorial, we'll be using a **software portfolio**, which is more accessible for initial configuration. You can choose from a number of compatible applications: **Electrum**, **Phoenix**, **Zeus**, **Muun**, etc.


For the demonstration, we'll use **Electrum**. Open **Electrum**, click on **Portfolio**, then on **Information** :


![capture](assets/fr/20.webp)


Next, copy the **master public key (xpub)**.


![capture](assets/fr/21.webp)


Once you've copied the master public key, paste it into the field provided on the BTCPay Server page.


![capture](assets/fr/22.webp)


After verification, you will be redirected to your store's dashboard.


![capture](assets/fr/23.webp)


### Generate a Point of Sale (PoS)


Once you've set up your store and portfolio, you can now set up a **Point of Sale (PoS)** to start receiving Bitcoin payments directly from your customers.


This integrated feature of **BTCPay Server** is ideal for **merchants, craftsmen, restaurateurs or service providers** wishing to accept Bitcoin **without a website** or special technical skills.


### What's the point of sale?


The **PoS** is a **simplified POS interface** that acts as a **Bitcoin payment terminal**.

It allows you to :


- Create a **menu of products or services** with fixed prices.
- Generate an **instant invoice with QR code** to scan.
- Share a **Payment URL** accessible via smartphone, tablet or computer.


In other words, PoS turns your BTCPay Server into a **direct sales interface**, where every payment is received **in your own Bitcoin wallet**, with no intermediaries.


### Configuring PoS


In the BTCPay dashboard, click on **PLUGINS**, then on **Point of sale**.


Then click on **Create a new PoS application**. This action adds a **new application** to your BTCPay store, as if you were installing a mini internal sales site.


A page opens to create your application. Define a **application name**: this is an internal name, visible only from your dashboard (e.g. _Shoe Shop_).


Click on **Create** to validate.


![capture](assets/fr/24.webp)


Once created, you will be redirected to the **Detailed configuration page** of the Point of Sale.


### Customize your sales interface


On this page, you can define the essential elements of your PoS:



- Application name** (internal management name, can be changed at any time).



- Display title** (what your customers will see at the top of the page).



- Point of sale style** (**Description** mode is suitable for services such as haircuts or meals, while **Product catalog** mode is ideal for stores offering several items).



- Display currency** (choose **XOF**, **EUR** or **USD** according to your usual prices).



- Product list** (add your products, descriptions and prices here).


![capture](assets/fr/25.webp)


![capture](assets/fr/26.webp)


### Save and test your PoS


When you've finished configuring, click **Save** to save your settings, then **View** to preview your PoS.


You'll see a page presenting your products, with each button corresponding to an item or service.


As soon as a customer selects a product :


1. BTCPay automatically generates a Bitcoin or Lightning** invoice.


2. A **QR code** appears on the screen.


3. Customers can **scan and pay directly** with their Bitcoin wallet.



![capture](assets/fr/27.webp)


### Final result


You now have a complete **Bitcoin Point of Sale** that you can :



- Open from a smartphone or tablet in your store ;



- Display on a screen for the customer to scan ;



- Or share via a public **URL**, like a simplified order page.


With each payment, the amount is automatically credited to **your own BTCPay wallet**, without intermediaries or third-party fees.

This turns your PoS into a **stand-alone Bitcoin payment terminal**.



## Everyday use


Before cashing out any real payments, we recommend you carry out **a test** to check that everything is working properly.


### Test a payment



- Create an invoice** from your PoS interface (for example, a 1 satoshi product or a small amount).



- Scan the on-screen QR code** using a Bitcoin or Lightning wallet (such as **Phoenix**, **Muun** or **Wallet of Satoshi**).



![capture](assets/fr/28.webp)



- Validate the payment** in your wallet: the transaction is sent instantly.



- Return to BTCPay Server**: the invoice will appear as **Paid** in the list.


![capture](assets/fr/29.webp)


Congratulations! Your Point of Sale is now **functional**. You can start receiving Bitcoin payments from your customers, simply, quickly and without intermediaries.


### Create an invoice for a customer


In the **Invoices** menu, click on **New invoice**.


![capture](assets/fr/30.webp)


Enter the **amount** and the **local currency** (BTCPay automatically calculates the equivalent in BTC), as well as other product information.


![capture](assets/fr/31.webp)


Share the **QR code** or **URL** with the customer.


![capture](assets/fr/32.webp)


### Track payments received


Still in the **Invoices** menu, you'll see a list of all your transactions.

The possible statuses are :



- Pending**: payment not yet confirmed.



- Paid**: payment confirmed.



- Expired**: invoice not paid by the due date.


### Refunding a customer


In the **Invoices** menu, select the invoice to be reimbursed.


![capture](assets/fr/33.webp)


Click on **Refund** and enter the Bitcoin address provided by the customer.


![capture](assets/fr/34.webp)


![capture](assets/fr/35.webp)


### Reports and data export


BTCPay Server lets you **export your transactions** (in CSV or Excel format). This is very practical for your accounting and cash register follow-up.


![capture](assets/fr/36.webp)


In the **Report** menu, click on **Export**: all your transactions will be saved in a CSV file, which you can then consult locally.


## Safety and best practices


The autonomy conferred by BTCPay Server (full sovereignty over your funds) is a real strength. But with this freedom comes greater responsibility in terms of security. By managing your own payments, you take on the role of your own bank. That's why it's imperative to adopt best practices to protect your funds, your data and your infrastructure. Here are the main points to consider.


### Secure access to your server



- Use a strong password: combine upper and lower case letters, numbers and special characters. Avoid reusing an existing password.
- Activate two-factor authentication (2FA) to access your BTCPay interface.
- Regularly update your operating system, your BTCPay Server instance and your dependencies (Docker, Bitcoin node, Lightning node...). Updates often correct security vulnerabilities.


### Managing and backing up private keys



- Save your private keys and seedphrases offline, on physical media (paper or metal).
- Preferably use a wallet hardware wallet.
- Keep several copies of your backups, in separate, protected physical locations.


### Secure payments and confidentiality



- Use the Tor network or a VPN to hide your server's IP address and protect your privacy.
- Disable unnecessary ports on your server and restrict SSH connections to trusted addresses only.
- Activate HTTPS (SSL certificate) for all connections to your BTCPay web interface.
- Never share your administration interface with personnel not trained in Bitcoin portfolio management.


### Implementing best practices for the Lightning network


Your store is connected to a **Lightning node hosted on Voltage**, which considerably simplifies the technical management of the network. Nevertheless, it remains important to adopt **good monitoring and security practices**:



- Save your Voltage node's API** login and access keys (which enable BTCPay to connect).
- Protect your Voltage account** with two-factor authentication and a strong password.
- Monitor node and channel status** from your Voltage dashboard: this helps you spot any anomalies or desynchronization.
- Avoid sharing your API** credentials or exposing them publicly (e.g. in site code).
- In the event of migration, simply **reconfigure the link between BTCPay and Voltage**: no channel needs to be closed manually.


With Voltage, you benefit from a **secure, highly available** and **automatically backed-up** infrastructure, while retaining **full sovereignty over your Lightning payments**.


### Organize and structure internal procedures



- Define a clear access management policy: who can create an invoice, view payments, access the node, etc.
- Document your backup and restore procedures so you can react quickly in the event of an incident.
- Regularly test the restoration of your backups to make sure they're working properly.
- Train your staff or collaborators in basic operational security: vigilance against phishing, use of secure passwords, respect for confidentiality.


### Supervise and establish ongoing maintenance



- Continuously monitor your server's activity using logging or monitoring tools.
- Schedule a periodic security review: check updates, access, backups and transaction consistency.


Congratulations! You've reached the end of this tutorial. You can now get to grips with BTCPay Server on your own, making it easier for you to manage your store.


To find out more, I recommend you take our complete training course on integrating Bitcoin into your company:


https://planb.academy/courses/a804c4b6-9ff5-4a29-a530-7d2f5d04bb7a