---
term: 適配器簽名
---

結合真實簽章與附加簽章（稱為「適配簽章」）以揭示秘密資料的加密方法。此方法的運作方式是，只要知道有效簽章、適配簽章和密碼中的兩個 Elements，就可以推斷出缺失的第三個元素。這個方法其中一個有趣的特性是，如果我們知道對方的適配器簽章，以及橢圓曲線上與用來計算這個適配器簽章的秘密相連的特定點，我們就可以推導出我們自己的適配器簽章，與相同的秘密相匹配，而無需直接取得秘密本身。在兩個互不信任的利害關係人之間的 Exchange 中，這項技術允許同時揭露參與者之間的兩項敏感資訊。這個過程消除了瞬間交易（如 Coin Swap 或 Atomic Swap）中對信任的需求。讓我們舉一個例子來更好地理解它。Alice 和 Bob 想互相發送 1 BTC，但他們不信任對方。因此，他們將使用適配器簽名來消除對方在此 Exchange 中的信任需求（從而使其成為 「原子 」Exchange）。他們的步驟如下：


- Alice 發起這個原子 Exchange。她創建了一個交易 $m_A$，向 Bob 發送 1 BTC。她使用她的私人金鑰 $p_A$ ($P_A = p_A \cdot G$) 並使用 Nonce $n_A$ 和秘密 $t$ ($N_A = n_A \cdot G$ 和 $T = t \cdot G$) 創建一個簽章 $s_A$，以驗證此交易：

$$s_A = n_A + t + H(N_A + T \parallel P_A \parallel m_A) \cdot p_A$$



- Alice 根據秘密 $t$ 和她的真實簽名 $s_A$ 計算出適應者簽名 $s_A'$：

$$s_A' = s_A - t$$



- Alice 送給 Bob 她的適配器簽章 $s_A'$、她未簽署的交易 $m_A$、與密碼 $T$ 對應的點及與 Nonce $N_A$ 對應的點資料。我們稱這些資訊為「適配器」。請注意，僅憑這些資訊，Bob 無法恢復 Alice 的 BTC。
- 然而，Bob 可以驗證 Alice 沒有欺騙他。為此，他會檢查Alice的適配器簽章$s_A'$是否與承諾的交易$m_A$相符。如果下面的等式是正確的，那麼他相信 Alice 的適配器簽章是有效的：

$$s_A' \cdot G = N_A + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$



- 此驗證提供 Bob 來自 Alice 的保證，讓他可以安心地繼續原子交換程序。然後，他將創建自己的交易 $m_B$，向 Alice 送出 1 BTC 和他自己的適配器簽章 $s_B'$，該簽章將與暫時只有 Alice 知道的相同秘密 $t$ 相連（Bob 不知道此值 $t$，而只知道 Alice 提供給他的相應點 $T$）：$$s_B' = n_B + H(N_B + T \parallel P_B \parallel m_B) \cdot p_B$$



- 鮑勃將他的適配器簽章 $s_B'$、他未簽署的交易 $m_B$、與密碼 $T$ 對應的點及與 Nonce $N_B$ 對應的點傳送給愛麗絲。Alice現在可以結合Bob的適配器簽章$s_B'$和只有她知道的秘密$t$，計算出有效簽章$s_B$的交易$m_B$，向她發送Bob的BTC：

$$s_B = s_B' + t$$


$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \parallel P_B \parallel m_B) \cdot P_B$$



- Alice 在 Bitcoin Blockchain 上廣播這個已簽署的交易 $m_B$，以收回 Bob 允諾給她的 BTC。Bob 在 Blockchain 上得知此交易。因此，他能夠擷取簽章 $s_B = s_B' + t$。從這些資訊中，Bob 可以分離出他所需要的著名秘密 $t$：

$$t = (s_B' + t) - s_B' = s_B - s_B'$$



- 然而，這個秘密 $t$ 是 Bob 從 Alice 的適配器簽章 $s_A'$ 生成有效簽章 $s_A$ 的唯一缺失資訊，這將允許他驗證從 Alice 向 Bob 發送 BTC 的交易 $m_A$。然後，他依次計算 $s_A$ 並廣播交易 $m_A$： $$s_A = s_A' + t$$


$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \parallel P_A \parallel m_A) \cdot P_A$$