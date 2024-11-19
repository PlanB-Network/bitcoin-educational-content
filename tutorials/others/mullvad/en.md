---
name: Mullvad VPN
description: Setting up a VPN paid for with bitcoins
---
![cover](assets/cover.webp)

A VPN ("*Virtual Private Network*") is a service that establishes a secure and encrypted connection between your phone or computer and a remote server managed by a VPN provider.

Technically, when connecting to a VPN, your internet traffic is redirected through an encrypted tunnel to the VPN server. This process makes it difficult for third parties, such as Internet Service Providers (ISPs) or malicious actors, to intercept or read your data. The VPN server then acts as an intermediary that connects to the service you wish to use on your behalf. It assigns a new IP address to your connection, which helps to hide your real IP address from the sites you visit. However, contrary to what some online advertisements may suggest, using a VPN does not allow you to browse the internet anonymously, as it requires a level of trust in the VPN provider who can see all your traffic.
![MULLVAD VPN](assets/fr/01.webp)
The benefits of using a VPN are numerous. Firstly, it preserves the privacy of your online activity from ISPs or governments, provided that the VPN provider does not share your information. Secondly, it secures your data, especially when you are connected to public Wi-Fi networks, which are vulnerable to MITM ("**man-in-the-middle**") attacks. Thirdly, by hiding your IP address, a VPN allows you to bypass geographical restrictions and censorship, to access content that would otherwise be unavailable or blocked in your region.

As you can see, the VPN shifts the risk of traffic observation to the VPN provider. Therefore, when choosing your VPN provider, it is important to consider the personal data required for registration. If the provider asks for information such as your phone number, email address, bank card details, or worse, your postal address, the risk of associating your identity with your traffic increases. In the event of a compromise of the provider or a legal seizure, it would be easy to associate your traffic with your personal data. Therefore, it is recommended to choose a provider that does not require any personal information and accepts anonymous payments, such as with bitcoins.

In this tutorial, I will present a simple, efficient, reasonably priced VPN solution that requires no personal information for its use.

## Introduction to Mullvad VPN
Mullvad VPN is a Swedish service that stands out for its commitment to user privacy. Unlike mainstream VPN providers, Mullvad requires no personal data at sign-up. There's no need to provide an email address, phone number, or name; instead, Mullvad assigns you an anonymous account number used for payment and accessing the service. Additionally, Mullvad claims to keep no activity logs that pass through their servers.
![MULLVAD VPN](assets/notext/02.webp)
For payment, it's not necessarily required to provide credit card information, as Mullvad accepts bitcoin payments (onchain only on their official site, but there is an unofficial method to pay via Lightning). They also accept cash payments through the mail.

Mullvad VPN also distinguishes itself through its transparency and security. Their software is open-source, and they regularly undergo independent security audits to assess their applications and infrastructure, the results of which are [published on their website](https://mullvad.net/fr/blog/tag/audits). The company behind Mullvad is based in Sweden, a country known for its strict privacy laws. They exclusively use self-hosted servers, thereby eliminating the risks associated with using third-party cloud services, such as hyperscalers AWS, Google Cloud, or Microsoft Azure.

In terms of features, Mullvad offers everything one expects from a good VPN client, including a kill switch that protects your traffic if the VPN disconnects, an option to disable the VPN for specific applications, and the ability to route your traffic through multiple VPN servers.

Naturally, this quality of service comes at a cost, but a fair price is often an indicator of quality and honesty. It can signal that the company has a business model without needing to sell your personal data to third parties. Mullvad VPN offers a flat rate of 5 euros per month, usable on up to 5 different devices.
![MULLVAD VPN](assets/notext/03.webp)
Unlike mainstream VPN providers, Mullvad has a model of purchasing access time to the service rather than a recurring, automatic subscription. You simply make a one-time payment in bitcoins for the chosen duration. For example, if you buy one year of access, you can use the service for that period, after which you must return to Mullvad's website to renew your access time.
Compared to IVPN, another high-quality VPN provider, Mullvad is slightly more economical. For instance, even when opting for a three-year purchase with IVPN, the monthly cost amounts to about €5.40. However, IVPN does offer some additional services and also has a cheaper plan than Mullvad's (the Standard plan), but this is limited to only 2 devices and excludes the "multi-hop" protocol.
I also conducted some informal speed tests to compare IVPN and Mullvad. Although IVPN showed a slight superiority in terms of performance, the speeds at Mullvad were still very satisfactory. Compared to mainstream VPN providers, IVPN and Mullvad proved to be at least as efficient, if not superior in some cases.

## How to install Mullvad VPN on a computer?

Visit the [official Mullvad website](https://mullvad.net/en/download/) and click on the "*Downloads*" menu.
![MULLVAD VPN](assets/notext/04.webp)
For Windows or macOS users, download the software directly from the site and follow the instructions provided by the setup wizard to complete the installation.
![MULLVAD VPN](assets/notext/05.webp)
For Linux users, you can find the instructions specific to your distribution in the ["*Linux*"](https://mullvad.net/en/download/vpn/linux) section.
![MULLVAD VPN](assets/notext/06.webp)
Once the installation is complete, you will need to enter your account ID. We will see how to obtain this in the following sections of this tutorial.

## How to install Mullvad VPN on a smartphone?

Download Mullvad VPN from your app store, whether it's the [AppStore](https://apps.apple.com/us/app/mullvad-vpn/id1488466513) for iOS users, the [Google Play Store](https://play.google.com/store/apps/details?id=net.mullvad.mullvadvpn) for Android, or [F-Droid](https://f-droid.org/packages/net.mullvad.mullvadvpn/). If you are using Android, you also have the option to download the `.apk` file directly from [the Mullvad site](https://mullvad.net/en/download/vpn/android).
![MULLVAD VPN](assets/notext/07.webp)
Upon first use of the app, you will be logged out. You will need to enter your account ID to activate the service.
![MULLVAD VPN](assets/notext/08.webp)
Now, let's move on to activating Mullvad on your devices.

## How to pay for and activate Mullvad VPN?

Go to the [official Mullvad website](https://mullvad.net/) and click on the "*Get Started*" button.
![MULLVAD VPN](assets/notext/09.webp)
Click on the "*Generate account number*" button.
![MULLVAD VPN](assets/notext/10.webp)Mullvad will then create your account. You do not need to provide any personal information. It is only your account number that will allow you to log in. It acts somewhat like an access key. Save it in a safe place like your password manager, for example. You can also make a paper copy.
![MULLVAD VPN](assets/notext/11.webp)
Then click on the "*Add time to your account*" button.
![MULLVAD VPN](assets/notext/12.webp)
You will then arrive at the login page for your account. Enter your account number and then click on the "*Log in*" button.
![MULLVAD VPN](assets/notext/13.webp)
Choose your payment method. I recommend paying in bitcoins, as you will benefit from a 10% discount, which brings the cost down to €4.50 per month. If you prefer to pay via Lightning, I will provide an alternative method in the following part.
![MULLVAD VPN](assets/notext/14.webp)
Click on the "*Create a one-time payment address*" button.
![MULLVAD VPN](assets/notext/15.webp)
Then pay with your Bitcoin wallet the amount indicated to the receiving address given to you.
![MULLVAD VPN](assets/notext/16.webp)
It may take a few minutes before the site detects your payment, once the transaction is confirmed. Once the payment is detected by Mullvad, the duration of your subscription will appear at the top left of the page, instead of the mention "*No time left*".
![MULLVAD VPN](assets/notext/17.webp)
You can then enter your account number on the software to activate the VPN.
![MULLVAD VPN](assets/notext/18.webp)
To activate the VPN on your mobile application, the process is exactly the same. You just need to enter your account number.
![MULLVAD VPN](assets/notext/19.webp)
## How to pay for Mullvad VPN with Lightning?

As you have understood, Mullvad does not yet accept payments via the Lightning Network. However, thanks to a recommendation from [Lounès](https://x.com/louneskmt), I discovered an informal service that allows you to bypass this limitation. This service, available on [vpn.sovereign.engineering](https://vpn.sovereign.engineering/), accepts your payments on Lightning and provides you with a valid plan for Mullvad in return.
![MULLVAD VPN](assets/notext/20.webp)
You have 2 different options on this site: you can trust the site manager and enter your account number directly, then click on "*Log in*" for your Mullvad package to be automatically validated. Or, you can click on the "*Heck yeah!*" button to buy a Voucher in Lightning, which you can then use on the official Mullvad site to get your package. ![MULLVAD VPN](assets/notext/21.webp) In both cases, you will then be asked to select the duration of your package. You can choose between 6 months and 1 year. ![MULLVAD VPN](assets/notext/22.webp) Then click on the "*Top-up with Lightning*" button. ![MULLVAD VPN](assets/notext/23.webp) To finalize the purchase, pay the invoice with your Lightning wallet. ![MULLVAD VPN](assets/notext/24.webp) If you opted to buy a Voucher, on the Mullvad site, select "*Voucher*" among the payment methods available on your account. Then, enter the Voucher number you received from the vpn.sovereign.engineering site in the designated box. ![MULLVAD VPN](assets/notext/25.webp) ## How to use and configure Mullvad VPN?

Now that you have an active account and have entered your account number in the Mullvad software or app, you can fully enjoy the services of your VPN. ![MULLVAD VPN](assets/notext/26.webp) To disconnect from the VPN, simply click on the "*Disconnect*" button. ![MULLVAD VPN](assets/notext/27.webp) The small red arrow next to the "*Disconnect*" button allows you to change servers without changing the current location. ![MULLVAD VPN](assets/notext/28.webp) If you want to change cities for your VPN server, click on "*Switch location*" to choose a new location. ![MULLVAD VPN](assets/notext/29.webp) At the top of the screen, you will see your device's nickname as well as the remaining duration of your package. ![MULLVAD VPN](assets/notext/30.webp) By clicking on the icon of the little man, you will access detailed information about your account. ![MULLVAD VPN](assets/notext/31.webp) To access settings, click on the gear wheel. ![MULLVAD VPN](assets/notext/32.webp) In the "*User interface settings*" menu, you can customize the settings of your software, including the interface language and its behavior on your system. ![MULLVAD VPN](assets/notext/33.webp) In the "*VPN settings*" menu, you will find options related to your VPN. I recommend enabling the "*Launch app on start-up*" and "*Auto-connect*" options so that your VPN connection automatically launches when your machine starts.
![MULLVAD VPN](assets/notext/34.webp) In the "*DNS content blockers*" submenu, you have the option to filter and block DNS requests to malicious, advertising, or unwanted websites.
![MULLVAD VPN](assets/notext/35.webp)
Finally, the "*Split tunneling*" menu allows you to select specific applications on your machine for which internet traffic will not be routed through the VPN.
![MULLVAD VPN](assets/notext/36.webp)
To get an overview of your Mullvad account and manage the various connected devices, you can click on the "*Devices*" menu on the website.
![MULLVAD VPN](assets/notext/37.webp)
And there you have it, you are now equipped to fully enjoy Mullvad VPN. If you're interested in discovering another VPN provider similar to Mullvad, both in terms of features and pricing, I also recommend checking out our tutorial on IVPN:

https://planb.network/tutorials/others/ivpn