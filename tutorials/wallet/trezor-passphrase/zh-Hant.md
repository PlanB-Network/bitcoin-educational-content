---
name: passphrase BIP39 Trezor
description: 如何將 passphrase 加入我的 Trezor 產品組合？
---
![cover](assets/cover.webp)



passphrase BIP39 是一個可選的密碼，結合 Mnemonic 短語，可為確定型和分層型 Bitcoin 組合提供額外的 Layer 安全性。在本教程中，我們將一併探索如何在 Trezor（Safe 3、Safe 5 和 Model One）上的安全 Bitcoin Wallet 上設定 passphrase。



![Image](assets/fr/01.webp)



在開始本教學之前，如果您不熟悉 passphrase 的概念、它的工作原理以及它對您的 Bitcoin Wallet 的影響，我強烈建議您參考我解釋一切的這篇其他理論文章（這非常重要，因為在不完全瞭解 passphrase 工作原理的情況下使用它會讓您的比特幣面臨風險）：



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

如果您在配置過程中選擇了 BIP39 標準，Trezor 上的 passphrase 會以經典方式處理（如果您不需要 * 多重共用備份*，我建議使用這種方式）。Trezor 的特別之處在於您可以直接在 Hardware Wallet 上輸入 passphrase，或是使用 Trezor Suite 軟體透過電腦鍵盤輸入。第二種方式的安全性較低，因為電腦的攻擊面遠大於 Hardware Wallet。然而，在傳統鍵盤上輸入複雜的 passphrase 可能比在 Hardware Wallet 上輸入更快，這可能會鼓勵使用強大的密碼。因此，使用 passphrase（即使必須鍵入）總比不使用 passphrase 好。不過，重要的是，仍要注意這意味著數字攻擊的風險會增加。



並非所有與 Trezor 相容的組合管理軟體都提供這些選項。例如，對於 Model One，可以通過 Sparrow Wallet 上的鍵盤輸入 passphrase。對於 Model T、Safe 3 和 Safe 5 型號，您必須使用 Trezor Suite 或直接在 Hardware Wallet 上輸入 passphrase，因為通過 Sparrow 輸入的選項幾年前已被 HWI 禁用。



![Image](assets/fr/02.webp)



在 Trezor Suite 中，您有兩種不同的方式來管理 passphrase 的需求。您可以在 「*設備*」標籤中啟用 "*passphrase*"選項。如果啟用，Trezor Suite 和所有其他組合管理軟體在每次啟動時都會系統地要求您輸入 passphrase。如果您喜歡更隱蔽地使用 passphrase，可以將設定保持為 「*標準*」。在這種情況下，您需要手動進入 Hardware Wallet 左上角的功能表，每次啟動時按一下「*+ passphrase*」按鈕。



在開始本教學之前，請確保您已經初始化了 Trezor 並生成了 Mnemonic 短語。如果您還沒有，而且您的 Trezor 是新的，請按照 Plan ₿ Network 上的特定型號教程進行。完成此步驟後，您可以返回本教程。



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02


## 在 Safe 3 或 Safe 5 中加入 passphrase



當您建立 Wallet、儲存 Mnemonic 並設定 PIN 碼後，您將會進入 Trezor Suite 首頁選單。在左上角會出現一個視窗，邀請您啟動 passphrase BIP39。



![Image](assets/fr/03.webp)



如果此視窗沒有出現，您需要在「*裝置*」設定標籤中手動啟動「*passphrase*」選項。



![Image](assets/fr/04.webp)



此視窗會要求您輸入 passphrase。選擇一個強大的 passphrase，並立即進行實體備份，備份在紙張或金屬等媒介上。在這個範例中，我選擇了 passphrase：`fH3&kL@9mP#2sD5qR!82`.這是一個範例；但是，我建議您選擇稍長的 passphrase。30 到 40 個字元之間會比較理想 (就像一個好的密碼)。



當然，您絕對不應該在網際網路上分享您的 passphrase，就像我在本教程中所做的一樣。此範例 Wallet 只會在 Testnet 上使用，並會在教學結束時刪除。**_



如需更多關於選擇 passphrase 的具體建議，我再次邀請您參閱這篇文章：



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

如果您要透過電腦鍵盤輸入您的 passphrase，請在提供的欄位中輸入，然後按一下「*存取 passphrase Wallet*」。



![Image](assets/fr/05.webp)



然後，您的 Hardware Wallet 將會顯示您的 passphrase。請確定它與您的實體備份（紙張或金屬）相符，然後在螢幕上按一下繼續。



![Image](assets/fr/06.webp)



這樣您就可以存取受 passphrase 保護的投資組合。



![Image](assets/fr/07.webp)



如果您希望只在 Trezor 上輸入 passphrase，以加強安全性，請在出現提示時按一下「*在 Trezor 上輸入 passphrase*」。



![Image](assets/fr/08.webp)



Trezor 上會出現 T9 鍵盤，讓您輸入 passphrase。完成輸入後，點選 Green 剔號，即可將 passphrase 套用至您的 Wallet。



![Image](assets/fr/09.webp)



然後您就可以存取您的 passphrase 安全 Wallet。



![Image](assets/fr/10.webp)



若要使用 Sparrow Wallet，程序類似，但對於 T、Safe 3 和 Safe 5 型號，必須在 Hardware Wallet 上輸入 passphrase，而非透過電腦鍵盤。



每當麻雀 Wallet 需要存取您的 Trezor，而 passphrase 自上次啟動後尚未套用時，您就需要使用 T9 鍵盤輸入。



![Image](assets/fr/11.webp)



## 將 passphrase 加到 Model One 上



在 Model One 上，使用 passphrase BIP39 幾乎是不可或缺的。由於此裝置沒有整合安全元件，因此較容易擷取敏感資訊。因此它無法抵抗實體攻擊。不過，由於 passphrase 在裝置關機後就不會保留在裝置上，因此使用強韌 (不可韌化) 的 passphrase 可以保護您在此機型上抵禦大部分已知的物理攻擊。



在 Model One 上，無法直接在 Hardware Wallet 上輸入 passphrase。您需要透過電腦鍵盤輸入。



當您建立 Wallet、儲存 Mnemonic 並設定 PIN 碼後，您將會進入 Trezor Suite 首頁選單。在左上角應該會出現一個視窗，邀請您啟動 passphrase BIP39。



![Image](assets/fr/12.webp)



如果此視窗沒有出現，您需要在設定的 「*裝置*」標籤中啟動 "*passphrase*"選項。



![Image](assets/fr/13.webp)



此視窗會要求您輸入 passphrase。選擇一個強大的 passphrase，並立即進行實體備份，備份在紙張或金屬等媒介上。在這個範例中，我選擇了 passphrase：`fH3&kL@9mP#2sD5qR!82`。這只是一個範例；然而，我建議您選擇稍長的 passphrase。30 到 40 個字元之間會比較理想 (就像一個好的密碼)。



如需更多關於選擇 passphrase 的具體建議，我再次邀請您參閱這篇文章：



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

在提供的欄位中輸入您的 passphrase，然後按一下「*存取 passphrase Wallet*」按鈕。



![Image](assets/fr/14.webp)



您的 Hardware Wallet 將顯示您的 passphrase。確定它與您的實體備份（紙張或金屬）相符，然後按一下右邊的按鈕，繼續。



![Image](assets/fr/15.webp)



這將帶您進入 passphrase 保護的投資組合。



![Image](assets/fr/16.webp)



之後使用 Sparrow Wallet，步驟仍然相同。每次 Sparrow 需要存取您的 Hardware Wallet，且 passphrase 自裝置上次啟動後尚未輸入時，您都需要輸入。



![Image](assets/fr/17.webp)



恭喜您，現在您已經能夠在 Trezor 硬件錢包上使用 passphrase BIP39 了。如果您想讓 Wallet 的安全性更進一步，請查看本教學，了解 Trezor 的 *Multi-share* 備份系統 (*Shamir's Secret Sharing Scheme*)：



https://planb.network/tutorials/wallet/backup/trezor-shamir-backup-7f98b593-face-48fb-a643-0e811b87c94e

如果您認為本教學有用，請在下方留下 Green 拇指。歡迎在您的社交網路分享這篇文章。非常感謝