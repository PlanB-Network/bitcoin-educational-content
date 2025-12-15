---
name: Electrum Airgap
description: 邁向安全的第一步，使用Electrum的冷錢包
---
![cover](assets/cover.webp)



## Cold Wallet



在本教程中，我將說明如何製作您的第一台 airgap signing 裝置，即使沒有專用的 Hardware Wallet，也可以斷開與網際網路的連線。您只需要有兩台電腦即可：




- 舊裝置將永遠無法連線至網際網路；
- 您日常使用的電腦。



這種配置比傳統的 "Hot Wallet 「具有更高的安全性：舊的電腦 - 沒有網路連線 - 是您私人金鑰的保管人，這些金鑰永遠不會暴露在網際網路上，而是離線儲存 (」airgap 「或 」Cold")。



取而代之的是，您會在日常使用的電腦上安裝 Wallet 顯示器 (「僅用於觀看」)，該顯示器連接到網路，例如，您可以用它來檢查餘額和準備收據交易。



## Wallet 氣隙：什麼和如何



透過執行本指南中的步驟，我們將在兩台不同的電腦上安裝兩個 Software Wallet Electrum，最後產生兩個具有不同金鑰庫的 Wallet：Wallet airgap 將使用 Wallet HD 的整個階層結構，而 Wallet display 則使用主公鑰產生。



這兩個錢包在各方面都會非常不同。正如我們將要看到的，它們唯一的共同點就是地址：




- airgap 電腦上的 gW-13 只能簽名，但由於與網路斷開，因此不知道所使用的餘額和位址；
- 在沒有私人金鑰的情況下，日常電腦上的 Wallet 只能準備和傳播交易，而無法處理支出。



## 初步準備



要下載 Electrum，我建議您按照本教學的第一個步驟進行：



https://planb.academy/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177

下載後，安裝前請先確認發行版本，然後進行「單一伺服器」設定，您可以在說明部分的「從虛擬 Wallet 開始」中找到。



只有安裝在日常電腦上的 Wallet 才需要執行「單一伺服器」組態作業，因為其他電腦會一直處於離線狀態。



下面的操作涉及在兩台不同的電腦（和錢包）上練習，因此為了方便和集中注意力，我選擇將 Wallet airgap 設定為淺色主題，而 Wallet 顯示器設定為深色主題。



## Wallet 氣隙創建



下載並驗證 Electrum 下載完成後，複製一份可執行檔，並將其離線帶到您的電腦上。然後啟動它並安裝 Electrum。



按兩下以啟動 Electrum：您要使用這台 Wallet 的電腦是離線的，請忽略網路設定，並進入 Wallet 的建立，在本指南中，我們稱之為`airgap`。



![image](assets/en/01.webp)



選擇_標準錢包_。



![image](assets/en/02.webp)



然後選擇 _Create a new seed_，讓軟體 generate Mnemonic。



![image](assets/en/03.webp)



準確地從 Electrum 謄寫 12 個 generate 單字到紙背，然後進行驗證步驟，在 Electrum 要求時按順序重新輸入單字。



![image](assets/en/04.webp)



![image](assets/en/05.webp)



Wallet 建立完成後，請設定複雜的密碼 (`Strong`)，以加密 airgap 裝置上的 Wallet 檔案。此步驟非常精細且重要，因為現在選擇的密碼可防止存取 Wallet，Wallet 具有處分權，能夠花費資金簽署交易。



![image](assets/en/06.webp)



按一下 _Finish_ 即可定義 Wallet，並顯示在螢幕上。當然，網路連線指示器（即右下角的彩點）是紅色的，因為電腦已斷線，不允許 Wallet 顯示線上按鍵。



![image](assets/en/07.webp)



## 視覺化的創作 Wallet



現在您的 Wallet 已經擁有離線私人金鑰，您需要設定一個顯示 Wallet，或稱為「僅用於觀看」，它可以讓您檢視餘額，以及準備收據交易，繼續安全地累積 Sats。



從位於離線裝置上的 Wallet，選擇 _Wallet_ -> _Information_ 功能表



![image](assets/en/08.webp)



包含您所有 Wallet 資訊的視窗將會出現，您可以勾選 `衍生路徑 ` 和 `主指紋 `，例如將它們標示在 Mnemonic 句子中的字旁 (強烈建議)。



![image](assets/en/09.webp)



請記住，您是從未連線的電腦取得這些資料，因此您必須將 `zpub` 複製/貼到文字檔，然後儲存到 USB 隨身碟。



現在您可以移動到連上網際網路的電腦，啟動 Electrum 並建立新的 Wallet。



從 _File_ 功能表中，選擇 _New/Restore_。



![image](assets/en/10.webp)



新的 Wallet 只限檢視，因此本指南中我們稱之為 `只限檢視`。



![image](assets/en/12.webp)



在下一個畫面中選擇 _Standard wallet_（標準錢包），然後按一下 _Next_ （下一步）。



![image](assets/en/13.webp)



在選擇 `Keystore` 時請小心：要建立顯示 Wallet 請選擇 _Use a master key_。然後繼續_Next_。



![image](assets/en/14.webp)



在此貼上從 Wallet 離線複製並透過 USB 媒體帶到此電腦的 `zpub`。



![image](assets/en/15.webp)



最後，也為此 Wallet 設定一個強密碼，可能與對應的 Cold 所選的密碼不同。



您會看到顯示 Wallet 並帶有警告。該訊息提醒您這是僅供顯示的 Wallet，您不能使用它來花費相關的資金。



**請注意**：*因此*，您需要始終擁有私人鑰匙來處置此 Wallet 的 UTXO。有了良好的備份系統，您就不難完全擁有您的比特幣。



![image](assets/en/16.webp)



每次打開 Wallet 都會出現這個警告。按一下 _Ok_，讓我們進入驗證步驟。



## 驗證兩個 Wallet



正如我們在本指南一開始所學到的，Wallet 空間閘道及其顯示器 Wallet 是兩個具有不同功能但**共用相同位址的組合**。



如果我們將兩個 Wallet 並排看，直觀上我們會發現在 Wallet 空格中有一個「seed」符號，而在只顯示的 Wallet 中則沒有。即使是這個細節也能讓您記住 Wallet 顯示 Wallet 沒有私密金鑰。



![image](assets/en/17.webp)



然而，為了進行準確的第一次檢查，請在兩個錢包中選擇「地址」功能表：由於兩者共用相同的地址，因此兩者的地址清單應該相同。



![image](assets/en/18.webp)



⚠️ **注意**： **不能有中間點；地址必須相同。如果它們不同，則必須刪除目前完成的所有工作，並重新開始**。



現在您可以進行兩種不同的檢查。首先，嘗試刪除兩個錢包，然後在適當的電腦上各自從頭開始還原。如果您繼續進行此驗證，則顯示 Wallet 的步驟與上述步驟相同。



但是，對於 Wallet airgap，您必須在 `keystore` 畫面中選擇 _I already have a seed_（我已經有種子），然後透過複製紙張備份中的文字來輸入。



在「無負擔」試用結束後，您可以嘗試進行小額交易，並立即消費。



## 收支交易



要開始使用您的 Electrum 空間，您可以先用少量的金額進行收據交易，然後將其花費在您自己的 Address 上。然後您就可以熟悉程序，驗證您是否完全掌控資金。



**注意**：在您有信心可以順利執行所有操作之前，我不建議您在 Wallet 上存入大量資金。



以下說明的步驟乍看之下似乎很複雜。不要因此而沮喪：當您第一次嘗試這些步驟時，您會發現只需要幾分鐘就可以完成。



要接收資金，您必須使用位於您電腦上連接到網際網路的顯示器 Wallet。從`接收`選單中點選_建立請求_，讓 Electrum generate 第一個可用的 Address，並使用它寄給我們幾個 Satss。



![image](assets/en/19.webp)



![image](assets/en/20.webp)



一旦交易被傳播，您就可以看到--很自然地--它只在顯示器 Wallet 上可見，而不在 Wallet 氣隙上。



![image](assets/en/21.webp)



在您的交易獲得一些確認後，您可以準備費用，從而嘗試從 Wallet 網外進行簽名程序。然後在專用看板上準備交易，並按 _Preview_ 來檢查。



![image](assets/en/22.webp)



您會看到進階交易視窗：




- 交易未簽署 (`Status:未簽署)；
- Sign 「和 」Broadcast "指令被禁止。



您唯一能做的就是將交易原封不動地匯出，拿到 Wallet 空間閘道上簽署。



將 USB 隨身碟插入電腦，然後從左下方的功能表中選擇 _Share_。



![image](assets/en/23.webp)



之後，選擇 _ 儲存到檔案_。



![image](assets/en/24.webp)



將交易儲存至 USB 隨身碟。



您會注意到，Electrum 給檔案的名稱帶有 transaction ID 的第一位數，而檔案的副檔名是 `.PSBT`，意思是 `Partially Signed Bitcoin Transaction`。



使用 `.PSBT` 檔案萃取媒體，並離線連接至電腦。



從 Wallet airgap，現在選擇 _Tools_ 功能表，然後選擇 _Load transaction_，接著選擇 From file_。



![image](assets/en/25.webp)



使用檔案管理員，從其位置選擇 `.PSBT`。



![image](assets/en/29.webp)



網外電腦軟體會自動開啟進階交易視窗，與您在 Wallet 顯示器上看到的完全相同。狀態是「未簽署」，但不同的是這裡的「簽署」指令是有效的。而這正是您要執行的。



![image](assets/en/26.webp)



![image](assets/en/27.webp)



現在交易已經簽署，請記住您的 Wallet 是在離線機器上。因此，即使您看到 `Broadcast` 指令已啟動，您的 Wallet 也無法將交易傳送到 Bitcoin 網路。



您現在需要做的是重複將已簽署的交易匯出到 usb 隨身碟的作業，這樣您就可以將它匯入連線到網際網路的電腦中，並將它傳播出去。



從左下方的功能表，再次選擇 _Share_ ，然後選擇 _Save to file_。



![image](assets/en/28.webp)



現在檔案的副檔名不同了： **交易的副檔名不是`.PSBT`，而是`.txn`。從現在開始，Electrum 會讓您從未簽署的交易中辨別出已簽署的交易**。



![image](assets/en/30.webp)



若要最終傳播交易，請將 usb 棒從離線電腦中取出，並插入連接至網際網路的電腦中。



從專用看板，重複匯入程序，即從 _Tools_ 功能表選擇 _Load transaction_，最後再選擇 _From file_。



![image](assets/en/31.webp)



Electrum 會為您打開交易視窗，與之前 Wallet 上顯示的視窗明顯不同，現在已經簽 署 (`Status:Signed`)，並可使用`Broadcast`指令。



您需要做的最後一個操作就是這樣：



![image](assets/en/32.webp)



## 結論



您的測試已經完成。如果您按照指南操作並得到了相同的結果，您已經在兩台不同的電腦上用 Electrum 創建了一個 Wallet Cold，您可以用空間隙的方式來儲存您的比特幣。



您唯一需要密切注意的有兩點：


1) **never use Wallet airgap to generate receiving addresses**.因為它是離線的，所以它永遠會提供您第一個 Address，這與您剛剛用來做測試交易的 Address 不謀而合；



![image](assets/en/33.webp)



_從上面的圖片可以看到，離線的 Wallet 不知道自己的 Address 歷史。它在這方面是完全盲目的。 ** 它唯一能為您做的任務就是儲存您的離線金鑰和簽署您的交易**_。



2) 使用專用的 USB 隨身碟，**不要使用您經常使用的媒體**。日常使用的工具更容易受到網路攻擊，而且在無意間，您甚至可能攻擊您保持與網路斷線的電腦。您僅用於此目的的 USB 隨身碟與您的電腦進行線上接觸的機會非常少，特別是如果您是一個不需要花費的 hodler，因此可以降低接收病毒、惡意軟體等後再傳輸的可能性。