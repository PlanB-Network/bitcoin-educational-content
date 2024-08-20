---
term: LABEL (SILENT PAYMENTS)
---

在Silent Payments协议中，标签是用于修改初始静态地址以创建许多其他静态地址的整数。这些标签的使用允许通过为每个用途使用不同的静态地址，而不会过度增加检测这些支付（扫描）的操作负担，来对通过Silent Payments发送的支付进行隔离。Bob使用一个由两个公钥组成的静态地址$B$：用于扫描的$B_{\text{scan}}$和用于支出的$B_{\text{spend}}$。将$b_{\text{scan}}$的哈希值和一个整数$m$，通过生成点$G$进行标量乘法后，加到支出公钥$B_{\text{spend}}$上，以此创建一种新的支出公钥$B_m$：

$$  B_m = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G  $$

例如，第一个密钥$B_1$就是以这种方式获得的：

$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$

Bob发布的静态地址现在将由$B_{\text{scan}}$和$B_m$组成。例如，带有标签$1$的第一个静态地址将是：

$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$

我们只从标签$1$开始，因为标签$0$是保留给找零的。Alice，希望向Bob提供的带标签的静态地址发送比特币，将使用新的$B_1$而不是$B_{\text{spend}}$来派生唯一的支付地址$P_0$：

$$  P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

实际上，Alice可能甚至不知道Bob有一个带标签的地址，因为她只是使用他提供的静态地址的第二部分，这种情况下是值$B_1$而不是$B_{\text{spend}}$。为了扫描支付，Bob将始终以这种方式使用他的初始静态地址的值$B_{\text{spend}}$：

$$   P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$

然后，他将简单地从每个输出中逐一减去他找到的$P_0$的值。然后，他检查这些减法的结果之一是否与他在钱包上使用的标签的值匹配。如果匹配，例如，对于带有标签$1$的输出#4，这意味着这个输出是与他的带标签的静态地址$B_1$相关联的Silent Payment：
$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

这是因为：
$$  B_1 = B_{\text{spend}} + \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G  $$
得益于这种方法，Bob可以使用多个静态地址（如 $B_1$, $B_2$, $B_3$...），这些地址都是从他的基础静态地址（$B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$）派生出来的，以便于合理分隔使用。

然而，这种静态地址的分隔仅从个人钱包管理的角度有效，但不允许分隔身份。由于它们都有相同的 $B_{\text{scan}}$，很容易将所有静态地址关联起来，并推断它们属于单一实体。