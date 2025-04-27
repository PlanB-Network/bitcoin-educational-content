---
name: Lipa
description: 設定和使用 Lipa lightning 移動 Wallet
---
![cover](assets/cover.webp)


Bitcoin Lightning Wallet 是一種行動應用程式，可在 Bitcoin 的 Lightning Network 上進行即時、低成本的交易。與主 Blockchain (On-Chain) 上的交易不同，Lightning 付款幾乎是瞬間完成，且所需費用極低，因此特別適用於日常的小額付款。


Lightning 電子錢包和所有移動電子錢包一樣，被認為是 "Hot "電子錢包，因為它們連接到互聯網。因此，它們主要用於管理您日常花費的小額資金。如果金額較大，最好使用硬體錢包等更安全的儲存解決方案。


如果您想進一步了解 Lightning Network 並瞭解其技術運作方式，我建議您參加此課程：


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

在本教程中，我們將介紹**Lipa**，這是瑞士開發的一款簡單有效的 Lightning Wallet。


## 介紹 Lipa


Lipa 是一款非監控的 Lightning Wallet，以其簡單的使用方式和不雜亂的 Interface 而與眾不同。它由瑞士團隊開發，強調保密性和初學者的易用性。


主要功能包括




- 直覺式使用者 Interface
- 自主 Lightning 通道管理
- 支援 LNURL 通訊協定
- 可直接在應用程式中購買比特幣


## 安裝和設定 Lipa


第一步是下載 Lipa 應用程式。目前，它只適用於 iOS ：




- [For Apple](https://apps.apple.com/app/lipa-Bitcoin-lightning/id1602180066)


Android 版本目前正在開發中，很快就會推出。


![Installation de Lipa](assets/fr/01.webp)


啟動應用程式後，您會進入主畫面，其中提供兩個選項：




- 建立新的 Wallet
- 從備份回復現有的 Wallet


選擇選項後，應用程式會提示您啟用通知。這一步很重要，因為通知對 .NET Framework 是必要的：




- 收到付款時會收到警示，即使應用程式已關閉也是如此
- 瞭解透過其整合解決方案購買 Bitcoin 所涉及的步驟


之後，應用程式會透過一系列的介紹畫面展示其主要功能：




- 無縫收款**：即使關閉應用程式，使用者仍可接收 Bitcoin 付款，保證可靠性與便利性。
- 非托管 Lightning 位址**：Lipa 現在支援非託管 Lightning 位址，讓使用者可以完全控制自己的比特幣，從而增強隱私和安全性。
- 控制分析資料** ：由於透明度和機密性至關重要，使用者可以檢視收集的資料類型，並選擇分享偏好。
- 透過電話號碼發送**：不需要複雜的地址 - 只需選擇聯絡人、輸入金額，即可直接將 bitcoins 傳送至其電話號碼。


應用程式在穩定性、安全性和可靠性方面也持續改進，以確保最佳的使用者體驗。


## 應用導覽


Lipa 的 Interface 包含 4 個主要標籤，可透過螢幕底部的導覽列存取：


![Navigation principale](assets/fr/02.webp)




- 首頁**：顯示您目前的餘額和交易記錄
- 掃描器**：可讓您掃描 QR 代碼進行付款
- 地圖**：顯示您所在地區接受 Bitcoin 的企業的互動地圖
- 設定**：存取應用程式設定、備份和偏好設定


向下拉主畫面可存取額外的功能表：


![Menu supplémentaire](assets/fr/03.webp)


這個手勢會顯示其他功能，例如 ：




- 購買比特幣
- On-Chain Bitcoin 存款
- 建立 Lightning 發票以收取比特幣
- 閃電 Invoice 付款


## 儲存您的 Wallet


若要備份您的 Wallet，請移至「設定」標籤並選擇「復原詞組」。Lipa 使用恢復短語，必須仔細寫在實體媒介（紙張、金屬）上。如果您的手機遺失或被盜，該短語是恢復資金的唯一方法。為了驗證您的備份，應用程式會要求您確認短語中的 3 個隨機單詞。


![Backup](assets/fr/04.webp)


如需更多關於如何正確備份和管理您的復原片段的資訊，我強烈建議您遵循此其他教學，特別是如果您是初學者的話：


https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## 接收比特幣


要接收 bitcoins，您有兩個選項。若要存取這些選項，請返回主畫面並拉下畫面。然後您可以選擇 ：




- 選擇 "Transfer BTC "接收比特幣 On-Chain。然後只需用您的其他 Wallet 掃描 QR 代碼，即可完成交易。
- 選擇「請求」透過 Lightning Network 收取，並輸入您希望收到的金額。


在這兩種情況下，您都必須支付相當於金額 0.4% 的費用，如果申請必須開啟新的付款管道 (第一次付款難免會如此)，則費用約為 2,500 Sats。


![Recevoir des bitcoins on chain](assets/fr/05.webp)


![Recevoir des bitcoins lightning](assets/fr/06.webp)


## 發送比特幣


若要傳送 bitcoins，請前往主畫面，向下拉畫面並選擇「Pay」。然後只需：




- 輸入閃電 LNURL Address
- 掃描閃電 QR 代碼進行付款。


您也可以前往畫面下方的第二個標籤，直接掃描 QR 代碼。


![Envoi de bitcoins](assets/fr/07.webp)


## 購買比特幣


Lipa 提供直接在應用程式中購買 bitcoins 的可能性，費用為 1.5%。要進行購買，請前往主畫面，向下拉顯示功能表。然後選擇「購買 BTC」。三個介紹畫面將引導您完成購買過程。


![Menu d'achat](assets/fr/08.webp)


然後，只需輸入您將用於購買的帳戶的銀行詳細資料。選擇您的貨幣並輸入您的電子郵件 Address。


在載入畫面之後，您會發現要包含在您要進行的轉帳中的參考號碼，以及 Exchange 的銀行詳細資料。


![Sélection du montant](assets/fr/09.webp)


您只需使用您的銀行轉帳所需的金額，透過指示先前檢索的 RIB 設定轉帳，並在交易時指示參考，以便 Lipa 可以將此銀行流動與您的 Lipa Wallet 相關聯。


![Confirmation d'achat](assets/fr/10.webp)


## 優點與缺點


### 優點




- 直觀的 Interface
- 正確的服務收費
- 非保管
- 整合式 Bitcoin 採購解決方案
- BTCmap 整合
- NFC 支援


### 缺點




- 無法傳送比特幣 on chain
- 比平均付款時間略長


Lipa 是入門使用 Lightning Network 的絕佳選擇，特別適合尋求日常支付簡單解決方案的使用者。Interface 的易用性和簡潔性使其成為初學者的理想 Wallet，同時提供日常 Lightning 使用的基本功能。


## 資源




- [Lipa官方網站](https://lipa.swiss/)
- [Lipa 支援](https://getlipa.atlassian.net/servicedesk/customer/portal/1)