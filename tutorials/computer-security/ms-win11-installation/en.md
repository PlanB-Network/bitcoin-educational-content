---
name: WINDOWS 11
description: Automatic Installation of Microsoft Windows 11
---
![cover](assets/cover.webp)

___

In this tutorial, we will learn how to install Windows 11 automatically using a method other than the standard Windows installation process.

___

## I. First : Download!

The first thing you’ll need is an installation file. The safest and most reliable place to download it is directly from Microsoft’s official website.

Simply visit the link provided below and follow the instructions to download the Windows 11 ISO file:

* [MS Windows 11](https://www.microsoft.com/en-us/software-download/windows11)
![Image](assets/en/02.webp)

Once you’re on the download page, scroll down to the section for downloading the ISO file.

![Image](assets/en/01.webp)

َAnd choose the proper version.

![Image](assets/en/03.webp)

After selecting Windows 11, click the Confirm button.

At this step, it may take a few seconds to process the request, and then you will see the following page:

![Image](assets/en/04.webp)

After confirming the request, you need to choose your preferred language.

![Image](assets/en/05.webp)

After selecting the language and clicking the Confirm button, the request will be processed. This step may take a few seconds.

Once the request is successfully processed, you will see a page with the download link for the .iso file. Click the 64-bit Download button to start the download.

The file size is about 5.5 GB, and the generated link will be valid for 24 hours.

## II. Second : Automation!
At this stage, we need to make changes to the standard Windows installation. In this stage, using Unattended install, we determine the items that we want to have changes during installation. In fact, in this method, an XML file is used to configure the installation steps and services installed in Windows. In other words, the use of the Unattended.xml file creates an automation process during installation, preventing the need to select multiple options and avoiding the tedious steps usually required during setup. This method is an unusual but standard method that has been introduced by Microsoft. More information is available on Microsoft's official website at the following address:

https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/update-windows-settings-and-scripts-create-your-own-answer-file-sxs?view=windows-11

There are various tools available on the internet for generating Unattended files. Some of them are online, while others are offline. One of the online tools for creating this file is the following website:

https://schneegans.de/windows/unattend-generator

After opening the above address, we are presented with the following page:

![Image](assets/en/06.webp)

As mentioned at the top of the page, this method can be used for installing Windows 10 and 11. In the first step, we select the Windows language. If we need to add a second or even a third language to the list of Windows display and keyboard languages, we can use the box below:

![Image](assets/en/07.webp)

In the next step, we select the desired location.

![Image](assets/en/08.webp)

At this stage, we can also specify the processor architecture for the computer. In this step, we can:

A: Decide whether to ignore Windows security features, such as TPM and Secure Boot. The Secure Boot feature ensures that if any core Windows files are tampered with during the boot process, the issue is detected and their execution is prevented. This feature also helps protect the system from installing malicious updates on Windows. Enabling the option to bypass these features is sometimes unavoidable on certain computers, especially older models. However, it is generally recommended to keep features like Secure Boot enabled.

B: Ignore the requirement for an internet connection to complete the process. This is useful in situations where a wired LAN connection is not available, because in most cases, the wireless card is not yet recognized during Windows installation, and internet access via cable is required. Activating this option resolves issues related to this step.

In the next step, we can choose a name for the computer.

![Image](assets/en/09.webp)

We can also allow Windows to choose a name for the system. In this step, we can select the type of Windows, whether compressed or uncompressed, or let Windows determine the appropriate version based on the computer’s specifications. The time zone can also be set at this stage.

The next step involves partition settings:

![Image](assets/en/10.webp)

At this stage, we can specify the partition type for installing Windows, as well as the required settings for installing the Windows Recovery Environment. By selecting the first option, the partition selection and partitioning are postponed to the time of Windows installation, and during setup, these questions will be asked just like in the normal installation method.

In this step, we select the version of Windows to install:

![Image](assets/en/11.webp)


If a product key is available, it can also be entered at this stage.

The next step involves configuring the Windows login account:

![Image](assets/en/12.webp)

At this stage:

A: We can define a name and password for the admin account. It is also possible to create multiple user or admin accounts.

B: Here, we specify which account to log into the first time after Windows installation. The different options for this section are shown in the image.

The next step involves configuring password and host file settings:

![Image](assets/en/13.webp)

At this stage, we determine whether passwords should have an expiration period. Additionally, this section includes security settings related to failed login attempts, which can be enabled or disabled based on your needs.

At the bottom of this section, there are settings for file display. None of these options are available during a standard Windows installation and must be configured after installation. In contrast, with the Unattended installation method, these settings are easily accessible.

The next step involves configuring Windows security settings:

![Image](assets/en/14.webp)

At this stage:

A: Windows Defender can be enabled or disabled. This feature acts like security software in Windows and helps prevent the execution of malicious files, certain network attacks, and more.

B: Automatic Windows updates can be disabled. This is one of the common challenges faced by Windows users!

C: This section allows enabling or disabling UAC (User Account Control). This feature prevents suspicious applications from running with elevated permissions for reading and writing.

D: This feature is used by Windows to detect potentially harmful software.

E: Enable or disable support for long paths in Windows applications, such as PowerShell and others.

F: Enable or disable Remote Desktop for accessing the system remotely.

Depending on the Windows version being used, some of these features may or may not be supported.

The next step involves configuring the icons:

![Image](assets/en/15.webp)

In this section:

A: Desktop icons are listed, which can be added or removed as needed.

B: Start menu icons are listed, which can also be added or removed based on requirements.

C: This section allows configuring whether virtualization-related tools are installed or not. This option is specific to Windows 11 and does not apply to Windows 10.

The next step involves configuring Wi-Fi settings:

![Image](assets/en/16.webp)

In this section, Wi-Fi network settings can be configured. As mentioned earlier, in most cases, the Wi-Fi card is not recognized during Windows installation, so connecting during setup is usually not possible. However, by configuring this section, if the wireless card is detected, the system can connect to the internet.

The next step involves an important setting:

![Image](assets/en/17.webp)

In this section, we specify whether system problem information should be sent to Microsoft or not.

The next step involves configuring default applications:

![Image](assets/en/18.webp)

In this section, we can choose any applications that we do not want to be installed by default. For example, we can opt not to install Cortana or Copilot.

The next step involves security settings related to application execution:

![Image](assets/en/19.webp)

By applying WDAC settings, the execution of certain applications can be prevented.

Finally, after applying the desired settings, the generated XML file can be downloaded:

![Image](assets/en/20.webp)

By clicking on Download XML File, the autounattend.xml file is downloaded. To use this file, simply mount the downloaded ISO on a USB drive, place the autounattend.xml file in the root directory, and then proceed with the Windows installation.

One of the tools available for creating a bootable USB drive is Rufus.

![Image](assets/en/21.webp)

In this software, after selecting the desired USB drive and the appropriate ISO file, we click on Start.

![Image](assets/en/22.webp)

At this stage, we disable all options, as having them enabled can cause conflicts when using the generated Unattend file. After the files are copied to the USB drive, we place the autounattend.xml file in the root directory:

![Image](assets/en/23.webp)

At this point, the USB drive is ready for use to install Windows automatically, and the installation can be started using this drive.

If you need to install Windows on a virtual machine, you can use software to create and edit ISO files. One such software is AnyBurn. After extracting the contents of the ISO file downloaded from the Microsoft website, place the autounattend.xml file in the root directory. Then, using AnyBurn, create a new ISO with the updated contents. On the main page of the software, select "Create Image from File/Folder":

![Image](assets/en/24.webp)

On the next page, select all the files extracted from the ISO along with the autounattend.xml file.

![Image](assets/en/25.webp)

In this step, we configure the settings to make the ISO file bootable:

![Image](assets/en/26.webp)

At this stage, the path to the bootfix.bin file must be set to make the ISO bootable. This file is located in the root of the ISO, inside the boot folder. It is also recommended to enable both ISO9660 and UDF options in the Properties section.

![Image](assets/en/27.webp)

After this step, clicking Next will create the ISO file. This file can be used in virtualization software such as Oracle VirtualBox.
