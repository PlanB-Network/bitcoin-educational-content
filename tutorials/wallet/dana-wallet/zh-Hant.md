---
name: Dana Wallet
description: 靜音付款的極簡組合 (BIP-352)
---

![cover](assets/cover.webp)



重複使用 Bitcoin 位址是對使用者機密性最直接的威脅之一。當收款人共用單一地址接收多筆付款時，任何觀察者都可以追蹤所有相關交易，並重建其財務歷史。這個問題特別會影響到那些希望公開顯示捐款地址，但又不損害自己或捐款人隱私的內容創造者、慈善團體或積極份子。



Dana Wallet 以優雅的解決方案回應這個問題：Silent Payments。這個於 2024 年推出的極簡、開放源碼 wallet，會產生一個可重複使用的靜態位址，同時保證收到的每筆付款最終都會出現在區塊鏈上的獨立位址上。寄件者不需要事先與收件者互動，外部觀察者也無法將個別交易連結在一起。在區塊鏈上，這些付款看起來就像完全普通的 Taproot 交易。



Dana Wallet 可在 Mainnet 和 Signet 上使用，但開發人員仍然認為它是實驗性的，並建議不要存入您不準備損失的資金。在本教程中，我們將在不冒任何真實資金風險的情況下，使用 Signet 版本來探索 Silent Payments。



## 什麼是 Dana Wallet？



### 理念與目標



Dana Wallet 採用「SP-first」方式：wallet 只會產生 Silent Payments 位址，並且只接受此類型的付款。您將無法使用此應用程式建立經典的 Bitcoin 位址 (傳統、SegWit 或 Taproot 標準)。這種刻意的限制可讓您專注於學習 BIP-352 通訊協定，而不會被其他功能分心。簡潔的介面刻意著重於易用性而非繁多的選項，即使是對 on-chain 機密概念一竅不通的使用者也能輕鬆上手。



該專案完全開放原始碼，使用 Flutter 開發行動介面，並使用 Rust 開發內部密碼邏輯。此架構結合了流暢的使用者體驗與密集掃描作業的最佳效能。



### 無聲付款如何運作？



無聲支付 (BIP-352) 是基於使用橢圓曲線 Diffie-Hellman 金鑰 Exchange (ECDH) 的精密加密機制。收款人會產生一個靜態位址 (在 mainnet 上以 `sp1...` 開頭，或在 Signet 上以 `tsp1...` 開頭)，該位址由兩個不同的公開金鑰組成：一個掃描金鑰 ($B_{scan}$) 用於偵測收到的付款，另一個花費金鑰 ($B_{spend}$) 用於花費收到的資金。這種分離方式可將支出金鑰保留在 wallet 硬體上，同時在連接的裝置上使用掃描金鑰。



當發送人想要付款時，他的 wallet 會結合他的輸入私人金鑰與收款人的公開掃描金鑰的總和，計算出一個共用的 ECDH 密碼。這個秘密會產生一個加密「調整」，加到收款人的消費金鑰上，為該交易建立一個唯一的 Taproot 位址。



收款人可以使用他的私人掃描金鑰和交易中可見的公開金鑰來複製這個計算（Diffie-Hellman 數學特性）。如此一來，他就能在不與寄件者事先互動的情況下，偵測並花費資金。



這種方法有幾個優點：




- 收款人保密性**：每筆付款的收款地址都不同
- 寄件者保密**：沒有連結付款的持久性識別碼
- 無需第三方伺服器**：協定可自主運作
- 無法區分的交易**：無聲支付看起來像普通的 Taproot 交易



主要的缺點是掃描的成本：收件人必須分析每筆新的 Taproot 交易，才能偵測出擬給他的交易。



如果您想了解更多關於 Silent Payments 的技術操作，我們建議您學習 BTC204 關於 Bitcoin 保密性的課程，其中有一章專門講述 Silent Payments：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## 支援的平台



Dana Wallet 以 Android 應用程式的形式提供。APK 可透過開發人員提供的專屬 F-Droid 套件庫、Obtainium 或直接從 GitHub 下載。對於 Linux 使用者，在技術上可以將 Flutter 應用程式編譯為桌面版。



此應用程式並未在 iOS 或透過官方商店（Google Play、App Store）推出，這反映出它的實驗性質及其專注於技術受眾。



## 安裝



### 必要的先決條件



若要在 Android 上安裝 Dana Wallet，您需要在安全設定中啟用「未知來源」選項的 Android 裝置。不需要帳號或註冊。



### 增加 F-Cold 押金



建議的方法是加入 Dana Wallet 專屬的 F-Droid 儲存庫。前往 `fdroid.silentpayments.dev`，您會在那裡找到儲存庫連結和要掃描的 QR 代碼。儲存庫目前提供 3 個應用程式：Mainnet 版本、Development 和 Signet。



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### 透過 F-Droid 安裝



在 Android 裝置上開啟 F-Droid 應用程式，然後透過右下方的圖示存取「設定」。選擇「儲存庫」以管理應用程式來源。按下「+」按鈕以新增儲存庫，然後掃描 QR 碼或貼上「https://fdroid.silentpayments.dev/fdroid/repo」連結。新增儲存庫後，您會看到 Dana Wallet 的三個可用版本。選擇「Dana Wallet - 書籤」，然後按「安裝」。



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## 初始設定



### 建立投資組合



首次啟動時，Dana Wallet 會顯示歡迎畫面，介紹其使命："沒有中間人的捐款收發」。按「開始」繼續。下一個畫面會介紹應用程式的三大優點：




- 輕鬆捐款**：數秒內即可開始接收捐款
- 預設的隱私權**：無需伺服器或複雜的基礎架構
- 類似電子郵件的體驗**：像收發電子郵件一樣簡單地收發比特幣



您可以選擇 "Restore 「還原現有的組合，或選擇 」Create new wallet "建立新的組合。按「建立新的 wallet」。



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



應用程式會產生復原短語，您應該仔細地在實體媒體上記下該短語。即使是沒有實際價值的測試資金，也要採用良好的備份作法。



### Interface 和參數



建立投資組合後，您會進入主介面，分為兩個標籤："交易」和「設定」。



交易**標籤會顯示您的比特幣餘額（及其兌換成幣值）、最近的交易清單，以及兩個操作按鈕：發送資金的 「支付 」和接收按鈕（下載圖示）。



設定**」標籤提供四個選項：




- 顯示 seed 詞組**：顯示您的復原詞組以供保管
- 變更法定貨幣**：變更顯示貨幣（預設為美元）
- 設定後端網址**：設定 Blindbit 伺服器網址 (請參閱下一節)
- 擦除 wallet**：從裝置中完全擦除 wallet



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### Blindbit 伺服器



Dana Wallet 使用稱為 **Blindbit** 的索引伺服器來偵測您的靜默支付。瞭解其運作方式對於評估應用程式的信任模式非常重要。



**我們為什麼需要伺服器？



若要偵測 Silent Payment，理論上您的 wallet 必須掃描每個區塊中的所有 Taproot 交易，並針對每個交易執行加密計算 (ECDH)。在手機上，此操作的運算量和頻寬都太密集。



Blindbit 伺服器透過預先計算所有 Taproot 交易的中間資料（稱為「調整」）來解決這個問題。您的 wallet 會下載這些調整資料（每筆交易 33 位元組），並執行**本地**的最終計算，以檢查付款是否屬於您。



**保密性**



不像傳統的 Electrum 伺服器會透露您的地址，Blindbit 伺服器不知道哪些付款是屬於您的。它向所有用戶提供相同的數據，並由您的手機執行最終的驗證。因此，您的資料對伺服器而言是保密的。



**預設伺服器



Dana Wallet 使用公共伺服器 `silentpayments.dev/blindbit/signet` (用於 Signet) 或 `silentpayments.dev/blindbit/mainnet` (用於 Mainnet)。如果您託管自己的伺服器，您可以在設定中變更這個 URL。



**架設您自己的 Blindbit 伺服器**



對於希望擁有完全主權的使用者，可以架設自己的 Blindbit Oracle 伺服器。這需要 ：




- 一個完整的 Bitcoin 核心節點 **非插箭** (非 pruned)
- 安裝 Blindbit Oracle (可在 GitHub 上取得：`setavenger/blindbit-oracle`)
- 約 10 GB 額外磁碟空間
- 技術技能（Go 編譯、伺服器配置）



Umbrel 或 Start9 尚未有套件應用程式。安裝方式暫時仍以手動方式為主。這個領域正處於積極的演進中，未來可能會出現更容易使用的解決方案。



## 每日使用



### 接收資金



要接收比特幣，請從主畫面按接收按鈕（下載圖示）。Dana Wallet 接著會在書籤上顯示您完整的 Silent Payment 位址，格式為`tsp1q...`。該介面提供多種選項：




- 顯示 QR 代碼**：顯示地址的 QR 代碼，方便掃描
- 分享**：透過手機應用程式分享位址
- 複製**：將位址複製到剪貼簿



如畫面所示，您可以在社交網路中公開分享此位址，而不會影響您的隱私。



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



要在 Signet 上獲得第一筆測試資金，請使用專用的 Silent Payments 龙头，可在 `silentpayments.de/faucet/signet`。複製您的地址 `tsp1...`，貼到龍頭上提供的欄位，然後驗證請求。等待區塊被挖出 (在 Signet 上約 10 分鐘)。



### 發送付款



若要傳送資金，請從主畫面按下「付款」按鈕。選擇收款人 "畫面會出現，有三個選項可指定收款人：




- 手動輸入付款資訊
- 從剪貼簿貼上**：從剪貼簿貼上地址
- 掃描 QR 碼**：掃描包含地址的 QR 碼



一旦收件人的地址通過驗證，「輸入金額 」畫面就會讓您輸入要發送的金額（以梭希為單位）。您的可用餘額會顯示出來以供參考。按「繼續費用選擇」繼續。



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



下一個畫面會顯示三種收費等級，視所需的緊急程度而定：




- 快速** (10-30 分鐘)：快速確認的費用較高
- 正常** (30-60 分鐘)：成本適中
- 慢速**（1 小時以上）：非緊急交易最低收費



選擇費用等級後，「準備好傳送了嗎？」確認畫面會總結所有詳細資訊：目的地地址、金額、預計時間和交易費用。請仔細檢查這些資訊，然後按「傳送」以傳送交易。



一旦發送，交易會以「未確認」狀態出現在您的歷史記錄中，直到它被納入凍結中。您的餘額也會相應更新。



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## 優點與限制



### 重點介紹





- 教學**：簡化介面，專注於學習 靜音付款
- 雙向**：與其他組合不同，同時支援傳送與接收
- 開放原始碼**：GitHub 上完全可稽核的程式碼
- 專用 Faucet**：更容易取得測試資金
- 無帳戶**：無需註冊或個人資料



### 需要考慮的限制條件





- 實驗**：未審核軟體，請謹慎使用 Mainnet
- 有限的平台**：主要是 Android，沒有 iOS 版本
- 功能減少**：無硬幣控制、無子帳戶、無 Lightning
- 密集掃描**：付款偵測會消耗大量資源



## 最佳實踐



### seed 安全性



即使是背景毫無價值的 Signet 測試，也要認真對待您的復原短語。使用設定中的「顯示 seed 詞組」選項仔細記下它。作為良好的慣例，為 Signet 和 Mainnet 維護完全獨立的錢包：絕對不要在用來接收真實資金的 wallet 上使用為測試而創建的 seed。



### 實驗狀態警告



Dana Wallet 仍被其開發人員視為實驗品。正如他們明確指出的"不要使用您不願意損失的資金。為了學習目的，請選擇 Signet 版本。如果您使用 Mainnet 版本，請限制自己的 token 金額。



### 備份與還原



Silent Payments 資金回收需要與 BIP-352 協定相容的 wallet。標準的 wallet 無法掃描區塊鏈來復原您的 UTXO Silent Payments。請保留已安裝的 Dana Wallet 或在首次啟動時使用「還原」選項來復原現有的 wallet。



## 與 BIP-47 和 PayJoin 的比較



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Silent Payments 以更昂貴的掃描成本消除 BIP-47 通知交易。PayJoin 可解決不同的問題 (輸入相關性)，並可與 Silent Payments 結合。



## 總結



Dana Wallet 是在無風險環境下學習無聲支付的寶貴教育工具。它的簡約方式讓您了解 BIP-352 協定的基本機制，而不會被次要功能所干擾。透過嘗試使用 Signet，您將對 Bitcoin 交易保密這項前景看好的技術有實際的了解。



Silent Payments 代表著在協調易用性和尊重隱私方面向前邁進了一大步。社群的熱情以及首次整合至各種錢包 (Cake Wallet、BitBox02、BlueWallet 用於發送) 都指向一個未來，即公佈捐款位址將不再危害其擁有人的財務隱私。



## 資源



### 官方文件




- Dana Wallet GitHub 資源庫：https://github.com/cygnet3/danawallet
- F-Cold 保證金：https://fdroid.silentpayments.dev
- Silent Payments 社區網站：https://silentpayments.xyz
- 規格 BIP-352: https://bips.dev/352



### Signet 測試工具




- Faucet 無聲付款：https://silentpayments.dev/faucet/signet
- Signet Mempool Explorer: https://mempool.space/signet



### Blindbit 伺服器 (自行託管)




- Blindbit Oracle (GitHub): https://github.com/setavenger/blindbit-oracle