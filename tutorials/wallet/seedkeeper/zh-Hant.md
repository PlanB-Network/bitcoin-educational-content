---
name: 種子管理員
description: 如何使用 Seedkeeper 智慧卡備份我的 Wallet Bitcoin？
---

![cover](assets/cover.webp)



Seedkeeper 是由 Satochip 開發的智慧卡，Satochip 是一家比利時公司，專門提供管理和保護數位機密的硬體解決方案。Satochip 以其 Bitcoin 生態系統的智慧卡系列而聞名，並設計 Seedkeeper 作為傳統 Mnemonic 詞組儲存方法的替代方案。



具體而言，Seedkeeper 採用多功能、經 EAL6 認證的智慧卡形式，具有安全處理器和防篡改記憶體（即「secure element*」）。顧名思義，它的作用是以加密和受保護的方式儲存 Bitcoin Mnemonic 短語和密碼。有了 Seedkeeper，您可以直接在卡片的安全元件中 generate、匯入、整理和儲存您的秘密。



在我看來，Seedkeeper 有兩個主要用途，我們將分別在兩個教學中探討：




- Bitcoin** Mnemonic 詞組儲存：您可以將 12 或 24 個詞組匯入智慧卡中，並使用 PIN 碼保護，而無需將詞組寫在紙上。
- 密碼管理**：您可以透過 Seedkeeper 應用程式 generate 強化密碼，並直接將密碼儲存在智慧卡中，讓您擁有方便好用的離線密碼管理器。



技術上來說，Seedkeeper 的容量為 8192 位元組，可儲存至少 50 個獨立的秘密（確實數量取決於秘密的大小以及與每個秘密相關的元資料）。Seedkeeper 可 [透過與電腦連接的智慧卡讀卡器](https://satochip.io/accessories/) 存取，或透過 NFC 連線的行動應用程式存取。整個系統以離線模式運作，無需網際網路連線，保證有限的攻擊面。



![Image](assets/fr/001.webp)



一個特別有趣的功能是可以複製一個 Seedkeeper 的內容到另一個 Seedkeeper，以建立備份。在本教程中，我們將教您如何做到這一點。



Seedkeeper 與 SeedSigner 或 Specter DIY 等無狀態 Hardware Wallet 結合時也非常有趣。在這種情況下，就不需要使用 Satochip 的電腦或行動用戶端。Seedkeeper 會將 seed 保存在其 secure element 中，並可直接與簽章裝置搭配使用，省去紙本 QR code。我不會在本教程中開發這個特殊的使用案例，因為這是另一個專門教程的主題 ：



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

## 1.Seedkeeper 有哪些用例？



在本教程中，我只會處理與 Bitcoin 相關的用例，因為這就是本教程的主題。我們不會討論密碼管理功能，這將是另一個教學的主題。



與 Mnemonic 詞組的簡單紙本備份相比，使用 Seedkeeper 有幾項優點：





- 防盜：** 您 Wallet 中的 seed 無法以明確文字存取。要提取它，您需要知道 Seedkeeper PIN。小偷拿到裝置後，如果沒有這個密碼，就無法使用它做任何事。





- 將風險分散在兩個因素上：** 您可以將安全性分為數位因素和實體因素。例如，如果您將 Seedkeeper PIN 儲存在密碼管理器中，您就需要同時擁有此管理器的存取權和智慧卡的實體持有權，才能取得 seed（攻擊機率大幅降低）。





- 集中管理：** Seedkeeper 方便管理來自不同組合的多個種子。





- 輕鬆備份：** 只需將加密備份複製到其他 SeedKeepers。



但是，與簡單的 seed 紙本備份相比，有許多缺點：





- 價格：** 雖然不高（約 25 歐元），但仍高於一張紙的價格。





- 依賴一般用途的運算裝置：** 輸入和管理 seed 需要電腦或智慧型手機，這表示您的 Mnemonic 所經過的機器比 Hardware Wallet 的攻擊面更廣。如果工作站受到攻擊，這可能代表一種風險。這就是為什麼我不建議使用 Seedkeeper 來儲存 Hardware Wallet 的 seed（除非是無電腦的無狀態使用，如 SeedSigner）。Hardware Wallet 的作用正是在極簡、高度安全的環境中儲存 seed。在您常用的電腦上手動輸入 seed，它就不再局限於 Hardware Wallet：它也會結束在一般用途的機器上，暴露在多種攻擊媒介下。因此，使用 Seedkeeper 的 Hot Wallet 比使用 Cold 的 Wallet 更好 (SeedSigner / 無狀態 Hardware Wallet 除外)。





- 與 PIN 碼相關的遺失風險：** seed 與紙本備份不同，其直接無法存取的特性確實提供了防止實體盜竊的保護。但一如往常，安全性是盜竊風險與遺失風險之間的平衡。如果您的備份需要 PIN 碼，丟失此代碼將無法恢復您的 Mnemonic 短語，從而無法存取您的比特幣。



鑑於這些優缺點，我認為 Seedkeeper 的最佳用途 (除了密碼管理器功能之外)，一方面是儲存您的 ** 軟體投資組合中的種子，因為這些種子已經存在您的手機或電腦中，或是您的無螢幕硬體錢包 (例如 Satochip)，另一方面是與無狀態 Hardware Wallet (例如 SeedSigner)結合使用，這才是它真正發揮作用的地方。



Seedkeeper 另一個特別有趣的用例是可以安全可靠地備份投資組合的 *描述符*。



## 2.如何取得 Seedkeeper？



有兩種主要方式可以獲得您的 Seedkeeper。您可以 [直接從 Satochip 官方商店購買](https://satochip.io/product/seedkeeper/) 或從授權經銷商處購買。但由於 [Seedkeeper applet 是開放原始碼的](https://github.com/Toporin/Seedkeeper-Applet)，您也可以選擇自行安裝在 [空白的智慧卡](https://satochip.io/product/blank-javacard-for-diy-project/)。



如果您希望使用 Seedkeeper 的備份功能，您顯然需要購買兩張智慧卡。



## 3.安裝 Seedkeeper 用戶端



在本教程中，我們將在 Seedkeeper 上備份 seed 投資組合。第一步是在電腦或智慧型手機上安裝軟體。在電腦上，您需要 [下載最新版本的 Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases)。在手機上，Seedkeeper 應用程式可在 [Google Play 商店](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) 以及 [Apple App 商店](https://apps.apple.com/be/app/seedkeeper/id6502836060) 下載。



![Image](assets/fr/002.webp)



## 4.Seedkeeper 初始化



啟動應用程式，然後按一下「*Click & Scan*」按鈕。



![Image](assets/fr/003.webp)



您會被要求輸入 Seedkeeper 的 PIN 碼。由於這是一張新卡，因此尚未定義 PIN 碼。請輸入任何代碼以跳過此步驟，然後按一下「*下一步*」。



![Image](assets/fr/004.webp)



然後將卡放在智慧型手機背面。應用程式會偵測到 Seedkeeper 尚未初始化，並會提示您設定智慧卡的密碼，長度在 4 到 16 個字元之間。為了達到最佳的安全性，請選擇一個盡可能長、隨機且由多種字符組成的強大密碼。此 PIN 碼是防止實體存取您的復原短語的唯一障礙。



**請記住現在**保存此 PIN 碼，例如保存在密碼管理器中，或保存在單獨的實體媒體中。在後者的情況下，切勿將載有 PIN 碼的媒體與 Seedkeeper 放在相同的地方，否則這種安全性將變得毫無用處。有一個可靠的備份非常重要：沒有 PIN，您就無法復原儲存在 Seedkeeper 上的秘密。



![Image](assets/fr/005.webp)



再次確認您的 PIN 碼。



![Image](assets/fr/006.webp)



您的 Seedkeeper 現在已初始化。您可以輸入剛才設定的 PIN 碼來解除鎖定。



![Image](assets/fr/007.webp)



現在您將進入智慧卡管理頁面。



![Image](assets/fr/008.webp)



## 5.在 Seedkeeper 上註冊 seed



當您的 Seedkeeper 解鎖後，按一下「*+*」按鈕。



![Image](assets/fr/009.webp)



選擇「匯入密碼*」。*generate secret*」選項可讓您直接在應用程式中建立新的 Mnemonic 詞組。



![Image](assets/fr/010.webp)



在我們的案例中，我們要將 seed 儲存到我們的組合中。按一下「*Mnemonic*」。



![Image](assets/fr/011.webp)



為此秘密指定「*標籤*」，以便在 Seedkeeper 中儲存多項資訊時，可以輕易識別。



![Image](assets/fr/012.webp)



然後在提供的欄位中輸入您的復原短語。如果您願意，也可以加入 passphrase BIP39 或您的 *描述符*。然後按一下「匯入*」。



![Image](assets/fr/013.webp)



*此圖片中顯示的 Mnemonic 是虛構的，不屬於任何人。它只是一個例子。切勿向任何人透露您自己的 Mnemonic，否則您的比特幣將會被盜。



將 Seedkeeper 放在智慧型手機背面。



![Image](assets/fr/014.webp)



您的 seed 已註冊。



![Image](assets/fr/015.webp)



## 6.在 Seedkeeper 上存取您的 seed



如果您想檢查您的 Mnemonic 詞組，請拿起您的 Seedkeeper，然後按一下「*Click & Scan*」按鈕。



![Image](assets/fr/016.webp)



輸入 PIN 碼，然後按「*下一步*」。



![Image](assets/fr/017.webp)



將 Seedkeeper 放在智慧型手機背面。



![Image](assets/fr/018.webp)



這會帶您進入所有註冊秘密的清單。在這個範例中，我想要顯示我組合中的 seed「*BLOCKSTREAM App*」，因此我點選它。



![Image](assets/fr/019.webp)



按下「*揭示*」按鈕。



![Image](assets/fr/020.webp)



再次掃描您的 Seedkeeper。



![Image](assets/fr/021.webp)



您先前錄製的 Mnemonic 樂句會顯示在螢幕上。



![Image](assets/fr/022.webp)



## 7.備份 Seedkeeper



我們現在要把我的 Seedkeeper 備份到第二個 Seedkeeper 上，這樣就有兩個副本了。這種備援可以是保護您的比特幣策略的一部分：例如，將您的短語存放在兩個不同的地點以限制實體風險，或將副本託付給可信賴的親戚作為繼承計劃的一部分。



若要執行此步驟，請帶著您的第二個 Seedkeeper（記得在兩個 Seedkeeper 之中的一個做上標記，以免混淆）。依照本教學第 4 步所述，開始初始化它。再次選擇一個強大的密碼。根據您的策略，您可以選擇不同的密碼或保留相同的密碼。



![Image](assets/fr/023.webp)



開啟應用程式，按一下「*Click & Scan*」，輸入 Seedkeeper n°1 (來源) 的密碼，然後掃描。



![Image](assets/fr/024.webp)



這會帶您進入首頁，並顯示您的秘密清單。按一下 Interface 右上方的三個小圓點。



![Image](assets/fr/025.webp)



選擇 「*製作備份*」，然後按 「*開始*」。



![Image](assets/fr/026.webp)



輸入備份卡的 PIN 碼 (Seedkeeper n°2)。



![Image](assets/fr/027.webp)



然後掃描卡片。



![Image](assets/fr/028.webp)



對主卡 (Seedkeeper n°1)進行相同操作，然後按一下「*製作備份*」。



![Image](assets/fr/029.webp)



您的 Seedkeeper n°2 現在包含 Seedkeeper n°1 儲存的所有秘密。



![Image](assets/fr/030.webp)



您可以掃描 Seedkeeper n°2 來檢查秘密是否已被複製。



![Image](assets/fr/031.webp)



就是這麼多了！現在您知道如何使用 Seedkeeper 儲存 Bitcoin Wallet 的 Mnemonic 詞組了。在未來的教學中，我們將介紹如何使用 Seedkeeper 來儲存密碼。我也邀請您發現它與 SeedSigner 的結合使用：



https://planb.network/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.network/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

在本教程中，我們已多次提到 Bitcoin 產品組合中的 ***Descriptors*** 。不知道它們是什麼？如果是這樣的話，我建議您參加我們免費的 CYP 201 培訓課程，該課程會深入詳細地介紹操作 HD 投資組合所涉及的所有機制！



https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f