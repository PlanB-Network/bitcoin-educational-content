---
name: Lynis
description: 使用 Lynis 執行 Linux 機器的安全稽核
---
![cover](assets/cover.webp)



___



*本教學依據 Fares CHELLOUG 於 [IT-Connect](https://www.it-connect.fr/) 發表的原始內容。原始碼授權類型 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有變更。



___



## I.簡報



**在本教程中，我們將學習如何使用 Lynis 在 Linux 機器上執行安全稽核！對於那些不知道**Lynis 的人來說，**它是一個小型的命令列工具，可以分析您伺服器的配置，並提出**改善機器安全性的建議。



Lynis 是 CISOFY 的開放原始碼工具，CISOFY 是一家專門從事系統稽核與強化的公司。如果您想在加固 Linux 和常用服務 (SSH、Apache2 等) 方面取得進展，Lynis 就是您的盟友！Lynis 不僅會告訴您哪裡出了問題，還會提供建議，為您指出正確的方向 (並節省您的時間)。



**Lynis** 可與大多數 Linux 發行版搭配使用，包括 **Debian、FreeBSD、HP-UX、NetBSD、NixOS、OpenBSD、Solaris**。Lynis 主要針對 Linux / UNIX 使用者，但也相容於**macOS**。安裝非常快速，在套件層級上沒有相依性管理。



它有多種用途：





- 安全稽核
- 合規性測試（PCI、HIPAA 和 SOX）
- 更強大的系統組態
- 漏洞偵測



系統管理員、IT 稽核人員和五測人員等廣泛使用者都廣泛使用此工具。在分析方面，該工具是以**CIS Benchmark、NIST、NSA、OpenSCAP**等標準，以及**Debian、Gentoo、Red Hat**的官方建議為基礎。



該專案可在 **Github** 上的此 Address 處取得：





- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [從 CISOFY 下載 Lynis](https://cisofy.com/lynis/#download)



在這個逐步教學中，我將**使用一個執行 Debian 12 的 VPS**，我將專注於 SSH 部分，因為我想檢查其設定並加以改善。



## II.下載與安裝



有幾種方式可以下載和安裝 Lynis。請從下列清單中選擇您喜歡的一種。



### A.從 Debian 套件庫安裝



此安裝模式允許您在系統上的任何地方使用 **lynis** 指令，不像從原始碼安裝，您需要位於目錄中。



透過 SSH 連接到您的伺服器，並輸入下列指令來安裝 Lynis ：



```
sudo apt-get update
sudo apt-get install lynis -y
```



這就是您所得到的：



![Image](assets/fr/024.webp)



### B.從官方網站下載



您也可以從 Cisofy 網站下載：



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



這就是您所得到的：



![Image](assets/fr/032.webp)



接下來，我們使用下列指令解壓縮歸檔：



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



這就是您所得到的：



![Image](assets/fr/020.webp)



讓我們移到 **lynis** 資料夾：



```
cd lynis
```



我們可以使用下列指令檢查更新：



```
./lynis update info
```



這就是您所得到的：



![Image](assets/fr/023.webp)



### C.從 GitHub 下載



我們將從官方 GitHub 套件庫下載 **Lynis**，請使用下列指令（您的機器上必須有 *git*）：



```
git clone https://github.com/CISOfy/lynis.git
```



這就是您所得到的：



![Image](assets/fr/060.webp)



## III.使用 Lynis



Lynis 已經出現在我們的機器上，讓我們來學習如何使用它！



### A.主要控制和選項



若要顯示可用的指令，只需輸入下列指令：



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe:
./lynis
```



這就是您所得到的：



![Image](assets/fr/039.webp)



而且您還可以獲得以下選項：



![Image](assets/fr/040.webp)



若要顯示所有可用的指令，請輸入下列指令：



```
sudo lynis show
```



這就是您所得到的：



![Image](assets/fr/022.webp)



如果要顯示所有選項，必須輸入 ：



```
sudo lynis show options
```



這就是您所得到的：



![Image](assets/fr/021.webp)



在本文的其餘部分，我們將學習如何使用某些選項。



### B.執行系統稽核



我們要請 **Lynis** 來稽核我們的系統，強調哪些設定是正確的，哪些是可以改善的。為此，請輸入以下指令：



```
sudo lynis audit system
# ou
./lynis audit system
```



預設情況下，如果您執行此指令時不是以 root 登入，工具會以目前登入使用者的權限執行。某些測試不會在此情境下執行：



![Image](assets/fr/052.webp)



以下是在此模式下不會執行的測試：



![Image](assets/fr/051.webp)



命令執行後，分析就會開始。請稍候片刻。



在稽核結束時，您會得到這個結果 (我們可以看到 **Lynis** 已經正確地識別出 **Debian 12** 系統，並將使用 **Debian 外掛程式** 進行分析)：



![Image](assets/fr/017.webp)



接下來，Lynis 會列出一組與他在我們系統上所檢查的一切相對應的點數。這是依類別組織的，我們將會看到。另外值得注意的是，會使用顏色代碼來強調建議：





- 紅色***表示關鍵 Elements 或最佳實作未遵守（例如套件遺失），即您的伺服器未遵守此點
- 黃色***代表建議或部分符合建議（比方說，符合以這種顏色強調的某一點（非優先）是件好事）
- Green** 適用於您的伺服器組態符合規定的點數
- 白色**，中性時



在這裡，我們可以看到 Lynis 建議安裝 **fail2ban**：



![Image](assets/fr/057.webp)



在 "**Boot and services**"部分，我們看到透過 *systemd* 提供的服務保護有待改進。好的一面是，Grub2 已經存在，而且 .NET 上的權限也沒有問題：



![Image](assets/fr/029.webp)



接下來是 "**Kernel**「 和 」**Memory and Processes**" 區段：



![Image](assets/fr/037.webp)



接下來是 「**使用者、群組與驗證**」部分。工具通知我們「**/etc/sudoers.d**」目錄的權限有警告。目前，我們還不知道更多資訊，但我們可以在分析結束時看到建議內容。



![Image](assets/fr/049.webp)



以下是「**Shells」、「Files Systems」和「USB Devices」** 部分的內容。其中，我們可以看到有關掛載點的建議，以及 USB 裝置目前在此機器上是允許的。



![Image](assets/fr/048.webp)



接下來是各個部分：「**名稱服務」、「連接埠與套件」、「網路」。** 這裡指出，不再使用的套件可能會被清除，而且沒有能夠管理自動更新的公用程式。



![Image](assets/fr/058.webp)



我們可以看到防火牆已啟動（沒錯，還有 iptables！）。此外，我們可以看到它已找到未使用的規則，並安裝了 Apache 網頁伺服器。



![Image](assets/fr/055.webp)



接下來是網頁伺服器本身的分析，因為服務已經被識別出來。



我們可以看到它找到了**Nginx**的設定檔，而 SSL/TLS 部分，**ciphers**的設定是使用了會不安全的協定。另一方面，根據 Lynis，日誌管理是正確的。



![Image](assets/fr/038.webp)



我的 VPS 伺服器上有 SSH 服務。它的設定由 Lynis 分析。不得不說 SSH 的安全性很容易就能改善！當我們獲得建議後，我們會再詳細討論這個領域。



![Image](assets/fr/026.webp)



以下是 **「SNMP支援」、「資料庫」、"PHP"、「Squid支援」、「LDAP服務」、「日誌與檔案 」**部分。



關於日誌管理，有一個非常重要的建議：強烈建議您不要只將日誌儲存在本機的機器上。如果機器被攻擊者破壞，他很可能會嘗試刪除他的痕跡...所以我們需要將日誌外部化。



![Image](assets/fr/050.webp)



在這裡，我們有易受攻击的服務、帳戶管理、排程工作和 NTP 同步的稽核。在橫幅和識別部分，顯示的層級很低：這是可以理解的，如果您顯示系統版本，就會給潛在的攻擊者一個指示。這是預設設定。



如果能啟動 **auditd**，在進行**鑑識**分析時就能獲得日誌，這會很有趣。也會檢查 **NTP**，因為若要有效率地搜尋日誌，最好是系統能準時開機，這樣可以簡化搜尋。



![Image](assets/fr/036.webp)



Lynis 接著檢視加密 Elements、虛擬化、容器和安全框架。有些部分是空的，因為與分析的機器沒有對應關係。不過，我們可以看到我有兩個過期的 SSL 證書，而且我還沒有啟用 **SELinux**。



![Image](assets/fr/027.webp)



這裡也有改善的空間：沒有防毒或防惡意軟體掃描器，而且我們對檔案權限也有建議。



![Image](assets/fr/028.webp)



接下來，Lynis 著重於收緊 Linux 核心組態 (包括 IPv4 堆疊的規則)，以及管理 Linux 機器的「Home」目錄。



![Image](assets/fr/035.webp)



分析到此為止...最後這一點顯示，在這台機器上安裝 ClamAV 對我們有百利而無一害。



![Image](assets/fr/030.webp)



## IV.建議



審核之後，就是閱讀和分析建議的時候了。在這裡我們可以得到 Lynis 進行的每項測試的建議和說明。



以 SSH 建議為例。 **對於每項建議，您都會找到推薦的參數，以及可以解釋安全點的連結 ** 這得由您自己決定，視您的情況和使用方式而定。



讓我們來看看一些建議的範例，這些建議直接呼應了整個稽核中強調的重點...



### A.建議範例





- 如我們先前所見，NTP 對於記錄時間戳非常重要：



![Image](assets/fr/043.webp)





- Lynis 也建議安裝 **apt-listbugs** 套件，以便在套件安裝期間透過 **apt.** 取得關鍵 bug 的資訊。



![Image](assets/fr/041.webp)





- 該工具建議我們安裝 **needrestart，以便能夠**查看哪些進程使用了舊版本的函式庫，需要重新啟動。



![Image](assets/fr/054.webp)





- 此建議建議安裝 **fail2ban**，以自動封鎖無法驗證的主機 (特別是暴力破解)。



![Image](assets/fr/044.webp)





- 要強化系統服務，他建議我們針對機器上的每個服務執行 blue 指令。



![Image](assets/fr/056.webp)





- 他建議為所有受保護的帳戶密碼設定到期日。



![Image](assets/fr/031.webp)





- 這項建議建議設定密碼年齡的最小值和最大值。除其他事項外，這將確保定期更改密碼。



![Image](assets/fr/042.webp)





- 我們建議使用獨立的磁碟分割，以限制磁碟空間問題對一個磁碟分割的影響。



![Image](assets/fr/047.webp)





- 本建議建議停用 USB 儲存裝置和 firewire，以防止資料洩漏



![Image](assets/fr/033.webp)





- 若要符合此建議，只需安裝並設定 **unnatended-upgrade**，例如。



![Image](assets/fr/053.webp)



### B.安裝建議的套件



為了改善系統配置，我們要在機器上安裝一些套件：有些是 Lynis 建議的，有些是我個人推薦的。



只要您花一點時間設定它們，您就會有一個良好的工作基礎。要做到這一點，請參考 IT-Connect 網站、網站上的其他文章和工具說明文件。



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



一些關於已安裝套件的資訊 ：





- Clamav** 是一種防毒軟體。
- unattend-upgrades** 可以讓您自動管理更新，甚至重新開機或自動清除舊套件，它是完全可設定的。
- rkhunter** 是一種反 rootkit，可掃描您的檔案系統。
- Fail2ban** 會根據您允許它讀取的內容來建立日誌檔案，並且會與 **iptables** 搭配使用，例如禁止嘗試在 SSH 中「強行」您伺服器的 IP 位址。



### C.SSH 的建議



讓我們來看看 SSH 的建議。它們列在下面。別擔心，我們會立即說明如何改善配置。



![Image](assets/fr/034.webp)



讓我們仔細看看我目前在:**/etc/ssh/sshd_config** 中的 **SSH** 設定



![Image](assets/fr/018.webp)



以下建議的配置仍可進行最佳化，但可提供您一個良好的基礎。 *請注意，為了提高可讀性*，我刪除了一些註解。



我們將：





- 變更 SSH 連線埠（忘記預設的 22）
- 增加日誌的詳盡程度，從 **INFO 到 VERBOSE**
- 將 ** 登入權限時間** 設定為 **2 分鐘**



如果在兩分鐘內沒有輸入連線資訊，連線就會中斷。





- 啟動 **strictModes**



指定 "sshd" 在驗證連線之前，是否應該檢查使用者檔案的模式和擁有者，以及使用者的主目錄。這通常是可取的，因為有時新手會不小心讓他們的目錄或檔案完全被所有人存取。預設值是 "yes"。





- 將 **MaxAuthtries** 設為 3



這代表通訊結束前驗證失敗的次數。





- 將 **MaxSessions** 設為 2



這代表同時會話的最大數目。





- 啟用公開金鑰驗證



```
PubkeyAuthentication yes
```





- 保留密碼驗證 ：



```
PasswordAuthentication yes
```



禁止空密碼和**Kerberos**驗證，以及**直接根驗證**



```
PermitEmptyPasswords no
PermitRootLogin no
```



確定您有 "**PermitRootLogin no「，如果它等於 」yes「，就是 」absolute evil "**。





- 禁止 TCP 連線重定向



```
AllowTcpForwarding no
```



表示是否允許 TCP 重定向，預設值為 「是」。請注意：如果使用者可以存取 shell，停用 TCP 重定向並不會提高安全性，因為他們仍然可以設定自己的重定向工具。





- 禁止 X11 重導



```
X11Forwarding no
```



表示是否接受 X11 重定向，預設值為 「否」。請注意：即使停用 X11 重定向，也不會增加安全性，因為使用者仍可設定自己的重定向器。如果選擇 **使用登入**，X11 重定向會自動停用。





- 設定用戶端與 sshd 之間的通訊逾時時間



```
ClientAliveInterval  300
```



定義以秒為單位的逾時時間，逾時後如果沒有收到用戶端的資料，sshd 服務會傳送訊息要求用戶端回應。預設情況下，此選項設定為 "0"，表示不會傳送這些訊息給用戶端。只有 SSH 協定的版本 2 支援此選項。



```
ClientAliveCountMax 0
```



根據 sshd 的 [documentation (*man page*)](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html)，這個選項的意思如下："設定在客戶端沒有回應的情況下，**sshd** 所傳送的保留訊息（見上文）的數量。如果在傳送保留訊息時達到此臨界值，**sshd** 會斷開客戶端並終止會話。值得注意的是，這些保留訊息與 **KeepAlive** 選項 (如下) 有很大的不同。連線保留訊息是透過加密的隧道傳送，因此無法偽造。由 **KeepAlive** 啟用的 TCP 層級連線保持是可偽造的。當用戶端或伺服器需要知道連線是否閒置時，連線保持機制就會引起興趣"。





- 透過停用 **motd、banner、lastlog** 防止資訊洩露



```
PrintMotd no
```



指定當使用者以互動模式登入時，sshd 是否應該顯示「/etc/motd」檔案的內容。在某些系統上，shell 也可能透過 /etc/profile 或類似的檔案顯示此內容。預設值是 "yes"。



```
Banner none
```



值得注意的是，在某些司法管轄區，在認證之前傳送訊息可能是法律保護的先決條件。指定檔案的內容會在連線授權之前傳送給遠端使用者。此選項需要設定，因為預設情況下不會顯示訊息。



在影像中，這提供 ：



![Image](assets/fr/019.webp)



### D.審計得分



最後，別忘了檢查 **Lynis 稽核分數**！我們看到 ** 我的硬化分數是 63**，報告檔案可以在「**/var/log/lynis-report.dat**」中查看。還有檔案「**/var/log/lynis.log**」。



**換句話說，分數越高越好！因此，您需要在讓您的機器和託管服務正常運作 (也就是進行功能測試) 的同時，致力於您的組態以取得可能的最高分數。



![Image](assets/fr/046.webp)



讓我們來看看我的第二台伺服器的結果，我在這台伺服器上花了多一點時間進行加固！所以分數較高 (**76**) 是很正常的。



![Image](assets/fr/045.webp)



## V.Lynis 自動規劃



**Lynis** 也提供透過排程任務執行檢查的選項。事實上，**"--cronjob "** 選項會執行所有 Lynis 測試，而不需要驗證或使用者動作。然後，您可以非常簡單地建立一個腳本，執行 **Lynis**，並將輸出放在一個帶有時間戳記的檔案中，並註明有問題的伺服器名稱。這裡有一個這種類型的檔案，您可以放在 */etc/cron.daily* 資料夾：



```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```



**"AUDITOR_NAME 「**變數只是一個變數，我們會在**Lynis**的**」--auditor "**選項中設定這個變數，以便在報告中顯示這個名稱：



![Image](assets/fr/059.webp)



我們還要建立一些上下文變數，這些變數可以幫助我們更好地組織自己，例如用來命名報告和標記時間的主機名稱和日期，以及我們要放置報告的資料夾路徑。



## VI.總結



Lynis 是一個非常實用的工具，當您想要瞭解更多 Linux 伺服器組態的狀態，尤其是安全性方面的資訊時，它可以幫助您節省時間，提高效率。但是，請不要忘記，每項修改在應用於生產之前都必須經過測試，並考慮到您自己的使用情況和上下文。



您可能不會對暴露在網路上的 VPS 應用相同的設定，因為您只需要一個 SSH 連線（因為您是唯一的連線者），不像**bastion** 或 **scheduler**需要多重 **SSH.**連線。



一旦您有了適合您的加固設定，建議您採用自動化工具，這樣您就不必手動重做任務，因為這樣既費時又容易出錯。例如，您可以使用 **：Puppet、Chef、Ansible 等...**。



在實施之前，別忘了與您的團隊溝通：您需要讓他們了解為什麼要做這些改變，而不只是告訴他們您要做這些改變。最後，我們的目標是傳承良好的實務，這將增加您成功的機會。



最後，您也可以將 **Lynis** 與其他工具進行比較，而其他工具有好幾種。如果您想要邁向集中化管理，同時保持開放原始碼，我推薦 [Wazuh] 工具 (https://wazuh.com/)。



**本教程結束，祝您和 Lynis 玩得愉快！