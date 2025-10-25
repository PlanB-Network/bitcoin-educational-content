---
name: Boltzmann Calculator
description: 瞭解熵的概念以及如何使用 Boltzmann
---
![cover](assets/cover.webp)


**繼 Samourai Wallet 的創始人於 4 月 24 日被捕並其伺服器被查封之後，KYCP.org 網站目前無法存取。寄存 Python Boltzmann Calculator 程式碼的 Gitlab 也被查封。目前已無法下載此工具。不過，在未來幾週內，有可能會有其他人重新發表程式碼。在此期間，您仍可利用本教學瞭解 Boltzmann 計算機的運作。此工具提供的指標適用於任何 Bitcoin 交易，也可以手動計算。我將在本教程中提供所有必要的計算方法。如果您已經在您的機器上下載了 Python 工具，或者您使用的是 RoninDojo，您可以繼續使用該工具，並像往常一樣跟隨本教程，它仍然有效。**


我們正密切注意此案例的發展，以及相關工具的發展。請放心，我們會在有新資訊時更新本教學。


本教學僅為教育和資訊目的而提供。我們不贊同或鼓勵將這些工具用於犯罪目的。每位使用者都有責任遵守其司法管轄區的法律。


---

Boltzmann Calculator 是一種工具，可透過測量 Bitcoin 交易的熵水平以及其他先進的指標來分析 Bitcoin 交易。它可讓您深入瞭解交易的輸入和輸出之間的關係。這些指標可提供交易隱私權的量化評估，並有助於識別潛在錯誤。


這個 Python 工具是由 Samourai Wallet 和 OXT 的團隊所開發，但它可以用在任何 Bitcoin 交易上。


## 如何使用 Boltzmann 計算機？

要使用 Boltzmann 計算機，您有兩個選擇。第一種是直接在您的機器上安裝 Python 工具。另外，您也可以選擇 KYCP.org (_Know Your Coin Privacy_) 網站，它提供了一個簡化的使用平台。對 RoninDojo 使用者而言，請注意此工具已整合至您的節點中。


使用 KYCP 網站相當容易：只要在搜尋列中輸入您想要分析的交易識別碼 (txid)，然後按下「ENTER」即可。

![KYCP](assets/1.webp)

然後，您會發現有關交易的不同資訊，包括輸入和輸出之間的連結。按一下「決定性連結」。

![KYCP](assets/2.webp)

您將到達 Boltzmann 計算機指標專用頁面。

![KYCP](assets/3.webp)

若要直接從 RoninDojo 節點使用該工具，可透過 `RoninCLI > Samourai Toolkit > Boltzmann Calculator` 進行存取。


與 KYCP.org 網站一樣，安裝 Python 工具後，您只需貼上想要分析的交易的 txid。


![KYCP](assets/7.webp)


然後，按下 `ENTER` 鍵獲得結果。


![KYCP](assets/8.webp)


## Boltzmann 計算機的指標是什麼？

### 組合 / 詮釋：

軟體計算的第一個指標是可能組合的總數，在工具中的 `nb combinations` 或 `interpretations` 下顯示。


考慮到交易中涉及的 UTXOs 的值，這個指標計算出輸入與輸出相關聯的方式的數量。換句話說，它決定了從分析交易的外部觀察者的角度來看，交易可以引發的合理詮釋的數量。

例如，根據 Whirlpool 5x5 模型結構的 CoinJoin 顯示了`1,496`可能的組合： ![KYCP](assets/4.webp)

另一方面，一個 Whirlpool 突波週期 8x8 CoinJoin，提出了`9,934,563`可能的解釋： ![KYCP](assets/5.webp)

相比之下，具有 1 個輸入和 2 個輸出的較傳統交易只會呈現單一解釋： ![KYCP](assets/6.webp)


### 熵：

計算的第二個指標是交易的熵，以 `Entropy` 表示。


在密碼學和資訊的一般情況下，熵是一種量度與資料來源或隨機過程相關的不確定性或不可預測性的定量方法。換句話說，熵是量度資訊是否難以預測或猜測的一種方式。


在鏈式分析的特定情況下，熵也是一個指標的名稱，源自香儂熵和 [由 LaurentMT 發明](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)，它是用 Boltzmann 工具計算出來的。


當一筆交易有許多可能的組合時，參考它的熵通常更有意义。這個指標可以測量分析師對交易的確切配置缺乏了解的程度。換句話說，熵值越高，分析師識別輸入和輸出之間 Bitcoin 移動的任務就越困難。


在實務中，熵顯示了從外部觀察者的角度來看，交易是否僅基於輸入和輸出的數量，而不考慮其他外部或內部模式和啟發式方法，就能提出多種可能的詮釋。因此，高熵等同於交易有更好的保密性。


Entropy 定義為可能組合數的二進位對數。以下是使用的公式：

```plaintext
E: the entropy of the transaction
C: the number of possible combinations for the transaction

E = log2(C)
```


在數學中，二進位對數 (base-2 logarithm) 對應於指數化 2 的逆運算。換句話說，`x` 的二進位對數是為了得到`x` 而必須將`2` 提升到的指數。因此，這個指標是以位數來表示的。


讓我們以計算根據 Whirlpool 5x5 模型結構的 CoinJoin 交易的熵為例，如前所述，它提供的可能組合數為 `1,496`：

```plaintext
C = 1,496
E = log2(1,496)
E = 10.5469 bits
```

因此，這筆 CoinJoin 交易的熵值為 10.5469 位元，非常令人滿意。此值越高，交易可接受的不同解釋就越多，從而加強其隱私等級。

對於呈現 `9,934,563` 詮釋的 8x8 CoinJoin 交易，熵將為：

```plaintext
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bits
```


讓我們以另一個較傳統的交易為例，它有一個輸入和兩個輸出：[1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://Mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) 對於這個交易，唯一可能的解釋是：`(In.0) > (Out.0 ; Out.1)`。因此，它的熵為 `0`：

```plaintext
C = 1
E = log2(1)
E = 0 bits
```


### 效率：

Boltzmann 計算機提供的第三個指標名為「Wallet 效率」。該指標通過與相同配置下的最佳交易進行比較來評估交易效率。


這引導我們討論最大熵的概念，它對應於特定交易結構理論上可以達到的最高熵。然後，將這個最大熵與所分析交易的實際熵相對照來計算交易的效率。


使用的公式如下：

```plaintext
ER: the actual entropy of the transaction expressed in bits
EM: the maximum possible entropy for a given transaction structure expressed in bits
Ef: the efficiency of the transaction in bits

Ef = ER - EM
```


例如，對於 Whirlpool 5x5 型 CoinJoin 結構，最大熵設定為 `10.5469`：

```plaintext
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bits
```


此指標也以百分比表示，其計算公式如下：

```plaintext
CR: the actual number of possible combinations
CM: the maximum number of possible combinations with the same structure
Ef: the efficiency expressed as a percentage

Ef = CR / CM
Ef = 1,496 / 1,496
Ef = 100%
```


因此，「100%」的效率表示交易根據其結構最大化其隱私的潛力。


### 熵密度：

第四個指標是熵密度，在工具「熵密度」中指出。它提供了相對於交易的每個輸入或輸出的熵的角度。這個指標有助於評估和比較不同規模的交易效率。要計算它，只要將交易的總熵除以所涉及的輸入和輸出總數即可：

```plaintext
ED: the entropy density expressed in bits
E: the entropy of the transaction expressed in bits
T: the total number of inputs and outputs in the transaction

ED = E / T
```


讓我們以 Whirlpool 5x5 CoinJoin 為例：

```plaintext
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bits
```


我們也來計算一下 Whirlpool 8x8 CoinJoin 的熵密度：

```plaintext
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bits
```


### Boltzmann Score：

Boltzmann 計算機提供的第五項資訊是輸入和輸出之間的匹配概率表。這個表格透過 Boltzmann 分數顯示特定輸入與特定輸出相關的條件概率。


因此，它是交易中輸入和輸出之間發生關聯的條件概率的定量測量，其基礎是在一組詮釋中，此事件的有利發生次數與可能發生的總次數的比率。


再以 Whirlpool CoinJoin 為例，條件概率表會強調每項輸入和輸出之間的連結機會，提供交易中關聯模糊性的量化量測：


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
| ------- | -------- | -------- | -------- | -------- | -------- |
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

在這裡，我們可以清楚地看到，每個輸入都有同等的機會與任何輸出產生關聯，這就提高了交易的機密性。

計算 Boltzmann 分數的方法是將發生特定事件的詮釋數目除以可用詮釋的總數。因此，要確定輸入 0 與輸出 3（`512` 種解釋）相關的分數，必須使用下列程序：

```plaintext
Interpretations (IN.0 > OUT.3) = 512
Total Interpretations = 1496
Score = 512 / 1496 = 34%
```


以 Whirlpool 8x8 CoinJoin (突波循環) 為例，Boltzmann 表如下：


|       | OUT.0 | OUT.1 | OUT.2 | OUT.3 | OUT.4 | OUT.5 | OUT.6 | OUT.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| IN.0  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.1  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.2  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.3  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |

但是，如果是只有單一輸入和兩個輸出的簡單交易，情況就不同了：


| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

在這裡，我們可以觀察到每個輸出源自 0 號輸入的概率是 `100%`。因此，較低的機率會淡化輸入和輸出之間的直接關聯，從而轉化為更大的隱私。


### 確定連結：

提供的第六項資訊是確定性連結的數量，並輔以這些連結的比率。這個指標揭示了在所分析的交易中，有多少輸入和輸出之間的連結是不容置疑的，其概率為「100%」。另一方面，比率提供了一個角度，顯示這些確定性連結在整組交易連結中的比重。

例如，Whirlpool 類型的 CoinJoin 交易沒有確定的連結，因此顯示一個指標和`0%`的比率。相反地，在我們檢驗的第二個簡單交易（有一個輸入和兩個輸出）中，指標設定為「2」，比率達到「100%」。因此，由於輸入和輸出之間沒有直接和不容置疑的聯繫，指標為空表示保密性極佳。


**外部資源：**



- Samourai 上的 Boltzmann 代碼
- [Bitcoin 交易與隱私權 (Part I) by Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Bitcoin 交易與隱私權 (第二部分) by Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Bitcoin Transactions & Privacy (Part III) by Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- KYCP 網站
- [Medium文章：Laurent MT的Boltzmann腳本簡介](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)