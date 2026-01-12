---
name: Qubes
description: A reasonably safe operating system.
---

![cover](assets/cover.webp)


Qubes OS is a free, open-source operating system designed for users who place security at the top of their priorities. Its particularity is based on a simple but radical idea: instead of considering the computer as a whole, it divides its use into independent compartments called **_qubes_**.


Each qube functions as an **isolated virtual environment**, with a specific trust level and function. So even if an application is compromised, the attack remains confined to its qube without affecting the rest of the system.


> If you're serious about security, Qubes OS is the best operating system available today. - **Edward Snowden**.

However, installing Qubes OS requires more preparation than installing a conventional operating system. It involves checking certain hardware prerequisites, understanding the basics of virtualization and accepting a different experience, where every day-to-day task is thought of in terms of separation. But once in place, Qubes OS offers a robust framework that redefines the way you interact with your computer on a daily basis. In this tutorial, we'll explain how Qubes OS works and how to install it easily on your system.


## How does Qubes OS work?


Qubes OS is based on the principle of compartmentalization. Rather than using a single system, it relies on the **Xen** hypervisor to create isolated virtual machines, called qubes. Each qube is dedicated to a specific task or level of trust (work, personal browsing, banking, etc.). This separation ensures that any compromise in one qube cannot spread to the others, acting as several independent computers within a single machine.


User Interface is managed by a central, secure domain called **dom0**. This domain is totally isolated from the Internet, making it the heart of the system. Although windows and menus are displayed by dom0, the actual execution of applications takes place in their respective qubes.


## The different types of qubes


Around dom0 revolve different types of qubes, each with a very specific role to play.



- The **AppVM** are used to run everyday applications: the user can thus separate his professional e-mails from his web browsing or banking activities, with each environment remaining totally independent of the others.



- These AppVMs are themselves based on **TemplateVMs**, which serve as centralized templates for installing and updating software, eliminating the need to manage each qube separately.


Qubes OS also integrates virtual machines specialized in **system services**.



- The **NetVM** directly manages the **network devices** and ensures connection to the Internet. They are often associated with **FirewallVMs**, which intervene to **filter traffic** and limit the exposure of other qubes.



- ServiceVMs play a similar role, for example in USB device management, always with the same logic: isolate the riskiest components to reduce the attack surface.


Finally, for occasional or risky tasks, Qubes OS offers **DisposableVM**. These ephemeral qubes are created on the fly to **open a suspicious document** or **visit a dubious site**, then disappear completely when closed, erasing all traces and preventing any persistent attack.


### The secure copy mechanism (qrexec)


Exchanges between qubes are based on **qrexec**, an inter-VM communication system designed for security. Instead of letting qubes communicate freely, qrexec imposes **specific policies**: a file copied from one AppVM to another, or text transferred via the clipboard, always passes through a channel monitored and validated by the system. In this way, even the simple act of copying and pasting is controlled to prevent the spread of malware.


### Disk management


Qubes OS uses an ingenious system for storage management. TemplateVMs contain the common software base, while AppVMs add only their personal data and specific files. This reduces disk space usage and facilitates global updates. DisposableVMs, on the other hand, use temporary volumes that disappear completely when closed. This model not only guarantees greater security, but also efficient resource management.


## Why choose Qubes OS?


The advantages of Qubes OS lie above all in its unique security model. At the heart of this approach is compartmentalization, which protects the user by isolating each task in separate virtual machines. In practical terms, an infected e-mail or malicious website can only compromise a single qube, leaving the rest of the system and your personal data fully protected. This architecture considerably limits complex attacks which, on a conventional system, could propagate freely.


Qubes OS also offers total transparency and control over your digital environment. You know exactly which software has access to which resource, whether it's the network, a USB device or other sensitive components. The system integrates advanced security features by default, such as full disk encryption, and facilitates the use of anonymizing services like the Whonix operating system.


https://planb.academy/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

Rather than seeking to create an impenetrable system, Qubes OS focuses on resilience: it encapsulates damage in the event of compromise, reducing the risk to the rest of the system. This pragmatic approach makes Qubes OS a preferred choice for users with high security needs, or who wish to retain maximum control over their digital lives.


## Installing Qubes OS


Before installing Qubes OS, it's essential to ensure that your hardware meets the minimum requirements, as the system relies on virtualization to isolate qubes. The main components to check are :


- The **Processor**: A 64-bit processor compatible with hardware virtualization (Intel VT-x or AMD-V).
- RAM: a minimum of 8 GB is required, but we recommend RAM of 16 GB or more to run several qubes simultaneously.
- **Storage space**: a minimum of 36 GB, ideally 128 GB on an SSD for optimum performance.


To install Qubes OS, download the official ISO image from the Qubes OS [official site](https://www.qubes-os.org/downloads/). It is essential to check the integrity of the ISO using the GPG signatures provided, to ensure that the file has not been tampered with and that the download is secure.


https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)


Once the ISO has been verified, you need to create a bootable installation medium, usually a USB stick. To do this, download and install software such as **Rufus** on Windows or **Etcher** on Windows, Linux or macOS. These tools enable you to copy the ISO to the USB stick so that it is bootable.


Before starting installation, it is necessary to configure your computer's **BIOS or UEFI** to **enable virtualization** and allow boot from USB. Depending on your machine model, it may be necessary to **disable Secure Boot**, as Qubes OS may not boot with this option enabled.


![0_02](assets/fr/02.webp)


Once these conditions have been met, restart your computer and access the BIOS/UEFI by immediately pressing **Esc**, **Del**, **F9**, **F10**, **F11** or **F12** (depending on manufacturer). In the boot menu, select the USB key as the boot device to launch the Qubes OS installation.


**Start-up screen**

When booting from the USB stick, you'll be taken directly to the **GRUB** menu, where you can choose the action to be performed. Using the arrow keys on your keyboard, select "Install Qubes OS" and press "Enter".


![0_03](assets/fr/03.webp)


**Choice of language** :


When the installation starts, the first step is to **choose the language** and **regional variant** suitable for your configuration. This ensures that the system and installation options are displayed correctly in your preferred language.


![0_04](assets/fr/04.webp)


**Parameter configuration** :


At this stage, you'll need to configure a number of elements before launching the installation on your machine.


![0_05](assets/fr/05.webp)


**Keyboard layout** :


Click on the **Keyboard** option, then select the **appropriate layout** for your computer. Once you've made your choice, click **Terminated** to move on to the next step.


**Choice of destination** :


Select the "Installation destination" option to choose the disk on which you wish to install Qubes OS. By default, partitioning takes place automatically, allowing you to remove all data from the disk and install the system on it. You can, however, choose **Customized** or **Advanced Customization** to perform a customized partitioning. Then click on "Done". The system will ask you to set a **password**, which acts as a security layer to encrypt your data. Be sure to choose a complex and unique password.


![0_06](assets/fr/06.webp)


![0_07](assets/fr/07.webp)


**Select date and time format** :

Click on the Time and date option, then select your geographical zone. You can also choose your preferred time format: 24h or 12h.


![0_08](assets/fr/08.webp)


**User account creation** :

Click on **Create user** to create your **first account**, which will enable you to log in to Qubes OS.


![0_09](assets/fr/09.webp)


**Activate root account** :

You can also **enable the root account** by setting a separate password for administration.


![0_10](assets/fr/10.webp)


Once these settings have been made, click on **Start installation** to start the process.


![0_11](assets/fr/11.webp)


Wait for the **end of installation**, then click on **restart system** to finalize installation and start Qubes OS.


![0_12](assets/fr/12.webp)


**Additional configuration** :

After reboot, Qubes OS prompts you to finalize the **default templates and qubes configuration**. Enter the password defined to encrypt the disk.


![0_13](assets/fr/13.webp)


Next, start by selecting the **TemplateVM** you wish to install. Common options include **Debian 12 Xfce**, **Fedora 41 Xfce** and **Whonix 17**, the latter being recommended for uses requiring **anonymity and network security**. You can also define the **default template**, which will serve as the basis for the creation of new **AppVMs**.


![0_14](assets/fr/14.webp)


In the **Main configuration** section, you can choose to automatically create essential system qubes such as **sys-net**, **sys-firewall** and **default DisposableVM**. It is advisable to enable the option to make **sys-firewall and sys-usb disposable**, to limit device and network exposure in the event of compromise. You can also create default **AppVMs**, such as **personal**, **work**, **untrusted** and **vault**, to organize your activities according to their level of trust.


![0_15](assets/fr/15.webp)


Qubes OS also lets you create a **qube dedicated to USB devices** (sys-usb) and configure **Whonix Gateway and Workstation qubes** to secure your communications via the Tor network. For advanced users, the **Advanced configuration** section lets you create a **LVM thin pool** to efficiently manage disk space between qubes.


Once all these options have been configured, click on **Complete**, then on **Finish configuration**. Wait while the system applies these settings. You will then be prompted to **log in to your user account**, and your Qubes OS environment will be ready for use, secure and properly isolated for your various activities.


![0_17](assets/fr/17.webp)


Your operating system is now installed and ready to use.


![0_18](assets/fr/18.webp)


## Create a qube on your system


To create a qube, the process is managed by the **Qube Manager** tool, accessible from the Start menu. In the tool window, simply click on the **Create qube** icon to open a new configuration window. First, enter a name for your qube, such as "perso-web" or "work", to identify its use.


Next, you'll select its **Type**, usually **AppVM** for routine tasks, or **DisposableVM** for temporary use. It's crucial to choose the **Template** on which your qube will be based, such as "fedora-39" or "debian-12", as this will provide the operating system and software. You will also designate the **NetVM**, which is the qube responsible for Internet access, by default **sys-firewall**.


Finally, after adjusting storage size and RAM if necessary, a simple click on **OK** will launch the creation process. Once the process is complete, your new qube will be visible in the list and ready for use.


In conclusion, Qubes OS is no ordinary operating system, but a cutting-edge security solution that rethinks the architecture of the personal computer. Its approach, based on compartmentalization and isolation through virtualization, offers unrivalled protection against the most sophisticated threats. By segmenting the work environment into specialized qubes for each task, it ensures that malware cannot spread and endanger the entire system.


Whether you need to surf the web securely, protect sensitive information or work with varying levels of trust, Qubes OS provides a resilient, transparent framework. By adopting good practices and making full use of its features, you'll have a **digital fortress** adapted to modern threats. Learn more about protecting your data and privacy.


https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1