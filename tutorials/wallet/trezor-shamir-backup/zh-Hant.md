---
name: Trezor Shamir 備份
description: Trezor 上的單股和多股 Mnemonic 詞組
---
![cover](assets/cover.webp)



*圖片來源：[Trezor.io](https://trezor.io/)*



## Trezor 上的新備份選項



自 2023 年起，Trezor 開始提供一種新的備份格式，稱為「***單份備份***」，逐漸取代多數投資組合中以 BIP39 為基礎的經典方式。與傳統的 12 或 24 個字的 Mnemonic 詞組不同，這種新格式基於單一的 20 個字詞組，該詞組來自中本聰技術實驗室 (SatoshiLabs) 開發的標準： **SLIP39**。其目的在於改善備份的穩定性和可讀性，同時使其能順利轉換至分散式備份模式。



這種分散式模式稱為 ***Multi-share Backup***。它以相同的原則為基礎，但不是產生單一的 Mnemonic 詞組，而是將其分割成多個稱為 ***shares*** 的片段，每個片段本身都是一個 Mnemonic 詞組。若要還原組合，必須重新整合一定數量的 *shares*（由 *threshold* 定義）。舉例來說，在 3 對 5 方案中，5 份中的任何 3 份*都能恢復組合。請注意 Trezor 的分散式備份系統與 Multisig 錢包不同。要花費比特幣，只需要您的 Hardware Wallet Trezor。只需要一個簽名。分佈式只適用於 Mnemonic 詞組的層級，即備份。



![Image](assets/fr/01.webp)



此系統解決了 Mnemonic 語句的單點故障問題，卻沒有管理 Multisig 或 passphrase BIP39 的相關缺點。恢復過程不再以單一資訊為基礎，而是以多項資訊為基礎，並因臨界值而增加了損失容忍度的好處。



使用*單一共用備份*建立組合的使用者可隨時切換至*多共用備份*，而無需遷移組合。收件地址和帳戶將保持相同。*Multi-share* 系統只會影響備份，而組合的其他部分則維持不變。



Trezor Model T、Safe 3 和 Safe 5 提供多重共用備份*。Trezor Model One 不支援此功能。



**重要提示：** Trezor 的 *Multi-share* 系統使用 *Shamir's Secret Sharing* 方案進行分發，因此在密碼學上是安全的。我們強烈建議不要手動套用類似的系統，自行分割經典的 Mnemonic 詞組。這是一個不好的做法，會大大增加比特幣被盜和丟失的風險，所以不要這麼做。經典 Mnemonic 詞組會完整地儲存。



## Shamir 在 SLIP39 中的秘密分享



Trezor 上的 *Multi-share* 備份所依據的加密機制是 *Shamir's Secret Sharing Scheme* (SSSS)。其原理如下：密碼資訊（在本例中為投資組合的 seed）被轉換成數學多項式。然後計算這個多項式的幾個點，每個點成為一份。原始的秘密會透過多項式插值，收集最少的點數 (臨界值) 來重建。



任何秘密資訊都無法從低於臨界值的份數中推斷出來，保證了秘密資訊在理論上的完美安全性。換句話說，如果沒有達到臨界值，即使擁有無限計算能力的攻擊者也無法猜出 seed。



SLIP39 使用此方案分配 seed 組合。每個分享是一個 20 個字的句子，由 1024 個字的清單所組成 (與 BIP39 清單不同)。



## 在 Trezor 上設定多重共用備份



在 Trezor 上建立您的投資組合時，您有三種不同的選項：




- 使用 12 或 24 個字的經典 BIP39 Mnemonic 詞組；
- 使用單一共用 Mnemonic 詞組 (SLIP39)；
- 在多重共用 (SLIP39) 中設定多個 Mnemonic 詞組。



如果您選擇單份 SLIP39 Mnemonic 組合，日後便可升級為多份組合，而無需重新設定組合。另一方面，如果您一開始使用的是經典 BIP39 組合（12 或 24 字詞組），則無法直接轉換為多重共用。您必須從頭開始建立一個新的 Multi-share 組合，並通過一個或多個 Bitcoin 交易將您的資金從舊組合轉入新組合。這是一個更複雜、更昂貴的操作。如果您想進行這種轉移，我建議您購買一個新的 Hardware Wallet Trezor，以避免在投資組合軟件上輸入您的 seed。



在本教程中，我們將先瞭解如何在建立投資組合時設定多重股票，然後在接下來的章節中，我們將瞭解如何在現有的投資組合中將單一股票轉換為多重股票。



如果您在裝置的初始設定上需要協助，我們也針對每種 Trezor 機型提供了詳細的教學：



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### 關於新的投資組合



現在您已經完成了 Trezor 的初始配置，可以開始創建組合了。在 Trezor Suite 中，點擊 「*創建新的 Wallet*」按鈕。



![Image](assets/fr/02.webp)



選擇「*多重共用備份*」選項，然後按一下「*建立 Wallet*」。



![Image](assets/fr/03.webp)



接受 Trezor 上的使用條款，並確認建立投資組合。



![Image](assets/fr/04.webp)



在 Trezor Suite 中，按一下「*繼續備份*」。



![Image](assets/fr/05.webp)



仔細閱讀指示，確認後按一下「*建立 Wallet 備份*」。



![Image](assets/fr/06.webp)



如需更多關於儲存和管理 Mnemonic 詞組的正確方法的資訊，我強烈建議您參考這篇教學，尤其是對於初學者而言：



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

在 Trezor 上，選擇您想要設定的總股數。最常見的配置是 2-de-3 和 3-de-5。在本範例中，我將建立 2-de-3 ，因此我將選擇 3 個共享。每個共用將代表一個 20 字的 Mnemonic 詞組。



*對於 Safe 5 使用者，雖然螢幕上會顯示「*點擊繼續*」，但實際上您需要向上滑動才能確認



![Image](assets/fr/07.webp)



然後確認門檻值，即重新存取 Wallet 及其所含比特幣所需的份數。



![Image](assets/fr/08.webp)



Trezor 會使用隨機數字產生器建立您的各種共享（Mnemonic 詞組）。請確保您在操作過程中沒有被監視。將螢幕上提供的字詞寫在您選擇的實體媒體上。請務必保持單字的編號和順序。



我建議您在單獨的媒體上記下每個共用，並小心管理其儲存，以避免在同一個地方存取多個共用。舉例來說，對於像我這樣的 2 對 3 組態，其中一個選擇是將一份存放在家中，另一份存放在值得信賴的朋友家中，最後一份則存放在銀行保險箱中。儲存位置的選擇取決於您的個人安全策略。



您可以在螢幕上方看到目前正在檢視的分享。



當然，您絕對不能在網路上分享這些文字，就像我在本教程中所做的一樣。本範例 Wallet 只會用在 Testnet 上，並會在教學結束時刪除。**_



![Image](assets/fr/09.webp)



若要移至下一個單字，請按一下螢幕底部。您可以向下滑動來倒退。記下所有單字後，請將手指停留在螢幕上，即可進入下一份，重複上述操作。



![Image](assets/fr/10.webp)



在每次分享錄音結束時，您會被要求選擇 Mnemonic 詞組中的單字，以確認您所寫下的單字是否正確。



![Image](assets/fr/11.webp)



就這樣，您已成功使用多重共用選項備份您的投資組合。現在您可以繼續進行其餘的設定指示。



### 現有單一股票組合



如果您已經擁有一個單份備份的 Trezor Wallet（SLIP39 Mnemonic 詞組，而不是經典的 BIP39 詞組），並希望提高 Wallet 備份的可用性和安全性，您可以建立一個多份系統，而無需轉移您的比特幣。



為此，請連接並解鎖您的 Hardware Wallet。在 Trezor Suite 中，移至 Settings（設定）。



![Image](assets/fr/12.webp)



移至「*裝置*」標籤。



![Image](assets/fr/13.webp)



然後按一下「*建立多共用備份*」。



![Image](assets/fr/14.webp)



閱讀說明，然後按一下「*建立多共用備份*」。



![Image](assets/fr/15.webp)



接下來您需要在 Trezor 螢幕上輸入目前的 Mnemonic 詞組 (單股)。選擇字數 (預設為 20)。



![Image](assets/fr/16.webp)



然後使用 Trezor 的螢幕鍵盤輸入目前 Mnemonic 詞組的每個單字。



![Image](assets/fr/17.webp)



然後，您可以按照上一節提供的指示選擇多共用備份的組態。



![Image](assets/fr/18.webp)



建立多重共用備份後，您需要決定如何處理原始的單一共用 Mnemonic 詞組。由於 Bitcoin 組合維持不變，這個單一短語將永遠允許存取。這將取決於您的安全策略，但一般而言，建議銷毀此短語以消除單點故障，這正是多共用備份的目的。如果您決定銷毀它，請確保您安全地銷毀它，因為**它仍然可以存取您的比特幣**。



恭喜您，現在您已經掌握了在 Trezor 硬件錢包上使用單份備份和多份備份的方法。如果您想進一步提升 Wallet 的安全性，請參閱這篇 BIP39 口令教學：



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

如果您認為本教學有用，請在下方留下 Green 拇指。歡迎在您的社交網路分享這篇文章。非常感謝



## 額外資源





- [SLIP-0039: Shamir's Secret-Sharing for Mnemonic Codes](https://github.com/satoshilabs/slips/blob/master/slip-0039.md)；
- [Trezor上的多重分享備份](https://trezor.io/learn/a/multi-share-backup-on-trezor)；
- [Wikipedia: Shamir's secret sharing](https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).