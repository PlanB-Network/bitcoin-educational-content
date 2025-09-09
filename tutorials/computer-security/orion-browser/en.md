---
name: Orion Browser
description: How to use Orion Browser to protect your privacy on Mac and iPhone?
---

![cover](assets/cover.webp)


## Introduction


In a context where the majority of browsers massively collect our personal data, the choice of a privacy-friendly browser becomes crucial. Chrome dominates with 65% of the global market, but its business model is based on the exploitation of your browsing data. Safari, although integrated into the Apple ecosystem, lacks advanced protection features and does not flexibly support third-party extensions.


![Répartition du marché des navigateurs](assets/fr/01.webp)

*Web browser market breakdown: Chrome dominates with over 65% market share, followed by Safari, Edge and Firefox*


**Orion Browser** presents itself as an innovative alternative for Apple users. Developed by Kagi, this browser combines the speed of the WebKit engine with a zero telemetry philosophy. Unlike its competitors, Orion sends no data to remote servers and natively blocks 99.9% of ads and trackers, including YouTube.


Its unique feature? Orion is the **only WebKit** browser to natively install Chrome **and** Firefox extensions, offering the best of both worlds. This compatibility, combined with memory consumption 2 to 3 times lower than other browsers and seamless integration with the Apple ecosystem (iCloud, Keychain), makes it the ideal choice for privacy-conscious Mac and iPhone users.


## Why choose Orion Browser?


### Key benefits


**Maximum protection right out of the box**: Orion blocks 99.9% of ads (including YouTube) and all first-party and third-party trackers by default. Its technology combines WebKit's Intelligent Tracking Prevention with EasyPrivacy lists for maximum efficiency. Unique feature: Orion blocks fingerprinting scripts **before they are executed**, making tracking literally impossible - a more radical approach than other browsers which only attempt to "mask" data.


**Zero verifiable telemetry**: Orion takes a radical approach to privacy, with zero telemetry by design. Unlike other browsers, which make hundreds of network requests at start-up (IP exponent, browser fingerprint, personal information), Orion never "phone home". This fundamental difference completely eliminates the risk of unintentional data leakage.


**Exceptional performance**: Based on an optimized version of WebKit, Orion equals or even surpasses Safari in speed on the Mac. Speedometer 2.0/2.1 tests consistently place it first on Apple Silicon processors. Native ad blocking further accelerates page loading by 20 to 40%.


**Universal extension support**: A major innovation, Orion allows you to install extensions from the Chrome Web Store **and** Mozilla Add-ons. WebExtensions support is currently experimental, with a target of 100% compatibility at beta release. You can use many popular extensions like uBlock Origin, Bitwarden, even on iPhone - a world first on iOS, although some may not work perfectly.


### Limitations to be aware of



- Limited availability**: Currently reserved for macOS and iOS/iPadOS. A Linux version is reaching development milestones (Milestone 2 in 2025), but no public build is available. Windows and Android are not in development for lack of resources.
- Closed source code**: Although some components are open-source, Orion remains predominantly proprietary, a point of debate in the privacy community.
- Experimental extensions**: Extension support remains in beta, with frequent incompatibilities. Extensions can affect performance, and some don't work at all.
- WebKit security**: Unlike Chromium, WebKit doesn't offer such robust per-site process isolation, which can pose security risks in certain scenarios.
- Blocking tests**: Orion performs deliberately poorly in online advertising tests (26-35%), as Kagi considers these tests to be "fundamentally flawed". Actual effectiveness in everyday use is far superior.


## Orion Browser installation


### On macOS


![Page d'accueil Kagi avec Orion Browser](assets/fr/02.webp)

*Kagi homepage presenting Orion Browser as "an ad-free browser with total privacy protection and universal extension support "*



- Go to [kagi.com/orion](https://kagi.com/orion/)
- Click on "**Download Orion for macOS**"


![Page de téléchargement d'Orion Browser](assets/fr/03.webp)

*Orion Browser download page showing availability for macOS and iOS, with links to the App Store*



- Open the downloaded `.dmg` file
- Drag the Orion application into the Applications folder
- On first launch, macOS will ask you to confirm opening


**Alternative Homebrew**:

```bash
brew install --cask orion
```


### On iPhone/iPad



- Open the **App Store**
- Search for "**Orion Browser by Kagi**"
- Install the free app (iOS 15+ compatible)


### Initial configuration


On first launch, Orion guides you through several steps:


**1. Welcome screen

![Écran de bienvenue d'Orion](assets/fr/04.webp)

*Orion Browser welcome screen highlighting key features: faster browsing, zero telemetry, ad blocking and extension support*


**2. Interface** customization

![Options de personnalisation](assets/fr/05.webp)

*Customization screen lets you configure the appearance of tabs and the Interface to suit your preferences*



- Data import**: Easily transfer favorites and passwords from Safari, Chrome or Firefox
- ICloud sync**: Activate to find your favorites and tabs on all your Apple devices


**3. Installation on mobile devices**

![Installation sur iOS](assets/fr/06.webp)

*Installation screen on iOS showing the QR code to quickly download Orion Browser from the App Store*


**4. Interface welcome and essential tools


![Page d'accueil Orion](assets/fr/07.webp)

*Orion Browser Interface home page: the arrow indicates the three key tools accessible directly from the address bar*


Once the configuration is complete, you'll discover Orion's streamlined Interface with its **three essential tools** (indicated by the arrow):



- Shield 🛡️**: Displays Privacy Report with number of items blocked on current page
- Brush 🖌️**: Customize page display (theme, font, remove distracting elements)
- Gear ⚙️**: Configure website-specific parameters (permissions, blocking, etc.)


These tools are always available and allow you to control your browsing experience on a site-by-site basis.


**Important**: Orion is free and requires no registration or account creation to operate.


![Orion+ dans les préférences](assets/fr/08.webp)

*Orion+ subscription screen in preferences, offering an optional subscription to support development*


**Orion+ (optional)**: To support project development, Kagi offers Orion+ ($5/month, $50/year, or $150 lifetime). This voluntary subscription enables:


- Communicate directly with the development team
- Influence the browser's evolution according to your needs
- Access Nightly versions with the latest experimental features
- Benefit from the latest WebKit engine
- Get a distinctive badge on the feedback forum


Orion+ guarantees the project's independence: "Your financial contribution helps us remain independent and keep our promise to become the best browser for our users". It is this user-funding model that keeps Orion ad-free and telemetry-free.


## Configuration for maximum confidentiality


### Essential parameters


Access preferences via **Orion → Preferences** (or ⌘,):


**1. Search - Private search engine**


![Configuration du moteur de recherche](assets/fr/09.webp)

*Default search engine configuration: DuckDuckGo is selected for maximum privacy*



- Default engine**: Select **DuckDuckGo**, **Startpage** or **Kagi** for optimum privacy (avoid Google/Bing)
- Search suggestions**: Disable them to prevent keystrokes from leaking to search engine servers


**2. Privacy - General** protection


![Content Blocker dans les préférences](assets/fr/12.webp)

*Orion privacy settings showing Content Blocker with 119,156 active rules, tracker removal options and custom user agent*


**Content Blocker active by default**:


- EasyList**: 119k+ ad-blocking rules
- EasyPrivacy**: Protection against tracking
- Manage Filter Lists**: Add additional lists (Hagezi recommended)


**Privacy options**:


- Remove trackers from URLs**: "For Private Browsing only" cleans up copied links
- Share crash reports**: "After asking for approval" respects your consent
- Custom user agent**: Can be modified to bypass certain blockages


![YouTube avec Privacy Report](assets/fr/10.webp)

*Example of YouTube viewed with Orion: no advertising visible and Privacy Report showing the many elements blocked*


**3. Website Settings - Control by site**


![Website Settings pour YouTube](assets/fr/11.webp)

*Website Settings for YouTube showing compatibility options, content blocking and site-specific permissions*


**Quick access**: Click on the gear ⚙️ in the address bar to adjust:


- Compatibility Mode**: Solves display problems by suspending extensions
- Content Blockers**: Deactivate blocking for a specific site if necessary
- JavaScript/Cookies**: Granular control by site
- Permissions**: Camera, microphone, location individually configured


**4. Advanced Custom Filters** (see below)


**Create custom filters** (Privacy → Manage Filter Lists → Custom Filters):


**Simplified syntax** (Adblock Plus compatible):


- `reddit.com##.promotedlink`: Hides sponsored Reddit posts
- `||ads.example.com^`: Completely blocks an advertising domain
- `@@||site-utile.com^`: Creates an exception for a site


**Tip: Visit [FilterLists.com](https://filterlists.com) for thousands of ready-to-use specialized lists.


### Recommended extensions


Orion natively supports Chrome and Firefox extensions. Install them directly from the official stores:


**Essentials**:


- uBlock Origin**: Adds granular control to the native blocker
- Bitwarden**: Open-source password manager
- ClearURLs**: Deletes URL tracking parameters


**Optional**:


- LocalCDN**: Serves shared libraries locally
- Cookie AutoDelete**: Automatically deletes cookies after closing tabs
- NoScript**: Total control over JavaScript execution (advanced users)


To install a:


- Visit [chrome.google.com/webstore](https://chrome.google.com/webstore) or [addons.mozilla.org](https://addons.mozilla.org)
- Click on "Add to Chrome/Firefox"
- Orion will intercept and install the extension automatically


**Caution**: As extension support is experimental, many extensions may not work properly or may affect performance. In the event of a problem (site no longer working, slowness), disable the extensions one by one to identify the source.


## Daily use


### Interface and unique features



![Outil de personnalisation pinceau](assets/fr/13.webp)

*Orion brush menu for customizing the display: font size, theme (light/dark), deactivation of sticky headers and removal of distracting elements*


**Brush tool: advanced customization**


Orion's **brush** tool is a unique feature that lets you customize the display of each website:


**Theme options**:


- Switch between light and dark themes for each site
- Automatic adaptation to your system preferences


**Typographical control**:


- Font size**: Adjust legibility with the A- and A+ buttons
- Font style**: Change font family (default or custom)


**Interface cleaning**:


- Disable sticky headers**: Removes headers that remain stuck at the top when scrolling
- Erase Elements**: Permanently remove annoying elements (ads, pop-ups, cookie banners)
  - Click on "+ Erase" then select the item to be hidden
  - Very useful for sites with persistent ads or visual tracking elements


**Persistence**: All these settings are saved per domain and automatically reapplied the next time you visit.


**Advanced tab management**:


- Vertical tabs**: Activate via the menu bar (Tabs on the Side function)
- Compact tabs**: In Preferences → Tabs → Layout "Compact" to save space
- Tab groups**: Organize your sessions by theme
- Multiple profiles**: Create separate identities via the menu bar (Profiles function) with completely isolated data


**Low Power Mode**: Inspired by the iPhone, this mode automatically suspends inactive tabs after 5 minutes and can reduce energy consumption by up to 90%. Activate it via Orion's menu bar on Mac, or in settings on iOS.


**Built-in tools** (Edit menu and others):


- Edit Text on Page**: temporarily modify any text (Edit menu)
- Allow Copy & Paste**: Bypasses copy restrictions (Edit menu)
- Copy Clean Link**: Right-click on a link to remove tracking parameters
- Focus Mode**: distraction-free, full-screen navigation
- Picture-in-Picture**: Watch videos in a floating window
- Open in Internet Archive**: Direct access to archived versions
- Privacy Report**: Click on the shield 🛡️ to see the items blocked by page


### Private browsing management


Orion's private navigation (⌘⇧N) offers:


- Complete isolation of cookies and sessions
- Automatic deletion on closing
- History and cache deactivation
- Enhanced protection against fingerprinting


**Tip**: For advanced compartmentalization, create **separate profiles** via the menu bar (Profiles function). Each profile appears as a separate app in the Dock, with its own settings, extensions and data completely isolated.


### Performance optimization and privacy


To keep Orion fast and private:


- Extensions**: Limit to the strict minimum (may reduce performance)
- Low Power Mode**: Activate for long sessions (90% savings possible)
- Privacy Report**: Click on the shield 🛡️ to see blockages in real time
- Visual customization**: Use the 🖌️ brush to adapt the display and remove distracting elements
- Copy Clean Link**: Right-click to copy links without trackers
- Separate profiles**: Use dedicated profiles to compartmentalize your activities
- Website Settings**: Click on the gear ⚙️ to adapt permissions by site
- Regular cleaning**: Clear the cache via Orion → Clear Browsing Data


## Comparison with alternatives


| Critère | Orion | Safari | Chrome | Firefox | Brave |
|---------|-------|--------|---------|----------|--------|
| **Télémétrie** | Aucune | Minimale | Extensive | Modérée | Minimale |
| **Bloqueur natif** | 99,9% efficace | Basique | Absent | Partiel | Complet |
| **Extensions** | Chrome + Firefox | Limitées | Chrome uniquement | Firefox uniquement | Chrome uniquement |
| **Performance Mac** | Excellente | Excellente | Bonne | Moyenne | Bonne |
| **Consommation RAM** | Très faible | Faible | Élevée | Moyenne | Moyenne |
| **Open Source** | Partiel | Partiel (WebKit) | Partiel | Complet | Complet |
| **Plateformes** | Mac/iOS | Mac/iOS | Toutes | Toutes | Toutes |

**Versus Safari**: Orion offers superior protection with its advanced blocker and extension support, while maintaining WebKit performance.


**Versus Chrome**: unrivalled privacy without compromising compatibility, thanks to support for Chrome extensions.


**Versus Firefox**: Faster on the Mac, Interface more intuitive, but less granular control and not open-source.


**Versus Brave**: Similar philosophy, but Orion avoids crypto/BAT controversies and offers better Apple integration.


## Recommended use cases


**Ideal for**:


- Apple users seeking more privacy than Safari
- People who want to block all ads (including YouTube) without extensions
- Developers requiring WebKit devtools with integrated privacy protection
- IPhone users wanting desktop extensions on mobile (unique innovation)
- Professionals who need to compartmentalize their activities (multiple profiles)
- Mobile users looking for better battery management (Low Power Mode)


**Avoid if**:


- You mainly use Windows/Linux (no version available)
- Full open-source is essential for your threat model
- You depend on specific extensions that may not work
- You need cross-platform synchronization beyond the Apple ecosystem
- You prefer a proven, stable solution (permanent beta status since 2021)


## Points of attention and safety


### Unique safety features


**Revolutionary anti-fingerprinting protection**: Orion is the only browser to completely block the execution of fingerprinting scripts before they can scan your system. This "no script running = no fingerprinting possible" approach outperforms traditional masking methods used by other browsers.


**Transparent Whitelist**: Orion maintains a small public list of sites (browserbench.org, wizzair.com) where blocking is automatically disabled to avoid malfunctions. This transparency enables users to understand exactly when and why blocking is alleviated.


**Unaudited extensions**: Support for Chrome/Firefox extensions introduces additional risks, as these extensions were not designed for WebKit and are not specifically audited for this environment.


### Maintenance and updates



- Automatic updates**: Orion updates automatically on macOS via Sparkle
- Vulnerability tracking**: Regularly check release notes for security patches
- Bug reporting**: Use [orionfeedback.org](https://orionfeedback.org) to report problems



## Conclusion


Orion Browser represents a significant step forward for privacy on macOS and iOS. Its zero telemetry approach, combined with an ultra-efficient native blocker and unique support for universal extensions, makes it an excellent choice for privacy-conscious Apple users.


**Important**: Orion remains in permanent beta since 2021, with extension compatibility limitations and inherent WebKit risks. Assess these trade-offs according to your threat model.


For everyday use on a Mac or iPhone, it's probably the best compromise between confidentiality, performance and ease of use available in the Apple ecosystem, provided you accept its limitations.


Remember: protecting your privacy doesn't just depend on your browser. Combine Orion with best practices (strong passwords, 2FA, VPN if necessary) for optimum online security.


## Resources and support


### Official documentation


- Official website**: [kagi.com/orion](https://kagi.com/orion/)
- Full FAQ**: [browser.kagi.com/faq](https://browser.kagi.com/faq)
- Community forum**: [community.kagi.com](https://community.kagi.com)
- Bug tracking**: [orionfeedback.org](https://orionfeedback.org)
- GitHub Orion**: [github.com/OrionBrowser](https://github.com/OrionBrowser) - Open-source components
- Blog Kagi**: [blog.kagi.com](https://blog.kagi.com) - News and updates


### Recommended verification tests


After configuration, test your setup:


- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/) - Fingerprint test
- [DNS Leak Test](https://www.dnsleaktest.com/) - Check for DNS leaks
- [BrowserLeaks](https://browserleaks.com/) - Complete suite of privacy tests


### Alternatives on Plan ₿ Network

For maximum protection, consult our other guides:


- [Firefox hardened](https://planb.network/tutorials/computer-security/communication/firefox-11814cec-3415-4ed9-a06e-f6fda5c9510f) - Advanced multi-platform configuration
- [Tor Browser](https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb) - Complete network anonymity
- [Mullvad Browser](https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e) - Maximum fingerprinting protection


If you'd like to learn more about the history and operation of browsers, as well as the main digital objects in your daily life, I invite you to discover our new free training course SCU 202, available on Plan ₿ Network:


https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
