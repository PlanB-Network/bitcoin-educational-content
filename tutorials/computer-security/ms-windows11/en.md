---
name: WINDOWS 11
description: Microsoft windows 11 installation
---
![cover](assets/en/cover.webp)

___

In this tutorial, we’ll walk you through the step-by-step process of installing Microsoft Windows 11 on a VirtualBox virtual machine (version 7.1.10).

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

![Image](assets/en/06.webp)

## II. Second : VirtualBox!
The next step is to install the downloaded file in VirtualBox. In this tutorial, I am using version 7.1.10 of the software.
After opening VirtualBox, go to the Machine menu and select New:

![Image](assets/en/07.webp)

After choosing a suitable name and location for the virtual machine, in the second field, specify where the virtual machine’s files (hard drive location) will be stored.

![Image](assets/en/08.webp)

In the third field, add the .iso file downloaded from the Microsoft website.
In the fourth field, choose the appropriate Windows version. In this tutorial, I selected Windows 11 Education.
If the Skip Unattended Installation option is selected, you can proceed with the installation without entering a product key and activate Windows later. Otherwise, you need to configure this section before continuing.

![Image](assets/en/09.webp)

In this step, enter your desired username and password for the account, and also input the purchased Product Key in the corresponding field.
Other hardware settings, such as the minimum 4 GB of RAM, are suitable as default.
After clicking Finish, you can start the virtual machine. 

## III. Third : Start It!
Once it boots, you will see the following screen.
Here, select the Windows installation language and the time zone.

![Image](assets/en/10.webp)

In this step, choose the input (keyboard) language.

![Image](assets/en/11.webp)

In the next step, choose whether to install a new version of Windows or to upgrade/repair the existing one. Since we are installing a new Windows, select the first option.

![Image](assets/en/12.webp)

In the following step, you are asked to enter a Product Key. Click I don’t have a Product Key to skip this step.

![Image](assets/en/13.webp)

In the next step, select the Windows edition you want to install.

![Image](assets/en/14.webp)

After this step, read the terms and agreement, and if you agree, click the Accept button.
Otherwise, cancel the Windows installation!

![Image](assets/en/15.webp)

In the next step, you need to select the hard disk for the installation.
Since we are installing on a virtual machine, this step is not very **critical**. However, if you are installing on a physical machine, complete this step carefully, as mistakes here could **lead to data loss on your hard drive**.

![Image](assets/en/16.webp)

After this, click Install to start the installation process.

![Image](assets/en/17.webp)

The duration of this step depends on the speed and power of your hardware.
After this step is complete, the virtual or physical machine will restart.

![Image](assets/en/18.webp)

During this stage, the system may restart one or more times.

![Image](assets/en/19.webp)


After this process is complete, the system will restart, and the following screen will appear:

Here, you can correct your country/region if it was selected incorrectly.

![Image](assets/en/20.webp)

In the next step, you can adjust the system input language.

![Image](assets/en/21.webp)

In the next step, if you need to add a new input language, you can do so.

![Image](assets/en/22.webp)

In the next step, an internet connection is required to download some drivers.
If you prefer, you can continue the remaining steps without an internet connection.
After this, click Install to start the installation process.

![Image](assets/en/23.webp)

The duration of this step depends on the speed and power of your hardware.

In the next step, enter your desired account name.
This account, in addition to being an Administrator, will have full access.

![Image](assets/en/24.webp)

In the next step, you can set a password for the created account, or leave the field blank.

![Image](assets/en/25.webp)

In the next step, you will see the privacy settings.
Here, you can limit access to various privacy-related features, such as location and more.
For example, if location access remains enabled, you will receive information such as weather updates, traffic, and more.

![Image](assets/en/26.webp)

After completing all the steps, the following screen will appear:

![Image](assets/en/27.webp)

At this stage, Windows is finalizing the installation.
Once this step is complete, you will see the following screen:

![Image](assets/en/28.webp)



## Congratulations!
   
**You have successfully installed Windows!**


