---
name: 復原測試
description: 如何測試您的備份，以確保您不會遺失比特幣？
---
![cover](assets/cover.webp)


當建立 Bitcoin Wallet 時，您會被要求記下一個 Mnemonic 詞組，通常由 12 或 24 個單詞組成。這個短語允許您在承載 Wallet 的設備丟失、損壞或被盜的情況下恢復對比特幣的存取。在您開始使用新的 Bitcoin Wallet 之前，驗證 Mnemonic 詞組的有效性是非常重要的。最好的方法是進行乾式恢復測試。


這個測試是在存入任何比特幣之前模擬 Wallet 恢復。只要 Wallet 是空的，我們就會模擬存放金鑰的裝置遺失的情況，而我們只剩下 Mnemonic 詞組來嘗試復原我們的 bitcoins。


![RECOVERY TEST](assets/notext/01.webp)


## 目的是什麼？


此測試過程可讓您驗證 Mnemonic 短語的實體備份（無論是紙張或金屬）是否正常。如果在此恢復測試中失敗，則表示短語備份出錯，從而使您的比特幣處於風險之中。另一方面，如果測試成功，則證明您的 Mnemonic 短語完全正常運作，您就可以放心使用此 Wallet 來保護比特幣了。


執行乾式回復測試具有雙重優點。它不僅能讓您檢查 Mnemonic 語句的準確性，還能讓您有機會熟悉 Wallet 復原程序。這樣，您就可以在真實情況出現之前發現潛在的困難。在您真正需要恢復 Wallet 的那一天，您的壓力就會減少，因為您已經知道了流程，降低了出錯的風險。這就是為什麼不要忽視這個測試步驟，並花必要的時間正確進行測試的重要性。


## 什麼是恢復測試？


測試過程相當簡單：


- 在建立您的新 Bitcoin Wallet 之後，以及存入您的第一個 Satoshis 之前，請記下見證人資訊，例如 xpub、第一個接收的 Address，甚至是主密鑰指紋；
- 然後，故意刪除仍是空的 Wallet，例如，將您的 Hardware Wallet 重設為出廠設定；
- 接下來，僅使用 Mnemonic 語句和 passphrase 的紙本備份 (如果您使用 passphrase 的話)，模擬復原 Wallet；
- 最後，檢查證人資訊是否與再生的 Wallet 匹配。如果資訊相符，您就可以放心您的實體備份的可靠性，然後您就可以傳送您的第一個 bitcoins 到這個 Wallet。

請注意，在還原測試期間，**您必須使用與最終 Wallet 相同的裝置**，以免增加 Wallet 的攻擊面。例如，如果您在 Trezor Safe 5 上建立 Wallet，請務必在相同的 Trezor Safe 5 上執行復原測試。重要的是，不要在任何其他軟體中輸入您的復原短語，因為這會危及您的 Hardware Wallet 所提供的安全性，即使 Wallet 仍然是空的。


## 如何執行復原測試？


在本教程中，我將說明如何使用 Sparrow Wallet（用於 Hot Wallet）在 Bitcoin Software Wallet 上執行復原測試。但是，對於任何其他類型的裝置，流程都是一樣的。同樣地，**如果您使用的是 Hardware Wallet，請勿在 Sparrow Wallet 上執行復原測試** (請參閱前一節)。


我剛剛在 Sparrow Wallet 上創建了一個新的 Hot Wallet。目前，我還沒有向它發送任何比特幣。它是空的。


![RECOVERY TEST](assets/notext/02.webp)


我在一張紙上仔細地記下了我的 12 個字的 Mnemonic 詞組。由於我想加強這個 Wallet 的安全性，所以我也設定了一個 BIP39 passphrase，並儲存在另一張紙上：


```txt
1. shield
2. brass
3. sentence
4. cube
5. marble
6. glad
7. satoshi
8. door
9. project
10. panic
11. prepare
12. general
```


```text
Passphrase: YfaicGzXH9t5C#g&47Kzbc$JL
```


****很明顯，您絕對不應該在網路上分享您的 Mnemonic 詞組和您的 passphrase，這與我在本教程中所做的不同。這個範例 Wallet 將不會被使用，並會在教學結束時刪除。


我現在會在草稿上記下 Wallet 的目擊者資訊。您可以選擇不同的資訊，例如第一個接收 Address、xpub 或主密鑰指紋。我個人建議選擇第一個接收的 Address。這可讓您驗證是否能找到通往此 Address 的完整第一衍生路徑。


在 Sparrow 上，按一下「*地址*」標籤。


![RECOVERY TEST](assets/notext/03.webp)


然後，在一張紙上記下您的 Wallet 的第一個接收 Address。在我的例子中，Address 是：


```txt
tb1qxv56mma5x5r7uhdkn0ldvcx6m0gj6f3kre0gwd
```


記下資訊後，前往「*檔案*」功能表，然後選擇「*刪除 Wallet*」。我再次提醒您，在進行此操作之前，您的 Bitcoin Wallet 必須是空的。


![RECOVERY TEST](assets/notext/04.webp)


如果您的 Wallet 確實為空，請確認刪除您的 Wallet。


![RECOVERY TEST](assets/notext/05.webp)


現在您需要重複 Wallet 的建立程序，但要使用我們的紙張備份。按一下「*檔案*」功能表，然後按一下「*新增 Wallet*」。


![RECOVERY TEST](assets/notext/06.webp)


再次輸入您 Wallet 的名稱。


![RECOVERY TEST](assets/notext/07.webp)


在「*腳本類型*」功能表中，您需要選擇與之前刪除的 Wallet 相同的腳本類型。


![RECOVERY TEST](assets/notext/08.webp)


然後按一下「*新增或匯入 Software Wallet*」按鈕。


![RECOVERY TEST](assets/notext/09.webp)


為您的 seed 選擇正確的字數。


![RECOVERY TEST](assets/notext/10.webp)


在軟體中輸入您的 Mnemonic 詞組。如果出現 "*Invalid Checksum*" 訊息，表示您的 Mnemonic 詞組備份不正確。由於恢復測試失敗，您必須從頭開始建立 Wallet。


![RECOVERY TEST](assets/notext/11.webp)


如果您有 passphrase，就像我的情況一樣，也請輸入。


![RECOVERY TEST](assets/notext/12.webp)


按一下「*建立金鑰庫*」，然後按一下「*匯入金鑰庫*」。


![RECOVERY TEST](assets/notext/13.webp)


最後，按一下「*應用*」按鈕。


![RECOVERY TEST](assets/notext/14.webp)


現在您可以返回「*地址*」標籤。


![RECOVERY TEST](assets/notext/15.webp)


最後，確認第一個收到的 Address 與您在草稿上註明的見證人相符。


![RECOVERY TEST](assets/notext/16.webp)


如果接收位址相符，表示您的復原測試成功，您可以使用新的 Bitcoin Wallet。如果它們不匹配，這可能表示腳本類型的選擇有誤，導致衍生路徑不正確，或是您的 Mnemonic phrase 或 passphrase 的備份有問題。在這兩種情況下，我強烈建議您從頭開始，重新建立一個新的 Bitcoin Wallet，以避免任何風險。這一次，請注意 Mnemonic 詞組不要出錯。

恭喜您，現在您已經可以進行復原測試了！我建議您在建立所有 Bitcoin 錢包時都採用此流程。如果您覺得這篇教學對您有幫助，請在下方留下拇指讚。歡迎在您的社交網路分享這篇文章。非常感謝您！