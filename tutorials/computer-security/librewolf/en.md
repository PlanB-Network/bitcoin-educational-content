---
name: LibreWolf
description: How to use the LibreWolf privacy browser
---

![cover](assets/cover.webp)


Every click, every search, every site visited: your web browser has become a sophisticated snitch feeding a global commercial surveillance system. Google Chrome, used by over 3 billion people, turns your daily browsing into lucrative data for the advertising giants. Even Firefox, despite its reputation as an "ethical" browser, activates telemetry mechanisms by default that transmit your browsing habits to Mozilla.


This reality raises an essential question: is it still possible to browse freely on the Internet without being constantly spied on and profiled? Fortunately, the answer is yes, thanks to community projects that put the user back at the center of their concerns.


LibreWolf embodies this philosophy of digital resistance. The brainchild of a community of independent developers, this browser transforms Firefox into a veritable shield against online surveillance. Where commercial browsers seek to monetize your attention, LibreWolf does the opposite: making you invisible to trackers while preserving a fluid, modern browsing experience.


In this tutorial, we'll discover how LibreWolf can transform the way you surf the web, offering robust protection against tracking without sacrificing performance or web compatibility.


![LIBREWOLF](assets/fr/01.webp)

*Web browser market share: Chrome dominates with 65% of the market, followed by Safari and Edge. This domination raises questions about web diversity and privacy*


## Introducing LibreWolf


**FreeWolf** is an open-source web browser derived from Mozilla Firefox, developed and maintained by an independent community of free software enthusiasts. Its main objective is to offer browsing focused on the user's privacy, security and freedom.


In concrete terms, LibreWolf uses Firefox's Gecko engine, but with a radically different philosophy: where Firefox has to balance privacy and ease of use, LibreWolf opts for privacy by default. The project removes anything that might infringe on your privacy (telemetry, data collection, sponsored modules) while integrating enhanced security settings.


### Objectives: privacy and freedom


LibreWolf aims to maximize protection against tracking and fingerprinting while enhancing browser security. Its main objectives include:



- Eliminate all telemetry and data collection** in Firefox
- Disable functions that run counter to user freedom**, such as proprietary DRM modules
- Apply privacy/security settings** and specific patches from the outset
- Community development guarantees transparency and independence** from commercial interests


In short, LibreWolf presents itself as "Firefox as it would have been if privacy were top priority" - a browser that respects you by default, with no additional configuration required.


### Main features


Right from the start, LibreWolf offers a range of privacy-oriented features:


**No telemetry or data collection:** Unlike Chrome or Firefox, which send certain usage statistics, LibreWolf collects absolutely nothing from your browsing. No crash reports, no user studies, no sponsored suggestions.


**LibreWolf natively integrates the uBlock Origin extension, one of the best ad blockers and trackers on the market. By default, LibreWolf aggressively filters out anything that might track you online (intrusive ads, tracking scripts, cryptocurrency Mining).


**Private search engine by default:** LibreWolf defaults to DuckDuckGo as its initial search engine, which retains no history of your queries. Other privacy-oriented alternatives (Searx, Qwant, Whoogle) are also available.


**Reinforced anti-fingerprint protection:** Fingerprinting allows a browser to be uniquely identified via its configuration, even without cookies. To counter this, LibreWolf activates RFP (Resist Fingerprinting) technology from the Tor project, to make your browser as generic as possible. Tests show that a standard Firefox is ~90% unique on tools such as coveryourtracks.eff.org, compared with only ~10-20% for LibreWolf (these figures are indicative and may vary according to software and hardware configuration and installed extensions).


![LIBREWOLF](assets/fr/07.webp)

*EFF test page [Cover Your Tracks](https://coveryourtracks.eff.org/) with the TEST YOUR BROWSER button. This page is used to evaluate protection against trackers and fingerprinting


![LIBREWOLF](assets/fr/08.webp)

*Cover Your Tracks test result. The message "you have strong protection against Web tracking" is displayed, showing the effectiveness of LibreWolf.* protection


**LibreWolf activates strict security settings by default. Firefox's Enhanced Tracking Protection is pushed to the Strict level to block thousands of trackers, third-party cookies and malicious content. It also activates site and cookie isolation (*Total Cookie Protection*) to partition data for each domain, and restricts WebRTC (limiting *ICE candidates* and routing via proxy when a proxy is present) to reduce the risk of IP address leakage.


**Fast engine updates:** The project follows Firefox developments very closely: LibreWolf is always based on the latest stable version of Firefox, and the maintainers strive to release a new version within 24 to 72 hours of each official Firefox release.


## Advantages and disadvantages


### Benefits



- No telemetry or unwanted connections:** LibreWolf transmits no usage data, ensuring total respect for your privacy.



- Open-source and community-based:** The project is 100% open-source and maintained by volunteers. This independence guarantees that no advertising model will influence development.



- Pre-configured for privacy:** LibreWolf saves you precious time: there's no need to spend hours hardening Firefox settings, everything's already done.



- Native ad blocker/tracker:** uBlock Origin is integrated as standard, so you don't have to do a thing to protect yourself against ads and bugs.



- Excellent anti-fingerprinting protection:** Thanks to RFP and numerous privacy settings, LibreWolf drastically reduces your unique digital footprint on the web.



- Improved performance and light weight:** By removing telemetry and certain non-essential features, LibreWolf can be slightly faster and less power-hungry than standard Firefox.


### Disadvantages and limitations



- No built-in automatic updates:** LibreWolf does not update itself. It's up to you to install new versions as soon as they're released, to stay safe.



- Reduced compatibility with certain services:** Due to its very strict settings, LibreWolf may encounter problems on certain websites. Netflix and Disney+ streaming platforms will not work, as LibreWolf disables Widevine DRM by default.



- No built-in anonymous network:** Unlike Tor Browser, LibreWolf does not route traffic via Tor or a VPN on its own. If you need network anonymity, you'll need to manually configure a proxy/VPN.



- Non-persistent cookies and sessions (default):** For reasons of confidentiality, LibreWolf deletes cookies, history and site data each time you close your browser. You will need to log in to your accounts again each time you log in.



- No mobile version or cloud synchronization:** LibreWolf is only available on the desktop (Windows, Linux, macOS). There is no mobile application, and therefore no synchronization of accounts or bookmarks via a cloud.


## Installing LibreWolf


**Official website:** [librewolf.net](https://librewolf.net)


LibreWolf is available for all major desktop operating systems: Linux, Windows and macOS. To download LibreWolf, visit the official website:


![LIBREWOLF](assets/fr/02.webp)

*LibreWolf home page (librewolf.net) showing the browser logo, a blue Install button, and the Source Code and Documentation links. A large blue arrow points to the Install button*


Click on the "Installation" button to access detailed instructions for your operating system:


![LIBREWOLF](assets/fr/03.webp)

*Operating system selection page for LibreWolf.* download


Installation differs depending on your OS:


### On Linux

LibreWolf offers builds for many distributions. On Debian/Ubuntu and derivatives, an official APT repository is available. Alternatively, LibreWolf is published in Flatpak on Flathub:

```
flatpak install flathub io.gitlab.librewolf-community
```


### On Windows

Download the installer (.exe) from the official website or use the:


- Chocolatey:** `choco install librewolf`
- WinGet:** `winget install librewolf`


### On macOS

LibreWolf is available as a .dmg package for Mac. Download the disk image from the official website and drag and drop the LibreWolf application into your Applications folder. Alternatively, you can install it via Homebrew.



## Configuration and first use


On first startup, you'll notice the familiar Firefox Interface, except that it's more stripped down: the home page contains only the search bar and no sponsored suggestions. You'll see the uBlock Origin icon in the toolbar - a sign that the blocker is active.


![LIBREWOLF](assets/fr/04.webp)

*LibreWolf home page with extensions and menu. A blue arrow in the top right corner indicates the menu icon (three horizontal bars)


LibreWolf automatically loads your pages in "strict" (anti-tracking) mode, and the default search engine will be DuckDuckGo. You can try visiting a tracking test site (e.g. amiunique.org) to observe the exposed footprint - it should be much more generic than with a standard browser.


### Privacy settings


LibreWolf is already optimally configured for privacy. In Menu → Options → Privacy & Security, you'll see that LibreWolf is set to Enhanced Tracking Protection mode: Strict. This mode blocks:


- Inter-site trackers
- Third-party cookies
- Known tracking content
- Cryptomining
- Digital fingerprint detectors


![LIBREWOLF](assets/fr/05.webp)

*Security and privacy tab page showing LibreWolf.* security settings


WebRTC is disabled (preventing IP leaks), and Total Cookie Protection is in place. Telemetry and Firefox surveys are fully disabled.


### Cookie and history management


By default, LibreWolf deletes cookies and local storage each time it closes. If this behavior bothers you, you can adjust it in Privacy & Security → Cookies and site data by unchecking "Delete cookies and site data when closing LibreWolf".


![LIBREWOLF](assets/fr/06.webp)

*Same page a little further down, showing the option to delete cookies when the browser is closed*


### Adding useful extensions


As a matter of principle, LibreWolf discourages the addition of unnecessary extensions, as each extension can be a tracking vector. Nevertheless, some reputable extensions can enhance your experience:


- Firefox Multi-Account Containers** (by Mozilla) for compartmentalized browsing
- Decentraleyes** or **LocalCDN** to serve common libraries locally


Especially avoid "free VPN" extensions or dubious proxies - uBlock Origin already covers 99% of your needs.


## Everyday use


### Daily web browsing

Use LibreWolf for your day-to-day Internet activities. The major difference with other browsers is that you leave far fewer advertising traces. Accept cookie" banners disappear on many sites, thanks to uBlock's filtering lists.


### Use private tabs to compartmentalize

Even though LibreWolf deletes everything at the end of the session, it can be useful to open a private browser window (Ctrl+Shift+P) for certain tasks during the session, in order to partition off a specific identity.


### Take advantage of multi-account containers

Installing the Multi-Account Containers extension can greatly help you segment your activities into watertight silos. For example, you can define a "Banking" container for your banking sites, a "Social Networks" container for Facebook/Twitter, etc. Each container has its own cookies, sessions and isolated storage. Each container has its own cookies, sessions and isolated storage.


### Fine-tuned permissions management by site

LibreWolf lets you control the permissions you give to sites (Location, Camera, Microphone, Notifications) on a case-by-case basis. Grant permissions only to sites you trust and where necessary.


## Best practices with LibreWolf


1. **Keep LibreWolf up to date:** Check the site regularly for new versions, especially after a stable Firefox release.


2. **Avoid mixing personal identity and private browsing:** Ideally, you should not log in with your personal accounts on the same session where you are doing sensitive research.


3. **Don't overload LibreWolf with superfluous extensions:** Every extension you install may introduce security or fingerprinting risks.


4. **Use a VPN or Tor proxy in addition:** LibreWolf does not make you anonymous to your ISP. For network anonymity, you can use LibreWolf behind a trusted VPN.


5. **Save your important data:** Bookmarks, passwords if stored locally. Consider an external password manager (KeePassXC, Bitwarden) rather than the browser's basic password manager.


## Comparison with other browsers


LibreWolf is part of the "toolbox" of privacy-oriented browsers:


**LibreWolf vs. Firefox:** LibreWolf arrives already hardened and without any telemetry. Firefox retains the advantage of multi-device synchronization and a very large user base, but requires manual configuration to achieve LibreWolf's level of confidentiality.


**Brave uses Chrome/Chromium code and integrates a business model via its optional advertising program. LibreWolf, being a community Fork for Firefox, retains Mozilla's free ecosystem and has no ties to Google.


**LibreWolf vs Tor Browser:** Tor Browser is irreplaceable for anonymity in the face of powerful surveillance, but it's slow and uncomfortable in everyday use. LibreWolf, for everyday browsing on the classic web, is much faster and more practical.


**LibreWolf vs Mullvad Browser:** Mullvad Browser goes even further in standardization, but at the cost of reduced usability (impossible to keep a login cookie). LibreWolf strikes a balance: very private, but usable on a daily basis.


## Conclusion


LibreWolf represents an excellent solution for those looking for an ultra-private "everyday" browser without going as far as the extreme anonymity of Tor. It's an ideal choice for activists, journalists, developers or power users who want classic web browsing (fast, compatible with modern sites) while escaping ad tracking and Big Tech.


Although it has certain limitations (no automatic updates, reduced compatibility with certain services), LibreWolf is a valuable tool in the arsenal of anyone wishing to regain control of their digital privacy. Its ease of use and default configuration make it a wise choice for privacy-conscious users.


## Resources


### Official documentation


- [LibreWolf official website](https://librewolf.net)
- [Source code on Codeberg](https://codeberg.org/librewolf)
- [Official FAQ](https://librewolf.net/docs/faq)


### Guides and comparisons


- [Privacy Guides](https://www.privacyguides.org/en/desktop-browsers/)
- [Comparative privacy tests](https://privacytests.org)


### Community support


- [Subreddit r/LibreWolf](https://www.reddit.com/r/LibreWolf/)
- [Canal Matrix LibreWolf](https://matrix.to/#/#librewolf:matrix.org)