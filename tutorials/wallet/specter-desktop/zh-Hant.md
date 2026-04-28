---
name: Specter Desktop
description: 使用您自己的節點，完全自主地管理您的多重簽章 Bitcoin 投資組合
---

![cover](assets/cover.webp)



Specter Desktop 是 Cryptoadvance 自 2019 年起開發的一款開放源碼應用程式（MIT 授權），有助於管理 Bitcoin 電子錢包與您的硬體電子錢包（Ledger、Trezor、Coldcard、BitBox02、Passport 等）以及您自己的 Bitcoin 基礎架構（Bitcoin 核心節點或 Electrum 伺服器）。此應用程式尤其擅長於多重簽章配置，可讓您透過在多個獨立硬體錢包之間分配簽章能力來保護大筆資金。



**在本教程中，您將學習如何：**




- 在電腦上安裝和設定 Specter Desktop（Windows、macOS 或 Linux）
- 將 Specter 連接到 Electrum 伺服器 (本範例中我們使用 Umbrel)
- 使用 wallet 硬體建立簡單的 wallet (Coldcard)
- 以完全主權的方式接收和發送比特幣
- 使用數個硬體錢包設置 2 對 3 多重簽章 wallet
- 在 Umbrel 伺服器上安裝 Specter（進階獎金）



您的所有交易將透過您自己的基礎架構在本機進行驗證，不會傳送任何資訊到外部伺服器，保證您的機密性和財務主權。簽署前請務必在您的 wallet 硬體螢幕上檢查交易。



## 下載與安裝



請造訪 Specter Desktop 官方網站下載應用程式。



![Page d'accueil Specter](assets/fr/01.webp)



在下載頁面，選擇與您作業系統相對應的版本：macOS、Windows 或 Linux。



![Téléchargement selon l'OS](assets/fr/02.webp)



下載完成後，請依照作業系統的一般指示安裝應用程式。對於 macOS，請將圖示拖曳到「應用程式」中。對於 Windows，執行安裝程式。對於 Linux，請遵循套件指示。



## 初始設定



第一次啟動時，Specter Desktop 會要求您選擇連線類型。您可以連線到 Electrum 伺服器或您自己的 Bitcoin 核心節點。



![Choix du type de connexion](assets/fr/03.webp)



在這個範例中，我們會使用連線到在 Umbrel 上執行的 Electrum 伺服器。



如需詳細資訊，請參閱我們的 Umbrel 教學：



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

此選項提供比 Bitcoin Core 更快的同步速度。如果您願意，可以選擇「Bitcoin Core」，然後設定與本機節點的連線。無論您選擇何種方式，以下步驟都相同。



選擇「Electrum 連線」，然後選擇「輸入我自己的」，設定您自己的 Electrum 伺服器。



![Configuration Electrum](assets/fr/04.webp)



輸入 Electrum 伺服器的位址。在我們使用 Umbrel 的情況下，位址將會是 `umbrel.local`，連接埠則是 `50001`。按一下「連線」建立連線。



連線後，會出現歡迎畫面，並提供清單讓您開始使用。現在您需要新增硬體錢包。



![Écran d'accueil](assets/fr/05.webp)



## 新增 wallet 硬體



在左側功能表中，按一下「新增裝置」以新增您的 wallet 硬體。



Specter Desktop 支援許多硬體錢包：Trezor、Ledger、BitBox02、Coldcard、KeepKey、Keystone、Cobo Vault 等等。



如果您想瞭解更多資訊，請參閱我們的硬體 wallet 教學。



![Sélection du type de hardware wallet](assets/fr/06.webp)



選擇您的 wallet 硬體。在這個範例中，我們使用 Coldcard MK4。



以下是 wallet 硬體的使用教學：



https://planb.academy/tutorials/wallet/hardware/coldcard-mk4-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

對於 Coldcard，您需要透過 USB 連線或 microSD 卡從 wallet 硬體匯出公開金鑰。



![Import des clés du Coldcard](assets/fr/07.webp)



按照顯示的指示從 Coldcard 匯出金鑰。為您的 wallet 硬體命名 (這裡是 "MK4 Tuto")。匯入金鑰後，您可以使用單一金鑰建立 wallet，或新增其他硬體錢包以建立多重簽章的 wallet。



![Dispositif ajouté](assets/fr/08.webp)



## 建立投資組合



新增 wallet 硬體後，按一下「建立單一金鑰 wallet」以建立單一簽章 wallet。



為您的投資組合命名（例如「Wallet for tuto」），並選擇位址類型。選擇「Segwit」以使用可優化交易成本的原生 bech32 位址。



![Configuration du portefeuille](assets/fr/09.webp)



當您的投資組合建立後，Specter 會提供一個備份的 PDF 檔案，其中包含所有還原投資組合所需的公開資訊（描述符、擴展的公開金鑰）。此檔案不包含您的私人密碼匙。



![Sauvegarde du portefeuille](assets/fr/10.webp)



## 接收比特幣



要接收比特幣，請在左側菜單中選擇您的 wallet，然後點擊「接收」標籤。



Specter 會自動產生具 QR 碼的新接收地址。



![Génération d'une adresse de réception](assets/fr/11.webp)



您可以複製地址或掃描 QR 代碼。在傳送地址給任何人之前，請務必檢查 wallet 硬體螢幕上的地址。



## 檢視歷史和地址



收到 bitcoins 後，您可以在「交易」標籤中檢視您的交易。



![Historique des transactions](assets/fr/12.webp)



地址」標籤可讓您檢視投資組合產生的所有地址，以及它們的使用狀態和相關金額。



![Liste des adresses](assets/fr/13.webp)



## 發送比特幣



要發送比特幣，請點擊 「發送 」標籤。輸入收件人的地址、要傳送的金額，如果您想手動選擇 UTXOs（硬幣控制），請勾選進階選項。



![Création d'une transaction](assets/fr/14.webp)



點擊 "Create Unsigned Transaction "建立交易。之後 Specter 會要求您使用 wallet 硬體簽署交易。



![Signature de la transaction](assets/fr/15.webp)



如果您使用的是 Coldcard，您可以選擇透過 USB 或使用 microSD 卡 (air-gapped) 來簽署。在 wallet 硬體螢幕上確認交易，仔細檢查目的地地址和金額。



交易簽署完成後，您就可以在 Bitcoin 網路上廣播。



![Options de diffusion](assets/fr/16.webp)



點擊 「發送交易 」發送交易。Specter 會確認您的交易已經傳送，您可以在「交易」標籤中追蹤其狀態。



![Diffusion de la transaction](assets/fr/17.webp)



## 建立和使用多重簽名組合



Specter Desktop 的主要資產之一，就是能夠簡化多重簽章組合的管理。多重簽章 wallet 需要多個簽章來授權交易，因此消除了單點故障。以 2 對 3 組態為例，需要來自三個獨立硬體錢包的兩個簽章，才能驗證任何支出。



若要建立多重簽章 wallet，首先要透過「新增裝置」新增所有簽章硬體錢包。在這個範例中，我們會使用三種不同的硬體錢包：Coldcard MK4 (先前已加入)、Passport 和 Ledger。製造商的多樣化避免了對單一供應鏈或韌體的依賴，從而加強了安全性。



以下是 Ledger 和 Passport 教學的連結：



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

透過命名 wallet 硬體 (例如「Passport multi」) 新增 Passport，並透過 microSD 卡或 QR 碼匯入其金鑰。然後按一下「繼續」繼續。



![Ajout du Passport](assets/fr/23.webp)



然後透過 USB 連接 Ledger，並在 wallet 硬體上開啟 Bitcoin 應用程式來新增 Ledger。命名它（例如，"ledger multi「）並點擊 」Get via USB「（通過 USB 獲取），然後點擊 」Continue"（繼續）以匯入其公開金鑰。



![Ajout du Ledger](assets/fr/24.webp)



在 Specter 註冊三個硬體錢包後，點選「新增 wallet」並選擇「多重簽章」選項，即可建立多重簽章 wallet。



![Choix du type de wallet](assets/fr/25.webp)



選擇您希望包含在多重簽章法定人數中的三個硬體錢包：MK4 Tuto、Passport multi 和 ledger multi。按一下「繼續」進入下一步。



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



選擇您的多重簽章配置。選擇「Segwit」作為地址類型，以受益於優化的費用。授權交易所需的簽名 (m of 3)」參數可讓您定義門檻：對於 2 對 3 組態，需要 2 個簽名。每個 wallet 硬體都會顯示其對應的多重簽名金鑰。按一下「建立 wallet」以完成建立。



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



您的 "Multi tuto "多重簽名組合現已建立。Specter 立即建議您儲存包含作品集描述的備份 PDF 檔案。點擊 「保存備份 PDF 」下載這個關鍵文件。



![Wallet multisig créé](assets/fr/28.webp)



Specter 也可讓您透過 QR 碼或檔案匯出 wallet 資訊到每個硬體錢包。這可讓某些硬體錢包 (例如 Coldcard 或 Passport) 直接在記憶體中儲存 multisig 設定。



對於 Passport，請解除鎖定您的裝置，然後到「管理帳戶」>「連接 Wallet」>「Specter」>「Multisig」>「QR Code」，然後掃瞄 Specter 所產生的 QR Code。接著，您的 Passport 會要求您掃描 wallet 的接收位址，以驗證 multiisig 設定。



對於 MK4，將其插入電腦並解鎖。然後按一下「儲存 MK4 Tuto 檔案」並將檔案儲存到您的 MK4。下次您簽署 wallet 硬體時，MK4 會使用此檔案完成多重簽章的設定。



![Export vers les hardware wallets](assets/fr/29.webp)



為了讓您瞭解資訊，您可以隨時從投資組合的「設定」標籤，然後選取「匯出」存取備份：



![Accès au backup PDF](assets/fr/30.webp)



日常使用仍類似於簡單的 wallet：您 generate 接收地址如常。要發送 bitcoins，請到「發送」標籤，輸入收件者的地址和金額，然後點選「建立未簽署交易」。



![Création d'une transaction multisig](assets/fr/31.webp)



Specter 建立 PSBT (Partially Signed Bitcoin Transaction) 並顯示「Acquired 0 of 2 signatures」。現在您必須使用三個硬體錢包中的至少兩個簽名。點選第一個 wallet 硬體 (例如「MK4 Tuto」) 以使用您的 Coldcard 簽署，然後點選第二個 (例如「Passport multi」) 以取得所需的第二個簽章。



![Signature de la transaction](assets/fr/32.webp)



取得所需的 2 個簽名後 (介面會顯示「Acquired 2 of 2 signatures」和「Transaction is ready to send」)，點選「Send Transaction」即可在 Bitcoin 網路上廣播交易。



![Transaction prête à être diffusée](assets/fr/33.webp)



這種多重簽名方式特別適合公司 (需要多位經理核准支出)、家庭 (保護多代遺產) 或管理大筆資金的個人 (硬體錢包的地理分佈可抵擋局部災害)。



### 多重簽章備份的關鍵重要性



**請注意**：備份多組位組合與備份單一組合有根本的不同。單靠您的復原短語 (seed 短語) 並不足以還原多重組合。您還必須備份**output descriptor** (output descriptor)，其中包含您的多重組合的組態資訊。



output descriptor 包括基本資料：每個聯署人的擴展公開金鑰 (xpubs)、簽署門檻（在我們的例子中為 2 對 3）、使用的腳本類型（原生、嵌套或傳統 Segwit），以及每個 wallet 硬體的旁路路徑。如果沒有這個描述符，即使您有三個恢復短語中的兩個，您也無法重建您的 wallet 或存取您的比特幣。描述符可讓您的軟體知道如何結合公開金鑰，以 generate 取得與您的資金對應的 Bitcoin 位址。



Specter Desktop 會在您建立 multiisig 組合時自動產生一份備份 PDF 檔案。此 PDF 文件包含完整的描述符、每個 wallet 硬體的指紋，以及還原所需的所有公開資訊。 **此檔案不包含您的私人金鑰**，因此本身不允許您花費您的比特幣，但它允許任何存取此檔案的人查看您完整的交易歷史和餘額。



若要正確備份您的多重簽名組態，請遵循以下步驟：建立您的作品集後，按一下「設定」標籤，然後按一下「匯出」，並選擇「儲存備份 PDF」。為此 PDF 創建幾份副本：在紙張上至少列印兩份副本，同時保留一份加密的數位副本。將 PDF 複本與您的每個復原短語一起儲存，並分別存放在不同的地理位置。



在防火防水的金屬板上鐫刻您的復原短語，以保證其壽命。永遠不要低估這些備份的重要性：如果您遺失了電腦上的「~/.specter」資料夾，而且在沒有描述符備份的情況下遺失了其中一個硬體錢包，那麼您所有的資金都將無法挽回，即使是 2 對 3 的配置也是如此。多重簽章備援可防止 wallet 硬體遺失，但前提是您已正確備份 wallet 的描述符。



## Specter Desktop 的優點與限制



**優點**：無需第三方伺服器即可進行完全本機驗證，達到最佳保密性。進階配置的多重簽章彈性（公司、家庭、個人）。廣泛的硬體 wallet 支援，具備完整的互通性 (USB 和 air-gapped)。



**限制**：對於進階的 Bitcoin 概念 (UTXO、描述符、衍生路徑) 有相當大的學習曲線。



## 最佳實踐



在驗證之前，請務必檢查硬體 wallet 螢幕上的位址和金額，以防止惡意軟體。



將 PDF 備份與您的種子分開保存。這些公開描述符可儲存於銀行保險庫或加密雲端，方便復原，而不會暴露您的私人金鑰。



在使用大額資金的投資組合之前，先在 token 的金額上測試復原。建立、測試、刪除和復原以驗證您的程序。



保持 Specter 和您的韌體為最新版本。將您的多重簽章共同簽章人分佈在不同的地理位置 (住家/辦公室/附近)，以抵擋局部性的災害。使用描述性標籤，方便會計和報稅。



## 獎勵：在 Bitcoin 伺服器上安裝 (Umbrel、RaspiBlitz、Start9)



如果您已經擁有 Bitcoin 伺服器，例如 Umbrel、RaspiBlitz、MyNode 或 Start9，您可以直接從它們的應用程式商店安裝 Specter Desktop。這種方式有幾個顯著的優點：應用程式會自動與您的本機 Bitcoin 核心節點進行設定，您可以從網路上的任何裝置透過 Web 介面全天候存取，甚至可以透過 Tor 安全地遠端存取。您的整個 Bitcoin 基礎架構都集中在單一專用伺服器上，簡化管理並加強您的主權。



### 從 Umbrel App Store 安裝



從您的 Umbrel 介面，前往 App Store 並搜尋 Specter Desktop。按一下「安裝」啟動安裝。



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



安裝完成後，在您的 Umbrel 上開啟 Specter Desktop。歡迎畫面會要求您選擇連線類型。如果您在 Umbrel 上使用 Specter，請點選「更新設定」來設定連線。



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



選擇「遠端 Specter USB 連線」，可以在遠端 Umbrel 伺服器上使用 Specter 時，使用連接到本機電腦的 USB 硬體錢包。



![Configuration Remote Specter USB](assets/fr/20.webp)



按照顯示的指示設定 HWI 網橋。您需要存取裝置網橋設定，並將網域 `http://umbrel.local:25441` 加入白名單。按一下「Update」儲存組態。



![HWI Bridge Settings](assets/fr/21.webp)



如果您也想從本機電腦使用 USB 硬體錢包，請下載 Specter Desktop 應用程式到您的電腦，並設定為 「是，我遠端執行 Specter」。點擊 "Save "完成配置。



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## 總結



Specter Desktop 將先進的 Bitcoin 配置民主化，在不犧牲您的主權或機密性的情況下，讓多重簽章成為可能。對於管理大筆資金的使用者而言，它可將機構作法轉變為私人也能部署的解決方案。



儘管應用程式需要在基礎架構和學習方面進行初始投資，但它提供了完全的主權：對驗證基礎架構的控制、鑰匙的實體所有權，以及不受第三方監控的交易。無論您是個人保護您的儲蓄、家庭建立多代同堂的保險箱，或是公司管理現金流，Specter Desktop 都是協調最高安全性與絕對主權的參考工具。



## 資源



### 官方文件




- [Specter Desktop 官方網站](https://specter.solutions/desktop/)
- [GitHub 原始碼](https://github.com/cryptoadvance/specter-desktop)
- [完整文件](https://docs.specter.solutions/)



### 社群與支援




- [Telegram Specter 社區群組](https://t.me/spectersupport)
- [Reddit討論區](https://reddit.com/r/specterdesktop/)
- [GitHub 錯誤報告](https://github.com/cryptoadvance/specter-desktop/issues)