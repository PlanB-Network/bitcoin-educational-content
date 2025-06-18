---
name: Lightning Network 理論介紹
goal: 從技術角度探索 Lightning Network
objectives: 
  - 瞭解網路頻道的運作。
  - 熟悉詞彙 HTLC、LNURL 和 UTXO。
  - 同化流動資金的管理和 LNN 的費用。
  - 確認 Lightning Network 為網路。
  - 瞭解 Lightning Network 的理論用途。

---
# 前往 Bitcoin 的第二個 Layer 之旅

深入了解 Lightning Network 的核心，這是未來 Bitcoin 交易的重要系統。LNP201 是關於 Lightning 技術運作的理論性課程。它揭開了第二個 Layer 網路的基礎和機制，旨在使 Bitcoin 支付快速、經濟且可擴展。

得益於其支付通道網絡，Lightning 可實現快速、安全的交易，而無需在 Bitcoin Blockchain 上記錄每個 Exchange。在整個章節中，您將學習通道的開啟、管理和關閉是如何工作的，支付如何安全地經過中介節點，同時最大限度地減少對信任的需求，以及如何管理流動資金。您將發現什麼是 Commitment 交易、HTLC、撤銷金鑰、懲罰機制、洋蔥路由和發票。

無論您是 Bitcoin 的初學者或是較有經驗的使用者，本課程將提供了解與使用 Lightning Network 的寶貴資訊。雖然我們會在前幾部分介紹 Bitcoin 的一些基本操作，但在深入學習 LNP201 之前，掌握 Satoshi 的基本發明是非常必要的。

享受您的發現！

+++

# 介紹
<partId>9da7290a-3895-49a2-93ea-2a6272ca4af4</partId>

## 課程概述
<chapterId>f2e71062-5121-4114-a7f8-27df69884ce8</chapterId>

歡迎參加 LNP201 課程！

本次培訓旨在讓您深入了解閃電網路的技術，閃電網路是一種旨在促進快速且通常低成本的比特幣交易的覆蓋網路。您將逐漸發現管理該系統的基本概念，從開放支付管道到路由技術和流動性管理。

**第 1 部分：基礎知識**
我們將首先對閃電網路進行概述，建立有關比特幣、其地址、UTXO 以及交易如何運作的基本基礎知識。為了理解閃電網路如何依賴底層區塊鏈機制安全運行，進行這項基本審查是必要的。

**第二部分：開啟和關閉 Channels**
在本節中，我們將探索通道開通過程，這是閃電網路的基石。您將了解如何建立承諾交易、撤銷金鑰在安全方面的作用以及如何以協作或單方面的方式關閉管道。每個步驟都會得到精確且專業的解釋，以幫助您掌握所有細節。

**第三部分：流動性網絡**
閃電網路並不局限於單一通道；它是一個真正的支付網路。我們將看到如何使用 HTLC 透過中間節點路由交易。本節也將向您介紹流入和流出流動性的挑戰。

第四部分：閃電網路工具
本節介紹閃電網路的實用工具，例如*Invoices*、*LNURL*和*Keysend*。您還將學習如何管理管道的流動性，這是確保順​​利付款和最大限度提高 Lightning 交易效率的重要方面。

**第五部分：進一步了解**
最後，我們將透過回顧所涵蓋的概念並為那些希望加深對閃電網路了解的人鋪平更高級的主題來結束培訓。

準備好揭開閃電網路的技術機制了嗎？讓我們開始吧！ 介紹

# 基本原理

<partId>32647d62-102b-509f-a3ba-ad1d6a4345f1</partId>

## 瞭解 Lightning Network

<chapterId>df6230ae-ff35-56ea-8651-8e65580730a8</chapterId>

:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::

歡迎來到 LNP201 課程，此課程旨在說明 Lightning Network 的技術功能。

Lightning Network 是建構在 Bitcoin 通訊協定之上的付款通道網路，旨在實現快速且低成本的交易。它允許在參與者之間建立付款通道，在此通道中，交易幾乎可以立即進行且費用極低，而無需在 Blockchain 上個別記錄每筆交易。因此，Lightning Network 旨在提高 Bitcoin 的可擴展性，使其可用於低額支付。

在探索 「網路 」方面之前，了解 Lightning 上**付款通道**的概念、其運作方式及其具體細節是非常重要的。這是第一章的主題。

### 付款管道的概念

付款通道允許雙方（在此為 **Alice**和 **Bob**）透過 Lightning Network 進行 Exchange 資金交易。每個主角都有一個節點，以圓形符號表示，而他們之間的通道則以線段表示。

![LNP201](assets/en/01.webp)

在我們的範例中，Alice 在信道的一端有 100,000 衛星，Bob 有 30,000 衛星，總共 130,000 衛星，這就是 **信道容量**。

**But what is a Satoshi? **

**Satoshi**（或 "sat"）是 Bitcoin 的記帳單位。類似於歐元的美分，Satoshi 只是 Bitcoin 的一小部分。一個 Satoshi 等於 **0.00000001 Bitcoin**，或一億分之一的 Bitcoin。隨著 Bitcoin 價值的上升，使用 Satoshi 變得越來越實用。

### 渠道中的資金分配

讓我們回到付款通道。這裡的關鍵概念是「通道的**面」。每個參與者都有自己通道一邊的資金：Alice 100,000 薩托希，Bob 30,000。正如我們所見，這些資金的總和代表了通道的總容量，這個數字是在通道打開時設定的。

![LNP201](assets/en/02.webp)

讓我們以閃電交易為例。如果 Alice 想發送 40,000 薩托希給 Bob，這是可能的，因為她有足夠的資金（100,000 薩托希）。交易完成後，Alice 擁有 60,000 順位，Bob 則擁有 70,000 順位。

![LNP201](assets/en/03.webp)

通道容量**為 130,000 衛星，保持不變。改變的是資金的分配。這個系統不允許傳送超過一個人所擁有的資金。舉例來說，如果 Bob 想要傳送 80,000 薩托希給 Alice，他就不能傳送，因為他只有 70,000 薩托希。

另一種想像資金分配的方式，是想像一個**滑桿**，顯示資金在通道中的位置。一開始，Alice 有 100,000 順位，Bob 有 30,000 順位，滑桿在邏輯上是在 Alice 一邊。在交易 40,000 薩托希後，滑桿會稍微移向鮑勃這邊，他現在有 70,000 薩托希。

![LNP201](assets/en/04.webp)

此表示法對於想像通道中的資金平衡非常有用。

### 付款通道的基本規則

首先要記住的一點是，**通道的容量**是固定的。它有點像管道的直徑：它決定了一次可以透過通道傳送的最大資金量。

讓我們舉個例子：如果 Alice 身邊有 130,000 薩托希，她在單筆交易中最多只能寄 130,000 薩托希給 Bob。但是，Bob 可以將這些資金部分或全部寄回給 Alice。

需要瞭解的是，通道的固定容量限制了單筆交易的最大金額，但不限制可能的交易總數，也不限制通道內交換資金的總量。

**您應該從本章中獲得什麼？


- 通道的容量是固定的，它決定了單筆交易中可以傳送的最大金額。
- 通道中的資金在兩個參與者之間進行分配，每個參與者只能向對方傳送自己一方擁有的資金。
- 因此，Lightning Network 可以在尊重通道容量限制的前提下，快速、高效地 Exchange 資金。

第一章到此為止，我們已經為 Lightning Network 打下基礎。在接下來的章節中，我們會看到如何開啟頻道，並深入探討這裡所討論的概念。

## Bitcoin、地址、UTXO 和交易

<chapterId>0cfb7e6b-96f0-508b-9210-90bc1e28649d</chapterId>

:::video id=75323eef-ea03-45ac-9a6e-46d73ca255de:::

本章有點特別，因為它不會直接介紹「閃電」，而是介紹 Bitcoin。事實上，Lightning Network 是 Bitcoin 上的 Layer。因此，理解 Bitcoin 的某些基本概念對於在接下來的章節中正確掌握 Lightning 的運作是非常重要的。在本章中，我們將回顧 Bitcoin 接收位址、UTXOs 以及 Bitcoin 交易功能的基本知識。

### Bitcoin 位址、私人密碼匙和公用密碼匙

Bitcoin Address 是一串從 ** 公鑰**衍生出來的字元，而 ** 公鑰本身則是從 ** 私鑰**計算出來的。您一定知道，它是用來鎖定比特幣的，等於在我們的 Wallet 中接收比特幣。

私密金鑰是**絕對不能共用的秘密元素，而公開金鑰和 Address 則可以共用，沒有安全風險 (它們的洩露只代表您的隱私有風險)。以下是我們在整個培訓過程中將採用的通用表示法：


- 私密金鑰**將以**反向**表示。
- **公鑰**將以**橫向**表示。
- 它們的顏色表示誰擁有它們（Alice 是橙色，Bob 是黑色...）。

### Bitcoin 交易：發送資金和腳本

在 Bitcoin 上，交易涉及從一個 Address 向另一個 Address 發送資金。讓我們以 Alice 傳送 0.002 Bitcoin 給 Bob 為例。Alice 使用與她的 Address 相關聯的私密金鑰來簽署交易，從而證明她確實能夠使用這些資金。但這筆交易背後到底發生了什麼？Bitcoin Address 上的資金是由**指令碼**鎖定的，這是一種迷你程式，強制某些條件才能使用資金。

最常見的腳本需要使用與 Address 相關的私密金鑰簽名。當 Alice 用她的私人密碼匙簽署交易時，她就**解鎖了封鎖資金的腳本**，然後資金就可以被轉移。轉移資金涉及為這些資金加入新的腳本，規定這次要花掉這些資金，需要**Bob 的**私鑰簽名。

![LNP201](assets/en/05.webp)

### UTXOs：未使用的交易輸出

在 Bitcoin 上，我們實際上 Exchange 並不是直接的 bitcoins，而是 **UTXOs**（_Unspent Transaction Outputs_），意思是「未使用的交易輸出」。

一個 UTXO 是一塊 Bitcoin，可以是任何價值，例如：**2,000 bitcoins**、**8 bitcoins**，甚至是**8,000 Sats**。每個 UTXO 都由一個腳本鎖定，要花費它，必須滿足腳本的條件，通常是用特定接收 Address 對應的私鑰簽名。

UTXO 不能分割。每次使用它們來花費它們所代表的比特幣金額時，都必須全部花費。這有點像鈔票：如果你有一張 10 歐元的鈔票，而你欠麵包師傅 5 歐元，你不能直接把鈔票切成兩半。您必須把 10 歐元的鈔票交給他，他才會給您 5 歐元的零錢。這與 Bitcoin 上的 UTXO 原理完全相同！舉例來說，當 Alice 用她的私人密碼匙解鎖一個腳本時，她就解鎖了整個 UTXO。如果她只想傳送這個 UTXO 所代表的部分資金給 Bob，她可以將它「分割」成幾個較小的。然後，她會將 0.0015 BTC 寄給鮑勃，並將剩餘的 0.0005 BTC 寄給一個 ** 變更 Address**。

以下是一個有 2 個輸出的交易範例：


- 鮑勃的 UTXO 為 0.0015 BTC，由需要鮑勃私人金鑰簽章的腳本鎖定。
- 愛麗絲的 UTXO 為 0.0005 BTC，由需要她本人簽名的腳本鎖定。

![LNP201](assets/en/06.webp)

### 多重簽名地址

除了由單一公開金鑰所產生的簡單位址外，也可以由多個公開金鑰建立**多重簽章位址**。對 Lightning Network 來說，一個特別有趣的案例是 **2/2多重簽章 Address**，由兩個公開金鑰所產生：

![LNP201](assets/en/07.webp)

若要使用此 2/2 多重簽章 Address 鎖定的資金，必須使用與公開金鑰相關的兩個私人金鑰簽章。

![LNP201](assets/en/08.webp)

這種類型的 Address 正是 Bitcoin Blockchain 上支付通道在 Lightning Network 上的表示。

**您應該從本章中獲得什麼？


- **Bitcoin Address** 來自公開金鑰，而公開金鑰本身則來自私人金鑰。
- Bitcoin 上的資金由 ** 腳本**鎖定，若要使用這些資金，必須滿足腳本的要求，這通常涉及提供相應私密金鑰的簽章。
- UTXOs** 是由腳本鎖定的比特幣碎片，Bitcoin 上的每筆交易都包括解鎖一個 UTXO，然後再建立一個或多個新的 UTXO，以作為回報。
- 2/2 多重簽章地址**需要兩個私人金鑰的簽章才能使用資金。這些特定的位址在 Lightning 的背景下用來建立付款通道。

關於 Bitcoin 的這一章讓我們回顧了一些接下來的基本概念。在下一章中，我們將特別探討 Lightning Network 開啟通道的原理。

# 開啟和關閉通道

<partId>900b5b6b-ccd0-5b2f-9424-4b191d0e935d</partId>

## 通道開啟

<chapterId>96243eb0-f6b5-5b68-af1f-fffa0cc16bfe</chapterId>

:::video id=6098fee1-735e-4d8d-9f57-0faf5fef6d76:::

在本章中，我們將更精確地了解如何在 Lightning Network 上開啟付款通道，並理解此操作與底層 Bitcoin 系統之間的聯繫。

### 閃電通道

正如我們在第一章中看到的，Lightning 上的**支付通道**可以比作兩個參與者（在我們的例子中是**Alice**和**Bob**）之間交換資金的 「管道」。此通道的容量相當於雙方可用資金的總和。在我們的範例中，Alice 有**100,000 Satoshis**，Bob 有**30,000 Satoshis**，因此**總容量**為**130,000 Satoshis**。

![LNP201](assets/en/09.webp)

### 資訊層級 Exchange

關鍵是要清楚區分 Lightning Network 上 Exchange 的不同等級：


- 點對點通訊（Lightning 協議）**：這些是 Lightning 節點互相傳送以進行通訊的訊息。我們會在圖表中以黑色虛線表示這些訊息。
- 付款通道（閃電協定）**：這些是在 Lightning 上交換資金的路徑，我們將以黑色實線表示。
- Bitcoin 交易 (Bitcoin 協定)**：這些是在鏈上進行的交易，我們將用橙色線表示。

![LNP201](assets/en/10.webp)

值得注意的是，Lightning 節點可以透過 P2P 通訊協定進行通訊，而無需開啟通道，但對於 Exchange 資金而言，通道是必要的。

### 開啟 Lightning 通道的步驟


- 訊息 Exchange**：Alice 想要與 Bob 開啟一個通道。她傳送給 Bob 一則訊息，內容包含她想要存入頻道的金額 (130,000 Sats)，以及她的公開金鑰。Bob 藉由分享他自己的公開金鑰來回應。

![LNP201](assets/en/11.webp)


- 建立多重簽章 Address**：有了這兩個公開金鑰，Alice 就建立了一個 **2/2 多重簽章的 Address**，也就是說，稍後存放在這個 Address 上的資金需要兩個簽章 (Alice 和 Bob) 才能使用。

![LNP201](assets/en/12.webp)


- 存款交易**：Alice 準備一筆 Bitcoin 交易，將資金存入此多重簽章 Address。例如，她可能會決定寄送 **130,000 薩托希** 到這個多重簽章 Address。此交易已在 Blockchain 上**建構，但尚未發佈。

![LNP201](assets/en/13.webp)


- 提款交易**：在公佈存款交易之前，Alice 會建構一個提款交易，以便在鮑勃出現問題時，她可以取回她的資金。事實上，一旦 Alice 發佈存款交易，她的 Sats 將被鎖定在 2/2 多重簽章 Address 上，需要她和 Bob 的簽章才能解鎖。Alice 藉由建構可讓她取回資金的取款交易來防止此損失風險。

![LNP201](assets/en/14.webp)


- 鮑勃的簽名**：Alice 將存款交易傳送給 Bob 作為證明，並請他在提款交易上簽名。一旦取得鮑勃在提款交易上的簽名，愛麗絲就能保證隨時取回她的資金，因為現在只需要她自己的簽名就能解除多重簽章的鎖定。

![LNP201](assets/en/15.webp)


- 公佈存款交易**：一旦獲得 Bob 的簽章，Alice 就可以在 Bitcoin Blockchain 上公佈存款交易，從而正式打開兩位使用者之間的 Lightning 通道。

![LNP201](assets/en/16.webp)

### 頻道何時開放？

一旦存款交易包含在 Bitcoin 區塊中，且達到一定的確認深度（跟蹤區塊的數量），該通道即被視為開放。

**你應該從本章記住什麼？


- 開啟通道始於雙方之間**訊息的 Exchange（金額和公開金鑰的 Exchange）。
- 建立一個 **2/2 多重簽章 Address** 並透過 Bitcoin 交易將資金存入其中，即可形成通道。
- 開啟通道的人在公佈存款交易之前，確保他們可以透過對方簽署的提款交易**取回資金。

在下一章中，我們將探討渠道中 Lightning 交易的技術運作。

## Commitment Transaction

<chapterId>7d3fd135-129d-5c5a-b306-d5f2f1e63340</chapterId>

:::video id=c17454f3-14c5-47a0-8c9c-42ee12932bd3:::

在本章中，我們將發現 Lightning Network 上通道內交易的技術功能，也就是當資金從通道的一邊移到另一邊時。

### 渠道生命週期的提醒

如前所述，Lightning 通道是通過 Bitcoin 交易開啟的。通道可以隨時**關閉**，也是通過 Bitcoin 交易。在這兩個時刻之間，幾乎可以在通道內執行無數個交易，而無需經過 Bitcoin Blockchain。讓我們看看通道中的交易會發生什麼。

![LNP201](assets/en/17.webp)

### 通道的初始狀態

在開啟通道時，Alice 在通道的多重簽章 Address 上存入了**130,000 Satoshis**。因此，在初始狀態，所有資金都在 Alice 一方。在開啟通道之前，Alice 也讓 Bob 簽署了一份**提款交易**，如果她想關閉通道，就可以取回她的資金。

![LNP201](assets/en/18.webp)

### 未公開的交易：Commitment 交易

當 Alice 在通道中進行交易，將資金發送給 Bob 時，就會創建一個新的 Bitcoin 交易，以反映資金分配的這種變化。此交易稱為 **Commitment Transaction**，不會在 Blockchain 上公佈，但代表通道在 Lightning 交易後的新狀態。

讓我們以 Alice 傳送 30,000 Satoshis 給 Bob 為例：


- 最初**：Alice 有 130,000 薩托希。
- 交易後**：Alice 有 100,000 順位，Bob 有 30,000 順位。

為了驗證這項轉移，Alice 和 Bob 建立一個新的**未公開 Bitcoin 交易**，從多重簽章 Address 傳送**100,000 Satoshis 給 Alice**和**30,000 Satoshis 給 Bob**。雙方獨立建構此交易，但使用相同的資料（金額和地址）。建構完成後，雙方各自簽署交易，並與對方交換簽章。這允許任何一方在必要時隨時公布交易，以恢復他們在主 Bitcoin Blockchain 上的通道份額。

![LNP201](assets/en/19.webp)

### 轉移過程：Invoice

當 Bob 想要接收資金時，他會寄給 Alice 一張 30,000 Satoshis 的 **_invoice_**。然後，Alice 開始在通道內轉帳，以支付這筆 Invoice 款項。正如我們所見，這個過程有賴於建立和簽署新的 **Commitment Transaction**。

每個 Commitment Transaction 代表轉帳後通道中新的資金分佈。在這個範例中，交易完成後，Bob 有 30,000 Satoshis，Alice 有 100,000 Satoshis。如果這兩位參與者中的任何一位決定在 Blockchain 上公佈此 Commitment Transaction，就會導致通道關閉，而資金將根據此最後的分配進行分配。

![LNP201](assets/en/20.webp)

### 第二次交易後的新狀態

讓我們再舉一個例子：在第一筆交易後，Alice 傳送了 30,000 Satoshis 給 Bob，Bob 決定傳送 **10,000 Satoshis 回給 Alice**。這會產生一個新的通道狀態。新的 **Commitment Transaction** 將代表這個更新的分佈：


- 愛麗絲**現在有**110,000 薩托希**。
- 鮑勃**有 **20,000 薩托希**。

![LNP201](assets/en/21.webp)

同樣地，此交易不會在 Blockchain 上公佈，但在頻道關閉的情況下，可以隨時公佈。

總而言之，當資金在 Lightning 通道內轉移時：


- Alice 和 Bob 建立新的 **Commitment Transaction**，反映新的資金分配。
- 此 Bitcoin 交易由雙方**簽署**，但只要通道保持開啟，**不會在 Bitcoin Blockchain 上公佈**。
- Commitment 交易可確保每位參與者可隨時在 Bitcoin Blockchain 上公佈最後一次簽署的交易，以收回其資金。

然而，這個系統有一個潛在的缺陷，我們將在下一章 Address 討論。我們將看每個參與者如何保護自己，以防對方企圖作弊。

## 撤銷金鑰

<chapterId>f2f61e5b-badb-5947-9a81-7aa530b44e59</chapterId>

:::video id=1d850f23-eff1-4725-b284-ce12456a2c26:::

在本章中，我們將透過討論防止作弊的機制，深入探討 Lightning Network 上的交易是如何運作的，以確保每一方都遵守通道內的規則。

### 提醒事項：Commitment 交易

如前所述，Lightning 上的交易依賴未公開的 **Commitment 交易**。這些交易反映了通道中資金的當前分配情況。當進行新的 Lightning 交易時，雙方會建立並簽署新的 Commitment Transaction，以反映通道的新狀態。

讓我們舉一個簡單的例子：


- 初始狀態**：Alice 有 **100,000 薩托希**，Bob 有 **30,000 薩托希**。
- 在 Alice 傳送 **40,000 薩托希**給 Bob 的交易後，新的 Commitment Transaction 會以下列方式分配資金：
  - 愛麗絲 **60,000 薩托希*
  - 鮑勃 **70,000 薩托希*

![LNP201](assets/en/22.webp)

任何時候，雙方都可以發佈**最新簽署的 Commitment Transaction** 來關閉通道並收回資金。

### 缺點：透過發佈舊交易作弊

如果其中一方決定**騙取**，發布舊的 Commitment Transaction，就會出現潛在的問題。舉例來說，Alice 可以發佈一個舊的 Commitment Transaction，在這個 Commitment Transaction 中，她有**100,000 繫幣**，儘管現實中她只有**60,000 繫幣**。這樣她就可以從 Bob 手中竊取 **40,000 薩托希**。

![LNP201](assets/en/23.webp)

更糟的是，Alice 可能會公開第一筆提款交易，也就是頻道開放前的那筆交易，在那筆交易中，她有**13 萬 Satoshis**，因此竊取了整個頻道的資金。

![LNP201](assets/en/24.webp)

### 解決方案：撤銷金鑰和時間鎖

為了防止 Alice 這種作弊行為，在 Lightning Network 上，Commitment 交易中加入了**安全機制：


- 時間鎖**：每個 Commitment Transaction 包含 Alice 資金的時間鎖。時間鎖是一個 Smart contract 原始物件，它設定了一個時間條件，交易必須滿足這個條件才能加入區塊。這表示，如果 Alice 發佈了其中一個 Commitment 交易，在經過一定數量的區塊之前，她無法取回她的資金。這個時間鎖從 Commitment Transaction 的確認開始適用。其持續時間一般與通道的大小成正比，但也可以手動設定。
- 撤銷金鑰**：如果 Bob 擁有**撤銷金鑰**，Alice 的資金也可以立即被 Bob 使用。此金鑰由 Alice 持有的秘密和 Bob 持有的秘密組成。請注意，每個 Commitment Transaction 的這個秘密都是不同的。

由於這兩種機制的結合，鮑勃有時間偵測到愛麗絲企圖作弊，並透過撤銷金鑰取回他的輸出來懲罰她，對鮑勃來說，這意味著取回通道的所有資金。我們新的 Commitment Transaction 現在會變成這樣：

![LNP201](assets/en/25.webp)

讓我們一起詳細說明這個機制的運作。

### 交易更新流程

當 Alice 和 Bob 用新的 Lightning 交易更新通道的狀態時，他們會預先 Exchange 他們各自的**秘密**為之前的 Commitment Transaction（即將過時並可能允許其中一人作弊的那個）。這表示，在通道的新狀態中：


- Alice 和 Bob 有一個新的 Commitment Transaction，代表閃電交易後目前的資金分佈。
- 每個人都有對方之前交易的秘密，只有當其中一方嘗試作弊，在 Bitcoin 節點的 mempool 中發佈舊狀態的交易時，他們才能使用撤銷金鑰。事實上，為了懲罰對方，必須同時持有兩個秘密和對方的 Commitment Transaction，其中包括已簽署的輸入。如果沒有這個交易，光有撤銷金鑰是沒有用的。要取得這筆交易的唯一方法，就是在時間鎖定期間，從 mempool（等待確認的交易中）或 Blockchain 上已確認的交易中擷取，這證明對方無論有意或無意，都在試圖作弊。

讓我們舉個例子來了解這個過程：


- 初始狀態**：Alice 有 **100,000 薩托希**，Bob 有 **30,000 薩托希**。

![LNP201](assets/en/26.webp)


- Bob 希望透過他們的 Lightning 頻道從 Alice 收到 40,000 Satoshis。要做到這一點
   - 他傳送 Invoice 給她，並附上他之前 Commitment Transaction 的撤銷金鑰的秘密。
   - 作為回應，Alice 提供她對 Bob 的新 Commitment Transaction 的簽章，以及她對之前交易的撤銷金鑰的秘密。
   - 最後，Bob 為 Alice 的新 Commitment Transaction 傳送他的簽章。
   - 這些交易所允許 Alice 透過他們的通道在 Lightning 上向 Bob 傳送 **40,000 薩托希**，而新的 Commitment 交易現在反映了這種新的資金分配方式。

![LNP201](assets/en/27.webp)


- 如果 Alice 嘗試公開她仍擁有 **100,000 薩托希**的舊 Commitment Transaction，Bob 在取得撤銷金鑰後，可以立即使用此金鑰收回資金，而 Alice 則會被時間鎖阻擋。

![LNP201](assets/en/28.webp)

即使在這種情況下，鮑勃對嘗試作弊沒有任何經濟利益，但如果他還是這樣做，愛麗絲也會從提供相同保證的對稱保護中獲益。

**您應該從本章中獲得什麼？

Lightning Network 上的**Commitment 交易**包含安全機制，可降低作弊的風險以及作弊的誘因。在簽署新的 Commitment Transaction 之前，Alice 和 Bob 會 Exchange 他們各自對於之前 Commitment 交易的**秘密**。如果 Alice 試圖發表舊的 Commitment Transaction，Bob 可以使用 **revocation key** 在 Alice 收回所有資金之前收回（因為她被時間鎖阻擋），這會懲罰她試圖作弊。

此安全系統可確保參與者遵守 Lightning Network 的規則，而且他們無法從發布舊的 Commitment 交易中獲利。

訓練到此，您已知道 Lightning 通道如何開啟，以及通道內的交易如何運作。在下一章中，我們將發現關閉通道和在主 Blockchain 上收回比特幣的不同方法。

## 通道封閉

<chapterId>29a72223-2249-5400-96f0-3756b1629bc2</chapterId>

:::video id=4d8ad4e6-32ff-46d3-bd17-343929aa863b:::

在本章中，我們將討論在 Lightning Network 上**關閉通道**，這是透過 Bitcoin 交易完成的，就像開啟通道一樣。在了解通道內的交易如何運作後，現在該看看如何在 Bitcoin Blockchain 上關閉通道並收回資金。

### 渠道生命週期的提醒

通道的**生命週期**始於透過 Bitcoin 交易進行的**開啟**，然後在其中進行 Lightning 交易，最後，當交易各方希望收回資金時，通道會透過第二次 Bitcoin 交易進行**關閉**。在 Lightning 上進行的中間交易由未公開的 **Commitment 交易來表示。

![LNP201](assets/en/29.webp)

### 通道封閉的三種類型

關閉此通道的方法主要有三種，可稱為**良民、蠻民、逃兵** (靈感來自 Andreas Antonopoulos 在 _Mastering Lightning Network_ 一書)：


- 好的**：**合作關閉**，Alice 和 Bob 同意關閉通道。
- 壞**：**強制關閉**，其中一方決定誠實地關閉通道，但未經對方同意。
- 醜陋**：**結案有作弊**，其中一方企圖透過發布舊的 Commitment Transaction（任何但非最後一份，它反映了實際且公平的資金分配）來竊取資金。

讓我們舉個例子：


- Alice 擁有 **100,000 薩托希**，Bob 擁有 **30,000 薩托希**。
- 此分佈反映在 **2 個 Commitment 交易**（每個使用者一個）中，這些交易並未公佈，但在通道關閉時可能會公佈。

![LNP201](assets/en/30.webp)

### 好處：合作關閉

在**合作關閉**中，Alice 和 Bob 同意關閉通道。事情是這樣的


- Alice 透過 Lightning 通訊協定傳送訊息給 Bob，建議關閉通道。
- Bob 同意，雙方在通道中不再進行交易。

![LNP201](assets/en/31.webp)


- Alice 和 Bob 一起協商**成交交易**的費用。這些費用通常根據成交時的 Bitcoin 費用市場來計算。必須注意的是，**總是由開啟通道的人**（在我們的例子中為 Alice）支付成交費用。
- 他們建構一個新的 ** 結束交易。此交易類似 Commitment Transaction，但沒有時間鎖或撤銷機制，因為雙方都是合作的，不存在作弊的風險。因此，這種合作式成交交易與 Commitment 交易不同。

例如，如果 Alice 擁有**100,000 Satoshis**，Bob 擁有**30,000 Satoshis**，在沒有時間限制的情況下，成交交易會將**100,000 Satoshis**傳送至 Alice 的 Address，並將**30,000 Satoshis**傳送至 Bob 的 Address。一旦雙方簽署此交易，Alice 就會公佈此交易。一旦交易在 Bitcoin Blockchain 上確認，Lightning 通道將正式關閉。

![LNP201](assets/en/32.webp)

**合作關閉**是首選的關閉方式，因為它速度快（無時間鎖定），而且交易費用會根據當前的 Bitcoin 市場情況進行調整。這可避免支付太少，可能導致交易在 mempools 中受阻的風險，或不必要地支付過多，導致參與者不必要的財務損失。

### 壞處：被迫關閉

當 Alice 的節點傳送訊息到 Bob 的節點要求合作關閉時，如果他沒有回應 (例如，由於網際網路中斷或技術問題)，Alice 可以透過發佈**上一次簽署的 Commitment Transaction** 來進行**強制關閉**。

在這種情況下，Alice 只需發佈最後一個 Commitment Transaction，它反映了最後一個 Lightning 交易發生時的通道狀態，並有正確的資金分配。

![LNP201](assets/en/33.webp)

此交易包括 Alice 資金的**時間鎖定**，使得結算速度較慢。

![LNP201](assets/en/34.webp)

另外，Commitment Transaction的費用在結算時可能不適合，因為這些費用是在建立交易時設定的，有時是在幾個月前。一般而言，Lightning 客戶會高估費用以避免日後的問題，但這可能會導致過高的費用，反之也可能過低。

總而言之，**強制關閉**是對等端不再回應時的最後選擇。它比合作關閉更慢、更不經濟。因此，應該儘量避免。

### 騙子：作弊

最後，當其中一方嘗試公布舊的 Commitment Transaction，通常是他們持有的資金比他們應該持有的還要多時，就會發生**作弊**的關閉。例如，Alice 可能會公佈一筆舊的交易，其中她擁有**120,000 薩托希**，但實際上她現在只擁有**100,000**。

![LNP201](assets/en/35.webp)

鮑勃為了防止這種作弊行為，會監控 Bitcoin Blockchain 及其 Mempool，以確保愛麗絲不會發佈舊的交易。如果 Bob 偵測到有作弊的企圖，他可以使用 **revocation key** 來收回 Alice 的資金，並透過拿走通道的全部資金來懲罰她。由於 Alice 的輸出被時間鎖阻擋，Bob 有時間在他這邊沒有時間鎖的情況下，在他擁有的 Address 上花費時間來取回全部的款項。

![LNP201](assets/en/36.webp)

很明顯，如果 Bob 沒有在 Alice 輸出的時間鎖所規定的時間內採取行動，作弊就有可能成功。在這種情況下，Alice 的輸出被解鎖，允許她消耗輸出來建立一個新的輸出到她所控制的 Address。

**您應該從本章中獲得什麼？

有三種方法可以關閉通道：


- 合作關閉**：快速且成本較低，雙方同意關閉通路，並發佈量身訂做的關閉交易。
- 強制關閉**：不太可取，因為它依賴於發布 Commitment Transaction，有可能不適合的費用和時間鎖定，這會減慢關閉速度。
- 作弊**：如果其中一方嘗試透過公開舊交易來盜取資金，另一方可以使用撤銷金鑰來懲罰這種作弊行為。

在接下來的章節中，我們將從更廣闊的角度來探討 Lightning Network，著重於其網路的運作方式。

# 流動資金網絡

<partId>a873f1cb-751f-5f4a-9ed7-25092bfdef11</partId>

## Lightning Network

<chapterId>45a7252c-fa4f-554b-b8bb-47449532918e</chapterId>

:::video id=38419c23-5592-4573-b0a7-84824a5bfb77:::

在本章中，我們將探討在Lightning Network上的付款如何能到達收款人，即使他們之間沒有直接的付款通道連接。事實上，Lightning 是一個**支付通道的網路，它允許透過其他參與者的通道將資金傳送至遠方的節點。我們將發現支付如何在整個網路中傳遞、流動資金如何在通道之間移動，以及交易費用是如何計算的。

### 付款管道網路

在 Lightning Network 上，交易對應於兩個節點之間的資金轉移。如前幾章所見，要進行 Lightning 交易，必須與某人打開一個通道。這個通道允許幾乎無限次的 off-chain 交易，然後再關閉，以收回 On-Chain 的餘額。但是，這種方法的缺點是需要與對方建立直接的通道才能接收或發送資金，這意味著每個通道都有一個開啟交易和關閉交易。如果我打算與此人進行大量付款，開啟和關閉一個通道就變得很划算。相反，如果我只需要執行幾筆 Lightning 交易，開立直接通道就不具優勢，因為這會讓我花費 2 個 On-Chain 交易來進行有限的 off-chain 交易。舉例來說，當想在某個商家使用 Lightning 付款而不打算返回時，就可能發生這種情況。

為了解決這個問題，Lightning Network 允許透過多個通道和中介節點來路由付款，因此可以在沒有與對方直接通道的情況下進行交易。

例如，想像一下：


- Alice** (橘色) 與 **Suzie** (灰色) 有一個通道，她這邊有 **100,000 聰明**，而 Suzie 這邊有 **30,000 聰明**。
- Suzie** 與 **Bob** 有一個頻道，其中她擁有 **250,000 薩托希**，而 Bob 沒有任何薩托希。

![LNP201](assets/en/37.webp)

如果 Alice 想要將資金寄給 Bob 而不直接與他開通管道，她就必須透過 Suzie，而每個管道都需要調整雙方的流動性。 **發送的 Satoshis 會留在各自的通道**內；它們實際上並沒有「跨過」通道，而是透過調整每個通道的內部流動性來進行轉移。

假設 Alice 想要寄送 **50,000 Satoshis** 給 Bob：


- Alice** 在他們的共同頻道中向 **Suzie** 傳送 50,000 Satoshis。
- Suzie** 複製此轉移，在他們的頻道中傳送 50,000 薩托希給 **Bob**。

![LNP201](assets/en/38.webp)

因此，付款是透過每個通道中的流動資金移動來傳送給 Bob。操作結束時，Alice 最終擁有 50,000 Sats。她確實轉移了 50,000 Sats，因為最初她有 100,000。Bob 這邊則多了 50,000 Sats。對 Suzie (中間節點) 來說，這個操作是中性的：最初，她與 Alice 的通道中有 30,000 Sats，與 Bob 的通道中有 250,000 Sats，總共 280,000 Sats。操作之後，她與 Alice 的頻道中有 80,000 Sats，與 Bob 的頻道中有 200,000 Sats，總數與開始時相同。

因此，這種轉移受到轉移方向上**可用流動性的限制。

### 航線和流動性限制的計算

讓我們以另一個網路的理論範例與：


- 130,000 薩托希**在愛麗絲這邊（橘色）與**蘇西**（灰色）的頻道中。
- 90,000梭子**在**Suzie**一方，**200,000梭子**在**Carol**一方（粉紅色）。
- 150,000 薩托希**在**Carol**一方，**100,000 薩托希**在**Bob**一方。

![LNP201](assets/en/39.webp)

在此配置中，Alice 能發送給 Bob 的最大金額為 **90,000薩托希**，因為她受限於從 **Suzie 到 Carol** 的通道中可用的最小流動資金。在相反方向（從鮑勃到愛麗斯），則無法付款，因為在**蘇西與**愛麗斯**的通道中，**蘇西的**端不含任何梭子。因此，在這個方向上沒有可用於轉帳的**路徑。

Alice 透過通道傳送 **40,000 薩托希**給 Bob：


- Alice 轉了 40,000 薩托希到她和 Suzie 的頻道。
- Suzie 在他們共用的頻道中轉帳 40,000 Satoshis 給 Carol。
- Carol 最後轉了 40,000 Satoshis 給 Bob。

![LNP201](assets/en/40.webp)

每個通道中發送的**衛星**會留在通道中**，因此 Carol 發送給 Bob 的衛星與 Alice 發送給 Suzie 的衛星並不相同。轉移只會透過調整每個通道內的流動性來進行。此外，通道的總容量維持不變。

![LNP201](assets/en/41.webp)

如同上一個範例，交易完成後，來源節點 (Alice) 少了 40,000 Satoshis。中間節點 (Suzie 和 Carol) 保留相同的總金額，因此對他們來說，這項作業是中性的。最後，目的地節點 (Bob) 收到額外的 40,000 Satoshis。

因此，中間節點的角色對 Lightning Network 的運作非常重要。它們通過提供多種支付路徑來促進轉移。為了鼓勵這些節點提供其流動性並參與路由支付，我們會向它們支付**路由費**。

### 路由費

中間節點收取費用，允許付款通過其通道。這些費用由每個節點為每個通道**設定。費用包括 2 個 Elements：


- 「**基本費用**」：每個頻道的固定金額，預設通常是**1 sat**，但可自訂。
- 「**變量費用**」：傳輸數量的百分比，以**百萬分之一 (ppm) **計算。預設為 **1 ppm**（每百萬 Satoshis 轉移 1 sat），但也可以調整。

費用也因轉帳方向不同而異。例如，從 Alice 轉帳至 Suzie，則採用 Alice 的費用。相反，從 Suzie 轉帳至 Alice，則採用 Suzie 的費用。

例如，對於 Alice 和 Suzie 之間的通道，我們可以有：


- Alice**：基本費用為 1 sat，可變費用為 1 ppm。
- Suzie**: 基本費用為 0.5 sat，浮動費用為 10 ppm。

![LNP201](assets/en/42.webp)

為了更了解費用的運作方式，讓我們來研究之前相同的 Lightning Network，但現在的路由費用如下：


- 頻道 **Alice - Suzie**：Alice 的基本費用為 1 Satoshi 和 1 ppm。
- 頻道 **Suzie - Carol**：Suzie 的基本費用為 0 Satoshi 和 200 ppm。
- Carol - Bob** 通道：基本費用為 1 Satoshi 和 Suzie 的 1 ppm 2.

![LNP201](assets/en/43.webp)

同樣是支付**40,000 薩托希**給鮑勃，愛麗絲必須多寄一點，因為每個中介節點都會扣除其費用：


- Carol** 在與 Bob 的頻道上扣除 1.04 Satoshis：

$$ f*{text{Carol-Bob}} = （基本費用）+ left(\frac{text{ppm} \times \text{amount}}{10^6}\right) $$$

$$ f*{text{Carol-Bob}} = 1 + \frac{1 \times 40000}{10^6} = 1 + 0.04 = 1.04 \text{ Sats} $$


- Suzie** 在與 Carol 的頻道上扣除 8 Satoshis 的費用：

$$ f*{text{Suzie -Carol}} = \text{base fee}+ left(\frac{text{ppm} \times \text{amount}}{10^6}\right) $$$

$$ f*{text{Suzie-Carol}} = 0 + \frac{200 \times 40001.04}{10^6} = 0 + 8.0002 \approx 8 \text{ Sats} $$

因此，在這條路徑上支付的費用總額為 **9.04 薩托希**。因此，愛麗絲必須寄出 **40,009.04 繫幣**，鮑勃才能收到準確的 **40,000 繫幣**。

![LNP201](assets/en/44.webp)

因此更新了流動性：

![LNP201](assets/en/45.webp)

### 洋蔥路由

要將付款從寄件者路由至收件者，Lightning Network 使用一種稱為「**洋蔥路由**」的方法。傳統資料的路由是由每個路由器根據目的地決定資料的方向，洋蔥路由的運作方式則不同：


- 發送節點會計算整個路徑**：例如，Alice 決定她的付款必須先經過 Suzie 和 Carol 才能到達 Bob。
- 每個中介節點只知道它的近鄰**：Suzie 只知道她從 Alice 收到資金，而且她必須將資金轉帳給 Carol。但是，Suzie 不知道 Alice 是來源節點還是中介節點，她也不知道 Carol 是收款節點還是只是另一個中介節點。這個原則也適用於 Carol 和路徑上的所有其他節點。因此，洋蔥路由透過遮蔽寄件者和最終收件者的身分，來保護交易的機密性。

為了確保傳送節點能在洋蔥路由中計算出通往接收者的完整路由，它必須維護一個 ** 網路圖，以了解其拓樸並決定可能的路由。

**您應該從本章中獲得什麼？


- 在 Lightning 上，付款可在透過中介渠道間接連接的節點之間傳遞。這些中介節點中的每個節點都促進了流動性中繼。
- 中介節點會就其服務收取佣金，包括固定費用和浮動費用。
- 洋蔥路由允許傳輸節點在中介節點不知道來源或最終目的地的情況下計算完整的路由。

在本章中，我們探討了 Lightning Network 上的付款路由。但有一個問題出現：如何防止中間節點接受收到的付款而不將其轉送到下一個目的地，以達到截取交易的目的？這正是我們將在下一章研究的 HTLC 的角色。

## HTLC - 散列時間鎖定 Contract

<chapterId>4369b85a-1365-55d8-99e1-509088210116</chapterId>

:::video id=6f204b92-55a5-4939-9440-7c5b96a297bf:::

在本章中，我們將發現 Lightning 如何允許付款通過中介節點而無需信任它們，這要歸功於 **HTLC**（_Hashed Time-Locked Contracts_）。這些智能合約確保每個中介節點只有在轉發付款給最終收款人時，才會從其通道收到資金，否則，付款將不被驗證。

因此，支付路由所產生的問題是對中介節點以及中介節點之間的必要信任。為了說明這一點，讓我們重溫一下有 3 個節點和 2 個通道的 Lightning Network 簡化範例：


- Alice 與 Suzie 有一個頻道。
- Suzie 和 Bob 有一個頻道。

Alice 想要傳送 40,000 Sats 給 Bob，但她與 Bob 沒有直接通道，也不想開啟通道。她尋找一條路徑，並決定經過 Suzie 的節點。

![LNP201](assets/en/46.webp)

如果 Alice 天真地寄 40,000 薩托希給 Suzie，希望 Suzie 將這筆錢轉給 Bob，Suzie 可以將這筆資金據為己有，不傳送任何東西給 Bob。

![LNP201](assets/en/47.webp)

為了避免這種情況，在 Lightning 上，我們使用 HTLCs (Hashed Time-Locked Contracts，散列時間鎖定合約)，它讓中介節點的付款成為有條件的，也就是說 Suzie 必須滿足某些條件，才能存取 Alice 的資金並轉帳給 Bob。

### HTLC 的工作原理

HTLC 是基於兩個原則的特殊 Contract：


- 存取條件**：收款人必須揭露一個秘密，才能解鎖應付給他們的付款。
- 到期**：如果在規定期限內未完全完成付款，則會取消付款，並將資金退回給發行者。

以下是在我們的範例中，Alice、Suzie 和 Bob 是如何運作的：

![LNP201](assets/en/48.webp)

**創建秘密**：鮑勃產生一個隨機秘密，記為 _s_（前影像），並使用記為 _h_ 的 Hash 函數計算其 Hash，記為 _r_。我們有

$$
r = h(s)
$$

使用 Hash 函式會使得只用 _h(s)_ 就無法找到 _s_，但如果提供 _s_，就很容易驗證它是否對應 _h(s)_。

![LNP201](assets/en/49.webp)

**傳送付款請求**：Bob 傳送一個 **Invoice** 給 Alice 要求付款。此 Invoice 顯然包含 Hash _r_。

![LNP201](assets/en/50.webp)

**寄出有條件的付款**：Alice 寄出 40,000 薩托希的 HTLC 給 Suzie。Suzie 收到這些資金的條件是，她提供 Alice 一個滿足以下等式的秘密 _s'_：

$$
h(s') = r
$$

![LNP201](assets/en/51.webp)

** 將 HTLC 轉移給最終接收者**：Suzie 若要從 Alice 處取得 40,000 薩托希，必須將類似的 40,000 薩托希的 HTLC 轉移給 Bob，而 Bob 也有相同的條件，就是他必須提供 Suzie 一個滿足等式的秘密 _s'_：

$$
h(s') = r
$$

![LNP201](assets/en/52.webp)

** 由秘密 _s_** 驗證：Bob 提供 _s_ 給 Suzie，以獲得 HTLC 承諾的 40,000 薩托希。有了這個秘密，Suzie 就可以解鎖 Alice 的 HTLC，並從 Alice 取得 40,000 薩托希。然後付款就會正確地傳送至 Bob。

![LNP201](assets/en/53.webp)

這個過程可以防止 Suzie 在沒有完成轉帳給 Bob 的情況下保留 Alice 的資金，因為她必須將款項傳送給 Bob 才能取得秘密 _s_，進而解除 Alice 的 HTLC 的鎖定。即使路由包含數個中間節點，操作仍然相同：只需針對每個中間節點重複 Suzie 的步驟即可。每個節點都會受到 HTLC 條件的保護，因為接收者解鎖最後一個 HTLC 會自動觸發串聯中所有其他 HTLC 的解鎖。

### HTLC 的到期和問題時的管理

如果在付款過程中，其中一個中介節點或收款節點停止回應，尤其是在網路或電力中斷的情況下，那麼付款就無法完成，因為解鎖 HTLC 所需的秘密並未傳送。以 Alice、Suzie 和 Bob 為例，如果 Bob 沒有傳送秘密 _s_ 給 Suzie，這個問題就會發生。在此情況下，路徑上游的所有 HTLC 都會被封鎖，它們所保證的資金也會被封鎖。

![LNP201](assets/en/54.webp)

為了避免這種情況，Lightning 上的 HTLC 有一個到期日，如果交易在某個時間後仍未完成，就可以移除 HTLC。過期遵循特定的順序，因為它首先從最接近收件人的 HTLC 開始，然後逐漸上移到交易的發行者。在我們的範例中，如果 Bob 從未將秘密 _s_ 交給 Suzie，這會首先導致 Suzie 對 Bob 的 HTLC 過期。

![LNP201](assets/en/55.webp)

然後從 Alice 到 Suzie 的 HTLC。

![LNP201](assets/en/56.webp)

如果到期的順序相反，Alice 可以在 Suzie 能夠保護自己免於潛在作弊之前收回她的付款。事實上，如果鮑勃回來領回他的 HTLC，而愛麗絲已經移除她的 HTLC，Suzie 就會處於劣勢。因此，HTLC 到期的連鎖順序可確保沒有中間節點遭受不公平的損失。

### HTLC 在 Commitment 交易中的代表性

Commitment 交易代表 HTLC，在 HTLC 的生命週期中，如果通道強制關閉，它們對 Lightning 施加的條件可以轉移到 Bitcoin。提醒一下，Commitment 交易代表兩個使用者之間通道的當前狀態，並允許在發生問題時單方強制關閉。通道的每個新狀態都會建立兩個 Commitment 交易：每一方一個。讓我們重溫 Alice、Suzie 和 Bob 的範例，但更仔細地看看當 HTLC 建立時，Alice 和 Suzie 之間的通道層級會發生什麼事。

![LNP201](assets/en/57.webp)

在 Alice 和 Bob 之間的 40,000 Sats 支付開始之前，Alice 與 Suzie 的通道中有 100,000 Sats，而 Suzie 持有 30,000。他們的 Commitment 交易如下：

![LNP201](assets/en/58.webp)

Alice 剛收到 Bob 的 Invoice，其中特別包含 _r_，也就是秘密的 Hash。因此，她可以與 Suzie 建立一個 40,000 Satoshis 的 HTLC。這個 HTLC 在最新的 Commitment 交易中表示為 Alice 一方稱為「**_HTLC Out_**」的輸出，因為資金是流出的，而 Suzie 一方稱為「**_HTLC In_**」，因為資金是流入的。

![LNP201](assets/en/59.webp)

這些與 HTLC 相關的輸出具有完全相同的條件，即：


- 如果 Suzie 能提供秘密 _s_，她就能立即解鎖此輸出，並將其傳輸到她所控制的 Address 上。
- 如果 Suzie 不擁有秘密 _s_，她就無法解鎖此輸出，而 Alice 將可在時間鎖後解鎖，將輸出傳送至她所控制的 Address。因此，如果 Suzie 取得 _s_，時間鎖會賦予她一段反應時間。

這些條件只適用於通道關閉 (即 Commitment Transaction 發佈 On-Chain)，而 HTLC 仍在 Lightning 上活動的情況，也就是說 Alice 和 Bob 之間的付款尚未完成，而且 HTLC 尚未過期。由於這些條件，Suzie 可以藉由提供 _s_ 來收回 HTLC 欠她的 40,000 薩托希。否則，Alice 會在時間鎖到期後才取回資金，因為如果 Suzie 不知道 _s_，就表示她沒有轉帳 40,000 Satoshis 給 Bob，因此 Alice 的資金並不欠她。

此外，如果通道在數個 HTLC 待處理時關閉，則會有與正在進行的 HTLC 數量相同的額外輸出。

如果通道沒有關閉，那麼在 Lightning 付款到期或成功之後，就會創建新的 Commitment 交易來反映新的、現在已經穩定的通道狀態，也就是沒有任何 HTLC 的待定狀態。因此，與 HTLC 相關的輸出可以從 Commitment 交易中移除。

![LNP201](assets/en/60.webp)

最後，在 HTLC 活動時合作通道關閉的情況下，Alice 和 Suzie 會停止接受新的付款，並等待正在進行的 HTLC 解決或到期。這讓他們可以發表較輕的關閉交易，而不需要 HTLC 相關的輸出，因此可以減少費用，並避免等待可能的時間鎖定。

**您應該從本章中獲得什麼？

HTLC 可使 Lightning 付款通過多個節點進行路由，而無需信任這些節點。以下是需要記住的重點：


- HTLC 可透過秘密（預設影像）和過期時間確保付款的安全性。
- HTLC 的解析或到期遵循特定順序：然後從目的地朝向來源，以保護每個節點。
- 只要 HTLC 既未解決也未過期，它就會保留為最新 Commitment 交易的輸出。

在下一章中，我們將發現發出 Lightning 交易的節點如何尋找和選擇路徑，使其付款到達收款節點。

## 尋找方向

<chapterId>7e2ae959-c2a1-512e-b5d6-8fd962e819da</chapterId>

:::video id=e5baa834-111d-46f5-a28b-3538bed2bbb0:::

在前面的章節中，我們看到了如何使用其他節點的通道來路由付款，並在不透過通道直接連接到節點的情況下到達該節點。我們也討論了如何在不信任中介節點的情況下，確保轉帳的安全性。在本章中，我們將專注於尋找到達目標節點的最佳路徑。

### 閃電中的路由問題

正如我們所見，在 Lightning 中，付款節點必須計算到收款人的完整路由，因為我們使用的是洋蔥路由系統。中介節點既不知道起始點，也不知道最終目的地。它們只知道付款來自哪裡，以及接下來必須傳送到哪個節點。這意味著，發送節點必須維護一個動態的本地網路拓樸，包括現有的 Lightning 節點和每個節點之間的通道，並考慮到開放、關閉和狀態更新。

![LNP201](assets/en/61.webp)

即使 Lightning Network 採用這種拓樸結構，仍有一些傳送節點無法取得的重要路由資訊，也就是通道在任何特定時刻的確切流動資金分佈。事實上，每個通道只顯示其**總容量**，但資金的內部分佈只有兩個參與節點知道。這對有效路由造成挑戰，因為付款成功與否主要取決於其金額是否小於所選路徑的最低流動性。但是，發送節點無法看到所有的流動性。

![LNP201](assets/en/62.webp)

### 網路地圖更新

為了保持其網路地圖的最新狀態，節點會透過稱為 "**_gossip_**"的演算法定期傳送 Exchange 訊息。這是一種分散式演算法，用來以流行的方式將資訊傳播給網路中的所有節點，可在幾個通訊週期內完成 Exchange 和頻道的 Global State 同步。每個節點將資訊傳播給一個或多個隨機或非隨機選擇的鄰居，這些鄰居再將資訊傳播給其他鄰居，如此類推，直到達到全球同步狀態。

Lightning 節點之間交換的 2 個主要訊息如下：


- 「**頻道公告**」：標示開啟新頻道的訊息。
- 「**通道更新**」：通道狀態的更新訊息，特別是費用的演變（但不包括流動性的分佈）。

Lightning 節點也會監控 Bitcoin Blockchain 以偵測通道關閉交易。關閉的通道會從地圖上移除，因為它不能再用來路由我們的付款。

### 路由付款

讓我們以一個有 7 個節點的小型 Lightning Network 為例：Alice、Bob、1、2、3、4 和 5。想像一下，Alice 想要傳送款項給 Bob，但必須經過中間節點。

![LNP201](assets/en/63.webp)

以下是這些管道的實際資金分佈：


- Alice 和 1**之間的通道：Alice 側 250,000 Sats，1 側 80,000 (總容量為 330,000 Sats)。
- 1 號與 2 號之間的通道**：1 側 300,000 Sats，2 側 200,000 (總容量為 500,000 Sats)。
- 2 號與 3 號之間的通道**：2 號側 50,000 Sats，3 號側 60,000 (總容量為 110,000 Sats)。
- 2 和 5 之間的通道**：90,000 Sats 位於第 2 側，160,000 位於第 5 側（總容量為 250,000 Sats）。
- 2 和 4 之間的通道**：第 2 側 180,000 Sats，第 4 側 110,000 (總容量為 290,000 Sats)。
- 4 和 5 之間的通道**：第 4 側 200,000 Sats，第 5 側 10,000 (總容量 210,000 Sats)。
- 3 和 Bob 之間的通道**：50,000 Sats 位於 3 號側，250,000 位於 Bob 側（總容量為 300,000 Sats）。
- 5 和 Bob 之間的通道**：260,000 Sats 位於 5 號側，100,000 位於 Bob 側（總容量為 360,000 Sats）。

![LNP201](assets/en/64.webp)

要從 Alice 向 Bob 支付 100,000 Sats，路由選擇受限於每個通道的可用流動性。根據已知的流動性分佈，Alice 的最佳路徑可能是序列 `Alice → 1 → 2 → 4 → 5 → Bob`：

![LNP201](assets/en/65.webp)

但由於 Alice 不知道每個通道中資金的確切分佈情況，因此她必須以概率方式估計最佳路徑，並考慮到下列準則：


- 成功概率**：總容量較高的通道更有可能包含足夠的流動性。例如，節點 2 和節點 3 之間的通道總容量為 110,000 Sats，因此不太可能在節點 2 一側找到 100,000 Sats 或更多，儘管仍有可能。
- 交易費用**：在選擇最佳路由時，傳送節點也會考慮每個中間節點所收取的費用，並尋求總路由成本最小化。
- HTLC 的到期時間**：為避免付款受阻，HTLC 的到期時間也是需要考慮的參數。
- 中間節點的數量**：最後，更廣泛來說，發送節點會尋求與最少的節點一起尋找路徑，以降低失敗的風險，並限制 Lightning 交易費用。

透過分析這些標準，傳送節點可以測試最可能的路由，並嘗試最佳化。在我們的範例中，Alice 可以將最佳路由排序如下：


- `Alice→1→2→5→Bob`，因為這是容量最大的最短路徑。
- `Alice→1→2→4→5→Bob`，因為這條路線提供良好的容量，雖然它比第一條路線長。
- `Alice→1→2→3→Bob`，因為此路徑包括`2→3`通道，該通道的容量非常有限，但仍有可能可用。

### 付款執行

Alice 決定測試她的第一條路線 (`Alice→1→2→5→Bob`)。因此，她向節點 1 傳送 100,000 Sats 的 HTLC。此節點與節點 2 檢查是否有足夠的流動資金，並繼續傳輸。節點 2 接著收到節點 1 的 HTLC，但意識到它與節點 5 的通道中沒有足夠的流動資金來傳送 100,000 Sats 的付款。於是節點 2 將錯誤訊息傳回節點 1，再由節點 1 傳送給 Alice。此路由失敗。

![LNP201](assets/en/66.webp)

然後 Alice 嘗試使用她的第二個路由 (`Alice→1→2→4→5→Bob`)來路由她的付款。她將 100,000 Sats 的 HTLC 傳送給節點 1，節點 1 傳送給節點 2，然後傳送給節點 4、節點 5，最後傳送給 Bob。這一次，流動資金充足，路由也正常運作。每個節點使用鮑勃提供的預先影像 (秘密 _s_)，逐級解鎖其 HTLC，這使得愛麗絲支付給鮑勃的款項得以成功落實。

![LNP201](assets/en/67.webp)

路由的搜尋方式如下：發送節點先找出可能的最佳路由，然後連續嘗試付款，直到找到可運作的路由為止。

值得注意的是，Bob 可以在 **Invoice** 中為 Alice 提供資訊，以方便路由。例如，他可以指出附近有足夠流動性的頻道，或揭示私人頻道的存在。這些指示可讓 Alice 避開成功機會不高的路徑，並首先嘗試 Bob 建議的路徑。

**您應該從本章中獲得什麼？


- 節點透過公告和監視 Bitcoin Blockchain 上的通道關閉情況來維護網路拓樸圖。
- 尋找付款的最佳路徑仍然是概率性的，並且取決於許多標準。
- Bob 可以在**Invoice**中提供指示，以指導 Alice 的路由選擇，讓她不用測試不可能的路由。

在下一章中，除了 Lightning Network 上使用的一些其他工具外，我們將特別研究發票的功能。

# Lightning Network 的工具

<partId>74d6c334-ec5d-55d9-8598-f05694703bf6</partId>

## Invoice、LNURL 和 Keysend

<chapterId>e34c7ecd-2327-52e3-b61e-c837d9e5e8b0</chapterId>

:::video id=309c3412-506e-4189-ad46-5e5088c55008:::

在本章中，我們將進一步了解 Lightning **發票**的操作，也就是收款節點發送給發款節點的付款請求。我們的目標是了解如何在Lightning上付款和收款。我們還將討論經典發票的兩個替代方案：LNURL 和 Keysend。

![LNP201](assets/en/68.webp)

### Lightning 發票的結構

如 HTLC 章節所述，每次付款都會先由收款人產生**Invoice**。然後將 Invoice 傳送給付款方（透過 QR 碼或複製貼上），以啟動付款。Invoice 包含兩個主要部分：


- 人類可讀部分**：此部分包含清晰可見的元資料，以提升使用者體驗。
- Payload**: 此部分包含供機器處理付款的資訊。

Invoice 的典型結構以表示「閃電」的識別符`LN`開頭，接著是表示 Bitcoin 的`bc`，然後是 Invoice 的數量。分隔符 "1 "將人類可讀部分與資料（有效載荷）部分區分開來。

讓我們以下面的 Invoice 為例：

```invoice
lnbc100u1p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

我們已經可以將它分成 2 個部分。首先是人類可讀的部分：

```invoice
lnbc100u
```

然後是打算用於有效載荷的部分：

```invoice
p0x7x7dpp5l7r9y50wrzz0lwnsqgxdks50lxtwkl0mhd9lslr4rcgdtt2n6lssp5l3pkhdx0cmc9gfsqvw5xjhph84my2frzjqxqyz5vq9qsp5k4mkzv5jd8u5n89d2yc50x7ptkl0zprx0dfjh3km7g0x98g70hsqq7sqqqgqqyqqqqlgqqvnv2k5ehwnylq3rhpd9g2y0sq9ujyxsqqypjqqyqqqqqqqqqqqsqqqqq9qsq3vql5f6e45xztgj7y6xw6ghrcz3vmh8msrz8myvhsarxg42ce9yyn53lgnryx0m6qqld8fql
```

這兩個部分以`1`分隔。選用此分隔符而非特殊字元，是為了方便雙擊即可複製貼上整個 Invoice。

在第一部分中，我們可以看到：


- `LN` 表示這是一個 Lightning 交易。
- `bc` 表示 Lightning Network 在 Bitcoin Blockchain 上（而不在 Testnet 或 Litecoin 上）。
- `100u` 表示 Invoice 的數量，以 **microbitcoins** 表示 (`u`意為「微」)，在此等於 10,000 Sats。

為了指定付款金額，它以 Bitcoin 的子單位表示。以下是使用的單位：


- Millibitcoin (表示 `m`)：** 代表千分之一的 Bitcoin。

$$
1 \, \text{mBTC} = 10^{-3} \, \text{BTC} = 10^5 \, \text{satoshis}
$$


- Microbitcoin (表示`u`):** 有時也稱為 "bit"，代表 Bitcoin 的百萬分之一。

$$
1 \, \mu\text{BTC} = 10^{-6} \, \text{BTC} = 100 \, \text{satoshis}
$$


- Nanobitcoin (表示`n`):** 代表十億分之一的 Bitcoin。

$$
1 \, \text{nBTC} = 10^{-9} \, \text{BTC} = 0.1 \, \text{satoshis}
$$


- Picobitcoin (表示`p`):** 代表 Bitcoin 的萬億分之一。

$$
1 \, \text{pBTC} = 10^{-12} \, \text{BTC} = 0.0001 \, \text{satoshis}
$$

### Invoice 的有效載荷

Invoice 的有效負載包括處理付款所需的幾項資訊：


- Timestamp：** Invoice 的創建時刻，以 Unix Timestamp 表示（自 1970 年 1 月 1 日起經過的秒數）。
- 哈希秘密**：正如我們在 HTLC 一節中所看到的，接收節點必須提供預影像的 Hash 給發送節點。這在 HTLC 中用來確保交易安全。我們稱之為 "_r_"。
- 付款秘密**：另一個秘密是由收件者產生，但這次是傳送給發件節點。它用於洋蔥路由，以防止中間節點猜測下一個節點是否是最終收件人。因此，對於路由上的最後一個中間節點而言，這可為收件者維持一種保密性。
- 收款人的公開金鑰**：向付款人表示要付款人的識別碼。
- 有效期限**：Invoice 付費的最長時間（預設為 1 小時）。
- 路由提示**：收件人提供的附加資訊，以協助寄件人最佳化付款路徑。
- 簽名**：透過認證所有資訊，保證 Invoice 的完整性。

然後，發票會以 **bech32** 編碼，格式與 Bitcoin SegWit 位址相同（格式以 `bc1` 開頭）。

### LNURL 退出

在傳統的交易中，例如商店購物，Invoice 是為要支付的總金額所產生的。一旦出示 Invoice（以 QR 碼或字符串的形式），客戶就可以掃瞄它，並完成交易。接下來的付款過程就是我們在上一節所研究的傳統流程。然而，這個流程有時對使用者體驗而言可能非常麻煩，因為它需要接收者透過 Invoice 將資訊傳送給寄送者。

在某些情況下，例如從線上服務提取比特幣，傳統的流程太過繁瑣。在這種情況下，**LNURL**提款解決方案通過顯示一個QR碼來簡化這個過程，收款人的Wallet掃描這個QR碼就可以自動創建Invoice。然後，該服務支付 Invoice，用戶只需看到一個即時提款。

![LNP201](assets/en/69.webp)

LNURL 是一種通訊協定，它指定了一系列功能，旨在簡化 Lightning 節點和用戶端以及第三方應用程式之間的互動。因此，正如我們剛剛看到的，LNURL撤銷只是其他功能中的一個例子。

此協定基於HTTP，允許為各種操作創建鏈接，如付款請求、提款請求或其他增強用戶體驗的功能。每個LNURL都是一個帶有lnurl前綴的bech32編碼URL，一旦被掃描，就會觸發Lightning Wallet上的一系列自動操作。

例如，LNURL-withdraw (LUD-03) 功能允許通過掃描 QR 代碼從服務中提取資金，而無需手動 generate 和 Invoice。同樣地，LNURL-auth (LUD-04) 可使用 Lightning Wallet 上的私人密碼匙而非密碼登入線上服務。

### 在沒有 Invoice 的情況下發送閃電付款：Keysend

另一種有趣的情況是在沒有事先收到 Invoice 的情況下轉移資金，稱為「**Keysend**」。此通訊協定允許在加密的付款資料中加入只有收款人才能存取的前置影像來傳送資金。此預設影像可讓收款人解鎖 HTLC，從而在未事先產生 Invoice 的情況下取回資金。

簡而言之，在此通訊協定中，是由寄件者而非收件者產生 HTLC 中使用的秘密。實際上，這可讓寄件者在付款前不必與收件者互動。

![LNP201](assets/en/70.webp)

**您應該從本章中獲得什麼？


- **Lightning Invoice** 是由人機可讀部分和機器資料部分組成的付款請求。
- Invoice 採用**bech32**編碼，其中的`1`分隔符方便複製，而資料部分則包含處理付款所需的所有資訊。
- Lightning 上還存在其他支付流程，特別是 **LNURL-Withdraw** 以方便提款，以及 **Keysend** 用於無需 Invoice 的直接轉帳。

在下一章中，我們將介紹節點經營者如何管理其通道的流動性，使其永遠不會被封鎖，並永遠能夠在 Lightning Network 上發送和接收付款。

## 管理您的流動資金

<chapterId>cc76d0c4-d958-57f5-84bf-177e21393f48</chapterId>

:::video id=96096aef-e4ce-4c44-a022-57e27082232a:::

在本章中，我們將探討在 Lightning Network 上有效管理流動性的策略。流動性管理因使用者類型和環境而異。我們將探討主要原則和現有技術，以便更好地瞭解如何優化這種管理。

### 流動資金需求

Lightning 上有三種主要的用戶類型，每種類型都有特定的流動性需求：


- 付款人**：這是付款者。他們需要流出的流動資金，才能將資金轉移給其他使用者。例如，這可能是消費者。
- 賣方（或收款人）**：這是接受付款的一方。他們需要流入的流動資金才能接受付款到他們的節點。例如，這可能是一個企業或網上商店。
- 路由器**：中介節點 (intermediary node)，通常專門負責路由付款，必須優化其在每個通道的流動性，以路由盡可能多的付款並賺取費用。

這些設定檔顯然不是固定的；用戶可以根據交易在付款人和收款人之間切換。舉例來說，Bob 可以透過 Lightning 從他的雇主領取薪水，這讓他處於需要流入流動資金的「賣方」位置。隨後，如果他想用自己的工資購買食物，他就變成了 「付款人」，必須有流出的流動資金。

為了更好地理解，讓我們以一個由三個節點組成的簡單網路為例：買方 (Alice)、路由器 (Suzie) 和賣方 (Bob) 。

![LNP201](assets/en/71.webp)

假設買方想要寄送 30,000 Sats 給賣方，而付款是透過路由器的節點。這時，每一方都必須在付款方向上有最低限度的流動資金：


- 付款方必須在其與路由器之間的通道上至少有 30,000 Satoshis。
- 賣家必須有一個對方有 30,000 Satoshis 的頻道，才有能力接收。
- 路由器必須在付款方的通道上有 30,000 Satoshis，同時在與賣方的通道上也有 30,000 Satoshis，才能路由付款。

![LNP201](assets/en/72.webp)

### 流動資金管理策略

付款方必須確保在其渠道一側維持足夠的流動資金，以保證流出的流動資金。這一點被證明相對簡單，因為只需開啟新的 Lightning 通道即可擁有這筆流動資金。事實上，Multisig On-Chain 鎖定的初始資金在一開始就完全在付款方的 Lightning 通道中。因此，只要開通的通道有足夠的資金，支付能力就能得到保證。當流出的流動資金用盡時，只需開啟新的通道即可。

另一方面，對於賣方而言，任務則更加複雜。為了能夠收到付款，他們必須在其通道的對方有流動資金。因此，僅僅開通一個通道是不夠的，他們還必須在這個通道中進行付款，將流動資金轉移到對方，然後他們自己才能收到付款。對於某些 Lightning 用戶類型，例如商家，他們的節點發送的和接收的明顯不成正比，因為商家的目標主要是收取比支出更多的錢，以 generate 獲取利潤。幸運的是，對於這些有特定傳入流動性需求的使用者，有幾種解決方案：


- 吸引通路**：商家因其節點預期的付款量而享有優勢。考慮到這一點，商家可以嘗試吸引那些希望從交易費用中獲利的路由節點，這些節點可能會向商家開放通道，希望路由商家的付款並收取相關費用。
- 流動資金移動**：賣方也可以打開一個通道，透過虛構付款給另一個節點，將部分資金轉移到對方，而另一個節點則會以另一種方式歸還資金。我們將在下一部分看到如何進行此操作。
- 三角開放**：有一些平台可以讓希望合作打開通道的節點，讓每個節點都能從即時流入和流出的流動資金中獲益。例如，[LightningNetwork+](https://lightningnetwork.plus/) 提供這項服務。如果 Alice、Bob 和 Suzie 想要以 100,000 Sats 來開通一個通道，他們可以在這個平台上達成協議，讓 Alice 開通一個面向 Bob 的通道，Bob 開通一個面向 Suzie 的通道，Suzie 開通一個面向 Alice 的通道。如此一來，每個人都有 100,000 Sats 的流出流動資金和 100,000 Sats 的流入流動資金，而只鎖定了 100,000 Sats。

![LNP201](assets/en/73.webp)


- 購買通道**：租賃 Lightning 通道的服務也存在，以獲得流入的流動資金，如 [Bitrefill Thor](https://www.bitrefill.com/thor-lightning-network-channels/) 或 [Lightning Labs Pool](https://lightning.engineering/pool/)。例如，Alice 可以向她的節點購買 100 萬 Satoshis 的通道，以便能夠接收付款。

![LNP201](assets/en/74.webp)

最後，對於路由器而言，其目標是將處理的付款數量和收取的費用最大化，因此他們必須：


- 以策略性節點開啟資金充裕的通路。
- 根據網路的需求，定期調整渠道中的資金分配。

### 圈出服務

由 Lightning Labs 提供的 [Loop Out](https://lightning.engineering/loop/)服務，可以將流動資金移到通道的對面，同時回收 Bitcoin Blockchain 上的資金。例如，Alice 透過 Lightning 將 100 萬 Satoshis 傳送至一個循環節點，該節點再將這些資金以 On-Chain 比特幣歸還給她。這就平衡了她的通道，每邊都有 100 萬 Satoshis，優化了她接收付款的能力。

![LNP201](assets/en/75.webp)

因此，這項服務能夠在回收個人比特幣 On-Chain 的同時，讓流動資金流入，這有助於限制使用 Lightning 接受付款所需的固定現金。

**您應該從本章中獲得什麼？


- 要在 Lightning 上發送付款，您必須在您的渠道中擁有足夠的流動資金。要增加這種發送能力，只需開闢新渠道即可。
- 要接收付款，您需要在您的通道中擁有對方的流動資金。增加這種接收能力比較複雜，因為它需要其他人向您打開通道，或進行（虛構或真實的）付款，將流動資金轉移到對方。
- 根據渠道的使用情況，維持所需的流動性可能更具挑戰性。這就是為什麼有工具和服務可以幫助平衡所需的渠道。

在下一章中，我建議回顧這項訓練最重要的概念。

# 更進一步

<partId>6bbf107d-a224-5916-9f0c-2b4d30dd0b17</partId>

## 訓練總結

<chapterId>a65a571c-561b-5e1c-87bf-494644653c22</chapterId>

:::video id=5f4f4344-ef27-4765-8f09-8262e6833bde:::

在標誌著 LNP201 訓練結束的最後一章中，我建議重溫我們一起涵蓋過的重要概念。

本訓練的目的是讓您對 Lightning Network 有全面的技術性了解。我們發現 Lightning Network 如何依賴 Bitcoin Blockchain 來執行 off-chain 交易，同時保留 Bitcoin 的基本特性，特別是不需要信任其他節點。

### 付款管道

在最初的章節中，我們探討了雙方如何透過開啟付款通道，在 Bitcoin Blockchain 以外進行交易。以下是所涵蓋的步驟：


- 通道開啟**：通道的建立透過 Bitcoin 交易完成，該交易將資金鎖定在 2/2 多重簽章 Address 中。此存款代表 Blockchain 上的 Lightning 通道。

![LNP201](assets/en/76.webp) 2. **Transactions in the Channel**: In this channel, it is then possible to carry out numerous transactions without having to publish them on the blockchain. Each Lightning transaction creates a new state of the channel reflected in a commitment transaction.

![LNP201](assets/en/77.webp)


- 安全與關閉**：參與者透過交換撤銷金鑰來承諾通道的新狀態，以確保資金安全並防止任何作弊行為。雙方可以透過在 Bitcoin Blockchain 上進行新的交易來合作關閉通道，或作為最後的手段透過強制關閉。後一種方式雖然效率較低，因為時間較長，有時在費用方面的評估也較差，但仍然可以追回資金。在作弊的情況下，受害者可以藉由收回 Blockchain 上通道的所有資金來懲罰作弊者。

![LNP201](assets/en/78.webp)

### 渠道網路

在研究了孤立的通道之後，我們將分析範圍擴大到通道網路：


- 路由**：當交易雙方沒有透過通道直接連線時，網路允許透過中介節點進行路由。付款會從一個節點轉移到另一個節點。

![LNP201](assets/en/79.webp)


- HTLCs**：透過中間節點傳輸的付款是以「_哈希時間鎖定合約_」(HTLC) 作為安全保障，它允許在完成端對端付款之前鎖定資金。

![LNP201](assets/en/80.webp)


- 洋蔥路由**：為了確保付款的機密性，洋蔥路由會將最終目的地遮蔽給中介節點。因此，發送節點必須計算整個路由，但在缺乏有關通道流動性的完整資訊的情況下，它會透過連續的測試來進行路由付款。

![LNP201](assets/en/81.webp)

### 流動資金管理

我們已經看到，流動資金管理是 Lightning 上的一項挑戰，以確保付款的順暢流通。發送付款相對簡單：只需要打開一個通道。但是，接收付款需要在通道的另一端擁有流動資金。以下是討論的一些策略：


- 吸引通道**：透過鼓勵其他節點朝自己開放通道，使用者可以獲得流入的流動資金。
- 移動流動性**：藉由將付款傳送至其他通路，流動資金就會移動到對方。

![LNP201](assets/en/82.webp)


- 使用 Loop 和 Pool** 等服務：這些服務允許重新平衡或購買對方具有流動性的通道。

![LNP201](assets/en/83.webp)


- 合作開倉**：也有一些平台可供連接進行三角開盤，並有流入的流動資金。

![LNP201](assets/en/84.webp)

# 總結

<partId>b8715c1c-7ae2-49b7-94c7-35bf85346ad3</partId>

## 評論與評分

<chapterId>38814c99-eb7b-5772-af49-4386ee2ce9b0</chapterId>

<isCourseReview>true</isCourseReview>
## 期末考試

<chapterId>7ed33400-aef7-5f3e-bfb1-7867e445d708</chapterId>

<isCourseExam>true</isCourseExam>
## 總結

<chapterId>afc0d72b-4fbc-5893-90b2-e27fb519ad02</chapterId>

<isCourseConclusion>true</isCourseConclusion>
