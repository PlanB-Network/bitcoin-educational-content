---
name: JoinMarket

description: 如何使用 JoinMarket 通过命令行在 Bitcoin 上执行 CoinJoin 的指南和教程
---

![cover](assets/cover.webp)



---

如果你是在网上搜索 "JoinTmarket "而找到本页的，我向你表示衷心的感谢。不过，您偶然发现的这本指南涉及的是一个完全不同但又极其有趣的话题！🚬🍁



本教程旨在通过命令行说明 JoinMarket 的理论和实际操作。🐢 💚



## JoinMarket 理论定义



我们可以把 JoinMarket 定义为一种工具或 Wallet，它能够以完全 Trustless 的方式与其他用户进行 CoinJoin，而不需要任何中央协调者。



由于该工具的整个理论部分非常宽泛，我决定在播客中专门介绍 Address。对于那些能听懂意大利语的人，我强烈建议在听完这一集后继续阅读，以便更好地吸收正确使用该程序的基本概念。



您可以通过以下直接链接收看本期节目：




- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [谷歌播客](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) （在此您可以直接从浏览器收听）。
- [Antenna pod](https://antennapod.org/) 是一款免费开源的播客管理器，无需注册。要查找这一集，请下载该应用程序，在 _feed rss_ 部分粘贴 [this link](https://Anchor.fm/s/bd5d5b20/podcast/rss) 以手动添加我的播客，然后搜索专门介绍 JoinMarket 的这一集。



## 安装



操作系统





- 拉斯皮利茨
- 伞
- 我的节点
- Raspibolt



## 配置文件



JoinMarket 是個可自訂的軟件，有無限的設定；這些設定是在主程式目錄中名為「Joinmarket.cfg」的設定檔中指定的。



在本节中，我们将介绍一些您可能会感兴趣的字段，您可以根据自己的需要进行探索和/或修改。我想强调的是，以下列出的所有更改都是有用的，以便根据个人需要调整软件的操作，而不是强制性的。



首先，让我们移动到 `joinmarket/scripts` 文件夹并运行命令：



```bash
python wallet-tool.py generate
```


此时应该会出现错误，但这样做会导致软件为我们生成 generate 预设设置文件。我们可以在终端上编辑设置文件，方法如下



```bash
nano joinmarket.cfg
```



或



```bash
vim joinmarket.cfg
```



打开后，我们会发现许多行中有各种设置及其英文解释。下面我们将具体分析最有趣的变量：





- `merge_algorithm` (合并算法)，如果我们是制作者，这个字段将调整软件合并未用输出的积极程度。如果我们有很多 UTXOs 需要合并，将_gradual_（渐进）切换为_greedy_（贪婪）可能会更合理。
- tx_fees "用于调整支付交易的费用，如果您经常使用不倒翁（我们稍后会讨论），更改此设置非常有用，因为如果在执行不倒翁的过程中费用激增，如果我们没有正确设置此字段，就有可能为了 CoinJoin 而花费大量 Sats。通过设置以千为单位的值（如 2000），相当于 2 Sats/vBytes，3500 相当于 3.5 Sats/vBytes，以此类推。根据您的需求，我建议您使用 1500 到 6000 之间的数值。
- max_cj_fee_abs "用于指定我们愿意为在 CoinJoin 期间选择的制作人支付的绝对值。默认情况下，制造商的这一字段值为 200 Sats，一个好的选择可能是每个对等物 200 到 1000 Sats 不等（这取决于您想花多少钱，以及您为您的 CoinJoins 寻求多少额外设置）。
- max_cj_fee_rel "的功能与上述字段相同，但指定了我们愿意支付给每个对手方的相对费用（百分比）。由于这是一个 "百分比 "值，因此请注意不要设置过高的值，以避免大额 CoinJoins 产生过高的费用。制造商的默认值是 _0.00002_，我建议使用类似或稍高的值。
- `minimum_makers` 是指定与我们进行 CoinJoin 交易的其他对手数量的字段，默认情况下，joinMarket 总是从 4 到 9 个对手中进行选择，如果我们想要获得更多隐私，可以将该值提高到 5 或 6（不过，这会使交易成本更高）。
- cjfee_a "指定在我们作为制造者的情况下，我们租用流动性所要收取的 Sats 的绝对值。这个字段完全是主观的，默认值已经很不错了（作为做市商，我们会有更好的隐私），如果我们想在更短的时间内赚取更多的 CoinJoin，可以考虑将其设为 0。
- cjfee_r "与上述字段相同，但以百分比而非绝对值表示。我再次建议保留默认值或将其调低，以吸引更多投标者。
- 订单类型"（ordertype），在这个字段中，我们可以从制造商处选择是绝对出价（absoffer）还是百分比出价（reloffer）。通常，对于经济问题，出价者更倾向于绝对出价。
- `minsize` 如果作为制作者，我们不希望 UTXO 太小，我们可以指定参与的最小 CoinJoin。这个字段用 Satoshi 表示，完全是主观的。我们可以将该字段保留为 0 或增加到 500000 (Sats)、1000000 (Sats)，等等。



请务必小心，不要编辑错误的字段，joinmarket.cfg 文件中的某些变量如果设置错误，可能会危及软件的功能或完全破坏您的隐私，因此请睁大眼睛，谨慎行事！



## 工作环境设置



有些节点会自动在 joinmarket.cfg 文件中为这些字段设置正确的值，我建议手动重新检查：





- `rpc_user = yourusername-as-in-Bitcoin.conf` `rpc_user = yourusername-as-in-Bitcoin.conf
- rpc_password = yourpassword-as-in-Bitcoin.conf
- rpc_host = localhost #默认值通常是正确的
- `rpc_port = 8332 # Mainnet` 的默认值



此时，我们就可以在 JoinMarket 中创建 Wallet：



```bash
python wallet-tool.py generate
```



当命令询问是否支持保真债券时，我建议使用 _yes_ 选项，返回的输出结果将如下所示：



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


如果出现错误，很可能是我们错误地设置了上面指定的 4 个 RPC 字段。如果是这样，请参考 JoinMarket 文档中的 [this guide](https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure)。



我们已经完成了工作环境的设置，可以开始探索对我们最有用的命令了。我们将要讨论的所有脚本都可以在控制台中启动，然后点击"--help "以获得深入解释。



现在我们可以尝试发射了：



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



该命令将显示所有不同的 Wallet 混合深度和不同的地址分类：




- 全新（Address 从未使用过）
- 变更（先前交易的剩余部分）
- Cj-输出（CoinJoin 的输出）



下面是一个实际结果的例子：



```bash
JM wallet
mixdepth	0	xpub6CMAJ67vZWVXuzjzYXUoJgWrmuvFRiqiUG4dwoXNFmJtpTH3WgviANNxGyZYo27zxbMuqhDDym6fnBxmGaYoxr6LHgNDo1eEghkXHTX4Jnx
external addresses	m/84'/0'/0'/0	xpub6FFUn4AxdqFbnTH2fyPrkLreEkStNnMFb6R1PyAykZ4fzN3LzvkRB4VF8zWrks4WhJroMYeFbCcfeooEVM6n2YRy1EAYUvUxZe6JET6XYaW
m/84'/0'/0'/0/0     	bc1qt493axn3wl4gzjxvfg03vkacre0m6f2gzfhv5t	0.00000000	new
m/84'/0'/0'/0/1     	bc1q2av9emer8k2j567yzv6ey6muqkuew4nh4rl85q	0.00000000	new
m/84'/0'/0'/0/2     	bc1qggpg0q7cn4mpe98t29wte2rfn2rzjtn3zdmqye	0.00000000	new
m/84'/0'/0'/0/3     	bc1qnnkqz8vcdjan7ztcpr68tyec7dw2yk8gjnr9ze	0.00000000	new
m/84'/0'/0'/0/4     	bc1qud5s2ln88ktg83hkr6gv9s576zvt249qn2lepx	0.00000000	new
m/84'/0'/0'/0/5     	bc1qw0lhq7xlhj7ww2jdaknv23vcyhnz6qxg23uthy	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/0'/1
Balance:	0.00000000
Balance for mixdepth 0:	0.00000000
mixdepth	1	xpub6CMAJ67vZWVXyTJEaZndxZy9ACUufsmNuJwp9k5dHHKa22zQdsgALxXvMRFSwtvB8BRJzsd8h17pKqoAyHtkBrAoSqC9AUcXB1cPrSYATsZ
external addresses	m/84'/0'/1'/0	xpub6FNSLcHuGnoUbaiKgwXuKpfcbR63ybrjaqHCudrma13NDqMfKgBtZRiPZaHjSbCY3P3cgEEcdzZCwrLKXeT5jeuk8erdSmBuRgJJzfNnVjj
m/84'/0'/1'/0/0     	bc1qhrvm7kd9hxv3vxs8mw2arcrsl9w37a7d6ccwe4	0.00000000	new
m/84'/0'/1'/0/1     	bc1q0sccdfrsnjtgfytul5zulst46wxgahtcf44tcw	0.00000000	new
m/84'/0'/1'/0/2     	bc1qst6p8hr8yg280zcpvvkxahv42ecvdzq63t75su	0.00000000	new
m/84'/0'/1'/0/3     	bc1q0gkarwg8y3nc2mcusuaw9zsn3gvzwe8mp3ac9h	0.00000000	new
m/84'/0'/1'/0/4     	bc1qkf5wlcla2qlg5g5sym9gk6q4l4k5c98vvyj33u	0.00000000	new
m/84'/0'/1'/0/5     	bc1qz6zptlh3cqty2tqyspjk6ksqelnvrrrvmyqa5v	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/1'/1
Balance:	0.00000000
Balance for mixdepth 1:	0.00000000
mixdepth	2	xpub6CMAJ67vZWVY2cq5fmVxXw92fcgTchphGNFxweSiupYH1xYfjBiK6dj5wEEVAQeA4JcGDQGm2xcuz2UsMnDkzVmi2ESZ3xey63mQMY4x2w2
external addresses	m/84'/0'/2'/0	xpub6DqkbMG3tj2oixGYniEQTFamLCHTZx9CeAbUdBttiGuYwgfGZbrLMor8LWeJBUqTpsa81JcJqAUXuDxhXdLpKDxJAEqKMqPgJyXstj5dp3o
m/84'/0'/2'/0/0     	bc1qwtdgg928wma8jz32upkje7e4cegtef7yrv233l	0.00000000	new
m/84'/0'/2'/0/1     	bc1qhkuk2gny4gumrxcaw999uq3jm3fjrjvcwz7lz3	0.00000000	new
m/84'/0'/2'/0/2     	bc1qvu753lkltc8akfasclnq89tdv8yylu2alyg76y	0.00000000	new
m/84'/0'/2'/0/3     	bc1qal3r040k26cw2f08337huzcf00hrnws5rhfrz3	0.00000000	new
m/84'/0'/2'/0/4     	bc1qpv4nm7wwtxesgwsr0g0slxls33u0w02gqx2euk	0.00000000	new
m/84'/0'/2'/0/5     	bc1qk3ekjzlvw3uythw738z7nvwe2sg93w2rtuy6ml	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/2'/1
Balance:	0.00000000
Balance for mixdepth 2:	0.00000000
mixdepth	3	xpub6CMAJ67vZWVY3uty61M6jeGheGU5ni5mQmqMW2QLQbEa8ZQXuBw1K2umKFZsmU8EMEafJZKQkGS1trtWE5dtz4XmDbvLvUccAPn26ZC5i2o
external addresses	m/84'/0'/3'/0	xpub6EvT4QFPRdkt2sji3QdLLZjkJQmk7G2y3umT99ceomKTXGYvZ5S9TLaGos6cEugXEuxS6s9kvSUj1Xvpiu65dn5yzK7CgdZLzXawpKC9Mpe
m/84'/0'/3'/0/0     	bc1q9ph5l2gknjezcmzv84rnhu4df566jgputzef7l	0.00000000	new
m/84'/0'/3'/0/1     	bc1qrlvmmxfuryr3mfhssjv45h0fl6s43g3vzrkwca	0.00000000	new
m/84'/0'/3'/0/2     	bc1q40xkajgv9q42ve92zstwjc9v4jgauxme9su6uc	0.00000000	new
m/84'/0'/3'/0/3     	bc1q38pfk8yfnu97v4mckkuk2dhk9u8geuyzu9c0hc	0.00000000	new
m/84'/0'/3'/0/4     	bc1q2qzxyw56em9qdxc5z5s5xjz3j6s2qlzn3juvtu	0.00000000	new
m/84'/0'/3'/0/5     	bc1qd2f8f3dau5pfjqu7dpuvt6fahj36w4rgl3xevr	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/3'/1
Balance:	0.00000000
Balance for mixdepth 3:	0.00000000
mixdepth	4	xpub6CMAJ67vZWVY7gT4oJQBMc1fhbausT57yNVLCLCMwaGed5spHKaQY1EMQxvL2vTgDfhEimuAy7bzBE1qx5uY6D7cpUjQtXPHpyJzFuUtQPN
external addresses	m/84'/0'/4'/0	xpub6EQWpKsBTG3N9TFU4v6WtCcBJuLAeTZTcUwVJTxYUAsHeVPFdey4qT1dg4G7MqvnFFgHZDxqTo37S81UWUA2BqKKoTff1pcHTcSFzxyp5JG
m/84'/0'/4'/0/0     	bc1qdpjh3ewm367jm5eazqdf8wfrm09py50wn47urs	0.00000000	new
m/84'/0'/4'/0/1     	bc1q2x0fmtms5nr3wz3x3660c8wampg7t22e6m30t8	0.00000000	new
m/84'/0'/4'/0/2     	bc1q23595yg3dkj8gd3jrgup0hyzslhzf9skrg50r5	0.00000000	new
m/84'/0'/4'/0/3     	bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl	0.00000000	new
m/84'/0'/4'/0/4     	bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes	0.00000000	new
m/84'/0'/4'/0/5     	bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/4'/1
Balance:	0.00000000
Balance for mixdepth 4:	0.00000000
Total balance:	0.00000000
```


现在，我们可以在一个或多个地址中存入我们的第一个 Satoshis，记住，无论制作者或接收者是谁，软件都不会直接将 UTXO 合并到不同的混合深度中，这样我们就可以在 Wallet 中保留不同隐私级别的 Satoshis。



## 将 Bitcoin 与 CoinJoin 单机一起发送



现在我们可以移动 Satoshis 了。该软件的主要命令之一是脚本：



```bash
pyhton sendpayment.py
```


这将使我们能够在有或没有 CoinJoin 的情况下向其他地址发送交易。下面我们来看看它的工作原理和一些实际例子。默认情况下，该命令的格式为（请记住用符号 < 和 > 替换括起来的文本）：



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



一个基本的使用示例可能是



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


在这种情况下，我们将通过为 CoinJoin 选择 4 到 9 个对应方（默认选项），从混合深度 0（默认深度）向 Address 发送 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0.05 Btc，即 5000000 Satoshi。



要进一步控制如何使用UTXO以及使用哪些UTXO，我们可以查看该命令的附加选项：



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


在本例中，我们增加了两个规格： -N 表示我们要与多少个对手方混合，-m 表示我们要从中提取资金的混合深度。事实上，我们向 Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 发送了 100,000,000 Sats（1 btc），资金在混合深度 1 中，与 5 个对手方混合。



如果我们指定一个混合深度，将发送值设为 0，joinMarket 就会执行所谓的 "清扫"，即把该混合深度内的所有资金合并在一起发送：



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



在这里，我们将混合深度为 0 的所有资金（我们可以不指定，因为这是默认值）与 7 个对应方混合。



sendpayment 命令用于将资金从 joinMarket 转移到外部 Wallet 或通过在我们与某人之间添加 Layer 隐私来向其发送 Satoshi。要在我们的UTXO上获得足够的隐私，使用tumbler.py命令更为合适，我们将在本指南的稍后部分进行说明。



## 做一个制造者



本节要介绍的脚本是



```bash
yg-privacyenhanced.py
```



该程序用于在 joinMarket 中充当做市商。该软件将连接到我们的 Bitcoin 节点和平台的内部市场，在该市场中，做市商作为流动性投标人展示自己，而做市商则寻找交易对手。如果您想使用保真债券，可以使用此格式创建一个：



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



例如



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



返回给我们的输出将是 Bitcoin Address（即您需要存入您要分配给 Fidelity 的资金的输出）。



**注意**：如果您要创建保真债券（又称 FB），有两点需要密切注意；





- 资金一旦存入，在过期之前就不能再移动。注意向 Address 发送的 Satss 数量和日期格式。不允许出现错误！
- 保真债券在链上很容易识别，因此建议通过 CoinJoin 和与您身份无关的来源存入资金。一旦你想将过期的保真债券移出 JoinMarket，也应该这样做。



重要的是要记住，只需一次交易即可重新充值保真债券，如果是 UTXO 多次交易，则只有最大的一次交易才被视为有效的 FB。



现在让我们来处理本段开头提到的脚本，一旦我们创建了保真债券（我们记得这是可选的），我们就可以运行可执行文件，在 joinMarket 上充当做市商了。将 Sats 存入不同的地址和混合深度后，我们就可以运行命令了：



```bash
python yg-privacyenhanced.py <wallet name>
```



从这时起（连接到网络几分钟后），直到我们停止脚本，我们的 JoinMarket 客户端将出现在协议上的活跃做市商列表中，并向不同的交易对手提供我们的流动性，以进行 CoinJoin。不要指望每天会有几十个 CoinJoins（除非您在 Wallet 上有大量的闲置资金和流动资金），还要记住，所需费用和存入的 Satoshis 等因素会影响您成为做市商的频率。



运行下面的命令，您就可以查看 Wallet 上所有交易的历史记录，以及在 Wallet 使用期间的收益（如果您是制造者）或费用支出（如果您是接受者）。



```bash
python wallet-tool.py <wallet name> history
```



一旦你的 Satoshis 进行了 CoinJoins，它们就会从一个混合深度移动到另一个混合深度，直到到达最后一个混合深度。在将它们转移到 Cold Wallet 之前，您可以自行决定要获得多少隐私，建议您完成一个完整的 Wallet 循环。



## 不倒翁



我们终于来到 JoinMarket 最精彩的部分，不倒翁！如果您听过播客，就已经知道这是怎么回事了。在我们开始之前，有一个建议： **当心费用！** 记得在 joinmarket.cfg 文件中设置限制（如开头所解释的），并考虑只在链上费用相对较低时（低于 10 Sats/vB）运行程序。



要启动不倒翁，必须先停止脚本的运行（如果脚本处于激活状态），然后才能运行命令：



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



必须为滚揉机输入 ** 至少 ** 3 个输出地址：这是为了确保良好的私密性，并且在整个过程中不会在UTXO之间产生明显的链接。像往常一样，在命令中添加"--help"，就可以查看所有其他细节。让我们来看一个更复杂的带有高级规则的示例：



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



在这种情况下，我们启动了一个翻滚脚本，该脚本将不使用默认的对应物数量（-N 参数表示我们需要 7 个对应物，最大方差为 2，因此制作者的随机数量为 5 到 9），并且每个混合深度的 CoinJoin 数量更大（默认情况下，该脚本为 Wallet 的每个部分制作随机数量为 1 到 3 的 CoinJoin，使用 -c 3 1 命令则为 2 到 4）。这样，我们将花费更多的 Sats 费用，但匿名集却更大。



您还可以添加任意数量的输出地址（最少 3 个，除常识外没有最大值）。但是，出于隐私考虑，无法决定 Satoshi 如何在指定的输出地址中分配。



Tumbler 是一个特意设计的冗长程序，偶尔可能会出现某些功能停止工作的情况，但在大多数情况下，这种情况会在几小时内自行解决。如果出现完全崩溃，我们可以尝试用命令重新启动：



```bash
python tumbler.py --restart
```



或者只需重新启动一个新的翻滚指令。这不会启动前一个滚揉机的调度，但会启动一个新的混合周期。如果关闭节点的 SSH 终端也会停止脚本，你可以利用该命令安装的 `TMUX` 程序：



```bash
sudo apt install tmux
```



在 shell 中键入 `tmux` 启动它，将为您打开一个终端，即使您关闭了远程连接，该终端也会在后台保持激活状态。当你使用 `tmux attach` 命令重新连接到你的节点时，你将重新打开终端：attach` 命令重新连接节点时，将重新打开在后台保持激活状态的 shell。



## 结论



JoinMarket 是一個無限的、可自訂的軟件。在這份指南中，我們發現了它的主要功能，讓任何人都可以使用它（至少我已經嘗試過，我知道使用這個軟體並不是一件容易的事）。JoinMarket 最大的問題之一就是：使用它的人數和成為製造商的人數。如果只有少数用户利用这个软件，那么整体的隐私（anon-set）就会降低。这就是为什么我希望本指南能激励使用，并说服你下载和安装我最喜欢的软件来制作 CoinJoin。如果你想更深入地了解某些方面，我建议你阅读 github 上的各种深度文档，它们做得非常好，你可以在这里找到。



搅拌乌龟快乐！🐢 💚



[Here](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) 您可以支持 Turtlecute