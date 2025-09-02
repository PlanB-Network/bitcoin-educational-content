---
name: Graylog
description: 集中並輕鬆分析您的日誌
---
![cover](assets/cover.webp)



___



*本教學是根據 Florian BURNEL 發表於 [IT-Connect](https://www.it-connect.fr/) 的原始內容。原始碼授權類型 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)。原文可能有變更。



___



## 在 Debian 12 上部署 Graylog



### I.簡報



Graylog 是一個開放原始碼的「日誌匯集」解決方案，旨在即時集中、儲存和分析來自您的機器和網路設備的日誌。在本教程中，我們將學習如何在 Debian 12 電腦上安裝免費版的 Graylog！



在資訊系統中，每台**伺服器，不論是執行**Linux**或**Windows**，以及每台**網路裝置** (交換器、路由器、防火牆......等) 都會**產生自己的日誌**，並儲存在本機中。由於日誌儲存在每台機器的本機，因此事件分析與關聯非常困難...這就是**Graylog**出現的原因。它將扮演**日誌匯集器的角色，這表示**您所有的機器都會傳送它們的日誌** (例如透過 syslog)。Graylog 會儲存這些日誌並編入索引，同時允許您執行全局搜尋並建立警示。



Graylog 是一種分析和監控工具，可讓您更容易識別可疑行為和各種問題 (穩定性、效能等)。




![Image](assets/fr/034.webp)



**註：免費版本 **Graylog Open** 並非 Wazuh 所謂的 SIEM，尤其是它缺乏真正的入侵偵測功能。



### II.先決條件



**stack Graylog** 基於我們需要安裝和設定的**多個元件。在此，我們將在同一台伺服器上安裝所有元件，但也可以根據多個節點建立叢集，並將角色分佈在多台伺服器上。在本教程中，我們將安裝 **Graylog 6.1**，這是目前最新的版本。





- MongoDB 7**，Graylog 目前的建議版本（最低 5.0.7，最高 7.x）。
- OpenSearch**, 由 Amazon 所建立的 Elasticsearch 開放原始碼 Fork (最低 1.1.x，最高 2.15.x)
- OpenJDK 17**



**Graylog伺服器**是在**Debian 12**上執行，但也可以在其他發行版上安裝，包括透過Docker。虛擬機器配備 **8 GB 記憶體** 和 **256 GB 磁碟空間**，以便為所有元件提供足夠的資源（否則會對效能造成重大影響）。不過，我只是提供一個粗略的指引，因為**Graylog 架構的大小取決於要處理的資訊量**。Graylog 可以每天處理 30 MB 或 300 MB 的資料，也可以每天處理 300 GB 的資料...它是一個**可擴充的解決方案**，能夠處理**兆位元組的日誌** (請參閱 [本頁](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0))。



![Image](assets/fr/032.webp)



來源: Graylog



開始設定前，請先為 Graylog 機器指定靜態 IP Address，並安裝最新更新。請務必設定本機的時區，並定義用於日期和時間同步的 NTP 伺服器。以下是要執行的指令：



```
sudo timedatectl set-timezone Europe/Paris
```



**Note: 如果您使用 **Graylog Data Node**，**OpenSearch 安裝是可選的**。



### III 逐步安裝 Graylog



讓我們先更新套件快取，並安裝未來所需的工具。



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A.安裝 MongoDB



完成後，我們就開始安裝 MongoDB。下載與 MongoDB 儲存庫相對應的 GPG 金鑰：



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



然後將 MongoDB 6 套件庫新增至 Debian 12 機器：



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



接下來，我們會更新套件快取，並嘗試安裝 MongoDB ：



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



由於缺少相依性，因此無法安裝 MongoDB： **libssl1.1**.我們必須手動安裝這個套件才能繼續，因為 Debian 12 的套件庫中沒有這個套件。



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



我們要用 **wget** 指令下載名為「**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**」（最新版本）的 DEB 套件，然後用 **dpkg** 指令安裝。這會產生以下兩個指令：



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



重新啟動 MongoDB 安裝：



```
sudo apt-get install -y mongodb-org
```



然後重新啟動 MongoDB 服務，並使其在 Debian 伺服器啟動時自動啟動。



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



安裝好 MongoDB 後，我們就可以繼續安裝下一個元件。



#### B.安裝 OpenSearch



讓我們繼續在伺服器上安裝 OpenSearch。以下指令會新增 OpenSearch 套件的簽章金鑰：



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



然後加入 OpenSearch 套件庫，以便我們之後能夠使用 **apt** 下載套件：



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



更新您的套件快取：



```
sudo apt-get update
```



然後**安裝 OpenSearch**，注意**定義您的實例的管理**帳號的預設密碼。這裡的密碼是 "**IT-Connect2024!**"，但請使用強大的密碼取代此值。 **Avoid weak passwords** like "**P@ssword123**" and use at least **8 characters** with at least one character of each type (lowercase, uppercase, number and special character), otherwise there will be an error at the end of the installation. **自 OpenSearch 2.12.** 起，這是一項先決條件。



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



安裝期間請耐心等待...



完成後，請花一點時間執行最基本的設定。開啟 YAML 格式的設定檔：



```
sudo nano /etc/opensearch/opensearch.yml
```



當檔案開啟時，設定下列選項：



```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```



此 OpenSearch 設定是用來設定單一節點。以下是我們使用不同參數的一些說明：





- cluster.name: graylog**: 此參數以 "**graylog**" 命名 OpenSearch 集群。
- node.name：${HOSTNAME}**：節點名稱是動態設定的，以符合本機 Linux 機器的名稱。即使我們只有一個節點，正確命名也是很重要的。
- path.data：/var/lib/opensearch**：此路徑指定 OpenSearch 在本機上儲存資料的位置，在本例中為「**/var/lib/opensearch**」。
- path.logs：/var/log/opensearch**：此路徑定義 OpenSearch 日誌檔案的儲存位置，這裡是 "**/var/log/opensearch**"。
- discovery.type：single-node**：此參數可將 OpenSearch 設定為使用單一節點，因此選擇「**single-node**」選項。
- network.host：127.0.0.1**：這項設定確保 OpenSearch 只會在其 Interface 區域迴路上進行監聽，由於它與 Graylog 位於同一台伺服器上，因此這樣就足夠了。
- action.auto_create_index：false**：關閉自動建立索引的功能，當傳送的文件沒有現有索引時，OpenSearch 就不會自動建立索引。
- plugins.security.disabled：true**：這個選項會停用 OpenSearch 安全外掛，這表示將不會有驗證、存取管理或通訊加密。此設定可在設定 Graylog 時節省時間，但在生產中應該避免使用 (請參閱 [this page](https://opensearch.org/docs/1.0/security-plugin/index/))。



有些選項已經存在，所以您只需要移除「#」來啟動它們，然後再指出您的值。如果找不到選項，可以直接在檔案末尾宣告。



![Image](assets/fr/023.webp)



儲存並關閉此檔案。



#### C.配置 Java (JVM)



您需要設定 OpenSearch 使用的 Java 虛擬機器，以便調整此服務可使用的記憶體數量。編輯下列設定檔：



```
sudo nano /etc/opensearch/jvm.options
```



使用此處部署的配置，**OpenSearch 將以 4 GB 的分配記憶體開始，並可增加到 4 GB**，因此在操作期間不會有記憶體變化。這裡的配置考慮到虛擬機器共有 **8 GB 記憶體**。兩個參數的值必須相同。這表示將 ：



```
-Xms1g
-Xmx1g
```



有了這些線條：



```
-Xms4g
-Xmx4g
```



以下是要進行修改的圖片：



![Image](assets/fr/022.webp)



儲存後關閉此檔案。



此外，我們需要檢查 Linux 核心中「**max_map_count**」參數的設定。它定義了每個進程映射的記憶體區域限制，以滿足我們應用程式的需求。 **OpenSearch** 和 Elasticsearch** 一樣，建議將此值設為「262144」，以避免記憶體管理錯誤。



原則上，在新安裝的 Debian 12 機器上，數值已經正確。但讓我們檢查一下。執行此指令：



```
cat /proc/sys/vm/max_map_count
```



如果得到的值不是 "**262144**"，請執行以下指令，否則不必執行。



```
sudo sysctl -w vm.max_map_count=262144
```



最後，啟用 OpenSearch 自動啟動功能，並啟動相關服務。



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



如果您顯示系統狀態，您應該會看到一個 Java 進程有 4 GB RAM。



```
top
```



![Image](assets/fr/029.webp)



下一步：安裝期待已久的 Graylog！



#### D.安裝 Graylog



若要 ** 安裝最新版本的 Graylog 6.1**，請執行下列 4 個指令，以 ** 下載並安裝 Graylog 伺服器** ：



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



完成後，在嘗試啟動 Graylog 之前，我們需要對 Graylog 的設定做一些變更。



讓我們先設定這兩個選項：





- password_secret**：這個參數用來定義 Graylog 用來確保使用者密碼儲存安全的金鑰 (如同鹽化金鑰的精神)。此密鑰必須是 ** 唯一 ** 且 ** 隨機的。
- root_password_sha2**: 這個參數對應於 Graylog 的預設管理員密碼。它儲存為 Hash SHA-256。



我們先為 **password_secret** 參數產生 96 個字元的金鑰：



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



複製回傳值，然後開啟 Graylog 配置檔案：



```
sudo nano /etc/graylog/server/server.conf
```



將密鑰貼入 **password_secret** 參數，就像這樣：



![Image](assets/fr/027.webp)



儲存並關閉檔案。



接下來，您需要為預設建立的「**admin**」帳號設定密碼。在配置文件中，必須儲存密碼的 Hash，也就是說必須計算出密碼的 Hash。下面的示例提供了密碼 "**LogsWells@**"的 Hash：將該值適應為您的密碼。



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



複製獲得的值作為輸出（行末不含連字符號）。



再次開啟 Graylog 配置檔案：



```
sudo nano /etc/graylog/server/server.conf
```



將此值貼入 **root_password_sha2** 選項，就像這樣：



![Image](assets/fr/026.webp)



在設定檔中，設定「**http_bind_address**」選項。指定 "**0.0.0.0:9000**"，以便 Graylog 的 Interface Web 可以透過任何伺服器 IP Address 在**9000**埠上存取。



![Image](assets/fr/024.webp)



然後將「**elasticsearch_hosts**」選項設為「http://127.0.0.1:9200」，以宣告我們的本機 OpenSearch 實例。這是必要的，因為我們沒有使用 **Graylog Data Node**。如果沒有這個選項，我們就無法繼續前進...



![Image](assets/fr/025.webp)



儲存並關閉檔案。



此指令會啟動 Graylog，使其在下次開機時自動啟動，並立即啟動 Graylog 伺服器。



```
sudo systemctl enable --now graylog-server
```



完成後，嘗試從瀏覽器連線至 Graylog。輸入伺服器的 IP Address（或名稱）和埠 9000。



**供您參考：**



不久之前，當您第一次登入 Graylog 時，會出現類似下面的驗證視窗。您必須輸入登入名稱「**admin**」和密碼。然後，您會驚訝地發現連線無法正常運作。



![Image](assets/fr/031.webp)



我們必須回到 Graylog 伺服器的命令列，並查看日誌。這樣我們就可以看到，**第一次連線時，必須**使用日誌中指定的臨時密碼**。



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



然後，您必須使用使用者「**admin**」和臨時密碼重新嘗試連線，這才允許您登入！



**現在已經不是這種情況了。您只需使用管理員帳號和命令列上設定的密碼登入即可



![Image](assets/fr/033.webp)



**歡迎來到Graylog的Interface！



![Image](assets/fr/019.webp)



#### E.Graylog: 建立新的管理員帳戶



與其使用 Graylog 原生創建的管理員帳戶，您可以創建自己的個人管理員帳戶。按一下「**系統**」功能表，然後按一下「**使用者與團隊**」，按一下「**建立使用者**」按鈕。然後填寫表單，並為您的帳戶指定管理員角色。



![Image](assets/fr/020.webp)



個人化帳戶可以包含其他資訊，例如名和姓以及電子郵件 Address，這與原生管理員帳戶不同。更重要的是，當每個人使用具名帳戶工作時，這可確保更好的可追溯性。



## 使用 rsyslog 將日誌傳送至 Graylog



### I.簡報



在第二部分中，我們將學習如何設定 Linux 機器將日誌傳送至 Graylog 伺服器。為此，我們將在系統上安裝和設定 Rsyslog。



### II.設定 Graylog 以接收 Linux 日誌



我們先從設定 Graylog 開始。有三個步驟需要完成：





- 建立**輸入**，以建立允許 Linux 機器透過 UDP**傳送 Syslog 日誌的入口點。
- 建立新的 ** 索引 **，以儲存和 ** 索引所有 Linux 日誌 **。
- 建立**Stream**，將 Graylog 接收到的日誌**路由到新的 Linux 索引。



#### A.建立 Syslog 輸入



登入 Graylog Interface，按一下功能表中的 「**系統**」，然後按一下 「**輸入**」。在下拉列表中，選擇「**Syslog UDP**」，然後按一下標示為「**啟動新輸入**」的按鈕。也可以建立 TCP Syslog 輸入，但這需要使用 TLS 憑證：這是安全性的加分项，但不在本文的討論範圍內。



![Image](assets/fr/001.webp)



螢幕上會出現一個精靈。請先為此輸入命名，例如「**Graylog_UDP_Rsyslog_Linux**」，並選擇一個連接埠。預設埠為 "**514**"，但您可以自訂。這裡選擇的是連接埠「**12514**」。



![Image](assets/fr/016.webp)



您也可以勾選「**儲存完整訊息**」選項，將完整的日誌訊息儲存到 Graylog 中。按一下「**啟動輸入**」。



![Image](assets/fr/017.webp)



新的 Input 已經建立，並已啟用。Graylog 現在可以透過 12514/UDP 連接埠接收 Syslog 日誌，但我們還沒有完成應用程式的設定。



![Image](assets/fr/018.webp)


**注意：一個 Input 可以用來儲存多台 Linux 機器的日誌。



#### B.建立新的 Linux 索引



我們需要在 Graylog 中建立一個索引來儲存來自 Linux 機器的日誌。Graylog 中的 **index** 是一個儲存結構，包含所接收的日誌，也就是所接收的訊息。Graylog 使用 OpenSearch 作為其儲存引擎，訊息被編入索引是為了能夠快速、有效率地搜尋。



從 Graylog，按一下功能表中的 「**系統**」，然後按一下 「**索引**」。在出現的新頁面中，按一下「**建立索引集**」。



![Image](assets/fr/005.webp)



為這個索引命名，例如「**Linux 索引**」，在確認之前加入說明和前綴。在此，我們會將所有 Linux 日誌**儲存於此索引**。也可以建立特定索引，僅儲存某些日誌 (僅 [SSH] 日誌 (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH")、Web 服務日誌等)。



![Image](assets/fr/006.webp)



現在我們需要建立一個新的串流，將訊息路由到這個索引。



#### C.建立串流



若要建立新的串流，請點選 Graylog 主功能表中的「**串流**」。然後按一下右邊的「**建立串流**」按鈕。在出現的視窗中，為串流命名，例如「**Linux 串流**」，並在「**索引集**」欄位中選擇索引「**Linux 索引**」。確認您的選擇。



**註：與此串流對應的訊息也會包含在「**預設串流**」中，除非您勾選「**從「預設串流」中移除匹配**」選項。



![Image](assets/fr/002.webp)



然後，在您的 steam 設定中，點選「**新增串流規則**」按鈕來新增訊息路由規則。如果您找不到這個視窗，請點選功能表中的「**Streams**」，然後在您的串流對應的那一行，點選「**More**」，再點選「**Manage Rules**」。



選擇「**match input**」類型，並選擇先前建立的 **Rsyslog input in UDP**。使用「**建立規則**」按鈕確認。現在，所有傳送到新輸入的訊息都會傳送到 Linux 的索引。



![Image](assets/fr/003.webp)



您的新 Stream 應該會出現在清單中，而且應該處於「**Running**」狀態。訊息頻寬會顯示「**0 msg/s**」，因為我們目前沒有傳送任何記錄到 Rsyslog UDP 輸入。若要檢視串流的記錄，只要按一下其名稱即可。



![Image](assets/fr/004.webp)



**Everything's ready on the Graylog side**.下一步是設定 Linux 機器。



### III.在 Linux 上安裝和設定 Rsyslog



在本機或遠端登入 Linux 機器，並使用具有權限的使用者帳戶來提升其權限 (透過 sudo)。否則，請直接使用「root」帳戶。



#### A.安裝 Rsyslog 套件



首先更新套件快取，並安裝名為 "**rsyslog**" 的套件。



```
sudo apt-get update
sudo apt-get install rsyslog
```



然後檢查服務狀態。在大多數情況下，它已經在執行了。



```
sudo systemctl status rsyslog
```



#### B.設定 Rsyslog



Rsyslog 的主要設定檔位於此處：



```
/etc/rsyslog.conf
```



此外，"**/etc/rsyslog.d/**"目錄用來儲存 Rsyslog 的其他設定檔案。在主配置檔中，有一個 Include 指令可以匯入這個目錄中的所有「**.conf**」檔案。這樣就可以在不修改主檔案的情況下，為 Rsyslog 設定額外的檔案。



在此目錄中，您必須使用數字來定義載入順序，因為檔案是依字母順序載入的。加入數字前綴可讓您管理數個組態檔案之間的優先順序。在這裡，我們只有一個額外的檔案，所以問題不大。



在此目錄中，我們將建立一個名為「**10-graylog.conf**」的檔案：



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



在此檔案中，插入這一行 ：



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



以下是如何解釋這一行：





- `*.*`：表示將 Linux 機器上的所有 Syslog 日誌傳送至 Graylog。
- `@`：表示傳輸以 UDP 執行。您必須指定「**@@**」才能切換到 TCP。
- 192.168.10.220:12514：表示 Graylog 伺服器的 Address 以及傳送記錄的連接埠（與輸入相對應）。
- `RSYSLOG_SyslogProtocol23Format`: 對應於要傳送至 Graylog 的訊息格式。



完成後，儲存檔案並重啟 Rsyslog。



```
sudo systemctl restart rsyslog.service
```



執行此動作之後，第一批訊息應該會到達您的 Graylog 伺服器！



### IV.在 Graylog 中顯示 Linux 日誌



從 Graylog，您可以點選「**Streams**」並選擇您的新串流來檢視相關訊息。或者，點選「**搜尋**」，選擇您的 Steam 並啟動搜尋。



以下是 Interface 的一些主要功能：



**1** - 選擇顯示訊息的期間。預設會顯示最近 5 分鐘的訊息。



**2** - 選擇要顯示的串流。



**3** - 啟用自動刷新訊息清單 (例如每 5 秒刷新一次)。否則，它是靜態的，您必須手動刷新。



**4** - 在修改期間、串流或篩選條件後，按一下放大鏡以啟動搜尋。



**5** - 用來指定搜尋篩選項的輸入欄。在這裡，我指定「**source:srv\-docker**」，以只顯示我剛設定 Rsyslog 的新機器的日誌。



日誌由 Linux 機器傳送：



![Image](assets/fr/015.webp)



### V.識別 SSH 連線失敗



Graylog 的優勢在於其索引日誌的能力，並能依據各種條件進行搜尋：源機器、Timestamp、訊息內容等...我們可以尋找識別失敗的 SSH 連線。



從遠端機器 (例如 Graylog 伺服器)，嘗試連線到您剛設定 Rsyslog 的 Linux 伺服器。例如



```
ssh [email protected]
```



然後故意輸入不正確的**使用者名稱**和**密碼**，以**generate 連線錯誤**。在「**/var/log/auth.log**」檔案中，這將會出現類似以下的 generate 日誌訊息：



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



您應該可以在 Graylog 上找到這些訊息。



在 Graylog 上，使用下列搜尋篩選器，僅顯示符合條件的訊息：



```
message:Failed password AND application_name:sshd
```



如果您有多台伺服器，並希望分析特定伺服器的日誌，請在 .NET Framework 2.0 以外指定其名稱：



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



以下是在一台機器上的結果總覽，在這台機器上，我在一天中的不同時間產生了多次連線錯誤：



![Image](assets/fr/009.webp)



從 IP Address "**192.168.10.199**" 的機器嘗試連線不成功。如果您想知道更多關於這台主機的活動，可以**搜尋此 IP Address**。Graylog 會輸出所有主機（已設定傳送日誌）上引用此 IP Address 的所有日誌。



在這種情況下，要使用的濾波器可以是 ：



```
message:"192.168.10.199"
```



我們得到額外的結果（這並不令人意外，因為我們並沒有在 SSH 應用程式上進行過濾）：



![Image](assets/fr/008.webp)



### VI.總結



按照本教學，您應該可以設定 Linux 機器將其日誌傳送至 Graylog 伺服器。這樣，您就可以將 Linux 主機的日誌集中到您的日誌匯！



若要更進一步，可考慮建立儀表板和警示，以便在偵測到異常時收到通知。



![Image](assets/fr/007.webp)