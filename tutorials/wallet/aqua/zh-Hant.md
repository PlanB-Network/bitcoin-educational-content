---
name: Aqua
description: Bitcoin、Lightning 和 Liquid 合併為一個 Wallet
---
![cover](assets/cover.webp)


Aqua 是一個行動應用程式，可讓 Bitcoin 和 Liquid 輕鬆建立 Hot Wallet，也提供使用 Lightning 的可能性，由於整合了交換功能，因此不需要複雜的節點管理。它還可以讓 USDT 穩定幣在各種網路中進行管理。


Aqua 應用程式由 JAN3 公司在 Samson Mow 的指導下開發，最初是專門針對拉丁美洲使用者的需求而設計，儘管它適用於全球任何使用者。對於初學者和每天使用 Bitcoin 進行支付的人來說，它尤其有趣。


在本教程中，我們將了解如何使用 Aqua 的許多功能。但在此之前，我們先花一點時間了解 Bitcoin 上的 Sidechain 是什麼，以及 Liquid 的運作方式，這樣才能完全掌握 Aqua 的價值。


![AQUA](assets/fr/01.webp)


## 什麼是 Sidechain？


Bitcoin 通訊協定有其刻意的技術限制，這些限制有助於維持網路的分散性，並確保安全性分佈於所有使用者。然而，這些限制有時會讓使用者感到挫折，尤其是在同時進行大量交易造成擁塞時。有關 Bitcoin 可擴展性的爭論在社群中長期存在分歧，尤其是在區塊大小戰爭期間。自從這次事件之後，Bitcoin 社群廣泛認同可擴展性必須透過 off-chain 解決方案，在第二個 Layer 系統上來確保。這些解決方案包括側鏈，與 Lightning Network 等其他系統相比，側鏈仍相對不為人知，也很少使用。


Sidechain 是與主 Bitcoin Blockchain 平行運作的獨立 Blockchain。它使用 Bitcoin 作為記帳單位，這要歸功於稱為 「*雙向掛鉤*」的機制。此系統可將比特幣鎖定在主鏈上，以便在 Sidechain 上複製其價值，在 Sidechain 上，比特幣以原始比特幣支持的代幣形式流通。這些代幣通常會與鎖定在主鏈上的比特幣保持同等價值，這個過程可以逆轉，以收回 Bitcoin 上的資金。


側鏈的目的是提供額外的功能或技術改進，例如更快的交易速度、更低的費用或支援智慧合約。在不影響 Bitcoin Blockchain 的去中心化或安全性的情況下，這些創新往往無法直接在 Bitcoin Blockchain 上實現。因此，側鏈使測試和探索新解決方案成為可能，同時保留 Bitcoin 的完整性。然而，這些協定通常需要妥協，特別是在分散性和安全性方面，這取決於所選擇的治理模式和共識機制。


## 什麼是 Liquid？


Liquid 是 Bitcoin 的聯邦 Sidechain 疊加，由 Blockstream 開發，以提高交易速度、保密性和功能性。它使用在聯邦上建立的雙邊錨定機制，將比特幣鎖定在主鏈上，並創建 Liquid 比特幣 (L-BTC) 作為回報，代幣在 Liquid 上流通，同時仍由原始比特幣提供支持。


![AQUA](assets/fr/02.webp)


Liquid Network 依賴參與者聯盟，由來自 Bitcoin 生態系統的認可實體組成，負責驗證區塊和管理雙邊掛鉤。除了 L-BTC，Liquid 也能發行其他數位資產，例如 USDT 穩定幣和其他加密貨幣。


![AQUA](assets/fr/03.webp)


## 安裝 Aqua 應用程式


第一步當然是下載 Aqua 應用程式。前往您的應用程式商店：



- [For Android](https://play.google.com/store/apps/details?id=io.aquawallet.android)；
- [For Apple](https://apps.apple.com/us/app/Aqua-Wallet/id6468594241).

![AQUA](assets/fr/04.webp)


對於 Android 使用者，您也可以選擇透過 `.apk` 檔案 [可在其 GitHub 上取得](https://github.com/AquaWallet/Aqua-Wallet/releases) 安裝應用程式。


![AQUA](assets/fr/05.webp)


啟動應用程式，然後勾選「*我已閱讀並同意服務條款與隱私權政策*」方塊。


![AQUA](assets/fr/06.webp)


## 在 Aqua 上建立您的 Wallet


按一下「*建立 Wallet*」按鈕。


![AQUA](assets/fr/07.webp)


瞧，您的 Wallet 已經建立！


![AQUA](assets/fr/08.webp)


但首先，由於這是一個自我保管的 Wallet，因此必須對您的 Mnemonic 進行實體備份。 **這台 Mnemonic 讓您可以完全不受限制地存取您所有的比特幣**。任何持有此 Mnemonic 的人都可以盜取您的資金，即使沒有實體存取您的手機。


它允許您在手機丟失、被盜或破損的情況下恢復對比特幣的存取。因此，將其小心保存在實體媒介上（而非數位媒介）並存放在安全的地方是非常重要的。您可以把它寫在一張紙上，或者為了增加安全性，如果這是一個大型的 Wallet，我建議把它刻在一個不鏽鋼支架上，以保護它免受火災、水災或倒塌的風險（對於一個專為保護少量比特幣而設計的 Hot Wallet，簡單的紙張備份可能就足夠了）。


若要執行此操作，請按一下「設定」功能表。


![AQUA](assets/fr/09.webp)


然後按一下「*檢視 seed 詞組*」。製作這 12 個字短語的實體備份。


![AQUA](assets/fr/10.webp)


在相同的設定選單中，您也可以變更應用程式語言和使用的法定貨幣。


![AQUA](assets/fr/11.webp)


在您的 Wallet 收到您的第一枚比特幣之前，**我強烈建議您進行一次空復原測試**。記下一些參考資訊，例如您的 xpub 或第一次收到的 Address，然後在 Aqua 應用程式上刪除您的 Wallet，而它還是空的。然後嘗試使用您的紙張備份在 Aqua 上還原您的 Wallet。檢查還原後生成的 cookie 資訊是否與您最初寫下的相符。如果是的話，您可以放心您的紙本備份是可靠的。若要瞭解有關如何進行測試復原的更多資訊，請參閱此其他教學：


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

你在我的螢幕上看不到它，因為我用的是模擬器，但是在設定中，你會發現一個選項，可以用生物辨識認證系統鎖定應用程式。我強烈建議您啟用這項安全功能，因為如果沒有這項功能，任何有權進入您未鎖定手機的人都有可能偷走您的比特幣。您可以使用 iOS 上的 Face ID 或 Android 上的指紋。如果這些方法在驗證過程中失敗，您仍然可以使用手機的 PIN 碼存取應用程式。


## 在 Aqua 上接收比特幣


現在您的 Wallet 已設定完成，您已準備好接收第一台 Sats！只要點選「*Wallet*」功能表中的「*接收*」按鈕即可。


![AQUA](assets/fr/12.webp)


您可以選擇在 Liquid 鏈上或透過 Lightning 接收比特幣。


![AQUA](assets/fr/13.webp)


對於 onchain 交易，Aqua 將 generate 特定的接收 Address，您可以在此接收您的 Sats。


![AQUA](assets/fr/14.webp)


同樣地，選擇 Liquid，Aqua 將為您提供 Liquid Address。


![AQUA](assets/fr/15.webp)


如果您希望透過 Lightning 接收資金，您首先需要指定所需的金額。


![AQUA](assets/fr/16.webp)


然後按一下「*generate Invoice*」。


![AQUA](assets/fr/17.webp)


Aqua 將建立一個 Invoice 來接收來自 Lightning Wallet 的資金。請注意，與 onchain 和 Liquid 選項不同，透過 Lightning 收到的資金會使用 Boltz 工具在 Liquid 上自動轉換為 L-BTC，因為 Aqua 不是 Lightning 節點。這個過程允許您透過 Lightning 接收和發送資金，但不會在 Lightning 上儲存您的比特幣。


![AQUA](assets/fr/18.webp)


就我個人而言，我打算先透過 Lightning 將 bitcoins 傳送至 Aqua。一旦與提供的 Invoice 完成交易，我們就會收到確認。


![AQUA](assets/fr/19.webp)


若要跟進交換的進度，請返回您的 Wallet 首頁，點選「*L2 Bitcoin*」帳號，其中會列出 Lightning (透過交換) 和 Liquid 的交易。


![AQUA](assets/fr/20.webp)


在這裡您可以檢視您的交易和您的 L-BTC 結餘。


![AQUA](assets/fr/21.webp)


## Bitcoin 與 Aqua 對調


現在您的 Aqua Wallet 中已有資產，您可以直接從應用程式中進行交換，將資產轉移到主 Bitcoin Blockchain 或 Liquid。您也可以將比特幣轉換為 USDT 穩定幣（或其他）。要這樣做，請到「*市場*」功能表。


![AQUA](assets/fr/22.webp)


按一下「*交換*」。


![AQUA](assets/fr/23.webp)


在 「*轉移自*」方塊中，選擇您想要交易的資產。目前，我只擁有 L-BTC，所以我選擇 L-BTC。


![AQUA](assets/fr/24.webp)


在 「*轉移到*」方塊中，選擇您交換的目標資產。就我而言，我選擇了 Liquid Network 上的 USDT。


![AQUA](assets/fr/25.webp)


輸入您要轉換的金額。


![AQUA](assets/fr/26.webp)


按一下「*繼續*」確認。


![AQUA](assets/fr/27.webp)


確定您滿意交換設定，然後拖動螢幕下方的「*Swap*」按鈕確認。


![AQUA](assets/fr/28.webp)


您的交換現已確認。


![AQUA](assets/fr/29.webp)


回顧我們的 Wallet，我們可以看到現在 Liquid 上有 USDT。


![AQUA](assets/fr/30.webp)


## 使用 Aqua 傳送比特幣


現在您的 Aqua Wallet 中已有比特幣，您可以傳送它們。按一下「*傳送*」按鈕。


![AQUA](assets/fr/31.webp)


選擇您要傳送的資產或選擇進行交易的網路。就我而言，我要透過 Lightning 傳送 bitcoins。


![AQUA](assets/fr/32.webp)


接下來，輸入發送付款所需的資訊：對於 onchain 或 Liquid 比特幣，您需要輸入接收的 Address；對於 Lightning，則需要輸入 Invoice。您可以直接將這些資訊貼到提供的欄位中，或使用 QR 碼圖示開啟相機，掃描 Address 或 Invoice。然後按一下「*繼續*」。


![AQUA](assets/fr/33.webp)


如果所有資訊似乎都正確，請再次按一下「*繼續*」。


![AQUA](assets/fr/34.webp)


Aqua 隨後會向您顯示交易摘要。確保所有資訊正確無誤，包括目的地 Address、費用和金額。若要確認交易，請滑動螢幕下方的「*滑動發送*」按鈕。


![AQUA](assets/fr/35.webp)


之後您就會收到寄件確認。


![AQUA](assets/fr/36.webp)


因此，現在您知道如何使用 Aqua 應用程式在 Bitcoin、Lightning 和 Liquid 上收款和消費了，所有這些都是透過單一的 Interface。


如果您覺得本教學有用，請在下方留下 Green 拇指。歡迎在您的社交網路分享這篇文章。非常感謝


我也建議您看看 Blockstream Green 手機應用程式的其他全面教學，這是設定 Liquid Wallet 的另一個有趣解決方案：


https://planb.network/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a
