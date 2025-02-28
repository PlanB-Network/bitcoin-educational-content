---
name: Stonewall
description: 理解并使用Stonewall交易
---
![cover stonewall](assets/cover.webp)

***警告：** 继Samourai Wallet的创始人于4月24日被捕，其服务器被查封之后，现在使用Samourai Wallet应用需要连接到您自己的Dojo才能正常工作。除此之外，Stonewall交易完全不受影响，仍然可以毫无问题地执行。实际上，这些类型的交易是自主进行的，不需要外部合作或通过Soroban连接。*

_我们正在密切关注此案件以及相关工具的发展情况。请放心，一旦有新信息，我们将更新本教程。_

_本教程仅供教育和信息目的使用。我们不支持或鼓励使用这些工具进行犯罪活动。每个用户都有责任遵守他们所在司法管辖区的法律。_

---

> *"用数学上可证明的疑问打破区块链分析对交易发送者和接收者之间假设。"*

## 什么是Stonewall交易？
Stonewall交易是一种特定形式的比特币交易，旨在通过模仿两方之间的coinjoin来增加用户在交易中的隐私，但实际上并不是coinjoin。事实上，这种交易不是协作性的。用户可以单独构建它，只涉及他们自己的UTXOs作为输入。因此，您可以在任何场合创建Stonewall交易，而无需与另一个用户协调。

Stonewall交易的操作如下：作为输入，发送者使用属于他们的2个UTXOs。作为输出，交易产生4个输出，其中2个将是完全相同的金额。其他2个将是找零。在两个相同金额的输出中，只有一个实际上会去支付给收款人。

Stonewall交易中只有2个角色：
- 发送者，进行实际支付；
- 收款人，可能不知道交易的具体性质，只是期待来自发送者的支付。

让我们通过一个例子来理解这种交易结构。Alice在面包店买她的法棍面包，价格是`4,000 sats`。她想用比特币支付，同时保持她支付的一定隐私级别。因此，她决定为支付创建一个Stonewall交易。
![transaction stonewall bakery](assets/en/1.webp)
分析这笔交易，我们可以看到面包师确实收到了`4,000 sats`作为法棍面包的支付。Alice使用了2个UTXOs作为输入：一个是`10,000 sats`，另一个是`15,000 sats`。作为输出，她收到了3个UTXOs：一个是`4,000 sats`，一个是`6,000 sats`，还有一个是`11,000 sats`。在这笔交易中，Alice的净余额是`-4,000 sats`，这对应于法棍面包的价格。

在这个例子中，我故意省略了挖矿费用以便于理解。实际上，交易费用完全由发送者承担。

## Stonewall与Stonewall x2有什么区别？
Stonewall交易的操作方式与StonewallX2交易相同，唯一的区别在于后者需要合作，而经典的Stonewall交易则不需要，因此有了“x2”的称呼。实际上，Stonewall交易可以在不需要外部合作的情况下执行：发送者可以在没有其他人帮助的情况下完成它。然而，对于Stonewall x2交易，需要一个额外的参与者，称为“合作者”，加入这个过程。合作者将自己的比特币作为输入，与发送者的比特币一起，然后接收全部的输出金额（扣除挖矿费）。

让我们回顾一下Alice在面包店的例子。如果她想进行Stonewall x2交易，Alice就必须在创建交易时与Bob（第三方）合作。他们每个人都会提供一个输入UTXO。然后，Bob会收到他输入的全部金额作为输出。面包师会以与Stonewall交易相同的方式收到他的面包款项，而Alice会收到她的初始余额，扣除面包的成本。

从外部视角看，交易的模式将保持完全相同。

总之，Stonewall和Stonewall x2交易共享相同的结构。两者之间的区别在于它们的合作性质。Stonewall交易是单独开发的，不需要合作。相比之下，Stonewall x2交易依赖于两个个体之间的合作来实施。

[**-> 了解更多关于Stonewall x2交易的信息**](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)

## Stonewall交易的目的是什么？
Stonewall结构为交易增加了大量的熵，并且使链分析变得模糊。从外部视角看，这样的交易可以被解释为两个人之间的小型coinjoin。但实际上，就像Stonewall x2交易一样，它是一种支付方式。因此，这种方法在链分析中创建了不确定性，甚至可能导致错误的线索。

让我们再次回顾Alice在面包店的例子。区块链上的交易将如下所示：
一个依赖于常见链分析启发式的外部观察者可能错误地得出结论，认为“*两个人进行了一个小型coinjoin，每个人输入一个UTXO，每个人输出两个UTXO*”。
这种解释是不正确的，因为你知道，一个UTXO被发送给了面包师，输入中的2个UTXO来自Alice，她收到了3个找零输出。
即使外部观察者设法识别出Stonewall交易的模式，他们也不会拥有所有信息。他们将无法确定两个相同金额的UTXO中哪一个对应于支付。此外，他们也无法确定输入中的两个UTXO是来自两个不同的人，还是属于一个将它们合并的人。这最后一点是因为我们上面谈到的Stonewall x2交易，遵循与Stonewall交易完全相同的模式。从外部来看，如果没有关于上下文的额外信息，就不可能区分Stonewall交易和Stonewall x2交易。然而，前者不是合作交易，而后者是。这更增加了对这笔支出的疑问。![Stonewall还是Stonewall x2？](assets/en/3.webp)
## 如何在Samourai Wallet上进行Stonewall交易？
与Stowaway或Stonewall x2（共谋）交易不同，Stonewall交易不需要使用Paynyms。它可以直接进行，无需任何准备步骤。要做到这一点，请按照我们在Samourai Wallet上的视频教程操作：
![Stonewall教程 - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)

## 如何在Sparrow Wallet上进行Stonewall交易？
与Stowaway或Stonewall x2（共谋）交易不同，Stonewall交易不需要使用Paynyms。它可以直接进行，无需任何准备步骤。要做到这一点，请按照我们在Sparrow Wallet上的视频教程操作：
![Stonewall教程 - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)


**外部资源：**
- https://docs.samourai.io/en/spend-tools#stonewall.