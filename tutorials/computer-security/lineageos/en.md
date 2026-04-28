---
name: LineageOS
description: Free, unglued Android operating system for smartphones
---

![cover](assets/cover.webp)


Conventional Android systems pre-installed on our smartphones pose a number of well-known problems: intensive integration of Google services leading to constant data tracking, unwanted sponsored applications (bloatware) imposed by manufacturers, and the abandonment of update tracking after a few years, condemning still-functioning devices to programmed obsolescence.


LineageOS presents itself as an elegant answer to these problems. A product of the open source community and a direct successor to CyanogenMod (discontinued at the end of 2016), LineageOS is a free Android-based mobile operating system that puts users back in control of their smartphones. Officially launched in December 2016, the project now boasts over 4.4 million active installations worldwide and supports hundreds of phone models from over 20 different brands.


![lineageos-homepage](assets/fr/01.webp)


*Official LineageOS website presenting the project and its objectives*


## What is LineageOS?


### Philosophy and objectives


LineageOS is an open source mobile operating system based on the Android Open Source Project (AOSP), developed by a vast community of volunteer contributors worldwide. Its unofficial motto could be "Your device, your rules": the project aims to extend the lifespan of smartphones while offering a streamlined, privacy-friendly Android experience.


The project rose from the ashes of CyanogenMod, one of the most popular alternative Android ROMs in history. When CyanogenMod Inc. closed its doors in December 2016, the community mobilized to create LineageOS, retaining the spirit of innovation and open-source philosophy that characterized its predecessor.


Unlike OEM Android distributions, LineageOS does not pre-install any Google applications by default, and completely eliminates bloatware. Users start with a minimalist system including only essential applications (phone, messages, camera, browser) and are free to choose what to add later.


### Impact and community


Official statistics reveal the scale of the project: with over 4.4 million active installations in 224 countries, LineageOS represents one of the most widely adopted Android alternatives in the world. Brazil leads the way with over 2 million users, followed by China and the USA, demonstrating the universal appeal of a free, customizable Android.



## Main features


### Interface and user experience


**Pure Android**: LineageOS offers an authentic Android experience close to AOSP, without manufacturer overlays or superfluous applications. The Interface remains familiar to Android users while offering optimal fluidity thanks to the absence of bloatware.


**Google-free by default**: No Google services are pre-installed, for legal and ethical reasons. This "Google-free" approach guarantees total control over your personal data and improves performance by avoiding services running in the background.


### Customization and safety


**Advanced customization**: LineageOS unlocks many options unavailable on stock Android: navigation button reconfiguration, customizable system themes, usage profiles adapted to different contexts (work, personal, gaming).


**Outil Trust**: Integrated functionality that monitors your device's security status and alerts you to potential threats, providing real-time visibility of your system's security.


**Extended updates**: The LineageOS community is committed to providing monthly security patches, allowing devices discontinued by their manufacturers to continue receiving the latest Android security patches.


## Compatible devices


LineageOS supports hundreds of devices from over 20 manufacturers: Samsung, Xiaomi, OnePlus, Motorola, Sony, Google Pixel, Fairphone and many others. This broad compatibility is one of the project's major advantages over alternatives such as GrapheneOS, which are limited to Pixel devices.


![devices-compatibility](assets/fr/02.webp)


*LineageOS-compatible devices page with filters by manufacturer*


![google-devices](assets/fr/03.webp)


*Google devices supported, including the Pixel 4 (codename "flame")*


### Popular devices


According to official statistics, the most-used models include a variety of devices covering different price and age ranges, demonstrating LineageOS's ability to breathe new life into older smartphones as well as optimizing newer ones.


### Crucial points before installation


**Unlockable bootloader**: Check that your manufacturer/operator allows unlocking. Some brands, such as Huawei, have done away with this possibility on recent models, while others impose specific procedures.


**Exact model**: It's crucial to download the ROM that corresponds precisely to your device. Two models with similar trade names may differ technically (Galaxy S10 vs S10 5G for example) and require different images.


**Scalable support**: Newer devices may not be supported immediately, as porting requires a volunteer developer to take care of them. Conversely, support may stop if a device's maintainer withdraws from the project.


## Installation


### Essential prerequisites


⚠️ **Read these instructions completely before you start** to avoid any problems!


**Return to stock firmware (if necessary) :**


- Android Flash Tool**: Use the official Google tool [flash.android.com](https://flash.android.com) to easily restore your Pixel device to stock Android from your web browser (Chrome/Edge required)
- Alternative**: Factory images manually from [developers.google.com/android/images](https://developers.google.com/android/images)


**Mandatory prerequisite tests:**


- Boot your device at least once** with the original stock system
- Test all features**: SMS, calls, Wi-Fi, mobile data
- Important**: Check that you can send/receive SMS and make/receive calls (including via WiFi and 4G/5G). If it doesn't work on the stock system, it won't work on LineageOS either!
- Recent devices**: Some require VoLTE/VoWiFi to be used at least once on the stock system to provision IMS


**System preparation:**


- Remove all Google** accounts from your device to avoid Factory Reset Protection, which may block activation
- Full backup** : The process will completely erase your phone. Back up photos, contacts, applications and important files


**ADB and Fastboot tools:** Follow the [official LineageOS guide](https://wiki.lineageos.org/adb_fastboot_guide#installing-adb-and-fastboot) to install the Android SDK Platform Tools. Verify installation with `adb version` and `fastboot --version`.


**Phone configuration:**


- Activate **Developer options**: Settings > About > tap "Build number" 7 times


![android-version](assets/fr/06.webp)


*Navigate to Settings > About Phone to activate developer mode*



- Enable **USB debugging** in Developer options
- Activate **OEM Unlock** (essential for unlocking the bootloader)


![developer-options](assets/fr/07.webp)


*Enable Developer Options, USB debugging and OEM unlocking*


### Detailed installation


⚠️ **These instructions are specific to LineageOS 22.2. Follow each step precisely. Don't move on if something fails!


#### Step 1: Firmware check


**Firmware required**: Your device must have Android 13 installed before continuing (for Pixel 4). Firmware refers to the device-specific images included in the stock system.


![pixel4-info](assets/fr/04.webp)


*Official Pixel 4 page with download links and installation guides*


![downloads-page](assets/fr/05.webp)


*LineageOS build download page and files*


**Pixel 4 specific downloads:**


- Build LineageOS**: [download.lineageos.org/devices/flame/builds](https://download.lineageos.org/devices/flame/builds)
- Required files**: Download the 3 required files from this page (they will be used in the following steps):
  - `lineage-22.2-YYYYMMDD-nightly-flame-signed.zip` (main ROM)
  - dtbo.img` (partition device tree blob)
  - `boot.img` (recovery LineageOS)


⚠️ **Important**: Check the Android version, not the manufacturer's OS version. Being on a custom ROM (even LineageOS) does not guarantee that this requirement is met.


💡 **Tip**: If in doubt about your firmware, return to the stock system before continuing!


#### Step 2: Unlocking the bootloader


⚠️ **This step deletes all your data!



- Test the ADB connection**: Connect your device via USB and test with the command `adb devices` from your computer terminal


![adb-devices](assets/fr/08.webp)


*Check ADB connection with `adb devices`* command



- Authorize connection** on your phone


![usb-debugging-auth](assets/fr/09.webp)


*USB debugging enabled with computer's RSA fingerprint*



- Boot into bootloader mode** :

```
adb -d reboot bootloader
```

Or hold **Volume Down + Power** device off



- Check the fastboot** connection:

```
fastboot devices
```


![fastboot-mode](assets/fr/10.webp)


*Fastboot commands in terminal to check connection*


![bootloader-screen](assets/fr/11.webp)


*Pixel 4's fastboot display with system information*



- Unlock the bootloader** :

```
fastboot flashing unlock
```

On the device, use the Volume keys to navigate and press the **Power** button to select "Unlock the bootloader" and confirm the operation


![unlock-bootloader](assets/fr/12.webp)


*Confirmation of bootloader unlock on device*


⚠️ **The phone will restart automatically** after confirmation of unlocking



- After automatic restart**, re-enable USB debugging in the developer options



#### Step 3: Flash additional partitions


⚠️ **Required for recovery to work properly**



- Restart bootloader**: Volume Down + Power
- Flash** (replace `/path/to/` with the folder where you downloaded the file) :

```
fastboot flash dtbo /chemin/vers/dtbo.img
```


![flash-partitions](assets/fr/13.webp)


*Flash of dtbo and boot.img partitions via fastboot*


#### Step 4: Installing LineageOS recovery



- Flash recovery** (replace `/path/to/` with the folder where you downloaded the file) :

```
fastboot flash boot /chemin/vers/boot.img
```


- Restart in recovery** to check


#### Step 5: Installing LineageOS



- Restart in recovery**: Volume Down + Power → Recovery Mode


![recovery-mode](assets/fr/14.webp)


*Interface from LineageOS recovery with main menu*



- Factory Reset** : Type "Factory Reset" → "Format data / factory reset"


![factory-reset](assets/fr/15.webp)


*Factory reset process in LineageOS* recovery



- Return to main menu**
- Sideload LineageOS** :
   - On the device: "Apply Update" → "Apply from ADB"
   - On PC: `adb -d sideload /path/to/lineageos.zip`


![apply-update](assets/fr/16.webp)


*Select "Apply Update" then "Apply from ADB" in recovery*


![sideload-process](assets/fr/17.webp)


*LineageOS installation in progress via sideload*


![sideload-terminal](assets/fr/18.webp)


*Sideload command in terminal with installation progress*


💡 **Normal**: The process may stop at 47% or display "Success" errors - this is normal!


#### Step 6: First start-up



- Reboot**: "Reboot system now"
- First boot**: May take up to 15 minutes


🎉 **Installation complete!**


### Points of attention


⚠️ **Warning**: LineageOS is provided "as is" without warranty. While we make every effort to ensure that everything works, you install this at your own risk!


**Critical checks:**


- Firmware compatibility**: Be sure to check the firmware version required on your model's download page
- Never relock** the bootloader after installing LineageOS
- Follow the specific instructions** for your device


## Configuration and applications


### First start-up

Streamlined Interface, close to stock Android, without Google. Simple configuration: language, Wi-Fi, no account required.


### Alternative applications


**Secure application sources:**


**F-Droid** : The benchmark open source application store, preinstalled with LineageOS for microG or downloadable directly. F-Droid offers only open-source software that has been verified and compiled transparently, guaranteeing the absence of trackers or malicious components.


**Aurora Store**: Anonymous client for accessing the Google Play Store without a Google account. Aurora borrows shared anonymous accounts, allowing you to download mainstream apps while preserving your privacy.


**Essential alternative applications:**



- Navigation**: Organic Maps (offline maps based on OpenStreetMap)
- Communication**: Signal (end-to-end encrypted messages), K-9 Mail (free email client)
- Media**: NewPipe (ad-free, tracking-free YouTube), VLC (universal media player)
- Productivity**: Nextcloud (self-hosting cloud), Simple Calendar (CalDAV synchronization)
- Security**: Bitwarden (password manager), Aegis Authenticator (2FA codes)


These applications, most of which are available via F-Droid, form a coherent ecosystem that can fully replace Google services while offering a modern, functional user experience.


## Use and maintenance


### Daily experience


LineageOS transforms the Android experience, giving priority to fluidity and responsiveness. The streamlined Interface is particularly effective on older devices, which are given a new lease of life, with performance generally superior to manufacturer ROMs thanks to the absence of heavy overlays and superfluous processes.


Basic functionalities (calls, SMS, photos, browsing) operate seamlessly, while customization tools enable the system to be finely tuned to individual preferences without compromising stability.


### OTA update system


LineageOS features a particularly easy-to-use Over-The-Air update system. New versions are proposed automatically via notifications, and installation takes just a few clicks, with no need for complex technical intervention. The process fully preserves your installed data and applications.


These regular updates are a major asset, especially for devices that have been discontinued by their manufacturers, who can continue to benefit from the latest Android security patches.


### Recommended best practices


**Post-installation security:**


- Set a strong PIN or password for unlocking
- Check that storage encryption is enabled (usually by default)
- Install a password manager like Bitwarden via F-Droid


**Preventive maintenance:**


- Regular OTA updates for security
- Limit application installation to trusted sources (F-Droid, Aurora Store)
- Periodically review the permissions granted to applications
- Occasional restarts optimize performance and free up memory


## Advantages and limitations


✅ **Benefits:**


- Default privacy (no Google tracking)
- Wide compatibility (300+ models)
- Superior performance (no bloatware)
- Extended updates on older devices


❌ **Limitations:**


- Technical installation
- No Android Auto/Google Pay
- Banking apps can be problematic


## GrapheneOS vs LineageOS: What's the difference?


### Distinct approaches


**GrapheneOS** focuses exclusively on maximum security, and runs only on Google Pixels to exploit their dedicated security chips. The system incorporates numerous advanced mitigations against exploits and considerably strengthens application sandboxing.


**LineageOS** balances security, privacy and convenience on as many devices as possible. The approach is more pragmatic, aiming for extended compatibility rather than absolute security.


### Managing Google services


**GrapheneOS**: Offers an optional sandboxed Google Play system. Google Play can be installed but runs in a strict sandbox, with no special system privileges. This unique approach makes it possible to use the Google ecosystem while maintaining strict security control.


**LineageOS**: Lets the user choose to install Google services (GApps), microG (free alternative), or remain entirely Google-free. Maximum flexibility to suit your needs.


### Technical comparison



| **Aspect** | **GrapheneOS** | **LineageOS** |
|------------|----------------|---------------|
| **Compatibility** | Pixels only | Hundreds of devices |
| **Security** | Advanced mitigations | Standard AOSP security |
| **Google Play** | Optional sandboxing | Classic installation possible |
| **Installation** | Web interface + USB | Technical manual procedure |
| **Philosophy** | Security above all | Balance and freedom of choice |

### Recommendations for use


**Choose GrapheneOS** if you own a Pixel, if maximum security is your top priority, and if you accept constraints for enhanced protection.


**Go for LineageOS** if you have a non-Pixel device, are looking for a good privacy/practicality balance, or want the freedom to choose your level of compromise with the Google ecosystem.


## Conclusion


LineageOS offers a mature alternative for regaining control of your Android smartphone. Unglued experience, optimal performance, extensive compatibility: the ideal choice for combining privacy and everyday practicality.


## Resources


### Official documentation


- [LineageOS official website](https://lineageos.org)
- [LineageOS Wiki](https://wiki.lineageos.org) - Installation guides by model
- [LineageOS for microG](https://lineage.microg.org) - Version with integrated microG


### Community


- [Subreddit r/LineageOS](https://reddit.com/r/LineageOS)
- [Mastodon account @LineageOS](https://fosstodon.org/@LineageOS)


https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1