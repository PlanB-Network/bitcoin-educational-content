---
name: KeePass
description: 如何設定本機密碼管理器？
---
![cover](assets/cover.webp)


在數位時代，我們需要管理眾多線上帳戶，涵蓋日常生活的各個層面，包括銀行、金融平台、電子郵件、檔案儲存、健康、行政管理、社交網路、電子遊戲等。


為了在每個帳戶上認證自己，我們使用一個識別碼，通常是電子郵件 Address，再加上一個密碼。面對無法記住大量獨特密碼的問題，我們可能會重複使用相同的密碼，或稍微修改常用的密碼基礎，使其更容易記住。但是，這些做法會嚴重影響您帳戶的安全性。


密碼要遵循的第一個原則是不要重複使用。每個線上帳號都應該使用獨一無二且完全不同的密碼來保護。這一點很重要，因為如果攻擊者成功破解了您的一個密碼，您不希望他們有權存取您的所有帳戶。為每個帳戶設定獨一無二的密碼可以隔離潛在的攻擊，並限制其範圍。例如，如果您在電子遊戲平台和電子郵件中使用相同的密碼，而該密碼透過與遊戲平台相關的網路釣魚網站被洩露，攻擊者就可以輕易存取您的電子郵件，並控制您所有其他的線上帳戶。


第二個基本原則是密碼的強度。如果密碼很難被暴力破解，也就是說很難通過嘗試和錯誤來猜測，那麼這個密碼就被認為是強大的。這意味著您的密碼必須盡可能隨機、長且包含多種字符（小寫、大寫、數字和符號）。


在日常生活中應用這兩項密碼安全原則（唯一性和穩健性）可能會很困難，因為幾乎不可能為我們的所有帳戶記憶一個唯一、隨機和強大的密碼。這就是密碼管理器發揮作用的地方。


密碼管理器可生成並安全地儲存強大的密碼，讓您無需個別記憶即可訪問所有線上帳戶。您只需要記住一個密碼，即主密碼，就可以存取管理器中儲存的所有密碼。使用密碼管理器可以提高您的線上安全性，因為它可以防止重複使用密碼，並系統地生成隨機密碼。但它也能集中存取您的敏感資訊，簡化您日常使用帳戶的方式。

在本教程中，我們將學習如何設置和使用本機密碼管理器來增強您的在線安全性。在此，我會向您介紹 KeePass。但是，如果您是初學者，而且希望擁有一個能夠在多個裝置上同步的線上密碼管理器，我建議您參考我們關於 Bitwarden 的教學：

https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

---

*注意：密碼管理器是儲存密碼的好幫手，但 ** 您絕對不能將 Bitcoin Wallet 的 Mnemonic 短語儲存其中！** 請記住，Mnemonic 短語應該專門以實體格式儲存，例如紙張或金屬。


---

## KeePass 簡介


KeePass 是一款免費且開放原始碼的密碼管理器，非常適合想要免費且安全的本機管理解決方案的使用者。它是安裝在個人電腦上的軟體，如果不加裝外掛程式，就不會與網際網路溝通。這與我們在之前的教學中介紹過的 Bitwarden 完全不同。Bitwarden 與 KeePass 不同，它允許在多個設備上同步，因此需要將密碼存儲在線上服務器上。


預設情況下，KeePass 不支援使用 Bitwarden 等瀏覽器擴充套件；因此，您需要手動複製並粘貼軟體中的密碼。雖然這看起來像是一種限制，但複製和粘貼密碼而不是使用自動填寫對您的在線安全是一種很好的做法。


KeePass 的設計既輕巧又易於使用，同時遵守高安全標準。該軟件在本機對您的資料庫進行加密，為您的憑證提供最佳保護。KeePass 也是唯一通過 ANSSI（法國網絡安全機構）驗證的密碼管理器。


KeePass 的主要優勢之一是其靈活性。它可以以多種不同的方式使用，例如在 USB 隨身碟上使用，而無需安裝在電腦上。此外，由於其 [外掛環境](https://keepass.info/plugins.html)，KeePass 可以進行定制以滿足更多特定需求。

![KEEPASS](assets/notext/01.webp)

## 如何下載 KeePass？


KeePass 的安裝過程因您使用的作業系統而異。對於 Windows 或 Linux 用戶，安裝過程相對簡單。但是，如果您使用的是macOS，由於KeePass是在.NET平台上開發的，而macOS不直接支援.NET平台，因此需要額外的步驟。因此，您需要配置一個相容的環境，讓 KeePass 在 Apple 裝置上執行。


對於 Debian/Ubuntu 使用者，請開啟終端機，並輸入下列指令：


```bash
sudo apt-get update

sudo apt-get install keepass2

```

For Fedora:

```

sudo dnf install keepass

```

For Arch Linux:

```

sudo pacman -S keepass

```

If you are on a Windows computer, go to the [official KeePass download page](https://keepass.info/download.html), and download the latest version of the installer:
![KEEPASS](assets/notext/02.webp)
Click on the downloaded file to run it, then follow the instructions of the setup wizard to complete the installation (see next section).

For macOS users, the installation is a bit more complex. If you wish to use the original version of KeePass as on Windows, follow the instructions below. Otherwise, you can opt for [KeePassXC](https://keepassxc.org/), an alternative version compatible with macOS, which offers a slightly different interface.

To use KeePass, you will need a runtime environment for .NET applications. I recommend installing Mono for this. Go to the [official Mono page](https://www.mono-project.com/download/stable/#download-mac) in the "*macOS*" section, and click on the link to download the installation package (`.pkg`).
![KEEPASS](assets/notext/03.webp)
Open the downloaded `.pkg` file and follow the instructions to install Mono on your Mac.
![KEEPASS](assets/notext/04.webp)
Next, go to the official KeePass website and download the latest portable version in `.zip` format.
![KEEPASS](assets/notext/05.webp)
After downloading the `.zip` file, double-click to extract it. You will get a folder containing several files, including `KeePass.exe`. Open a terminal, navigate to the KeePass folder (replace `xx` with the version number):

```

cd ~/Downloads/KeePass-2.xx

```

And finally, run KeePass with Mono:

```

mono KeePass.exe

```