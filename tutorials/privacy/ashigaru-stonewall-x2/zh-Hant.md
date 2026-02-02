---
name: Ashigaru - Stonewall x2
description: 在 Ashigaru 上瞭解和使用石牆 x2 交易
---
![cover stonewall x2](assets/cover.webp)



> *讓每次花費都是硬幣匯入

## 什麼是石牆 x2 交易？



石牆 x2 是一種特殊形式的 Bitcoin 交易，旨在透過與不參與支出的第三方合作，增加使用者消費時的機密性。此方法模擬兩個參與者之間的迷你 Coinjoin，同時向第三方付款。石牆 x2 交易可在 Ashigaru 應用程式上使用，這是 Samourai Wallet 的 fork（這種交易類型的創造團隊）。



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

其運作方式相對簡單：您使用自己擁有的 UTXO 進行付款，並尋求第三方的協助，第三方也會使用自己的 UTXO 付款。交易最後會有四個輸出：兩個是等額的，一個是收款人的地址，另一個是屬於合作者的地址。第三個 UTXO 返回到屬於合作者的另一個地址，讓他可以收回初始金額（對他來說是中性行為，模擬 mining 成本），最後一個 UTXO 返回到屬於我們的地址，這構成了付款交換。



石牆 x2 交易中因此定義了三種不同的角色：




- 實際付款的發行人 ；
- 合作者，提供比特幣以提高交易的匿名性，同時在交易結束時全額收回其資金（對他而言是中性行為，模擬 mining 成本）；
- 收件人可能不知道交易的具體性質，只是期望從寄件人處付款。



讓我們舉個例子。Alice 去面包店买她的法棍，价格是`4,000 sats`。她想用比特币支付，同时对她的付款保留一定的保密性。所以她打電話給她的朋友 Bob，Bob 會幫她完成這件事。



![image](assets/fr/01.webp)



分析這筆交易，我們可以看到麵包師傅實際收到`4,000 sats`的長棍付款。Alice 在投入中使用了 `10,000 sats`，在产出中收回了`6,000 sats`，淨結餘為`-4,000 sats`，與長棍的價格相符。至於Bob，它提供了`15,000 sats`的投入，並收到兩筆產出：一筆是`4,000 sats`，另一筆是`11,000 sats`，結餘為`0`。



在這個範例中，我刻意忽略了 mining 的費用，使其更容易理解。實際上，交易費用是由付款發行商和合作夥伴平分的。



## 石牆和石牆 x2 有什麼不同？



StonewallX2 交易的工作方式與 Stonewall 交易完全相同，只是前者是合作式的，而後者不是。正如我們所看到的，Stonewall X2 交易涉及第三方的參與，該第三方在支付之外，並將提供自己的比特幣以加強交易的保密性。在典型的石牆交易中，合作者的角色由發送者擔當。



讓我們回到 Alice 在麵包店的例子。如果她找不到像 Bob 這樣的人陪她一起瘋狂消費，她可以自己做一個石牆。這樣一來，進去時的兩個 UTXO 就會是她的了，而出來時她也會撿到三個。



![image](assets/fr/02.webp)




從局外人的角度來看，交易仍會維持原樣。



![image](assets/fr/05.webp)



因此，當您想要使用 Ashigaru 支出工具時，邏輯應該如下：




- 如果商家不支持 Payjoin Stowaway，您可以與其他人在支付之外進行協作交易，感謝石牆 x2 ；
- 如果您找不到人進行石牆 x2 交易，您可以只進行石牆交易，這會模仿石牆 x2 交易的行為。



https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-033daa45-d42c-40e1-9511-cea89751c3d4

## 石牆 x2 交易的意義何在？



石牆 x2 結構為交易增加了大量的熵，混淆了鏈式分析。從外觀來看，這樣的交易可能會被解釋為兩個人之間的一個小 Coinjoin。但實際上，這是一筆付款。因此，這種方法會造成連鎖分析的不確定性，甚至導致錯誤的線索。



讓我們以 Alice、Bob 和 Boulanger 為例。區塊鏈上的交易會是這樣的：



![image](assets/fr/03.webp)



外部觀察者依賴一般的鏈分析啟發法，可能會錯誤地得出「*Alice 和 Bob 做了一個小的合併，各有一個 UTXO 輸入，各有兩個 UTXO 輸出*」的結論。



![image](assets/fr/04.webp)



這個解釋是不正確的，因為如您所知，有一台 UTXO 被送到 Boulanger，Alice 只有一個交換輸出，而 Bob 則有兩個。



![image](assets/fr/01.webp)



即使外部觀察者能夠找出 Stonewall X2 交易的付款人，他也無法掌握所有資訊。他無法確定兩筆相同金額的UTXO中，哪一筆與該筆款項相對應。他也無法確定是 Alice 還是 Bob 支付了這筆款項。最後，他也無法確定輸入的兩個 UTXO 是否來自兩個不同的人，或是屬於一個人，而這個人合併了這兩個 UTXO。最後這一點是由於上面所討論的經典石牆交易，與石牆 x2 交易遵循完全相同的 paterne。從外觀來看，如果沒有額外的上下文資訊，就不可能區分石牆交易和石牆 x2 交易。前者不是合作交易，而後者則是。這更增加了支出的疑點。



![image](assets/fr/05.webp)




## 如何在 Paynyms 之間建立連接？



如同 Ashigaru 上的其他合作交易 (*Cahoots*)，石牆 x2 涉及傳送者與合作者之間部分簽章交易的交換。這種交換可以手動進行 (如果您與合作者親自在一起)，或使用 Soroban 通訊協定自動進行。



如果您選擇第二個選項，您需要在執行石牆 x2 之前建立 Paynym 之間的連線。要做到這一點，您的Paynym必須 "*follow*"您合作者的Paynym，反之亦然。要瞭解如何做到這一點，您可以按照此其他教程的開頭：



https://planb.academy/tutorials/privacy/on-chain/paynym-bip47-a492a70b-50eb-4f95-a766-bae2c5535093

## 如何在 Ashigaru 上進行石牆 x2 交易？



要進行Stonewall x2交易，點擊屏幕左上角您的Paynym圖像，然後打開 "Collaborate "菜單。與您一起參與交易的人也必須這樣做，除非你們是當面交換 QR 代碼。



![Image](assets/fr/06.webp)



您有兩個選項：如果您是付款的寄件人，請選擇「啟動」；如果您是交易的合作者，但既非付款人也非實際收款人，請選擇「參與」。



![Image](assets/fr/07.webp)



如果您有合作者的角色，程序非常簡單。若要透過 Soroban 網路進行遠端協作，請點選「參與」，選擇您要使用的帳號，然後按下「等待 CAHOOTS 請求」，等待付款人傳送的請求。



![Image](assets/fr/08.webp)



另一方面，若要透過 QR 碼掃描進行當面協作，請前往 wallet 的首頁，按下螢幕上方的 QR 碼圖示，然後掃描啟動交易的付款人所提供的 QR 碼。



![Image](assets/fr/09.webp)



如果您是付款人角色，也就是啟動交易的人，請前往「協作」功能表，然後選擇「啟動」。



![Image](assets/fr/10.webp)



對於交易類型，由於我們希望執行 Stonewall X2，請選擇此選項。



![Image](assets/fr/11.webp)



然後，您可以選擇線上協作 (*Cahoots* 透過 *Soroban*) 或面對面協作 (使用 QR 代碼交換)。



![Image](assets/fr/12.webp)



### 線上 Cahoots



如果您選擇了「線上」選項，則從您關注的 Paynyms 中選擇您的合作者。



![Image](assets/fr/13.webp)



按一下「設定交易」，然後選擇您要支出的帳戶。



![Image](assets/fr/14.webp)



在下一頁，輸入交易詳細資料：付款實際收款人的地址、要傳送的金額和費率。然後按一下「檢視交易設定」。



![Image](assets/fr/15.webp)



仔細檢查資料，確定您的合作夥伴正在聆聽 *Cahoots* 請求，然後按一下綠色的 `BEGIN TRANSACTION` 按鈕，開始透過 Soroban 交換 PSBT。



![Image](assets/fr/16.webp)



等到兩個參與者都簽署交易後，再在 Bitcoin 網路上廣播。



![Image](assets/fr/17.webp)



### 面對面討論



如果您希望親自進行兌換，請選擇「STONEWALL X2」交易類型，然後選擇「親自/手動」選項。



![Image](assets/fr/18.webp)



按一下「設定交易」，然後選擇您要支出的帳戶。



![Image](assets/fr/19.webp)



在下一頁，輸入交易詳細資料：付款實際收款人的地址、要傳送的金額和費率。然後按一下「檢視交易設定」。



![Image](assets/fr/20.webp)



檢查詳細資料，然後按下綠色的「BEGIN TRANSACTION」按鈕，開始透過 QR 掃描交換 PSBT。



![Image](assets/fr/21.webp)



交換方式是與合作者交替掃描：按一下 `SHOW QR CODE` 顯示您的 QR 代碼給您的合作者，由他掃描。然後他會按一下 `SHOW QR CODE` 顯示他的 QR 代碼，您則使用 `LAUNCH QR Scanner` 掃描。重複這個過程，直到完成所有五個交換步驟為止。



![Image](assets/fr/22.webp)



完成所有交換後，檢查交易詳細資料，然後拖動螢幕底部的綠色箭頭即可解除。



![Image](assets/fr/23.webp)



[The transaction has been published](https://mempool.space/testnet4/tx/9082f3d989728aacd290535a1ac374ab8c04a241a1d798b378db626dabea7a24).其結構如下：



![Image](assets/fr/24.webp)



*信用：[mempool.space](https://mempool.space/)*



我們可以觀察到兩個輸入來自我的投資組合，分別是 `91,869 sats` 和 `64,823 sats`，而另外兩個輸入則來自我合作者的 wallet。在輸出方面，一個UTXO的`100,000 sats`被發送給實際收款人，兩個UTXO的`100,000 sats`和`159,578 sats`返回到我合作者的投資組合。對他來說，這個操作是中性的，因為他收回了投入的全部資金（不包括他投入的 mining 成本）。最後，我收到了 `56,270 sats` 的交換 UTXO，相應於我的總投入和發送給收件人的付款 `100,000 sats` 之間的差額。



很明顯，我可以描述這個結構，因為我自己建立了這個交易。但對於外部觀察者來說，無論是輸入或輸出，一般都無法確定哪些 UTXO 屬於哪些參與者。



為了加深您對 Bitcoin 上鏈隱私管理的認識，我建議您參加我在 Plan ₿ Academy 上的 BTC 204 培訓：



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c