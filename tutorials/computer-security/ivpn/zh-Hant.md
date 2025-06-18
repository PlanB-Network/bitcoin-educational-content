---
name: IVPN
description: 設定以比特幣支付的 VPN
---
![cover](assets/cover.webp)


VPN (「*虛擬私人網路*」) 是一種服務，可在您的手機或電腦與 VPN 供應商管理的遠端伺服器之間建立安全且加密的連線。


技術上來說，當連線到 VPN 時，您的網際網路流量會透過加密隧道重新導向到 VPN 伺服器。此過程令第三方（如互聯網服務供應商 (ISP) 或惡意行為者）很難截取或讀取您的資料。VPN 伺服器接著會扮演中介的角色，代表您連線到您想要使用的服務。它會為您的連接分配一個新的 IP Address，這有助於向您訪問的網站隱藏您的真實 IP Address。然而，與某些線上廣告所暗示的相反，使用 VPN 並不能讓您匿名瀏覽網際網路，因為這需要對 VPN 供應商的一種信任，因為他們可以看到您的所有流量。

![IVPN](assets/fr/01.webp)

使用 VPN 有許多好處。首先，只要 VPN 供應商不分享您的資訊，就能保護您的線上活動隱私不受 ISP 或政府的干擾。其次，它可以保護您的資料安全，尤其是當您連線到容易受到 MITM（中間人）攻擊的公共 Wi-Fi 網路時。第三，透過隱藏您的 IP Address，VPN 可讓您繞過地理限制和審查，存取您所在區域無法存取或封鎖的內容。


如您所見，VPN 將流量觀察的風險轉移給 VPN 供應商。因此，在選擇 VPN 供應商時，必須考慮註冊所需的個人資料。如果提供商要求提供您的電話號碼、電子郵件 Address、銀行卡詳細資料，或者更糟糕的是您的郵政 Address，則會增加將您的身份與您的流量聯繫起來的風險。如果提供商受到攻擊或被依法扣押，很容易將您的流量與您的個人資料聯繫起來。因此，建議選擇不需要任何個人資料且接受匿名付款（如使用比特幣）的供應商。


在本教程中，我介紹了一個簡單、高效、價格合理的 VPN 解決方案，使用時不需要任何個人資訊。


## IVPN 簡介


IVPN 是專為尋求隱私的使用者所設計的 VPN 服務。與 YouTube 上經常宣傳的流行 VPN 供應商不同，IVPN 以其透明度、安全性和對隱私的尊重而脫穎而出。

IVPN 的隱私政策非常嚴格：註冊時不需要提供任何個人資訊。您可以在不提供電子郵件Address、姓名或電話號碼的情況下開設帳戶。付款時，不需要輸入信用卡資料，因為 IVPN 接受比特幣付款（onchain 和 Lightning）。此外，IVPN 聲稱不保留任何活動日誌，這意味著，理論上，該公司不會記錄您的互聯網流量。

IVPN 也是 [完全開放原始碼](https://github.com/ivpn)，關於其軟體、應用程式，甚至他們的網站，允許任何人驗證和檢閱他們的程式碼。他們每年也會進行獨立的安全稽核，稽核結果會公佈在他們的網站上。


IVPN 獨家使用自行託管的伺服器，因此消除了使用 AWS、Google Cloud 或 Microsoft Azure 等協力廠商雲端服務的相關風險。


該服務提供許多先進功能，例如多跳功能，可將流量透過位於不同司法管轄區的多個伺服器路由，以提高匿名性。IVPN 還整合了追蹤器和廣告封鎖程式，並提供不同 VPN 通訊協定的選擇。


當然，這種服務品質是有成本的，但足夠的價格通常是品質和誠信的指標。它可能是一個信號，表明該公司有一個不需要出售個人資料的商業模式。IVPN 隨後提供 2 種計劃：標準計劃，最多可連接 2 台裝置；專業計劃，最多可連接 7 台裝置，並包含「*Multi-hop*」協定，可透過多台伺服器路由您的流量。


與主流 VPN 供應商不同，IVPN 採用購買服務存取時間的模式運作，而非經常性訂閱。您只需為所選的使用時間支付一次比特幣。例如，如果您購買一年的訪問時間，您可以在該期間使用服務，之後您需要返回 IVPN 網站購買更多的訪問時間。


IVPN 價格](https://www.ivpn.net/en/pricing/) 依購買的存取時間長短而漸進。以下是標準計劃的價格：


- 1 週$2
- 1 個月$6
- 1 年：$60
- 2 年：100 美元
- 3 年：$140


至於 Pro 計劃：


- 1 週$4
- 1 個月$10
- 1 年：100 美元
- 2 年：160 美元
- 3 年：$220


## 如何在電腦上安裝 IVPN？

為您的作業系統下載[軟體的最新版本](https://www.ivpn.net/en/apps-windows/)，然後根據安裝精靈中的步驟進行安裝。！[IVPN](assets/notext/02.webp)

Linux 使用者請參閱 [this page](https://www.ivpn.net/en/apps-linux/) 上針對您的發行版所提供的說明。

![IVPN](assets/notext/03.webp)

安裝完成後，您需要輸入您的帳戶 ID。我們將在本教學的以下部分瞭解如何取得。

![IVPN](assets/notext/04.webp)

## 如何在智慧型手機上安裝 IVPN？


從您的應用程式商店下載IVPN，無論是iOS用戶的[AppStore](https://apps.apple.com/us/app/ivpn-secure-vpn-for-privacy/id1193122683)，Android用戶的[Google Play Store](https://play.google.com/store/apps/details?id=net.ivpn.client)，還是[F-Droid](https://f-droid.org/en/packages/net.ivpn.client)。如果您使用 Android，您也可以選擇直接從 [IVPN 網站](https://www.ivpn.net/en/apps-android/) 下載`.apk`檔。

![IVPN](assets/notext/05.webp)

首次使用應用程式時，您將會登出。您需要輸入您的帳戶 ID 來啟動服務。

![IVPN](assets/notext/06.webp)

現在，讓我們繼續在您的裝置上啟動 IVPN。


## 如何支付和啟用 IVPN？


前往 IVPN 官方網站 [付款頁面](https://www.ivpn.net/en/pricing/)。

![IVPN](assets/notext/07.webp)

選擇最適合您需求的方案。在本教程中，我們將選擇標準方案，它允許我們在電腦和智慧型手機等設備上啟用 VPN。

![IVPN](assets/notext/08.webp)

然後 IVPN 將建立您的帳戶。您不需要提供任何個人資料。只有您的帳戶ID將允許您登錄。它的作用有點像一個訪問鑰匙。保存在一個安全的地方，例如您的密碼管理器。您也可以複製一份紙本。

![IVPN](assets/notext/09.webp)

在同一頁面上，選擇您訂閱服務的期限。

![IVPN](assets/notext/10.webp)

然後選擇您的付款方式。就我而言，我將透過 Lightning Network 付款，因此我按一下「*Bitcoin*」按鈕。

![IVPN](assets/notext/11.webp)

檢查一切是否符合您的要求，然後按一下「*使用閃電付款*」按鈕。

![IVPN](assets/notext/12.webp)

一個Lightning Invoice將在他們的BTCPay伺服器上顯示給您。用您的 Lightning Wallet 掃描 QR 代碼，然後進行支付。

![IVPN](assets/notext/13.webp) Once the invoice is paid, click on the "*Return to IVPN*" button.

![IVPN](assets/notext/14.webp)

您的帳戶現在顯示為 "*Active*"，您可以看到您存取 VPN 的有效日期。在此日期之後，您需要重新付款。

![IVPN](assets/notext/15.webp)

要在電腦上透過 IVPN 啟用連線，只需複製您的帳號 ID 即可。

![IVPN](assets/notext/16.webp)

並將其貼到之前下載的軟體中。

![IVPN](assets/notext/17.webp)

然後按一下「*登入*」按鈕。

![IVPN](assets/notext/18.webp)

按一下核取標記以啟動 VPN 連線，就這樣，您電腦的網際網路流量現在已透過 IVPN 伺服器加密和路由。

![IVPN](assets/notext/19.webp)

對於您的智能手機，程序是相同的。粘貼您的帳戶 ID 或掃描與您的 IVPN 帳戶相關的 QR 代碼。然後點擊核取標記建立連接。

![IVPN](assets/notext/20.webp)

## 如何使用和設定 IVPN？


就使用和設定而言，相當簡單。從主 Interface，您只需使用核取標記即可啟用或停用連線。

![IVPN](assets/notext/21.webp)

您也可以選擇在特定時間內暫停 VPN。

![IVPN](assets/notext/22.webp)

按一下目前的伺服器，您可以從可用的伺服器中選擇另一個伺服器。

![IVPN](assets/notext/23.webp)

也可以啟動或關閉整合式防火牆以及防追蹤功能。

![IVPN](assets/notext/24.webp)

若要存取其他設定，請按一下設定圖示。

![IVPN](assets/notext/25.webp)

在「*帳戶*」標籤中，您可以找到與帳戶相關的設定。

![IVPN](assets/notext/26.webp)

在「*一般*」標籤中，有幾個用戶端設定。我建議您勾選「*自動連線*」中的「*登入時啟動*」和「啟動時*」選項，以便在啟動電腦時自動與 VPN 建立連線。

![IVPN](assets/notext/27.webp)

在「*連線*」標籤中，您可以找到與連線相關的各種選項。您可以在此變更所使用的 VPN 通訊協定。

![IVPN](assets/notext/28.webp)

*IVPN 防火牆*」標籤允許您在電腦啟動時系統地啟動防火牆，確保在 VPN 外部不會建立任何連線。

![IVPN](assets/notext/29.webp)

*Split Tunnel*" 標籤提供從 VPN 連線排除某些軟體的可能性。即使啟用 VPN，在此新增的應用程式仍可繼續以一般網際網路連線運作。

![IVPN](assets/notext/30.webp)

在「*WiFi 控制*」標籤中，您可以選擇根據所連接的網路設定特定動作。例如，您可以將您的家庭網路指定為「*受信任*」，並設定 VPN 不會在此網路啟動，但會在任何其他 WiFi 網路上自動啟動。

![IVPN](assets/notext/31.webp)

在「*反追蹤器*」功能表中，選擇反追蹤器的封鎖設定檔。此功能可在您瀏覽網際網路時，透過封鎖向追蹤服務提出的請求，來封鎖廣告、惡意軟體和資料追蹤程式。這可以防止公司收集和出售您的瀏覽資料，從而提高您的隱私。還提供「*硬核模式*」，可完全封鎖 Google 和 Meta 擁有的所有網域，以及所有依附服務。

![IVPN](assets/notext/32.webp)

就這樣，您就可以完全享受 IVPN 的樂趣了。如果您還想使用本地密碼管理器來增強您的線上帳戶的安全性，我邀請您查看我們關於 KeePass 的教程，這是一個免費的開源解決方案：


https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

如果您有興趣發現另一個與 IVPN 相似的 VPN 供應商，無論是在功能還是價格方面，我也建議您查看我們關於 Mullvad 的教程：


https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8