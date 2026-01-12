---
name: Alby

description: Bitcoin 和 Lightning Network 的瀏覽器延伸功能
---

![cover](assets/cover.webp)




使用比特幣讓支付變得越來越容易，是該行業許多公司面臨的挑戰。Alby 憑藉其適用於瀏覽器的 Alby wallet 擴展功能脫穎而出。該擴展旨在建立一個流暢的框架，自動檢測地址，並允許您進行無摩擦的比特幣支付。在本教程中，我們將發現 Alby 擴展功能，並測試它如何方便地從瀏覽器進行支付。




![video](https://youtu.be/nd5fX2vHuDw)




## Alby 延伸



Alby 擴充套件是一種工具，可讓您的網頁瀏覽器與 Bitcoin 網路及其 Lightning Network 層輕鬆且安全地互動。它的特點有三個方面：




- Lightning Network wallet：連結您的 Alby 節點或帳戶，透過 Lightning Network 層快速且便宜地傳送和接收比特幣。
- 通過 Web 進行流動支付：在支援 Lightning 的網站上進行比特幣支付，無需掃描 QR 碼或在應用程式之間切換。只需點擊一下，它就能實現流暢的交易，如果您已設定預算，則無需確認。
- Nostr 管理器：該擴充套件可管理您的 Nostr 金鑰，讓您能輕鬆連結 Nostr 應用程式並與之互動，以安全簽章人的身份行事，而無需將您的私人金鑰暴露給每個平台。



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## 連接至分機



在本教程中，我們將在 Ubuntu 作業系統下的 Firefox 瀏覽器中使用 Alby 延伸功能。不過，它也適用於 Windows 以及 Chrome 等瀏覽器。



您可以造訪 [Firefox] 延伸功能商店 (https://addons.mozilla.org/fr/firefox/addon/alby/) 或 [Chrome] 延伸功能商店 (https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe)，將 Alby 延伸功能新增至您的瀏覽器。



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ 請務必確認擴充套件的作者確實是 Alby 官方帳號，以避免任何形式的盜版或竊取您的 bitcoins。



按一下右邊的按鈕，將擴充套件加入瀏覽器。


授予安裝和使用擴充套件的必要權限，然後將擴充套件釘在工具列上以方便檢索。



![pin](assets/fr/03.webp)



您還應該定義一個解鎖密碼（非常重要），這將保證從瀏覽器安全訪問您的 Lightning wallet。我們建議您設定一個強大的字母數字密碼。



ℹ️ 將此密碼保存在安全的地方，以便您忘記時可以存取，因為密碼可以變更但無法取回。



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Alby 提供您兩種選擇，展現其適應能力：




- 如果您想在享受應用程式的同時控制您的比特幣，請繼續使用 Alby 帳戶。
- 如果您已有擴充套件支援的 wallet 或 Lightning 節點，請連接您自己的 wallet 或 Lightning 節點。



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


在本教程中，我們選擇繼續使用 Alby 帳戶，以利用 Alby 生態系統的功能。



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

登入您的 Alby 帳戶，如果您還沒有 Alby 帳戶，請建立一個。



![signup](assets/fr/05.webp)



## 首次付款



登入後，您可以按一下工具列上的 Alby 擴充套件來存取您的投資組合。



![buzzin](assets/fr/06.webp)



一旦您創建了您的 Alby 帳戶，您就需要將它與 wallet 連接起來，以便花費 Satoshis。要將比特幣 wallet 連接到您的 Alby 帳戶，我們建議您使用 Alby Hub 節點，您可以在您的電腦上設置這個節點，或者訂購 Alby 提供的計劃。



![hubplan](assets/fr/13.webp)




在本教程中，我們的 Alby 帳戶由機器上的本機安裝支援。


若要建立您自己的 Alby 節點，我們建議您參考我們的 Alby Hub 教學。



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

此節點可讓您建立自我保管的 Lightning 投資組合，並有效管理您的 Lightning 通道，以傳送和接收 Satoshis。



![channels](assets/fr/14.webp)



開啟接收通道，定義可接收的衛星訊號總數。



![receivechanal](assets/fr/15.webp)



透過封鎖 bitcoin onchain 位址上的 satoshis 來開啟發送通道。您封鎖的 Satoshis 定義了您可以花費的 Satoshis 總數。



![spend](assets/fr/16.webp)



現在您可以透過 Alby 擴充套件傳送和接收 Satoshis。



![exchange](assets/fr/08.webp)



從這一點開始，Alby 擴充套件能夠偵測到您所瀏覽網頁上的 Lightning 位址和可用發票，並會建議您直接從擴充套件以 bitcoin 或 Lightning 付款。



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## 使用主密鑰保護復原密鑰



Alby 擴充套件提供的主密鑰可作為保護層，讓您與主 Bitcoin 網路層 (Onchain)、Nostr 系統進行安全通訊，並讓您啟動與 Nostr 應用程式的 Lightning 連線。



![masterKey](assets/fr/11.webp)



此主密鑰的形式與您的復原短語相似，共有 12 個字。因此，我們建議您使用安全的方法儲存它，以確保可隨時存取。



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



現在您可以使用 Alby 擴展功能體驗無摩擦的比特幣和 Lightning 支付。如果您喜歡本教學，我們推薦您使用我們的 Alby Hub 教學來建立您自己的 Alby 節點，並從流暢而強大的介面控制 Alby 錢包的所有方面。



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a