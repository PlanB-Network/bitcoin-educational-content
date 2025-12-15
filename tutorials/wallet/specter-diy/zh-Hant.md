---
name: Specter DIY
description: Specter DIY 設定指南
---

![cover](assets/cover.webp)


## Specter-DIY


> Cypherpunks 寫程式碼。我們知道必須有人寫軟體來捍衛隱私，既然除非大家都寫，否則我們無法獲得隱私，所以我們要寫。

*Cypherpunk 的宣言 - Eric Hughes - 1993 年 3 月 9 日*


該專案的構想是利用現成的元件建立硬體 wallet。

儘管我們有一個擴充板，可以將所有東西都放在一個很好的外形中，並幫助您避免任何焊接，但我們仍會繼續支援並維持與標準元件的相容性。


![image](assets/fr/01.webp)


我們也希望保持專案的彈性，讓它可以在任何其他元件上運作，只需最小的變更。也許您想要在不同的架構（RISC-V？）上製作硬體 wallet，並使用音訊調製解調器作為通訊管道 - 您應該可以做到。增加或變更 Specter 的功能應該很容易，我們盡可能抽象邏輯模組。


QR 碼是 Specter 與主機通訊的預設方式。QR 碼是相當方便的，而且可以讓使用者控制資料傳輸 - 每個 QR 碼的容量都非常有限，而且通訊是單向發生的。而且它是 airgapped - 任何時候都不需要將 wallet 連接到電腦。


對於秘密儲存，我們支援不可知模式 (wallet 關閉時會忘記所有秘密)、不計較模式 (將秘密儲存於應用程式微控制器的快閃記憶體中)，secure element 整合也即將推出。


我們的主要重點是與其他硬體錢包的多重簽章設定，但 wallet 也可作為單一簽章器使用。我們盡可能讓它與 Bitcoin Core 相容 - PSBT 用於無簽章交易，wallet 描述符用於匯入/匯出多重簽章錢包。為了更容易與 Bitcoin Core 溝通，我們也正在開發 [Specter Desktop app](https://github.com/cryptoadvance/specter-desktop) - 一個與 Bitcoin Core 節點對話的小型 python flask 伺服器。


大部分的韌體都是以 MicroPython 寫成，這使得程式碼很容易審核與變更。我們使用 Bitcoin Core 的 [secp256k1](https://github.com/bitcoin-core/secp256k1) 函式庫進行橢圓曲線計算，並使用 [LittlevGL](https://lvgl.io/) 函式庫進行 GUI。


## 免責聲明


本專案已相當成熟，Specter-DIY 的安全層級已可媲美市面上的商用硬體錢包。我們實作了一個安全的開機載入程式，可以驗證韌體升級，因此您可以確定在初始設定之後，只有經過簽章的韌體才能上傳到裝置。然而，與商業簽章裝置不同的是，開機載入程式必須由使用者手動安裝，而非在裝置供應商的工廠中設定。因此，在初始韌體安裝時請格外注意，確保您已驗證 PGP 簽署，並從安全的電腦上快閃韌體。


如果有什麼問題無法解決，請在此開啟問題，或在我們的 [Telegram 群組](https://t.me/+VEinVSYkW5TUl5Ai) 中提出問題。


## Specter-DIY 購物清單


在此我們會說明需要購買的產品，而在組裝的下一部分，我們會說明如何將它組裝起來，以及一些關於電路板的注意事項 - 電源跳線、USB 連接埠等。


### 探索板


裝置的主要部分為開發板：



- STM32F469I-DISCO 開發板 (即來自 [Mouser](https://eu.mouser.com/ProductDetail/STMicroelectronics/STM32F469I-DISCO?qs=kWQV1gtkNndotCjy2DKZ4w==) 或 [Digikey](https://www.digikey.com/product-detail/en/stmicroelectronics/STM32F469I-DISCO/497-15990-ND/5428811))
- 迷你**USB 纜線
- 透過 USB 進行通訊的標準 MicroUSB 纜線


可選擇但建議使用：


- [Waveshare QR code scanner](https://www.waveshare.com/barcode-scanner-module.htm) 搭配 [these](https://eu.mouser.com/ProductDetail/Samtec/DW-02-10-T-S-571?qs=sGAEpiMZZMvlX3nhDDO4AE5PKXAQeC6NPk%2FcLBS9yKI%3D) 或 [these](https://www.amazon.com/gp/product/B015KA0RRU/) 之類的長針腳接頭，將掃描器連接至電路板 (需要 4 針腳接頭)。


我們目前正在製作一個擴充板，其中包括智慧卡插槽、QR 碼掃描器、電池和 3d 列印外殼，但不包括主要部分 - 您需要另外訂購的 discovery 板。這樣供應鏈攻擊仍然不是問題，因為安全關鍵元件是從隨意的電子商店購買的。


即使沒有任何額外的元件，您也可以開始使用 Specter，但您可以透過 USB 或內建的 SD 卡插槽與 Specter 進行通訊。透過 USB 使用 Specter 意味著它沒有對空連結，因此您會失去一個重要的安全特性。


### QR 掃描器


對於 QR 代碼掃描器，您有多種選擇。


**選項 1.推薦**來自 Waveshare 的相當不錯的掃描器 (40$)


[Waveshare掃描器](https://www.waveshare.com/barcode-scanner-module.htm) - 您需要想辦法把它安裝好，或許可以使用某種 Arduino Prototype 擋板和一些鴨嘴膠。


不需要焊接，但如果您有焊接技巧，您可以讓 wallet 變得更漂亮;)


**Option 2.** Mikroe 非常好的掃描器，但相當昂貴（150 美元）：


[Barcode Click](https://www.mikroe.com/barcode-click) + [Adapter](https://www.mikroe.com/arduino-uno-click-shield)


**選項 3.** 任何其他 QR 掃描器


您可以在中國找到一些便宜的掃描器。它們的品質通常不是很好，但您可以冒險一試。也許 ESPcamera 也可以完成工作。您只需要連接電源、UART（引腳 D0 和 D1）和觸發器到 D5。


**選項 4.** 無掃瞄器。


那麼您只能使用 USB / SD 卡來使用 Specter。


除非您建立自己的通訊模組，使用其他東西來取代 QR 碼 - 音訊數據機、藍牙或其他任何東西。只要能觸發並透過序列傳送資料，您就可以為所欲為。


### 選購組件


如果您加上一個小小的電力儲存器或電池與電力充電器/增壓器，您的 wallet 就可以完全獨立運作了;)



## 組裝 Specter-DIY



![video](https://youtu.be/1H7FqG_FmCw)


### 連接 Waveshare 條碼掃描器


wallet 韌體會在第一次執行時為您設定掃瞄器，因此不需要手動預先設定。


以下是將 scanner 連接到電路板的方法：


![image](assets/fr/02.webp)


為了方便起見，您可以購買 Arduino Protype 保護罩，然後將所有東西焊接並安裝在上面 (例如 [這個](https://www.digikey.com/catalog/en/partgroup/proto-shield-rev3-uno-size/79347))


### 電源管理


在電路板的頂端有一個跳線，用來定義電源的位置。您可以改變跳線的位置，將電源選擇為其中一個 USB 埠或 VIN 引腳，並在此連接外部電池 (應為 5V)。


### 適用於 DIY 的外殼


查看 [附文](https://github.com/cryptoadvance/specter-diy/tree/master/docs/enclosures) 資料夾。


### 要有創意！


組裝您自己的 Specter-DIY，並將圖片寄給我們（提出拉取請求或聯絡我們）。


看看 [圖庫](https://github.com/cryptoadvance/specter-diy/blob/master/docs/pictures/gallery/README.md) 與社群組合的 Specters！




## 安裝已編譯的程式碼


使用安全開機載入程式後，韌體的初始安裝方式略有不同。升級更容易，而且不需要將硬體 wallet 連接到電腦。


![video](https://youtu.be/eF4cgK_L6T4)


### 閃存初始韌體


**Note** 如果您不想使用釋出版本中的二進位檔，請查看 [bootloader documentation](https://github.com/cryptoadvance/specter-bootloader/blob/master/doc/selfsigned.md) 說明如何編譯與設定，以使用您的公開金鑰而非我們的金鑰。



- 如果您要從 `1.4.0` 以下的版本升級，或是第一次上傳韌體，請使用 [releases](https://github.com/cryptoadvance/specter-diy/releases) 頁面的 `initial_firmware_<version>.bin` 。
 - 根據 [Stepan 的 PGP 金鑰] 驗證 `sha256.signed.txt` 檔案的簽章(https://stepansnigirev.com/ss-specter-release.asc)
 - 將 `initial_firmware_<version>.bin` 的切細值與儲存於 `sha256.signed.txt` 中的切細值進行驗證
- 如果您從一個空的開機載入程式升級，或看到開機載入程式錯誤訊息顯示韌體無效，請查看下一部分 - 更新已簽署的 Specter 韌體。
- 請確定您發現板的電源跳線位於 STLK 位置。
- 透過板卡頂端的 **miniUSB** 連接線，將發現板連接到您的電腦。
    - 主機板應該會以名為 `DIS_F469NI` 的抽取式磁碟出現。
- 將 `initial_firmware_<version>.bin` 檔案複製到 `DIS_F469NI` 檔案系統的根目錄。
- 當主機板完成韌體更新後，主機板將會自行重設，並重新開機至 Bootloader。Bootloader 將檢查韌體並開機進入主韌體。如果看到找不到韌體的錯誤訊息 - 請按照更新指示，透過 SD 卡上傳韌體。
- 現在您可以將電源跳接器切換到您喜歡的位置，並使用電源銀行或電池為電路板供電。


透過複製貼上`.bin`檔來更新初始韌體有時會失敗 - 通常是因為連接線的問題，或是您透過 USB 集線器連接裝置。在這種情況下，您可以多嘗試幾次 (通常嘗試 2-3 次即可成功)。


如果總是失敗，您可以使用 [stlink](https://github.com/stlink-org/stlink/releases/latest) 開放原始碼工具。安裝後，在終端機輸入`st-flash write <path/to/initial_firmare.bin> 0x8000000`。這通常會更可靠。


### 升級韌體



- 從 [releases](https://github.com/cryptoadvance/specter-diy/releases) 下載 `specter_upgrade_<version>.bin`。
- 將此二進位檔複製到 SD 卡的根目錄 (FAT 格式，最大 32 GB)
 - 確定根目錄中只有一個 `specter_upgrade***.bin` 檔案
- 將 SD 卡插入探索板的 SD 插槽並開啟電源
- Bootloader 會閃存韌體，完成後會通知您。
- 重新啟動主機板 - 您會看到 Specter-DIY 介面，它會建議您選擇 PIN 碼。


每當有新版本推出時，只要從版本中下載`specter_upgrade_<version>.bin`，將它放入 SD 卡，然後就像上一步一樣升級裝置。Bootloader 將確保只有經過簽署的韌體才能載入到主機板上。


### 如何找出韌體版本


進入「裝置設定」功能表 - 畫面標題下方會顯示版本號碼。


## 使用 Specter-DIY wallet



![video](https://youtu.be/Oysg-hhBusc)



![video](https://youtu.be/XfMr7B_uUIk)



![video](https://youtu.be/BzBlh_knIww)



## Specter-DIY 的安全性


### 硬體


顯示器由應用 MCU 控制。


安全元件整合尚未完成 - 目前機密也儲存在主 MCU 上。但您可以使用 wallet，而無需儲存秘密 - 您需要每次輸入恢復短語。如果您能記住整個記憶體，為何要記住長長的 passphrase？


裝置使用外部快閃記憶體儲存某些檔案 (QSPI)，但所有使用者檔案都由 wallet 簽署，並在載入時進行檢查。


QR 掃描功能位於單獨的微控制器上，因此所有影像處理都發生在安全關鍵 MCU 之外。目前 USB 和 SD 卡仍由主 MCU 管理，因此如果您想降低攻擊面，就不要使用 SD 卡和 USB。


### PIN 保護（使用者驗證）


在第一次開機時，主 MCU 會產生一個獨特的密碼。此密碼可讓您確認裝置並未被惡意的裝置取代 - 當您輸入 PIN 碼時，您會看到一組字詞，當密碼存在時，這些字詞將保持不變。


您的 PIN 碼與這個獨特的秘密一起用來 generate 解密您的 Bitcoin 金鑰 (如果您有儲存的話)。因此，如果攻擊者能夠繞過 PIN 螢幕，解密仍然會失敗。


如果您已經鎖定韌體 (TODO：在此加入說明連結)，它也會有效地鎖定秘密，因此如果攻擊者在主機板上刷新不同的韌體，秘密就會被刪除，當您開始輸入 PIN 碼時，您就可以識別它 - 字元順序將會不同。


### 復原詞組的產生


這是 wallet 最重要的部分之一 - 要安全地 generate 關鍵。為了做好這一點，我們使用多種熵源：



- 微控制器的 TRNG。專屬、經過認證，也許是好東西，但我們不信任它
- 觸控螢幕。每次您觸摸螢幕時，我們都會測量您觸摸的位置和發生的時間（以微控制器的 180MHz 嘀嗒聲為單位）。
- 內建麥克風 - 尚未有。板上有兩個麥克風，因此硬體 wallet 可以聆聽您的聲音，並將這些資料混入熵池中。


所有這些熵都會散列在一起，並轉換為您的恢復詞組。所得的熵總是比任何單獨的來源都要好。


### 高階邏輯 - 錢包


Specter 作為金鑰儲存器運作。Specter 儲存了 HD 私密金鑰，這些金鑰可以用於錢包。錢包是由其描述符定義的。我們也支援 miniscript。


每個 wallet 都屬於一個特定的網路。這表示如果您在 `testnet` 上匯入一個 wallet，它將不能在 `mainnet` 或 `regtest` 上使用 - 您需要切換到這個網路，然後分別匯入 wallet。


### 交易驗證


以下規則適用於 wallet 將會簽署的交易：



- 如果發現來自不同錢包的混合輸入，會警告使用者 ([attack](https://blog.trezor.io/details-of-the-multisig-change-address-issue-and-its-mitigation-6370ad73ed2a))
- 變更輸出會顯示傳送至 wallet 的名稱
- 若要使用 multiisig 或 miniscript，您首先需要加入 wallet 描述檔 (透過 QR、USB 或 SD 卡) 來匯入 wallet


## 描述符支援


所有正常的 Bitcoin 描述符都可以使用。除此之外，我們還有一些擴充功能：


### 描述符中的多重分支


為了節省 QR 碼的空間，我們允許一次加入多個分支的描述符。如果您想使用 `wpkh(xpub/0/*)` 來接收地址，並使用 `wpkh(xpub/1/*)` 來變更地址，您可以將它們合併為單一描述符： `wpkh(xpub/{0,1}/*)` - wallet 會將 `{}` 設定部分的第一個索引視為接收地址的分支，而第二個索引則視為變更地址的分支。


您也可以指定兩個以上的分支，而且不同的聯署人的分支索引可以不同，所以這個描述符非常奇怪，但完全有效：


```
wsh(sortedmulti(2,xpubA/{22,33,44}/*,xpubB/34/*/{1,8,6},pubkey3))
```


在此，wallet 將使用 `wsh(sortedmulti(2,xpubA/22/17,xpubB/34/17/1,pubkey3))` 中的指令碼來接收位址號碼 17。


唯一的要求是所有資料集中的索引數量相同 (上述案例中為 3)。


### 預設衍生


如果描述符包含主公鑰但不包含通配符衍生，預設衍生 `/{0,1}/*`將被加入描述符中的所有擴充金鑰。如果至少有一個 xpub 有通配符衍生，描述符將不會改變。


描述符 `wpkh(xpub)` 將會轉換為 `wpkh(xpub/{0,1}/*)`。


### 迷你腳本


Specter 支援 miniscript，但不支援 policy-tominiscript 編譯（因為太昂貴）。我們會對 miniscipt 執行一些檢查，因此頂層只允許使用 `B` scripts，子 miniscripts 中的所有參數都必須根據 [spec](http://bitcoin.sipa.be/miniscript/) 具有屬性。


您可以使用 [bitcoin.sipa.be](http://bitcoin.sipa.be/miniscript/) 來 generate 策略中的描述符，然後將其匯入 wallet。


例如，「我現在可以花，或者 100 天後我太太可以花」的保單可以這樣轉換成 wallet：


政策：`或(9@pk(xpubA),and(older(14400),pk(B)))` (我的金鑰是 9 倍的可能性)


Miniscript：`or_d(pk(xpubA),and_v(v:pkh(xpubB),older(14400)))`


Descriptor：`wsh(or_d(pk(xpubA),and_v(v:pkh(xpubB),alier(14400))))`)


由於這裡沒有任何萬用字元，預設的 `/{0,1}/*`將附加到 xpubs。



---

MIT 授權


版權所有 (c) 2019 cryptoadvance


---