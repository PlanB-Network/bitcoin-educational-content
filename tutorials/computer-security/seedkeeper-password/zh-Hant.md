---
name: Seedkeeper - 密碼管理器
description: 如何使用 Seedkeeper 智慧卡儲存密碼？
---

![cover](assets/cover.webp)



Seedkeeper 是由 Satochip 開發的智慧卡，Satochip 是一家比利時公司，專門提供管理和保護數位機密的硬體解決方案。Satochip 以其為 Bitcoin 生態系統設計的一系列智慧卡而聞名，Seedkeeper 的構想是取代傳統的記憶短語和其他數位機密的儲存方式。



具體而言，Seedkeeper 採用多功能、經 EAL6 認證的智慧卡形式，具有安全處理器和防篡改記憶體（所謂的「安全元件」）。正如其名所示，它的作用是以加密和受保護的方式儲存 Bitcoin 產品組合的首字母詞彙和密碼。有了 Seedkeeper，您可以直接在卡片的安全元件中儲存 generate、匯入、整理和儲存您的秘密。



在我看來，Seedkeeper 有兩個主要用途，我們將分別在兩個教學中探討：




- Bitcoin** 記憶詞組儲存：您可以將 12 或 24 個詞彙匯入智慧卡中，並以 PIN 碼保護，而不需將它們寫在紙上。
- 密碼管理**：您可以透過 Seedkeeper 應用程式 generate 強密碼，並直接儲存在智慧卡中，讓您擁有方便好用的離線密碼管理器。



技術上來說，Seedkeeper 的容量為 8192 位元組，可儲存至少 50 個獨立的秘密（確實數量取決於秘密的大小以及與每個秘密相關的元資料）。Seedkeeper 可 [透過與電腦連接的智慧卡讀卡器](https://satochip.io/accessories/) 存取，或透過 NFC 連線的行動應用程式存取。整個系統在離線模式下運作，無需網際網路連線，保證了有限的攻擊面。



![Image](assets/fr/001.webp)



一個特別有趣的功能是可以複製一個 Seedkeeper 的內容到另一個 Seedkeeper，以建立備份。在本教程中，我們將教您如何做到這一點。



在本教程中，我們只會介紹如何使用 SeedKeeper 以密碼管理器的方式儲存傳統密碼。如果您想使用 SeedKeeper 來儲存 Bitcoin wallet 助記詞組，請參閱此其他教學：



https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356

## 1.如何取得 Seedkeeper？



有兩種主要方式可以獲得您的 Seedkeeper。您可以 [直接從 Satochip 官方商店購買](https://satochip.io/product/seedkeeper/) 或從授權經銷商處購買。但由於 [Seedkeeper applet 是開放原始碼的](https://github.com/Toporin/Seedkeeper-Applet)，您也可以選擇自行安裝在 [空白的智慧卡](https://satochip.io/product/blank-javacard-for-diy-project/)。



如果您希望使用 Seedkeeper 的備份功能，您顯然需要購買兩張智慧卡。



## 2.安裝 Seedkeeper 用戶端



第一步是在電腦或智慧型手機上安裝軟體。在電腦上，您需要 [下載最新版本的 Satochip-Utils](https://github.com/Toporin/Satochip-Utils/releases)。在手機上，Seedkeeper 應用程式可在 [Google Play 商店](https://play.google.com/store/apps/details?id=org.satochip.seedkeeper) 和 [Apple App 商店](https://apps.apple.com/be/app/seedkeeper/id6502836060) 下載。



![Image](assets/fr/002.webp)



## 3.Seedkeeper 初始化



啟動應用程式，然後按一下「*Click & Scan*」按鈕。



![Image](assets/fr/003.webp)



您會被要求輸入 Seedkeeper 的 PIN 碼。由於這是一張新卡，因此尚未定義 PIN 碼。請輸入任何代碼以跳過此步驟，然後按一下「*下一步*」。



![Image](assets/fr/004.webp)



然後將卡放在智慧型手機背面。應用程式會偵測到 Seedkeeper 尚未初始化，並會提示您設定智慧卡的 PIN 碼，長度在 4 到 16 個字元之間。為了達到最佳的安全性，請選擇一個盡可能長、隨機且由多種字符組成的強大 PIN 碼。此 PIN 碼是防止實體存取密碼的唯一屏障。



**請記住現在**保存此 PIN 碼，例如保存在密碼管理器中，或保存在單獨的實體媒體中。在後者的情況下，切勿將載有 PIN 碼的媒體與 Seedkeeper 放在相同的地方，否則這種安全性將變得毫無用處。有一個可靠的備份非常重要：沒有 PIN，您就無法復原儲存在 Seedkeeper 上的秘密。



![Image](assets/fr/005.webp)



再次確認您的 PIN 碼。



![Image](assets/fr/006.webp)



您的 Seedkeeper 現在已初始化。您可以輸入剛才設定的 PIN 碼來解除鎖定。



![Image](assets/fr/007.webp)



現在您將進入智慧卡管理頁面。



![Image](assets/fr/008.webp)



## 4.在 Seedkeeper 上儲存密碼



當您的 Seedkeeper 解鎖後，按一下「*+*」按鈕。



![Image](assets/fr/009.webp)



選擇「產生密碼*」。*Import a secret*」選項可讓您儲存現有的密碼 (例如，您過去建立的密碼)。



![Image](assets/fr/010.webp)



在我們的案例中，我們要儲存密碼。按一下「*密碼*」。



![Image](assets/fr/011.webp)



為此秘密指定「*標籤*」，以便在 Seedkeeper 中儲存多項資訊時，可以輕易識別。您也可以加入與密碼和網站 URL 相關的識別碼。



![Image](assets/fr/012.webp)



選擇密碼的長度和參數，然後按一下「*產生*」，再按「*匯入*」。



![Image](assets/fr/013.webp)



將 Seedkeeper 放在智慧型手機背面。



![Image](assets/fr/014.webp)



您的密碼已經註冊。



![Image](assets/fr/015.webp)



## 5.存取您的 Seedkeeper 密碼



如果您要檢查密碼，請拿起 Seedkeeper，然後按一下「*Click & Scan*」按鈕。



![Image](assets/fr/016.webp)



輸入 PIN 碼，然後按「*下一步*」。



![Image](assets/fr/017.webp)



將 Seedkeeper 放在智慧型手機背面。



![Image](assets/fr/018.webp)



這會帶您進入所有已註冊密碼的清單。在這個範例中，我想要顯示 Plan ₿ Academy 帳戶的密碼，因此我按一下它。



![Image](assets/fr/019.webp)



按下「*揭示*」按鈕。



![Image](assets/fr/020.webp)



再次掃描您的 Seedkeeper。



![Image](assets/fr/021.webp)



您先前儲存的密碼會出現在螢幕上。您可以複製它並在相關網站上使用。



![Image](assets/fr/022.webp)



## 6.備份 Seedkeeper



我們現在要將我的 Seedkeeper 備份到第二個 Seedkeeper 上，這樣我們就有了兩份副本。這種備援可以是保護您最重要密碼的策略的一部分：例如，將您的 Seedkeeper 分別存放在兩個不同的地點，以限制實體風險，或將一份副本託付給可信賴的親人。



若要執行此步驟，請帶著您的第二個 Seedkeeper（記得在兩個 Seedkeeper 之中的一個做上標記，以免混淆）。依照本教學第 3 步所述，開始初始化它。再次，選擇一個強大的 PIN 碼。根據您的策略，您可以選擇不同的 PIN 碼或保留相同的 PIN 碼。



![Image](assets/fr/023.webp)



開啟應用程式，點選「*Click & Scan*」，輸入 Seedkeeper n°1 (來源) 的 PIN 碼，然後掃描。



![Image](assets/fr/024.webp)



這會帶您進入首頁，並顯示您的秘密清單。按一下介面右上方的三個小圓點。



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



就是這麼多了！現在您知道如何使用 Seedkeeper 儲存密碼了。在未來的教學中，我們將介紹如何使用 Seedkeeper 備份 Bitcoin wallet。我也邀請您發現它與 SeedSigner 的結合使用：



https://planb.academy/tutorials/wallet/hardware/seedkeeper-seedsigner-45cca4c4-1f22-46bb-87ae-9cddb68aa579

https://planb.academy/tutorials/wallet/backup/seedkeeper-906dfff8-1826-4837-92d1-8669e216d356