---
name: Liana
description: 在 Liana 上設定和使用 Wallet
---
![cover](assets/cover.webp)


在本教程中，我們將逐步解釋如何在電腦上使用 Liana 應用程式。其中，您將學習如何設定自動繼承計劃、在正常情況下接收和發送比特幣，以及在特定期限後從現有的 Wallet 中取回資金。


2025 年 1 月，與 Liana 相容的硬體錢包有BitBox02、Blockstream Jade、Blockstream Jade Plus、COLDCARD MK4、COLDCARD Q、Ledger Nano S、Ledger Nano S Plus、Ledger Nano X、Ledger Flex、Specter DIY。


如果您希望從現有的 Liana Wallet 復原資金，請閱讀下面的介紹，並直接前往「復原比特幣」部分。


## 介紹 Liana 軟體


Liana 是一套開放原始碼軟體，專為建立和管理進階錢包而設計，尤其是作為自動繼承系統或強大備份機制的一部分。該專案自 2022 年起由 Kévin Loaec 和 Antoine Poinsot 共同創立的 Wizardsardine 公司開發。在官網上，Liana 被介紹為「一個簡單的個人收藏 Wallet，具有復原與繼承功能」。該軟體可在 Linux、MacOS、Windows 等電腦上執行，其 (開放) 原始碼 [可在 GitHub 上取得](https://github.com/wizardsardine/Liana)。


Liana 以 Bitcoin 的可編程性為基礎，創建了先進的 Wallet。特別是，它利用了時間鎖 (*timelocks*) 的優勢，時間鎖只允許在特定時間過後才可動用資金，而時間鎖涉及到比特幣的回收。因此，一個 Liana Wallet 是由數個支出路徑組成的：




- 一個主要的消費途徑，隨時可用；
- 至少有一個復原路徑，可在特定時間後存取。


下圖說明具有兩個支出路徑的 Wallet 的運作：


![Schéma explicatif](assets/fr/01.webp)


此操作可讓您設定各種配置，包括 ：




- 繼承（或繼承）計劃，使繼承人能夠在使用者死亡時收回資金。如需更多相關資訊，建議閱讀 BTC102 課程的 [第 4 部分](https://planb.network/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f/233c88d3-2e8e-5eba-ac06-efe67a209038)。
- 具有恢復時間的強化備份，讓使用者可以使用 Wallet，而無需保留相對應的密語，例如在盜竊時冒著被竊的風險。
- 以 Bitcoin 開始的人的安全網：他們將管理自己的 Wallet，而他們的「監護人」（例如親戚）將保留在特定期限後收回資金的權利。
- 多方簽章方案 (*Multisig*) 可隨時間降低要求，以應付一個或多個參與者（如公司的合作夥伴）消失的情況。


Liana 的最大優勢在於它引入了一種標準化的方式，保證在用於當期支出的主鑰丟失時能收回資金。這對於乾淨的資金保管來說是一項巨大的創新，而資金保管是充滿風險的，尤其是當您對這方面不甚了解的時候。因此，Liana 可以鼓勵即使是最不願冒險的使用者停止使用保管人（例如 Exchange 平台）來保管他們的資金，並重新獲得他們的資金 Ownership，以符合 Bitcoin 的 Cypherpunk 精神。


當然，Liana 也有其缺點。首先，您必須在 Bitcoin Blockchain 上進行交易，定期更新您的 Wallet。這可能很麻煩（取決於您使用軟體的頻率），而且成本很高（取決於當時的費用水平），但這是您為了額外的安全性所付出的代價。


第二個負面因素可能是機密性。當您讓其他人參與設定時，他或她會知道您的所有位址，因此可以監控您的活動。不過，如果您選擇強化備份，或選擇繼承計畫，讓您的繼承人無法立即知道 Wallet 的詳細資訊，這就不成問題了。


## 準備工作


在本教程中，我們將設定繼任計劃。我們將使用 .NET Framework 2.0：




- Ledger Nano S Plus，用於日常開支；


https://planb.network/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4


- Blockstream Jade，用於回收資金；


https://planb.network/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3


- 兩個儲存媒體 (USB 隨身碟)，用來儲存 Wallet 描述符；
- 繼承書，包含收回資金的指示；
- 有編號的密封袋，以確保回收裝置 (Jade) 未被使用。


## 安裝與設定


請造訪 Wizardsardine 官方網站並下載 Liana，網址為 https://wizardsardine.com/Liana/。您也可以 [從 GitHub 倉庫] 下載最新版本(https://github.com/wizardsardine/Liana/releases)，您可以檢查軟體的真實性。本教學使用的版本為 0.9。


![Télécharger Liana](assets/fr/02.webp)


要瞭解如何在安裝前手動驗證軟體的真實性和完整性，建議您參閱本教程 ：


https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

在您的機器上安裝軟體並啟動。選擇「*建立新的 Liana Wallet*」選項來設定您的 Wallet。


![Accueil Liana](assets/fr/03.webp)


選擇您的 Wallet 類型。如果您想要設定具有復原時間的增強備份，您可以選擇「*建立您自己的*」選項，並選擇預設方案。這將以大致相同的方式運作，只是您不需要保留 Hardware Wallet 復原短語。


我們在此忽略了*擴充 Multisig*的情況，它設定了更複雜的配置。


在本教程中，我們將使用簡單的繼承。


![Choisir type de portefeuille](assets/fr/04.webp)


以下是快速說明。


![Rapide explication](assets/fr/05.webp)


閱讀完解釋後，您就可以設定 Liana Wallet 的鑰匙了。這是關鍵的一步，因為它決定了您帳戶的消費特性。


![Configurer clés](assets/fr/06.webp)


首先，在 「進階設定 」功能表中，您可以決定 「描述符類型」，即 Contract 在鏈上的寫入方式。您可以選擇兩種類型：P2WSH (SegWit) 或 Taproot。在這兩種情況下，支出條件的語義將是相同的。P2WSH 使 Contract 更容易理解，而 Taproot 的優點在於它隱藏了未使用的條件，並在檢索時節省成本。


此選項為選項：若有疑問，請保留預設選項 (版本 0.9 時為 P2WSH，但此選項可能會變更)。


![Choisir le type de descripteur](assets/fr/07.webp)


接下來，設定您的主索引鍵 (*primary key*)。這個鍵（或者說，這組鍵）將用於當前的資金支出，不受任何時間條件的限制。點擊 「*設定*」，您可以選擇相應的*簽署裝置*。在我們的案例中，我們選擇了 Ledger Nano S Plus Hardware Wallet。


授權分享裝置的擴充公開金鑰。給這個金鑰一個有意義的名稱 (在此例中為 "Nano S+")。請注意，裝置上安裝的所有應用程式都會繼續正常運作。


![Configurer clé principale](assets/fr/08.webp)


接下來，設定回報延遲，也就是*繼承權鑰*可以花費資金的時間。此延遲以區塊定義，每個區塊平均相隔 10 分鐘。它的範圍從 10 分鐘 (1 個區塊) 到大約 15 個月 (65,535 個區塊)。這個上限是 Bitcoin 通訊協定的限制，因為鎖定時間是以 16 位元編碼。


除非有特殊情況，否則請選擇最長的交貨期：15 個月或 65,535 塊。這將節省您的成本。不過，我們建議您每年執行一次更新程序 (如「更新 Wallet」一節所述)，總是在每年的同一時間進行，以「儀式化」這項作法，避免遺忘。


在此，我們設定恢復時間為一小時（6 個區塊）來進行測試。


![Configurer temps de verrouillage](assets/fr/09.webp)


最後，設定您的遺產金鑰。這個金鑰 (或者說，一組金鑰) 將會在您失蹤時用來追回資金。按一下「*設定*」，選擇簽署裝置，並驗證在其上共用擴充的公開金鑰。


在本教程中，我們選擇 Jade。給鑰匙取一個喚起靈感的名字 (這裡是 "Jade")。與第一個裝置一樣，傳統的帳號仍可繼續運作。


![Configurer clé de succession](assets/fr/10.webp)


完成所有這些動作後，請檢查一切正常，然後按一下「*繼續*」確認您的選擇。


![Confirmer clés](assets/fr/11.webp)


下一步是儲存您的 Wallet 描述符。這是您在帳戶中尋找資金所需的資訊。與 Mnemonic 短語相反，描述符不允許您花費資金，因此公開描述符只會造成保密問題（對方會知道您所有的交易）。


將說明書的兩份副本保存在 USB 隨身碟等電子媒體上。確保您也列印出兩份紙本副本，以便在電子媒體損壞時可以存取。每個備份都必須與簽章裝置相關聯。


![Sauvegarder descripteur](assets/fr/12.webp)


我們的描述符（在本教程的最後分析）如下：


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


Wallet 初始配置的最後一步是驗證每個作為簽章裝置的硬體錢包中的描述符。


![Enregistrer descripteur](assets/fr/13.webp)


對每個簽章裝置執行相同步驟。您需要檢查並確認描述符已加入每個 Hardware Wallet。


![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)


您的 Wallet 資訊現在已經註冊完成，剩下的就是設定您要如何連線到 Bitcoin 網路。您可以選擇使用自己的節點（本機或遠端），或是使用 WizardSardine 的基礎架構。在後者的情況下，您需要將電子郵件 Address 連接到您的 Wallet，這樣就可以擷取描述符。WizardSardine 將可存取您所有的交易。因此建議您選擇第一種方式。


![Sélectionner connexion réseau](assets/fr/15.webp)


我們選擇使用自己的節點。您可以使用現有的節點，或在您的機器上安裝一個 * 經過修剪的節點*。如果您無法使用其他節點，請在您的機器上安裝自己的節點，這應該需要一些時間（約數天）。


![Choisir type de nœud](assets/fr/16.webp)


在本教程中，我們使用了一個現有的（公共）Electrum 伺服器。但是要小心！它可以存取我們使用 Liana Wallet 的所有活動。所以如果您想保護您的隱私，請使用您自己的節點。


![Connexion serveur Electrum public](assets/fr/17.webp)


節點設定完成後，應該會開啟主畫面，顯示您新建立的 Liana Wallet。


把握機會將復原裝置存放在安全的地方。它應該存放在策略性的地點，以便在您過世時，您的繼承人可以找到它。


為了增加安全性，您可以將用於復原的元件放入密封袋中 (* 防拆袋*)，並在某處寫下其序號。這樣可以確保沒有人存取過，而且您的裝置仍然有效。


在我們的範例中，我們組裝了下列 Elements：




- Blockstream Jade 作為產業的簽章裝置；
- 一條 USB 傳輸線，用於連接裝置和為裝置充電；
- 在裝置發生故障或損壞時，可將句子以紙張形式備份（請注意，媒體也可以是金屬，因此可免受 Elements 的保護，例如 Cryptosteel 膠囊就是如此）；
- 包含 Wallet 描述符的 USB 密鑰 ；
- 描述符的紙張備份，以防 USB key 發生故障或損壞（此備份未在此拍照）；
- 繼承書，說明收回資金所採取的步驟。


![Éléments de récupération](assets/fr/18.webp)


我們把這些項目放在 Seal 項下！


![Sachet scellé récupération](assets/fr/19.webp)


## 收到資金


Liana 的主螢幕會顯示您的餘額以及與 Wallet 相關聯的交易（過去和現在）。在我們的情況下，餘額為零，這是正常的。


![Écran principal](assets/fr/20.webp)


若要接收資金，請移至「*接收*」標籤，然後按一下「*generate Address*」。一個新的 Address 應該會出現在您的螢幕上。它比傳統錢包要長：它是一個連結到獨立 Contract (P2WSH 或 Taproot) 的 Address。


![Générer nouvelle adresse](assets/fr/21.webp)


您需要在 Hardware Wallet 上按一下「*在硬體裝置上驗證*」來驗證此 Address。


![Vérifier adresse portefeuille matériel](assets/fr/22.webp)


一旦資金匯出，交易就會出現在主畫面上（先是未確認，後是已確認）。在這裡，我們發送了 50,000 薩托希（轉帳時剛好超過 50 美元）進行測試。不言而喻，由於交易費用的關係，在您的情況下，轉帳金額必須比這個數值高出一個數量級。


![Vérifier solde](assets/fr/23.webp)


您可以進入 「*硬幣*」標籤查看您資金的到期狀態。此標籤會顯示您 Wallet 中的不同硬幣 (UTXO)。在這裡，我們可以看到我們的交易創建的 50,000 Satoshis 硬幣在同一天（一小時後）到期。


![Obtenir informations pièce](assets/fr/24.webp)


要更好地理解 Bitcoin 中使用的 UTXO 表示模型，您可以參考 Loïc Morel 撰寫的 Bitcoin 中保密性課程的第一部分 ：


https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## 經常開支


目前的支出是使用 Liana 的正常情況。使用主密鑰發送比特幣的工作方式與所有經典 Bitcoin 錢包（如 Electrum 或 Sparrow）相同。


要進行充值，請移至 「*發送*」標籤，然後輸入基本資訊：收件人的 BTC Address、要發送的金額以及所需的充值費率。為了您的個人方便，還可以添加描述（儲存在本地）。在我們的例子中，我們發送了 10,000 Satoshis 到某 Bob，收費率為 4 Sat/ov，或交易時的 0.67 美元。


Liana 也提供「硬幣控制」功能：您可以指出要花費的硬幣 (UTXO)。在這裡，我們選擇了之前製作的 50,000 薩托希斯硬幣。


![Envoyer fonds clé principale](assets/fr/25.webp)


然後點擊 "*Sign*"，使用與主密鑰相連的簽名裝置簽署交易。您需要在 Hardware Wallet 上驗證和確認交易。在這裡，我們使用 Nano S Plus 來簽署交易。


![Signer transaction clé principale](assets/fr/26.webp)


最後，按一下「*Broadcast*」即可在網路上廣播交易。請注意，傳送資金會重設已使用硬幣的回收時間。


![Diffuser transaction clé principale](assets/fr/27.webp)


交易會顯示在主畫面上，您的結餘也會更新。


![Solde après dépense](assets/fr/28.webp)


## 投資組合更新


如上所述，Liana Wallet 要求您定期在 Blockchain 上執行交易來更新您的資金。如果您沒有這樣做，您的資金可能會被您的繼承人（或在強化備份的情況下被您的第二台裝置）取回。這種情況並非極度危險，但卻有違設置此機制的目的：在不求助於可信賴的第三方的情況下，繼續控制您的比特幣，同時受益於安全網。


在您的資金 (或部分資金) 過期前會顯示警告，並可由復原金鑰支出。它會顯示您的「復原路徑」（*復原路徑*）即將可用。鑑於我們的復原時間很短（一小時），因此在我們的情況下會直接顯示此訊息。


![Avertissement chemin récupération](assets/fr/29.webp)


當截止日期臨近時，會出現一個按鈕提示您更新相關資金。


![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)


若要更新您的硬幣，請前往「*硬幣*」標籤，然後在對應的硬幣方塊中點擊「*刷新硬幣*」。如果您有多個錢幣，為了保密起見，您應該逐一刷新，而且間隔要相對較短。為了降低成本，您可以整合您的資金，將整個 Wallet 傳送至新的接收 Address，但這會影響您的機密性。


![Actualiser pièce](assets/fr/31.webp)


註明所需的交易費率。由於這是轉帳給自己，您可以設定相當低的費率，尤其是在到期前幾天轉帳。


![Transfert à soi-même](assets/fr/32.webp)


交易（標示為「*自行轉帳*」）只會在「*交易*」標籤中顯示。


![Transactions après auto-transfert](assets/fr/33.webp)


一旦確認，您的硬幣就安全了！在下一個到期日之前，您可以高枕無憂。


## Bitcoin 回收


從 Liana Wallet 復原資金時，您可能會面臨以下兩種情況之一。您可能可以存取安裝軟體的電腦，在這種情況下，您只需要開啟軟體即可（在增強備份型號的情況下會出現這種情況）。但是，您可能無法存取此電腦，因此我們在此從頭開始。請注意，兩種情況下的復原步驟相同。


若要開始使用，請從 [Wizardsardine 官方網站](https://wizardsardine.com/Liana/) 下載 Liana，或從 [GitHub 套件庫](https://github.com/wizardsardine/Liana/releases) 下載，您可以檢查軟體的真實性。安裝軟體並執行。我們使用的版本是 0.9，因此視覺效果可能有所改變。在歡迎畫面中，選擇「新增現有的 Liana Wallet」選項。


![Ajouter portefeuille existant](assets/fr/34.webp)


設定連接網路的方式。您可以選擇使用自己的節點（本機或遠端），或是使用 WizardSardine 的基礎架構。如果是後者，您需要 Wallet 創建者使用的電子郵件 Address，以便自動定位資金。如果您沒有這些資訊，請選擇第一個選項。


![Sélectionner connexion réseau](assets/fr/35.webp)


如果您使用自己的節點，請匯入 Wallet 描述符。這是帳戶的技術描述，可讓您擷取帳戶中持有的資金。在我們的案例中，它是以下資訊：


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


![Importer descripteur](assets/fr/36.webp)


Liana 接著會要求您輸入 Mnemonic 詞組。如果您有可用的簽章裝置 (Hardware Wallet)，請跳過這一部分。如果您的裝置遺失或損壞，但您有相對應的 12 或 24 個詞組，您仍然可以使用此選項。為了安全起見 (如果要復原的數量很高)，我們仍建議您取得新的 Hardware Wallet，然後用 Mnemonic 來復原上面的鑰匙。


在我們的案例中，我們使用 Blockstream Jade Hardware Wallet 作為復原裝置，並選擇跳過 ("*Skip*")此步驟。


![Passer phrase mnémotechnique](assets/fr/37.webp)


在螢幕上選擇簽章裝置，檢查並儲存簽章裝置中的描述符。如果您的 Hardware Wallet 沒有出現，請檢查是否已連線並解鎖。檢查並確認此資訊已加入您的裝置。


![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)


設定您的節點。您可以使用現有的節點，或在您的機器上安裝一個 * 經過修剪的節點*。在我們的案例中，我們使用現有的節點。


![Choisir type de nœud](assets/fr/39.webp)


在本教程中，我們使用公共的 Electrum 伺服器。然而，它可以存取我們使用 Liana Wallet 的所有活動。如果您想保護您的隱私，最好使用您自己的節點。


![Connexion serveur Electrum public](assets/fr/17.webp)


設定好節點後，您會進入 Wallet 的主畫面，在這裡您可以檢視帳戶餘額及與帳戶連結的過去交易。您也可以查看是否可以擷取資金。在這裡，我們看到可以擷取一個硬幣。


![Accueil Liana récupération](assets/fr/40.webp)


若要恢復 Wallet 中的資金，請前往左下方的 Settings（設定）（"*Settings*"），然後按一下「*Recovery*」。


![Récupération dans paramètres](assets/fr/41.webp)


勾選適當的方塊，在 Wallet 中花費硬幣。指出您希望發送資金到的 BTC Address，以及交易費率。然後點擊 「*下一步*」。


![Récupération des pièces](assets/fr/42.webp)


按一下「*簽署*」並在您的 Hardware Wallet 上驗證交易，以簽署交易。


![Signer transaction clé de récupération](assets/fr/43.webp)


然後按一下「*廣播*」，在網路上廣播。


![Diffuser transaction clé de récupération](assets/fr/44.webp)


交易應該會出現在主畫面上。一旦確認，復原就完成了！


![Écran principal après récupération](assets/fr/45.webp)


## 獎勵：描述符分析


描述符是一個可由人類讀取的字元字串，可詳盡描述一組位址。它結合了許多重要的資訊，可用於擷取進階 Wallet 的零件 (UTXO)。描述符的書寫方式以 [Miniscript syntax](https://bitbox.swiss/blog/understanding-Bitcoin-miniscript-part-2/) 為基礎，這是 Andrew Poelstra、Pieter Wuille 和 Sanket Kanjalkar 於 2019 年開發的腳本語言。


為了更好地理解為什麼這個字串很重要，讓我們分析一下範例中的描述符，它是 ：


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


可從此描述符擷取下列資訊：




- `wsh`（*見證腳本 Hash* 的縮寫）：這是建立的交易輸出類型。如果我們選擇使用 Taproot，識別符應該是 `tr`。
- `or_d`：這是一個邏輯運算符號，表示必須符合下列兩個*條件之一，才能接受支出 (`_d`表示特定的語法)。
- `pk`（*公鑰*的縮寫）：此運算符號會根據下列公開金鑰檢查指定的簽章，並將答案顯示為布林值 (TRUE 或 FALSE)。
- `[3689a8e7/48'/0'/0'/2']`:此元素包含主 Hardware Wallet (在此為 Nano S Plus) 的主密鑰的 * 指紋 *，以及連結擴充私密金鑰 (所有其他私密金鑰皆由此衍生) 的衍生路徑。
- `xpub6FKY ...WQa`：這是連結到主 Hardware Wallet (這裡是 Nano S Plus) 的擴充公開金鑰
- `/<0;1>/*`:這些是取得簡單金鑰和位址的衍生路徑： `0`用於接收，`1`用於內部作業 (*change*)，有一個 「通配符」 (`*`)，允許以可設定的方式依序衍生數個位址，類似於經典 Wallet 軟體的 "gap limit" 管理。
- and_v`：這是一個邏輯運算符號，表示*必須符合下列兩個*條件，支出才會被接受 (`_v`表示特定的語法)。
- `v:pkh`（*verify: public key Hash*的簡稱）：此運算符號針對後續的公開金鑰 Hash (*Hash*) 來驗證指定的簽章和公開金鑰。這基本上與 P2PKH 和 P2WPKH 腳本的檢查相同。
- `[42e629dd/48'/0'/0'/2']`:這是與上述相同的元素 (由追蹤路徑和衍生路徑所組成)，除了硬體復原 Wallet 的主密鑰 (在此為 Jade) 的追蹤路徑會被指出。
- `xpub6DpQ ...WQd`：這是與硬體復原 Wallet (這裡是 Jade) 連結的擴充公開金鑰。
- `older(6)` : 此運算符檢查所建立的交易輸出必須有嚴格大於 6 個區塊的年齡，才能使用。


最後一個資料項目 (`8alrve5h`)是描述符校驗和，對應於 Wallet 識別碼。


此 Wallet 所建立的腳本將採用下列形式：


```plaintext
<primary_key> CHECKSIG IFDUP NOTIF DUP HASH160 <recovery_key_hash> EQUALVERIFY CHECKSIGVERIFY <locktime> CHECKSEQUENCEVERIFY ENDIF
```


由於您的 Bitcoin Wallet 的安全性也取決於您對其工作原理的瞭解，因此我建議您參加 Plan ₿ Network 這個免費培訓課程，深入研究確定型錢包和分層錢包的機制：


https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f