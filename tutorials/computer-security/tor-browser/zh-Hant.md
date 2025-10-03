---
name: Tor Browser
description: 如何使用 Tor 瀏覽器？
---
![cover](assets/cover.webp)


顧名思義，瀏覽器是用來瀏覽網際網路的軟體。它是用戶機器與網路之間的閘道，將網站的代碼轉譯為互動且可讀取的頁面。瀏覽器的選擇非常重要，因為它不僅會影響您的瀏覽體驗，還會影響您的線上安全和隱私。


請注意不要混淆瀏覽器和搜尋引擎。瀏覽器是您用來存取網際網路的軟體 (例如 Chrome 或 Firefox)，而搜尋引擎則是一種服務，例如 Google 或 Bing，可以協助您在網路上尋找資訊。


如今，Google Chrome 是迄今為止使用率最高的瀏覽器。2024 年，它約佔全球市場的 65%。Chrome 瀏覽器的速度和效能備受讚賞，但它不一定是每個人的最佳選擇，尤其是如果隱私權是您的優先考量。Chrome 屬於 Google，該公司以收集和分析使用者的大量資料而聞名。事實上，他們的內部瀏覽器是他們監控策略的核心。這個軟體是您大部分線上互動的核心元件。掌握瀏覽器的資料收集對 Google 來說是一個重要的課題。

![TOR BROWSER](assets/notext/01.webp)

*來源：[gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*


瀏覽器有幾個主要系列，每個系列都是以特定的渲染引擎為基礎。Google Chrome、Microsoft Edge、Brave、Opera 或 Vivaldi 等瀏覽器都是建立在 Chromium 瀏覽器上，Chromium 瀏覽器是 Google 開發的 Chrome 瀏覽器的輕量級開放原始碼版本。所有這些瀏覽器都使用 Blink 渲染引擎，它是 WebKit 的 Fork，本身則源自 KHTML。Chromium 在市場上佔有優勢，使得衍生自 Chromium 的瀏覽器特別有效率，因為網頁開發人員傾向於主要針對 Blink 來最佳化他們的網站。


Apple 的瀏覽器 Safari 使用同樣來自 KHTML 的 WebKit。


另一方面，Mozilla Firefox、LibreWolf 和 Tor Browser 等瀏覽器依賴 Gecko，這是一種不同的呈現引擎，最初來自 Netscape 瀏覽器。


選擇正確的瀏覽器取決於您的需求。但如果您至少關心您的隱私，因此也關心您的安全，我建議您選擇一般使用的 Firefox 瀏覽器，以及隱私性更高的 Tor 瀏覽器。在本教程中，我將教您如何輕鬆上手使用 Tor 瀏覽器。

![TOR BROWSER](assets/notext/02.webp)


## Tor 瀏覽器簡介


Tor 瀏覽器是專為安全且盡可能隱私的網路導覽而設計的瀏覽器。該瀏覽器基於 Firefox，因此也基於 Gecko 渲染引擎。

Tor 瀏覽器使用 Tor 網路將您的流量加密並經由多個中繼伺服器路由，再傳送至目的地。這種被稱為 "*onion routing*"的多層路由過程有助於隱藏您的真實 IP Address，使您的位置和在線活動難以被識別。不過，瀏覽速度必然會比不使用 Tor 網路的標準瀏覽器慢，因為它是間接的。

與其他瀏覽器不同的是，Tor Browser 整合了特定的功能來防止您的線上活動被追蹤，例如隔離每個造訪的網站，並在關閉時自動刪除 cookies 和歷史記錄。它的設計還可以讓所有使用者看起來與所造訪的網站盡可能相似，從而將指紋識別的風險降到最低。


您可以很好地使用 Tor 瀏覽器來存取標準網站 (`.com`、`.org` 等)。在這種情況下，您的流量會透過數個 Tor 節點進行匿名化，然後才到達出口節點，與 Clearnet 上的最終網站進行通訊。

![TOR BROWSER](assets/notext/03.webp)

您也可以使用 Tor 瀏覽器存取隱藏的服務 (位址以 `.onion` 結尾)。在這種情況下，所有流量都留在 Tor 網路中，沒有出口節點，確保使用者和目的地伺服器的完全隱私。這種操作模式主要用於存取有時被稱為 「*暗網*」的地方，也就是傳統搜尋引擎無法索引的網際網路部分。

![TOR BROWSER](assets/notext/04.webp)


## Tor 網路和 Tor 瀏覽器有什麼不同？


Tor 網路和 Tor 瀏覽器是兩種截然不同的東西，不應混為一談，但兩者是相輔相成的。Tor 網路是由使用者所操作的中繼伺服器所組成的全球基礎架構，它透過幾個節點來匿名化網際網路流量，然後再將其導向最終目的地。這就是著名的洋蔥路由。


另一方面，Tor 瀏覽器是專為方便以簡單的方式存取此網路而設計的特定瀏覽器。它在預設情況下整合了連線到 Tor 網路的所有必要設定，並使用修改版的 Firefox 來提供熟悉的瀏覽體驗，同時最大化隱私和安全性。


Tor 網路不僅被 Tor 瀏覽器使用。各種軟體和應用程式都可以利用它來保護通訊安全。例如，可以在您的 Bitcoin 節點上啟用透過 Tor 網路進行的通訊，以便向其他使用者隱藏您的 IP Address，並防止網際網路服務供應商監視您的 Bitcoin 相關流量。

總而言之，Tor 網路是提供我們網路瀏覽隱私的基礎架構，而 Tor 瀏覽器是讓我們使用此網路作為網路瀏覽一部分的軟體。


## 如何安裝 Tor 瀏覽器？


Tor 瀏覽器適用於電腦的 Windows、Linux 和 macOS，以及智慧型手機的 Android。若要在電腦上安裝 Tor 瀏覽器，請造訪 [Tor Project 官方網站](https://www.torproject.org/)。

![TOR BROWSER](assets/notext/05.webp)

按一下「*下載 Tor 瀏覽器*」按鈕。

![TOR BROWSER](assets/notext/06.webp)

選擇適合您作業系統的版本。

![TOR BROWSER](assets/notext/07.webp)

按一下可執行檔開始安裝，然後選擇您的語言。

![TOR BROWSER](assets/notext/08.webp)

選擇安裝軟體的資料夾，然後按一下「*安裝*」按鈕。

![TOR BROWSER](assets/notext/09.webp)

等待安裝完成。

![TOR BROWSER](assets/notext/10.webp)

最後，按一下「*完成*」按鈕。

![TOR BROWSER](assets/notext/11.webp)


## 如何使用 Tor 瀏覽器？


Tor 瀏覽器的使用方式與標準瀏覽器相同。

![TOR BROWSER](assets/notext/12.webp)

第一次啟動時，瀏覽器會顯示一個頁面，邀請您連線到 Tor 網路。只需按一下「*連線*」按鈕即可建立連線。

![TOR BROWSER](assets/notext/13.webp)

如果您希望軟件在將來的使用過程中自動連線到 Tor 網路，請勾選「*Always connect automatically*（*總是自動連線*）」選項。

![TOR BROWSER](assets/notext/14.webp)

一旦連線到 Tor 網路，您就會到達首頁。

![TOR BROWSER](assets/notext/15.webp)

要在網際網路上執行搜尋，只需在搜尋列中輸入您的查詢內容，然後按「*enter*」鍵即可。

![TOR BROWSER](assets/notext/16.webp)

然後，您就可以像使用其他瀏覽器一樣，從搜尋引擎取得結果。

![TOR BROWSER](assets/notext/17.webp)

DuckDuckGo 上的「*Onionize*」選項允許您透過其在 Tor 網路上的隱藏服務使用搜尋引擎，方法是存取其 `.onion` Address。

![TOR BROWSER](assets/notext/18.webp)


## 如何設定 Tor 瀏覽器？


在瀏覽器螢幕的頂端，您會發現一個匯入收藏夾的選項。這樣您就可以將舊瀏覽器中的書籤自動整合到 Tor 瀏覽器中。

![TOR BROWSER](assets/notext/19.webp)

您也可以選擇按一下位於所瀏覽網頁右上方的星形圖示來新增書籤。

![TOR BROWSER](assets/notext/20.webp)

在右邊的功能表中，您可以存取各種選項。

![TOR BROWSER](assets/notext/21.webp)The "*New identity*" button allows you to change your Tor identity. Specifically, this enables you to start a new user session on Tor, meaning changing your IP address and resetting cookies and open sessions.

![TOR BROWSER](assets/notext/22.webp)

*Bookmarks*" 功能表可讓您管理書籤。

![TOR BROWSER](assets/notext/23.webp)

如果您已在設定中啟用「*歷史記錄*」，則可存取瀏覽歷史記錄。

![TOR BROWSER](assets/notext/24.webp)

透過「*附加元件與主題*」功能表，您可以自訂瀏覽器的外觀或新增擴充套件。由於 Tor 瀏覽器是以 Mozilla Firefox 為基礎，因此您可以使用適用於 Firefox 的主題和擴充套件。

![TOR BROWSER](assets/notext/25.webp)

最後，「*設定*」按鈕可讓您存取瀏覽器的設定。

![TOR BROWSER](assets/notext/26.webp)

在設定的「*一般*」標籤中，有各種選項可讓您自訂 Tor 瀏覽器使用者 Interface。

![TOR BROWSER](assets/notext/27.webp)

在「*首頁*」標籤中，您可以選擇變更開啟 Tor 瀏覽器和開啟新標籤時顯示的預設頁面。

![TOR BROWSER](assets/notext/28.webp)

在「*搜尋*」標籤中，您可以選擇搜尋引擎。Tor 瀏覽器預設為 DuckDuckGo，這是一個專注於保護使用者隱私的搜尋引擎，但您也可以選擇 Google 或 Startpage 等。

![TOR BROWSER](assets/notext/29.webp)

您也可以在搜尋引擎中設定捷徑。

![TOR BROWSER](assets/notext/30.webp)

例如，您可以在瀏覽器的搜尋列中輸入「*@wikipedia*」，接著輸入您的搜尋字詞，例如「*Bitcoin*」。

![TOR BROWSER](assets/notext/31.webp)

此功能會直接在 Wikipedia 網站執行搜尋。

![TOR BROWSER](assets/notext/32.webp)

因此，您可以為不同的網站設定其他自訂捷徑。


接下來，在「*隱私與安全*」標籤中，您可以找到所有與隱私和安全相關的設定。

![TOR BROWSER](assets/notext/33.webp)

您可以選擇保留或刪除瀏覽記錄。

![TOR BROWSER](assets/notext/34.webp)

您也可以管理授予不同網站的存取權限。

![TOR BROWSER](assets/notext/35.webp)

為了確保瀏覽器的整體安全性，「*Safer*」和「*Safest*」模式可讓您調整網頁功能和您造訪的網站所執行的指令碼。這樣可以將利用漏洞的風險降到最低，但也會反過來影響網站的顯示和互動性。![TOR BROWSER](assets/notext/36.webp) 您會發現其他安全選項，包括危險內容封鎖程式和 HTTPS 純模式，可確保與網站的連線始終遵守此協定。![TOR BROWSER](assets/notext/37.webp)最後，在「*連線*」標籤中，您可以找到與連線到 Tor 網路相關的所有設定。您可以在這裡設定橋接，以便從 Tor 可能受到審查的地區存取 Tor。![TOR瀏覽器](assets/notext/38.webp) 就這樣，您就可以以更安全、更隱私的方式瀏覽網際網路了！如果您對線上隱私感興趣，我也建議您參考 Mullvad VPN 的其他教學：


https://planb.network/tutorials/computer-security/communication/mullvad-968ec5f5-b3f0-4d23-a9e0-c07a3e85aaa8