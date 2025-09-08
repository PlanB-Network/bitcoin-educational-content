---
name: Firefox
description: How to configure Firefox to protect your privacy?
---

![cover](assets/cover.webp)


## Introduction


We all spend hours online, often without realizing what our browser is revealing about us. Every click, every search, every site we visit feeds a massive industry of personal data collection.


![Statistiques navigateurs 2024](assets/fr/01.webp)

*Web browser market share: Chrome dominates with 65% of the market, followed by Safari and Edge. Source: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*


As this graph shows, Google Chrome dominates massively, with over 65% of worldwide usage. This hegemony means that the majority of Internet users entrust their browsing data to Google, a company whose business model is based on targeted advertising. Firefox, with just 3% of the market, represents an alternative developed by Mozilla, a non-profit organization with no commercial interest in exploiting your data.


But choosing Firefox is only the first step. By default, even Firefox requires adjustments to maximize your protection. This guide takes you step by step, from the simplest to the most advanced, to transform Firefox into a veritable shield against tracking while preserving a pleasant browsing experience.


### Why Firefox?



- Free and open-source** (Gecko engine): auditable, transparent code
- Non-profit organization**: Mozilla Foundation, mission of general interest
- Built-in native protections**: Enhanced Tracking Protection (ETP), Total Cookie Protection (TCP), State Partitioning, HTTPS-only mode, DNS over HTTPS (DoH)
- Advanced customization**: unlike Chrome, Firefox lets you modify its behavior in depth


### Important principles before you start



- No universal recipe**: the more you modify, the more you risk standing out (fingerprinting). The aim is to be better protected without standing out from the crowd.
- Step-by-step progress**: Change a setting, test your usual sites, then continue. There's no need to change everything at once.
- Personal balance**: Find YOUR compromise between privacy and ease of use.


## Quick installation


![Téléchargement Firefox](assets/fr/02.webp)


**Official download:** Go to [firefox.com/browsers/desktop](https://www.firefox.com/en-US/browsers/desktop/). On this page, select your operating system (Windows, macOS, Linux) to access the appropriate download page with specific installation instructions.



- Windows**: download the `.exe` installer, double-click and follow the installation wizard
- macOS**: download the `.dmg` file, open it and drag Firefox into the Applications folder
- Linux**: several options available - package `.deb`/`.rpm`, Flatpak (Flathub), Snap, or via package manager (apt, dnf, pacman). Prefer official Mozilla sources.


**Tip:** Once installed, check for updates via Help → **About Firefox** (important for security patches).


![Configuration initiale Firefox](assets/fr/03.webp)

*First screen on launching Firefox: set Firefox as your default browser, add it to your shortcuts, then click "Save and continue "*


![Création compte Firefox](assets/fr/04.webp)

*Optional step: create or log in to a Firefox account. You can skip this step by clicking on "Not now" at bottom right*


![Page d'accueil Firefox](assets/fr/05.webp)

*Firefox home screen once configuration is complete. Note the ☰ menu at top right, which gives access to Settings and Extensions for customizing Firefox*


## Protections already activated by default (reassuring)



- Site isolation (Fission)**: in progressive deployment. This feature runs each site in a separate process to prevent one malicious tab from accessing another's data. Check its status via `about:support` (search for "Fission"). If not enabled, you can manually activate it in `about:config` with `fission.autostart = true`.
- Total Cookie Protection (TCP)**: active by default. Cookies and other storage are confined to the first-party site (one "jar" per site), which neutralizes cross-site tracking. Temporary exceptions are made via the Storage Access API when necessary (integrated login buttons).
- Bounce/Redirect Tracking Protection**: Firefox automatically detects and cleans up cookies left behind by bounce sites (links that redirect you via a tracker before the destination), reducing this tracking channel without any action on your part.


## Level 1 - Essential (≤ 10 minutes)


Objective: big privacy gains without breaking the web. For 90% of users.


To access the settings, click on the menu ☰ at the top right, then **"Settings "**:


![Paramètres généraux](assets/fr/07.webp)

*Firefox settings page - "General" tab. This is where you configure most of your privacy options*


**Tracking protection (ETP)**


- Switch **ETP** to **Strict**. You block more trackers (cross-site cookies, fingerprinting, cryptomining, social widgets...).
- If a site breaks (video, login button...), deactivate protection only for that site via the 🛡️ shield, then refresh the tab.


Here are the different ETP security levels:


- Standard** (balanced, maximum compatibility)
  - Blocks: social trackers, cross-site cookies (all windows), tracking content in private browsing, cryptocurrency miners, fingerprint detectors.
  - Includes **Total Cookie Protection** (TCP): one jar per site.
- Strict** (recommended for confidentiality)
  - Also blocks tracking content in all windows + known and suspected fingerprinting.
  - May break some sites; use the 🛡️ shield for a local exception.
- Custom** (advanced)
  - Fine tuning: cookies, tracking content, minors, fingerprinting (known/suspected).


![Paramètres protection contre le pistage](assets/fr/06.webp)


**Cookies and site data


- Enable **"Delete cookies and site data on close "** to restart cleanly each time you restart.
- Add **Exceptions** for 2-3 essential sites if you wish (e-mail, bank).

**Automatic data entry, suggestions and home page**


- Deactivate **auto-fill** (IDs, addresses, cards). Use a password manager instead.
- Search**: deactivate **"Show search suggestions "**.
- Address bar**: cut **"Sponsored suggestions "** and **"Contextual suggestions "**.
- Home**: disable **Pocket** and **sponsored content**.


![Paramètres cookies et mots de passe](assets/fr/08.webp)


**HTTPS only**


- Activate **"HTTPS mode only in all windows "**.

![Configuration DNS over HTTPS](assets/fr/09.webp)


**Telemetry and advertising measurement


- In "Data collection by Firefox", **uncheck all**.
- Deactivate **"Privacy-friendly advertising measures "** (PPA).
- Safe Browsing**: keep it enabled (recommended). Firefox checks sites against threat lists via hashed queries and local checks, protecting against phishing and malware with minimal privacy impact.


**Global Privacy Control (optional)**


- Activate the **GPC** to signal your refusal to sell/share data.


**Search engine


- Switch to **DuckDuckGo**, **Startpage**, **Qwant** or **Brave Search** (Settings → Search).


![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)


**Private navigation**


- Private windows (Ctrl/Cmd+Shift+P) for one-off sessions (gifts, secondary accounts...). Avoid "always private" mode: extensions may be inactive and cookie exceptions less useful.


**Essential extensions** (install from the official catalog)


- uBlock Origin**: blocks ads and current tracking, lightweight.
- Privacy Badger**: learns to block what follows you; sends Do Not Track / GPC.
- ClearURLs** (optional): Firefox (ETP Strict) and uBO already clean up a lot; keep it if you still see "dirty" URLs (utm, fbclid).
- Firefox Multi-Account Containers**: **isolates cookies/sessions and storage per container; parallel multi-accounts; less cross-site tracking**. Official extension: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.


![Extension Multi-Account Containers](assets/fr/12.webp)


**Passwords and 2FA**


- Use a dedicated password manager** (Bitwarden, KeePassXC). **Avoid** storing passwords in the browser. **Enable 2FA** wherever possible.


## Level 2 - Reinforced (Compartmentalization & Network)


Objective: compartmentalize activities and reduce network leakage.


**DNS over HTTPS (DoH)**


- Default status**: Automatically activated in some regions (USA, Canada, Russia, Ukraine). Elsewhere, manual activation required.
- Configuration**: Settings → General → Network settings → **Enable DoH** → **Cloudflare** or **Quad9** → **Maximum protection**.
- Maximum protection = TRR-only** (no fallback to system DNS). If a corporate/hotel network blocks, switch back to **Standard** or disable DoH.
- Redundancy**: If you're already using a trusted VPN with its own secure DNS, DoH can be redundant.
- Verification test**: `https://www.dnsleaktest.com/` should display only the chosen DoH provider.


![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)


**Compartmentalization with containers and profiles


- Multi-Account Containers**: create spaces (Personal, Work, Finance, Social Networks, Shopping, Disposable). Configure **"Always open in this container "** for your recurring sites. Official extension: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.
- Why use them?
  - Strong isolation** of cookies/sessions/storage by space.
  - Less cross-site tracking**: confine the giants (Facebook, Google).
  - Simultaneous multi-accounts** on the same service.
  - Less risk of CSRF/XSS** between segmented identities.
  - Tip: at the very least, dedicated containers for Social Networks/Google, Work, Finance.
- Facebook Container** (optional): a simplified version dedicated to FB/Instagram.
- Separate profiles**: via `about:profiles` (main profile, minimal "ultra-secure" profile, test profile). Total data and extension compartmentalization.


**Advanced extensions** (to be reserved)


- Cookie AutoDelete**: deletes a site's cookies as soon as the tab is closed (useful if Firefox is open for a long time).
- LocalCDN**: serves current libraries locally (reduces calls to Google/Microsoft). Partial compatibility.


**Mobile (Android)**


- Firefox Android + uBlock Origin**: similar protection on the move.


## Level 3 - Expert (about:config & Arkenfox)


Objective: advanced hardening with accepted compromises. Recommended on a **separate profile**.


Choose only one of the following two approaches:


**Approach A - Manual modifications**: A few targeted adjustments via `about:config` (simpler, more precise control)

**Approach B - Arkenfox user.js**: Full automated configuration (more complex, maximum protection)


➡️ **Arkenfox already includes ALL the about:config changes mentioned below** + hundreds more. If you choose Arkenfox, ignore the about:config section.


### Approach A: Manual modifications via about:config


Type `about:config` in the address bar → Accept risk.


![Avertissement about:config](assets/fr/13.webp)


![Interface about:config](assets/fr/14.webp)


![Préférences about:config](assets/fr/15.webp)



- Resistance to fingerprinting (inherited from Tor Browser)

```text
privacy.resistFingerprinting = true
```

Effects: UTC time zone, **letterboxing** (standard window sizes), standardized User-Agent/policies, Canvas/WebGL/AudioContext restrictions. More uniformity, but a few "quirks" (offset time, sometimes a bit of English).



- Disable WebRTC (avoids IP leaks; breaks Web visio)

```text
media.peerconnection.enabled = false
```



- Referer plus compatible (default)

```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```

Strict option (can break payments/SSO):

```text
network.http.referer.XOriginPolicy = 2
```



- Limiting chattering APIs and speculation

```text
dom.battery.enabled = false
device.sensors.enabled = false
beacon.enabled = false
geo.enabled = false
media.navigator.enabled = false
network.prefetch-next = false
browser.urlbar.speculativeConnect.enabled = false
network.http.speculative-parallel-limit = 0
```


Golden rule: if something breaks, go back to the last change.


### Approach B: Arkenfox user.js (Fully automated configuration)


The **Arkenfox** project provides a community-maintained `user.js` file that automatically applies hundreds of privacy- and security-oriented Firefox preferences. On restart, Firefox reads this file from your profile and applies these settings.



- What's the point? Start from a **consistent hardened base** without "clicking everywhere"; reduce oversights; save time.
- What it changes (examples): telemetry cut, cookies/cache/referrer/HTTPS strengthened, **RFP** + letterboxing, **WebRTC disabled**, DoH/TLS adjustments, chatty APIs limited.
- When to use it: if you want Firefox hardened in 10 minutes and accept a few exceptions (DRM/streaming, Web visio, SSO/payments).
- Advantages: fast, consistent, **updated** (ESR-aligned), very well **documented** (wiki + comments), **customizable** via overrides.
- Limitations: compatibility (some web apps), comfort (UTC, window sizes), and a reminder: **it's not Tor** (no network anonymity).


Installation (ideally on a **dedicated profile**)

1. Save profile/favorites and list your sites with cookie exceptions.

2. Download `user.js` from `https://github.com/arkenfox/user.js` (ESR/stable version).

3. Find your profile folder via `about:profiles`:


   - Windows: `%APPDATA%/Mozilla/Firefox/Profiles/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Library/Application Support/Firefox/Profiles/...`

4. Close Firefox and move `user.js` to the root of the profile folder.

5. Relaunch; customize via `about:config` or an overrides file.


Updates


- Follow the Arkenfox releases (ESR aligned), replace the `user.js`, relaunch Firefox; read the release notes.


**Customization via Overrides**


Arkenfox is deliberately restrictive by default. To adapt certain settings to your needs (streaming, visio, specific sites), you can create a `user-overrides.js` file in the same folder as `user.js`. This file allows you to "override" certain Arkenfox preferences without modifying the main file.


Create `user-overrides.js` and add your customizations:

```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (si vous préférez le garder)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Historique moins restrictif
user_pref("places.history.expiration.max_pages", 200000);

// Synchronisation Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (si visio nécessaire)
user_pref("media.peerconnection.enabled", true);

// Referer plus compatible
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```


Best practices


- Use a separate **"Arkenfox" profile** and keep a "normal" profile for comfort.
- Minimize extensions (uBlock Origin OK) to limit attack surface and uniqueness.
- Add site-by-site exceptions (shield 🛡️, uBO, NoScript if used) when necessary.
- Test after every change: WebRTC/DNS leaks, Cover Your Tracks, CreepJS.


## Best practices



- Updates**: Firefox and extensions up to date.
- Extensions**: reasonable and reliable; watch out for "dubious" redemptions.
- Downloads**: caution; test sensitive files on VirusTotal.
- Passwords**: **dedicated manager** (Bitwarden, KeePassXC); **2FA** enabled; avoid storing in browser.
- Hygiene**: confine Google/Facebook to containers; close/open regularly to "reset" context.


## Limits & Alternatives



- A hardened browser ≠ network anonymity: without **VPN**, your IP remains visible; even with it, correlation remains possible.
- Modifying too much can make you **unique**. **RFP** standardizes; randomization tools (e.g. Chameleon) can... set you apart. Test, compare, adjust.
- Alternatives/complements:
 - Tor Browser: network anonymity via Tor; slower. See our complete installation and configuration guide**:


https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb


 - Mullvad Browser: "Tor without Tor", to be combined with VPN; standardized footprint. Find out how to install it in our dedicated tutorial**:


https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e


- Recommended combinations: Firefox (Level 2) + VPN for everyday use; Tor/Mullvad for sensitive activities; separate profiles for compartmentalization.


## Conclusion


By following this step-by-step guide, you've transformed Firefox into a true bulwark against digital surveillance. From essential Level 1 settings to advanced Arkenfox configurations, every change strengthens your privacy without compromising your browsing experience.


**Your privacy is now better protected**: ad trackers blocked, cookies compartmentalized, IP address leaks neutralized, telemetry disabled. Firefox is no longer just a browser, but a digital resistance tool tailored to your needs.


**Remember: confidentiality is never a given. Test your protection regularly, update your settings, and don't hesitate to adjust your configuration as your habits change. Your online anonymity depends as much on your tools as on your practices.


## Resources


### Plan ₿ Network


- SCU 202 - Improving your personal digital security: To learn more about the digital security concepts covered in this tutorial**


https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Mozilla documentation


- [Enhanced Tracking Protection](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop): Official guide to enhanced tracking protection
- [State Partitioning](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning): Technical documentation on state partitioning
- [MDN Web Security](https://developer.mozilla.org/docs/Web/Security): Complete reference on web security


### Arkenfox


- [Wiki and installation guide](https://github.com/arkenfox/user.js/wiki): Complete Arkenfox project documentation
- [Deposit and releases](https://github.com/arkenfox/user.js): Download user.js file and track updates


### Guides & communities


- [PrivacyGuides - Desktop browsers](https://www.privacyguides.org/en/desktop-browsers/): Browser recommendations and comparisons
- Reddit**: r/firefox, r/privacy for feedback and support
- PrivacyGuides forum**: in-depth technical discussions


### Test tools


- [Cover Your Tracks (EFF)](https://coveryourtracks.eff.org/): Digital fingerprinting and anti-tracking effectiveness
- [DNS Leak Test](https://www.dnsleaktest.com/): DNS leak test and DoH efficiency
- [BrowserLeaks](https://browserleaks.com/): Complete test suite (WebRTC, Canvas, Fonts, etc.)
- [BadSSL](https://badssl.com/): SSL/TLS certificate validation tests
- [CreepJS](https://abrahamjuliot.github.io/creepjs/): Advanced analysis of 50+ fingerprinting vectors
- [Cloudflare DNS Test](https://1.1.1.1/help): Checking that Cloudflare DoH is working properly
