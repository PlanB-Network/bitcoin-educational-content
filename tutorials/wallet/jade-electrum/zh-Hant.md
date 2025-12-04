---
name: 玉 - Electrum
description: 如何在 Electrum (桌上型電腦) 上使用您的 Jade 或 Jade Plus
---

![cover](assets/cover.webp)



_本指南取自 [Bitcoin Workshops 課程](https://officinebitcoin.it/lezioni/jadeele/index.html)_



本教學是使用 Jade Classic 所製作，但其操作也適用於使用 Jade Plus 的使用者。



初始化 Jade 之後，您就可以開始使用它，並選擇 wallet 顯示器。



Jade 是一款可與多個 wallet (或 Blockstream 在其網站上指定的配套應用程式) 搭配使用的裝置。



在本教程中，您將看到透過 USB 纜線連接使用 Electrum Wallet 的步驟。



## 公開金鑰傳輸



取出並打開初始化的 Jade。當您開啟它時，它會像這樣：




![img](assets/en/32.webp)



如果您選擇 _Unlock Jade_，就會出現功能表，您必須在此選擇如何將裝置連線至同伴應用程式。



使用 Electrum，您只能透過 USB 連接 Jade，因此請選擇此方法。



啟動 Electrum，它會開啟建議作為預設選項開啟最後使用的 wallet。



如果這是您第一次將 Jade 連接到 Electrum，請選擇 _Create New Wallet_（建立新錢包），然後選擇 _Finish_（完成）。



![img](assets/en/34.webp)



名稱 wallet.



![img](assets/en/35.webp)



選擇標準 Wallet。



![img](assets/en/36.webp)



選擇keystore時，必須選擇 _使用硬體裝置_。



![img](assets/en/37.webp)



Electrum 開始掃描硬體裝置。



![img](assets/en/38.webp)



將 USB 連接到電腦（USB C 端已連接到 Jade），wallet 硬體就會以鎖定模式出現在您眼前。輸入設定時所設定的六位數 PIN 碼，Jade 即會解鎖。




![img](assets/en/39.webp)



解鎖硬體裝置，Electrum 檢測到 Jade。按下 _Next_ 繼續。



![img](assets/en/40.webp)



此時 Electrum 會要求您設定政策指令碼：選擇 _Native Segwit_。



![img](assets/en/41.webp)



wallet 從 Jade 傳送公開金鑰至顯示 Electrum 的階段開始。



當公開金鑰匯出完成時，程序即告結束。



專用看板準備就緒，Electrum 會以下列畫面提示完成。



![img](assets/en/42.webp)



wallet 已經建立，您可以開始探索它：您可以看到_地址_、_錢包資訊_，最重要的是，您可以在右下角看到它是 Blockstream 裝置的指示。Blockstream 標誌旁的綠點表示裝置已開啟，並正確連線至本端網路。



![img](assets/en/43.webp)



## 收支交易



從 Electrum 的 _Receive_ 功能表，generate 一個 `scriptPubKey` (位址) 來接收資金。一開始一定要從小數額開始，並進行接收+支出測試。



![img](assets/en/44.webp)



收到薩斯後，您可以在 _History_ 功能表中檢查它們是否到達。



![img](assets/en/45.webp)



![img](assets/en/46.webp)



交易確認後，您就可以花費這筆 UTXO 並完成測試。



費用涉及使用 Jade 來簽名。



到 Electrum 的 _Send_ 功能表，貼上 scriptPubKey 並確認好。



![img](assets/en/47.webp)



完成後，按下 _Pay_。



交易視窗開啟，在此必須設定正確的交易費用。完成所有設定後，按一下右下角的 _Preview_。



![img](assets/en/48.webp)



交易視窗會顯示一些重要的詳細資訊，首先是狀態：未簽署」。



在此階段，您也可以看到 _Sign_ 指令，您必須按一下此指令才能貼上 Jade 的簽名。



![img](assets/en/49.webp)



現在開始顯示器 wallet 與硬體裝置之間的通訊階段，Electrum 會提醒您遵循硬體裝置上的指示，開啟並準備簽署。



![img](assets/en/50.webp)



**首先，您最好驗證一下您要簽署的內容：您剛才設定的所有交易參數，也會出現在 Jade** 上，您可以全部驗證。



![img](assets/en/51.webp)



若要繼續操作，請確定您永遠將游標放在通往下一個步驟的 `→` 箭頭上，而不要放在 `X` 上，除非您想在未完成操作的情況下結束操作。



驗證部分以費用顯示結束。此時的確認等同於簽名。



![img](assets/en/52.webp)



在短暫的時間內，Jade 會處理此操作，完成後會返回主功能表。



![img](assets/en/53.webp)



在 Electrum 上，您可以看到交易的狀態，已從 `未簽名 ` 變成 `已簽名 `，現在您可以按一下 _Broadcast_ 來傳播它。



![img](assets/en/54.webp)



經測試的 wallet 可用於接收擬安全儲存的 UTXO。



![img](assets/en/55.webp)



本指南是如何使用您的 Jade，透過 USB 連接到 wallet 純手錶的範例。Electrum 是一個經典的範例，但您也許會喜歡其他 wallet 軟體。Jade 將公開金鑰匯出到許多其他的錢包：找到您在本教學中讀到的類似功能，來引導您，並找到如何運用它您最喜歡的 companio 應用程式。