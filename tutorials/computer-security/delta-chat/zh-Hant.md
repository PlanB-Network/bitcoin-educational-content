---
name: 三角洲聊天室
description: 分散式訊息傳送工具實用指南
---

![image](assets/cover.webp)




## 簡介 - 聊天控制與隱私權



近年來，有關 Chat Control 的討論越來越多，這是一項監管提案，目的在於在主要通訊平台上引進自動掃描私人訊息的機制。宣稱的目標是打擊非法內容，問題是這個機制事實上會涉及大規模的監控，去破壞端對端加密，進而破壞所有使用者的隱私，而不只是犯罪者。



真正的風險是聊天變成受控制的環境，每則訊息、圖片或附件都可能在傳送至收件者之前就被檢查。這就是一個可能的解決方案：擺脫集中式平台，轉向分散式訊息系統，因為分散式訊息系統不依賴單一供應商，不容易受到這種審查。



本教程將介紹其中一種解決方案：Delta Chat。一個成熟且已經可用的工具。




## 為何使用 Delta Chat 及其運作方式



Delta Chat 已經是非常適合日常使用的訊息解決方案：對於與朋友、家人和其他人聊天非常有用，就像真正等同於 WhatsApp。



它是一個完全以電子郵件為基礎的分散式訊息系統。它基本上利用了傳統電子郵件的基礎架構，但在其上建立了現代的即時通訊界面和體驗。乍看之下，這似乎有點即興，但實際上它運作得非常好，而且強大得令人驚訝。您可以使用稱為 ChatMail 的專用郵件伺服器，但它也可以與一般的電子郵件伺服器無縫運作。這表示如果您願意的話，您可以使用現有的帳號登入，而不需要建立任何新的帳號。



另一個亮點是支援 WebXDC，這是可以直接在聊天中使用的小型 Web 應用程式，類似於 Telegram 中的迷你應用程式。重要的差別在於這些應用程式無法存取網際網路，因此無法追蹤使用者或傳送資料到外部。



從安全的角度來看，Delta Chat 使用經過驗證的端對端加密，以 PGP 為基礎，但有現代化的擴充，使其保護等級可媲美 Signal。目前唯一欠缺的是 Perfect Forward Secrecy，但這也是一個不斷演進的層面。



由於 Delta Chat 完全以電子郵件為基礎，因此可以完全避免使用電子郵件：




- 強制性電話號碼
- 集中式 ID
- 與單一服務相連的註冊



而這也是這個工具非常能抵抗如 Chat Control 等入侵性規範的原因。




## 安裝



從 [Delta Chat] (https://delta.chat/download) 的官方網站，您可以進入下載區。在 Linux 上可透過 Flathub 下載，但也有 Arch、NixOS、Snap 和獨立版本的套件。



![image](assets/it/01.webp)



它也適用於




- [F-Droid](https://f-droid.org/app/com.b44t.messenger)
- [Play 商店](https://play.google.com/store/apps/details?id=chat.delta)
- [iOS](https://apps.apple.com/it/app/delta-chat/id1459523234)
- [Windows](https://apps.microsoft.com/detail/9pjtxx7hn3pk)
- [macOS](https://apps.apple.com/it/app/delta-chat-desktop/id1462750497)
- [Ubuntu Touch](https://open-store.io/app/deltatouch.lotharketterer)
- 和其他商店...



如果您正在尋找安裝 F-Droid 的指南，本教學可能會對您有所幫助：



https://planb.academy/tutorials/computer-security/data/f-droid-2cd1aae5-7028-4c04-8fbe-95aeaf278ef4

有一點非常重要：桌面版不需要手機。與 WhatsApp 或 SimpleX Chat 不同，您不需要先從手機註冊。您可以直接在 PC 上建立個人檔案，或從其他裝置傳輸。




## 建立個人資料



打開應用程式後，Delta Chat 會詢問您是要建立新的個人資料，還是使用現有的個人資料。



![image](assets/it/02.webp)



透過建立新的個人資料，您可以輸入：




- 名
- 圖片（可選）



預設是建議使用 ChatMail 伺服器，但這是可能的：




- 選擇另一個 ChatMail 伺服器
- 使用經典的電子郵件帳號
- 手動設定 IMAP 和 SMTP
- 使用其他使用者的邀請碼註冊



幾秒鐘之後，設定檔就準備好了，您就可以開始使用應用程式。



![image](assets/it/03.webp)




## Interface 和聊天



介面非常簡單直接：




- 裝置訊息，即本機通訊
- 儲存的訊息，類似 Telegram 中的訊息，並可在裝置之間同步處理



![image](assets/it/04.webp)



若要新增連絡人，只需




- 顯示您的 QR 代碼
- 掃描對方的
- 透過連結邀請 (分享邀請連結)。



![image](assets/it/05.webp)



建立連線後，會自動設定端對端加密。聊天使用者介面與 WhatsApp 非常相似：




- 文字和語音訊息
- 照片、視訊和檔案
- 對消息的回應
- 反應
- 彈出消息
- 自訂通知。



![image](assets/it/06.webp)



## WebXDC: 聊天中的應用程式：



Delta Chat 允許使用 WebXDC，即嵌入在會話中的小型應用程式。以下是已識別出的最有用的簡短清單：




- 調查
- 圖板
- 臨時私人聊天
- 共享聊天分數的遊戲



也可以開始更複雜的遊戲，這顯示了此工具的靈活性。



![image](assets/it/07.webp)



## 群組、頻道和進階功能



您可以建立群組、使用貼紙 (尤其是在桌上型電腦上)，如果啟動實驗選項，甚至可以建立類似 Telegram 的頻道。



在進階設定中，您可以開啟：




- 語音通話（仍在實驗中）
- 進階電子郵件設定檔管理
- 完整備份。



![image](assets/it/08.webp)



## 多裝置與備份



Delta Chat 完全支援多裝置：




- 您可以透過 QR 代碼新增第二台裝置
- 您可以透過備份執行完整傳輸。



只需幾秒鐘，您就可以再次找到您的聊天記錄、群組和完整的歷史記錄，而無需依賴中央伺服器。



![image](assets/it/09.webp)




## 總結



當有越來越多人談論要控制私人通訊時，Delta Chat 代表了一個具體的答案：分散式、加密的訊息傳輸，真正每天都能使用。



在我試過的所有解決方案中，它是最讓我信服的簡單、隱私和自由的解決方案。如果您願意，也可以透過以下 [邀請連結](https://i.delta.chat/#38824F04DD40600D5D4F079C1F5E0EBA875A6D7E&i=GStGfNW5LMIXhwQMiuQWj3QU&s=cVi5izRJ9NsbIcPlU8yC_SeB&a=9l4la5imj%40nine.testrun.org&n=SatoSats) 在 Delta Chat 上與我聯絡。



如果您喜歡這份指南，您可以透過捐款和留下大拇指來支持我。請記住：只有在行動和桌上型電腦上使用和探索 Delta Chat，您才能真正發現它的全部功能。



下次再見。