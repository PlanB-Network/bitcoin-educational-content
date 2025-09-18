---
name: Samourai Wallet - Recover
description: 如何恢復卡在 Samourai Wallet 上的 bitcoins？
---

![cover](assets/cover.webp)


在 Samourai Wallet 的創辦人於 4 月 24 日被捕並其伺服器被扣押之後，該應用程式的某些功能現在無法運作，而沒有自己 Dojo 的使用者也無法再進行廣播交易。


在最近幾天協助了幾位使用者恢復他們的 bitcoins 之後，我相信我已經遇到了大部分在 Samourai Wallet 恢復過程中可能會發生的問題。因此，本教學將以狀況報告開始，以辨識 Samourai Wallet 生態系統內仍可運作的功能和已無法使用的功能，以及受此事件影響的軟體。接下來，我們將逐步使用 Sparrow Wallet 軟體來復原 Samourai Wallet。我們將檢查在此過程中遇到的所有潛在障礙，並查看解決方案。最後，在最後一部分，您將會發現伺服器被竊取之後，您的隱私可能面臨的風險。


_衷心感謝 [@Louferlou](https://twitter.com/Louferlou)，他協助多位使用者進行復原，並與我分享他的經驗，他也協助測試以確定哪些功能仍可使用。_


## Samourai Wallet 是否仍在運作？


是的，** Samourai Wallet 應用程式仍可使用**，但必須在特定條件下。


首先，該應用程式必須先前已安裝在您的智慧型手機上。Google Play 商店已移除該應用程式，而 APK 則託管在被查封的網站上。因此，目前安裝 Samourai 十分複雜。您可能會在線上找到 APK，但我建議不要下載，除非您確定來源。


鑑於 Samourai Wallet 頁面已不在 Google Play 商店中，因此無法停用自動更新。如果該應用程式回到下載平台，在獲得更多關於案件發展的資訊之前，**停用自動更新**是明智之舉。


如果您的智慧型手機上已經安裝 Samourai Wallet，您應該仍然可以存取該應用程式。要使用Samourai的Wallet功能，必須連接一個Dojo。在此之前，沒有個人Dojo的用戶只能依賴Samourai的伺服器來存取Bitcoin Blockchain的資訊和進行交易廣播。隨著這些伺服器被扣押，應用程式將無法再存取這些資料。

如果您之前沒有連接 Dojo，但現在有了，您可以將其設定為再次使用您的 Samourai 應用程式。這包括檢查您的備份、刪除 Wallet（Wallet，而非應用程式），然後透過連接您的 Dojo 到應用程式來恢復 Wallet。關於這些步驟的更多細節，您可以參考[本教學，在「_準備您的Samourai錢包_」部分：CoinJoin - DOJO](https://planb.network/tutorials/privacy/on-chain/coinjoin-dojo-c4b20263-5b30-4c74-ae59-dc8d0f8715c2)。

如果您的 Samourai 應用程式已經連接到您自己的 Dojo，那麼 Wallet 部分對您來說就可以完美運作。您仍然可以看到您的餘額和廣播交易。儘管發生了這些事情，我認為 Samourai Wallet 仍然是目前最好的行動 Wallet 軟體。就我個人而言，我打算繼續使用它。


您可能遇到的主要問題是無法從應用程式存取 Whirlpool 帳號。通常，Samourai會嘗試與您的Whirlpool CLI建立連線，並開始CoinJoin週期，然後才讓您存取這些帳號。然而，由於此連線已不再可能，應用程式會繼續無限期地搜尋，但卻無法讓您存取 Whirlpool 帳戶。在這種情況下，您可以在另一個 Wallet 軟體上恢復這些帳戶，而只保留 Samourai 上的存款帳戶。


### Samourai 上還有哪些工具？


另一方面，有些工具不是受到伺服器關機的影響，就是完全無法使用。


關於個人消費工具，只要您有自己的道場，一切都能正常運作。正常的石牆交易（而非石牆 x2）沒有任何問題。


Twitter 上的評論強調，「石牆 」交易提供的隱私現在可能會減少。石牆交易的附加價值在於，就結構而言，它與石牆 x2 交易無法區分。當分析師遇到這種特定模式時，他們無法判斷這是單一使用者的標準石牆交易，還是涉及兩個使用者的石牆 x2 交易。然而，正如我們將在以下段落中看到的，由於無法使用 Soroban，進行石牆 x2 交易變得更加複雜。因此，有些人認為，分析師現在可能會假設任何具有這種結構的交易都是正常的石牆交易。我個人並不同意這種假設。雖然石牆 x2 交易的頻率可能較低（我認為在這次事件之前就已經是了），但事實上，它們仍有可能發生，這可能會使基於它們不是石牆交易的假設而進行的整個分析失效。

**[-> 進一步瞭解石牆交易](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)**

關於 Ricochet，我無法證實這項服務是否仍在運作中，這是由於我在 Testnet 上並沒有自己的 Dojo，而且我寧願不冒險花 `100 000 Sats` 去購買可能會被官方控制的 Wallet。如果您最近有機會測試此工具，我邀請您與我聯絡，以便我們更新這篇文章。


如果您需要使用 Ricochet，請注意您可以隨時使用任何 Wallet 軟體手動執行此操作。若要學習如何手動正確執行各種跳轉，我建議您參考這篇其他文章：[**RICOCHET**](https://planb.network/tutorials/privacy/on-chain/ricochet-e0bb1afe-becd-44a6-a940-88a463756589)


JoinBot 工具已不再運作，因為它完全依賴 Samourai 管理的 Wallet 的參與。


至於其他類型的合作交易（通常稱為「cahoots」），它們仍然是可能的，但只能手動進行。在伺服器關閉之前，您有兩個選項來執行 Stonewall x2 或 Stowaway (PayJoin) 交易：



- 使用 Soroban 網路自動遠端 Exchange PSBT；
- 或透過掃瞄多個 QR 代碼手動執行這些交換。


經過多次測試後，Soroban 似乎已無法運作。因此，要執行這些協同交易，資料的 Exchange 必須手動完成。以下是執行此 Exchange 的兩個選項：



- 如果您與合作夥伴的距離很近，您可以連續掃描 QR 代碼；
- 如果您與合作者距離較遠，您可以透過應用程式的外部通訊管道 Exchange PSBT。不過，請務必小心，因為這些 PSBT 所包含的資料在隱私方面相當敏感。我建議使用加密訊息服務，以確保 Exchange 的機密性。


**[-> 瞭解更多關於石牆 x2 交易.](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)**


**[-> 進一步瞭解 Stowaway 交易。](https://planb.network/tutorials/privacy/on-chain/payjoin-samourai-wallet-48a5c711-ee3d-44db-b812-c55913080eab)**


至於 Whirlpool，協定似乎不再運作，即使是擁有自己 Dojo 的使用者也是如此。這幾天我一直在監控我的 RoninDojo，並嘗試進行一些基本操作，但自伺服器關閉後，Whirlpool CLI 就無法連線了。


不過，我仍然希望在未來幾週內，可以視情況的發展，重新啟動或以不同的方式重新構想這項協議。這次暫停可能是探索新方法或改善此系統潛力的機會。


### 還有哪些外部工具可用？


至於其他與 Samourai 環境相關的工具，有些仍然可用，有些則不可用。


很遺憾，免費的連鎖分析網站 OXT.me 暫時已無法使用。


Whirlpool Stats Tool 已不再提供下載，因為它寄存在 Samourai 的 GitLab 上。即使您之前已將此 Python 工具下載到您的本機，或已安裝在您的 RoninDojo 節點上，WST 也暫時無法運作。事實上，它的運作有賴於 OXT.me 所提供的資料，而這個網站已經無法存取。目前，WST 並不是特別有用，因為 Whirlpool 通訊協定已停止運作。


KYCP.org 網站目前已無法存取。


託管 Boltzmann Calculator Python 工具程式碼的 GitLab 也已被查封。因此，目前已無法下載此工具。但如果您有 RoninDojo，您可以像以前一樣繼續使用 Boltzmann Calculator。


至於 RoninDojo，儘管某些特定工具（如 Whirlpool CLI 和 WST）無法使用，但這個節點在盒中的軟體仍能繼續正常運作。由於 Fulcrum 或 Electrs 的緣故，它仍可用於其他 Wallet 軟體。如果您希望獲得更多關於 RoninDojo 的資訊，或是您有特定的問題，我鼓勵您加入 [他們的 Telegram 群組](https://t.me/RoninDojoNode)。


然而，RoninDojo 的原始碼目前已無法取得，因為它寄存在 Samourai 的 GitLab 上。因此目前無法在 Raspberry Pi 上手動安裝。


關於 Watch-only wallet 軟體 Sentinel，情況與 Samourai 應用程式類似。如果您有自己的 Dojo，您可以繼續使用 Sentinel 而不會有任何問題。但是，如果您沒有 Dojo，就無法再建立連線。與 Samourai 不同，Sentinel 網站仍可線上存取。但請謹慎使用此網站及其提供的 APK，因為目前還不清楚誰在控制這些資源。


### 麻雀 Wallet 是否受到影響？


Sparrow Wallet 繼續正常運作，除了 Samourai 工具不再可用。目前，已無法透過 Sparrow 執行硬幣接合。同樣地，協同花費工具也無法再使用，因為 Sparrow 與 Samourai 不同，不提供 PSBT 手動 Exchange 的選項。至於所有其他功能，Sparrow 的操作都沒有問題。必要時，您也可以使用此軟體復原 Samourai Wallet。


## 如何復原 Samourai Wallet？


正如我們在前幾節所看到的，如果您擁有自己的道場，不一定需要轉換軟體。 **Samourai仍然是您日常消費Hot Wallet**的絕佳選擇。然而，如果您沒有道場，或是您偏好選擇其他軟體，我將為您說明完整的恢復過程，詳細說明您可能遇到的任何潛在障礙。


在任何情況下，重要的是要慢慢來，並確保不犯任何錯誤。請記住，不要著急，因為您持有您的私人密碼匙，Samourai 伺服器被扣押並不會對您的私人密碼匙造成任何影響。無論發生什麼事，他們顯然無法存取您的私人密碼匙。


### 驗證 passphrase


要復原您的 Wallet，您必須有您的 passphrase，即使您選擇透過備份檔案進行復原。首先驗證這個passphrase的有效性。打開您的Samourai Wallet應用程式，點擊左上方的Paynym圖標，然後選擇`Settings`。


![samourai](assets/1.webp)


接下來，按一下「疑難排解」，然後按一下「passphrase/備份測試」。


![samourai](assets/2.webp)


輸入您的 passphrase，然後按一下`Ok`。如果正確，Samurai 會確認。如果您打算稍後再使用備份檔案，您也可以選擇確認。


![samourai](assets/3.webp)


此步驟是可選的，但建議使用。它可以確認 passphrase 正確無誤，消除日後出現問題的潛在來源。如果 Samourai 在此階段顯示 passphrase 不正確，則無法恢復。請確認您已正確輸入 passphrase，並再次檢查。


### 選項 1：使用備份檔案復原 Sparrow 上的 Wallet


自Sparrow Wallet的1.8.6版本起，您可以使用您的應用程式自動產生的備份文字檔`samourai.txt`直接匯入您的Samourai Wallet。此檔案包含復原您的 Wallet 所需的所有資訊，並與您的 passphrase 加密以策安全。


如果您選擇此選項，您將需要最新的 `samourai.txt` 檔案和您的 passphrase。若要在 Samourai Wallet 上 generate 此檔案，請按一下右上方的三個小點，然後選擇`匯出 Wallet 備份`。


![samourai](assets/4.webp)

接下來，選擇「匯出至剪貼簿」。之後，您需要將這個檔案安全地傳輸到您的電腦。由於檔案已加密，但僅 passphrase 就足以將其解密，因此在傳輸過程中必須採取預防措施。如果您選擇以純文字直接傳輸，您需要在電腦上建立一個 `samourai.txt` 檔案，並將剪貼板的內容貼入其中。另一個選擇是直接從您手機上儲存的檔案中擷取 `samourai.txt` 檔案。

在電腦上取得檔案後，開啟 Sparrow Wallet，按一下「檔案」標籤，然後選擇「匯入 Wallet」，開始匯入您的 Wallet。


![samourai](assets/5.webp)


向下捲動到`Samourai Backup`，按一下`Import File`，然後選擇您的`samourai.txt`檔。


![samourai](assets/6.webp)


之後 Sparrow 會要求您輸入密碼來解密檔案。這個密碼其實就是您的 passphrase。在相應的欄位中輸入，然後點擊 `導入`。


![samourai](assets/7.webp)


如果在此階段，您的 Wallet 沒有出現，可能是您在複製 `samourai.txt` 檔案或輸入 passphrase 時出錯。您可以參閱疑難排解部分以獲得更多幫助。


![samourai](assets/8.webp)


對於腳本類型，如果您沒有在 Samourai 設定其他腳本，通常應該只使用 SegWit V0 (Native SegWit / P2WPKH)。保留這個預設腳本，然後點選 `Import`。


![samourai](assets/9.webp)


為您的 Wallet 命名，例如「Samourai Recovery」，然後按一下「建立 Wallet」。


![samourai](assets/10.webp)


然後 Sparrow 會要求您選擇一個密碼。此密碼僅能保護您在此電腦上存取 Wallet，與 Wallet 金鑰的衍生無關。請務必選擇一個強大的密碼，並記下來以便於記憶，然後點擊 "Set Password"（設定密碼）。


![samourai](assets/11.webp)


之後，Sparrow 會得出您的 Wallet 的鑰匙，並搜尋相對應的交易。


![samourai](assets/12.webp)


目前，只有您的存款帳戶可以存取。如果您只使用 Samourai 這個帳戶，您應該可以看到您所有的資金。但是，如果您也在使用 Whirlpool，您需要衍生出 `premix`、`postmix` 和 `badbank` 帳戶。在 Sparrow 上，只需點擊「設定」標籤，然後點擊「新增帳戶...」。


![samourai](assets/13.webp)

在開啟的視窗中，從下拉式功能表中選擇「Whirlpool 帳戶」，然後按一下「確定」。

![samourai](assets/14.webp)


然後您會看到您的各種 Whirlpool 帳戶出現，Sparrow 會得出使用相關比特幣所需的金鑰。


![samourai](assets/15.webp)


如果您使用不同於 Sparrow 的軟體，例如 Electrum，來復原您的 Samourai Wallet，以下是手動復原的 Whirlpool 帳號索引：



- 存款： `m/84'/0'/0'`
- 壞銀行`m/84'/0'/2147483644'`
- 預混合：`m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`


現在您可以在 Sparrow 上存取您的比特幣了。如果您在使用 Sparrow Wallet 時需要幫助，也可以查看 [我們的專用教學](https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)。


我也建議您在 Samourai 上手動匯入與您的 UTXO 相關的標籤。這可讓您隨後在 Sparrow 上執行有效的硬幣控制。


### 方案 2：用 Mnemonic 短語恢復 Sparrow 上的 Wallet


如果您不想使用備份檔案執行復原，您可以選擇更傳統的方法，只需使用 12 個字的復原短語和您的 passphrase。第二個選項通常比較簡單。


開始時，請確定您手邊有復原短語和 passphrase。然後，開啟 Sparrow Wallet 軟體，點選「檔案」標籤，並選擇「匯入 Wallet」，開始匯入您的 Wallet。


![samourai](assets/16.webp)


選擇「Mnemonic Words (BIP39)」，並在下拉式功能表中，點選「Use 12 Words」。


![samourai](assets/17.webp)


以正確的順序輸入 12 個復原詞組。


![samourai](assets/18.webp)


如果 Sparrow 顯示「無效校驗和」訊息，表示復原詞組的校驗和無效，這可能表示您在輸入詞組時出錯。


![samourai](assets/19.webp)


如果您的詞組正確，請勾選 `使用 passphrase?`方塊，並在專用欄位中輸入您的 passphrase。最後，如果一切似乎都正確，請按一下 `Discover Wallet` 按鈕。


![samourai](assets/20.webp)


為您的 Wallet 命名，例如「Samourai Recovery」，然後按一下「建立 Wallet」。


![samourai](assets/21.webp)

之後 Sparrow 會要求您選擇一個密碼。此密碼只保護您在此電腦上存取 Wallet 的權限，與 Wallet 金鑰的衍生無關。請務必選擇一個強大的密碼，寫下來以方便記憶，然後點選 `Set Password`。

![samourai](assets/22.webp)


Sparrow 接著會推導出您 Wallet 的金鑰，並搜尋相對應的交易。


![samourai](assets/23.webp)


如果在此階段，您的 Wallet 沒有出現，可能是您在輸入 passphrase 或復原短語時出錯。您可以參考專門的疑難排解章節以獲得更多幫助。


目前，只有您的存款帳戶可以存取。如果您只使用 Samourai 這個帳戶，您應該可以看到您所有的資金。但是，如果您也在使用 Whirlpool，您需要衍生出 `premix`、`postmix` 和 `badbank` 帳戶。在 Sparrow 上，只需點擊「設定」標籤，然後點擊「新增帳戶...」。


![samourai](assets/24.webp)


在開啟的視窗中，從下拉式清單中選擇「Whirlpool 帳戶」，然後按一下「確定」。


![samourai](assets/25.webp)


然後您會看到您的各個 Whirlpool 帳戶出現，Sparrow 會得出使用相關比特幣所需的金鑰。


![samourai](assets/26.webp)


如果您使用其他軟體如 Electrum 來復原您的 Samourai Wallet，以下是手動復原的 Whirlpool 帳號索引：



- 存款： `m/84'/0'/0'`
- 壞銀行`m/84'/0'/2147483644'`
- 預混合：`m/84'/0'/2147483645'`
- Postmix: `m/84'/0'/2147483646'`


現在您可以在 Sparrow 上存取您的比特幣了。如果您在使用 Sparrow Wallet 時需要幫助，也可以參考 [我們的專用教學](https://planb.network/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d)。


我也建議您在 Samourai 上手動匯入與您的 UTXO 相關的標籤。這可讓您隨後在 Sparrow 上執行有效的硬幣控制。


### 遇到的常見問題有哪些？


在過去幾天協助了幾個人之後，我相信我已經解決了大部分可能會讓您的 Wallet 無法復原的問題。如果您在使用之前的教學後仍然無法存取您的 Wallet，以下是一些額外的建議。

首先，也是最重要的是，要使復原成功，復原短語的正確性是絕對重要的。如果您無法找到您的12字短語，您可以使用_選項1_從Samourai的備份檔案中恢復。您也可以直接在Samourai Wallet中進入 "Settings「，然後選擇 」Wallet「，最後選擇 」Show 12-word recovery phrase"。


接下來，如果您的 passphrase 在復原過程中出現打字錯誤，將導致衍生鍵不正確，無法在 Sparrow 上復原您的 Wallet。 **passphrase必須完全正確！**


要解決這個問題，我首先建議您在 Samourai 應用程式中檢查 passphrase 的有效性，如本文「_驗證密碼_」部分所述：


1. **在 Samourai 中驗證：** 如果 Samourai 確認 passphrase 正確無誤，請從頭再試一次復原，確保在 Sparrow 中準確無誤地輸入 passphrase；

2. **passphrase 錯誤：** 如果 Samourai 顯示 passphrase 不正確，則繼續嘗試 Sparrow 是沒有意義的。只要找不到正確的 passphrase，就不可能復原您的 Wallet。如果您已永久遺失 passphrase，請妥善保管您的 Samourai 應用程式。您所能做的就是希望伺服器重新啟動，這樣您就可以直接從應用程式進行支出，而不需要復原。 **在此情況下，請勿嘗試連線道場**，因為這意味著要在 Samourai 上重新設定您的 Wallet，而這需要存取 passphrase。


在其他遇到的錯誤中，許多都與 Sparrow 上的網路設定有關。


首先，確保 Sparrow 正確設定在 `Mainnet` 模式，而非 `Testnet` 模式。事實上，如果 Sparrow 在 Testnet 上搜尋您的交易，它什麼也找不到，因為您的 Wallet 是在 Mainnet 上。Testnet 是 Bitcoin 的另一個版本，僅用於測試和開發，在主網絡 (Mainnet) 之外的獨立網絡上運行，有自己的區塊和交易。若要檢查您在哪個網路，請按一下 `Tools` 標籤，然後按一下 `Restart In`。如果顯示 `Mainnet` 選項，表示您不在主網路上。選擇它以在 Mainnet 上重新啟動 Sparrow，然後再開始您的復原程序。


![samourai](assets/27.webp)

有些人在連接 Sparrow 到節點時也遇到困難。在 Sparrow 的右下方，有一個彩色的開關，表示您的軟體是否正確地連接到 Bitcoin 節點。要檢索您的 Samourai 交易，軟體必須連接良好。請檢查開關是否啟動，如下圖所示（黃色代表公共節點，Green 代表 Bitcoin Core，藍色代表 Electrum 伺服器）。

![samourai](assets/28.webp)


如果開關未啟動，請按一下以重新啟動連線。


![samourai](assets/29.webp)


如果問題仍然存在，以下是一些可能的解決方案：



- 如果您嘗試連線到您自己的 Electrum 伺服器 (藍色) 或您的 Bitcoin Core (Green)，而 Sparrow 無法連線，請檢查`檔案 > 偏好設定... > 伺服器`下的連線資訊。> 伺服器`；


![samourai](assets/30.webp)



- 如果連線問題持續，可能是因為您的節點未完全同步化。確保您的節點和索引器 100% 同步。如有必要，作為最後的手段，請中斷您的節點與 Sparrow 的連線，並連線至公共節點；
- 如果您已經連線到公用節點，但連線失敗，請嘗試從下拉清單中選擇另一個節點，以變更節點。


![samourai](assets/31.webp)


如果您已成功復原 Wallet，但看起來不完整，可能是與衍生有關的問題。


如果您使用的Samourai存款帳戶的腳本類型與`P2WPKH`不同，可能會發生問題。在預設情況下，Samourai 使用這種腳本類型，但如果您手動更改了腳本類型，在 Sparrow 上復原時也必須調整。


若要衍生其他腳本類型的分支，您需要針對每個使用的腳本類型重複復流程。為此，請移至 Sparrow 上的「檔案 > 新增 Wallet」，從下拉式清單中選擇另一種腳本類型，按一下「新增或匯入 Software Wallet」，並遵循與初始教學相同的步驟。


![samourai](assets/32.webp)


我遇到的另一個衍生問題與 Gap Limit 值有關。這個值會告訴 Sparrow 在多少個空位址之後，就應該停止衍生新的位址。如果在恢復後，您發現有些交易丟失了，這可能是由於 Gap Limit 太低造成的。要解決這個問題，請進入造成問題的帳戶，例如，postmix 帳戶（如果涉及多個帳戶，請對每個帳戶重複此操作）。


![samourai](assets/33.webp)


按一下「設定」索引標籤，然後按一下「進階...」按鈕。

![samourai](assets/34.webp)

逐漸增加 Gap Limit 的值，例如，我在這裡設定為 `400`。然後按一下 `Close` 按鈕。


![samourai](assets/35.webp)


點擊 「應用 」完成。之後，Sparrow 會衍生出更多地址，並在這些地址上搜尋資金，這應有助於恢復您的所有交易。


![samourai](assets/36.webp)


這包括了過去幾天我所遇到的各種復原問題。如果在嘗試所有這些解決方案之後，您還是有問題，我邀請您加入 [Discover Bitcoin Discord](https://discord.gg/xKKm29XGBb) 尋求協助。我定期訪問這個 Discord，如果我有解決方案，我很樂意提供幫助。其他比特幣玩家也可以分享他們的經驗並提供協助。 **在任何情況下，必須對您的復原短語、備份檔案和您的 passphrase 保密**。不要與任何人分享，因為這可能會讓他們盜取您的比特幣。


一旦復原完成，您現在就可以存取您的比特幣了。這是件好事，但可能還不夠。事實上，伺服器被扣押為您的隱私帶來了新的潛在風險。在下一節中，我們將詳細研究這些風險，並概述保護您的隱私應採取的預防措施。


## 對您的交易隱私有什麼影響？


### 身為沒有 Dojo 的 Samourai 使用者


如果您使用 Samourai Wallet 而沒有連上自己的 Dojo，您的 xpub 必須傳送到 Samourai 的伺服器，應用程式才能運作。隨著這些伺服器被扣押，有可能官方現在可以存取這些 xpubs。


此情況仍屬假設。我們不知道這些 xpub 是否被記錄下來，是否有任何潛在的儲存空間被毀壞，當局是否已恢復這些 xpub，以及他們是否打算使用這些 xpub 來進行連鎖分析。然而，在這種情況下，為了謹慎起見，我們應該考慮最壞的情況，即官方擁有沒有連接自己 Dojo 的使用者的 xpub。

作為參考，xpub 是一個字符串，包含所有生成子公開金鑰所需的 Elements (公開金鑰 + 鏈碼)。它用於分層式確定性錢包中，以 generate 接收地址並觀察帳戶的交易，而不會暴露相關的私密金鑰。舉例來說，這允許建立一個「只供觀察」的 Wallet。然而，公開 xpubs 可能會損害使用者的隱私，因為它們允許第三方追蹤交易並查看相關帳戶的餘額。

因此，任何知道您 xpub 的人都可以看到您 Wallet 的所有接收位址，包括過去使用過的位址，以及將來產生的位址。


對於沒有 Dojo 的使用者來說，您的 xpubs 可能洩漏會有兩個主要後果：



- 從隱私權的角度來看，任何知道您 xpubs 的人都無法看到您所執行的硬幣接合，因此您的硬幣將失去所有隱私權；
- 此人也可以追蹤您的 Samourai Wallet 的所有收件地址。


因此，重要的是要考慮最壞的情況，並放棄這台可能洩露隱私的 Wallet。要做到這一點，請使用其他軟件（如 Sparrow Wallet）從頭開始創建一個新的 Wallet。驗證備份的有效性後，透過交易轉移所有資金。雖然此操作不會破壞您的錢幣的可追蹤性鏈接，但它會阻止當局確定地知道您的新 Wallet 的地址。


在此轉移操作中，我建議避免鞏固您的硬幣。如果我們假設您的 xpub 已經被洩露，那麼從可以訪問這些 xpub 的人的角度來看，合併將不會有任何影響，因為您的隱私已經被這些 xpub 洩露。然而，我建議您不要過度鞏固您的硬幣，主要是為了保護您的隱私不被他人竊取。在最壞的情況下，可能只有當局可以訪問您的xpubs，但世界上其他人不知道他們。因此，從其他人的角度來看，因為通用輸入 Ownership 啟發式（CIOH），整合您的硬幣可能會大大損害您的隱私。


**Note:** 為了徹底打破追蹤，您也可以考慮從這個新的 Wallet 執行共同接合。

**警告：** 僅僅在 Sparrow Wallet 上復原您的 Samourai Wallet 是不夠的。如果您想避免使用可能已經洩漏的 xpubs，就必須以新的復原短語建立全新的 Wallet。如果您將現有的 seed 匯入 Sparrow，您只是改變了 Wallet 的管理軟體，但 Wallet 仍然是一樣的。


### 身為使用 Dojo 的 Sparrow 或 Samourai 使用者


如果您的 Wallet 只在 Sparrow Wallet 上管理，無論您使用的是公共節點還是您自己的 Bitcoin 節點，您的 xpubs 都不可能洩漏。同樣地，如果您使用的是 Samourai 應用程式，而且自從您的 Wallet 建立以來就一直將這個應用程式連接到您自己的 Dojo，那麼您的 xpub 也是安全的。


然而，如果您在**沒有自己的 Dojo** 期間使用了相同的 Wallet，然後又使用了自己的 Dojo，那麼 Samourai 伺服器可能已經存取了您的 xpub，因此官方可能會知道這些 xpub。如果您處於這種特定情況，我建議您遵循上一節的建議，並將您的 xpub 視為已被洩露。


對於那些一直使用 Sparrow 或 Samourai 並擁有自己 Dojo 的人來說，主要的風險是您的錢幣的 anonsets 可能會減少。假設在最壞的情況下，所有沒有 Dojo 的使用者都將他們的 xpubs 交到官方手中，那麼他們的錢幣在 CoinJoin 循環中的路徑可能會被這些官方追蹤。


為了說明這一點，讓我們舉一個具體的例子。假設您參加了 CoinJoin 的第一個週期，接著又參加了兩個下游的 CoinJoin 週期。如果沒有 Dojo 的使用者的 xpubs 沒有洩漏，那麼您的硬幣的潛在 anonset 將是 13。


![samourai](assets/37.webp)


然而，如果我們考慮到 xpubs 已經洩漏，而且您在最初的 CoinJoin 期間遇到一個沒有道場的使用者，然後在第一個下游的 CoinJoin 期間遇到 2 個，那麼從權威的角度來看，您的潛在 anonset 只會是 10 而不是 13。


![samourai](assets/38.webp)

這種潛在的停滯時間減少很難量化，因為它取決於許多因素，而且每個硬幣受到的影響都不同。舉例來說，在早期週期遇到沒有 Dojo 的使用者，其對潛在 anonset 的影響遠大於在後期週期遇到的使用者。為了讓您對這種情況有所瞭解（這仍然是假設的情況），Samourai 提供的最新統計資料顯示，涉及 Coinjoins 的硬幣有 85% 到 90% 來自使用 Dojo、Sparrow 或 Bitcoin Keeper 的用戶，也就是說，即使在最壞的情況下，這些用戶也不會看到他們的 xpubs 被洩露。

儘管這些數字很難驗證，但在我看來是一致的，原因有二：



- Sparrow Wallet 被廣泛使用；
- 大多數的 node-in-box 軟體都提供 Dojo 實作，而這些主流軟體如 Umbrel 現在非常流行。


因此，需要考慮幾個方面。如果您非常重視您的錢幣在官方面前的隱私，那麼為了謹慎起見，您應該為最壞的情況做好準備，而且很難保證 100％ 您的 Whirlpool CoinJoin 循環不會因為沒有 Dojo 的用戶可能洩露 xpubs 而被追蹤到。雖然這種假設的可能性極低，但並非不可能。


另一方面，如果您的硬幣隱私權對於可能擁有這些 xpubs 的權限並不重要，則可以不同的方式來考慮情況。


我指定「相對於當局」是因為必須記住，只有查封伺服器的當局才有可能知道這些 xpub。如果您使用 CoinJoin 的目的是要防止您的烘焙師能跟進您的資金，那麼他的資訊不會比伺服器被扣押之前更好。


最後，在伺服器被扣押之前，考慮您的硬幣的初始onset是非常重要的。讓我們以一個已經達到 40,000 的潛在 anonset 的錢幣為例；這個 anonset 的潛在減少可能是微不足道的。事實上，在基礎 anonset 已經非常高的情況下，沒有 Dojo 的幾個用戶不太可能從根本上改變情況。但是，如果您的硬幣的 anonset 是 40，那麼這個潛在的洩漏可能會嚴重影響您的 anonsets，並可能允許追蹤。

隨著 OXT.me 的關閉，WST 工具已經停止服務，您只能估算這些 anonsets。對於回溯的 anonset，沒有太多需要擔心的，因為 Whirlpool 模型確保它從第一個 CoinJoin 起就非常高，這要歸功於您的同行遺產。唯一可能造成問題的情況是，如果您的錢幣已經幾年沒有再混合，而且是在一個池子推出之初混合的。關於潛在的停用時間，您可以檢查您的代幣可供加入代幣的時間。如果已經有幾個月了，那麼它可能有一個非常高的潛在anonset。相反，如果它是在伺服器被查封前幾個小時才被加入的，那麼它的潛在失效時間可能非常低。

[**-> 詳細瞭解 anonsets 及其計算方法。**](https://planb.network/tutorials/privacy/analysis/wst-anonsets-0354b793-c301-48af-af75-f87569756375)


另一個需要考慮的方面是合併對已混合的錢幣的anonsets的影響。鑒於 Whirlpool 帳戶已無法透過 Samourai 應用程式存取，很可能有許多使用者已將 Wallet 轉移到其他軟體，並嘗試從 Whirlpool 提取資金。特別是在上週末，當 Bitcoin 網路的交易費用相對較高時，有強烈的技術和經濟誘因去鞏固混合後的硬幣。這意味著可能有很多用戶進行了大量的整合。


這些混合後合併的問題在於它們總是會降低 anonsets，不僅是對執行這些合併的使用者而言，對於他們在 CoinJoin 循環期間所遇到的使用者也是如此。雖然我無法精確地驗證或量化這個現象，但當時與交易費用相關的經濟誘因，可以讓我們假設 anonsets 有可能會降低。


### 身為哨兵使用者


Watch-only wallet 應用程式 Sentinel 的網路操作與 Samourai 相似。要存取您的 Wallet 資訊，應用程式必須傳送您提供的 xpub、公開金鑰和位址到 Dojo。如果您一直在 Sentinel 上使用自己的 Dojo，就沒有問題，您可以放心繼續使用應用程式。但是，如果您的 Sentinel 一直依賴 Samourai 的伺服器，您的 xpubs 就有可能已經暴露。在此情況下，建議您在連線至 Samourai 伺服器時，遵循針對 Samourai Wallet 所建議的相同 Wallet 變更程序。


如果您的道場使用 Samourai，但不使用 Sentinel，那麼您最好考慮您的 xpub 已經損壞。


## 總結


感謝您將本文閱讀完畢。如果您認為有遺漏的資訊，或是您有任何建議，請不要猶豫，立即與我聯絡，分享您的想法。此外，如果您需要更多的協助來復原您的 Samourai Wallet，儘管有這篇教學，我邀請您加入 [發現 Bitcoin Discord](https://discord.gg/xKKm29XGBb) 來尋求協助。我會定期訪問這個 Discord，如果我有解決方案，我很樂意幫助您。其他比特幣玩家也可以分享他們的經驗並提供支援。 **在任何情況下，必須對您的復原短語、備份檔案和您的 passphrase 保密**。不要與任何人分享，因為這可能會使他們盜取您的比特幣。