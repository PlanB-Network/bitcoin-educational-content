---
name: Alby Hub
description: 如何輕鬆啟動自己的 Lightning 節點？
---
![cover](assets/cover.webp)


Alby Hub 是廣受歡迎的 Lightning 網頁延伸功能背後公司 Alby 最新推出的開放源碼軟體。Alby Hub 是一個自我保管的 Wallet，擁有最容易使用的 Lightning 節點，可從任何地方存取，與數十個應用程式整合。Alby Hub 是易於使用的 Interface，用於管理 Lightning 節點。


在本教程中，我們將探討 Alby Hub 的不同使用方式，如何將其連接到 Alby Go、Alby 手機應用程式或 Alby 瀏覽器擴充套件。這將使您能夠在移動中使用 Sats，同時自主管理您的節點。


![ALBY HUB](assets/fr/01.webp)


## 什麼是 Alby Hub？


Alby Hub 將成為 Alby 生態系統的新旗艦工具。此軟體可讓使用者透過整合式 Lightning 節點輕鬆管理自己的自保管 Wallet，同時保留鑰匙的 Ownership（自保管）。


Alby Hub 是一款具有高度適應性的工具。它可以滿足初學者和高級用戶的需求。新手使用它可以輕鬆地自行操作一個真正的 Lightning 節點，而無需處理底層的複雜性。對於更有經驗的用戶，Alby Hub可以作為一個完整的Interface來進階管理現有的Lightning節點。


根據您的需求，Alby Hub 有 4 種配置可供選擇：




- Alby Hub Cloud :**


第一個選項是 Alby 雲端選項，非常適合新手。它允許您直接在 Alby 管理的伺服器上部署 Hub，並透過您的 Alby Hub Interface 進行存取。雖然 Alby 負責管理伺服器，但您仍保留對資金的主權，因為您的金鑰是使用只有您知道的密碼加密的。但是，您的金鑰必須在 RAM 中保持解密狀態，節點才能運作，理論上，如果有人實際存取伺服器，金鑰就會有風險。對於初學者來說，這是一個有趣的折衷方案，但必須注意風險。


此方案的主要優點是，您可以獲得一個全天候運行的Lightning節點，而無需自己管理託管。更重要的是，Lightning 節點的備份是簡化和自動化的，相比之下，自助託管方案則需要您自己管理通道備份。


Alby Cloud 是付費服務 [查看他們的定價](https://albyhub.com/#pricing) 了解更多詳情。費用會透過 Alby 發出的 Lightning Invoice 從您的 Wallet 中自動扣除。這是透過 NWC 連線完成的，該連線可設定您的節點自動支付與您訂閱相關的 Alby 發票。





- Alby Hub 與現有節點 :**


如果您已經有一個節點託管，例如在 Umbrel 或 Start9 上，Alby Hub 可以像 ThunderHub 或 RTL 一樣，作為進階管理 Interface。




- Alby Hub 本地 :**


您也可以直接在電腦上安裝 Alby Hub，不過這個方案不太實際，因為您的電腦必須隨時保持活動狀態，才能遠端存取 Lightning 節點。不過，這個選擇可能適合您的特定需求。




- Alby Hub 在個人伺服器上：**


對於進階使用者，Alby Hub 可以透過簡單的指令部署在個人伺服器上。本教學未涵蓋此選項，但您可以 [Alby 的 GitHub](https://github.com/getAlby/hub?tab=readme-ov-file#docker) 上找到專門的說明。


本教學主要著重於 Interface，無論選擇哪個選項都是一樣的。我們也會看看如何使用付費雲端選項部署 Alby Hub，然後再使用節點內置選項 (Umbrel 或 Start9)。


![ALBY HUB](assets/fr/02.webp)


若要在個人電腦上進行本機安裝，請 [根據您的作業系統下載並安裝軟體](https://github.com/getAlby/hub/releases)，然後按照 Interface 上的相同指示進行安裝。


![ALBY HUB](assets/fr/03.webp)


## 建立 Alby 帳戶


第一步是建立 Alby 帳戶。雖然這不是使用 Alby Hub 的必要條件，但卻能讓您充分利用可用的選項，包括取得 Lightning Address 的可能性。


前往 [Alby 官方網站](https://getalby.com/) 並點選「*建立帳號*」按鈕。


![ALBY HUB](assets/fr/04.webp)


輸入暱稱和電子郵件 Address，然後按一下「*註冊*」。此電子郵件 Address 將用於稍後登入您的帳戶。


![ALBY HUB](assets/fr/05.webp)


輸入您從電子郵件收到的驗證碼。


![ALBY HUB](assets/fr/06.webp)


登入您的線上帳戶後，按一下「*繼續*」按鈕。


![ALBY HUB](assets/fr/07.webp)


再次按一下「*繼續*」。


![ALBY HUB](assets/fr/08.webp)


## 雲端主機選項


接下來，您必須選擇自我託管選項（即在自己的裝置上安裝 Alby Hub）或付費選項。我會先解釋如何進行 Pro Cloud 選項（請注意，這是付費選項，詳情請參閱上一節）。


按一下「*升級*」。


![ALBY HUB](assets/fr/09.webp)


按一下「*立即訂閱*」以確認。


![ALBY HUB](assets/fr/10.webp)


按一下「*啟動 Alby Hub*」。


![ALBY HUB](assets/fr/11.webp)


等待片刻，您的節點就會建立。


![ALBY HUB](assets/fr/12.webp)


就這樣，您的 Alby Hub 已經設定完成。在下一節，我會告訴你如何在現有節點上安裝 Alby Hub。如果您還沒有閃電節點，您可以跳到下一節，在 Alby Cloud 上設定 Alby Hub。


![ALBY HUB](assets/fr/13.webp)


## 自我託管選項


如果您想使用 Alby Hub 作為您現有 Lightning 節點的 Interface，您有幾個選擇：將它安裝在伺服器上、本機安裝在您的電腦上，或透過 node-in-box (Umbrel 或 Start9)。在這些配置中使用 Alby Hub 是免費的。我們將專注於 node-in-box 選項，因為我發現伺服器選項在沒有實體存取的情況下，會帶來與雲端版本類似的風險，而且本機安裝在電腦上通常並不適合。


若要在 Umbrel 上進行設定 (Start9 的步驟相同)，您必須先設定好 LND 節點。


登入您的 Umbrel Interface 並前往應用程式商店。


![ALBY HUB](assets/fr/14.webp)


尋找「*Alby Hub*」應用程式。


![ALBY HUB](assets/fr/15.webp)


將其安裝在您的節點上。


![ALBY HUB](assets/fr/16.webp)


您的 Alby Hub Interface 已準備就緒。您可以像使用雲端 Interface 一樣跟著教學的其他部分，但沒有付費版本的選項。此外，與雲端版本不同的是，您的金鑰會儲存在您的本機節點上，而不是 Alby 的伺服器上。


![ALBY HUB](assets/fr/17.webp)


## 啟動 Alby Hub


按一下「*開始*」按鈕。


![ALBY HUB](assets/fr/18.webp)


Alby Hub 接著會提示您選擇一個密碼。這個密碼非常重要，因為它會用來加密您的 Wallet。在付費雲端版本中，您的金鑰會儲存在 Alby 伺服器上，並以這個只有您知道的密碼進行加密，然後再解密並僅儲存在 RAM 中，以便在必要時簽署交易。


因此，選擇一個強大的密碼是非常重要的。任何擁有此密碼的人都有可能存取您的節點。確保您也將這個密碼備份在一張紙上，或更好的是，備份在一塊金屬上，以增加安全性。


小心選擇並儲存密碼後，按一下「*建立密碼*」。


![ALBY HUB](assets/fr/19.webp)


現在您可以存取您的 Lightning 節點。


![ALBY HUB](assets/fr/20.webp)


要採取的第一個動作是儲存您的復原短語，您的金鑰就來自該短語。要執行此動作，請按一下「設定」。如果您啟用自動備份，此短語可讓您恢復 Wallet 的存取權。


![ALBY HUB](assets/fr/21.webp)


然後前往「*備份*」標籤。輸入密碼即可存取。


![ALBY HUB](assets/fr/22.webp)


然後您就可以使用 12 個字的復原短語。用紙張或金屬製作一個或多個這句話的實體備份，並將其存放在安全的地方。


![ALBY HUB](assets/fr/23.webp)


儲存短語後，請勾選方塊確認已儲存，然後按一下「*繼續*」。


![ALBY HUB](assets/fr/24.webp)


## 我該如何恢復比特幣的存取權？


在向您的 Alby Hub 傳送資金之前，重要的是要瞭解在發生問題時如何恢復資金，以及恢復資金需要哪些資訊。這個過程會根據要追回資金的性質和您節點的託管模式而有所不同。


對於付費雲端使用者而言，完全復原您的 bitcoins 需要三個必要的 Elements：



- 您的恢復詞組；
- 存取您的 Alby 帳戶，擷取自動備份。


如果沒有這兩項資訊中的任何一項，就不可能完全找回您的 bitcoins。


對於在自己的裝置上執行 Alby Hub 的使用者而言，恢復過程已記錄在 [這裡](https://guides.getalby.com/user-guide/alby-account-and-browser-extension/alby-hub/backups-and-recover#alby-hub-self-hosted-with-an-alby-account)。


如果您在現有節點上安裝 Alby Hub，您需要遵循該特定節點作業系統的復原程序。舉例來說Umbrel 提供 [一個選項](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) 來加密您 Lightning 頻道的最新狀態，並透過 Tor 以動態匿名方式儲存。請注意，只有 Alby 的自動備份才能讓您在不關閉任何通道的情況下完全復原 Hub。


## 購買您的第一個 Lightning 頻道


現在您可以按照 Alby Hub 提供的指示進行操作。按一下按鈕，開啟您的第一個入金管道。


![ALBY HUB](assets/fr/25.webp)


選擇「*開放頻道*」。如果您不打算成為路由節點，也沒有特別的需求，我建議您選擇私人頻道。


![ALBY HUB](assets/fr/26.webp)


Alby Hub 會 generate 和 Invoice 供您付款。這筆款項包括開啟您的通道所需的交易費用，以及 LSP (*Lightning Service Provider*) 的服務費用，LSP 會開啟通道到您的節點，讓您立即收到付款。


![ALBY HUB](assets/fr/27.webp)


一旦支付了 Invoice 並確認了交易，您的第一個 Lightning 通道就建立了。


![ALBY HUB](assets/fr/28.webp)


在 「*節點*」標籤中，您可以看到現在您有現金收入，使您能夠透過 Lightning 接收付款。


![ALBY HUB](assets/fr/29.webp)


若要收款，請按一下「*Wallet*」標籤，然後按一下「*收款*」。


![ALBY HUB](assets/fr/30.webp)


輸入金額，必要時加入說明，然後按一下「*建立 Invoice*」。


![ALBY HUB](assets/fr/31.webp)


我收到了第一筆付款 120,000 Sats。


![ALBY HUB](assets/fr/32.webp)


返回 "*Wallet*"標籤，您可以查看您的 Wallet 結餘。請注意，Alby Hub 會在您首次付款時自動預留 354 Sats。之後您開啟的每個 Lightning 通道，Alby Hub 都會自動預留相當於通道容量 1%的儲備金。這筆儲備金是一項安全措施，讓您的節點能夠在您的對等方試圖詐騙的情況下收回通道的資金。這就是為什麼，雖然我已經發送了 120,000 Sats，但我的餘額上只顯示了 119,646 Sats。


![ALBY HUB](assets/fr/33.webp)


## 在鏈上存入比特幣


如果您想要有外流的現金來付款，您也可以自己開一個通道。要做到這一點，您的 Wallet 中需要 onchain bitcoins。


從「*節點*」標籤，按一下「*存款*」。


![ALBY HUB](assets/fr/34.webp)


發送 bitcoins 到顯示的 Address。此 Address 來自您先前儲存的復原短語。


![ALBY HUB](assets/fr/35.webp)


我發送了 72,000 Sats。現在它們在 「*儲蓄餘額*」中可以看到，其中包括我在鏈上擁有的所有資金，而不是 Lightning 上的資金。


![ALBY HUB](assets/fr/36.webp)


## 開啟「閃電」頻道


現在您已經擁有了onchain資金，您可以開啟一個新的Lightning通道。建議您開設多個通道，並提供足夠的金額，以確保您可以隨時無限制地進行支付。大多數 LSP（*閃電服務供應商*）要求至少 150,000 Sats 才能為您開通一個通道。


在「*節點*」標籤中，按一下「*開啟通道*」。


![ALBY HUB](assets/fr/37.webp)


選擇通道的大小。我建議您不要開啟太小的通道，因為這是一個 Lightning 節點，存放您金鑰的機器無法提供與 Hardware Wallet 相同的安全等級。所以請小心選擇封鎖的數量。


![ALBY HUB](assets/fr/38.webp)


在 「*進階選項*」選單中，您可以選擇使用哪個 LSP 來開啟通道，或手動輸入另一個 Lightning 節點。


![ALBY HUB](assets/fr/39.webp)


然後按一下「*開啟頻道*」。


![ALBY HUB](assets/fr/40.webp)


等待您的頻道在線上確認。


![ALBY HUB](assets/fr/41.webp)


您的新頻道現在會出現在 "*Node*" 標籤中。


![ALBY HUB](assets/fr/42.webp)


## 節點管理


管理您的 Lightning 頻道比您想像中容易。Alby Hub 允許您在支出餘額和 On-Chain 餘額之間轉移 Sats。這樣您就可以增加支出或接收容量。


![ALBY HUB](assets/fr/66.webp)


## 連接開支應用程式


現在您已經擁有一個可以運作的 Lightning 節點，您可以每天使用它來接收和消費 Sats。雖然 Alby Hub 的網頁 Interface 對於管理您的節點很方便，但對於在移動中進行快速交易卻不太理想。因此，我們要使用安裝在智慧型手機上的 Lightning Wallet 應用程式。


在本教程中，我建議您選擇 Alby Go，它非常容易使用，但您也可以使用 Zeus 等其他相容的應用程式。


![ALBY HUB](assets/fr/43.webp)


若要安裝 Alby Go，請前往裝置的應用程式商店：




- [For Android](https://play.google.com/store/apps/details?id=com.getalby.mobile)；
- [For Apple](https://apps.apple.com/us/app/alby-go/id6471335774).


![ALBY HUB](assets/fr/44.webp)


Android 使用者也可以透過 `.apk` 檔案 [可在 Alby 的 GitHub 上取得](https://github.com/getAlby/go/releases) 安裝應用程式。


![ALBY HUB](assets/fr/45.webp)


啟動應用程式後，按一下「*連線 Wallet*」。


![ALBY HUB](assets/fr/46.webp)


在您的 Alby Hub 中，在 App Store 下找到 "Alby Go「，然後點擊 」連接"。

![ALBY HUB](assets/fr/47.webp)

按一下「與單一標籤連線」。這將允許您使用 Alby Go 一鍵連接您的 Alby Hub 與其他應用程式。


![ALBY HUB](assets/fr/48.webp)


Alby Hub 接著會以 generate 加密建立與 Alby Go 的連線。


![ALBY HUB](assets/fr/49.webp)


回到 Alby Go 應用程式，掃描 QR 代碼或貼上秘訣。


![ALBY HUB](assets/fr/50.webp)


按一下「完成*」。


![ALBY HUB](assets/fr/51.webp)


您現在可以從智慧型手機遠端存取由 Lightning 節點供電的 Alby Hub，讓您每天在移動中輕鬆消費和接收 Sats。


![ALBY HUB](assets/fr/52.webp)


如有必要，您可以直接在 Alby Hub 上按一下此連線，以管理其權限。


![ALBY HUB](assets/fr/53.webp)


若要接收 Sats，只需按一下「*接收*」。


![ALBY HUB](assets/fr/54.webp)


點選「*Invoice*」，修改 Invoice 的金額和說明。


![ALBY HUB](assets/fr/55.webp)


為 Invoice 充電，以接收 Sats。


![ALBY HUB](assets/fr/56.webp)


若要傳送 Sats，請按一下「*傳送*」。


![ALBY HUB](assets/fr/57.webp)


掃描您要支付的 Invoice。


![ALBY HUB](assets/fr/58.webp)


然後按一下「*Pay*」。


![ALBY HUB](assets/fr/59.webp)


您的交易已確認。


![ALBY HUB](assets/fr/60.webp)


按一下小箭頭，即可存取交易記錄。


![ALBY HUB](assets/fr/61.webp)


這些交易也可以在您的 Alby Hub 上看到。


![ALBY HUB](assets/fr/62.webp)


## 自訂您的 Lightning Address


Alby 提供您 Lightning Address 的選項。這可讓您在節點上接收付款，而無需每次手動 generate 和 Invoice。預設情況下，Alby 會為您分配一個 Lightning Address，但您也可以自定義。登入您的 Alby 線上帳戶，按一下右上角您的名字，然後選擇「*設定*」。


![ALBY HUB](assets/fr/63.webp)


導覽至「*閃電 Address*」功能表。


![ALBY HUB](assets/fr/64.webp)


修改您的 Address，然後按一下「*更新您的閃電 Address*」確認。


![ALBY HUB](assets/fr/65.webp)


請注意，一旦您的 Address 被變更，它就不再屬於您。所以請確保您永遠不會再寄送 Sats 到它。


就這樣，您現在知道如何使用 Alby Hub 工具在自己的節點上使用 Lightning 了。如果您覺得本教學有用，請在下方寫上 Green 拇指，我將非常感激。請隨時在您的社交網路分享這篇文章。非常感謝


要詳細瞭解我們在本教程中使用的所有 Lightning 機制，我強烈建議您瞭解我們關於此主題的免費培訓：


https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb