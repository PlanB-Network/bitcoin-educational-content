---
name: Angry IP Scanner
description: 掃描網路的簡單方法
---
![cover](assets/cover.webp)



___



*本教學是根據 Florian BURNEL 發表於 [IT-Connect](https://www.it-connect.fr/) 的原始內容。原始碼授權類型 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有變更。*



___



## I.簡報



如何快速輕鬆地掃描 Windows 網路中的連線機器？答案就是 Angry IP Scanner。這個開放原始碼專案可讓您使用簡單易用的圖形 Interface 輕鬆掃描網路。



個人可使用此工具掃描其本機網路，IT 專業人士也可使用此工具達到相同目的。證明**此工具非常實用**，它已被**些網路犯罪團體**用來掃描企業網路（與 Nmap 的方式相同）。一個很好的例子就是 [贖金軟體組織 RansomHub](https://www.it-connect.fr/deja-210-victimes-pour-le-groupe-de-ransomware-ransomhub-lance-en-fevrier-2024/)。它仍然是一個完善的軟體，但就像其他網路與安全導向的工具一樣，它的使用可能會被濫用。



在此，我們將在 **Windows 11** 上使用，但完全可以在其他版本的 **Windows** 以及 **Linux** 和 **macOS** 上使用。



雖然沒有 Nmap 那麼全面，但 **Angry IP** Scanner 對於快速、基本的網路分析仍相當有趣，也因為它在每個人的能力範圍之內。它會**偵測連線到網路的主機**，並辨識**主機名稱**和**開啟的連接埠**。



如果您想更進一步，請參閱 Nmap 的教學：



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d

## II.開始使用 Angry IP Scanner



### A.下載並安裝 Angry IP Scanner



您可以從應用程式的官方網站或 GitHub 下載最新版本的 Angry IP Scanner。我們將採用後者。點擊下面的鏈接，下載 EXE 版本："**ipscan-3.9.1-setup.exe**".





- [Angry IP Scanner GitHub](https://github.com/angryip/ipscan/releases/latest)



![Image](assets/fr/016.webp)



執行可執行檔以繼續安裝。安裝過程中沒有特別的事情要做。



![Image](assets/fr/013.webp)



### B.執行初始網路掃描



首次啟動時，請花時間閱讀「**開始使用**」視窗中的說明，以瞭解更多關於工具如何運作的資訊。順便說一下，有幾個名詞需要注意：





- **Feeder**：負責從隨機 IP 範圍或包含 IP 位址清單的檔案中，產生要掃描的 IP 位址清單的模組。
- **Fetcher**：一組擷取網路上主機資訊的模組。例如，有偵測 MAC 位址、掃描連接埠、偵測主機名稱或傳送 HTTP 請求的擷取器。



![Image](assets/fr/018.webp)



若要掃描 IP 子網路，只要在「**IP 範圍**」欄位中輸入**開始 IP Address** 和**結束 IP Address**（否則請在右側變更類型）。然後按一下「**開始**」按鈕。



![Image](assets/fr/019.webp)



幾十秒後，結果就會在軟體的 Interface 中顯示出來。 **對於分析範圍內的每個 IP Address，您會看到 Angry IP Scanner 是否偵測到主機。** 畫面上也會出現摘要，顯示有效主機的數量 (在此例中為 6)，以及開啟連接埠的主機數量。



![Image](assets/fr/020.webp)



在這裡，我們可以看到一台名為「**OPNsense.local.domain**」的主機，與 IP Address 「**192.168.10.1**」相關，並可透過**埠 80** 和 **443**（HTTP 和 HTTPS）存取。在主機上按滑鼠右鍵可存取其他指令，例如 ping、追蹤路由和透過此 IP Address 開啟瀏覽器。



![Image](assets/fr/012.webp)



### C.新增掃描連接埠



預設情況下，**Angry IP Scanner** 會掃描 3 個連接埠： **80** (HTTP)、**443** (HTTPS) 和 **8080**。您可以在應用程式偏好設定中加入更多要掃描的連接埠。按一下「**工具**」功能表，然後按一下「**連接埠**」標籤。



在這裡，您可以透過「**連接埠選擇**」選項修改連接埠清單。您可以**指定以逗號分隔的特定連接埠號，或連接埠範圍**。下面的範例新增了兩個連接埠： **445** (SMB) 和 **389** (LDAP)。若要掃描 1 到 1000 的連接埠，請輸入「**1-1000**」。未指定埠掃描是否以 TCP、UDP 或兩者執行。



![Image](assets/fr/021.webp)



如果您再次執行掃描，很可能會得到新的資訊。在下面的範例中，Angry IP Scanner 告訴我，由於新設定了要掃描的連接埠，主機 "**SRV-ADDS-01**「和 」**SRV-ADDS-02**"上的連接埠 389 和 445 是開啟的。



![Image](assets/fr/022.webp)



**註**：從「**掃描器**」功能表，您可以將掃描結果匯出到文字檔。



如果您希望進一步掃描，請按一下「**工具**」功能表，然後按一下「**擷取**」。這會增加掃描的「能力」。只要選取一個擷取器，並將其往左移動即可啟用。這會在掃描結果中增加一列。



![Image](assets/fr/014.webp)



下面的範例顯示「**NetBIOS info**」和「**Web detection**」功能。前者提供附加資訊，例如機器的 MAC Address 和網域名稱，而後者則顯示網頁標題 (可能會在某程度上顯示網頁伺服器或應用程式的類型)。



![Image](assets/fr/011.webp)



最後，從偏好設定中，您也可以變更 "**ping**"所使用的方法，也就是考慮主機是否活躍。由於有些主機不會回應 ping，因此您可以嘗試其他方法 (UDP 封包、TCP 埠探測、ARP、UDP + TCP 組合等)。



## III.總結



簡單有效：Angry IP Scanner 可偵測連線至網路的主機，並讓您設定連接埠掃描。就選項而言，它沒有 Nmap 靈活，也沒有那麼深入，但它是快速掃描的好開始。



如果您想使用圖形化 Interface 的 **Nmap**，您可以使用 **the Zenmap 應用程式** (請參閱下面的概述)。



![Image](assets/fr/015.webp)



https://planb.network/tutorials/computer-security/communication/nmap-862300d7-6dfb-4660-970d-f56a9f58f60d