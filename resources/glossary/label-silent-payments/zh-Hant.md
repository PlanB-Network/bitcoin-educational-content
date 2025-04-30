---
term: 標籤
---

在 Silent Payments 協議中，標籤是用來修改初始靜態 Address 的整數，以便創建許多其他靜態地址。這些標籤的使用允許透過無聲支付發送的付款進行分隔，每次使用都使用不同的靜態地址，而不會過度增加檢測這些付款（掃描）的操作負擔。Bob 使用靜態 Address $B$，由兩個公開金鑰組成：$B_{\text{scan}}$ 用於掃描，$B_{\text{spend}}$ 用於支出。$B_{\text{scan}}$的Hash和一個整數$m$，經標量乘以產生點$G$，被添加到花費公開密鑰$B_{\text{spend}}$，以創建一種新的花費公開密鑰$B_m$：


$$ B_m = B_{text{spend}}+ text{Hash}(b_{text{scan}} \text{ ‖ } m) \cdot G $$


例如，第一個金鑰 $B_1$ 是以這種方式獲得的：


$$ B_1 = B_{text{spend}}+ text{Hash}(b_{text{scan}} \text{ ‖ } 1) \cdot G $$


Bob 發佈的靜態 Address 現在將由 $B_{text{scan}$ 和 $B_m$ 組成。例如，第一個標籤為 $1$ 的靜態 Address 將為：


$$ B = B_{\text{scan}}\text{ ‖ }B_1 $$


我們只從標籤 $1$ 開始，因為標籤 $0$ 是預留給變更的。Alice 希望發送比特幣到 Bob 提供的標籤靜態 Address，將使用新的 $B_1$ 取代 $B_{text{spend}}$，得出唯一的付款 Address $P_0$：


$$ P_0 = B_1 + \text{Hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$


實際上，Alice 甚至可能不知道 Bob 有一個已標籤的 Address，因為她只是使用他提供的靜態 Address 的第二部分，在此情況下是值 $B_1$，而不是 $B_{text{spend}}$。為了掃描付款，Bob 將始終以這種方式使用其初始靜態 Address 的值 $B_{text/{spend}}$：


$$ P_0 = B_{text{spend}}+ \text{Hash}(\text{inputHash} \cdot b_{text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

然後，他只需從每個輸出逐一減去他找到的 $P_0$ 值。然後，他會檢查這些減法的結果之一是否與他在 Wallet 上使用的標籤之一的值相符。如果符合，例如標籤為 $1$ 的輸出 #4，這表示此輸出是與他的標籤為 $B_1$ 的靜態 Address 相關的 Silent Payment：

$$ Out_4 - P_0 = \text{Hash}(b_{text{scan}} \text{ ‖ } 1) \cdot G $$


這樣做是可行的，因為


$$ B_1 = B_{text{spend}}+ text{Hash}(b_{text{scan}} \text{ ‖ } 1) \cdot G $$


有了這個方法，Bob 可以使用許多靜態位址 (有 $B_1$、$B_2$、$B_3$...)，這些位址都來自他的基本靜態 Address ($B = B_{text{scan}} \text{ ‖ } B_{\text{spend}}$)，以便適當地區分用途。


然而，從個人 Wallet 管理的角度來看，這種分離靜態位址的做法只有效，卻無法分離身分。由於它們都有相同的 $B_{text/{scan}}$，因此很容易將所有的靜態位址聯繫在一起，並推斷出它們屬於單一個實體。