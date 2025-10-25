---
name: Zeus Embedded
description: 如何使用 Lightning Zeus 嵌入式 Wallet
---
![cover-zeus-embedded](assets/cover.webp)



ZEUS 最初是用於遠端管理閃電節點的行動應用程式，可讓您控制安裝在遠端伺服器上的節點


但此應用程式還有一個「嵌入式節點」。



**在本教程中，我們將探討應用程式的這個面向。這讓任何人都可以在行動裝置上擁有自己的閃電節點，而不需要專用伺服器，就像 ACINQ 提供其令人難以置信的 Wallet Lightning Phoenix 一樣。**



https://planb.network/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf

*提醒一下，Lightning 是一個與 Bitcoin 並行運作的網路，使比特幣的交換無需有系統地進行 On-Chain 交易。其結果是近乎瞬間的交易，無需等待 10 分鐘來驗證一個區塊。這在支付實體世界中的商家時特別有用。更重要的是，Lightning 提供了 Bitcoin 網路所不具備的* **保密性**。



**Zeus "Integrated "** 針對希望最大化隱私和自主權的比特幣使用者。


簡而言之，它有可能是**cypherpunks夢寐以求的Wallet手機**。儘管它仍處於起步階段（alpha 版本），而且有一些錯誤，但它的功能非常多，毫無疑問會讓我們中最無畏的人感到高興，因為他們想要最大的控制權和可選性。



另一方面，我不認為它目前適合不熟悉 Bitcoin、只想用簡單方式傳送/接收 Satoshis 的初學者。儘管這種情況在未來可能會改變，因為透過 Cashu (chaumian Ecash) 協定的保管功能正在為初學者實作中...



## 安裝應用程式



前往 [專案網站](https://zeusln.com/) 下載適用於您智慧型手機作業系統的應用程式：



![image](assets/fr/01.webp)



![image](assets/fr/02.webp)



## 建立投資組合



應用程式啟動後，按一下「快速啟動」按鈕開始建立 Wallet。



![image](assets/fr/03.webp)





接著會出現一系列初始化畫面。等待片刻，然後再等待幾分鐘，直到節點透過 Neutrino 達到 100% 同步。



這可能需要幾分鐘。為了提供資訊，neutrino 是行動錢包存取 Blockchain Bitcoin 資訊的一種方式，而不需要執行 Full node。



![image](assets/fr/04.webp)





片刻之後，您就可以開始了。



![image](assets/fr/05.webp)




## 應用程式設定



準備好了，但不完全是，因為不言而喻，一個名符其實的 Zeus 使用者會以優雅和時尚的方式瀏覽他的 Wallet。所以我們得換他的頭像。



按一下螢幕右上角的頭像：



![image](assets/fr/06.webp)





按一下齒輪，然後按一下加號 "+" ：



![image](assets/fr/07.webp)





選擇最美麗的宙斯照片來代表這張 Wallet，然後按一下畫面下方的「CHOOSE PICTURE」，再按一下右上方的箭頭返回。



![image](assets/fr/08.webp)





最後，為您的 Wallet 賦予暱稱，然後按一下「儲存 Wallet 設定」使變更生效。最後，按一下左上角的返回箭頭，回到主畫面。



![image](assets/fr/09.webp)





這次我們可以真正開始了。



![image](assets/fr/10.webp)



### 生物辨識



若要保護 Wallet 的存取權，您可以新增 PIN 碼/密碼，並啟用生物辨識技術。



按一下左上方的水平虛線，即可進入 Wallet 主功能表。



![image](assets/fr/11.webp)





選擇「設定」，然後選擇「安全性」，最後選擇「設定/變更 PIN」。



![image](assets/fr/12.webp)





建立您的 PIN 碼、確認 PIN 碼，然後按相應的「Biometrics」按鈕啟動生物辨識技術。  使用左上方的箭頭返回主功能表。



![image](assets/fr/13.webp)




### 保存 Mnemonic 短語



回到主功能表後，按一下「備份 Wallet」，然後閱讀警告文字，該文字會告訴您，失去您即將收到的 24 個字就等於失去您的資金存取權，而且除了您之外，任何擁有這些字的人都可以存取您的資金。切勿將這些字詞交給任何人。



選擇螢幕下方的「I UNDERSTAND」。然後在 24 個單字上逐一按一下，將它們顯示出來，並仔細記下它們。



您可以將它寫在紙上，或者，為了增加安全性，也許將它刻在不銹鋼上，以防止火災、水災或倒塌。Mnemonic 的媒介選擇取決於您的安全策略，但如果您將 Zeus 用作包含中等金額的支出組合，紙張應該就足夠了。



如需更多關於儲存和管理 Mnemonic 詞組正確方法的資訊，我強烈建議您參考這篇教學，尤其是對於初學者而言：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![image](assets/fr/14.webp)



完成後，按一下螢幕下方的「我已經備份了我的 24 個字元」，我們就回到主畫面，準備接收第一筆比特幣了。




## 選項 1 - 接收 On-Chain 比特幣並開啟閃電通道



**Zeus Embedded** 主要設計為嵌入式閃電節點，但也可當作 Wallet On-Chain 使用。



要接收 On-Chain 比特幣，請點擊「On-Chain」按鈕，然後點擊「接收」。


最後，掃描 QR 代碼或複製 Bitcoin Address 存入資金。



![image](assets/fr/15.webp)





一旦確認資金並存入您的 Wallet，您就可以使用這些資金來開啟**閃電通道**。您的 Lightning 頻道是您通往 Lightning Network 的門戶，讓您能以更保密、更快速的方式 Exchange 比特幣。





- 若要這樣做，請按一下「將 On-Chain 資金移至 LIGHTNING」。



在下一個畫面中，您會被要求與**"Olympus by Zeus "**（Wallet 偏好的 LSP（閃電服務供應商））合作開啟一個通道。


在本教程中，為了簡單起見，我們會選擇這個選項，但也完全可以與網路上的任何節點開啟通道。


透過選擇「OPENDITIONAL CHANNEL」，甚至可以在單一交易中開啟多個通道。 *但我們會在 **Zeus Embedded** 教學的「進階」版本中研究這個問題。*





- 然後選擇您希望專用於此頻道的金額。在我們的情況下，我們所有的 On-Chain 資金都會被使用，所以我們啟動「使用所有可能的資金」按鈕。





- 最後，選擇螢幕下方的「開啟頻道」按鈕。



![image](assets/fr/16.webp)





幾秒鐘之內，通道就建立好了，我們就可以進行第一筆 Lightning 交易了。在主螢幕上，我們可以看到 Wallet 結餘旁有一個小鐘。這是因為我們仍需要等待 3 次 On-Chain 確認，通道才能真正運作。



![image](assets/fr/17.webp)





經過 3 次確認後，我們注意到我們的餘額現在已存入 Lightning insert。



![image](assets/fr/18.webp)



一個小細節：當我們點擊螢幕底部的菜單檢視我們的閃電通道狀態時，我們會發現我們的餘額中有一小部分無法使用：我們只能使用 208253 薩托希，而不是實際擁有的 210370 薩托希。這是正常的，因為這是閃電協定特有的情況。



最後，需要注意的是，我們的合作夥伴Olympus保留自行決定關閉頻道的權利，例如在頻道未被使用的情況下。為了確保我們的頻道能維持下去，我們就必須付費給 LSP（Lightning Service Provider，閃電服務供應商），就像我們在下一段會看到的，透過第 2 種方式開啟頻道。





## 透過 Lightning 傳送 bitcoins



現在我們的頻道已經開始運作，讓我們看看如何使用它來支付 Invoice（Invoice）閃電。



若要執行此操作，請按一下「閃電」按鈕，然後按一下「傳送」。



![image](assets/fr/19.webp)





在下一個螢幕，將您的 Invoice 複製到專用欄位，或按一下右上方的圖示掃描。最後，將「滑動付款」按鈕向右滑動即可付款。



![image](assets/fr/20.webp)






再等幾秒鐘，Invoice 已經付清，而您的衛星也已經以光速飛行。



![image](assets/fr/21.webp)





然後，Zeus 可讓您新增一張紙幣以計值您的付款，或檢視您的 Satoshis 在抵達目的地前所經過的路線（以及所有中間節點所徵收的費用）。這正是我們所喜愛的 Wallet 功能。



![image](assets/fr/22.webp)



請注意，與 [Phoenix]([Plan ₿ Network - Phoenix](https://planb.network/fr/tutorials/wallet/mobile/phoenix-0f681345-abff-4bdc-819c-4ae800129cdf))這樣的 Wallet 不同，對於 Zeus，路由是在本地計算的，而不是委託給第三方（在 Phoenix 的情況下是 ACINQ）。所以只有您自己知道付款的收款人。我們失去了一點效率（完成付款需要一點時間，但在隱私方面我們得到了很多）。





按一下主畫面下方的小箭頭，您也可以檢視我們的付款記錄。在這裡，我們看到在 Green 中，On-Chain 收到了 212,121 Sats，然後分別在紅色中看到用於打開我們頻道的 211,756 Sats，然後是用於支付我們 Invoice 閃電的 121,212 薩托希。



![image](assets/fr/23.webp)





## 選項 2 - 直接在 Lightning 上接收比特幣



與其像我們剛剛看到的那樣手動開通一個通道，不如使用 Zeus LSP Olympus，即使沒有預先存在的通道，也可以直接通過 Lightning 接收資金。




- 若要執行此操作，請按一下主畫面上的「Lightning」按鈕，然後按一下「接收」。
- 然後在「金額」方塊中選擇您希望收到的金額，並選擇螢幕下方的「CREATE Invoice」按鈕。



![image](assets/fr/24.webp)





下一個畫面顯示要支付 Invoice 才能收到 Satoshis。我們被告知，如果以 Lightning 付款，LSP 會扣留 10,000 Sats。我們稍後就會知道這些頻道開通費是如何計算出來的。



支付 Invoice 或讓其他人支付，通道會自動打開，但會按照協定扣除 10,000 Sats。



![image](assets/fr/25.webp)





我們現在處於 2 個閃電頻道的首端，可按一下首頁畫面底部白色箭頭指示的按鈕，檢查其狀態。



我們可以看到，與從 On-Chain 標準開啟的通道不同，直接透過閃電開啟的通道不會顯示任何警告。


由於您已付費建立此頻道，LSP（Lightning Service Provider）承諾維護此頻道 3 個月，並提供您「接收流動性」。在底部通道，您可以看到接收容量為 96383 薩托希。因此，LSP 綁定了資金，讓您可以在開啟通道後直接接收付款。



因此，支付的 10,000 Satoshi 費用包括：開啟運河的成本（Bitcoin On-Chain 交易、保證維護運河 3 個月以及資本鎖定）。



![image](assets/fr/26.webp)





恭喜您，現在您已準備好使用 Zeus Embedded，這是擁有市場上最先進功能的 Wallet 行動照明系統。





若要瞭解更多關於 Lightning Network 的技術操作，您可以找到 Fanis Michalakis 優秀的免費 Plan ₿ Network 培訓：



https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb