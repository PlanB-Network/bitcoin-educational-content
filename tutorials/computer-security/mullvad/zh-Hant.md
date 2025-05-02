---
name: Mullvad VPN
description: 設定以比特幣支付的 VPN
---
![cover](assets/cover.webp)


VPN (「*虛擬私人網路*」) 是一種服務，可在您的手機或電腦與 VPN 供應商管理的遠端伺服器之間建立安全且加密的連線。


技術上來說，當連線到 VPN 時，您的網際網路流量會透過加密隧道重新導向到 VPN 伺服器。此過程令第三方（如互聯網服務供應商 (ISP) 或惡意行為者）很難截取或讀取您的資料。VPN 伺服器接著會扮演中介的角色，代表您連線到您想要使用的服務。它會為您的連接分配一個新的 IP Address，這有助於向您訪問的網站隱藏您的真實 IP Address。然而，與某些線上廣告所暗示的相反，使用 VPN 並不允許您匿名瀏覽網路，因為這需要對 VPN 提供商有一定程度的信任，而 VPN 提供商可以看到您的所有流量。

![MULLVAD VPN](assets/fr/01.webp)

使用 VPN 有許多好處。首先，只要 VPN 供應商不分享您的資訊，就能保護您的線上活動隱私不受 ISP 或政府的干擾。其次，它可以保護您的資料安全，尤其是當您連線到容易受到 MITM（「**中間人**」）攻擊的公共 Wi-Fi 網路時。第三，透過隱藏您的 IP Address，VPN 可讓您繞過地理限制和審查，存取您所在區域無法存取或封鎖的內容。


如您所見，VPN 將流量觀察的風險轉移給 VPN 供應商。因此，在選擇 VPN 供應商時，必須考慮註冊所需的個人資料。如果提供商要求提供您的電話號碼、電子郵件 Address、銀行卡詳細資料，或者更糟糕的是您的郵政 Address，將您的身份與您的流量聯繫起來的風險就會增加。如果提供商受到攻擊或被依法扣押，就很容易將您的流量與您的個人資料聯繫起來。因此，建議選擇不需要任何個人資料且接受匿名付款（如使用比特幣）的供應商。


在本教程中，我將介紹一個簡單、高效、價格合理的 VPN 解決方案，使用時不需要任何個人資訊。


## Mullvad VPN 簡介

Mullvad VPN 是一項瑞典服務，因其 Commitment 對使用者隱私的重視而脫穎而出。與主流 VPN 供應商不同，Mullvad 在註冊時不需要提供任何個人資料。您無需提供電子郵件 Address、電話號碼或姓名；相反，Mullvad 會為您指定一個匿名帳號，用於付款和存取服務。此外，Mullvad 聲稱不會保留通過其伺服器的活動記錄。

![MULLVAD VPN](assets/notext/02.webp)

在付款方面，不一定需要提供信用卡資訊，因為 Mullvad 接受 Bitcoin 付款（僅在其官方網站的 onchain 付款，但有一種非官方的方法可透過 Lightning 付款）。他們也接受郵寄現金付款。


Mullvad VPN 也因其透明度和安全性而與眾不同。他們的軟體是開放原始碼的，並且定期接受獨立的安全稽核，以評估他們的應用程式和基礎架構，稽核結果會 [公布在他們的網站上](https://mullvad.net/fr/blog/tag/audits)。Mullvad 背後的公司位於瑞典，瑞典以嚴格的隱私權法律著稱。他們完全使用自行託管的伺服器，因此消除了使用第三方雲端服務 (例如超級擴充的 AWS、Google Cloud 或 Microsoft Azure) 的相關風險。


在功能方面，Mullvad 提供良好 VPN 用戶端所需的一切功能，包括在 VPN 斷線時保護流量的關閉開關、針對特定應用程式禁用 VPN 的選項，以及透過多個 VPN 伺服器路由流量的功能。


當然，這種服務品質是有成本的，但公平的價格通常是品質和誠信的指標。它可以表示該公司擁有不需要將您的個人資料出售給第三方的商業模式。Mullvad VPN 提供每月 5 歐元的固定價格，最多可在 5 台不同的裝置上使用。

![MULLVAD VPN](assets/notext/03.webp)

與主流 VPN 供應商不同，Mullvad 採用購買服務存取時間的模式，而非經常性的自動訂閱。您只需以比特幣一次性支付所選的使用時間。舉例來說，如果您購買一年的使用權，您可以在這段期間內使用服務，之後您必須回到 Mullvad 的網站更新您的使用時間。

與另一個高品質的 VPN 供應商 IVPN 相比，Mullvad 略為經濟。舉例來說，即使選擇購買 IVPN 的三年期，每月的費用約為 5.40 歐元。不過，IVPN 也提供一些額外的服務，而且也有比 Mullvad 更便宜的方案（標準方案），但只限於 2 台裝置，而且不包括「多跳」協定。

我也進行了一些非正式的速度測試來比較 IVPN 和 Mullvad。雖然 IVPN 在效能上略微佔優，但 Mullvad 的速度仍然令人非常滿意。與主流的 VPN 供應商相比，IVPN 和 Mullvad 的效率至少不相上下，甚至在某些情況下更勝一籌。


## 如何在電腦上安裝 Mullvad VPN？


造訪 [Mullvad 官方網站](https://mullvad.net/en/download/)，點選「*下載*」功能表。

![MULLVAD VPN](assets/notext/04.webp)

Windows 或 macOS 使用者可直接從網站下載軟體，並依照設定精靈提供的指示完成安裝。

![MULLVAD VPN](assets/notext/05.webp)

對於 Linux 使用者，您可以在 ["*Linux*"](https://mullvad.net/en/download/vpn/linux)部分找到適用於您發行版的特定說明。

![MULLVAD VPN](assets/notext/06.webp)

安裝完成後，您需要輸入您的帳戶 ID。我們將在本教學的以下部分瞭解如何取得。


## 如何在智慧型手機上安裝 Mullvad VPN？


從您的應用程式商店下載 Mullvad VPN，無論是 iOS 使用者的 [AppStore](https://apps.apple.com/us/app/mullvad-vpn/id1488466513)、Android 使用者的 [Google Play Store](https://play.google.com/store/apps/details?id=net.mullvad.mullvadvpn) 或 [F-Droid](https://f-droid.org/packages/net.mullvad.mullvadvpn/)。如果您使用 Android，您也可以選擇直接從 [Mullvad 網站](https://mullvad.net/en/download/vpn/android) 下載`.apk`檔。

![MULLVAD VPN](assets/notext/07.webp)

首次使用應用程式時，您將會登出。您需要輸入您的帳戶 ID 來啟動服務。

![MULLVAD VPN](assets/notext/08.webp)

現在，讓我們在您的裝置上啟動 Mullvad。


## 如何支付及啟動 Mullvad VPN？


前往 [Mullvad 官方網站](https://mullvad.net/)，點選「*開始*」按鈕。

![MULLVAD VPN](assets/notext/09.webp)

按一下「*generate 帳號*」按鈕。

![MULLVAD VPN](assets/notext/10.webp)Mullvad will then create your account. You do not need to provide any personal information. It is only your account number that will allow you to log in. It acts somewhat like an access key. Save it in a safe place like your password manager, for example. You can also make a paper copy.

![MULLVAD VPN](assets/notext/11.webp)

然後按一下「*將時間加入您的帳戶*」按鈕。

![MULLVAD VPN](assets/notext/12.webp)

然後您就會到達您帳戶的登入頁面。輸入您的帳號，然後按一下「*登入*」按鈕。

![MULLVAD VPN](assets/notext/13.webp)

選擇您的付款方式。我建議您使用比特幣支付，因為您可以享受 10% 的折扣，使每月的費用降至 4.50 歐元。如果您喜歡透過 Lightning 付款，我將在下文中提供另一種付款方式。

![MULLVAD VPN](assets/notext/14.webp)

按一下「*建立一次性付款 Address*」按鈕。

![MULLVAD VPN](assets/notext/15.webp)

然後使用您的 Bitcoin Wallet 將指定的金額支付給給您的收款 Address。

![MULLVAD VPN](assets/notext/16.webp)

交易確認後，網站可能需要幾分鐘時間才能偵測到您的付款。一旦 Mullvad 偵測到您的付款，您的訂閱期限將顯示在頁面左上方，而不是 「*無剩餘時間*」的提示。

![MULLVAD VPN](assets/notext/17.webp)

之後您就可以在軟體上輸入帳號來啟動 VPN。

![MULLVAD VPN](assets/notext/18.webp)

要在手機應用程式上啟用 VPN，過程完全相同。您只需輸入您的帳號。

![MULLVAD VPN](assets/notext/19.webp)

## 如何使用 Lightning 支付 Mullvad VPN？


正如您所瞭解的，Mullvad 目前還不接受透過 Lightning Network 付款。不過，感謝 [Lounès](https://x.com/louneskmt) 的推薦，我發現了一個非正式的服務，可以讓您繞過這個限制。這項服務在 [vpn.sovereign.engineering](https://vpn.sovereign.engineering/) 上提供，它接受您在 Lightning 上的付款，並提供您一個有效的 Mullvad 計劃作為回報。

![MULLVAD VPN](assets/notext/20.webp)

在這個網站上，您有兩種不同的選擇：您可以相信網站管理員，直接輸入您的帳號，然後點擊 「*登入*」，您的 Mullvad 套裝就會自動生效。或者，您可以點擊 "*Heck yeah!*"按鈕，在 Lightning 購買代金券，然後在 Mullvad 官方網站使用代金券來獲得您的套餐。![MULLVAD VPN](assets/notext/21.webp)在這兩種情況下，接下來您都會被要求選擇套餐的期限。您可以選擇 6 個月或 1 年。![MULLVAD VPN](assets/notext/22.webp) 然後點擊 "*Top-up with Lightning*"按鈕。![MULLVAD VPN](assets/notext/23.webp) 要完成購買，請用您的 Lightning Wallet 支付 Invoice。![MULLVAD VPN](assets/notext/24.webp) 如果您選擇購買代用券，請在 Mullvad 網站上，在您帳戶中可用的付款方式中選擇 「*代用券*」。然後，在指定的方塊中輸入您從 vpn.sovereign.engineering 網站收到的代金券號碼。![MULLVAD VPN](assets/notext/25.webp) ## 如何使用及設定 Mullvad VPN？


現在您已經擁有一個有效的帳號，並在 Mullvad 軟體或應用程式中輸入您的帳號，您就可以完全享受 VPN 的服務了。![MULLVAD VPN](assets/notext/26.webp) 要斷開 VPN，只需點擊 "*Disconnect*"按鈕。![MULLVAD VPN](assets/notext/27.webp) "*Disconnect*"按鈕旁邊的紅色小箭頭允許您在不改變當前位置的情況下更改服務器。![MULLVAD VPN](assets/notext/28.webp) 如果您想為 VPN 伺服器更換城市，請點選「*Switch location*」選擇新的位置。![MULLVAD VPN](assets/notext/29.webp) 在螢幕上方，您會看到您裝置的暱稱以及套餐的剩餘時間。！[MULLVAD VPN](assets/notext/30.webp) 點擊小人圖標，您將訪問您的帳戶的詳細信息。![MULLVAD VPN](assets/notext/31.webp) 要存取設定，請點選齒輪。![MULLVAD VPN](assets/notext/32.webp) 在「*使用者 Interface 設定*」選單中，您可以自訂軟體的設定，包括 Interface 語言及其在系統上的行為。![MULLVAD VPN](assets/notext/33.webp) 在「*VPN 設定*」功能表中，您可以找到與 VPN 相關的選項。我建議啟用「*啟動時啟動應用程式*」和「*自動連線*」選項，這樣當您的機器啟動時，您的 VPN 連線就會自動啟動。

![MULLVAD VPN](assets/notext/34.webp) In the "*DNS content blockers*" submenu, you have the option to filter and block DNS requests to malicious, advertising, or unwanted websites.

![MULLVAD VPN](assets/notext/35.webp)

最後，「*分割隧道*」功能表可讓您選擇機器上的特定應用程式，這些應用程式的網際網路流量不會透過 VPN 傳送。

![MULLVAD VPN](assets/notext/36.webp)

若要總覽您的 Mullvad 帳戶，並管理各種連接的裝置，您可以點選網站上的「*裝置*」功能表。

![MULLVAD VPN](assets/notext/37.webp)

就這樣，你現在就可以完全享受 Mullvad VPN 了。如果您有興趣了解另一家與 Mullvad 功能和價格相似的 VPN 供應商，我也建議您看看我們關於 IVPN 的教學：


https://planb.network/tutorials/computer-security/communication/ivpn-5a0cd5df-29f1-4382-a817-975a96646e68