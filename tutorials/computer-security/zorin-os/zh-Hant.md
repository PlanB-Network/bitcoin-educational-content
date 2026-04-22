---
name: Zorin OS
description: 安裝和使用 Zorin OS 作為 Windows 現代替代方案的完整指南
---

![cover](assets/cover.webp)



## 簡介



作業系統 (OS) 是讓電腦運作的基本軟體：它管理硬體、軟體、安全性和使用者介面。


Zorin OS 是專為簡化從 Windows 過渡而設計的 Linux 發行版，同時提供開放原始碼軟體的優點：安全性、穩定性、隱私性和效能。



Zorin OS 以 Ubuntu LTS 為基礎，結合了高度的軟體相容性與熟悉的客製化介面，使其成為 Windows 的可靠且易於使用的替代方案。



## 為何選擇 Zorin OS？





- 熟悉的 Interface**：類似 Windows 的外觀（開始功能表、工作列）
- 輕鬆過渡**：專為來自 Windows 的使用者設計
- 增強安全性**：Linux 架構，較少暴露於病毒中
- 尊重隱私**：無侵擾性資料收集
- 最佳化效能**：在一般機器上運作良好
- Ubuntu LTS** 基礎：穩定性、定期更新與廣泛相容性
- 進階個人化**：透過 Zorin 外觀工具。



## 安裝與設定



### 1.先決條件



**所需設備：**





- 至少 **8 GB**（建議 12 GB）的 USB 密鑰；
- 至少有 **25 GB 可用磁碟空間的電腦**
- 網際網路連線（建議）。



### 2.下載 Zorin OS





- 請造訪官方網站：[https://zorin.com/os](https://zorin.com/os)



![Page de téléchargement Balena Etcher](assets/fr/03.webp)





- 選擇 **Zorin OS Core** (建議使用免費版本)



![Page de téléchargement Balena Etcher](assets/fr/04.webp)





- 下載 ISO 映像



Zorin OS 也提供 .NET 和 .NET 平台：





- Zorin OS Lite**（舊型電腦）
- Zorin OS Pro**（付費，具備進階功能與支援）



## 建立可開機 USB 密鑰



您可以使用多種工具，例如 Balena Etcher ：





- 下載並安裝 [Balena Etcher](https://etcher.balena.io/)。
- 開啟 Balena Etcher，然後選擇 Zorin ISO 映像。
- 選擇 USB 隨身碟作為目的地媒體。
- 按一下 Flash，等待程序完成。



![Utilisation de Balena Etcher](assets/fr/05.webp)



## 按鍵開機與 BIOS 存取



關閉要安裝 Zorin OS 的電腦，然後插上 USB 密鑰。


當您的電腦啟動時，請存取 BIOS (`ESC`、`F9` 或`F11`，視不同品牌而定)，並選擇 USB 隨身碟為開機裝置，然後按下`Enter`以啟動開機程序。





- 啟動時，選擇 ** 嘗試或安裝 Zorin OS**。



![capture](assets/fr/08.webp)





- 如果您有 NVIDIA 顯示卡，請選擇 ** 嘗試或安裝 Zorin OS (現代 NVIDIA 驅動程式)**。
- 檢查檔案時請稍候。



![capture](assets/fr/09.webp)





- 在 Zorin OS 安裝程式中，選擇語言 **法文**，然後按一下安裝 **Zorin OS**。



![capture](assets/fr/10.webp)





- 選取鍵盤配置。



![capture](assets/fr/11.webp)





- 勾選 ** 在安裝 Zorin OS 期間下載更新** 及 ** 安裝顯示卡和 Wi-Fi 硬體以及其他媒體格式的第三方軟體**。



![capture](assets/fr/12.webp)





- 若要在整個磁碟上安裝 Zorin OS：選擇 ** 刪除磁碟並安裝 Zorin OS**。



![capture](assets/fr/14.webp)



要在安裝 Windows 的同時安裝 Zorin OS (雙重開機) ：





- 選擇 ** 安裝 Windows 開機管理器旁邊的 Zorin OS**。



![capture](assets/fr/15.webp)





- 如果您尚未分割磁碟，請選擇您要分配給 Zorin OS 的磁碟空間，然後按一下 ** 立即安裝**。



![capture](assets/fr/16.webp)





- 確認光碟上的變更兩次。



![capture](assets/fr/16.webp)



![capture](assets/fr/17.webp)





- 選擇地理區域 **巴黎**。



![capture](assets/fr/18.webp)





- 建立您的使用者帳號，並為您的電腦命名。



![capture](assets/fr/19.webp)





- Zorin OS 正在安裝中，請稍候。



![capture](assets/fr/20.webp)





- 安裝完成後，按一下 ** 立即重新啟動**。



![capture](assets/fr/21.webp)





- 移除 USB 安裝鍵，然後按 Enter。



![capture](assets/fr/22.webp)



## 發現和使用 Zorin OS



### 首次啟動



啟動電腦時，您會進入 GRUB - Linux 開機管理程式。預設選取 **Zorin OS**；30 秒後，它會自動啟動。



![capture](assets/fr/23.webp)



如果您已將 Zorin OS 安裝為 Windows 的雙重開機，您可以選擇 **Windows 開機管理員**，開機至 Windows。



使用您的使用者帳號登入 ：



![capture](assets/fr/24.webp)



首次啟動時，會啟動 **Welcome to Zorin OS** 應用程式，協助您發現您的新作業系統。



![capture](assets/fr/25.webp)



![capture](assets/fr/26.webp)



![capture](assets/fr/27.webp)



![capture](assets/fr/28.webp)



![capture](assets/fr/29.webp)



![capture](assets/fr/30.webp)



![capture](assets/fr/31.webp)



![capture](assets/fr/32.webp)





### 更新系統



Update Manager（更新管理器）很快就會開啟，讓您知道有可用的更新。按一下 ** 立即安裝** 按鈕即可安裝。



![capture](assets/fr/33.webp)



您可以在 **Software** > Updates 應用程式中手動檢查更新：



![capture](assets/fr/34.webp)



### 個人化



使用 Zorin OS 的第一件事，就是選擇您最喜歡的**桌面佈局。您會發現布局與 Windows 上的布局類似（Pro 版本的布局更類似）。



若要這樣做，請開啟 **Zorin Appareance** > **Type** ：



![capture](assets/fr/35.webp)



然後開啟 ** 設定**，自訂您的系統：


**聲音 - 設定 - Zorin OS



![capture](assets/fr/36.webp)



**線上帳戶 - 設定 - Zorin OS



![capture](assets/fr/37.webp)



### 應用



安裝應用程式有幾種方式：





- Software**, Zorin OS 應用程式商店。應用程式有幾種來源：Apt、Flatpak 和 Snap。



![capture](assets/fr/38.webp)



![capture](assets/fr/39.webp)





- apt** 安裝 (命令列) ：



```bash
sudo apt install gparted
```



![capture](assets/fr/40.webp)



有關在 Zorin OS 安裝應用程式的詳細資訊，請參閱此頁面：[Install Apps (zorin.com)](https://zorin.com/help/install-apps/).



### Windows 應用程式



若要安裝 Windows 應用程式，請先透過終端機安裝 **zorin-windows-app-support** 套件：



```bash
sudo apt install zorin-windows-app-support
```



如需相容 Windows 應用程式及其相容性等級的清單，請參閱 [Wine 應用程式資料庫] 頁面 (https://appdb.winehq.org/)。在那裡您會找到以下徽章，與相容性等級相對應 (從最佳到最差)：白金、金、銀、銅和垃圾。



若要安裝 Windows .exe 或 .msi 應用程式，您有兩個選項：





- 開啟 **PlayOnLinux**，按一下 ** 安裝** 按鈕，瀏覽相容的應用程式和遊戲。



![capture](assets/fr/41.webp)





- 按兩下應用程式的 **.exe 或 .msi** 檔案，讓安裝程式引導您。



![capture](assets/fr/42.webp)



![capture](assets/fr/43.webp)



## 結論與其他資源



Zorin OS 是 Windows 的可靠、經濟實惠的替代方案，結合了簡單性、安全性和隱私性。



它可讓您順利過渡到 Linux，而不會犧牲舒適度或生產力。



為了進一步保護您的數位生活，我們建議您使用隱私權友善的服務，尤其是加密通訊：



https://planb.academy/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2