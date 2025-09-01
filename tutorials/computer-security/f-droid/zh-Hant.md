---
name: F-Cold
description: 免費與開放原始碼應用程式目錄。
---

![cover](assets/cover.webp)



在數位時代，大型企業和機構正努力讓網際網路更加集中化，將網際網路的控制權交到自己手中，進而妨礙所有使用者的隱私和自由。這不是烏托邦，它已經在發生了。身為一個 bitcoiner，去中心化、尊重隱私和個人自由是你所堅持的原則，尤其是在你每天使用的工具上。Android 與 iOS 不同，多年來一直允許多個應用程式商店在其生態系統內共存，讓您可以自由地從您喜愛的來源尋找並安裝應用程式。



在本教程中，我們將介紹 F-droid，這是一個應用程式目錄，可替代 Google Play Store 和 Microsoft Store 等應用程式商店。



## 開始使用 F-Droid



F-Droid 是一個應用程式與工具商店，可讓您在 Android 平台上安裝免費的開放原始碼應用程式。F-droid 本身是由 Ciaran Gultnieks 及其他幾位貢獻者於 2010 年開始的開源專案。該專案的主要目的是讓開放原始碼應用程式能夠被存取，並讓開放原始碼專案的發起人能夠找到一個平台，讓他們不必參考 Google Play 商店就能發佈自己的工具。



不幸的是，F-Droid 並非 iOS 上的應用程式，其中包含許多專為 Android 系統設計的工具。



您可以從 [官方網站](https://f-droid.org/) 下載 APK 格式的 F-droid，然後手動安裝到您的 Android 手機上。



![download](assets/fr/02.webp)



在 Android 上，請確定您已授予下載 F-Droid 的瀏覽器的安裝權限。



安裝完成後，F-Droid 會啟動開放原始碼應用程式目錄的更新，以豐富商店中的應用程式。



![repositories](assets/fr/03.webp)



現在您可以在手機上安裝應用程式，而無需透過 Google Play 商店。



## F-Droid 書店



在應用程式商店中，您可以找到多種類別的應用程式，以滿足您的需求。在 ** 類別** 標籤中，您會找到超過 20 種應用程式，從瀏覽器到自由文字編輯器，而且都只需要您提供最少的資訊。



您想要安裝特定的應用程式嗎？按一下 **Search** 按鈕，然後輸入您要找的應用程式名稱。



![search](assets/fr/04.webp)



F-Droid 提供您想要安裝的每個應用程式的全面資訊。



點擊應用程式，您會發現，除其他事項外 ：




- 最新可用版本中新增的功能和變更
- 詳細介紹應用程式、其功能、使用原因以及該專案背後的開放原始碼社群。



![features](assets/fr/05.webp)





- 專案使用的授權、與原始碼的連結，以及使用應用程式時遇到的問題
- 應用程式所需的權限



![permissions](assets/fr/06.webp)



請參閱 Thunderbird 教學：



https://planb.network/tutorials/computer-security/communication/thunderbird-91d02325-0361-4641-b152-8975890284a8

F-Droid 提供您所需的所有資訊，讓您決定使用應用程式是否能保護您的資料並提高您的隱私。掃描所有您要使用的應用程式，然後按一下 ** 安裝** 按鈕，下載並安裝您的應用程式。


在設定中啟用選項，授予 F-Droid 安裝權限。



![settings](assets/fr/07.webp)



## Exchange 您的應用程式



F-Droid 鼓勵實踐開放原始碼和社區貢獻，特別是透過其 **Near By** Exchange 選項。透過 .NET 與您周圍的使用者連線：




- 藍牙偵測；
- 相同的 Wi-Fi 網路；
- QR 碼或 IP:PORT Address 在瀏覽器中輸入。



有了這個選項，您只需幾個步驟就能與親朋好友分享和接收安裝在 Android 手機上的應用程式。



![swap](assets/fr/08.webp)



## 更新



在 ** 更新** 標籤中，請參閱可用更新的清單，並確保您也閱讀每個應用程式新版本的相關資訊，以瞭解您正在使用的版本是否有任何重大變更。



![updates](assets/fr/09.webp)



您也可以透過刷新頁面更新可用的應用程式清單 (向下捲動)。



## 新增您自己的應用程式



F-Droid 是一個開放原始碼專案，鼓勵大家貢獻以使用者隱私為優先的應用程式。您可以透過對 F-Droid GitLab 原始碼的貢獻，將您自己的 Android 行動應用程式加入商店。



您的應用程式必須是開放原始碼，例如在 GitHub 或 GitLab 上公開原始碼。


然後，您必須依照 F-Droid 提出的 [metadata template](https://f-droid.org/docs/Build_Metadata_Reference/)，準備一個描述您的應用程式的 YAML 檔案 (metadata)，包括使用該應用程式所需的所有資訊和權限。



在 [文件](https://f-droid.org/en/docs/) 的 ** 開發者** 部分，您可以找到在 F-Droid 上發佈和維護應用程式所需的所有資源。



### 誠信與安全



將應用程式放入開放原始碼通常是增加安全性的代名詞，但也有相當大的風險。如何確保 F-Droid 上的應用程式的原始碼沒有被惡意修改？



F-Droid 根據官方原始碼和編譯指示，在自己的伺服器上編譯應用程式。每個已發佈的應用程式都經過重建和驗證，以確保沒有受到損害。這可確保所提供的 APK 忠於開發者所公佈的原始碼。此外，透過 F-Droid 安裝的每個應用程式都經過數位簽章，然後將簽章指紋與應用程式開發人員在官方網站或 Git 儲存庫中公佈的指紋進行比較。



如果您喜歡本教學，請進一步瞭解我們的 IT 安全與資料管理課程：



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1