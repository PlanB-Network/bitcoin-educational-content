---
name: Satodime
description: 瞭解如何透過行動應用程式使用 Satodime
---
![cover](assets/cover.webp)



本指南將介紹 Satodime 手機應用程式的安裝、配置和使用。您將學會如何擁有您的卡片、建立保險箱、增加資金、解封和找回私人密碼鑰匙。附錄提供資源、最佳實務和技術說明。



## 簡介



**Satodime** 是由 **[Satochip](https://satochip.io/fr/)**所開發，是一種安全的不記名卡，能以有形且簡單的方式儲存 Bitcoin。它可作為自我保管的 Hardware Wallet，您可以完全控制自己的私密金鑰，而無需依賴第三方。它是開放原始碼並通過 EAL6+ 認證，最多可支援三個獨立的保險箱。



### 產品背景



Satodime 是一種 **carte au porteur，屬於實際擁有它的人**，無需事先註冊或識別。它能滿足安全、可攜式 Bitcoin 儲存的需求，讓任何持有卡片的人都能透過行動應用程式掃描卡片，使用卡片或轉移比特幣，以取得擁有權或解除保險箱封鎖。與紙鈔不同的是，它使用安全的晶片來 Seal 私密金鑰，只有在解封後才會顯示出來，這使得這張卡與現金類似，Ownership 是由實際擁有來決定的。它非常適合用來贈送比特幣作為禮物，方便比特幣在人與人之間的安全傳輸，而行動應用程式則利用 NFC 進行可存取的智慧型手機互動。





- 安全性**：私密金鑰產生並儲存在防篡改晶片中；可見狀態（密封、未密封、空）。
- 功能**：直接透過應用程式購買比特幣（Paybis 合作夥伴）；管理 Mainnet 和 Testnet。
- 開放原始碼**：程式碼採用 AGPLv3 授權，可在 GitHub 上驗證。



### 持續演進



應用程式會定期更新。請查看 Satochip 網站或商店以獲得更新。例如，可能會增加新的區塊鏈或購買功能。請查看 [Satochip GitHub](https://github.com/Toporin/Satodime-Applet) 了解持續的發展。



## 1.先決條件



在開始使用 **Satodime** 之前，請確定您已備妥下列物品：





- 相容的智慧型手機**：具備 NFC 功能的 Android 或 iOS 裝置。
- Satodime** 卡：新的或未初始化的。
- 網際網路連線**：下載應用程式。
- 基本知識**：瞭解私人/公用金鑰以及遺失的風險（不可逆轉）。
- 安全媒體**：記錄私人密碼鑰匙解封後的安全地點（紙張、金屬；絕非數位）。



## 2.安裝





- 下載申請表** ：
 - [App Store](https://apps.apple.com/be/app/satodime/id1672273462)** (iOS)
 - [Google Play 商店](https://play.google.com/store/apps/details?id=org.satochip.satodimeapp)** (Android)
 - 檢查開發商 (Satochip) 以避免詐騙。
 - Satodime 是**開放原始碼**。原始碼 ：[Satochip 的 GitHub](https://github.com/Toporin/Satodime-Applet)。





- 安裝並啟動應用程式**：必要時啟動手機上的 NFC。



![image](assets/fr/01.webp)



## 3.初始設定



### 3.1 啟動應用程式並進行掃描



開啟應用程式並按照精靈操作。將 Satodime 卡放在手機的 NFC 讀卡器上（通常在背面）。在整個操作過程中按住不放，以確保穩定的連接。





- 如果 NFC 無法運作，請檢查手機的設定。
- 祝酒證實成功：「成功閱讀」。



![image](assets/fr/02.webp)



一般而言，**下列所有操作都需要透過掃瞄 Satodime 卡來確認**



### 3.2 領取卡片 (*Ownership*)



首次使用時，請成為卡片的擁有者，以確保卡片安全：





- 按一下應用程式中的「*Take Ownership*」。
- 確認操作：這會產生一個唯一的擁有者金鑰。
- 再次掃描地圖以套用變更。
- 警告**：此步驟是不可逆的。請參考 [*Ownership* 文章](https://satochip.io/satodime-Ownership-explained/)。



![image](assets/fr/03.webp)




## 4.建立一個安全的



Satodime 支援最多 3 個保險箱。建立一個來儲存 Bitcoin ：





- 選擇一個空的保險箱（例如：保險箱 01）。
- 選擇 Blockchain (Bitcoin)。
- 按一下「*建立與 Seal*」。
- 掃描卡片至 generate 和 Seal 私密金鑰 (解封前未知)。
- 恭喜**：您的保險箱現在已封存，可以接收資金。



![image](assets/fr/04.webp)



![image](assets/fr/05.webp)



## 5.增加資金



密封後，將比特幣裝入保險箱：





- 選擇保險箱。
- 按一下「*新增資金*」。
- 複製公開的 Address 或掃描 QR 代碼。
- 從另一個 Wallet 傳送資金。
- 在 Blockchain 上確認後檢查餘額。
- 購買選項：按一下「*購買*」，直接透過 Paybis（Visa、Mastercard 等）購買。適用費用。



![image](assets/fr/06.webp)



## 6.拆封保險箱



若要存取私人密碼匙並將資金轉移至其他地方，請解除保險箱的封鎖：





- 選擇密封保險箱。
- 按一下「解除封印」。
- 確認警告：此操作是不可逆的。
- 掃描卡片即可解封。
- 保險箱設定為 "*Unsealed*"；現在可以檢視/匯出私人密碼匙。
- 警告**：一旦解封，就可以存取私人密碼匙。如果有人佔有您的智慧型手機，他們可以存取此密鑰，進而取回您保險箱中的資金（不可逆轉）。



![image](assets/fr/07.webp)



## 7.復原私人密碼匙



解封後，匯出金鑰供其他 Wallet 使用：





- 確保您在安全的環境中。
- 按一下「*Show private key*」。
- 選擇格式：Legacy、SegWit、WIF 等。
- 複製密鑰或掃瞄 QR 代碼。
- 安全性**：絕不共用您的私人密碼匙。離線儲存。
- 匯入與基金管理相容的 Wallet 軟體程式 (例如 Sparrow wallet 或 Electrum)。



![image](assets/fr/08.webp)





## 8.重設行李箱



重設保險箱會不可逆地刪除相關的私人密碼匙。換句話說，如果您沒有取得私人密碼匙的副本，或沒有將其匯入另一個 Wallet，重設保險箱將導致保險箱內的資金不可逆轉地損失。



![image](assets/fr/09.webp)



重設中繼器會使插槽為空，並為新中繼器做好準備。



## 9.轉移 Ownership



例如，若要透過 Satodime 提供比特幣，您必須 ：




- 以 Ownership 的卡片、
- 建立 Bitcoin 保險箱、
- 將 Satss 轉移到那裡、
- 轉移卡片 Ownership：下一位掃描卡片的人即成為卡片的擁有者、
- 將 Satodime 卡交給您選擇的人，並邀請他們下載應用程式，然後掃描卡片以取得 Ownership - 從而存取「儲存」在卡片上的 bitcoins。



![image](assets/fr/10.webp)




## 附錄



### A1.最佳實踐



若要安全使用 **Satodime** ：





- 保護卡片**：像對待現金一樣對待它；如果不是物主，遺失 = 損失資金。
- 金鑰備份**：解封後，將私人金鑰記錄在安全的實體媒體上。永遠不要數位化。
- 檢查狀態**：隨時掃描以確認卡片 Ownership 和保險箱的密封/非密封狀態。
- 保密性**：使用新地址；避免集中交換轉移。
- 更新**：透過商店隨時更新應用程式。
- 復原**：如果卡已遺失但擁有，資金在 Blockchain 上；如果未封存，請使用私密金鑰。



### A2.額外資源



特定於 Satodime ：




- [Satodime產品](https://satochip.io/fr/product/satodime/)
- [Mobile Guide](https://satochip.io/wp-content/uploads/2024/11/Satodime-FR-Short-tuto-app-mobile.pdf)



[Plan ₿ Network](https://planb.network/) 有關自我保管、私人金鑰等的教程。



**Save your recovery phrase** ：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Satochip (品牌的第一款產品) 的教學 :**



https://planb.network/tutorials/wallet/hardware/satochip-e9bc81d9-d59b-420d-9672-3360212237ba

**種子管理員教程：**



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

### A3.關於 Satochip



**官方連結** ：




- [Site Satochip](https://satochip.io/fr/)
- [GitHub](https://github.com/Toporin/Satodime-Applet)
- 支援：info@satochip.io



**Satochip**是一家比利時公司，專門開發用於管理和儲存比特幣及其他加密貨幣的硬體和軟體解決方案。其旗艦產品 Satochip Hardware Wallet 是配備 EAL6+ 認證 secure element 的 NFC 卡。除了 Mnemonic 短語和密碼管理器 Seedkeeper 之外，還有不記名卡 Satodime，Satochip 可針對使用者的需求提供全方位的產品。其裝置採用開放原始碼軟體，旨在使 Bitcoin 上的安全性平民化。