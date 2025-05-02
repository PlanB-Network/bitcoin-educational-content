---
name: COLDCARD Q
description: 設定和使用 COLDCARD Q
---
![cover](assets/cover.webp)


Hardware Wallet 是專門管理和保護 Bitcoin Wallet 私密金鑰的電子裝置。與安裝在經常連接到網際網路的通用機器上的軟體錢包（或 Hot 錢包）不同，硬體錢包能夠實體隔離私密金鑰，降低盜版和竊取的風險。


Hardware Wallet 的主要目的是儘可能減少裝置的功能，以盡量降低其攻擊面。較少的攻擊面也意味著較少的潛在攻擊媒介，也就是攻擊者可利用來存取比特幣的系統弱點較少。


建議您使用 Hardware Wallet 來保護您的比特幣，尤其是當您持有大量比特幣時，不論是絕對值或是佔您總資產的比例。


硬體錢包與電腦或智慧型手機上的 Wallet 管理軟體搭配使用。後者管理交易的建立，但使這些交易有效所需的加密簽章僅在 Hardware Wallet 內執行。這意味著私人金鑰永遠不會暴露在潛在的脆弱環境中。


硬體錢包為使用者提供雙重保護：一方面，它們透過保持私鑰離線來保護您的比特幣免受遠端攻擊；另一方面，它們通常對試圖提取鑰匙的行為提供更強的物理抵抗力。正是根據這兩個安全標準，我們可以對市場上的不同機型進行判斷和分類。


在本教程中，我想向您介紹一種這樣的解決方案：**COLDCARD Q**。


---
由於 COLDCARD Q 提供多種功能，我建議將其使用分成 2 個教學。在第一個教學中，我們將介紹裝置的初始設定和基本功能。然後，在第二篇教學中，我們將探討如何利用 COLDCARD 的所有進階選項。


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

---
## 介紹 COLDCARD Q


COLDCARD Q 是加拿大 Coinkite 公司開發的 Bitcoin 專用 Hardware Wallet，該公司以之前的 MK 型號而聞名。Q 代表了他們迄今為止最先進的產品，定位為 Bitcoin Hardware Wallet 的終極版。


在硬體方面，COLDCARD Q 配備了最佳使用者體驗所需的所有功能：




- 大型 LCD 顯示器簡化了導覽和操作；
- 全 QWERTY 鍵盤；
- 用於掃描 QR 代碼的整合式相機；
- 兩個 microSD 卡插槽 ；
- 完全隔離的電源選項，可透過三顆 AAA 電池 (不含) 或 USB-C 連接線 ；
- 來自兩家不同製造商的兩台 Secure Elements，可增加安全性；
- 透過 NFC 進行通訊的能力。


在我看來，COLDCARD Q 只有兩個缺點。首先，由於功能眾多，它相當笨重，長度接近 13 公分，寬度 8 公分，幾乎是一部小型智慧型手機的大小。由於電池槽的關係，它也相當厚。如果您正在尋找體積更小、行動性更高的 Hardware Wallet，更精巧的 MK4 可能是更好的選擇。第二個缺點顯然是它的成本，在官網上的售價為 ***$239.99**，也就是比 MK4 高出 72 美元，這讓 Q 直接與 Ledger Flex 或 Foundation's Passport 等高級硬體錢包競爭。


![CCQ](assets/fr/001.webp)


在軟體方面，COLDCARD Q 與 Coinkite 的其他裝置一樣，具備許多先進功能：




- 骰子滾動到 generate 您自己的恢復詞組 ；
- PIN 碼 ；
- 最終 PIN 鎖定倒數計時 ；
- BIP39 passphrase ；
- 最後鎖定的 PIN ；
- 連線倒數 ；
- SeedXOR；
- BIP85...


簡而言之，COLDCARD Q 提供比 MK4 更佳的使用者體驗，可能是尋求更容易使用的中高階使用者的理想選擇。


COLDCARD Q 在 [Coinkite 官方網站](https://store.coinkite.com/store/coldcard) 有售。也可向零售商購買。


## 準備教學


當您收到 COLDCARD 後，第一步是檢查包裝，確定它沒有被打開。如果包裝破損，可能表示 Hardware Wallet 已經損壞，可能不是正品。


![CCQ](assets/fr/002.webp)


打開盒子後，您應該會發現以下物品：




- COLDCARD Q 裝在密封袋中；
- 一張記錄您的 Mnemonic 詞組的卡片。


![CCQ](assets/fr/003.webp)


確保袋子沒有被拆封或損壞。此外，請檢查袋子上的號碼是否與袋子內紙張上的號碼相符。請保留此編號以供日後參考。


![CCQ](assets/fr/004.webp)


如果您希望在不連接電腦的情況下為 COLDCARD 供電 (空氣間隙)，請將三顆 AAA 電池插入裝置背面。另外，您也可以透過 USB-C 連接線將其連接到電腦。


![CCQ](assets/fr/005.webp)


在本教程中，您還需要 Sparrow Wallet 來管理您電腦上的 Bitcoin Wallet。從官方網站下載 [Sparrow Wallet](https://sparrowwallet.com/download/)。我強烈建議您在進行安裝之前，先檢查它的真實性（使用 GnuPG）和完整性（透過 Hash）。如果您不知道如何執行，請遵循此教學：


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

## PIN 碼選擇


現在您可以按左上角的按鈕開啟 COLDCARD。


![CCQ](assets/fr/006.webp)


按「*ENTER*」按鈕接受使用條款。


![CCQ](assets/fr/007.webp)


COLDCARD Q 螢幕上方會顯示一個號碼。請確保此號碼與密封袋上和袋內塑膠片上的號碼相符。這可確保您的包裹在由 Coinkite 包裝至您打開之間未被打開。按 "*ENTER*"繼續。


![CCQ](assets/fr/008.webp)


導覽至「*選擇 PIN 碼*」功能表，然後按「*ENTER*」按鈕確認。


![CCQ](assets/fr/009.webp)


此 PIN 碼用於解鎖您的 COLDCARD。因此可防止未經授權的實體存取。此 PIN 碼不涉及您的 Wallet 密鑰的衍生。因此，即使沒有這個PIN碼，擁有您的Mnemonic短語也可以讓您重新獲得您的比特幣。


COLDCARD PIN 碼分為兩部分：前綴和後綴，每部分可包含 2 到 6 位數，總共 4 到 12 位數。當您解鎖 COLDCARD 時，您首先需要輸入前綴，之後裝置會顯示 2 個單詞。然後輸入後綴。這兩個字詞會在此設定步驟中給您，並應小心保存，因為您每次解鎖 COLDCARD 時都需要用到它們。如果在解鎖時顯示的兩個字詞與您在設定時儲存的字詞相符，這將證實您的裝置自上次使用後未曾外洩。


再次按一下「*選擇 PIN*」。


![CCQ](assets/fr/010.webp)


確認您已閱讀警告。


![CCQ](assets/fr/011.webp)


現在您要選擇 PIN 碼。我們建議您選擇一個隨機的長PIN碼。請確保將此代碼保存在與 COLDCARD 不同的地方。您可以使用包裹中隨附的卡片來記錄此代碼。


輸入您選擇的前綴，然後按「*ENTER*」按鈕確認 PIN 碼的第一部分。


![CCQ](assets/fr/012.webp)


之後兩個反釣魚字樣就會顯示在您的螢幕上。請仔細保存，以供日後參考。您可以使用套件中隨附的卡片記下它們。


![CCQ](assets/fr/013.webp)


然後輸入 PIN 碼的第二部分，並按「*ENTER*」。


![CCQ](assets/fr/014.webp)


再次輸入 PIN 碼以確認您的 PIN 碼，並檢查這兩個防釣魚字詞是否與您之前儲存的相符。


![CCQ](assets/fr/015.webp)


從現在開始，每次您解鎖COLDCARD時，請記得檢查您輸入PIN碼前綴後螢幕上出現的兩個反釣魚字詞的有效性。


## 韌體更新


第一次使用您的裝置時，請務必檢查並更新韌體。若要執行此動作，請存取「*進階/工具*」功能表。


![CCQ](assets/fr/016.webp)


**重要事項：** 如果您打算升級您的韌體，而且這不是您第一次使用 COLDCARD（即您已經在 COLDCARD 上建立了一個 Wallet），請確保您的 Mnemonic 語句是可用的（以及可選的 passphrase，如果適用）。這一點很重要，可避免在裝置更新期間發生問題時遺失您的 bitcoins。


選擇「*升級韌體*」。


![CCQ](assets/fr/017.webp)


選擇「*顯示版本*」。


![CCQ](assets/fr/018.webp)


您可以檢查 COLDCARD 目前的韌體版本。例如，在我的情況下，版本是 "*1.2.3Q*"。


![CCQ](assets/fr/019.webp)


查看 [COLDCARD官方網站](https://coldcard.com/downloads) 是否有更新的版本。點選 "*Download*"下載新的韌體。


![CCQ](assets/fr/020.webp)


此時，我們強烈建議檢查下載韌體的完整性和真實性。為此，請下載 [包含所有版本的哈希值並由開發人員簽署的文件](https://raw.githubusercontent.com/Coldcard/firmware/master/releases/signatures.txt)，使用 [開發人員的公開金鑰](https://keybase.io/dochex) 驗證簽署，並確認簽署文件中指示的 Hash 與從網站下載的韌體相符。如果一切正確，您就可以繼續更新。


如果您不熟悉此驗證程序，我建議您參考此教程：


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

使用 microSD 卡，並將韌體檔案 (文件名為 `.dfu`)傳輸至該卡。將 microSD 卡插入 COLDCARD 的其中一個連接埠。


![CCQ](assets/fr/021.webp)


然後，在韌體更新功能表中選擇「*From MicroSD*」。


![CCQ](assets/fr/022.webp)


選擇韌體對應的檔案。


![CCQ](assets/fr/023.webp)


按下「*ENTER*」按鈕確認您的選擇。


![CCQ](assets/fr/024.webp)


更新韌體時，請稍候。


![CCQ](assets/fr/025.webp)


更新完成後，請輸入 PIN 碼以解除鎖定裝置。


![CCQ](assets/fr/026.webp)


您的韌體已更新。


## COLDCARD Q 參數


如果您願意，可以進入「*設定*」功能表探索 COLDCARD 的設定。


![CCQ](assets/fr/027.webp)


在此功能表中，您可以找到各種自訂選項，例如設定螢幕亮度或選擇預設測量單位。


![CCQ](assets/fr/028.webp)


我們將在下一教學中瞭解其他進階設定：


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0

## 建立 Bitcoin Wallet


現在要 generate 一個新的 Bitcoin Wallet！為此，您需要建立一個 Mnemonic 詞組。在 Coldcard 上，您有三種方法來產生這個短語：




- 僅使用內部隨機數字產生器 (TRNG)；
- 使用 TRNG 與擲骰的組合來增加熵；
- 僅使用擲骰。


**對於初學者和中級使用者，我們建議只使用 COLDCARD 的內部隨機數生成器**。


我不推薦只使用骰子的選項，因為執行不力可能會導致句子的熵值不足，危及 Wallet 的安全性。


然而，最好的選擇肯定是第二種，它結合 TRNG 與外部熵源的使用。此方法可保證與 TRNG 單獨使用時相同的最低熵，並在內部產生器可能失效（無論是否自發）的情況下增加額外的安全層級。選擇此結合 TRNG 與擲骰的選項，您可以更有效地控制判語的產生，而不會因您執行不力而增加風險。


按一下「*新增 seed 詞彙*」。


![CCQ](assets/fr/029.webp)


您可以選擇句子的長度。我建議您選擇 12 個字的句子，因為它的管理複雜度較低，提供的 Wallet 安全性也不比 24 個字的句子低。


![CCQ](assets/fr/030.webp)


然後 COLDCARD 將顯示 TRNG 所產生的復原短語。如果您希望增加額外的外部熵，請按 "*4*"鍵。


![CCQ](assets/fr/031.webp)


這將會帶您到一個頁面，您可以在這裡擲骰子來增加熵。擲出盡可能多的骰子（建議最少擲 50 次，但少一點也沒什麼，因為您已經從 TRNG 的熵中獲益），然後用「*1*」到「*6*」鍵記錄結果。完成後，按「*ENTER*」確認。


![CCQ](assets/fr/032.webp)


新的 Mnemonic 詞組會根據您剛剛提供的熵和 TRNG 的熵顯示出來。


**警告：這個 Mnemonic 可以完全無限制地存取您所有的 bitcoins**。任何持有此短語的人都可以盜取您的資金，即使沒有實體存取您的 COLDCARD。如果您的 COLDCARD 遺失、被盜或破損，這 12 個字的短語可以恢復您對比特幣的存取權。因此，小心保存並存放在安全的地方是非常重要的。


您可以把它寫在 COLDCARD 隨附的硬紙板上，或者為了增加安全性，我建議您把它刻在不銹鋼支架上，以防止火災、水災或倒塌的風險。無論如何，千萬不要保存在數位媒體上，否則您可能會丟失您的 bitcoins。


將螢幕上提供的字句寫在您選擇的實體媒體上。視您的安全策略而定，您可以考慮將該句子製作數份完整的實體複本 (但最重要的是，不要將它分割開來)。重要的是要保持單字的編號和順序。


很明顯，**您絕對不能在網路上分享這些字**，這與本教程不同。此範例 Wallet 只會用在 Testnet 上，並會在本教程結束時刪除。


寫下單字後，按「*ENTER*」。


![CCQ](assets/fr/033.webp)


為了確認您已正確儲存短語，系統會要求您確認某些字詞。在鍵盤上選擇每個單字對應的數字。


![CCQ](assets/fr/034.webp)


您的 Wallet 現已建立！在螢幕右上角，您可以看到您的主私人密碼匙指紋。按「*ENTER*」。


![CCQ](assets/fr/035.webp)


現在您可以進入 COLDCARD 的主功能表。


![CCQ](assets/fr/036.webp)


## 在 Sparrow 上設定新的 Wallet


在 Sparrow Wallet 軟體與 COLDCARD 之間建立通訊有幾種方式。最直接的是使用 USB-C 傳輸線。不過，您的 COLDCARD 預設已停用纜線和 NFC 通訊。若要重新啟動，請瀏覽「*設定*」，然後選取「*硬體開啟/關閉*」，並啟動所需的通訊選項。


![CCQ](assets/fr/037.webp)


如果您希望將 COLDCARD 與電腦完全隔離，您可以選擇使用 QR 碼或 microSD 卡進行間接的「空間」通訊。這就是本教學中要使用的方法。


前往「*進階/工具*」。


![CCQ](assets/fr/038.webp)


選擇「*匯出 Wallet*」。


![CCQ](assets/fr/039.webp)


然後選擇「*麻雀 Wallet*」。


![CCQ](assets/fr/040.webp)


按下「*ENTER*」以 generate 配置檔案。


![CCQ](assets/fr/041.webp)


然後選擇如何將此檔案傳送至 Sparrow。在這個例子中，我在插槽 "*A*「中插入了一個 microSD，所以我會選擇 」*1*"按鈕。您也可以按 "*QR*"按鈕，在 COLDCARD 螢幕上以 QR 碼的形式顯示資訊，然後用電腦的網路攝影機掃描這個 QR 碼。


![CCQ](assets/fr/042.webp)


啟動 Sparrow Wallet，跳過介紹頁面進入主畫面。檢查畫面右下方的開關，確定您已正確連線到節點。


![CCQ](assets/fr/043.webp)


強烈建議您使用自己的 Bitcoin 節點。在本教程中，我使用的是公共節點（黃色），因為我在 Testnet 上，但若要用於生產，最好在本地使用 Bitcoin Core (Green)，或在遠端節點上使用 Electrum 伺服器（藍色）。


進入「*檔案*」功能表，選擇「*新增 Wallet*」。


![CCQ](assets/fr/044.webp)


命名您的 Wallet，然後按一下「*建立 Wallet*」。


![CCQ](assets/fr/045.webp)


在 "*Script Type*"下拉菜單中，選擇保護比特幣安全的腳本類型。


![CCQ](assets/fr/046.webp)


按一下「*Airgapped Hardware Wallet*」。


![CCQ](assets/fr/047.webp)


在「*COLDCARD*」標籤下，如果您打算掃描 COLDCARD 上顯示的 QR 代碼，請點選「*Scan...*」，或點選「*Import File...*」從 microSD 匯入檔案 (這是 `.json` 檔案)。


![CCQ](assets/fr/048.webp)


匯入後，檢查 Sparrow 上顯示的 「*主指紋*」是否與 COLDCARD 上顯示的相符。點選 "*Apply*"確認建立。


![CCQ](assets/fr/049.webp)


設定一個強大的密碼，以確保存取 Sparrow Wallet 的安全性。此密碼將保護您的公開金鑰，地址，標籤和交易歷史，防止未經授權的訪問。


最好儲存此密碼，以免忘記（例如：儲存在密碼管理器中）。


![CCQ](assets/fr/050.webp)


您的 Wallet 現在已設定為 Sparrow Wallet。


![CCQ](assets/fr/051.webp)


在您的 Wallet 收到您的第一個 bitcoins 之前，**我強烈建議您執行一次空的恢復測試**。寫下一些參考資訊，例如您的 xpub，然後在 Wallet 仍為空時重設您的 COLDCARD Q。然後嘗試使用您的紙本備份將 Wallet 還原至 COLDCARD。檢查還原後生成的 xpub 是否與您最初寫下的相符。如果是的話，您可以放心您的紙本備份是可靠的。


若要進一步瞭解如何執行復原測試，我建議您參閱此其他教學：


https://planb.network/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

## 接收比特幣


要收到您的第一筆 bitcoins，請先開啟並解鎖您的 COLDCARD。


![CCQ](assets/fr/052.webp)


在 Sparrow Wallet 上，按一下「*接收*」標籤。


![CCQ](assets/fr/053.webp)


在使用 Sparrow Wallet 提出的 Address 之前，請在您的 COLDCARD 螢幕上檢查。這種做法可讓您確認 Sparrow 上顯示的 Address 並非詐騙，而且 Hardware Wallet 確實持有隨後使用此 Address 所保證的比特幣所需的私密金鑰。這可以幫助您避免幾種類型的攻擊。


若要執行此檢查，請按一下 COLDCARD 上的「*Address Explorer*」功能表。


![CCQ](assets/fr/054.webp)


選擇您在 Sparrow 上使用的腳本類型。我的情況是 SegWit P2WPKH。我點擊它。


![CCQ](assets/fr/055.webp)


然後您就可以依序看到您不同的衍生位址。


![CCQ](assets/fr/056.webp)


與 Sparrow 檢查 Address 是否相符。在我的案例中，衍生路徑為 `m/84'/1'/0'/0/0` 的 Address 在 Sparrow 和 COLDCARD 上確實是 `tb1qwfwwvzssep4wyjg3vsgezmwa037ehvd4fhmjvr`。


![CCQ](assets/fr/057.webp)


另一個驗證此 Address 的 Ownership 的方法是直接從您的 COLDCARD 掃描其 QR 代碼到 Sparrow。從 COLDCARD 主畫面，選擇「*Scan Any QR Code*」。您也可以使用鍵盤上的 "*QR*"鍵。


![CCQ](assets/fr/058.webp)


掃描 Sparrow Wallet 上顯示的 Address 的 QR 代碼。


![CCQ](assets/fr/059.webp)


確定 COLDCARD 上顯示的 Address 與 Sparrow 上顯示的相符。然後按下 "*1*" 按鈕。


![CCQ](assets/fr/060.webp)


Address 因此成功確認。


![CCQ](assets/fr/061.webp)


現在您可以新增一個 "*Label*" 來描述這個 Address 將要保護的 bitcoins 來源。這是一個很好的做法，可以讓您更好地管理您的 UTXO。


![CCQ](assets/fr/062.webp)


如需更多關於標籤的資訊，我也建議您參考這份教學：


https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

然後您就可以使用這個 Address 來接收比特幣。


![CCQ](assets/fr/063.webp)


## 發送比特幣


現在您已經在 COLDCARD 抵押的 Wallet 中收到第一張 Sats，您也可以花掉它們！


一如往常，首先開啟並解鎖您的 COLDCARD Q，然後打開 Sparrow Wallet，並導航至「*傳送*」標籤以準備新的交易。


![CCQ](assets/fr/064.webp)


如果您希望進行 「硬幣控制」，即具體選擇在交易中消耗哪些 UTXOs，請移至 "*UTXOs*"標籤。選擇您要消耗的 UTXOs，然後點擊 "*Send Selected*"。您將被重新導向至 「*發送*」標籤中的相同畫面，但您已為交易選擇了UTXO。


![CCQ](assets/fr/065.webp)


輸入目的地 Address。您也可以按一下「*+ 新增*」按鈕，輸入多個位址。


![CCQ](assets/fr/066.webp)


寫下「*標籤*」以記住此支出的目的。


![CCQ](assets/fr/067.webp)


選擇要傳送到此 Address 的金額。


![CCQ](assets/fr/068.webp)


根據當前市場調整交易費率。


![CCQ](assets/fr/069.webp)


確定所有交易參數都正確，然後按一下「*建立交易*」。


![CCQ](assets/fr/070.webp)


如果一切都令您滿意，請按一下「*完成簽署交易*」。


![CCQ](assets/fr/071.webp)


當您在Sparrow建立交易後，就該用您的COLDCARD來簽章了。要將 PSBT (未簽署的交易) 傳輸到您的裝置，您有幾種選擇。如果啟用有線資料傳輸，您可以直接透過 USB-C 連線傳送交易，就像傳送其他 Hardware Wallet 一樣。在這種情況下，在 Sparrow 上，您必須點選右下角的「*簽署*」按鈕。在我的範例中，由於 COLDCARD 並未透過纜線連接，因此此按鈕被阻擋。


![CCQ](assets/fr/072.webp)


如果您希望在 Hardware Wallet 與電腦之間維持沒有直接接觸的「空間」連線，您有兩個選擇。第一種，也是更複雜的，是使用 microSD 卡。將 microSD 卡插入電腦，透過 Sparrow 上的「*儲存交易*」按鈕記錄交易，然後將此卡傳輸至 COLDCARD 上的連接埠。


![CCQ](assets/fr/073.webp)


然後存取「*Ready To Sign*」功能表。


![CCQ](assets/fr/074.webp)


查看您的 COLDCARD 上的交易詳情，包括收款 Address、發送金額和交易費用。


![CCQ](assets/fr/075.webp)


如果一切無誤，請按「*ENTER*」按鈕簽署交易。


![CCQ](assets/fr/076.webp)


然後將 microSD 放回電腦，在 Sparrow 上點選「*載入交易*」，從 microSD 載入已簽署的交易。然後您就可以在上傳到 Bitcoin 網路之前執行最後檢查。


![CCQ](assets/fr/077.webp)


在 Air-Gap 中使用 COLDCARD 簽署的第二種方法比 microSD 方法簡單得多，就是直接透過裝置的相機掃描 PSBT。在 Sparrow 上，選擇「*Show QR*」。


![CCQ](assets/fr/078.webp)


在 COLDCARD 上，選擇「*掃描任何 QR 碼*」。您也可以使用鍵盤上的「*QR*」鍵。


![CCQ](assets/fr/079.webp)


使用 COLDCARD 的相機掃描 Sparrow 上顯示的 QR 代碼。


![CCQ](assets/fr/080.webp)


交易詳細資訊會再次出現以進行驗證。如果一切滿意，請按「*ENTER*」簽名。


![CCQ](assets/fr/081.webp)


然後，您的COLDCARD會以QR碼的形式顯示已簽署的交易。使用您電腦的網路攝影機，在Sparrow上選擇 "*Scan QR*"來掃描這個QR碼。


![CCQ](assets/fr/082.webp)


您已簽署的交易現在可以在 Sparrow 上看到。最後一次檢查一切是否正確，然後點擊「*廣播交易*」在 Bitcoin 網路上廣播。


![CCQ](assets/fr/083.webp)


您可以在 Sparrow Wallet 的「*交易*」標籤中追蹤您的交易。


![CCQ](assets/fr/084.webp)


恭喜您，現在您已掌握 COLDCARD Q 與 Sparrow Wallet 的基本使用方法！


如果您覺得本教學有用，請在下方留下 Green 拇指，我將非常感激。請隨時在您的社交網路分享本教學。非常感謝


我也建議您看看其他教學，其中我們討論了 COLDCARD Q 的進階選項：


https://planb.network/tutorials/wallet/hardware/coldcard-q-advanced-b8cc3f29-eea9-48fe-a953-b003d5b115e0