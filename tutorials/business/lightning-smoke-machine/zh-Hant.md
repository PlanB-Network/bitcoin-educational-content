---
name: Lightning Smoke Machine
description: 透過 ESP32 以 Lightning 付款觸發煙霧機。
---

![cover-lightning-smoke-machine](assets/cover.webp)



## 簡介



透過 Lightning Network 將經典煙霧機轉換為可在 Bitcoin 中付款的裝置。每次付款都會自動啟動煙霧噴射！





- 等級：中級
- 預計時間：2-3 小時
- 使用個案：Bitcoin 活動、藝術表演、閃電演示、自動舞台效果



## 先決條件



### 知識





 - 基本電子 (接線、繼電器)
 - 焊接（或使用杜邦連接器）
 - 網路設定 (WiFi、WebSocket)



### 所需帳戶





- BTCPay 伺服器：功能性實例 (自託管或託管)
- Blink Wallet : 帳戶 + 存取 API



### 存取





- BTCPay 伺服器的管理存取權
- ESP32 的 WiFi 連線



## 所需材料



### 硬體 - 電子零件





- 1 個微控制器 - ESP32-WROOM-32


*ESP32-WROOM-32 是一款小巧、低成本的 WiFi/Bluetooth 微控制器，可將電子設備連接到網際網路並進行遠端控制*。



![ESP32](assets/fr/1.webp)





- 1 繼電器模組 - 5V 含光耦合器


*繼電器就像是一個開關，ESP32 可以操作它來開啟或關閉煙霧機*。



![relay](assets/fr/2.webp)





- ~10 條 Dupont 電纜 - 公頭/公頭和公頭/母頭



![dupont-cables](assets/fr/3.webp)





- 1 供 ESP32 使用的電源 - 5V USB 或鋰電池



![battery](assets/fr/4.webp)





- 1 條 micro-USB 連接線 - 連接 ESP32 與電源供應器



![micro-usb-cables](assets/fr/5.webp)





- 1 部 220V 煙霧機，附 12V 電池遙控器



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 瓶與您的煙霧機相容的液體



### 硬體 - 工具





- 烙鐵 + 錫 (如果焊接)
- 螺絲起子
- 萬用表（建議）



### 軟體





- 韌體 BitcoinSwitch ： **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- WebSerial 相容的網頁瀏覽器 (Chrome/Edge/Brave)
- 已配置 BTCPay 伺服器。有關建立 BTCPay 伺服器實例的更多資訊，請瀏覽此教學：https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc。



## 系統架構



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **安全警告 - 繼續前請閱讀** **⚠️**



本專案涉及連接至**220V 主電源**的噴霧機。不當操作可能導致**致命觸電**或**火災**。



**不可協商的規則：**



1. **在打開遙控器或改動接線之前，請務必先將煙霧機從主電源**中斷開。


2. **操作前請先從遙控器**取出電池（有短路和損壞元件的風險）


3. **在重新連線之前，請檢查您所有的連線是否都已隔離**


4. **在遙控盒關閉並固定之前，切勿重新連接 220V**。



如果您不習慣這種處理方式，請帶著您習慣的人一起去。



---

## 第 1 部分：硬體組裝



### 步驟 1：準備遙控器



目標：將繼電器連接至遙控器上的 ON/OFF 按鈕


1.開啟遙控器




    - 識別 ON/OFF 按鈕
    - 擰開外殼以打開遙控器


2.定位連接




 - 確定 + 和 - 端子的位置。
 - 使用萬用表（選購）測試連通性



![smoke-machine-remote](assets/fr/8.webp)



3.按鈕接線（焊接或連接器）




    - 將黑色電纜焊接到按鈕的 - 端子上
    - 將紅色電纜焊接到共用 + 端子上



![smoke-machine-remote](assets/fr/9.webp)



### 步驟 2：連接繼電器模組



**提醒：中繼術語



| **Terminal**         | **Description**           | **Fonction**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit ouvert par défaut | Se ferme quand le relais est activé |
| NC (Normally Closed) | Circuit fermé par défaut  | S'ouvre quand le relais est activé  |
| COM (Common)         | Terminal central          | Bascule entre NO et NC              |

**從遙控器到繼電器模組的接線：**




- 來自 ON/OFF 按鈕的黑線 **→** NO (常開)
- 紅線 (共線) **→** COM (共線)



**邏輯：**


當 ESP32 啟動繼電器時，會連接 COM 和 NO，這與按下遙控器按鈕完全相同。


當 ESP32 切斷繼電器時，COM 和 NO 分離，相當於釋放按鈕。



![remote-relay](assets/fr/10.webp)



### 步驟 3：將 ESP32 連接到繼電器模組



**接線圖:**



| **ESP32** | **→** | **Module relais** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |

**驗證：**




- VCC 和 GND 連接良好（極性）
- GPIO 21 用於控制訊號
- 無明顯短路



![relay-esp32](assets/fr/11.webp)



**檢查點硬體**


切換到軟體之前，請檢查 ：




- 正確接線的遙控器
- 繼電器模組連接到 ESP32
- 無裸線接觸其他元件
- 220V 經常斷開



![relay-esp32](assets/fr/12.webp)





---


## 第 2 部分：軟體配置



我們以 *Blink* 為例，但 *BTCPay Server* 也提供 *Strike、Breez 和 Boltz*，如果您喜歡另一種選擇。



### 步驟 1：外掛程式、安裝 *BitcoinSwitch* + *Blink



1 - 使用管理帳戶進入您的*BTCPay伺服器*實例



2 - 建立您的第一個盲點



3 - 在*BTCPay伺服器*的左側，滾動到底部，進入*「管理外掛程式 」*。



![btcpay-plugins](assets/fr/13.webp)



4 - 我們將安裝*BitcoinSwitch*外掛程式以及*Blink*。



![btcpay-plugins](assets/fr/14.webp)



5 - 向下滾動插件列表，點擊 *「安裝 」* ： *BitcoinSwitch 和 Blink* (或您選擇的可用 wallet)



![btcpay-plugins](assets/fr/15.webp)



6 - 安裝完成後，重新啟動 *BTCPay 伺服器*，等待 1 分鐘讓實體重新啟動。



![btcpay-plugins](assets/fr/16.webp)



7 - 當您回到 *「管理外掛程式 」*，檢查兩個外掛程式是否都已安裝。



![btcpay-plugins](assets/fr/17.webp)



### 步驟 2：後端：*BTCPay 伺服器 + Blink* 設定



**1 - 建立 wallet *Blink***




- 請造訪 https://www.blink.sv
- 建立您的帳戶。請參考教學 ：



[https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd](https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - 產生 API 金鑰 *Blink***




- 存取 API 介面： **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** 並使用您建立 wallet *Blink* 時使用的相同帳號登入



![blink-api](assets/fr/18.webp)





   - 連線後，移至 *API Keys* 標籤



![blink-api](assets/fr/19.webp)





   - 按一下右上角的 *"+ "* 在右上角存取您的 API 密鑰設定



![blink-api](assets/fr/20.webp)





   - 為您的 API Key 命名，並保留預設設定。然後，在第三步，記下您的 API 密鑰 - 您只能看到一次：`blink_mZ5KxxxxxxxxxxxxxNbmX`。



![blink-api](assets/fr/21.webp)





   - 建立後，它應該會出現在您的活動 API 金鑰清單中。



![blink-api](assets/fr/22.webp)



**3 - 將 *Blink* 連接到 *BTCPay 伺服器****。




- 開啟您的*BTCPay伺服器*
- 導航至 ： *Wallet* **→** *閃電*



![btcpay-server](assets/fr/23.webp)





- 按一下 * 使用自訂節點*。
- 貼上下列連線字串：



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **重要** ：




- 請勿修改第一部分：type=blink;server=https://api.blink.sv/graphql`；
- 僅更換 ：
    - api-key= *使用您的 API Blink* 鑰匙
    - wallet-id= *根據您的 wallet Blink* ID
- 然後按一下 * 測試連線*，再按一下 * 儲存*。



![btcpay-server](assets/fr/24.webp)





 - 檢查連線是否建立（綠色狀態）



![btcpay-server](assets/fr/25.webp)



**4 - 建立銷售點 (PoS)**




- 在BTCPay伺服器中，進入*外掛*索引標籤，點選*銷售點*。



![btcpay-server](assets/fr/26.webp)





- 為您的 PoS 命名，然後按一下 *建立*。



![btcpay-server](assets/fr/27.webp)





- PoS 配置 ：
    - 選擇銷售點樣式 = *列印顯示*
    - 貨幣 = *SATS*
    - 按一下 *儲存



![btcpay-server](assets/fr/28.webp)





- 產品配置 ：
    - 刪除所有預設產品
    - 然後按一下 * 新增項目*。



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- 設定產品：
    - 標題 ： *煙霧機*
    - 價格 ： *10 sats*
    - Bitcoin GPIO 開關 : 21
    - Bitcoin 切換持續時間（以毫秒為單位） ：5000
    - 按一下 *關閉*，然後按一下 *儲存*，以儲存新產品



![btcpay-server](assets/fr/31.webp)



### 步驟 3：韌體：更新 ESP32



**1 - 進入 flash 網站




- 前往 ：[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash BitcoinSwitch 韌體**




- 使用 USB/Micro-USB 纜線將 ESP32 連接到您的電腦
- 然後按一下 * 連線至裝置*。
- 開啟視窗，選擇 ESP32 上的 USB 連接埠，然後按一下 *Connect* 。



![bitcoinswitch-lnbits](assets/fr/33.webp)





- 當您的ESP32連接好後，我們會更新BitcoinSwitch的韌體。在*T-Display*部分，點擊*Upload Firmware*獲得最新版本（目前：*bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- 等待上傳，當記錄顯示 *"離開..."*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- 拔下 ESP32 插頭



**3 - 檢查 BitcoinSwitch 韌體安裝情況




- 重新載入頁面：[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- 使用 USB/Micro-USB 纜線將 ESP32 重新連接到您的電腦。
- 然後按一下 *連線至裝置
- 選擇 ESP32 上的 USB 連接埠，然後按一下 *Connect* 如上所述
- 連接完成後，按下 ESP32 上的 **RESET** 按鈕。
- 檢查日誌中最後一行是否顯示 ：



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(這是正常現象，表示尚未設定，但已安裝韌體）



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - 生成 WebSocket LNURL** URL



預期最終格式 ：



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



生成步驟 ：




- 打開您的BTCPay伺服器實例，然後前往我們稍後建立的PoS。
- 然後按一下「檢視」，在瀏覽器中開啟您的 PoS



![btcpay-server-https](assets/fr/37.webp)





- 複製頁面的 URL，例如 ：



![btcpay-server-https](assets/fr/38.webp)



讓我們來拆解這個 URL：



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → 您的 BTCPay 伺服器實例的網域
- `46XXXXXXXXXXXXXXwFB` → 您的 PoS 唯一識別碼
- `/pos` → 表示銷售點



改造它：




- 將 `https://` 改為 `wss://`
- 在結尾加入 `/bitcoinswitch



結果：



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



保留此 URL 以備將來配置之用，因為它能讓您的 ESP32 與 BTCPay 伺服器進行即時通訊。WebSocket 協定 (`wss://`)在兩者之間建立永久連接：一旦您的 PoS 確認 Lightning 付款，BTCPay 即時將資訊傳送至 ESP32，然後便可觸發您的煙霧機。



**5 - 設定 WiFi 和 WebSocket




- 返回頁面：[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) 連接您的 ESP32
- 移至 * 設定裝置* → *Wifi 設定*。



通知 ：




- WiFi SSID：您的 WiFi 網路名稱
- WiFi 密碼：您的 WiFi 密碼



![bitcoinswitch-lnbits](assets/fr/39.webp)





- 在 *LNbits 裝置 URL* 區段中，貼上在上一步中建立的 WebSocket URL
- 按一下 * 上傳設定*。



![bitcoinswitch-lnbits](assets/fr/40.webp)





- 等待上傳完成；日誌應顯示您剛輸入的參數（SSID、密碼和 WebSocket URL）



![bitcoinswitch-lnbits](assets/fr/41.webp)





- 等待 ESP32 建立 WebSocket 連線。您應該會看到 ：



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- 現在您可以斷開 ESP32 的連接



---
## 保點軟體



在最後測試之前，請檢查 ：





- Blink 連接到 BTCPay
- 至少以 1 個項目建立 PoS
- 使用 BitcoinSwitch 更新 ESP32
- 在 ESP32 上設定 WiFi
- WebSocket URL 正確
- 無錯誤的 ESP32 日誌



---

## 測試與除錯



### 完成最後測試



1.插入煙霧機 (220V) 並開機


2.為 ESP32 供電 (電池或 USB)


3.在瀏覽器中打開您的BTCPay PoS


4.掃描 "smoke-machine" 項目


5.使用 wallet Lightning (Blink 或其他 wallet) 付款


6.觀察：




 - 繼電器點擊（發出聲音且繼電器 LED 亮起）
 - 啟動煙霧機
 - 產生煙霧！



### 公平性問題與解決方案



| **Problème**                        | **Cause probable**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 ne se connecte pas            | Driver USB manquant             | Installer [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relais ne clique pas                | Mauvais câblage GPIO            | Vérifier GPIO 21 → IN                                                                        |
| Smoke machine ne réagit pas         | Télécommande mal câblée         | Vérifier NO/NC/COM                                                                           |
| WebSocket timeout                   | URL incorrecte                  | Vérifier wss:// et /bitcoinswitch                                                            |
| WiFi ne se connecte pas             | SSID/Password erroné            | Re-flasher la config WiFi                                                                    |
| Paiement reçu mais rien ne se passe | ESP32 non connecté au WebSocket | Vérifier les logs RESET                                                                      |

## 資源



### 有用連結





- BitcoinSwitch 韌體：[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- BTCPay 伺服器文件 ：[https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 引腳佈局 ：[https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### 社區與支援





- BTCPay 伺服器** ：[chat.btcpayserver.org](https://chat.btcpayserver.org/) - 官方 Mattermost
- BTCPay 伺服器 Telegram** ：[t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** ：[t.me/lnbits](https://t.me/lnbits) - 官方 Telegram，活躍社群
- BitcoinSwitch (韌體錯誤)**：[github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### 原始碼





- BitcoinSwitch 韌體原始碼：[https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** 堆疊 sats、製造煙霧、享受樂趣、保持謙虛！ **⚡**