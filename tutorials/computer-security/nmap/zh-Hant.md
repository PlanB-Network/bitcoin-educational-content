---
name: Nmap
description: Master Nmap 用於網路映射與弱點掃描
---

![cover](assets/cover.webp)



*本教學依據 Mickael Dorigny 於 [IT-Connect](https://www.it-connect.fr/) 發表的原始內容。原始碼授權類型 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。已對原文進行修改。



___



歡迎來到本 Nmap 入門教學，本教學專為想要掌握這個強大網路掃描工具的人所設計。其目的是為您提供日常有效使用 Nmap 所需的基本知識。



Nmap 是一個多功能的工具，被 IT、網路和網路安全專業人員廣泛用於診斷、網路發現和安全審計。本教學是針對那些剛進入這些領域並想學習 Nmap 基礎知識的人。建議具備基本的系統與網路管理知識。



您將學習到 Nmap 的基礎知識、如何執行連接埠掃描、識別網路上的活動主機、偵測服務版本和作業系統、執行弱點掃描等等。每一部分都包括詳細的解釋和實例，幫助您掌握 Nmap 在各種情況下的使用。



本教學結束時，您將對 Nmap 有扎實的瞭解，並能有效地使用它來改善網路的安全性和管理。祝您閱讀愉快



## 1 - Nmap 簡介：什麼是 Nmap?



### I.簡報



在第一節中，我們將介紹 Nmap 網路掃描工具。我們會看看您需要知道的關於這個工具的關鍵 Elements 以及它的一般運作方式。這將有助於我們更好地理解本教學的其他部分。



### II.介紹 Nmap 工具



Nmap 是一種免費的開放原始碼工具，用於網路發現、映射和安全稽核。它也可用於其他任務，例如**網路清單、診斷或監控**。



它可以確定目標網路中的主機是否活躍且可以連線、哪些網路服務被暴露、哪些版本和技術正在使用，以及其他有用的分析資訊。Nmap 可用於掃描特定機器上的單一服務，或掃描大片網路，甚至整個網際網路。



Nmap 的優勢有很多：





- 功能強大且靈活**：Nmap 可以掃描大型網路，並使用先進的偵測技術。它支援 UDP、TCP、ICMP、IPv4 和 IPv6，並能執行版本偵測、弱點掃描或特定通訊協定的互動。它的架構是模組化的，這特別要歸功於 NSE (Nmap Scripting Engine) 腳本，我們稍後會在本教程中介紹。
- 易於使用**：官方文件豐富且品質一流。大量的社群資源也可協助您開始使用。
- 受歡迎且歷史悠久**：Nmap 自 1998 年以來一直是其領域的參考。在此更新時，目前的版本是 7.95。雖然有其他工具可用於特定任務，但 Nmap 仍是網路映射與分析的必備工具。



**Nmap at the movies**



Nmap 是少數在大眾中有一定知名度的安全工具之一。它出現在電影 _Matrix Reloaded_ 中，在 Trinity 使用它入侵系統的標誌性場景中：



![nmap-image](assets/fr/01.webp)



矩陣：以 Nmap 為特色的 Reloaded 場景



他也出現在其他電影作品中。



**意見回饋



身為系統管理員、網路安全稽核員及 pentester，我幾乎每天**都會使用 Nmap，而且我**經常將它推薦**給希望加強網路指揮能力及提升診斷能力的系統管理員。



### III.高階作業



Nmap 適用於 Linux、Windows 和 macOS。它主要以 C、C++ 和 Lua（用於 NSE 腳本）寫成。它主要在命令列上使用，雖然也有圖形介面，例如 Zenmap。不過，我們強烈建議您從命令列開始使用，以便更好地瞭解它的運作方式。



一個簡單的例子：



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



稍後會詳細解釋這個指令。在本教程中，我們將在 Linux 上使用 Nmap，但它在其他系統上的用途類似。在 Windows 下，Nmap 依賴 **Npcap** 函式庫（取代現已過時的 WinPcap）來擷取和注入網路封包。



Nmap 的使用就像傳統的二進位工具，例如 `ls` 或 `ip`。某些進階功能可能需要提升權限，因為該工具有時候會以非常規方式處理封包，以挑起目標系統的特定反應 (特別是服務或弱點偵測)。



### IV.使用 Nmap 的影響



在使用 Nmap 之前，必須瞭解其對網路和系統的潛在影響：





- 它可以在短時間內傳送**千甚至百萬個封包**，使某些網路基礎設施達到飽和。
- 它可以 generate ** 畸形或非標準**封包，很可能會擾亂某些設備（特別是工業系統）。
- 它可以產生類似攻擊的**行為，觸發安全系統 (防火牆、IDS/IPS 等) 的警示。



一般而言，**Nmap 是一個非常健談的工具**，因為它會產生大量流量，以便擷取盡可能多的資訊。因此，建議您在敏感或生產環境中使用之前，先充分瞭解它的運作方式。



### V.結論



本節介紹 Nmap 及其主要功能。我們已經看到它是一個重要、強大且靈活的網路映射工具。我們也討論了它的運作方式，以及使用它時的注意事項，為本教學的後續部分作好準備。



## 2 - 為什麼使用 Nmap？



### I.簡報



在本節中，我們將介紹 Nmap 網路掃描工具的主要用途。我們將看見它是一個在許多環境和專業中廣泛使用的工具，在您的工具箱中有這個工具並知道如何掌握它絕對是一個有用的技能。



### II.使用 Nmap 進行診斷和監督



Nmap 可用於網路診斷，更廣泛來說，也可用於監控。就像 ping 可以用來判斷兩台主機是否在通訊一樣，Nmap 也可以用來快速判斷主機是否在活動，或特定服務是否在運作。多虧了 [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap")，我們可以獲得關於主機回應時間、封包路由、特定服務回應等的精確資料。



例如，可使用下列指令和結果快速找出主機 **192.168.1.18** 上的 Web 伺服器是否啟動且回應正常：



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*使用 Nmap 從遠端伺服器擷取網路服務狀態*。



所以，在調試或診斷階段，使用 Nmap 比著名的 「ping 測試」 更進一步。我們稍後會看到，Nmap 有幾種方法可用來識別哪個服務正在某個指定的連接埠上聆聽，包括它的版本。



### III.使用 Nmap 進行網路映射



作為一個 _Network Mapper_，網路映射是此工具的主要目標。它可以用於本機網路，或跨多個網路、子網路和 VLAN，以列出所有可連接的主機和服務。Nmap 使這項任務比任何手動方法更快、更有效率。



例如，以下命令可用於快速識別 **192.168.1.0/24** 網路上的活動主機：



```
nmap -sn 192.168.1.0/24
```



*注意： `-sP`選項已經過時，由`-sn`取代。



![nmap-image](assets/fr/03.webp)



*使用 Nmap 發現網路中可連接的主機*



我們稍後就會看到 Nmap 有幾種方法用來判斷主機是否可被視為「活躍」，即使它先驗地沒有暴露任何服務。



### IV.使用 Nmap 評估過濾政策



Nmap 的優點在於它是以事實為依歸：它的結果讓確立具體的發現成為可能，這與任何架構文件或過濾政策都不同。它是評估資訊系統區隔有效性的重要工具，因為它可讓您**確認過濾政策是否確實被應用**。



在企業網路中，最佳實務規定系統必須根據其角色、重要程度或位置進行區隔。過濾規則 (通常透過防火牆實施) 必須限制區域之間的通訊。但這些設定通常都很複雜，而且容易出錯。



因此，要驗證政策是否受到尊重，沒有什麼比具體測試更重要。例如，您可以檢查敏感的管理服務 (SSH、WinRM、MSSQL、MySQL 等) 是否無法從使用者區域存取。



使用 **Nmap 測試過濾政策** 應該是有系統的，然後才將這樣的政策投入生產。不幸的是，這項檢查經常被忽略。



根據我的經驗，如果沒有驗證測試，許多組態錯誤都會被忽略。IP 範圍中的一個簡單錯誤或規則疏忽，都可能讓原本應該隔離的區域受到攻擊。



### V.使用 Nmap 進行安全稽核與滲透測試



Nmap 對於安全評估**、滲透測試 (pentests) 有許多有用的功能，不幸的是，對於攻擊者也是如此。



網路發現功能對於攻擊者來說是非常重要的，因為攻擊者需要在初始入侵後瞭解網路拓樸。但 Nmap 提供的功能遠不止於此：它整合了一個腳本引擎，**多是專門用於偵測弱點**。



例如，此指令可用於檢查 FTP 服務是否允許匿名連線，而無需手動連線：



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*使用 NSE 指令碼透過 Nmap.* 檢查匿名 FTP 認證



Nmap 漏洞偵測是稽核或滲透測試的第一步。它能讓您快速找出某些弱點，並優化您的分析工作。



但請注意： **漏洞掃描工具有其限制**。Nmap 只涵蓋一小部分的威脅，如果沒有偵測到任何問題，也不保證系統是安全的。因此，必須**瞭解所使用的腳本如何運作**，而不是完全依賴它們的判斷。



### VI.總結



我們已經看到，掌握 Nmap 可以涵蓋廣泛的用例，從診斷和監控到映射、安全策略評估和漏洞掃描。在下一節中，我們將進入細節並安裝 Nmap。




## 3 - 安裝和設定 Nmap



### I.簡報



在本節中，我們將學習如何在 Linux 和 Windows 作業系統安裝 Nmap 網路掃描工具。在本節的最後，我們將擁有開始使用 Nmap 的未來模組所需的一切。最後，我們會看到它在使用時可能需要哪些權限，以及為什麼。



### II.在 Linux 下安裝 Nmap



Nmap 最初是為了在 GNU/Linux 作業系統上執行而設計的。因此，由於它的長壽性和受歡迎程度，您可以在所有主要 Unix 發行版本的官方套件庫中找到它。在本教程中，我將使用基於 Debian 的作業系統 [Kali Linux](https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux")。但您也可以從經典的 Debian、CentOS、Red Hat 或其他作業系統，以完全相同的方式使用它！



在 Debian 下，要檢查 Nmap 是否存在於您目前的套件庫中，您可以使用下列指令：



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



這裡的答案很明顯表示 "nmap「 套件存在於套件庫 (這裡是 Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ 」Linux") 的套件庫)。從現在開始，您可以透過一般的安裝指令來安裝 Nmap，暫時沒有任何解除武裝的動作 🙂 ：



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



為了檢查 Nmap 是否安裝正確，我們會顯示它的版本：



```
nmap --version
```



以下是預期的結果：



![nmap-image](assets/fr/05.webp)



顯示 Nmap._ 目前版本的結果。



請注意這個顯示中有 "libpcap" (_Packet Capture Library_) 函式庫及其版本。libpcap" 也被 Wireshark 使用，Nmap 使用它來建立和操作封包，並監聽網路流量。



### III 在 Windows 上安裝 Nmap



若要在 Windows 作業系統上安裝，請先從官方網站下載二進位檔案（並非其他網站！）：





- 官方網站的 Nmap 下載頁面：[https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)




然後，您需要下載名為 `nmap-<VERSION>-setup.exe` 的二進位檔案：



![nmap-image](assets/fr/06.webp)



nmap for Windows 安裝二進位檔案下載頁面



一旦您的系統上有這個二進位檔，只要執行它就可以安裝 Nmap。這是一個直接的安裝，您可以將所有選項保留為預設值。



我的反應是取消勾選 "zenmap (GUI Frontend)"。這是 Nmap 的圖形化 Interface，我沒有使用，也不會在本教程中涵蓋，但是一旦您掌握了 Nmap 命令列工具，可以隨意試試！



![nmap-image](assets/fr/07.webp)



在 Windows 上安裝 Nmap 時可選擇取消 Zenmap



在 Nmap 安裝結束時，建議進行第二次安裝："Npcap "函式庫：



![nmap-image](assets/fr/08.webp)



在 Windows 下安裝 Nmap 時安裝「Npcap」函式庫



這是 Nmap 用來管理網路通訊的函式庫，也就是建立、傳送和接收網路封包。如果您在 Windows 上使用 Wireshark，您可能已經接觸到這個函式庫，因為它也使用這個函式庫，而且需要安裝。



與 Linux 一樣，您可以開啟命令提示符或 [Powershell] 終端 (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") 並輸入下列命令，以驗證 Nmap 是否已安裝：



```
nmap --version
```



以下是預期的結果：



![nmap-image](assets/fr/09.webp)



顯示 Nmap._ 目前版本的結果。



Nmap 現在已經安裝在 Windows 上。您可以按照本教程，以與 Linux 完全相同的方式使用它。



### IV.使用 Nmap 所需的本機權限



但順帶一提，當使用 Nmap 時，**是否需要在系統上擁有較高的本機權限？ **視情況而定**。



在它最基本的形式下，也就是在不使用它的選項的情況下，Nmap 不一定需要有權限。然而，您很快就會意識到，最好是在有權限的情況下使用 Nmap (Linux 下是 "root「，Windows 下是 」administrator" 或同等權限)，這樣才能充分發揮它的潛力，但也有可能收到像這樣的錯誤訊息：



![nmap-image](assets/fr/10.webp)



當 Nmap 選項需要 root 權限時，Linux 下會出現錯誤訊息。



無論是在Linux或Windows上，有許多Nmap會要求您有權限存取的情況。主要原因如下（非盡列）：





- 建構「原始」網路封包**：Nmap 可以使用廣泛的掃描方法，包括進階的封包處理和建構。舉例來說，當我們要執行 TCP SYN 掃描時，就會出現這種情況，因為 TCP SYN 掃描並不尊重 TCP 交換的經典 _Three-way handshake_。為了做到這一點，Nmap 需要使用作業系統原生以外的函數，因為作業系統只知道如何尊重網路通訊的良好作法 (它呼叫上面看到的 "Npcap「 和 」libcap" 函式庫)。正因為 Nmap 並非以 「標準 」的方式做事，所以它才能推斷出某些關於作業系統、服務和某些弱點的資訊。





- 監聽網路流量**：Nmap 的某些選項要求它監聽網路，以便擷取某些資訊。這個動作在作業系統上被認為是敏感的，因為它也允許您監聽系統上其他應用程式的通訊。就像 Wireshark 一樣，Nmap 需要特定的權限才能執行此動作，直接進入權限會話會比較容易取得這些權限。





- 在有權限的連接埠上監聽**：在作業系統上，從 0 到 1024 的連接埠（TCP 以及 UDP）被稱為有權限的連接埠，也就是說，它們在某種程度上被保留給非常特殊的用途，因此受到保護。儘管這個理由在今天已經有點過時了，但仍然需要有一定的權限來監聽這些連接埠，Nmap可能必須這樣做，這取決於它將如何被使用。





- 發送 UDP 封包：** 同樣地，在 UDP 連接埠上監聽網路應用程式（一個無狀態協定）需要操作系統上的特權。因此，如果您要執行 UDP 掃描，Nmap 將必須聆聽回應，以分析掃描的回覆，就需要有權限的會話。




更精確的說，至少在 Linux 下，可以在沒有 root 的情況下執行 Nmap 及其所有功能和選項。這是透過賦予二進位檔正確的_能力_來實現的。然而，這需要進階的操作，可能不如直接以權限執行 Nmap 來得實際。而且，這種方法較不常見，如果配置錯誤，可能會造成安全問題。



然而，這與我們的 Nmap 教學有點不同，所以我們暫時不談它。



在本教程的其他部分，假定 Nmap 总是以 "root 「身份运行（在 shell 中以 」root 「身份或通过 」sudo "命令），或者在 Windows 下以管理员终端运行，即使没有说明。否則，您可能會體驗到與教程中細微但明顯的差異。



### V.結論



就是這樣！Nmap 現在已經安裝在我們的作業系統上，並且準備好使用，不需要進一步的設定。本節結束了對 Nmap 的介紹和演示。我希望它能讓你垂涎三尺，並渴望開始練習。



說得嚴肅一點，我們現在對 Nmap 映射工具有了更清楚的了解，也知道它最常見的用途，以及它的限制。讓我們繼續往下看！




## 4 - 使用 Nmap 進行 TCP 和 UDP 連接埠掃描



### I.簡報



在本節中，我們將學習如何使用 Nmap 網路掃描工具執行第一次連接埠掃描。我們會看到如何使用它編譯主機上暴露的網路服務清單，不論是使用 TCP 或 UDP 通訊協定。



從現在開始，請記住只掃描您已獲得明確授權的受控環境中的主機。





- 作為提醒：[《刑法典》：第三章：攻擊自動資料處理系統](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




**如果您手邊沒有**，我推薦您使用下列免費的解決方案，它們就是您要的東西！





- [Hack The Box](https://app.hackthebox.com/ "Hack The Box")** ：黑客訓練平台 Hack The Box 不斷提供易受攻擊的系統，讓您隨心所欲地進行攻擊。有幾百個系統可供使用，但更新的 20 台機器全年免費提供，可透過 OpenVPN VPN 存取。





- [Vulnhub](https://www.vulnhub.com/ "Vulnhub")** ：此平台提供許多故意易受攻擊的系統供下載，可透過 VirtualBox (也是免費的解決方案) 或其他方式使用。一旦下載，就不需要 VPN - 一切都在本地。




此外，您也可以在您喜愛的作業系統上***建立虛擬機器，並在上面安裝各種服務作為測試目標。這樣做的好處是，您也可以在掃描時看到伺服器端發生了什麼事，尤其是使用 Wireshark，而且當我們進行更進階的測試時，您也可以在本機防火牆上插上一隻手。



讓我們實際一點！



### II.透過 Nmap 掃描主機的 TCP 連接埠



#### A.使用 Nmap 進行第一次 TCP 連接埠掃描



現在我們要透過 Nmap 執行第一次掃描。我們的目標很簡單：我們要找出剛剛部署的 Web 伺服器暴露了哪些服務，看看是否有任何意料之外的情況，例如不該被存取的管理服務，或是暴露了我們以為已停用的應用程式的連接埠。



在我的範例中，要掃描的主機的 IP Address 為「192.168.1.18」：



```
nmap 192.168.1.18
```



以下是一個可能的結果。我們看到一個經典的 Nmap 返回值，包含大量資訊：



![nmap-image](assets/fr/11.webp)



使用 Nmap._ 執行簡單 TCP 掃描的結果



快速查看此結果後，我們瞭解到 TCP/22 和 TCP/80 連接埠可在此主機上存取。



根據預設，如果您沒有告訴它，Nmap 只會掃描 TCP 連接埠。



#### B.瞭解簡單 Nmap 掃描的結果



然而，讓我們更進一步來理解這個輸出：每一行都很重要，首先是要知道剛剛做了什麼，其次是要正確解釋掃描結果本身。



第一行基本上是提醒掃描版本和日期（畢竟對於記錄和歸檔很有用！）：



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



第二行顯示主機「debian.home (192.168.1.19)」的開始掃描結果。當我們同時開始掃描數台主機時，這些資訊將會很有用：



```
Nmap scan report for debian.home (192.168.1.19)
```



第三行告訴我們有問題的主機是 "Up"，也就是活動的：



```
Host is up (0.00022s latency).
```



最後，Nmap 通知我們有 998 個 TCP 連接埠被認定為關閉，但卻沒有顯示在 .NET 中：



```
Not shown: 998 closed tcp ports (conn-refused)
```



這可讓我們省下近 1,000 行看起來像 .NET 的輸出：



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



感謝他讓我們免受此苦！



為什麼是 998 "closed" ports?加上 2 個開放的連接埠就有 1000 個，這就是 Nmap 在預設設定中會掃描的連接埠數，而不是現有的 65535 個 TCP 連接埠！我們稍後會看到這是完全且容易自訂的。但是，如果目標主機有一個服務在一個相當特殊的連接埠上監聽，這個「預設」掃描就不會發現它。



在這些資訊之後，我們發現了最有趣的東西：一個根據「PORT - STATE - SERVICE」三列組織的表格：





- 第一列「PORT」僅表示目標連接埠/通訊協定，這裡重要的是看它是 TCP 連接埠 (`<port>/tcp`)，還是 UDP (`<port>/udp`)。





- STATE "列顯示在此連接埠上發現的網路服務的狀態，並由 Nmap 根據取得的回應決定。它可以是 "open"、"close"、"filtered 「或 」unknown"。我們稍後會看到 Nmap 如何區分這些不同的狀態。





- SERVICE "列表示暴露在相關連接埠上的服務。但是請注意，我們在這裡沒有使用主動服務發現選項。Nmap 依賴於連接埠/協定與據稱指定的服務之間的本地參考："/etc/services "檔案




如果您查看 Linux 系統上的 "/etc/services「 檔案，您會發現一個類似於 Nmap 所顯示的 」port/protocol - service" 連結：



![nmap-image](assets/fr/12.webp)



提取 Linux 下「/etc/services」檔案的內容。



重要的是要了解，目前 Nmap 還沒有執行任何主動的服務發現。例如，如果是這樣的話，它就無法識別 TCP/80 連接埠後的 SSH 服務。因此，知道如何使用正確的選項是很重要的 - 這很快就會發生！



知道如何解釋 Nmap 的輸出是掌握這個工具的重要部分。好消息是，無論您使用何種選項，輸出都大致相同。



#### C.引擎蓋下：透過 Wireshark 進行網路分析



如果您仔細看看掃描伺服器的主機或伺服器本身的網路 Interface 上發生了什麼事，Nmap 的動作會更清楚。這就是我們要做的。



我在這裡所能展示的，只是 Wireshark 中可見的一部分。如果您想要更進一步，可以在掃描時自己進行網路擷取，然後瀏覽擷取的內容。



在這個測試中，我的掃描主機 (192.168.1.18) 和我的目標主機 (192.168.1.19) 位於同一個區域網路。



Nmap 首先會透過傳送 ARP 請求，找出目標主機是否在本機網路中活動。如果收到回應，它就知道主機是活動的，並開始網路掃描：



![nmap-image](assets/fr/13.webp)



_ARP 請求由 Nmap 發出，以確定本機網路中是否有目標主機。



如果要掃描的主機位於遠端網路，Nmap 會先傳送 ping 請求，並嘗試接達一些最常暴露的連接埠 (TCP/80、TCP/443)：



![nmap-image](assets/fr/14.webp)



由 Nmap 發出的 ping 請求，以判斷目標主機在遠端網路中是否可以連線



如果它獲得任何這些測試的回應，它就會認為目標處於活動狀態。



一旦 Nmap 確定目標是活動的，它就會嘗試使用網卡上設定的 DNS 伺服器解析其網域名稱：



![nmap-image](assets/fr/15.webp)



Nmap 掃描目標的 dNS 解析度



現在 Nmap 已經識別了它的目標並且知道它是活動的，它開始它的 TCP 連接埠掃描：



![nmap-image](assets/fr/16.webp)



在 Nmap 掃描過程中傳輸 tCP SYN 封包和接收 RST/ACK



為此，它會在預設範圍內的每個 TCP 連接埠上，**發送 TCP SYN 封包並等待回應**。在上面的截圖中，它會從掃描的伺服器接收 TCP RST/ACK 封包，意思是「請繼續前進，這裡沒什麼好看的」 - 換句話說，這些連接埠是關閉的。正如我們在結果中看到的，大部分掃描的連接埠都是如此。有兩個例外：



![nmap-image](assets/fr/17.webp)



回應傳送至連接埠 22 的 TCP SYN 封包，在掃描目標上啟動



在上面的截圖中，我們看到目標主機**傳送的 TCP SYN/ACK 封包。這個連接埠是活動的，並暴露了一個服務。Nmap 確認收到回應，然後終止連線 (TCP RST/ACK)。 **這就是它如何知道 TCP/22 連接埠是活動的**。



我們在這裡看到 Nmap 在掃描 TCP 網路時尊重 "Three Way Handshake"。基於效能考量，可以要求它不回應伺服器的回傳，這樣在掃描大型網路時就可以省下幾千個封包。不過這些選項和優化功能我們會在稍後的教學中再介紹。



我們現在對如何執行 TCP 掃描，以及執行時實際會發生什麼有了更好的了解。我們也看到，在預設情況下，Nmap 會在有限的連接埠上執行 TCP 連接埠掃描。



### III.使用 Nmap 掃描 UDP 連接埠



#### A.使用 Nmap 進行第一次 UDP 連接埠掃描



現在讓我們看看如何掃描主機的 UDP 連接埠。如我們所見，預設 Nmap 會一直掃描 TCP 連接埠。如果我們沒有注意到，這可能意味著會錯過很多資訊。



提醒一下，在此測試中，我的掃描主機 (192.168.1.18) 和目標主機 (192.168.1.19) 位於同一個區域網路。



```
nmap -sU 192.168.1.19
```



在此，所獲得的回傳格式與 TCP 掃描相同，但所顯示的作用中服務會依要求以 `<port>/UDP` 的格式顯示！



![nmap-image](assets/fr/18.webp)



使用 Nmap 執行簡單 UDP 掃描的結果。



-sU "選項用來告訴 Nmap 你想在 UDP 上工作，而不是預設的 TCP。



順便說一下，您可能會注意到 Nmap 需要「root」權限才能進行 UDP 掃描，這在教程前面已經提到。



注意：自從最新版本的 Nmap 開始，建議使用管理員權限執行 UDP 掃描，以確保可靠的結果，因為某些功能需要原始的網路套接字存取權限。



UDP 掃描可能需要很長的時間 (在我的例子中掃描 1000 個連接埠需要 1100 秒)，這是因為 UDP 沒有 "Three Way Handshake「 (三方握手)，這表示 Nmap 會等待每個傳送的 UDP 封包的回覆，只有在經過一定時間 (timeout) 仍沒有回覆時，才會判定連接埠為 」關閉"。掃描主機的這種回覆是不系統性的，而且通常會限制每秒回覆的次數，以避免某些擴大攻擊。這與 TCP 相反，在 TCP 中，無論連接埠是開啟或關閉，掃描主機都會立即回應。我們稍後會看到如何優化這一點。



UDP 的第二個難點是**服務並不總是回應進入的封包**，很簡單，因為這並不總是必要的，而且這是 UDP 的原則。在這種情況下，如果沒有收到 ICMP "port unreachable「，服務就會被 Nmap 標記為 」open|filtered"，如上圖所示。



#### B.引擎蓋下：透過 Wireshark 進行網路分析



就像我們的 TCP 掃描一樣，讓我們使用 Wireshark 分析來仔細看看在 UDP 掃描時在網路層級發生了什麼。Nmap 判斷主機是否在活動的行為是一樣的。



掃描 UDP 時唯一真正的差異是 Nmap 不會等待「三方握手」，因為 UDP (無狀態通訊協定) 不存在這個機制：



![nmap-image](assets/fr/19.webp)



在 Nmap 掃描期間傳送 uDP 封包和接收 ICMP (連接埠不可達)



在上面的截圖中，我們可以看到 Nmap 將傳送大量的 UDP 封包，而大部分的封包都會收到一個 ICMP "Destination unreachable (Port unreachable)" 封包的回應。這是正常的，因為這是 [RFC 1122](https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122")定義的 UDP 連接埠不可達時的適當回應：



![nmap-image](assets/fr/20.webp)



摘自 RFC 1122._



讓我們仔細看看這個 Wireshark 擷取，它顯示了 UDP 中***的三種可能情況：



![nmap-image](assets/fr/21.webp)



使用 Nmap._ 在不同連接埠進行 UDP 掃描時的網路擷取。



這三種情況如下：





- 第一個 Exchange 由封包 No.3、4 和 8、9。Nmap 在傳統 SNMP 連接埠上傳送 UDP 封包，因此**會事先構成符合通訊協定的封包。然後從伺服器取得回應 (封包編號 8 和 9)。結果：Nmap 收到回應，服務「開放」。





- 第二個 Exchange 由封包 6 和 7 組成。Nmap 傳送一個「空」UDP 封包 (沒有通訊協定結構) 到連接埠 UDP/165，並收到一個 ICMP 封包回覆："Destination unreachable (Port unreachable)"。結果：Nmap 收到（負面）回覆，主機正常運作，但它嘗試連線的服務在此連接埠上無法運作，此連接埠將被標記為 「關閉」。





- 最後一個 Exchange 包含第 12 個封包：Nmap 傳送一個「空」UDP 封包到連接埠 UDP/1235。沒有回應，甚至沒有來自被掃描主機的明確拒絕。結果：Nmap 將連接埠標示為 "open|filtered"，因為它無法分辨這是因為防火牆的存在，設定為不回應，還是因為無論如何都不回覆的活動 UDP 服務 (在 UDP 中不是強制性的)。




以下是 Nmap 在這三種情況下所顯示的結果：



![nmap-image](assets/fr/22.webp)



透過 Nmap._ 執行 UDP 掃描的可能結果



現在我們對如何進行 UDP 掃描以及掃描時實際發生的事情有了更好的了解。到目前為止，我們只是以非常簡單的方式使用 Nmap，並沒有真正決定要掃描哪些連接埠，但這將會改變！



### IV.使用 Nmap 微調連接埠掃描



#### A.提醒 Nmap 的預設行為



正如我們所看到的，如果您沒有指定任何選項，Nmap 會自己選擇要掃描的號碼和連接埠。這是 Nmap 使用的「預設」配置，當您沒有告訴它要做什麼。這些預設選項的設計是為了讓您知道主要暴露的連接埠，這些連接埠是依據暴露的頻率 (最常見或最常使用的連接埠) 而選擇，而不是依據數字順序 (連接埠 1、2、3 等等)，也是為了避免在您沒有指定適當選項的情況下，開始掃描 65535 個可能的連接埠，因為對於 「預設」 使用情況來說，這些選項會太長而且字太多。



** 如何選擇這些連接埠？



在預設模式中掃描的 1000 個連接埠，是根據它們出現的頻率來選擇的。這些統計資料由 Nmap 維護，更新的方式與二進位檔本身及其腳本 (模組) 相同。您可以在 "/usr/shares/nmap/nmap-services" 檔案中自行檢視這些統計資料：



![nmap-image](assets/fr/23.webp)



從檔案 "/usr/shares/nmap/nmap-services"._ 中萃取。



在此，在第三列中，我們看到看起來像是概率（介於 0 和 1 之間）或百分比分佈。這是每個連接埠／協定對出現的頻率。我們可以看到，最知名的連接埠（本摘要中的 FTP、SSH、TELNET 和 SMTP）的值比其他連接埠高出許多。



#### B.精確指定 Nmap 掃描的目標連接埠



然而，在現實世界中，我們可能只需要掃描一個特定的連接埠，或幾個連接埠，或特定範圍的連接埠。Nmap 可以很容易地做到這一點，以統一的方式掃描 UDP 和 TCP。



**透過 Nmap**掃描特定連接埠



如果我們希望掃描單一連接埠，而不是 1000，我們可以透過 Nmap 的 "-p「 或 」--port" 選項指定此連接埠：



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



因此，掃描的速度自然會快很多，Nmap 只會發出偵測主機是否啟動所需的封包，然後再偵測指定的連接埠是否可連接。如果您只想執行快速測試，看看您的展示網站的 web 服務是否還在運作，這樣可以節省時間。



**透過 Nmap**掃描多個連接埠



同樣地，我們可以使用相同的選項指定多個連接埠給 Nmap，並以逗號連接指定的連接埠：



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



無論順序如何，Nmap 會檢查所有這些連接埠，而且只檢查目標主機上的連接埠。您會注意到在 Nmap 的輸出中，它**明確地告訴我們所有的連接埠和它們的狀態**，即使它們是 「關閉 」的。不像預設的行為，這樣完整的輸出會佔去太多的空間：



![nmap-image](assets/fr/24.webp)



*Nmap TCP 掃描指定連接埠的結果。



**掃描一系列連接埠



如果要掃描的連接埠數目太多，您可以依範圍指定，例如 ：



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



當然，您也可以隨心所欲地搭配，例如



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**TCP 和 UDP 連接埠掃描



您也可以同時對選定的連接埠執行 UDP 和 TCP 掃描：



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



在最後一個範例中，您會注意到「U:」表示 UDP 連接埠，而「T:」表示 TCP 連接埠。以下是此類掃描的可能輸出：



![nmap-image](assets/fr/25.webp)



*使用 Nmap.* 進行 TCP 和 UDP 連接埠掃描的結果



這是自訂掃瞄的有趣方式！



**掃描所有連接埠



最後，您可以指定更大或更小的範圍給 Nmap。我們已經看到 Nmap 預設選取的清單包含 1000 個 ports。我們也可以使用 "--top-ports" 選項，要求前 100 個最常出現的連接埠，或前 200 個：



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



最後，我們可以要求它掃描所有可能的連接埠（全部 65535），使用「-p-」符號：



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



後者需要較長的時間，尤其是 UDP，但您一定不會錯過任何開啟的連接埠。



*注意：「-p-」選項是掃描所有 TCP 連接埠的建議方法。對於 UDP 掃描，基於效能考量，建議限制埠數，因為完整掃描所有 UDP 埠可能需要很長的時間。



在後面的教學中，我們會看到如何優化 Nmap 的掃描速度以符合我們的需求，這對所有 TCP 和 UDP 連接埠的掃描特別有用。



### V.結論



在這一節中，我們終於有了一些實際的操作，所以我們現在知道了**如何以基本的方式使用 Nmap 來掃描主機的 TCP 和 UDP 連接埠**。我們也詳細瞭解了在網路層級發生的事情，以及 ** Nmap 如何判斷 TCP 或 UDP 連接埠是否有效**。最後，我們知道如何精確地選擇我們要掃描的連接埠，以及 ** Nmap 的預設選項實際上是做什麼的**。接下來，我們將重複使用這些知識，並應用於掃描整個網路，包括全局映射和網路發現。




## 5 - 使用 Nmap 進行網路映射與發現



### I.簡報



在本節中，我們將學習如何使用 Nmap 網路掃描工具來映射您的網路。我們將透過 Nmap 的各種選項，瞭解它在這項任務中的效能。最後，我們會看看向 Nmap 指定掃描目標的不同方法。



特別是，我們將運用在上一節所學到的關於 Nmap 如何判斷主機是否活動且可連線的知識。



正如在 Nmap 的介紹中所提到的，這是一個網路映射器。因此，無論是本機或遠端，它都是建立網路中可存取主機清單的完美工具。



**作者回顧：**



事實上，身為網路安全稽核人員和五元測試員，我在進行內部滲透測試時會有系統地使用 Nmap 來找出我的位置、本機網路上的鄰居、可存取的其他網路，以及位於這些網路上的系統。我的目標很簡單：映射網路、確定資訊系統的大小，尤其是勾勒出其攻擊面。



網路映射在網路診斷、監督、資產映射方面也很有用（您真的確定您的 IS 僅由 Active Directory 或 GLPI/OCS Inventory 中的內容組成嗎？它也可用於偵測資訊系統中是否存在影子 IT。



### II.使用 Nmap 掃描網路範圍



#### A.使用 Nmap 掃描發現網路



現在我們要更上一層樓，分析整個區域網路。沒有比這更簡單的：我們只需要重複使用上一節的指令，但指定 CIDR 而非簡單的 IP Address。



CIDR (**Classless Inter Domain Routing**) 是指定網路範圍及其範圍 (使用遮罩) 的「經典」記號。例如，「192.168.0.0/24」就是十進位遮罩符號「255.255.255.0」的「轉譯」。



要透過指定 CIDR 來使用 Nmap，我們可以如下使用：



```
# Scan a CIDR
nmap 192.168.0.0/24
```



也可以指定多個主機、多個網路或範圍 ：



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



以下是我們在網路上執行掃描可能得到的結果範例：



![nmap-image](assets/fr/26.webp)



Nmap 掃描的結果，以對應多個網路



特別是，我們看到幾個活動的主機，每個主機區段都以這樣的一行開始：



```
Nmap scan report for <name> (<IP>)
```



這可讓我們清楚看到下列結果是指哪一台主機。最後一行也很重要：



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



我們知道，在掃描的網路中，Nmap 發現了 5 台活動的主機。



#### B.引擎蓋下：透過 Wireshark 進行網路分析



我們現在要仔細看看透過 Nmap 執行網路發現時，在網路層級會發生什麼。



正如我們在上一節所看到的，預設 Nmap 會使用 ARP 通訊協定來偵測本機網路中是否有主機：



![nmap-image](assets/fr/27.webp)



使用 Nmap 及其預設選項掃描本機網路時擷取的 aRP 封包



因此，它幾乎可以偵測到本端網路上的所有主機，因為對 ARP 請求的回應通常是由網路上所有活躍的主機所提供，而且不會以任何方式顯得可疑。



對於遠端網路，Nmap 使用多種技術的組合：



![nmap-image](assets/fr/28.webp)



使用 Nmap 及其預設選項掃描遠端網路時擷取的 iCMP 和 TCP 封包



更精確來說，Nmap 使用 ICMP echo 封包（ping 的經典情況）和 ICMP Timestamp 封包，通常用來計算封包傳輸時間。它希望從遠端網路的主機得到回應。



但事情不只如此。您可以在上面的 Wireshark 擷取畫面中看到，**TCP SYN** 封包有系統地傳送至要掃描網路中每一台潛在主機的 TCP/443 連接埠，以及**TCP ACK** 封包的 TCP/80 連接埠。



**為何要傳送 TCP 封包到連接埠作為網路發現的一部分？



傳送 SYN 封包到指定的連接埠，讓 Nmap 可以 ** 判斷該連接埠上是否有服務在聆聽。如果主機以 SYN/ACK 封包回應 SYN 封包，這表示它是活動的，而且有服務在該連接埠上進行監聽。因此，Nmap 會在此服務上嘗試運氣，**即使沒有得到 ping 的回應**。



傳送一個 ACK 封包到指定的連接埠，讓 Nmap 可以**判斷該主機上是否有防火牆。如果主機以 RST (Reset) 封包回應 ACK 封包，這表示該主機上可能有防火牆，並封鎖未請求的流量。因此，即使主機沒有回應其他請求，也會暴露它在網路上的存在。



但必須注意的是，使用此技術的防火牆偵測並非在所有情況下都完全可靠。某些主機可能會因為防火牆存在以外的原因（例如特定服務或作業系統設定）而 generate RST 回應。此外，現代的防火牆可以設定為不回應此類型的發現嘗試。



我們現在已經有了長足的進步，可以執行基本的網路發現。我們現在要看看一些選項，這些選項可以讓我們對 Nmap 的行為有更大的控制。



### III.使用 Nmap 在沒有連接埠掃描的情況下發現網路



您可能已經注意到了，在預設情況下，Nmap 會在發現一個活動的主機後**執行一個連接埠掃描，這會增加大量的封包和等待我們掃描的回應。如果您的網路上有 5 台主機，Nmap 會嘗試檢查大約 5,000 個連接埠的狀態，這會花費更長的時間。



但是，可以使用 Nmap 的選項來執行 ** 僅發現網路中的活動主機**，而不發現它們的服務。



如果我們只想知道哪些主機是可以連到的，而不想知道它們暴露的服務和連接埠的任何資訊，那麼我們可以使用「-sn」選項來執行**僅使用 ICMP Echo (ping) 和 ARP 請求**的掃描。換句話說，完全停用連接埠掃描：



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



以下是 Nmap 在沒有連接埠掃描的情況下執行網路發現的結果：



![nmap-image](assets/fr/29.webp)



未使用 Nmap 進行連接埠掃描的網路發現結果。



我們已經提到單獨使用 ICMP 來發現主機（對於遠端網路）可能有的限制。這就是為什麼 Nmap 也使用一些技巧，可以洩露防火牆或主機上特定服務的存在。在選項的幫助下，我們可以重複使用這些技巧，甚至擴展它們，而不必重新開始對發現的每一台主機進行完整的連接埠掃描。



要做到這一點，我們將使用「-PS」（TCP SYN）和「-PA」（TCP ACK）選項，這將允許我們指定我們希望加入的連接埠，作為主機發現的一部分，以及「-PP」選項：



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



此掃描已確保主機發現比預設選項更完整。



我們開始使用相當全面的命令，使用多種選項。這是因為我們知道 Nmap 如何運作，以及其「預設」選項的限制，有時這些選項會讓我們浪費時間或錯過重要的 Elements。這就是花時間掌握它的目的！



詳述我們上次訂單的選項：





- "`-sn`: 禁用 Nmap 發現的每個活動主機的連接埠掃描。





- "`-PP`: 啟用 ICMP echo (ping 掃描) 來發現主機。





- "`-PS <PORT>`"： 在指定的連接埠上傳送 TCP SYN 封包，以偵測是否有未回應 ping 的主機存在。





- "`-PA <PORT>`"： 在指定的連接埠上傳送 TCP ACK 封包，以偵測是否有任何作用中的防火牆背叛了未回應 ping 的主機。




在上面的例子中，我為「-PS」選項指定了我認為在我的 Nmap 上下文中最常暴露的連接埠。然後，這些不同的連接埠就會在每一台主機上進行測試，不是要看它們所承載的服務是否真的活躍，而是要看這是否能讓我們發現一台沒有回應我們的 ICMP Echo 而仍然活躍的主機 (透過服務或主機防火牆的回應)。



以下是在進行此類掃描時，在單一目標主機上進行擷取的網路擷取結果：



![nmap-image](assets/fr/30.webp)



Nmap 在進階網路發現過程中所傳送的封包，無需連接埠掃描



我們找到 TCP SYN 封包、埠 TCP/80 上的 TCP ACK 以及 ICMP echo。Nmap 會針對我們網路發現掃描的目標主機執行所有這些測試。



### IV.使用資產檔案作為 Nmap 的目標



在現實生活的資訊系統中，指定目標可能很快就會變得複雜，因為有時資訊系統會由數十或數百個網路、子網路和 VLAN 組成。這就是為什麼使用檔案作為 Nmap 的來源比在命令列上逐一指定要容易的原因。



首先，建立一個簡單的檔案，每行包含一個項目：



![nmap-image](assets/fr/31.webp)



檔案，每行包含一個目標 (主機或網路)



接下來，我們可以使用目前看到的所有 Nmap 選項，並指定「-iL <path/file>」選項：



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



Nmap 將會掃描我們檔案中的所有目標。



如果您想確保所有的目標都會被考慮到，您可以使用 "-sL -n" 選項。這樣，Nmap 只會解釋檔案中的 CIDR 和主機，並將它們顯示給您，而不會在網路上傳送任何封包：



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



這可確保要掃描的主機清單是準確的。



我想與您分享的最後一個重要提示，是關於掃描**中的**主機或網路排除。在許多情況下，這種排除主機的需求可能是必要的，尤其是當我們想要確保**資訊系統的敏感元件不會受到我們掃描**的干擾或破壞時。



公司擁有工業 (PLC) 或醫療保健設備時，就是經常出現這種需求的例子。這些設備有時設計不佳，根本不是用來接收格式不佳或太多的封包。基於可用性或商業/人為風險的明顯理由，最好將它們排除在測試之外。



若要從我們的掃描排除 IP 位址或網路，我們可以使用 Nmap 的「--exclude」選項，例如 ：



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



在這個範例中，我掃描網路 "192.168.1.0/24「，但不包括位於該處的主機 」192.168.1.140"。Nmap 將不會傳送任何封包到這台主機。另一個子網路排除的範例：



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



同樣地，我掃描大型網路「10.0.0.0/16」，但不會掃描網路「10.0.100.0/24」。我再次建議您使用「-sL -n」選項，以非常清楚地瞭解哪些主機會被掃描，哪些主機會被排除在掃描之外，尤其是當您在敏感的環境下操作時。



### V.網路發現與連接埠掃描



現在我們可以把這一節所學到的和上一節關於端口掃描選項所學到的結合起來。在預設情況下，我們已經看到 Nmap 會掃描它發現的每一台主機上最常出現的 1000 個連接埠。我們已經看到如果我們不想要的話，如何阻止這個行為，但是我們可以完全控制它，甚至可以擴展它，如果它適合我們的需要。



例如，以下命令將檢查每台掃描的主機上是否存在連接埠 TCP/22 的監聽服務：



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



Nmap 會先執行網路發現，列出活動中的主機，並檢查每個主機的 TCP/22 連接埠上是否有服務存在。



同樣地，我們可以對「192.168.0.0/24」網路上發現的每一台主機的所有 TCP 連接埠執行完整掃描，例如排除主機「192.168.0.4」：



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



您可以自由結合我們目前所學到的所有選項，以符合您自己的需求。



### VI.總結



在本節中，我們已經看到如何使用 Nmap 的各種選項來映射網路。現在我們對掃描的目標，以及 Nmap 的連接埠掃描行為和主機發現方法有了微調的了解。最重要的是，我們知道 Nmap 的預設行為和限制是什麼，以及如何使用它的主要選項來更進一步。



在下一節中，我們將瞭解發現 Nmap 掃描的服務和作業系統版本的機制和選項。




## 6 - 使用 Nmap 檢測服務和作業系統版本



### I.簡報



在本節中，我們將學習如何使用 Nmap 來發現並準確偵測掃描主機所使用的服務和作業系統版本。我們將詳細瞭解 Nmap 如何完成這項任務，以及該工具的限制，以便更好地理解和解釋其結果。



正如我們在本教程前面幾節所看到的，在預設情況下，Nmap不會查看它掃描並認為開放的端口上暴露了什麼服務。因此，如果您在 TCP/22 端口上监听一个 web 服务，Nmap 将继续报告它是开放的，但是作为一个 `SSH` 服务。這是因為它使用您系統本地的 [資料庫](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) 來尋找連接埠/通訊協定和服務名稱 (`/etc/services/`檔) 之間的關係。



在大多數情況下，[Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) 會提供您正確的資訊，因為在生產環境中很少會發現這種情況。然而，剩餘的情況會是經典服務 ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/)、HTTP 等) 暴露在非經典的連接埠 (例如 SSH 服務的 2022)，在這種情況下，Nmap 在它的本機資料庫中找不到符合的資料，或是與現實不符的資料，您就會錯過重要的資訊。



幸運的是，Nmap 提供了非常精確的選項和機制來發現可能隱藏在開放連接埠後面的確切服務。它甚至有一個查詢和簽章資料庫，可以識別確切的技術和版本。除了服務之外，Nmap 也可以識別所使用的技術及其版本。



這就是我們要在本節中討論的內容。



### II.如何偵測技術或版本



#### A.提醒如何識別技術或版本



識別技術和版本涉及擷取在目標連接埠監聽的服務、CMS、應用程式或軟體的名稱。例如，網頁由 CMS (`WordPress`)管理，由網路服務 (`Apache`、IIS、Nginx) 執行，並由伺服器 (Linux 或 Windows) 主控。但您如何知道哪個網路服務正在執行？



找出這些資訊的經典方法是_banner grabbing_，簡單來說就是找出有關服務顯示這些資訊的位置並讀取資料。通常，在預設設定或處理中，服務會在連線後的第一個回應中顯示其名稱甚至版本。



![nmap-image](assets/fr/32.webp)



當 FTP 服務建立 TCP 連線時，立即顯示版本



在此我們可以看到，透過 `telnet` 與此服務進行簡單的 TCP 連線，會產生包含其技術和版本的 TCP 封包。



一旦您知道了您要處理的服務類型，您也可以傳送特定的指令或請求給該服務，從中擷取資訊。您也可以盲目地傳送這些要求/指令 (而不確定它們是否為正確的服務類型)，希望其中一個要求/指令能引起相關服務的回應。



在其他更進階的情況下，則必須傳送特定封包以引起反應，例如錯誤，這將提供所使用版本或技術的詳細資訊。



如您所想，Nmap 會使用所有這些技術，嘗試找出埠上託管服務的確切類型，以及其技術和版本的名稱。



#### B.瞭解 Nmap 探測和匹配



為了在每個掃描的連接埠上執行所有這些檢查，Nmap 使用一個經常更新的本機資料庫 (就像二進位檔或它的模組一樣)。這是一個有幾千行的文字檔：/usr/share/nmap/nmap-service-probes`。



此檔案由許多條目組成，所有條目都圍繞兩個主要準則組織：





- `Probe`: 這是 Nmap 將要傳送的封包的定義，嘗試激起要識別的服務的反應。把它想像成一個盲目的嘗試，就像 _Hello?Guten Tag?哈囉？或許是 Buenos Dias？一旦目標服務收到它能理解的探測 (也就是說正確的通訊協定)，它就會回應給 Nmap，Nmap 就能確認它是哪一種服務。





- Match"：這些是 Nmap 應用到所獲得的回應的正規表示式。如果傳送 HTTP GET 請求已引起服務的回應，它會對此回應套用數十個正則表 達式，以識別是否存在，例如，`Apache`、`Nginx`、`Microsoft IIS` 等字元。




還有一些其他的指令用於特定的情況，但對於了解 Nmap 如何運作和自訂它的使用來說，主要是這些指令。為了讓理論部分更具體，這裡有一個範例：



![nmap-image](assets/fr/33.webp)



Nmap`/usr/share/nmap/nmap-service-probes`檔中的Probe範例



在這個範例的第一行，我們看到一個名為 `GetRequest` 的簡單易懂的 Probe。這是一個 TCP 封包，包含一個空的 HTTP GET 請求，使用 HTTP/1.0 傳送至網路服務根，接著是換行和空行。



ports "行會告訴 Nmap 要傳送這個 Probe 到哪個連接埠。這可以讓您排定測試的優先順序，節省時間。



最後，我們有兩個 `match` 的範例。例如，第一個範例會將掃描的 Web 服務歸類為 `ajp13` 如果這一行所包含的正規表示式與收到的服務回應相符。



為了幫助您瞭解探針的外觀，這裡列出了一些您會在此檔案中找到的探針 (在撰寫本教學時，共有 188 個探針)。



![nmap-image](assets/fr/34.webp)



Nmap使用的幾個Probes的範例，這些Probes存在於文件`/usr/share/nmap/nmap-service-probes`._中。



前兩個（稱為 `NULL` 和 `GenericLines`）在此特別值得注意，因為它們只會傳送一個空的 TCP 封包或一個包含換行符的封包。伺服器服務通常會在收到連線時即刻宣告自己的存在，而不需要用戶端的任何特定動作、指令或請求。



以下是稍微複雜的 _match_ 的情況：



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



這裏的 `m|` 和 `|` 之間包含了確切的正則表達式，它限定了此檔案中的任何正則表達式。請花時間閱讀整個範例。您會注意到正規表達式中的一個選項：`([\d.]+)`，用來隔離一個版本。這個範例也定義了其他的 Elements，例如產品名稱 `p/nginx/`、擷取的版本 `v/$1/` 以及版本為 `cpe:/a:igor_sysoev:nginx:$1/` 的 CPE。



CPE (Common Platform Enumeration，共通平台枚舉) 是一套標準化的記號系統，用於識別並描述軟體與硬體。此格式可更有效率地管理弱點與安全配置，最重要的是，無論是何種產品，都能以統一的方式來表示。以下是兩個 CPE 的範例：`cpe:/o:microsoft:windows_8.1:r1` 和`cpe:/a:apache:http_server:2.4.35`。



在此，我們清楚地識別出 OS `o`、應用程式、廠商、產品和版本的類型。



因此，當 _match_ 與這些正則表達式之一匹配時，我們不僅會擷取服務的名稱，也會擷取它的版本和確切的 CPE，讓我們更容易找到影響這個版本的 CVE。您會在 Nmap 的標準輸出中找到這些資訊，而且您會發現這些資訊對其他用途非常有用，我們會在幾節中介紹。



_matches_ 的確切語法，更廣泛來說，在 `/usr/share/nmap/nmap-service-probes`檔中的指令，並不止於此，如果你不習慣操作 Nmap 和它的結果，可能會看起來相當複雜。然而，您至少應該記住它的存在和一般操作，這在您以後想要了解或除錯結果、自訂掃描或甚至為 Nmap 開發做貢獻時會很方便。



### III.使用 Nmap 檢測版本



現在我們要透過一個簡單的選項來使用所有這些複雜的 _Probe_ 和 _Match_ 機制： `-sV`。這簡單地告訴 Nmap：嘗試找出您設定為開放的服務和連接埠版本。



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



以下是一個完整的範例，說明這樣的指令所產生的結果：



![nmap-image](assets/fr/35.webp)



Nmap 對暴露在網路上的應用程式進行版本偵測的結果



在這裡我們可以看到 Nmap 已經成功識別出這個目標暴露的所有網路服務版本，並在新的 `VERSION` 欄中顯示這些資訊。如果這些資訊是復原簽章的一部分，就有可能看到相當精確的資訊，甚至可以精確到作業系統。



要詳細瞭解漏洞掃描時發生的事情，我們可以使用 `--version-trace` 選項。這將提供一個 debug 模式檢視，顯示導致偵測的 _Probe_：



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



因此，我們會有很多資訊需要整理。嘗試找出以 `Service scan Hard match` 開頭的行。然後您會看到像這樣的行：



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



我們可以清楚地看到哪些 _Probes_ 被用來偵測技術和版本 (在本例中為 `NULL` 和 `GetRequest` _Probes_) 以及擷取的資訊。



### IV.掌握測試和檢測精確度



現在我們要回到 `/usr/share/nmap/nmap-service-probes` 檔案中的指令，我們之前沒有看過這個指令：



![nmap-image](assets/fr/36.webp)



在 `/usr/share/nmap/nmap-service-probes`._ 檔案中的 probes `rarity` 指令



這個指令用來表示與 _Probe_ 相關的稀有度 (也就是優先順序/可能性)。這個從 1 到 9 的記號允許您控制 Nmap 在傳送 _Probes_ 時所執行的分析的完整性。在Nmap的 "notation "系統中，1的稀有度提供了絕大多數情況下的資訊，而8或9的稀有度代表了非常特殊的情況，特定於很少出現的配置或服務。



為了更清楚一點，在預設的情況下，Nmap 會傳送稀有度從 1 到 7 的 _Probes 到每個要被識別的服務。為了讓您更了解_Probes_在_rarity_的分佈，這裡是它們的數量：



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



看起來可能有點違反直覺，因為`稀有度`8 和`稀有度`9 比其他的要多。這正是因為稀有度 1 的探針是通用的，在大多數情況下都能運作，不論是什麼服務 (還記得 `NULL` 探針嗎，它只會傳送一個空的 TCP 封包)。而更複雜的探針幾乎對每個服務都是獨一無二的。



如果我們希望手動管理我們希望在版本掃描中使用的 Probes，我們可以使用 `--version-intensity` 選項。以下是兩個範例：



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



為了結束這個主題，這裡有一個 _Probe_ 9 和 8 的範例：



![nmap-image](assets/fr/37.webp)



檔案 `/usr/share/nmap/nmap-service-probes`._ 中稀有度為 8 和 9 的探針範例



這兩個 _Probes_ 會偵測 Quake1 和 Quake2 伺服器 (視訊遊戲)。對於懷舊的人來說很有趣，但在日常生活中應該用處不大。



根據您對精確度或速度的需求，請記住這個「稀有性」原則是存在的，而且會影響結果。



### V.使用 Nmap 檢測作業系統



現在我們來看看 Nmap 如何幫助我們偵測網路中被掃描及偵測到的主機的作業系統。要做到這一點，請使用 Nmap 的 `-O`（表示 `OS Scan`）選項。



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



以下是結果的範例。在這裡，Nmap 告訴我們這可能是一個 Linux 作業系統，並提供我們關於其精確版本的各種統計資料。



![nmap-image](assets/fr/38.webp)



偵測 Nmap 識別作業系統的機率



為了達到這個目的，Nmap 會使用許多技術，其工作方式與 _Probes_ 和 _Matches_ 的技術和版本偵測非常相似。主要的差別是 Nmap 會使用相當「低階」的 ICMP、TCP、UDP 和其他通訊協定的參數。以下是兩個偵測 Microsoft Windows 11 作業系統的測試範例：



![nmap-image](assets/fr/39.webp)



Nmap 測試 Windows 11 作業系統的範例



讓我們面對現實吧，這些測試是很難解釋的，我們不會在 Nmap 入門教學中嘗試深入了解它們。如果你想深入研究這個主題，包含這些資訊的檔案是 `/usr/share/nmap/nmap-os-db`。



然而，您需要注意的是，作業系統偵測是 Nmap 建立的一種可能性，而非必然性。



### VI.總結



在本節中，我們學習了如何使用 Nmap 的選項來檢測已掃描的主機和服務的技術、版本和作業系統。我們現在對 Nmap 如何從遠端取得這些資訊有了很好的了解。我們也檢閱了管理動詞和測試準確性的選項，以及工具在這些主題上的限制。



在下一節，我們將學習如何使用 Nmap 的 NSE 腳本來執行資訊系統的安全分析。如果需要的話，請花時間重讀上一節的內容，並且不要猶豫，親自練習和深入工具的內部，以便更好地掌握我們目前所學到的知識。




## 7 - 安全性分析：偵測弱點



### I.簡報



在本節中，我們將學習如何使用 Nmap 網路掃描工具來偵測和分析掃描目標上的弱點。特別是，我們將檢視完成這項任務的各種可用選項，並研究該工具功能的限制，以便更好地理解和詮釋其結果。



在第一節中，我們將介紹 Nmap 的漏洞掃描器，看看如何使用基本的漏洞偵測選項。在接下來的幾節中，我們將進一步了解這個功能如何運作，以及如何自訂。



### II.使用 Nmap 檢測弱點



我們現在要使用 Nmap 網路掃描器來偵測資訊系統的服務和系統中的弱點。這表示除了發現活動主機、枚舉暴露的服務以及偵測版本和技術之外，Nmap 還會尋找漏洞。



為了達成這個目標，Nmap 仰賴 NSE (_Nmap Scripting Engine_) 腳本，這些腳本可以被視為模組，可以實現粒度化的測試方法。



有了正確的選項，我們會要求 Nmap 在每個被發現的服務上使用它的各種 NSE 腳本，使我們能夠發現 .NET 服務：





- 組態故障 ；





- 額外和更先進的版本和作業系統發現；





- 已知漏洞 (CVE) ；





- 弱識別碼 ；





- 惡意軟體感染的特徵 Elements ；





- 拒絕服務的可能性 ；





- 等等。




如您所見，NSE 腳本大幅擴展了 Nmap 在執行網路作業方面的能力。而這要比以前執行更多的進階任務。好消息是，像往常一樣，這些功能可以簡單地通過選項和在預設上下文中使用。這就是我們接下來要看的。



### III.弱點掃描的範例



使用 Nmap 掃描主機上的單一連接埠、主機上的所有服務或在數個網路中偵測到的所有服務時，都可以使用 NSE 腳本。因此，我們可以在目前所學過的所有情境中使用我們即將看到的選項。



要透過 Nmap 掃描啟用漏洞掃描，我們需要使用 `-sC` 選項：



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



請記住，在預設情況下，如果您沒有指定任何東西，Nmap 只會掃描 1000 個最常見的連接埠。它不會偵測到您的目標可能暴露在較特殊的連接埠上的漏洞。



在生產資訊系統使用此功能之前，請您繼續閱讀本教學。在接下來的章節中，我們將探討如何更好地控制執行測試的影響和類型。



透過重複使用之前學到的知識，例如，我們可以更全面地掃描目標的所有 TCP 連接埠：



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



以下是使用 NSE 腳本進行 Nmap 掃描的結果：



![nmap-image](assets/fr/40.webp)



透過 Nmap._ 對主機進行漏洞掃描的結果範例



在這裡，我們可以看到在弱點分析中顯示的其他相關資訊：





- FTP 服務可以匿名存取，不受驗證保護。負責驗證的 NSE 腳本會告訴我們，甚至會顯示 FTP 服務的部分樹狀結構。這裡我們看到我們可以存取 Windows 系統的 `C` 目錄！





- 負責進階網路服務擷取的 NSE 腳本會顯示頁面標題，讓我們更清楚知道網路服務的主機。





- 我們還有一個 SMB 服務設定的小型分析 (腳本 `smb2-time`、`smb-security-mode` 和 `smb2-security-mode`)。這些資訊在網路掃描結果之後，以稍微不同的方式顯示，使其更容易閱讀。特別的是，此資訊顯示沒有 SMB Exchange 簽名。此設定弱點可讓目標用於 SMB Relay 攻擊，這是入侵/網路攻擊測試中常被利用的顯著安全漏洞。




當然，這只是其中一個例子。Nmap 有許多服務的 NSE 腳本，針對範圍廣泛的弱點。我們會在下一節仔細看看這些可能性。



為了結束這篇對弱點掃描的介紹，這裡有一個完整的命令，用於網路發現、TCP 連接埠掃描、版本和弱點偵測：



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



這裡有一個開始看起來比較實際的 Nmap 使用案例的命令！



### IV.瞭解 Nmap 在弱點掃描的限制



讓我們弄清楚：Nmap 無法對您的資訊系統進行完整的滲透測試，也無法模擬 Red Team 的作業。它有幾個限制，如果您不想有虛假的安全感，就必須了解這些限制：





- 有限的覆蓋範圍**：雖然Nmap的NSE腳本功能強大，但與其他專門的漏洞發現工具相比，其測試覆蓋範圍可能有限。某些弱點可能無法被可用的 NSE 腳本涵蓋，例如 Active Directory 弱點、敏感資料曝光或更進階的 Web 應用程式弱點案例。





- 漏洞複雜性**：某些類型的漏洞可能會因為其複雜性而很難使用 NSE 腳本偵測到。例如，需要與遠端服務進行複雜互動的漏洞可能無法被 Nmap 有效偵測（例如檔案共用中的過多權限或 Web 應用程式中的權限控制漏洞）。





- 被動偵測**：Nmap 主要專注於主動掃描來檢測漏洞，這意味著它可能無法在沒有與目標主機建立主動連接的情況下有效地檢測潛在漏洞。因此，在主動掃描期間沒有顯現的漏洞可能會被遺漏（例如 web 應用程式中的程式碼注入）。





- 依賴更新**：Nmap的NSE腳本[資料庫](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/)是不斷演進的，但是在發現新的弱點和增加相應的腳本到Nmap之間可能會有延遲。因此，Nmap 並不總是最新的漏洞。





- 假陽性和假陰性**：和任何安全工具一樣，Nmap 的 NSE 腳本可能產生假陽性（假漏洞警報）或假陰性（未檢測到真漏洞）。這是分析 Nmap 結果時要注意的。




因此，了解 Nmap 做了什麼和沒有做什麼是很重要的，同樣地，知道如何解釋其結果也是很重要的。特別是，我們在本教程中看到，預設選項可能會讓我們錯過重要的 Elements，但只要仔細使用就能發現。



無論您是網路系統管理員、安全工程師，甚至是 CISO，使用 Nmap 都能讓您概觀資訊系統的安全狀態。這是保障系統安全的重要第一步，IT 團隊可以定期執行。但是，它不應該取代 [網路安全] 專家 (https://www.it-connect.fr/cours-tutoriels/securite-informatique/) 的介入和建議，因為他們能夠發現的弱點遠比 Nmap 更為全面。



### V.結論



在第三單元的第一節，我們介紹了透過 Nmap 進行漏洞掃描。我們現在知道如何使用主選項來執行這項任務，但我們也知道這項練習的限制。在下一節中，我們將進一步了解這項功能，使用 NSE 腳本將 Nmap 的功能擴展十倍。



## 8 - 使用 Nmap 的 NSE 腳本



### I.簡報



在本節中，我們將對 NSE（_Nmap Scripting Engine_）腳本進行深入瞭解。特別是，我們將探討為何它們是此工具的強大優勢之一、它們如何運作，以及如何瀏覽和使用許多現有的腳本。



本節是上一教學的延續，在上一教學中，我們學習了如何以基本的方式使用 Nmap 的漏洞掃描功能。現在我們將進一步了解 [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/)在這方面的工作原理，以便我們可以再次進行更精確和可控制的掃描。



### II.Nmap NSE 腳本的概念



Nmap 的 NSE 腳本允許您以一種高度靈活的方式來擴展它的功能。它們是用 LUA 寫成的，LUA 是一種比 Nmap 使用的 C 或 C# 更容易處理和存取的腳本語言。將 LUA 腳本與 Nmap 搭配使用，而不是使用獨立工具的好處是，我們可以利用 Nmap 的執行速度和標準功能 (主機、連接埠和版本發現等)。



這些腳本依類別排列，單一腳本可能屬於多個類別：



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


技術上來說，腳本所屬的類別會直接在其程式碼中顯示。



![nmap-image](assets/fr/41.webp)



nSE 腳本類別 `ftp-anon`._



本範例顯示 NSE 腳本 `ftp-anon.nse` 的部分程式碼，我們在上一節看到其執行。



### III.列出現有的 NSE 指令碼



預設情況下，Nmap的NSE腳本位於`/usr/share/nmap/scripts/`目錄，沒有特定的樹狀結構或層次。下面是這個目錄的內容概覽：



![nmap-image](assets/fr/42.webp)



提取包含 NSE scripts._ 的 `/usr/share/nmap/scripts/` 目錄的內容。



此目錄包含 5,000 多個 NSE 指令碼。在大多數情況下，指令碼名稱的第一部分包含其所屬的通訊協定或類別。這可讓我們對清單進行排序，例如，如果我們希望列出所有以 FTP 服務為目標的指令碼：



![nmap-image](assets/fr/43.webp)



名稱以 `ftp-`._ 開頭的 NSE Nmap 指令碼清單



Nmap 並沒有提供瀏覽和列出其 NSE 腳本的選項；您可以使用命令 `--script-help`，後面跟著類別名稱或字詞 ：



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



不過，輸出會是每個指令碼的名稱及其說明，如果搜尋出數十個指令碼，這並非最佳選擇：



![nmap-image](assets/fr/44.webp)



使用 Nmap `--script-help` 指令的結果



我認為最有效的方法是使用 `/usr/share/nmap/scripts/` 目錄中的經典 Linux 指令：



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



請隨意瀏覽與您相關模組的程式碼，以便更好地瞭解 NSE 指令碼的運作方式。



### IV.使用 Nmap 的 NSE 腳本



現在我們要學習如何透過仔細選擇我們感興趣的 NSE 腳本來進行弱點掃描。



#### A.依類別選擇腳本



首先，我們可以選擇執行屬於特定類別的所有指令碼。我們需要用參數 `--script <category>` 來向 Nmap 指出這個類別或這些類別：



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



第一個指令等同於 `nmap -sC` 指令。預設情況下，Nmap 會選擇 `default` 類別的 scripts，但這只是為了方便爭論。例如，下一個指令會使用 `discovery` 類別中的所有指令碼：



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



如我們所見，有些類別可讓我們快速識別相關 NSE 指令碼的作用 (`discovery`、`vuln`、`exploit`)，而其他類別則定義所執行測試的風險、偵測或穩定性等級。如果我們處於敏感的情境中，無法很好地掌握腳本選擇所執行的不同動作，我們可以選擇結合選擇，只選擇那些屬於「發現」和「安全」類別的腳本：



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



如果您絕對且明確地想要從 `dos` 和 `intrusive` 類別中排除指令碼，您可以使用下列符號：



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



請注意，如上所述指定排除條件會導致使用所有其他未明確排除的類別。為了更公平，我們可以指定，例如：



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



以下是一些按類別處理 NSE scripts 的範例，尤其是在實際環境中使用 Nmap 進行弱點分析時。



#### B.選擇腳本為單元



我們也可以選擇在分析期間執行單一特定測試，也就是與 NSE 指令碼相對應的測試。要做到這一點，我們需要在 `-script <name>` 參數中指定腳本的名稱。以 `ftp-anon.nse` 脚本为例：



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



我們就可以得到非常精確的結果：



![nmap-image](assets/fr/45.webp)



透過 Nmap._ 在 FTP 連接埠使用 NSE `ftp-anon` 指令碼的結果



我們看到在連接埠 21 執行 `ftp-anon` 指令碼的結果，沒有其他連接埠，因為我們指定了 `-p 21` 選項。我們也可以執行基本的連接埠掃描，只在發現的 FTP 服務上執行 `ftp-anon` NSE 指令碼：



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



因此，如果 Nmap 在另一個連接埠上找到 FTP 服務，它也會執行這個匿名連線測試。



如需 NSE 指令碼的簡要說明，您可以使用上述的 `--script-help` 選項：



![nmap-image](assets/fr/46.webp)



幫助顯示 NSE 腳本 `sshv1`._ 的結果



簡而言之，我們可以再次重複使用到目前為止的所有網路發現選項、服務、版本和技術！



#### C.管理腳本參數



在使用 Nmap 的過程中，您會遇到某些 NSE 腳本需要輸入參數才能正常運作。現在我們來看看如何透過 Nmap 的選項來傳遞參數給這些腳本。



以 `ssh-brute` 腳本為例，它可讓您對 SSH 服務執行暴力攻擊。



典型的暴力攻擊包括測試多個密碼（有時數以百萬計）以嘗試驗證特定帳戶。藉由嘗試這麼多個密碼，攻擊者賭的是使用者在用於攻擊的密碼字典中使用了弱密碼的可能性。



這個腳本有 「預設 」的選項，我們可以自訂以符合我們的情況。例如，在本攻擊的上下文中，我們可以向 Nmap 提供使用者清單和要使用的密碼字典。據我所知，不可能輕易列出腳本所需的參數，所以最可靠的方法是造訪 Nmap 官方網站。回應 `--script-help` 選項，可以得到 NSE 腳本說明文件的直接連結：



![nmap-image](assets/fr/47.webp)



顯示 NSE `ssh-brute` 腳本說明的結果，並連結至 nmap.org._



點擊指定的鏈接，我們就到達了網站 [https://nmap.org](https://nmap.org/) 的這個網頁：



![nmap-image](assets/fr/48.webp)



可以傳給 Nmap `ssh-brute` NSE 指令碼的參數清單



在這裡我們可以清楚的看到可以使用的參數，在我們的上下文中主要是 `passdb`（包含密碼清單的檔案）和 `userdb`（包含使用者清單的檔案）。這裡的說明文件指的是 Nmap 內部的函式庫，因為這些暴力破解機制和相關的選項是互通的，可以在幾個腳本中統一使用 (`ssh-brute`、`mysql-brute`、`mssql-brute` 等)，因此或多或少會有相同的參數：



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



在最後這個命令中可以看到，我們可以使用 `-scripts-args key=value,key=value` 選項來指定 Nmap 腳本的必要參數。下面是通過 `ssh-brute` NSE 腳本執行 SSH 暴力破解時，Nmap 輸出的可能結果：



![nmap-image](assets/fr/49.webp)



透過 Nmap._ 強行執行 SSH 的結果



如您所見，NSE 腳本所產生的資訊在互動式輸出(終端輸出)中以`NSE: [script name]`為前綴，使其更容易被找到。在通常的 Nmap 結果顯示中，我們只是有一個摘要，顯示是否發現了弱識別碼 (包括密碼，記住)。



為了讓事情更進一步，並提醒您這一切都可以用在我們已經看過的所有選項之外，這裡有一個命令，可以發現 `10.10.10.0/24` 網路、掃描 2000 個最常見的 TCP 連接埠，並對 FTP 服務執行匿名存取搜尋，以及對 SSH 服務執行暴力攻擊：



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



這只是眾多可用腳本及其選項中的一個例子。但我們現在對如何掌握 NSE 腳本、它們是否需要參數以及如何將這些參數傳給 Nmap 有了更好的了解。



### V.結論



在本節中，我們學習了如何使用Nmap的NSE腳本來執行各種任務。我邀請您花點時間去發現不同類別的腳本和腳本本身，看看它們可以自動執行多少測試。



幾節以來，我們已經累積了或多或少的進階發現、掃描和枚舉選項。到現在，您應該知道 Nmap 的輸出和結果顯示開始變得相當廣泛，有時甚至對我們的終端機來說太冗長了。在下一節中，我們將學習如何掌握這些輸出，特別是將它存儲到各種格式的文件中。






## 9 - 管理 Nmap 輸出資料




### I.簡報



在本節中，我們將看一下 Nmap 產生的輸出，特別是格式化輸出的各種選項。我們會看到 Nmap 可以產生多種輸出格式來滿足不同的需求，而這也是這個工具的強項之一。



預設情況下，Nmap 提供掃描和測試結果的詳細檢視。這包括掃描的主機和服務、檢測到可存取的主機和服務、開啟埠的具體情況、其狀態和版本。此外，NSE 腳本的詳細資訊也可在終端機輸出中找到。不過，即使資訊格式清楚，這些輸出也可能很快就變得浩如煙海，讓人很難在結果中找到精確的資訊。



### II.掌握 Nmap 輸出格式



#### A.將掃描結果儲存為文字檔



為了讓事情更簡單，[Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) 可以很容易地將其輸出儲存為文字檔。這對於存檔、與其他測試比較，以及使用專門的文字處理工具或腳本語言（例如 Sublime text、[PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/)、Python、grep、sed 等）來瀏覽這些輸出都很有用。要將 Nmap 的標準輸出儲存到一個文字檔中，我們可以使用 `-oN <filename>` 選項 ("normal 「中的 」N") ：



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



沒什麼好驚訝的，Nmap 會在我們的終端顯示它通常的標準輸出，但也會在指定的檔案中顯示。



#### B.generate 精簡格式的 Nmap 輸出



在「文字」樣式中還有第二種輸出格式，可以很容易地被人類解讀：「可繪圖」格式。



創建這個格式是為了提供一個 Nmap 輸出的 「濃縮 」視圖，其結構可以方便`grep`等工具處理。讓我們來看看這類輸出的範例：



![nmap-image](assets/fr/50.webp)



nmap 網路掃描並以 "greppable" 格式輸出。



在這裡，我執行了網路發現、連接埠掃描，以及分析 /24 網路上的技術和版本，然後將輸出存成「可擷取」格式的檔案。最後我得到一個檔案，裡面每個活動主機有兩行：





- 第一行告訴我這樣或那樣的主機是 _Up_；





- 第二行會告訴我哪些連接埠已被掃描、它們的狀態，以及以特定格式擷取的技術和版本資訊：`<連接埠>/<狀態/<協定>//<服務>//<版本>/,`




這種使用固定分隔符的格式可以讓文字處理工具 (例如 `grep`)，或腳本和程式語言快速處理。舉例來說，在 Nmap 執行了龐大的掃描，其輸出很難瀏覽的情況下，以下的指令可以讓我輕鬆地擷取主機 `10.10.10.5` 的資訊：



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



相反地，我也可以輕易列出所有開啟連接埠 21 的主機，因為連接埠和 IP 位於同一行：



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



要 generate 這樣的輸出，我們需要使用 `-oG <filename>.gnmap` 選項 ("grep 「中的 」G")。根據習慣，我在這裡使用 `.gnmap` 副檔名來表示這樣的檔案，但您也可以隨意使用您喜歡的副檔名：



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



此格式可用於多種用途，對於快速腳本/排序尤其有用。儘管如此，它有被拋棄的趨勢，而改用我們接下來要看的格式。



注意: `-oG` greppable 格式自 Nmap 7.90 起已被正式廢棄。它仍然可以用於相容性。它仍然可以用於相容性目的，但建議您使用 XML 或一般格式來進行任何開發或自動化解析。



#### C.Nmap 輸出的 XML 格式



本教學值得一提的最後一個格式是 XML。與前兩種格式不同，這種格式並非設計供人類讀取，而是供其他工具或腳本讀取。



XML (_eXtensible Markup Language_) 是一種用於儲存和傳輸資料的標記語言，透過自訂標籤提供分層結構。



在 Nmap 中，XML 格式用來 generate 執行掃描的詳細報告，包括偵測到的主機、連接埠和弱點資訊，以及標準 Nmap 輸出中未顯示的其他資訊。



要 generate XML 格式的輸出檔案，我們需要使用 `-oX` 選項 ("XML 「的 」O") ：



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



結果是 Nmap 在您終端的標準輸出，以及在您目前目錄中的 XML 格式檔案。



當然，XML 格式不是設計給人類讀取和詮釋的。儘管如此，如果您想對這種格式的 Nmap 輸出做腳本或自動化分析，您仍然需要對所使用的標籤和結構有所了解。例如，下面是Nmap創建的XML文件的部分內容，它顯示了1台主機的掃描結果：



![nmap-image](assets/fr/51.webp)



在 Nmap 掃描中 1 台主機的 XML 記錄範例



這裡有很多資訊，我們對兩個開放的連接埠特別感興趣：



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



我們了解到這種格式將有助於自動解析結果，因為每項資訊都整齊地排列在專屬、命名的標籤或屬性中。特別的是，我們發現了一項以前從未遇過的資訊：CPE。



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



我們在模組 2 的第 2 節簡略提到 CPE，此資訊是在版本偵測時以匹配方式決定的。Nmap 使用其服務、技術和版本偵測機制來尋找相關的 CPE。



這樣我們就可以在使用這些資訊的資料庫和應用程式中重複使用這些資訊。我特別想到參考 CVE 的 NVD 資料庫。對於每個 CVE，它包含受該漏洞影響的 CPE。以下是 NVD 資料庫中關於 `a:microsoft:internet_information_services:7.5` 的 CVE 的範例：



![nmap-image](assets/fr/52.webp)



在 NVD 資料庫的 CVE 詳細資料中出現 CPE



我們現在對這種格式的好處有了更深入的了解，它提供了非常清楚的資訊結構，並包含 Nmap 所收集或處理的所有資料。



作為一種反射，我系統地一次以所有三種格式儲存我的 Nmap 掃描。這是由 `-oA <name>` 選項 ("A 「代表 」All")促成的，它會建立一個 `<name>.nmap` 檔案、一個 `<name>.xml` 檔案和一個 `<name>.gnmap` 檔案。如此一來，當我需要回顧結果時，就不會有任何遺漏。



有了這三種格式，你應該有了保存和最終自動處理 Nmap 結果所需要的一切。我們會在下一節再次使用 XML 格式，那時我們會看看如何使用 Nmap 與其他安全工具。



#### III.從 Nmap 掃描產生 HTML 報告



XML 格式提供了許多可能性，其中最重要的是，它可以作為產生 HTML 格式報告的基礎，而 HTML 格式的報告在視覺上更容易瀏覽。



要將 XML 格式的 Nmap 檔案轉換成網頁，我們會使用 `xsltproc` 工具，我們需要先安裝這個工具：



```
# Install the xsltproc tool
sudo apt install xsltproc
```



安裝此工具後，只要提供要轉換的 XML 檔案和要產生的 HTML 報告名稱即可：



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



如此一來，我們的整個掃描就會有很好的結構，甚至在目錄中還會有一些顏色和可點選的連結！



![nmap-image](assets/fr/53.webp)



從 xsltproc._ 產生的 HTML 格式 Nmap 掃描報告中摘錄



概括來說，Nmap 儲存的 XML 檔案包含對另一個 XSL 格式檔案的參照：



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



因此，轉換為 HTML 是 Nmap 提供並促進的功能，`xsltproc` 是執行此任務的常用且公認的工具 (它不來自 Nmap 工具套件)。



XSLT (_Extensible Stylesheet Language Transformations_) 是 XSL 的子集，它允許 XML 資料顯示在網頁上，並與 XSL 風格並行「轉換」為 HTML 格式的可讀性格式化資訊。



來源：[helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_



報告的資訊等級等同於 Nmap 的 XML 格式，高於標準終端輸出 (_interactive output_)。



### IV.管理 Nmap 的冗長程度



現在我們來看看 Debugger Nmap 或追蹤進度的幾個選項。



我們應該提到的第一個選項是`-v`選項，它可以增加Nmap的verbosity。下面是一個例子：



![nmap-image](assets/fr/54.webp)



nmap 使用 `-v`._ 選項的詳盡輸出



在針對許多主機和連接埠的掃描中，由於顯示的資訊太多，終端輸出將變得難以利用。因此，這個選項應該和前面的選項結合使用，這些選項允許您把 Nmap 的標準輸出儲存到一個檔案中。與使用verbosity有關的資訊不會包含在這個輸出檔案中。從上面的範例可以看到，這個verbosity可以讓您清楚直接地追蹤Nmap的動作和發現。對於資料顯示可能較慢的長時間掃描，這可以避免對 Nmap 目前的活動視而不見，並知道事情的進展和速度。若要再增加一層級的動態度，您可以使用 `-vv` 選項。



要進一步追蹤 Nmap 在掃描期間的活動，可以使用 `--packet-trace` 選項。使用 `-v` 選項，我們會得到 Nmap 發現的所有開啟埠的即時日誌，而使用這個選項，我們會得到每個傳送到埠的封包的日誌行。這自然會產生一個非常冗長的輸出，但是允許詳細的監控Nmap的活動，下面是一個例子 ：



![nmap-image](assets/fr/55.webp)



透過`--packet-trace`._詳細監控 Nmap 活動。



同樣地，如果使用了 `-oN`、`-oG`、`-oX` 或 `-oA` 選項，這些資訊將不會記錄在 Nmap 產生的輸出檔案中。



最後，Nmap 也提供兩個偵錯選項：`-d`和`-dd`。這些選項的行為類似於 `-v` verbosity 選項，但增加了額外的技術資訊，例如在掃描開始時的技術參數摘要：



![nmap-image](assets/fr/56.webp)



時序選項會顯示在 Nmap 的除錯檢視中



在接下來的幾節中，我們會看看「時間」選項有哪些，以及為什麼值得了解這些選項。



最後，如果您只想要一個基本的、合成的 Nmap 掃描進度概觀，您可以使用 `--stats-every 5s` 選項。這裡的 "5s "是指 5 秒，可以依您的需求修改。這是我們從 Nmap 收到進度回饋的頻率：



![nmap-image](assets/fr/57.webp)



Nmap的`--stats-every`選項所顯示的資訊



特別是，我們可以取得進度百分比，以及所處階段的指示：透過 [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/)發現主機階段、發現暴露的 TCP 連接埠階段等。這些資訊也可以在掃描的過程中按下「Enter」從終端輸出中取得。



然而，Nmap 不擅長估計任務所需的時間，尤其是因為它無法預先知道有多少主機和服務需要掃描。



### V.結論



在本節中，我們瞭解了許多以不同檔案格式儲存 Nmap 掃描結果的選項。這將會非常方便，因為在現實環境中，掃描結果可能會佔去幾百甚至幾千行！我們也看到如何增加Nmap的verbosity等級來進行除錯或取得掃描進度報告。



XML 格式在下一節會特別有用，在這一節我們會看看一些可以處理 Nmap 結果的工具。




## 10 - 與其他安全工具一起使用 Nmap



### I.簡報



在本節中，我們將看一下 Nmap 與其他免費和開源安全工具的一些經典用法。特別是，我們將運用前幾節所學到的知識來進一步增強 Nmap 的功能和效率。



以 XML 儲存 Nmap 掃描結果的能力使資料與許多其他工具相容。由於目前幾乎所有的程式設計和腳本語言都有能夠解析 XML 的函式庫，這使得處理這些資料變得更容易。許多工具，尤其是針對攻擊性安全的工具，都有處理 Nmap 所產生的 XML 格式的功能。讓我們仔細看看。



我會提到一些攻擊性的工具，但不會詳細說明它們的使用方式或運作原理。我會假設讀者熟悉這些工具的基本用法，而且它們已經可以運作。[網路安全] 專業人員 (https://www.it-connect.fr/cours-tutoriels/securite-informatique/)、受訓中的人員或決定深入研究此主題的人士會對本節特別感興趣。



### II.將 Nmap 結果匯入 Metasploit



我們要瞭解的第一個在攻擊性安全和弱點研究中重複使用 Nmap 資料的工具是 Metasploit。



Metasploit 是一個攻擊框架。它是一個免費的解決方案，也是一個公認的工具，包含大量以 Ruby 或 Python 寫成的模組。這些模組可讓漏洞被利用、進行攻擊、產生後門、管理回呼 (C&C 或通訊與控制功能) 以及統一使用所有東西。



尤其是，這個廣為人知、廣泛使用的作業架構可以與 postgreSQL [資料庫](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/)一起運作，其中儲存了主機、連接埠、服務、驗證資訊等。





- Metasploit 官方文件：[https://docs.metasploit.com/](https://docs.metasploit.com/)




這就是 Nmap 及其輸出發揮作用的地方，因為 Nmap 輸出的 XML 格式可以輕鬆匯入 Metasploit 的資料庫，以填充其主機和服務資料庫，然後可以快速指定這些主機和服務為此或彼攻擊的目標。



一旦進入 Metasploit 互動式 shell，我就會先建立一個工作區，一種特定於我當天環境的空間：



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



我的工作區建立後，我們需要驗證與資料庫的通訊是否正常運作：



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



最後，我們可以使用 Metasploit `db_import` 指令以 XML 格式匯入我們的 Nmap 掃描：



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



以下是執行所有這些指令的結果：



![nmap-image](assets/fr/58.webp)



將 XML 格式的 Nmap 掃描匯入 Metasploit 資料庫



在此您可以看到每台主機及其服務都已匯入。這些資料可以透過特定服務的 `services` 或 `services -p <port>` 指令來顯示：



![nmap-image](assets/fr/59.webp)



從 XML 檔案匯入 Metasploit 資料庫的服務清單



最後，我們可以快速輕鬆地在模組中重複使用這些資料，這要歸功於 `-R` 選項，它會「轉換」所獲得的服務清單，作為 `RHOSTS` 指令的輸入，用來指定要進行攻擊的目標。下面是一個使用 `ssh_login` 模組的範例，它可以讓您對 [SSH] 服務進行暴力攻擊 (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/)：



![nmap-image](assets/fr/60.webp)



使用 `services -R` 選項匯入指定為攻擊目標的服務



這只是在 Metasploit 中使用 Nmap 資料的一個小例子，但它讓您對這些資訊可以如何快速輕鬆地重複使用，作為滲透測試、弱點掃描或網路攻擊的一部分，有了一個小小的概念。值得一提的是，Nmap 可以直接從 Metasploit 執行，將結果匯入資料庫（指令 `db_nmap`），這是另一個有趣的主題！



### III.使用 Nmap 與 Aquatone 網路掃描器



在重複使用 Nmap 結果以進行攻擊性安全與弱點分析這一節中，我要介紹的第二個工具是 Aquatone。



Aquatone 是一款網頁掃描器，設計用來有效率地探索網路中的網頁應用程式。它提供先進的 Web 服務發現、子網域識別、連接埠分析和 Web 應用程式指紋分析功能。所有功能均以 HTML、JSON 及文字報告的方式簡明呈現，讓您輕鬆進行網路安全分析。



如同 Metasploit，Aquatone 可以直接處理 Nmap 的 XML 格式，並將其作為掃描的目標。特別是，它可以從 Nmap 報告可能包含的所有資料中，只抽取出有興趣的主機和服務 (web 服務)。





- 工具連結：[Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)




要在 Aquatone 中使用 Nmap 的 XML 輸出，只要將 XML 檔案傳送至 Aquatone 的管道即可。以下是一個範例：



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Aquatone 通常會在主機上執行連接埠發現，以尋找網路服務，但在此情況下，它將完全依賴 Nmap 的結果，因為 Nmap 已經執行這項作業，因此可以節省時間：



![nmap-image](assets/fr/61.webp)



使用 XML 格式的 Nmap 結果與 `aquatone`._



以下是 Aquatone 所製作報告的摘錄，供您參考：



![nmap-image](assets/fr/62.webp)



報告範例



就我個人而言，我經常使用 Aquatone 來快速概覽網路上的網站類型，特別要感謝它的螢幕截圖功能。



同樣地，擁有 XML 格式的完整 Nmap 報告可以節省時間，並方便在其他工具中重複使用。



### IV.結論



這兩個例子清楚顯示，Nmap 的 XML 格式讓其他工具很容易使用它的結果，因為它是一種結構化、容易使用的資料格式。有許多其他工具能夠處理這些結果，例如自動報告工具、圖形表示法或更複雜的專屬弱點掃描器。



當然，您也可以使用 Python、[PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) 或任何其他具有 XML 解析函式庫的語言來開發您自己的腳本和工具，以便在您認為合適的情況下操作和重複使用 Nmap 結果資料。



本節是 Nmap 進階使用教學模組的尾聲，特別是透過 NSE 腳本進行漏洞掃描。



本教學的下一節將著重於，除其他事項外，一些額外的、更具技術性的最佳實踐，以及 Nmap 可以執行的特定掃描的提示。我們也會看看掃描效能最佳化選項，這些選項在掃描大型網路時特別有用。




## 11 - 改善網路掃描效能



### I.簡報



在本章中，我們將學習如何通過使用各種特定的選項來優化使用 Nmap 執行的網路掃描的速度。特別是，我們將學習更多關於 Nmap 的內部運作，從 _timeout_ 管理到工具的預存配置。



既然我們已經詳細瞭解了 Nmap 的功能，現在讓我們來了解一下這個怪獸和它的威力。如果您曾經在大型網路中使用過這個工具，您可能已經注意到，儘管這個工具功能強大，有些掃描還是需要很長的時間。這是有充分理由的：一個簡單的 `nmap` 指令加上幾個選項就可以 generate 數百萬個封包，目標是數十萬個潛在的系統和服務。



更重要的是，有些網路設備配置可能會故意強制較慢的速率（每秒封包數量），冒著拒絕您的封包或基於安全理由禁止您的 IP Address 的風險。



視情況而定，可能值得嘗試優化這一切，我們會在本章中看到。



無論如何，您可以透過 Nmap debug (選項 `-d` 見上一章) 檢查我們要看的參數的預設值，以及您要使用的選項是否已被正確考慮：



![nmap-image](assets/fr/63.webp)



透過 Nmap 的 `-d` 選項檢視 Timing 選項。



### II.管理 Nmap 掃描的速度



#### A.管理平行化



預設情況下，Nmap 在掃描中使用平行化來優化掃描，它使用的所有參數都可以通過各種選項來修改。然而，實際上需要修改這些參數的情況相當少，所以我們不會在本教程中詳細說明：





- `--min-hostgroup/max-hostgroup <size>`：平行主機掃描群組的大小。





- `--min-parallelism/max-parallelism <numprobes>`：探針的平行化。





- `-scan-delay/-max-scan-delay <time>`：調整探針間的延遲。




只要知道它們存在並可以使用即可。



#### B.管理每秒封包數量



預設情況下，Nmap 本身會根據網路回應調整每秒傳送的封包數量。但是可以透過定義每秒封包數的最高值和/或最低值來強制這個設定。這個設定是使用選項 `--min-rate<number>`和 `-max-rate<number>`，其中 `number` 代表每秒的封包數量。範例：



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



這些選項允許您根據您的特定需求調整掃描速度，可以加快掃描過程，也可以限制使用的頻寬。後一種情況 (限制掃描速度) 最有可能讓您使用這些選項，尤其是當您在使用 Nmap 時遇到網路延遲 (這種情況相當罕見)。



### III.管理連線故障和超時



另一個我們可以用來優化 Nmap 掃描速度 (或保證更高準確度) 的參數是 _timeout_ 和 _retry_。



對於 _timeouts_，這是 ** 沒有回應的逾時時間，** 之後 Nmap 將停止等待回應，並視該服務或主機為不可達。對於 _retry_，這是 Nmap 在繼續之前會執行的 ** 連續嘗試操作的次數**。



與平行化一樣，_timeout_ 和 _retry_ 管理可應用於主機或服務發現階段：





- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>`：指定 Exchange 的往返時間。同樣地，這個參數實際上是在掃描的過程中計算和調整的。您不太可能需要使用它，因為 Nmap 會根據網路反應即時計算這個時間。





- `-max-retries <number>`：限制在連接埠掃描時重傳封包的次數。預設情況下，Nmap 對單一服務最多可以重試 10 次，尤其是在發現網路層級的延遲或損失時，但大多數情況下只執行一次。





- `--host-timeout <time>`：指定Nmap在一台主機上進行所有操作的最長時間，包括端口掃描、服務偵測，以及任何其他與該主機相關的操作。如果超過這個時間間隔而沒有任何回應或**完成操作**，Nmap 會放棄這台主機而不顯示任何與它有關的結果，並移到它清單中的下一台。這允許您控制 Nmap 花在指定主機上的最長時間，避免卡在頑固的主機上，並最佳化整體掃描時間。




在我的日常工作中，我使用 `-max-retries` 和 `--host-timeout` 選項來優化掃描：



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



這些參數提供了額外的彈性，可根據特定需求和網路條件調整掃描行為。不過，您必須瞭解這些參數對掃描主機負載的影響，以及可能造成的精確度損失。



### IV.使用準備好的配置



我們在本章看到的各種選項可以單獨使用，也可以作為Nmap提供的現成配置的一部分。使這些_templates_(配置模板)能夠被使用的選項是 `-T <number>`或 `-T <name>`。有 5 個可用的 _templates_ 層級：



```
-T<0-5>: Set timing template (higher is faster)
```



預設情況下，Nmap 使用 _template_ 3 (_normal_)，這通常就足夠了。



就我而言，我通常在需要相當快速 (同時盡可能保持完整) 的情況下運作，而且我經常使用 `-T4` 選項。



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



以下是此掃描的除錯資訊：



![nmap-image](assets/fr/64.webp)



在 Nmap 掃描中使用 `-T4` 設定



### V.結論



在本章中，我們瞭解了您可以用來管理 Nmap 的能力、侵略性和效能的各種技術和選項。這些選項在掃描大型網路時特別有用，更罕見的是用於隱身目的。



在下一章，我們會看看使用 Nmap 並確保其安全性的一些最佳實務。




## 12 - 使用 Nmap 時的資料安全性與機密性



### I.簡報



在本章中，我們將探討關於 Nmap 所產生、處理和儲存的資料的安全性，尤其是機密性的一些良好實務。



在資訊系統中使用 Nmap 很快就會被歸類為攻擊性的行為。因此，需要採取許多預防措施，以便在法律框架內行事，同時保證預期目標、收集的資料和掃描所用系統的安全。



### II.取得適當授權



掃描網路或系統之前，請確定您已取得適當的授權。未經授權掃描系統的弱點 (「NSE scripts」) 可能是非法的，而且可能會有法律後果，尤其是當資訊系統安全不屬於您的官方職權範圍時。





- 作為提醒：[《刑法典》：第三章：攻擊自動資料處理系統](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




### III.保護敏感資料



Nmap 產生的結果可被視為敏感，尤其是當這些結果包含資訊系統中可能被攻擊者利用的弱點資訊時。但是，當這些結果涉及到不是每個人都能存取的系統 (例如敏感、工業、醫療保健或 [備份] 資訊系統 (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/))，也是如此。



我們也看到，根據所使用的 NSE 腳本，[Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) 的 NSE 掃描結果也可能包含識別碼。



因此，惡意的個人若能存取這些掃描結果，就能掌握資訊系統的地圖和豐富的技術資訊，而無需親自執行這些動作，也不會有被偵測到的風險。



因此，在使用 Nmap 時，務必注意不要不當地收集或儲存敏感資訊，包括但不限於下列資訊：





- 加密輸出資料：如果您需要儲存或傳輸 Nmap 掃描的結果，請務必加密以保護資料的機密性。這將防止未經授權攔截敏感資訊。理想情況下，資料一離開執行掃描的系統就應該加密（用強密碼加密的 ZIP 檔案是個很好的開始）。





- 設定存取控制：確保只有經過授權的人才能存取儲存 Nmap 掃描結果的地方。設定適當的存取控制，以保護敏感資訊免於未經授權的存取。





- 處理資料時的警覺性：在傳輸、複製或處理掃描資料時，請務必嚴格控制資料的安全性。這表示：不要讓它們隨處亂丟在連線至網際網路的工作站的「Download」目錄中，不要讓它們透過您的內部 HTTP 檔案 Exchange 應用程式傳輸，不要在午休時打開記事本而不鎖定工作站，等等。




### IV.管理侵略性掃描



正如我們在本教程中所看到的，Nmap 在網路層級上可以非常冗長。它也可以傳送格式不正確的封包，並且在它產生的網路訊框和封包中不嚴格遵守通訊協定結構。所有這些行為都會對某些系統和服務造成影響，有時甚至會導致系統和網路資源故障或飽和。



為了避免任何事故，你需要掌握Nmap的行為，並知道如何通過本教學討論的各種選項，使它適應使用的環境。在包含工業[硬體](https://www.it-connect.fr/actualites/actu-materiel/)的資訊系統中，我們使用Nmap的方式不一定和在由Windows系統組成的用戶網路中或在網路核心中使用Nmap的方式一樣。



希望本教學中的各種課程能讓您學會如何掌握和分析 Nmap 的行為，但最好的學習方式還是要靠實踐。所以確保您熟悉您要使用的 Nmap 選項。



### V.保護掃描系統



在第一章中，我們看到在大多數情況下，Nmap需要以`root`或本地管理員的身份運行。這是因為它透過網路函式庫執行網路操作，有時是在相當低的層級上，從系統穩定或其他應用程式的機密性的觀點來看，這些操作需要高風險的權限。



因此，Nmap 可被視為安裝它的系統的敏感元件。請務必使用最新版本的 Nmap，因為舊版本可能包含已知的安全漏洞。通過使用最新版本，您可以將使用該工具的風險降到最低。



如果您選擇不以`root`的會話身份使用Nmap，而是賦予有權限的使用者特定權限，讓他擁有使用Nmap所需的一切（`sudo`或_capabilities_），請注意Nmap可以作為完整的權限提升的一部分：



![nmap-image](assets/fr/65.webp)



透過 `sudo`._ 提升 Nmap 權限



在這裡，我透過 `sudo` 使用 Nmap 指令，但這讓我可以在系統上以 `root` 的身分取得互動 shell，這並不是我原本的目標。



在不是為執行網路掃描而設計的系統上安裝 Nmap 也是非常不可取的。我特別想到伺服器或工作站。一方面，這會增加權限提升的潛在媒介，但最重要的是，這會讓攻擊者毫不費力地取得攻擊工具。



最後，必須更廣泛地確保掃描所使用系統的安全性，以免其本身成為入侵或資訊洩漏的媒介。身為系統管理員，最好使用專用系統，最好是有使用期限的系統，而不是自己的工作站。



### VI.總結



總而言之，在實際生活或生產環境中使用 Nmap 之前，請確保您已正確掌握，並在處理和管理其結果時保持警覺。如果最初的目的是改善公司的安全性，但卻造成損害、洩漏資料或促成洩密事件，那就太可惜了。



## 13 - 透過 TCP 進行連接埠掃描：SYN、Connect 和 FIN



### I.簡報



在本章和下一章中，我們將從最常用的 TCP 掃描開始，仔細瞭解 Nmap 提供的不同類型的 TCP 掃描：SYN、Connect 和 FIN 掃描。



您可能已經注意到，Nmap 提供多種 TCP 掃描選項：



![nmap-image](assets/fr/66.webp)



Nmap._ 中提供的掃描技術



這裡的想法是要解釋其中一些方法，幫助您瞭解它們的差異、優點和限制。您會發現，依據不同的情境或您想知道的事情，選擇其中一種或另一種方法會比較好。



### II.TCP SYN 掃描或 "Half Open 掃描



我們要看的第一種 TCP 掃描是 `TCP SYN Scan`，也稱為 `Half Open Scan`。如果您還記得我們在第一次埠掃描後做過的網路掃描，這是 [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) 以 root 權限執行時預設使用的掃描類型。



這個翻譯可以幫助您了解這個掃描的運作方式。事實上，TCP SYN 掃描會傳送一個 TCP SYN 封包到每個目標連接埠，這是用戶端 (要求建立連線的用戶端) 傳送的第一個封包，是著名的 _Three way handshake_ TCP 的一部分。通常，如果目標伺服器上的連接埠是開放的，並有服務在其後運行，伺服器會傳回一個 TCP SYN/ACK 封包，以驗證用戶端的 SYN 並初始化 TCP 連線。此回應會以 SYN 和 ACK 旗標設定為 1 的 TCP 封包形式傳送，讓我們可以確認連接埠已開啟，並可連接到服務。



另一方面，如果連接埠被關閉，伺服器會傳送一個 RST 和 ACK 旗標設定為 1 的 `TCP` 封包給我們，以終止連線請求，這樣我們就會知道這個連接埠後面似乎沒有服務在運作：



![nmap-image](assets/fr/67.webp)



開啟和關閉連接埠的 tCP SYN Scan 行為圖表



為了更具體地瞭解 `TCP SYN Scan` 的情況，我對 TCP/80 連接埠進行了掃描，掃描的主機在此連接埠上安裝了活動的 Web 伺服器。使用 Wireshark 執行網路掃描，我們可以看到以下流程 (掃描來源：`10.10.14.84`)：



![nmap-image](assets/fr/68.webp)



在 TCP SYN 掃描開放連接埠時進行網路擷取



在第一行，我們看到掃描來源正在傳送 TCP 封包到主機 `10.10.10.203` 的 TCP/80 連接埠。在這個 TCP 封包中，SYN 標誌被設定為 1，表示這是一個 TCP 連線初始化請求。



然後，在第二行，我們看到目標回應了一個 `TCP SYN/ACK`，這表示它接受初始化連線，因此可以接收 TCP/80 連接埠上的串流。因此，我們可以推斷 TCP/80 連接埠是開啟的，而且掃描的伺服器上有網頁伺服器。



然後我們的主機會傳回一個 RST 封包來關閉連線，讓被掃描的主機不再維持開啟的 TCP 連線等待回應。在掃描許多連接埠的情況下，不關閉 TCP 連線可能會導致拒絕服務，使伺服器可維持等待回應的連線數量達到飽和（請參閱 [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood)）。



在 Wireshark 中，您可以看到我們執行的每個測試的 TCP 標誌狀態。這會顯示封包是否為 SYN、SYN/ACK、ACK 等封包：



![nmap-image](assets/fr/69.webp)



在 Wireshark 中檢視封包的 TCP 標誌 (TCP SYN 在此)



相反地，我在兩台機器之間執行相同的測試，但這次掃描的是沒有服務啟動的 TCP/81 連接埠（掃描來源：`10.10.14.84`）：



![nmap-image](assets/fr/70.webp)



在 TCP SYN 掃描關閉的連接埠時進行網路擷取



當連接埠未開啟時，掃描的主機會回傳一個 `TCP RST/ACK` 來回應我的 `TCP SYN` 。



如前所述，當從特權終端執行 Nmap 時，TCP SYN Scan 是預設模式，可以透過 `-sS` (`scan SYN`) 選項強制執行：



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




由於速度的關係，「TCP SYN 掃描」是最常用的掃描。另一方面，如果在伺服器上觀察到客戶端無法完成 _Three Way Handshake_ (也就是在伺服器 SYN/ACK 之後，沒有傳送 ACK) 的情況太多次，或是來自網路上的相同來源，就可能會讓人覺得可疑。事實上，用戶端在收到回應 TCP SYN 的 TCP SYN/ACK 封包後的正常行為是傳送「確認」(ACK)，然後開始 Exchange。



儘管如此，它的掃描速度還是稍微快了一點，因為它不需要為每個正面回應傳送 ACK。SYN Scan 的優點在於它的速度，因為每個要掃描的連接埠只會傳送一個封包，但卻犧牲了更大的偵測機會。



此外，TCP SYN 掃描能夠偵測連接埠是否被防火牆過濾（保護）。事實上，目標主機前方的防火牆在收到其應該保護的連接埠上的 TCP SYN 封包時，可以透過其行為偵測出來。它根本不會回應。但是，正如我們所見，在這兩種情況下（開啟或關閉連接埠），主機都會有回應。這第三種行為將揭示在被掃描主機和執行掃描的機器之間存在防火牆。下面是當掃描的連接埠被防火牆過濾時，Nmap 可以回傳的結果：



![nmap-image](assets/fr/71.webp)



nmap 在掃描已篩選連接埠時顯示



當我們在掃描時執行網路擷取，實際上可以看到沒有回應：



![nmap-image](assets/fr/72.webp)



在 TCP SYN 掃描防火牆過濾的連接埠時進行網路擷取



封閉連接埠和過濾連接埠的差別如下：過濾連接埠是受防火牆保護的連接埠；而封閉連接埠是沒有服務執行的連接埠，因此無法處理我們的 TCP 封包。某些類型的 TCP 掃描 (例如 TCP SYN 掃描) 可以偵測連接埠是否已被過濾，而其他類型的掃描則無法偵測。



### III.TCP 連線掃描或完全開啟掃描



第二種 TCP 掃描是 `TCP Connect 掃描`，也稱為 _Full Open Scan_。它的工作方式與 TCP SYN 掃描相同，但這次會在伺服器作出正面回應 (SYN/ACK) 後傳回「TCP ACK」。這就是為什麼它被稱為 `Full Open'，因為連線是完全開啟的，並在掃描期間開啟的每個連接埠上啟動，因此尊重 TCP _Three Way Handshake_：



![nmap-image](assets/fr/73.webp)



開啟和關閉連接埠的 tCP Connect Scan 行為圖表



以下是針對開放連接埠進行「TCP Connect 掃描」時，可以看到的網路傳輸內容：



![nmap-image](assets/fr/74.webp)



在 TCP Connect 掃描開放連接埠時進行網路嗅探



我們可以看到，第一個傳送的 TCP 封包是客戶端傳送的 `TCP SYN`，伺服器接著會回覆一個 `TCP SYN/ACK`，表示這個連接埠是開放的，並寄存了一個活動的服務。為了一路模擬合法的客戶端，Nmap 接著會傳送一個 `TCP ACK` 回給伺服器。相反地，當掃描一個封閉的連接埠 ：



![nmap-image](assets/fr/75.webp)



在 TCP Connect 掃描關閉的連接埠時進行網路擷取



請注意，伺服器對我們的 `SYN` 封包的回應再次是一個 `TCP RST/ACK` 封包，因此我們可以推斷出連接埠已關閉，而且沒有服務在上面執行。



使用Nmap時，`-sT`(`scan Connect`)選項用來執行TCP連線掃描。請注意，當 Nmap 是從非授權的會話使用時，這是預設的 TCP 掃描模式：



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



TCP 連線掃描」模擬更合法的連線請求，其行為最接近 lambda 用戶端，因此較難發現掃描的連接埠數量減少。不過，它的速度較慢，因為它會完全初始化掃描機器開放連接埠上的每個 TCP 連線。



如果安裝了網路入侵偵測與防護服務 (IDS、IPS、EDR)，Nmap 掃描 10,000 個連接埠還是很容易被偵測到。當攻擊者想要保持低調時，他會傾向於專注於少數策略性選擇的連接埠，例如 445 (SMB) 或 80 (HTTP)，這些連接埠經常在伺服器上開啟，並且存在常見的漏洞。



由於 TCP Connect Scan 在這兩種情況下都會期望回應，因此它也可以偵測到目標主機上是否存在可能過濾連接埠的防火牆。



### IV.TCP FIN 掃描或 "隱形掃描



TCP FIN Scan」，也稱為 _Stealth Scan_，使用用戶端終止 TCP 連線的行為來偵測開啟的連接埠。



在 TCP 中，會話結束表示傳送 FIN 標誌設定為 1 的 TCP 封包。在正常的 Exchange 中，伺服器會停止與用戶端的所有通訊 (沒有回應)。如果伺服器與用戶端之間沒有活動的 TCP 連線，就會傳送一個 `RST/ACK`。因此，我們可以透過傳送 `TCP FIN` 封包到一組連接埠來區分開放與關閉的連接埠：



![nmap-image](assets/fr/76.webp)



開啟和關閉連接埠的 tCP FIN 掃描行為圖



我再次在 _Stealth scan_ (隱形掃描) 時擷取網路，這就是您在掃描埠開啟時看到的畫面：



![nmap-image](assets/fr/77.webp)



在 TCP FIN 掃描開放連接埠時進行網路擷取



我們可以看到用戶端傳送一到兩個封包來終止 TCP 連線，而伺服器並沒有回應。它只是接受連線結束，並停止通訊。



下面是我們現在掃描封閉的連接埠時看到的情況：



![nmap-image](assets/fr/78.webp)



在 TCP FIN 掃描關閉的連接埠時進行網路擷取



我們看到伺服器傳回一個 `TCP RST/ACK` 封包，所以開放的埠和關閉的埠在行為上是有差異的，我們可以透過傳送 TCP FIN 封包來列出伺服器上開放的埠。使用 Nmap，`-sF`(`scan FIN`) 選項用來執行 TCP FIN Scan：



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



TCP FIN Scan 在 Windows 主機上不起作用，因為當傳送至未開啟的連接埠時，作業系統傾向於忽略 TCP FIN 封包。因此，如果您在 Windows 主機上執行 TCP FIN Scan，您會得到所有連接埠都關閉的印象。



因此，熟悉幾種掃描方法並瞭解它們之間的差異非常重要。



由於在任何一種情況下，TCP FIN 都不會等待回應，因此無法偵測目標主機與掃描來源之間是否存在防火牆。



以下是 Nmap 的 TCP FIN 掃描結果範例：



![nmap-image](assets/fr/79.webp)



Nmap 的 TCP FIN 掃描結果。



事實上，主機在指定連接埠上沒有回應可能表示該連接埠已被過濾，但也可能表示該連接埠是開放且活躍的。



這種掃描被稱為「隱形」，因為它不會產生 generate 許多流量，通常也不會造成目標系統的日誌記錄。它可以用來謹慎地發現網路中的連接埠，而不會引起任何警報。不過，如上所述，它的有效性可能因目標系統而異，也可能因安全設備的組態而異。



### V.結論



關於 Nmap 提供的不同 TCP 掃描類型的兩章中的第一章到此為止！在下一章，我們將看 XMAS、Null 和 ACK TCP 掃描類型，它們以不同的方式來偵測主機上開啟的連接埠。





## 14 - 透過 TCP 進行埠掃描：XMAS、Null 和 ACK



### I.簡報



在本節中，我們將繼續探索 Nmap 提供的各種 TCP 掃描方法。這裡我們將看一下 `XMAS`、`Null` 和 `ACK` 方法，這些方法使用 TCP 特定的功能來擷取指定目標上開啟的連接埠和服務的資訊。



### II.TCP XMAS 掃描



XMAS Scan TCP 有一點不尋常，因為它完全沒有模擬正常使用者或機器在網路上的行為。事實上，XMAS Scan 在傳送 TCP 封包時會將旗標 `URG` (Urgent), `PSH` (Push) 及 `FIN` (Finish) 設為 1，以繞過某些防火牆或過濾機制。



XMAS 這個名稱的由來，是因為看到這些旗標亮起是不尋常的。當 TCP 封包中的三個旗標同時設定時，看起來就像一棵點亮的聖誕樹：



![nmap-image](assets/fr/80.webp)



XMAS 掃描中使用的 tCP 標誌



這裡不詳細說明這些標誌的作用，重要的是要知道，當發送封包時啟用了這三個標誌，目標連接埠後的活動服務將不會傳回任何封包。另一方面，如果連接埠關閉，我們就會收到 TCP RST/ACK 封包。現在我們可以在列出機器上的連接埠時，區分開放與關閉連接埠的行為：



![nmap-image](assets/fr/81.webp)



開啟和關閉連接埠的 tCP XMAS Scan 行為圖表



仍然依照相同的邏輯，在偵測到開放連接埠 (掃描來源 `10.10.14.84`)時，對一台有使用中 Web 伺服器的主機的 TCP/80 連接埠進行網路掃描，會顯示下列行為：



![nmap-image](assets/fr/82.webp)



在 TCP XMAS 掃描開放連接埠時進行網路擷取



我們可以看到掃描來源傳送兩個 TCP XMAS 封包 (旗標 `FIN`、`PSH` 和 `URG` 設為 1) 到主機 `10.10.10.203`，而目標沒有回傳，表示連接埠是開放的。相反，在封閉的連接埠上執行 `TCP XMAS Scan` 時，會觀察到以下結果：



![nmap-image](assets/fr/83.webp)



在 TCP XMAS 掃描關閉的連接埠時進行網路擷取



我們的 TCP 封包的回應是 `TCP RST/ACK`，表示連接埠已關閉。要在 Nmap 中使用此技術，`-sX`(`scan XMAS`)選項允許您執行 TCP XMAS Scan：



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



值得注意的是，TCP XMAS 掃描無法偵測目標與掃描機器之間可能存在的防火牆，這與 TCP SYN 或 Connect 等其他掃描類型不同。事實上，如果目標連接埠已被過濾 (即受防火牆保護)，兩台主機之間的主動防火牆將可確保沒有 TCP 回傳。因此，在沒有回應的情況下，無法知道該連接埠是受到防火牆保護，還是開放且活躍。您也應該注意，就像 TCP FIN 掃描一樣，某些應用程式或作業系統 (例如 Windows) 可能會扭曲此類掃描的結果。



注意：最近版本的 Windows 對 XMAS/FIN/NULL 掃描的支援仍然有限，在此類目標上的結果可能不一致。(2025年更新)_



### III.TCP 空掃描



與 TCP XMAS 掃描相反，TCP Null 掃描會傳送所有旗標都設定為 0 的 TCP 掃描封包。這也是在機器間正常 Exchange 中永遠不會發現的行為，因為在描述 TCP 通訊協定的 RFC 中並沒有指定傳送沒有旗標的 TCP 封包。這就是為什麼它比較容易被偵測到。



與 TCP XMAS 掃描一樣，此掃描會干擾某些防火牆或過濾模組，允許封包通過：



![nmap-image](assets/fr/84.webp)



開啟和關閉連接埠的 tCP Null Scan 行為圖表



以下是在開放連接埠進行 TCP Null 掃描時，在網路上可以看到的情況：



![nmap-image](assets/fr/85.webp)



在 TCP Null 掃描開放連接埠時進行網路擷取



掃描機器會傳送一個無旗標的封包 (在 Wireshark 中為 `[<None>]`)，但伺服器不會有任何回應。相反地，當目標連接埠關閉 ：



![nmap-image](assets/fr/86.webp)



在 TCP Null 掃描關閉的連接埠時進行網路擷取



要使用 Nmap 執行 TCP Null 掃描，只需使用 `-sN` (`scan Null`) 選項：



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



由於連接埠開啟時的回應和防火牆啟動時的回應（兩種情況下都沒有伺服器回饋）完全相同，因此 TCP Null scan 無法偵測到防火牆的存在。更重要的是，防火牆甚至可能偽造結果，暗示連接埠是開啟的，因為它不會回應沒有標記的 TCP 封包，即使連接埠已被過濾。在使用無法區分開放連接埠與已過濾 (防火牆保護) 連接埠的掃描時，例如「TCP Null」、「XMAS」或「FIN」掃描，這是需要注意的重要資訊，以便在詮釋所得結果時保持一致。



### IV.TCP ACK 掃描



TCP ACK 掃描用於偵測目標主機上或目標與掃描來源之間是否存在防火牆。



與其他掃描不同，TCP ACK 掃描不會嘗試辨識主機上哪些連接埠是開啟的，而是嘗試辨識過濾系統是否啟動，對每個連接埠都會以 `filtered` 或 `unfiltered` 來回應。某些 TCP 掃描 (例如 `TCP SYN` 或 `TCP Connect`) 可以同時執行這兩項工作，而其他 TCP 掃描 (例如 `TCP FIN` 或 `TCP XMAS`) 則完全無法判斷是否存在過濾。這就是 TCP ACK 掃描可以發揮作用的原因：



![nmap-image](assets/fr/87.webp)



已過濾和未過濾連接埠的 tCP ACK Scan 行為圖表



我們使用 Nmap 的 `-sA` 選項來執行這類掃描。下面是 TCP ACK 掃描的結果，如果連接埠被過濾，也就是被防火牆封鎖和保護：



![nmap-image](assets/fr/88.webp)



在 TCP ACK Scan._ 期間 nmap 顯示



有防火牆和無防火牆主機的結果範例。Nmap 在主機 `10.10.10.203`的埠 TCP/80 和 TCP/81 上回傳 `filtered`。在透過 Wireshark 進行網路分析時，行為如下：



![nmap-image](assets/fr/89.webp)



在針對未被防火牆過濾的連接埠進行 TCP ACK 掃描時，進行網路擷取



如果存在防火牆，目標機器不會回傳任何資訊。



要使用 Nmap 啟動此掃描，請使用 `-sA` (`掃描 ACK`) 選項：



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V.結論



除了已介紹的方法外，我們還看了三種不同的 TCP 掃描方法。這些不同的方法必須在非常特定的條件和情境下使用，尤其是在滲透測試或紅色小組 (Red Team) 作業的情境下，因為在此過程中會有謹慎的概念。



## 15 - Nmap CheatSheet - 指南命令摘要



### I.簡報



這裡是 Nmap 許多指令和使用案例的簡短摘要，讓您可以在日常使用中快速找到並重複使用。



### II.Nmap：CheatSheet IT-Connect



以下是所介紹命令的小抄。這個頁面讓您輕鬆找到 Nmap 最常見的用法。





- 埠掃描




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- 發現使用中的主機




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



注意: `-sP`選項已經過時數年，應以`-sn`取代。(2025年更新)_



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- 版本偵測




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- NSE 指令碼：尋找漏洞




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Nmap 輸出管理




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- 效能最佳化




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- TCP 掃描類型




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



希望這些指令對您有用。不要忘記根據您的情況調整掃描的目標，並參考官方說明文件以完全掌握所執行的測試。



### III.總結



Nmap 教學到此為止。您現在已經掌握了使用這個全面且功能強大的工具所需的基本知識。我們強烈建議您先在受控環境 (Hack The Box、VulnHub、虛擬機器) 中練習，然後再在生產中使用。



關於這個工具的內部運作和進階功能，還有許多有待探索的地方。然而，掌握這裡所介紹的命令和概念將使您能夠自信地使用 Nmap，並使其具有實用性。