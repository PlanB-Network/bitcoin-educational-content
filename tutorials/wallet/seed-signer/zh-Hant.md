---
name: seed 簽署人

description: 設定您的 seed 簽章器
---

![cover](assets/cover.webp)


## 材質：


**Raspberry Pi Zero (版本 1.3)**


若要使用完全空氣封裝的解決方案，請務必使用沒有 WiFi 或藍牙功能的 1.3 版本，但任何 Raspberry Pi 2/3/4 或 Zero 型號都可以使用。


注意：Raspberry Pi 通常不附帶引腳；引腳需要焊接上去，或者使用稱為「GPIO Hammer」的東西。

GPIO 錘子


如果您的焊接技術不夠好，或者您還沒有烙鐵，那麼您可以使用「GPIO Hammer」來替代焊接。


**Hat LCD WaveShare 1.3 吋，螢幕 240 × 240 像素**。


WaveShare LCD Hat 1.3″ 240×240 pxl LCD


**註：** 請謹慎選擇 Waveshare 螢幕；請確認購買解析度為 240×240 像素的機型。


**相容於 Pi Zero 的相機模組**


Raspberry Pi 攝影機 Aokin/AuviPal 5MP 1080p 配備 OV5647 感應器的視訊攝影機模組；其他品牌的 OV5647 感應器模組也應該可以使用，但可能與 Orange Pill 外接盒不相容。


**Note:** 您需要專門與 Raspberry Pi Zero 相容的相機綵帶線。


**容量至少為 4 GB 的 microSD 卡**


廣泛資源：https://seedsigner.com/explainers/


## 軟體：


軟體安裝


1.下載最新的 "seedsigner_x_x_x.img.zip" 檔案

最新版本

2.解壓縮「seedsigner_x_x_x.img.zip」檔案

3.使用 Balena Etcher 或類似工具將解壓縮的 .img 映像檔寫入微 SD 卡中

BALENA ETCHER

4.在 SeedSigner 中安裝 microrosd 卡。

SeedSigner GPG 公開金鑰

seedigner_pubkey.gpg


## 教學影片


_指南取自 Southerbitcoiner，由 Cole 創建_


### 包含 SeedSigner 的視訊指南集：開放原始碼、DIY Hardware Wallet/Signing 裝置


![image](assets/1.webp)


SeedSigner 是一個 Bitcoin Signing Device，您可以從頭開始建立。聽起來很困難，但這個 4 部分的系列應該可以幫到您:)我建議您先觀賞第 1 和第 2 部分，然後決定要使用桌上型電腦 (觀賞第 3 部分) 還是行動裝置 (觀賞第 4 部分)。


您需要知道的一切都會在下面。其他有用的連結包括 SeedSigner 的網站、Github、Keybase、最新發行版和硬體需求。


### 第 1 部分：如何建立 SeedSigner：


在這個影片中，我會告訴您如何下載和驗證 SeedSigner 軟體、需要哪些零件，以及如何組裝您的 SeedSigner。


![video](https://youtu.be/mGmNKYOXtxY)


### 第二部分：測試您的 SeedSigner


在我使用 SeedSigner 之前，我做了一些測試來確保它沒有做任何惡意的事情。我想我也應該分享這個步驟。以下是如何驗證您的 SeedSigner 匯出正確的 Wallet (xpub)、如何驗證 SeedSigners 骰子滾動的數學，以及如何驗證 SeedSigners bip-85 子種子。


![video](https://youtu.be/34W1IyTyXZE)


### 第 3 部分：如何在 Sparrow Wallet 中使用 SeedSigner (桌上型電腦)


SeedSigner 能夠產生種子並簽署 Bitcoin 交易。但它本身無法建立交易。您需要在 SeedSigner 中使用 Wallet 「協調器」。這就是如何將 Sparrow Wallet 與 SeedSigner 搭配使用：


![video](https://youtu.be/IQb8dh-VTOg)


第 4 部分：如何使用 SeedSigner 與 Blue Wallet (手機)


SeedSigner 能夠產生種子並簽署 Bitcoin 交易。但它本身無法建立交易。您需要與 SeedSigner 一起使用 Wallet 「協調器」。這是如何將 Blue Wallet 與 SeedSigner 搭配使用：


![video](https://youtu.be/x0Ee35Ct0r4)


這些就是目前所有的 SeedSigner 指南！如果您認為我遺漏了什麼，請告訴我。這些都在我的潛在影片清單上：



- SeedSigner 總體評論。它是簽名裝置的好選擇嗎？優點/缺點？
- 如何在 SeedSigner 中使用 Bip-85
- 如何成為 SeedSigner 的吉姆叔叔


覺得這些很有價值嗎？請考慮寄送小費，以資助未來的影片：

https://www.southernbitcoiner.com/donate/