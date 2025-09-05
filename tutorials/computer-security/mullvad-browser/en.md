---
name: Mullvad Browser
description: How to use the Mullvad Browser for privacy
---

![cover](assets/cover.webp)


In a world where digital surveillance is becoming ubiquitous, protecting your online privacy has never been more crucial. Companies use sophisticated techniques to track you:



- Third-party cookies**: small files deposited by external sites to follow you from one site to another
- Fingerprinting**: collects unique characteristics of your browser and device (screen resolution, installed fonts, plugins, etc.) to identify you without cookies
- Tracking scripts**: invisible JavaScript codes that analyze your browsing behavior (clicks, scrolling, time spent)
- IP address analysis**: geographical location and identification of your Internet service provider


This data is then combined to create detailed profiles of your online behavior and monetized, often without your knowledge. This reality raises a fundamental question: how can you surf the Internet while preserving your anonymity and confidentiality?


The answer lies largely in your choice of web browser. This tool, which we use every day to access information, make purchases or communicate, plays a decisive role in protecting our personal data. Unfortunately, popular browsers such as Google Chrome (which holds around 65% of the global market) are designed around business models based on the massive collection of user data.


![MULLVAD BROWSER](assets/fr/01.webp)

*Mullvad Browser stands out for its exceptionally effective tracker blocking, far surpassing consumer browsers*


Faced with this challenge, new players are emerging with a different philosophy: that of placing privacy at the heart of their design. Among them, Mullvad Browser stands out as an innovative solution that combines the best privacy protections with a fluid, accessible browsing experience.


Unlike traditional browsers that seek to personalize your experience by collecting your data, Mullvad Browser takes the opposite approach: making all its users appear identical to websites, thus making individualized tracking virtually impossible.


In this tutorial, we'll discover together how Mullvad Browser can transform the way you browse the Internet, offering you robust protection against surveillance without sacrificing ease of use.



## Introducing Mullvad Browser


**Mullvad Browser** is a privacy-focused web browser developed in collaboration with the Tor Project and distributed free of charge by Swedish company Mullvad VPN. Launched in April 2023, it presents itself as a **"Tor Browser without the Tor network "**, designed to minimize online tracking and fingerprinting while allowing users to browse via a trusted VPN rather than the Tor network.


Mullvad Browser is a free, open-source browser based on Firefox ESR (the long-lasting version of Mozilla Firefox) and hardened by Tor Project experts. In concrete terms, it includes most of the **protection features of Tor Browser**, but **does not route traffic via the Tor network**. Instead, users can (and should) link it to a trusted encrypted VPN to anonymize their IP address.


In terms of user experience, Mullvad Browser resembles a classic browser, offering fluid navigation. It is available free of charge on Windows, macOS and Linux (no mobile version). You don't need to be a Mullvad VPN subscriber to use it; however, **using Mullvad Browser without masking your IP does not provide complete anonymity** - so it's highly recommended to use it in conjunction with a reliable VPN.


### Objectives: privacy and anti-tracking


The Mullvad browser has been designed with one main goal in mind: **protecting user privacy** online and countering common tracking and profiling techniques. Its main objectives include:



- Drastically reduce ad tracking and tracking** by websites and advertising agencies. By default, Mullvad Browser blocks third-party trackers, tracking cookies and fingerprinting scripts that could identify you.



- Standardize your browser's fingerprint** to **"blend in with the crowd "**. The fingerprint is like a unique "identity card" created by combining all the characteristics of your browser. Mullvad Browser ensures that all its users have exactly the same "identity card", making it impossible to distinguish them individually.



- Offering immediate protection without additional extensions**. Mullvad Browser comes in a "ready-to-use" configuration: the user doesn't need to install an array of extensions or modify any settings to be protected.



- Don't sacrifice performance or ergonomics** any more than necessary. In the absence of Tor routing, Mullvad Browser offers much faster browsing than Tor Browser, approaching the performance of a standard browser coupled with a VPN.


### Key Mullvad Browser features


Mullvad Browser includes a series of **security and privacy features** directly inspired by Tor Browser:



- Private browsing at all times:** Private browsing mode is activated by default and cannot be deactivated. **No history, cookies or cache is stored from one session to the next**. As soon as you close Mullvad Browser, all browsing data is deleted.



- Enhanced protection against fingerprinting:** The browser applies strict settings to thwart digital fingerprinting. This includes:
 - User agent** and browser version standardization
 - Time zone set to UTC** for all users
 - Letterboxing**: a technique that automatically adds gray margins around web pages to standardize display size and prevent identification by your screen dimensions
 - Block fingerprinting APIs**: Canvas (2D drawing), WebGL (3D graphics) and AudioContext (audio processing) technologies are disabled because they can reveal unique details about your hardware
 - Standardized system fonts** to avoid identification by installed fonts



- Blocking trackers and advertising:** Mullvad Browser natively integrates the **uBlock Origin** extension (pre-installed) with additional protection lists to block **third-party trackers, advertising scripts and other malicious content**. This protection is accompanied by **First-Party Isolation**: a technique that stores cookies in separate "pots" for each website, preventing one site from reading cookies deposited by another.



- Session reset button:** Like Tor Browser's "New Identity" button, Mullvad Browser offers a button for **quickly restarting the browser with a new, blank session**.



- Adjustable security levels:** You can adjust the security level (*Normal*, *Safer*, *Safest*) in the settings, just as in Tor Browser.


## Built-in extensions by default


Mullvad Browser includes **three pre-installed extensions** which form the core of its anti-tracking protection. **It is crucial never to remove them or modify their configurations**, as this would make you unique among Mullvad Browser users:


### **uBlock Origin**

This ad and tracker blocker extension comes pre-configured with **optimized filter lists** to block:


- Intrusive advertising
- Third-party trackers that collect your data
- Malicious scripts
- Behavioral tracking elements


uBlock Origin in Mullvad Browser uses standardized parameters to ensure that all users block exactly the same elements, thus preserving the uniformity of digital footprints.


### **NoScript**

NoScript runs in the background to manage the browser's **security levels**. This:


- Controls JavaScript** execution according to selected level (Normal/Most Secure/Most Secure)
- Filters out XSS** (Cross-Site Scripting) attacks automatically
- Blocks dangerous** active content on non-HTTPS sites
- Its icon is hidden by default, but can be displayed via "Customize toolbar"


### **Mullvad Browser** extension

This Mullvad-specific extension offers different functionalities depending on whether or not you are a Mullvad VPN customer:


#### **Without Mullvad VPN subscription:**


- Basic connection check**: displays your current public IP and some connection information
- Privacy recommendations**: tips for improving your security settings (DNS, HTTPS-only, search engine)
- WebRTC** control: enable/disable to prevent IP address leaks
- Can be deleted without impact** on your digital footprint if you don't use Mullvad VPN


#### **With Mullvad VPN subscription:**

The extension reveals its full potential with advanced features:



- Integrated SOCKS5 proxy**: one-click connection to Mullvad VPN server proxy
 - Fixed IP address**: unlike a VPN, which can change its IP address, a proxy always guarantees the same output address
 - Automatic kill switch**: if the VPN disconnects, browser traffic is immediately blocked
 - IPv6 support**: IPv6 connectivity even if your VPN connection doesn't have it enabled



- Multihop (double VPN)**: ability to change proxy location to create a tunnel within the tunnel
 - Your traffic first passes through your VPN server, then "jumps" to another Mullvad server
 - Use a different localization for the browser only



- Advanced connection monitoring**: real-time monitoring of your VPN status, connected server, and DNS leak detection



- Access to Mullvad Leta**: private search engine reserved for subscribers (although not recommended by Mullvad for reasons of correlation with your account)


These three extensions work together to create a coherent ecosystem of protection, where every user benefits from exactly the same defenses without the possibility of customization that would compromise collective anonymity.


## Advantages and disadvantages of Mullvad Browser


### Benefits



- Excellent privacy protection by default:** Mullvad Browser applies very strict privacy settings right from the start, with no need for manual configuration.



- Better performance than Tor Browser:** In the absence of onion routing, Mullvad Browser is **notably faster and more responsive** than Tor Browser for classic web browsing.



- Familiar Interface simplicity:** Mullvad Browser is based on Firefox's Interface. If you're used to Firefox or even Tor Browser, you won't feel out of place.



- Trusted collaboration and audited code:** Mullvad Browser benefits from the expertise of the Tor Project, and all source code is available for external auditing.


### Disadvantages



- No network anonymity without VPN:** The most important point is that **Mullvad Browser doesn't hide your IP address by itself** (like all other browsers, except Tor Browser). Your IP address is like your "postal address" on the Internet: it reveals your location and your ISP. It therefore **depends heavily on a VPN** (virtual private network) to hide this crucial information.



- No mobile version:** To date, Mullvad Browser is only available on PC (Windows, Mac, Linux).



- Incompatible with certain habits:** The **permanent private mode** means that you can't keep a session from one use to the next. It is impossible to remain connected to a web account from one session to the next.



- Restricted features:** To preserve fingerprint uniformity, Mullvad Browser has **disabled several features** present in Firefox and is not intended for customization.


## Installing Mullvad Browser


Mullvad Browser is available free of charge for Windows, macOS and Linux. To install it, go to [the official Mullvad website](https://mullvad.net/browser).


![MULLVAD BROWSER](assets/fr/02.webp)


*Official Mullvad Browser home page with download button highlighted.*


![MULLVAD BROWSER](assets/fr/03.webp)


*Select your operating system on the Mullvad Browser.* download page


Click on the **"Download "** button corresponding to your operating system.


For Linux, you can choose between different formats depending on your distribution. Once the download is complete:


### On Windows

Run the downloaded `.exe` file and follow the installation instructions.


### On macOS

Open the downloaded `.dmg` file and drag the Mullvad Browser application into your Applications folder.


### On Linux

Extract the `.tar.xz` archive into the directory of your choice and run the `start-mullvad-browser.desktop` file.


## Configuration and first use


When you first launch Mullvad Browser, you'll see a Interface very similar to that of Tor Browser. The browser is preconfigured for privacy and requires no special modifications.


![MULLVAD BROWSER](assets/fr/04.webp)


*Interface Mullvad Browser home page with extensions, broom icon to generate a new identity and application menu at top right.*


**Important:** Mullvad Browser does not mask your IP address by default. For complete protection, we strongly recommend using a VPN in parallel. You can use Mullvad VPN or any other trusted VPN service.


The browser also includes **DNS-over-HTTPS (DoH)** using Mullvad's DNS service: this technology encrypts your DNS requests (translating site names into IP addresses) to prevent your ISP from monitoring the sites you visit.


### Safety settings


You can adjust the security level by clicking on the **application menu** (three horizontal bars) at top right, then **"Settings "**, then the **"Privacy & Security "** tab. Scroll down to the **"Security "** section:


![MULLVAD BROWSER](assets/fr/05.webp)


*Choice of security levels: the arrows show the path from the application menu to the "Privacy & Security" tab to the security options*


Mullvad Browser offers three levels of security:



- Normal** (current default level): All browser and website functions enabled



- Safer**: Disables often dangerous website functions, which may lead to a loss of functionality on some websites:
 - JavaScript is disabled for non-HTTPS sites
 - Some fonts and mathematical symbols are disabled
 - Sound and video (HTML5 media) as well as WebGL are "click to play"



- The safest**: Allows only the website functions required for static sites and basic services:
 - JavaScript is disabled by default for all sites
 - Some fonts, icons, images and mathematical symbols are disabled
 - Sound and video (HTML5 media) as well as WebGL are "click to play"


### New session button


To restart with a blank session without closing the browser, click on the broom icon or use the application menu > **"New session "**.


![MULLVAD BROWSER](assets/fr/06.webp)


*Reset your identity" function to restart the browser with a completely new session*


## Everyday use


### Normal navigation


Mullvad Browser behaves like a classic browser for everyday browsing. All websites are accessible as usual, with the added benefit of enhanced protection against tracking.


### Cookie management and login


Because of the permanent private mode, you'll have to reconnect to your accounts each time you log on. This is the price you pay for maximum confidentiality.


### Extensions


Mullvad Browser technically allows you to install additional extensions from the Firefox catalog, but **it's important to understand the implications**. Each added extension changes your digital footprint and distinguishes you from other Mullvad Browser users, which goes against the browser's fundamental principle: to make all users appear identical.


As Mullvad explains: *"Sometimes, having no specific defense is better than having one. By wanting to increase online privacy, you install extensions that ultimately make you even more visible. "*


If you choose to install extensions anyway, be aware that you are creating a unique fingerprint that can be used to track you from site to site. For maximum protection, it's best to stick to the three pre-installed extensions, which are identical for all users.


## Best practices with Mullvad Browser


1. **Always use a VPN: Mullvad Browser does not mask your IP. A VPN is essential for complete anonymity.


2. **Don't customize the browser**: Avoid changing settings or adding extensions, as this could make you identifiable.


3. **Use the new session button**: Between different activities, use the reset function to partition your sessions.


4. **Choose the level of security that best suits your needs**:


   - Normal (recommended)**: For everyday browsing. Already offers excellent protection while keeping websites functional. This is the best balance for 95% of users.
   - Safer**: If you're visiting unknown or potentially dangerous sites, or for extra protection on public Wi-Fi networks. Some sites may malfunction.
   - Most secure**: Reserved for high-risk situations (investigative journalism, sensitive communications, hostile environments). Most modern sites will be broken, but that's the price of maximum security.


5. **Regularly check for updates**: Keep your browser up to date with the latest security patches.


6. **Use privacy-friendly search engines**: Choose DuckDuckGo, Startpage or Searx over Google.


7. **Enable HTTPS only mode**: In the settings, make sure that "HTTPS only" mode is enabled to force secure connections.


8. **Do NOT change any advanced settings**: Unlike other browsers, Mullvad Browser is designed so that ALL users have exactly the same configuration. Modifying settings in `about:config` or changing uBlock Origin/NoScript settings would make you unique and completely undo browser anonymity.


## Recommended DNS configuration


Mullvad Browser automatically integrates Mullvad DNS-over-HTTPS. If you're using Mullvad VPN, the extension will recommend that you **disable Mullvad DoH** as it's faster to use your VPN server's DNS server. If you're not using Mullvad VPN, keep Mullvad DoH enabled to avoid DNS monitoring by your ISP.


## Conclusion


Mullvad Browser is an excellent solution for those seeking privacy-friendly web browsing without the performance constraints of the Tor network. Combined with a quality VPN, it offers robust protection against online tracking and surveillance.


Although it has certain limitations (no mobile version, non-persistent sessions), Mullvad Browser is a valuable tool in the arsenal of anyone wishing to regain control of their digital privacy. Its ease of use and default configuration make it a wise choice for privacy-conscious users, whether beginners or experienced.


## Resources


### Official documentation


- [Official Mullvad Browser website](https://mullvad.net/fr/browser)
- [Mullvad Browser download page](https://mullvad.net/en/download/browser)
- [Detailed technical specifications](https://mullvad.net/en/browser/Hard-facts)
- [Mullvad Browser Extension](https://mullvad.net/en/help/mullvad-browser-extension)


### Guides and explanations


- [Why privacy matters](https://mullvad.net/en/why-privacy-matters/how-mass-surveillance-companies-collect-your-data)
- [Tor without Tor: Mullvad Browser concept](https://mullvad.net/en/browser/tor-without-tor)
- [How to choose a privacy-friendly browser](https://mullvad.net/en/browser/things-to-look-for-when-choosing-a-browser)
- [Understanding browser fingerprinting](https://mullvad.net/en/browser/browser-fingerprinting)


### Support and help


- [Mullvad Browser Help Center](https://mullvad.net/en/help/tag/mullvad-browser)
- [First steps to online privacy](https://mullvad.net/en/help/first-steps-towards-online-privacy)


### Community resources


- [Mullvad Browser Guide - Privacy Guides](https://www.privacyguides.org/en/desktop-browsers/)
- [Community discussions](https://discuss.privacyguides.net/t/about-changing-settings-in-mullvad-browser/18330)