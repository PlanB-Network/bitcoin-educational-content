---
name: BIP-39 密鑰 SeedSigner
description: 如何將 passphrase 加入我的 SeedSigner 投資組合？
---

![cover](assets/cover.webp)



passphrase BIP39 是一個可選的密碼，它與助記詞組合起來，為確定性和分層的 Bitcoin 電子錢包提供了額外的安全層。在本教程中，我們將一併探索如何在與 SeedSigner 一起使用的 Bitcoin wallet 上設定 passphrase。



![Image](assets/fr/01.webp)



## 新增密碼前的先決條件



在開始本教學之前，如果您不熟悉 passphrase 的概念、它的工作原理以及它對您的 Bitcoin wallet 的影響，我強烈建議您參閱這篇其他的理論文章，在這篇文章中我解釋了一切（這是非常重要的，因為在沒有完全理解它的工作原理的情況下使用 passphrase 會使您的比特幣處於風險之中）：



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

在開始本教學之前，請確認您已經初始化您的 SeedSigner 並產生您的助記語句。如果您還沒有，而且您的 SeedSigner 是全新的，請遵循 Plan ₿ Academy 上的教學。完成這一步驟後，您就可以回到本教學：



https://planb.academy/tutorials/wallet/hardware/seedsigner-2b274bff-6fc8-407a-92d7-f6ec4d1fadfb

## 如何將 passphrase 加入 SeedSigner？



將 passphrase 加入您透過 SeedSigner 管理的投資組合，會建立一個全新的投資組合，產生一組完全獨立的金鑰。因此，如果您已經有一個包含 satss 的組合，您將無法再使用 passphrase 來存取它，因為它會產生一個完全不同的組合。



若要在 SeedSigner 上套用 passphrase，請開啟裝置並如往常一樣掃描您的 SeedQR。SeedSigner 將會顯示您目前 wallet 的指紋，對應於**沒有 passphrase 的指紋。有 passphrase 的 wallet 將會有不同的指紋。



按一下「BIP-39 密碼」按鈕。



![Image](assets/fr/02.webp)



然後在提供的欄位中使用螢幕鍵盤輸入您選擇的 passphrase。請務必做一個或多個實體備份（紙張或金屬）：遺失 passphrase 將導致您永久無法存取您的比特幣。 **要還原 wallet，助記符和 passphrase 都是必不可少的 ** 如果其中一個丟失，您的比特幣將會被永久封鎖。



完成輸入後，按下 SeedSigner 右下方的 `KEY3` 按鈕進行驗證。



![Image](assets/fr/03.webp)



*在這個範例中，我使用 passphrase `pba`。不過，就您的情況而言，請確定您選擇了穩健的 passphrase。若要瞭解如何定義最佳的 passphrase，請參閱這篇文章： *



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

SeedSigner 會顯示 passphrase wallet 的新指紋。將這個指紋複製幾份：在使用 passphrase 與 wallet 時，這是很重要的，因為它可以讓您在每次輸入 passphrase 時檢查您是否有任何輸入錯誤，以及您是否存取正確的 wallet。



舉例來說，如果我在啟動 SeedSigner 時，錯誤地寫下 passphrase `Pba` 而不是 `pba`，這個簡單的從小寫到大寫的改變，將會導致建立一個與我想要存取的組合完全不同的組合。



此指紋不會對您 wallet 的安全性或機密性造成任何風險。它不會洩露任何關於您鑰匙的公開或隱私資訊。因此，與記憶體和 passphrase 不同，您可以將指紋保存在數位媒體上。我建議您在幾個地方保存一份副本：在一張紙上、在密碼管理器中，等等。



儲存您的指紋後，按一下`完成`。



![Image](assets/fr/04.webp)



然後，您就可以使用您的投資組合的所有功能，就像在經典的 SeedSigner 上一樣。



![Image](assets/fr/05.webp)



現在您可以將 keystore 匯入 Sparrow Wallet 並正常使用您的 wallet。每次重新啟動時，您都需要掃描您的 SeedQR，並使用鍵盤重新輸入您的 passphrase，就像我們在這裡所做的一樣。



在您實際使用您的 wallet 與 passphrase 之前，我強烈建議您執行一次完整的空復原測試。這將允許您確認您的助記語句和 passphrase 的備份是有效的。要瞭解如何執行此檢查，請參閱以下教學：



https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895