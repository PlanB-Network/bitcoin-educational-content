---
name: LN VPN

description: 設定您的 VPN
---

![image](assets/cover.webp)


LN VPN 是一款只接受閃電付款的客製化 VPN 服務。今天，我將教您如何使用它，並在瀏覽網際網路時減少留下痕跡。


有許多優質的 VPN 服務供應商，我們已在本文（超連結）中進行了全面的評論。然而，LN VPN 脫穎而出，我們不能錯過向您介紹它的機會。


大多數 VPN 服務供應商，如 ProtonVPN 和 Mullvad，都提供使用 bitcoins 付款的選項，但需要建立帳號並購買較長或較短期限的方案，這可能不符合每個人的預算。


LN VPN 透過 Lightning Network 實作 Bitcoin 付款，可在短至一小時內按需使用 VPN。即時和匿名的閃電付款為微額付款開啟了一片天地。


注意💡： **本指南說明如何從 Linux Ubuntu 22.04 LTS 系統使用 LN VPN。


## 先決條件：護線器


簡單來說，Wireguard 是用來在您的電腦和遠端伺服器之間建立一個安全的隧道，您可以通過該隧道瀏覽網際網路。該伺服器的 IP Address 將會在租用期間顯示為您的 IP，您可以按照本指南使用 Contract。


官方 Wireguard 安裝指南：https://www.wireguard.com/install/


```
Wireguard installation
$ sudo apt-get update
$ sudo apt install wireguard
```


## 先決條件：閃電 Bitcoin Wallet


如果您還沒有 Lightning Bitcoin Wallet，不用擔心，我們在這裡為您建立了一個非常簡單的指南。(LN教學部分可以幫到您)


## 步驟 1：Contract 租約


從 https://lnvpn.com，您需要選擇 VPN 通道出口 IP 的國家和持續時間。設定好這些參數後，按一下 Pay with lightning。


![image](assets/1.webp)


將會顯示閃電 Invoice，您只需用閃電 Wallet 掃描即可。


支付 Invoice 之後，您需要等待幾秒到兩分鐘的時間來產生您的 Wireguard 設定。如果時間稍長，請不要慌張，我們已經執行此程序數十次，有時只是時間稍長而已。

以下文字已翻譯成英文，但仍維持與原文相同的 markdown 排版：


下一個畫面將會出現，您只需按一下「Download as File」（以檔案形式下載），即可收到您的設定檔案，檔案名稱看起來像 lnvpn-xx-xx.conf，其中「xx」將對應目前的日期。

![image](assets/2.webp)


## 步驟 2：啟動隧道


首先，您需要重新命名上一步獲得的配置文件，以便 Wireguard 能自動識別。


在終端視窗中或使用檔案總管進入下載資料夾，將 lnvpn-xx-xx.conf 檔案重命名為 wg0.conf，就像這樣：


```
$ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
$ sudo wg-quick up ~/Downloads/wg0.conf
```


好了隧道啟動了


## 步驟 3：驗證


使用像 whatismyip 之類的線上服務，確認您的公共 IP Address 現在是您剛啟用的 VPN 的 IP。


## 步驟 4：停用


租約到期時，您需要停用連線才能重新存取網際網路。之後，只要您想與 LN VPN 建立租約，就可以重複步驟 1 到 3。


停用隧道：


```
$ sudo ip link delete dev wg0
```


就是這樣！您現在知道如何使用 LN VPN 這項獨特的 VPN 服務了！