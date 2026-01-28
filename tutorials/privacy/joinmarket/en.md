---
name: JoinMarket

description: Guide and tutorial on how to use JoinMarket to do CoinJoin over Bitcoin via command line
---

![cover](assets/cover.webp)


---

If you found this page by searching online for "JoinTmarket" you have my sincere appreciation. You have, however, stumbled upon a guide that deals with a completely different, but extremely interesting topic! 🚬🍁


The objective of this tutorial is to illustrate the theoretical and practical operation of JoinMarket, through the command line. 🐢 💚


## JoinMarket Theoretical Definition


We can define JoinMarket as a tool, or a Wallet, that enables CoinJoin with other users in a totally Trustless manner and without any central coordinator.


Since the whole theoretical part of this tool is extremely broad, I decided to address it in a specific episode of my podcast. For those who can understand Italian, I highly recommend continuing reading after listening to the episode, so as to better assimilate the basic concepts for using this program properly.


You can catch up with the episode at these direct links:


- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Google podcast](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (here you can listen to it directly from browser).
- [Antenna pod](https://antennapod.org/) is a free and opensource podcast manager that does not require registration. To find the episode download the app, manually add my podcast by pasting [this link](https://Anchor.fm/s/bd5d5b20/podcast/rss) in the _feed rss_ section, then search for the episode dedicated to JoinMarket.


## Installation


Operating systems:



- Raspiblitz
- Umbrel
- MyNode
- Raspibolt


## Configuration Files


JoinMarket is a customizable software with an infinite number of settings; these settings are specified in a configuration file located in the main program directory called `Joinmarket.cfg`.


In this section we are going to go over some fields that you may find interesting to explore and/or modify, depending on your needs. I would like to emphasize that all the changes listed below are useful to know in order to adapt the operation of the software to personal needs while not being mandatory.


First let's move to the `joinmarket/scripts` folder and run the command:


```bash
python wallet-tool.py generate
```

At this point we should get an error, but doing so will cause the software to generate a pre-set settings file for us. We can go and edit the settings file from the terminal with:


```bash
nano joinmarket.cfg
```


or:


```bash
vim joinmarket.cfg
```


once opened we will notice numerous lines with various settings and their explanation in English. Specifically we will analyze below the most interesting variables:



- `merge_algorithm` in case we do as a maker this field adjusts how aggressively the software will consolidate unspent Outputs. In case we have many UTXOs to consolidate, it might make sense to switch from _gradual_ to _greedy_
- `tx_fees` adjusts as a taker the fees with which to pay the transaction, it is very useful to change this setting in case you use the tumbler often (we will talk about this later) because if there is a spike in the fees during the execution of the latter, if we do not set this field correctly, we risk going to spend a lot of Sats for CoinJoin. By setting values in thousands (such as 2000) this will equate to 2 Sats/vBytes, 3500 to 3.5 Sats/vBytes, and so on. I would recommend a number ranging from 1500 to 6000 depending on your needs.
- `max_cj_fee_abs` is used to specify how much we are willing to pay in absolute terms for the makers we choose during CoinJoin. By default this field for makers is 200 Sats, a good option might be a number ranging from 200 to 1000 Sats per counterpart (this is based on how much you want to spend and how much anon-set you seek for your CoinJoins)
- `max_cj_fee_rel` has the same function as the field above but specifies the relative fees (percentages) we are willing to pay to each counterparty. Since this is a `percentage` value, be careful not to set high values to avoid high costs in CoinJoins with large amounts. The default value for makers is _0.00002_, I recommend a similar or slightly higher value.
- `minimum_makers` is the field that specifies how many other counterparties we do CoinJoin with, by default joinMarket always chooses from 4 to 9 counterparties, if we want, for more privacy, we can raise this value to 5 or 6 (it will make the transactions more expensive though).
- `cjfee_a` specifies, in case we act as a maker, how many Sats in absolute terms we want to collect for renting our liquidity. This field is totally subjective, the default value is already very good (we will thus have better privacy as a maker) we can consider taking it to 0 if we want to make more CoinJoin in less time.
- `cjfee_r` same as above field but in percentage terms and not absolute. Again I recommend leaving the default value or lowering it to attract more takers.
- `ordertype` with this field we choose from maker whether to charge absolutely (absoffer) or percentage (reloffer). Usually takers prefer absolute bids for economic issues.
- `minsize` if as a maker we do not want to have UTXO too small we can specify the minimum CoinJoin to participate. This field is expressed in Satoshi and is totally subjective. We could leave this field at 0 or increase to 500000 (Sats), 1000000 (Sats), and so on.


Be very careful not to edit the wrong fields, some of the varibles in the joinmarket.cfg file if set incorrectly could compromise the functionality of the software or completely annihilate your privacy, eyes open and caution to the max!


## Work Environment Setup


Some nodes automatically set the correct values for these fields within the joinmarket.cfg file I recommend rechecking manually:



- `rpc_user = yourusername-as-in-Bitcoin.conf`
- `rpc_password = yourpassword-as-in-Bitcoin.conf`
- `rpc_host = localhost #default usually correct`
- `rpc_port = 8332 # default for Mainnet`


At this point we can proceed with the creation of our Wallet within JoinMarket:


```bash
python wallet-tool.py generate
```


This command will have us enter a password with which to encrypt the Wallet and the name we want to give it, when it asks you whether or not you want to support fidelity bonds I recommend using the _yes_ option, the output returned will look like this:


```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```

in case an error appears it is most likely that we have incorrectly set the 4 RPC fields specified above. In case it might help to follow [this guide](https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure) found in the original JoinMarket documentation.


We have completed the setup of our working environment and can begin to explore the commands that will be most useful to us. All the scripts we will discuss can be launched in the console followed by `--help` for an in-depth explanation.


We can now try to launch:


```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```


this command will show you all the various wallet mixdepths with the various addresses categorized as:


- New (Address never used)
- Change-out (remainder of a previous transaction)
- Cj-out (output of a CoinJoin)


here is a practical example of the result:


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

Now we can proceed to deposit our first Satoshis within one or more addresses remembering that regardless of maker or taker, the software will never go and consolidate UTXO into different mixdepths directly, this way we can keep Satss with different levels of privacy separate within Wallet.


## Sending Bitcoin with CoinJoin Single


We can now move our Satoshis. One of the main commands in this software is the script:


```bash
pyhton sendpayment.py
```

which will allow us to send transactions to other addresses with or without CoinJoin. Let's go over how it works and some practical examples. By default the formatting of the command is (remember to replace the text enclosed by the symbols < and >):


```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```


a basic example of use might be:


```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```

in this case we are going to send to the address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0.05 Btc i.e. 5000000 Satoshi from our mixdepth 0 (the default one) by going to choose from 4 to 9 counterparts for CoinJoin (default option).


To have more control over how and which UTXOs to spend we can go over the additional options to this command:


```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```

in this example we have added two specifications: -N indicates how many counterparties we are going to mix with, -m the mixdepth from which we are going to withdraw funds. In fact, we have sent 100,000,000 Sats (1 btc) to the address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c with the funds in mixdepth 1 and mixing with 5 counterparties.


If we put 0 as the send value by specifying a mixdepth, joinMarket will perform a so-called `sweep`, that is, it will send all the funds in that mixdepth by consolidating them with each other:


```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


here we sent all the funds from mixdepth 0 (we could have not specified it because that is the default) mixing with 7 counterparts.


The sendpayment command is used to move funds from joinMarket to external Wallet or to send Satoshi to a person by adding a Layer of privacy between us and him. To gain a sufficient level of privacy on our UTXOs it is more appropriate to use the tumbler.py command which we will explain later in this guide.


## Being a Maker


The script we are going to cover in this section is:


```bash
yg-privacyenhanced.py
```


This program is used to act as a maker in the joinMarket. The software will connect to our Bitcoin node and to the internal marketplace of the platform in which the makers present themselves as liquidity bidders and takers look for counterparties. In case you want to use a fidelity bond you can create one with this formatting:


```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```


for example:


```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```


the output that will be returned to us will be a Bitcoin address (i.e., the one on which you will need to deposit the funds you want to allocate to fidelity).


**Caution**: There are two things to pay close attention to if you are going to create a Fidelity Bond (a.k.a. FB);



- once the funds have been deposited, they cannot be moved again until it expires. Pay attention to how many Satss you send to the address and how you format the date. Errors are not allowed!
- The fidelity bond is easily recognizable onchain, so it is advisable to deposit funds through a CoinJoin and with an origin unrelated to your identity. The same thing is also advisable to do once you want to move the expired fidelity bond out of JoinMarket.


It is important to remember that it is possible to reload the fidelity bond with only one transaction, in case of UTXO multiples only the largest one will be considered valid for FB.


Let us now deal with the script mentioned at the beginning of this paragraph, once we have created the fidelity bond (which we remember is optional) we are ready to run the executable to act as a maker on joinMarket. Once the Satss have been deposited at the various addresses and mixdepth we can run the command:


```bash
python yg-privacyenhanced.py <wallet name>
```


From this point on (after a few minutes of connecting to the network) and until we stop the script, our JoinMarket client will appear on the list of active makers on the protocol and offer our liquidity to various counterparties to make CoinJoin. Do not expect dozens of CoinJoins per day (unless you have huge fidlity and large liquidity deposited on Wallet), also remember that factors such as fees required and Satoshis deposited affect how often you will be a maker.


By running the command below you will be able to see the history of all the transactions made on Wallet and any gain (if you are a maker) or fee expense (if you are a taker) you have had over the lifetime of the wallet.


```bash
python wallet-tool.py <wallet name> history
```


Once your Satoshis make CoinJoins, they will move from mixdepth to mixdepth until they reach the last one. Once past the fourth they will return to mixdepth 0, it is up to you how much privacy to get before moving them to a Cold Wallet, it is advisable to finish a full Wallet cycle.


## Tumbler


Here we are finally at the juiciest part of JoinMarket, the tumbler! If you've listened to the podcast you already know what this is all about. One recommendation before we get started: **Beware of fees!** Remember to set the limits in the joinmarket.cfg file (as explained at the beginning) and consider running the program only when onchain fees are relatively low (under 10 Sats/vB).


To launch the tumbler it is necessary to have stopped the script from maker (if it was active), after that we can run the command:


```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```


It is essential to enter **at least** 3 output addresses for the tumbler: this is to ensure good privacy and not to create obvious links between UTXOs throughout the process. As usual by adding`--help` to the command you can go and see all the additional details. Let`s go to view a more complex example with advanced rules:


```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```


In this case we have launched a tumbling script that will not use the default number of counterparts (the -N parameter indicates that we require 7 counterparts with a maximum variance of 2, so a random number of makers from 5 to 9) and with a larger number of CoinJoin per mixdepth (by default this script makes a random number of CoinJoin per section of Wallet ranging from 1 to 3, using the -c 3 1 command instead will be from 2 TO 4). This way we will spend more Sats in fees but have a greater anonymity set.


You can also add as many output addresses as you want (minimum 3, there is no maximum other than common sense). However, it is not possible, for privacy issues, to decide how Satoshi will be distributed among the addresses specified as output.


Tumbler is a deliberately long process, occasionally it may happen that something stops working, in most cases this will resolve itself within a few hours. In case of a total crash we can attempt to restart it with the command:


```bash
python tumbler.py --restart
```


Or simply restart a new tumbling command. This will not start the scheduling of the previous tumbler but will start a new mixing cycle. In case closing the SSH terminal to your node also stops the script you can take advantage of the `TMUX` program that can be installed with the command:


```bash
sudo apt install tmux
```


Launching it from the shell by typing `tmux` will open a terminal for you that will remain active in the background even if you close the remote connection. When you re-connect to your node with the command: `tmux attach` you will re-open the shell that remained active in the background.


## Conclusion


JoinMarket is boundless and customizable software. In this guide we have discovered the main functions so that it is possible for anyone (or at least I have tried, I realize that using this software is not a walk in the park) to use it. One of the biggest problems with JoinMarket is just that: the number of people using it and being a maker. If few users take advantage of this software, the overall privacy (anon-set) is lowered. That's why I hope this guide will incentivize use and convince you to download and install my favorite software to make CoinJoin. In case you want to go even deeper into some aspects I recommend you to give a read to the various in-depth docs on github, they are really well done and you can find them here.


Happy mixing turtles!🐢 💚


[Here](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) you can support Turtlecute
