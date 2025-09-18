---
name: COLDCARD Q - 專家
description: 使用 COLDCARD Q 的進階選項
---
![cover](assets/cover.webp)


在之前的教學中，我們為初學者介紹了 COLDCARD Q 的初始設定及其基本功能。如果您剛剛收到 COLDCARD Q，還沒有進行設定，我建議您先從那個教學開始，然後再繼續這裡的教學：


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

本新教程專門介紹 COLDCARD Q 的進階選項，專為進階且偏執的使用者所設計。事實上，COLDCARD與其他硬體錢包的區別在於其許多進階的安全功能。當然，您不必使用所有這些選項。只需選擇適合您安全策略的選項即可。


**警告**，錯誤使用其中一些進階選項可能會導致您的比特幣丟失或您的 Hardware Wallet 損毀。因此，我強烈建議您仔細閱讀每個選項的建議和說明。


在您開始之前，請確定您可以存取 12 或 24 字元 Mnemonic 詞組的實體備份，並透過下列功能表檢查其有效性：`進階/工具 > 危險區 > seed 功能 > 檢視 seed 詞組`。


![CCQ](assets/fr/01.webp)


## BIP39 passphrase


如果您不知道什麼是 BIP39 passphrase，或者不完全清楚它的工作原理，我強烈建議您事先看看這篇教學，它涵蓋了瞭解使用 passphrase 相關風險所需的理論基礎：


https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

請記住，一旦您在 Wallet 上設定了 passphrase，僅靠 Mnemonic 並不足以重新獲得比特幣的存取權。您需要 Mnemonic 和 passphrase。此外，每次解鎖 COLDCARD Q 時，您都需要輸入 passphrase。這可提高安全性，因為沒有 passphrase，實體存取 COLDCARD 和獲知 PIN 碼都是不充分的。


在 COLDCARD 上，您有兩個選項可以管理您的 passphrase：


1. **Classic entry:**每次使用 Hardware Wallet 時，您都要手動輸入 passphrase，就像使用其他硬體錢包一樣。COLDCARD Q 的全鍵盤簡化了這項工作。


2. **您可以選擇加密 passphrase 並將其儲存在 microSD 卡中。在這種情況下，每次使用時您都需要將 microSD 插入 COLDCARD Q。請注意，此 microSD 只能在您的 COLDCARD Q 上使用，而非備份。因此，非常重要的是，您也應在紙張或金屬等實體媒體上保留一份 passphrase 副本。**


若要設定 BIP39 passphrase，請存取「*passphrase*」功能表。


![CCQ](assets/fr/02.webp)


使用鍵盤輸入您的 passphrase。請務必選擇強大的 passphrase（長且隨機），並做實體備份。


![CCQ](assets/fr/03.webp)


設定好 passphrase 後，COLDCARD Q 會顯示與此 passphrase 相關的新 Wallet 的主密碼指紋。請務必儲存此指紋。當您未來使用裝置時，再次輸入您的 passphrase 時，您可以檢查顯示的指紋是否與您儲存的指紋相符。這項檢查可確保您在輸入 passphrase 時沒有出錯。


![CCQ](assets/fr/04.webp)


現在您可以按下「*ENTER*」，將此 passphrase 套用至您的 Mnemonic 樂句，並啟用新的 Wallet。如果您希望將此 passphrase 儲存於 microSD 上，請將記憶卡插入適當的插槽，然後按「*1*」。


![CCQ](assets/fr/05.webp)


您的 passphrase 已套用。按鍵印記會出現在主螢幕和螢幕上方。


![CCQ](assets/fr/06.webp)


每次解鎖您的 COLDCARD Q 時，您都需要存取「*passphrase*」功能表，並以上述相同方式輸入您的 passphrase，將其套用至儲存於裝置中的 Mnemonic 並存取正確的 Bitcoin Wallet。


![CCQ](assets/fr/07.webp)


如果您已將 passphrase 儲存於 microSD 卡中，每次使用時，請將 microSD 卡插入 COLDCARD 並存取「*passphrase*」功能表。您的 COLDCARD 會直接從 microSD 載入 passphrase，所以您不需要手動輸入。點選「*Restore Saved*」。


![CCQ](assets/fr/08.webp)


檢查載入的 passphrase 的長度和首字母是否正確。


![CCQ](assets/fr/09.webp)


確認所顯示的指紋與您 Wallet 的指紋相符，然後按一下「*Restore*」。


![CCQ](assets/fr/10.webp)


請記住，使用 passphrase 表示您需要匯入一組新的金鑰，這組金鑰是由 Mnemonic 樂句與 passphrase 組合而來，並將其匯入 Wallet 管理軟體 (例如 Sparrow Wallet)。要做到這一點，請按照此其他教程中的步驟 「*在 Sparrow 上配置一個新的 Wallet*」進行：


https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3

## 解鎖選項


COLDCARD 在裝置解鎖過程中也享有許多選項。讓我們進一步瞭解這些進階選項。


### 詭計密碼


Trick PIN 是一個次要的 PIN 碼，有別於初始裝置設定時所定義的 PIN 碼。當 COLDCARD 開機時輸入此密碼，即可啟動預先設定的特定動作。您可以設定多個 Trick PIN 碼，每個都與不同的動作相連結。這些功能可讓您依照個人的安全策略調整 COLDCARD。這些功能特別適用於身體受脅迫的情況，例如搶劫時（Bitcoin 社群通常稱之為「*$5 扳手攻擊*」）。


若要啟動快速密碼並將其與動作關聯，請存取`設定 > 登入設定 > 快速密碼`功能表。


![CCQ](assets/fr/11.webp)


選取「*新增技巧*」。


![CCQ](assets/fr/12.webp)


設定與動作相關的 PIN 碼，並記得儲存。


![CCQ](assets/fr/13.webp)


然後選擇每次輸入此 Trick PIN 碼時要自動執行的動作。以下是 PIN 碼可用的動作清單：




- "*Brick Self*：如果輸入 Trick PIN 碼，此動作會銷毀兩顆 COLDCARD Q 晶片，使裝置完全無法使用。屆時將無法轉售、重複使用或甚至將其退回 Coinkite。裝置將無法復原地過時。此功能可在搶劫時使用，讓歹徒相信他永遠無法取得您的比特幣。 **請注意**：如果沒有Mnemonic短語和任何passphrase的實體備份，您的比特幣將永久丟失。


![CCQ](assets/fr/14.webp)




- "*Wipe seed*"：此功能表提供多種刪除 seed 的動作，也就是在不破壞 COLDCARD 的情況下重設 COLDCARD。與 "*Brick Self*"選項不同的是，它將可能使用您的 Mnemonic 語句備份來重新配置裝置。但是，如果沒有這個備份，您的 bitcoins 將會丟失。以下是可用的選項：
 - "*Wipe & Reboot* ：移除 seed 並重新啟動 COLDCARD，螢幕上不顯示任何資訊。
 - "*Silent Wipe*」：默默地擦除 seed，然後在隨機偽造的 Wallet 上解鎖 COLDCARD，就像什麼都沒發生過一樣。
 - "*Wipe -> Wallet*"：謹慎地移除 seed，並在預先設定的次要 Wallet 上解鎖 COLDCARD，此 Wallet 設計為誘餌。此 Wallet 可能包含您 Bitcoin 存款的一小部分，以滿足攻擊者的需求。
 - "*Say Wiped, Stop*"：刪除 seed，並在螢幕上顯示訊息「seed 已抹除，停止」。


![CCQ](assets/fr/15.webp)




- "*Duress Wallet*"：使用此動作，Trick PIN 碼會解鎖使用 BIP85 從 seed 衍生出來的 Wallet。這個次要的 Wallet 可以用作誘餌來滿足攻擊者。COLDCARD 就像真正的 Wallet，但如果沒有主密碼 (與 Trick PIN 不同)，攻擊者永遠無法存取真正的 Wallet。此策略旨在讓人們相信與 Trick PIN 連結的 Wallet 是唯一存在的 Wallet。


![CCQ](assets/fr/16.webp)




- 「*登入倒數*」：此功能表會將執行前有倒計時的動作歸類。 **警告**，其中一些可能會破壞您的裝置或導致您的 bitcoins 損失。以下是可用的子動作：
 - "*Wipe & Countdown* ：清除 COLDCARD 記憶體中的 seed，然後開始一小時倒數。如果沒有儲存您的 Mnemonic 或 passphrase，您的 bitcoins 將會遺失。這個選項的設計是為了騙取攻擊者，讓他們以為裝置會在倒數結束時解鎖，但事實上它會被重設為出廠設定。
 - "*Countdown & Brick*」：開始一小時倒數，倒數結束時 COLDCARD 會銷毀其兩個安全晶片，使其永久無法使用。如果沒有備份，您的比特幣將會丟失。這個動作是為了愚弄攻擊者而設計的，攻擊者會以為他在等待解鎖，但實際上裝置會自毀。
 - "*Just Countdown* ：觸發一個簡單的一小時倒數，之後 COLDCARD 會重新啟動，不需任何進一步的動作。seed 不會被刪除，裝置仍保持原樣。請小心不要將這個動作與 「*登入倒數*」選項混淆，這個選項會在主 PIN 碼上加入倒數，同時提供真正 Wallet 的存取權。


![CCQ](assets/fr/17.webp)




- "*Look Blank*"：這個動作會讓 COLDCARD 看起來是空的，讓人覺得 seed 已經被刪除。實際上，什麼都沒有發生，seed 仍然完好無損。這會模擬未使用或重設的 COLDCARD。


![CCQ](assets/fr/18.webp)




- "*Just Reboot* ：使用 Trick PIN 時，COLDCARD 只會重新開機。不執行其他動作。


![CCQ](assets/fr/19.webp)




- 「*Delta 模式*」：這個複雜的動作是專為有經驗的使用者所設計，以對抗高度複雜的脅迫攻擊，不論是來自國家或擁有特權資訊的親屬。當 Delta Mode 啟動時，COLDCARD 會提供存取真實 Wallet 的能力，讓攻擊者能夠瀏覽並確認這是正確的 Wallet。然而，交易簽章會被封鎖，因此無法進行任何 Bitcoin 傳輸。此外，Mnemonic 詞組的存取也會被停用，任何嘗試擷取的動作都會導致其刪除。為了提高可信度，與 Delta 模式一起使用的 Trick PIN 碼必須與真實 PIN 碼有相同的前綴 (以顯示相同的防釣字句)，但後綴必須不同。


![CCQ](assets/fr/20.webp)


選取動作後，請確認您的選擇。


![CCQ](assets/fr/21.webp)


然後，您可以在專屬功能表中檢視所有已設定的 Trick PIN。


![CCQ](assets/fr/22.webp)


選取現有的 Trick PIN，即可檢查相關的動作。您也可以使用「*隱藏秘訣*」隱藏它，使它在秘訣密碼功能表中不可見。您可以按一下「*Delete Trick*」將其刪除，或使用「*Change PIN*」變更 PIN 碼，但保留相關動作。


![CCQ](assets/fr/23.webp)


"*Trick PIN*「功能表中的 」*Add If Wrong*"選項可讓您設定特定動作，當嘗試輸入主 PIN 碼的次數不對時，該動作會自動啟動。允許嘗試的次數可以在設定時設定。


### 拼圖鍵盤


Scramble Keys 選項可讓您在輸入 PIN 碼時，擾亂鍵盤按鈕上顯示的數字。此功能可保護您 PIN 碼的機密性，即使在有人或攝影機監視的情況下也是如此。


若要啟動此選項，請存取功能表 `設定 > 登入設定 > 複製鍵'。


![CCQ](assets/fr/24.webp)


選擇「*擾亂鍵*」選項。


![CCQ](assets/fr/25.webp)


從現在開始，當您解鎖 COLDCARD Q 時，每次使用鍵盤上的按鍵時，都會隨機分配新的號碼。


![CCQ](assets/fr/26.webp)


### 登入倒數


此選項可讓您在每次嘗試解鎖COLDCARD時進行有系統的倒計時。該功能可與您的安全策略相結合，在發生盜竊時延遲對裝置的存取，或在簽署交易之前實施延遲，例如在發生脅持時保護您自己。然而，該倒計時適用於您的所有用途，包括合法使用 COLDCARD 時，您也必須耐心等待。請注意不要將此選項與 "*Just Countdown*「動作混淆，」*Just Countdown*"動作僅在使用特定的 Trick PIN 碼時啟動。


若要設定此選項，請存取功能表「設定 > 登入設定 > 登入倒數」。


![CCQ](assets/fr/27.webp)


選擇倒數時間。例如，如果您選擇 1 小時，則每次嘗試解鎖 COLDCARD Q 都必須等待 1 小時。


![CCQ](assets/fr/28.webp)


每次解鎖時，系統都會提示您輸入 PIN 碼。


![CCQ](assets/fr/29.webp)


然後等待倒數所設定的時間。


![CCQ](assets/fr/30.webp)


倒數結束時，您需要再次輸入 PIN 碼才能存取裝置。


![CCQ](assets/fr/31.webp)


### 計算機登錄


此選項可讓您在解鎖時將 COLDCARD 偽裝成計算機。若要啟動此功能，請進入功能表`設定 > 登入設定 > 計算機登入`。


![CCQ](assets/fr/32.webp)


選擇選項以啟動選項。


![CCQ](assets/fr/33.webp)


從現在開始，每次開啟裝置時，都會顯示一個包含基本指令的工作計算機。


![CCQ](assets/fr/34.webp)


例如，您可以計算「*Plan B 網路*」的 SHA256 Hash。


![CCQ](assets/fr/35.webp)


要從計算機模式解鎖 COLDCARD，首先輸入您的 PIN 碼前綴，後跟一個破折號。例如，如果您的PIN碼是`00-00`（這個代碼很弱，只是一個例子，所以請選擇一個強大的PIN碼），請輸入`00-`。然後COLDCARD會顯示您的兩個反釣魚字詞。


![CCQ](assets/fr/36.webp)


然後輸入完整的 PIN 碼，並以空格或破折號分隔，例如：`00 00`。


![CCQ](assets/fr/37.webp)


然後 COLDCARD 將退出計算機模式並正常解鎖。


## 徹底銷毀您的 COLDCARD


如果您打算棄置您的 COLDCARD Q，例如因為您現在使用另一個 Hardware Wallet，那麼正確銷毀裝置是很重要的。這可確保第三方無法復原與您的 Wallet 相關的資訊。


根據您的需求，資訊銷毀可分為三個層級。在您開始之前，請確定您的 Wallet 已經匯入另一個 Hardware Wallet，您可以存取您所有的資金，最重要的是，您的 Mnemonic phrase 和任何 passphrase 都是可以使用的。如果沒有 Wallet 備份，您的 COLDCARD 毀壞將會導致您的 bitcoins 損失。


第一層銷毀包括只刪除 seed。此選項可將您的 Mnemonic 詞組從 COLDCARD 的記憶體中刪除，但保留裝置的功能。如果您日後想要再次使用 COLDCARD Q，這是最理想的選擇。若要從記憶體中刪除 seed，請存取 `進階/工具 > 危險區 > seed 功能 > 毀滅 seed`功能表。


![CCQ](assets/fr/38.webp)


第二層破壞包括透過軟體永久停用 COLDCARD 的兩個安全晶片。這個動作會使裝置完全無法使用。您將無法轉售、重複使用或退回給Coinkite：它將被永久銷毀。若要繼續，請遵循上一節所述有關 "*Brick Me*" 的步驟。PIN碼，然後在解鎖COLDCARD時故意輸入此PIN碼。


第三級涉及 COLDCARD Q 安全元件的實體破壞。和之前一樣，這將使裝置無法使用。要做到這一點，請使用電鑽在裝置右上方的兩個晶片上開孔（一旦倒轉），靠近 "*SHOOT HERE*"字樣。


**重要預防措施** ：




- 為避免觸電的危險，請從本裝置取出電池，並在操作前拔下電源插頭。
- 關機後等待幾分鐘再開始鑽孔。
- 戴上絕緣手套和安全護目鏡，以確保您的安全。


![CCQ](assets/fr/39.webp)


一旦晶片已打孔，請勿嘗試重新連接 COLDCARD Q。


恭喜您，現在您已經熟悉 COLDCARD Q 的進階選項了！


如果您覺得本教學有用，請在下方留下 Green 的拇指，我將非常感激。歡迎在您的社交網路分享本教學。非常感謝


我也推薦這份教學，其中我們討論了 CCQ 的直接競爭對手 Ledger Flex ：


https://planb.network/tutorials/wallet/hardware/ledger-flex-3728773e-74d4-4177-b39f-bd923700c76a