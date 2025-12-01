---
name: Ashigaru Terminal
description: 在桌面上使用 Ashigaru 進行硬幣接合
---

![cover](assets/cover.webp)



Ashigaru Terminal 是 Ashigaru 團隊對 Sparrow Server 的改編，它實現了 Whirlpool 合併協定。此軟體是 Samourai Wallet 開始的工作的延續，特別是 Whirlpool GUI，其採用的基本原則是：自我保管和保密。



本軟體是 Sparrow Server 的 fork，經過修改與最佳化，可與 Samourai 團隊最初開發的 ZeroLink 硬幣接合通訊協定 Whirlpool 生態系統完全整合。



Ashigaru Terminal 以簡約的 TUI 介面運作，可部署在個人電腦或專用伺服器上。它可讓您直接與 Whirlpool 進行互動，以啟動「*Tx0*」、管理「*Deposit*」、「*Premix*」、「*Postmix*」和「*Badbank*」帳戶，並執行自動混音以加強零件的機密性。



簡而言之，如果您想要使用 Whirlpool 建立共同接續，Ashigaru Terminal 將會特別有用。



在第一個教學中，我會帶您了解 Ashigaru Terminal 的安裝和操作。接下來的第二個更進階的教學將專門講解如何建立硬幣接合。



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1.安裝 Ashigaru 終端機



要安裝 Ashigaru Terminal，您需要 Tor 瀏覽器，因為二進位檔只能透過 Tor 網路散佈。如果您還沒有安裝，請 [在您的機器上安裝](https://www.torproject.org/download/)。



### 1.1. 下載 Ashigaru Terminal



從 Tor 瀏覽器，前往 [其 Git 套件庫的發行版頁面](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) 下載適用於您作業系統的最新版 Ashigaru Terminal。



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



為您的作業系統下載下列 2 個檔案：




- 二進位檔案（Debian/Ubuntu 為`ashigaru_terminal_v1.0.0_amd64.deb`，macOS 為`.dmg`，Windows 為`.zip`）；
- 已簽署的雜湊檔案：`ashigaru_terminal_v1.0.0_signed_hashes.txt`。



### 1.2.檢查 Ashigaru Terminal



在您的設備上運行軟件之前，您需要檢查其真實性和完整性。這是很重要的一步，因為它可以防止您安裝可能會危及您的比特幣或感染您的機器的欺詐版本。



開啟新的瀏覽器標籤，進入 [Keybase 驗證工具](https://keybase.io/verify)。將您剛下載的 `.txt` 檔案內容貼入提供的欄位，然後按一下 `驗證` 按鈕。



![Image](assets/fr/02.webp)



為了讓您的驗證來源更多元化，您也可以將此訊息與 clearnet [ashigaru.rs](https://ashigaru.rs/download/) 網站上的 `/下載`區段中的訊息進行比較。



![Image](assets/fr/03.webp)



如果簽章有效，Keybase 會顯示一則訊息，確認檔案已由 Ashigaru 的開發人員簽章。



![Image](assets/fr/04.webp)



您也可以點選 Keybase 顯示的 `ashigarudev` 個人資料，檢查他們的金鑰指紋是否完全符合 : `A138 06B1 FA2A 676B`。



![Image](assets/fr/05.webp)



如果在此階段出現錯誤，表示簽章無效。在這種情況下，**請勿安裝下載的軟體**。從頭重新開始，或在繼續之前向社群尋求協助。



Keybase 已為您提供應用程式的驗證切細值。現在我們要檢查您下載的「.deb」、「.zip」或「.dmg」檔案的切細值是否與 Keybase 上驗證的相符。為此，請前往 [HASH FILE ONLINE](https://hash-file.online/)。



按一下 `BROWSE...`按鈕，然後選擇在步驟 1.1 中下載的 `.deb`、`.zip` 或`.dmg`檔。然後選擇 `SHA-256` 散列函數，並按一下 `CALCULATE HASH` 以 generate 為您的檔案取得散列值。



![Image](assets/fr/06.webp)



網站隨後會顯示軟體的切細值。將它與您在 Keybase.io 上驗證的雜湊值進行比較。如果兩者完全吻合，則表示真實性和完整性檢查成功。您就可以使用該軟體。



![Image](assets/fr/07.webp)



### 1.3 啟動 Ashigaru 終點站





- Debian / Ubuntu



若要安裝軟體，請執行指令 ：



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



根據下載的版本修改順序。



然後檢查安裝：



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



然後啟動軟體：



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- 視窗**



用滑鼠右鍵按一下您已下載並檢查過的「.zip」檔案，然後選擇「全部解壓縮...」以解壓縮其內容。



擷取完成後，按兩下 `Ashigaru-terminal.exe` 檔案以啟動軟體。



![Image](assets/fr/08.webp)



## 2.開始使用 Ashigaru Terminal



Ashigaru Terminal 是一個 TUI (*Text-based User Interface*) 程式，也就是直接在終端機執行的簡約介面。您可以使用選單和鍵盤快捷鍵與它互動，但不需要任何真正的經典圖形環境。



![Image](assets/fr/09.webp)



使用方法很簡單：使用鍵盤上的方向鍵瀏覽功能表，按「Enter」鍵確認動作或選擇。



## 3.將您的節點連接到 Ashigaru Terminal



預設情況下，Ashigaru Terminal 會連線至公用的 Electrum 伺服器。這顯然在機密性和主權方面存在風險。因此，我們將配置它直接連接到您自己的 Electrum Server。



若要執行此操作，請開啟 `偏好設定 > 伺服器 ` 功能表。



![Image](assets/fr/10.webp)



按一下 `< 編輯 >` 按鈕。



![Image](assets/fr/11.webp)



選取 `Private Electrum Server`，然後按一下 `<Continue>`。



![Image](assets/fr/12.webp)



輸入伺服器的 URL 和連接埠。您可以在 `.onion` 中指定 Tor 位址。然後按一下 `< Test >` 以驗證連線。



![Image](assets/fr/13.webp)



如果連線成功，則會出現 `Success` 訊息，以及您伺服器的詳細資訊。



![Image](assets/fr/14.webp)



如果您還沒有 Bitcoin 節點，我建議您參加這個課程：



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*在本教程中，我將中斷 Electrs 伺服器的連線，因為我要在 testnet 上工作。但是，在 mainnet.* 上的操作仍然完全相同。



## 4.在 Ashigaru Terminal 上建立投資組合



現在軟體已正確設定，我們可以新增 Bitcoin 組合。



您有兩個選擇：




- 您可以從頭開始建立一個新的 wallet，並只在 Ashigaru Terminal 上使用。在這種情況下，每次您想要與 wallet 進行互動時，都需要開啟此軟體；
- 另外，您也可以將現有的 Ashigaru wallet 直接從手機匯入 Ashigaru Terminal。此方法的缺點是會稍微降低設定的安全性，因為您的 wallet 會暴露在兩個而非一個有風險的環境中。另一方面，它的優點是可以讓 Ashigaru Terminal 持續運行以混合您的硬幣，同時允許您透過 Ashigaru 手機應用程式遠端花費硬幣。



在本教程中，我們將選擇第二種方法。不過，如果您想要建立全新的組合，步驟也一樣：唯一的差別在於建立時，您需要儲存新的記憶詞組和新的 passphrase。



另請注意，Ashigaru Terminal 不允許您直接花費比特幣。您可以在 Ashigaru Terminal 和 Ashigaru 應用程式上同步同一個錢包（這是我在本教學中要做的），或在 Sparrow Wallet 上進行同步。



如果您還沒有關於 Ashigaru 應用程式的 wallet，您可以按照專門的教學 ：



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

前往 `錢包`功能表。



![Image](assets/fr/15.webp)



然後選擇`建立/恢復 wallet...`。開啟 Wallet...` 選項可讓您稍後存取 Ashigaru Terminal 中已儲存的組合。



![Image](assets/fr/16.webp)



為您的投資組合命名。



![Image](assets/fr/17.webp)



然後選擇投資組合類型 `Hot Wallet`。






![Image](assets/fr/18.webp)



在這個階段，程序會根據您最初的選擇而有所不同：




- 如果您希望從頭開始建立一個新的組合，請按一下`<Generate New Wallet>`，定義一個 passphrase BIP39，然後小心地將您的助記語句和 passphrase 保存在實體媒體上；



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- 如果您希望使用與您的 Ashigaru 應用程式相同的 wallet，請直接在對應的欄位中輸入 12 個字的助記詞組和您的 passphrase BIP39。請以小楷、整詞、順序書寫單詞，並以空格分隔，不要使用數字或額外字符。



完成此步驟後，按一下 `< 下一步 >`。



*注意*：如果您無法點選此按鈕，表示您的助記詞組無效。請仔細檢查沒有任何字詞不正確或拼寫錯誤。



![Image](assets/fr/19.webp)



然後您需要設定密碼。這將用於解鎖您的 Ashigaru Terminal wallet，並防止未經授權的實體存取。它不參與您金鑰的加密推導：換言之，即使沒有這個密碼，任何人只要有您的助記短語和 passphrase 就能還原您的 wallet 並存取您的比特幣。



選擇一個長、複雜、隨機的密碼。在安全的地方保存一份副本：最好是保存在實體媒體或安全的密碼管理器中。



完成後按一下 `< OK >`。



![Image](assets/fr/20.webp)



## 5.使用投資組合



然後您可以選擇要存取的帳戶。目前，我們還沒有啟動任何混合，因此我們將訪問 `Deposit` 帳戶。



![Image](assets/fr/21.webp)



操作與 Sparrow 相同，因為 Ashigaru Terminal 是 Sparrow 伺服器的 fork。您會發現相同的選單：



![Image](assets/fr/22.webp)





- transactions": 可讓您查看與此帳戶相關聯的交易歷史。在我的情況下，有些交易已經出現，因為我曾在這個 wallet 上使用 Ashigaru 應用程式進行過一些交易。



![Image](assets/fr/23.webp)





- receive`：產生一個新的空白收據地址，用來將 satss 存入存款帳戶。



![Image](assets/fr/24.webp)





- addresses`: 顯示您所有位址的清單，不論這些位址是屬於您帳戶的內部或外部連鎖。



![Image](assets/fr/25.webp)





- `UTXOs`: 列出所有可用的 UTXO。



![Image](assets/fr/26.webp)





- 設定」：可存取您的投資組合*描述符*。您也可以查詢您的 seed、調整 *Gap Limit* 或變更投資組合的建立日期。



![Image](assets/fr/27.webp)



您現在已經知道如何安裝和使用 Ashigaru Terminal。 在下一個教學中，我們將了解如何使用此軟體執行 coinjoin，以及如何在「*Postmix*」中管理資金。
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
