---
term: 标签（无声支付）

---
在静默支付协议中，标签是用来修改初始静态地址的整数，以便创建许多其他静态地址。使用这些标签可以对通过静默支付发送的付款进行隔离，每次使用时使用不同的静态地址，而不会过度增加检测这些付款（扫描）的操作负担。鲍勃使用由两个公钥组成的静态地址 $B$：$B_{\text{scan}}$ 用于扫描，$B_{\text{spend}}$ 用于消费。$B_{\text{scan}}$ 的哈希值和一个整数 $m$（由生成点 $G$ 进行标量乘法）被添加到消费公钥 $B_{\text{spend}}$ 中，以创建一种新的消费公钥 $B_m$：

$$ B_m = B_{text{spend}} + \text{hash}(b_{text{scan}} \text{ ‖ } m+ text{hash}(b_{text{scan}} \text{ ‖ } m) \cdot G $$

例如，第一个密钥 $B_1$ 就是这样得到的：

$$ B_1 = B_{text{spend}} + \text{hash}(B_{text{scan}} \text{ ‖ } 1+ text{hash}(b_{text{scan}} \text{ ‖ } 1) \cdot G $$

现在，Bob 发布的静态地址将由 $B_{text{scan}$ 和 $B_m$ 组成。例如，第一个标签为 $1$ 的静态地址将是

$$ B = B_{\text{scan}}\文本{ ‖ }B_1 $$

我们只从标签$1$开始，因为标签$0$是为变更保留的。爱丽丝希望向鲍勃提供的静态地址发送比特币，她将使用新的 $B_1$ 而不是 $B_{text/{spend}}$，得出唯一的支付地址 $P_0$：

$$ P_0 = B_1 + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$

实际上，爱丽丝可能根本不知道鲍勃有一个标签地址，因为她只是使用了他提供的静态地址的第二部分，在本例中是 $B_1$ 而不是 $B_{\text{spend}}$。为了扫描付款，Bob 将始终以这种方式使用其初始静态地址的值 $B_{text/{spend}}$：

$$ P_0 = B_{text{spend}}+ \text{hash}(\text{inputHash} \cdot b_{text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

然后，他只需从每个输出中逐个减去他找到的 $P_0$ 值。然后，他会检查这些减法的结果中是否有一个与他在钱包上使用的某个标签的值相匹配。如果匹配，例如标签为 $1$的输出 #4，这意味着该输出是与标签为 $B_1$ 的静态地址相关联的静默支付：

$$ Out_4 - P_0 = \text{hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$

这样做的原因是

$$ B_1 = B_{text{spend}} + \text{hash}(B_{text{scan}} \text{ ‖ } 1+ text{hash}(b_{text{scan}} \text{ ‖ } 1) \cdot G $$

通过这种方法，Bob 可以使用大量静态地址（$B_1$、$B_2$、$B_3$......），所有这些地址都来自于他的基本静态地址（$B = B_{text{scan}} \text{ ‖ } B_{text{spend}}$），以便正确区分用途。

然而，这种静态地址分离仅适用于个人钱包管理角度，却无法实现身份分离。由于它们都具有相同的 $B_{text/{scan}}$，因此很容易将所有静态地址联系在一起，并推断出它们属于同一个实体。