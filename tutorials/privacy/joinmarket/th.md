---
name: JoinMarket

description: คู่มือและบทแนะนำวิธีการใช้ JoinMarket เพื่อทำ CoinJoin ผ่าน Bitcoin ผ่านทางบรรทัดคำสั่ง
---

![cover](assets/cover.webp)



---

หากคุณพบหน้านี้โดยการค้นหาออนไลน์สำหรับ "JoinTmarket" ฉันขอขอบคุณอย่างจริงใจ อย่างไรก็ตาม คุณได้พบกับคู่มือที่เกี่ยวข้องกับหัวข้อที่แตกต่างไปอย่างสิ้นเชิง แต่เป็นหัวข้อที่น่าสนใจอย่างยิ่ง! 🚬🍁



วัตถุประสงค์ของบทแนะนำนี้คือการแสดงการทำงานทางทฤษฎีและปฏิบัติของ JoinMarket ผ่านทางบรรทัดคำสั่ง 🐢 💚



## JoinMarket คำจำกัดความทางทฤษฎี



เราสามารถกำหนด JoinMarket เป็นเครื่องมือ หรือ Wallet ที่ช่วยให้ CoinJoin กับผู้ใช้อื่นในลักษณะ Trustless อย่างสมบูรณ์และไม่มีผู้ประสานงานกลางใดๆ



เนื่องจากส่วนทฤษฎีทั้งหมดของเครื่องมือนี้มีความกว้างขวางมาก ฉันจึงตัดสินใจที่จะพูดถึงมันในตอนเฉพาะของพอดแคสต์ของฉัน สำหรับผู้ที่สามารถเข้าใจภาษาอิตาลีได้ ฉันขอแนะนำอย่างยิ่งให้คุณอ่านต่อหลังจากฟังตอนนี้ เพื่อที่จะได้ซึมซับแนวคิดพื้นฐานสำหรับการใช้โปรแกรมนี้อย่างถูกต้อง



คุณสามารถติดตามตอนนี้ได้ที่ลิงก์โดยตรงเหล่านี้:




- [Spotify](https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Google podcast](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (ที่นี่คุณสามารถฟังได้โดยตรงจากเบราว์เซอร์)
- [Antenna pod](https://antennapod.org/) เป็นโปรแกรมจัดการพอดแคสต์ที่ฟรีและโอเพ่นซอร์สซึ่งไม่ต้องการการลงทะเบียน เพื่อค้นหาตอน ดาวน์โหลดแอป เพิ่มพอดแคสต์ของฉันด้วยตนเองโดยการวาง [ลิงก์นี้](https://Anchor.fm/s/bd5d5b20/podcast/rss) ในส่วน _feed rss_ จากนั้นค้นหาตอนที่อุทิศให้กับ JoinMarket



## การติดตั้ง



ระบบปฏิบัติการ:





- Raspiblitz
- Umbrel
- MyNode
- Raspibolt



## ไฟล์การกำหนดค่า



JoinMarket เป็นซอฟต์แวร์ที่สามารถปรับแต่งได้ด้วยการตั้งค่าที่ไม่มีที่สิ้นสุด; การตั้งค่าเหล่านี้ถูกระบุในไฟล์การกำหนดค่าที่อยู่ในไดเรกทอรีโปรแกรมหลักที่เรียกว่า `Joinmarket.cfg`.



ในส่วนนี้เราจะไปสำรวจบางฟิลด์ที่คุณอาจสนใจที่จะสำรวจและ/หรือแก้ไข ขึ้นอยู่กับความต้องการของคุณ ฉันอยากจะเน้นย้ำว่าการเปลี่ยนแปลงทั้งหมดที่ระบุไว้ด้านล่างนี้มีประโยชน์ที่จะรู้เพื่อปรับการทำงานของซอฟต์แวร์ให้เข้ากับความต้องการส่วนบุคคลโดยไม่จำเป็นต้องทำตาม



ก่อนอื่นให้ย้ายไปที่โฟลเดอร์ `joinmarket/scripts` และรันคำสั่ง:



```bash
python wallet-tool.py generate
```


ณ จุดนี้เราควรจะได้รับข้อผิดพลาด แต่การทำเช่นนั้นจะทำให้ซอฟต์แวร์สร้างไฟล์การตั้งค่าที่ตั้งไว้ล่วงหน้าสำหรับเรา เราสามารถไปแก้ไขไฟล์การตั้งค่าได้จากเทอร์มินัลด้วย:



```bash
nano joinmarket.cfg
```



หรือ:



```bash
vim joinmarket.cfg
```



เมื่อเปิดแล้ว เราจะสังเกตเห็นบรรทัดจำนวนมากที่มีการตั้งค่าต่างๆ และคำอธิบายเป็นภาษาอังกฤษ โดยเฉพาะอย่างยิ่งเราจะวิเคราะห์ตัวแปรที่น่าสนใจที่สุดด้านล่าง:





- `merge_algorithm` ในกรณีที่เราทำหน้าที่เป็นผู้สร้าง ฟิลด์นี้จะปรับวิธีการรวม Outputs ที่ยังไม่ได้ใช้ให้มีความเข้มข้นมากขึ้น หากเรามี UTXO จำนวนมากที่จะรวมเข้าด้วยกัน อาจจะมีเหตุผลในการเปลี่ยนจาก _gradual_ เป็น _greedy_
- `tx_fees` ปรับเป็นผู้รับค่าธรรมเนียมที่ใช้ในการจ่ายธุรกรรม ซึ่งมีประโยชน์มากในการเปลี่ยนการตั้งค่านี้ในกรณีที่คุณใช้ tumbler บ่อย ๆ (เราจะพูดถึงเรื่องนี้ในภายหลัง) เพราะถ้ามีการเพิ่มขึ้นของค่าธรรมเนียมในระหว่างการดำเนินการของสิ่งหลัง ถ้าเราไม่ตั้งค่าสนามนี้อย่างถูกต้อง เราเสี่ยงที่จะใช้ Sats มากสำหรับ CoinJoin โดยการตั้งค่าตัวเลขในหลักพัน (เช่น 2000) จะเท่ากับ 2 Sats/vBytes, 3500 จะเท่ากับ 3.5 Sats/vBytes และอื่น ๆ ฉันขอแนะนำตัวเลขที่อยู่ในช่วง 1500 ถึง 6000 ขึ้นอยู่กับความต้องการของคุณ
- `max_cj_fee_abs` ใช้เพื่อระบุจำนวนเงินที่เรายินดีจ่ายในรูปแบบตัวเลขที่แน่นอนสำหรับผู้ผลิตที่เราเลือกในช่วง CoinJoin โดยค่าเริ่มต้นฟิลด์นี้สำหรับผู้ผลิตคือ 200 Sats ตัวเลือกที่ดีอาจเป็นตัวเลขที่อยู่ในช่วง 200 ถึง 1000 Sats ต่อคู่ค้า (ขึ้นอยู่กับว่าคุณต้องการใช้จ่ายเท่าไรและต้องการ anon-set มากแค่ไหนสำหรับ CoinJoin ของคุณ)
- `max_cj_fee_rel` มีฟังก์ชันเดียวกับฟิลด์ด้านบนแต่ระบุค่าธรรมเนียมสัมพัทธ์ (เปอร์เซ็นต์) ที่เรายินดีจ่ายให้กับแต่ละคู่สัญญา เนื่องจากนี่เป็นค่า `เปอร์เซ็นต์` โปรดระวังอย่าตั้งค่าสูงเกินไปเพื่อหลีกเลี่ยงค่าใช้จ่ายสูงใน CoinJoins ที่มีจำนวนมาก ค่าเริ่มต้นสำหรับผู้ผลิตคือ _0.00002_ ฉันแนะนำค่าใกล้เคียงหรือสูงกว่านี้เล็กน้อย
- `minimum_makers` เป็นฟิลด์ที่ระบุว่ามีคู่สัญญาอื่น ๆ กี่รายที่เราทำ CoinJoin ด้วย โดยค่าเริ่มต้น JoinMarket จะเลือกจากคู่สัญญา 4 ถึง 9 ราย หากเราต้องการความเป็นส่วนตัวมากขึ้น เราสามารถเพิ่มค่านี้เป็น 5 หรือ 6 ได้ (แต่มันจะทำให้การทำธุรกรรมมีค่าใช้จ่ายสูงขึ้น)
- `cjfee_a` ระบุว่า ในกรณีที่เราเป็นผู้สร้าง เราต้องการเก็บ Sats เป็นจำนวนเท่าใดในเชิงสัมบูรณ์สำหรับการให้เช่าสภาพคล่องของเรา ฟิลด์นี้เป็นเรื่องส่วนตัวทั้งหมด ค่าดีฟอลต์นั้นดีมากอยู่แล้ว (เราจะมีความเป็นส่วนตัวที่ดีกว่าในฐานะผู้สร้าง) เราสามารถพิจารณาปรับเป็น 0 ได้หากเราต้องการทำ CoinJoin มากขึ้นในเวลาที่น้อยลง
- `cjfee_r` เหมือนกับฟิลด์ด้านบนแต่ในรูปแบบเปอร์เซ็นต์และไม่ใช่จำนวนเต็ม อีกครั้งที่ฉันแนะนำให้คงค่าเริ่มต้นไว้หรือลดลงเพื่อดึงดูดผู้เข้าร่วมมากขึ้น
- `ordertype` ด้วยฟิลด์นี้เราสามารถเลือกจากผู้สร้างว่าจะเรียกเก็บแบบแน่นอน (absoffer) หรือแบบเปอร์เซ็นต์ (reloffer) โดยปกติผู้รับมักจะชอบการเสนอราคาแบบแน่นอนสำหรับปัญหาทางเศรษฐกิจ
- `minsize` หากในฐานะผู้ผลิตเราไม่ต้องการให้ UTXO มีขนาดเล็กเกินไป เราสามารถระบุ CoinJoin ขั้นต่ำที่จะเข้าร่วมได้ ฟิลด์นี้แสดงใน Satoshi และเป็นเรื่องที่ขึ้นอยู่กับดุลยพินิจทั้งหมด เราสามารถปล่อยฟิลด์นี้ไว้ที่ 0 หรือเพิ่มเป็น 500000 (Sats), 1000000 (Sats) และอื่นๆ



ระวังอย่างมากที่จะไม่แก้ไขฟิลด์ที่ผิดพลาด บางตัวแปรในไฟล์ joinmarket.cfg หากตั้งค่าไม่ถูกต้องอาจทำให้การทำงานของซอฟต์แวร์มีปัญหาหรือทำลายความเป็นส่วนตัวของคุณอย่างสิ้นเชิง เปิดตาและระมัดระวังให้ถึงที่สุด!



## การตั้งค่าสภาพแวดล้อมการทำงาน



โหนดบางตัวตั้งค่าที่ถูกต้องสำหรับฟิลด์เหล่านี้โดยอัตโนมัติภายในไฟล์ joinmarket.cfg ฉันแนะนำให้ตรวจสอบอีกครั้งด้วยตนเอง:





- `rpc_user = yourusername-as-in-Bitcoin.conf`
- `rpc_password = yourpassword-as-in-Bitcoin.conf`
- `rpc_host = localhost #default usually correct`
- `rpc_port = 8332 # ค่าเริ่มต้นสำหรับ Mainnet`



ณ จุดนี้เราสามารถดำเนินการสร้าง Wallet ของเราภายใน JoinMarket ได้:



```bash
python wallet-tool.py generate
```



คำสั่งนี้จะให้เราป้อนรหัสผ่านเพื่อเข้ารหัส Wallet และชื่อที่เราต้องการตั้งให้มัน เมื่อมันถามว่าคุณต้องการสนับสนุน fidelity bonds หรือไม่ ฉันแนะนำให้ใช้ตัวเลือก _yes_ ผลลัพธ์ที่ได้จะมีลักษณะดังนี้:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


ในกรณีที่เกิดข้อผิดพลาด มีความเป็นไปได้สูงว่าเราได้ตั้งค่า 4 ฟิลด์ RPC ที่ระบุไว้ข้างต้นไม่ถูกต้อง ในกรณีที่อาจช่วยได้ ให้ทำตาม [คู่มือนี้](https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure) ที่พบในเอกสาร JoinMarket ดั้งเดิม



เราได้ตั้งค่าสภาพแวดล้อมการทำงานของเราเสร็จสิ้นแล้วและสามารถเริ่มสำรวจคำสั่งที่มีประโยชน์ที่สุดสำหรับเราได้ script ทั้งหมดที่เราจะพูดถึงสามารถเปิดใช้งานในคอนโซลตามด้วย `--help` เพื่อคำอธิบายเชิงลึก



เราสามารถลองเปิดตัวได้แล้ว:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



คำสั่งนี้จะแสดงให้คุณเห็นถึงความลึกของการผสม wallet ทั้งหมดพร้อมกับที่อยู่ต่าง ๆ ที่จัดหมวดหมู่เป็น:




- ใหม่ (Address ไม่เคยใช้)
- เปลี่ยนออก (ส่วนที่เหลือจากธุรกรรมก่อนหน้า)
- Cj-out (เอาต์พุตของ CoinJoin)



นี่คือตัวอย่างที่เป็นรูปธรรมของผลลัพธ์:



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


ตอนนี้เราสามารถดำเนินการฝาก Satoshis แรกของเราในที่อยู่หนึ่งหรือมากกว่า โดยจำไว้ว่าจะเป็นผู้สร้างหรือผู้รับก็ตาม ซอฟต์แวร์จะไม่รวม UTXO เข้ากับ mixdepths ที่แตกต่างกันโดยตรง ด้วยวิธีนี้เราสามารถเก็บ Satss ที่มีระดับความเป็นส่วนตัวต่างกันแยกไว้ภายใน Wallet ได้



## กำลังส่ง Bitcoin พร้อมกับ CoinJoin เดี่ยว



เราสามารถย้าย Satoshi ของเราได้แล้ว หนึ่งในคำสั่งหลักในซอฟต์แวร์นี้คือ script:



```bash
pyhton sendpayment.py
```


ซึ่งจะช่วยให้เราสามารถส่งธุรกรรมไปยังที่อยู่อื่น ๆ ได้ทั้งที่มีหรือไม่มี CoinJoin มาเริ่มกันเลยว่ามันทำงานอย่างไรและตัวอย่างการใช้งานจริง โดยค่าเริ่มต้น รูปแบบของคำสั่งคือ (อย่าลืมแทนที่ข้อความที่อยู่ภายในสัญลักษณ์ < และ >):



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



ตัวอย่างการใช้งานพื้นฐานอาจเป็น:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


ในกรณีนี้เราจะส่งไปยังที่อยู่ 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c จำนวน 0.05 Btc หรือ 5000000 Satoshi จาก mixdepth 0 ของเรา (ซึ่งเป็นค่าเริ่มต้น) โดยจะเลือกจาก 4 ถึง 9 คู่สัญญาสำหรับ CoinJoin (ตัวเลือกเริ่มต้น)



เพื่อให้มีการควบคุมมากขึ้นเกี่ยวกับวิธีและการใช้ UTXOs เราสามารถตรวจสอบตัวเลือกเพิ่มเติมสำหรับคำสั่งนี้:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


ในตัวอย่างนี้ เราได้เพิ่มสองสเปค: -N ระบุจำนวนคู่สัญญาที่เราจะผสมด้วย, -m ระบุระดับการผสมที่เราจะถอนเงินออกมา ในความเป็นจริง เราได้ส่ง 100,000,000 Sats (1 btc) ไปยังที่อยู่ 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c โดยใช้เงินในระดับการผสมที่ 1 และผสมกับคู่สัญญา 5 ราย



หากเราใส่ค่า 0 เป็นค่าในการส่งโดยระบุ mixdepth, joinMarket จะทำการ `sweep` ซึ่งหมายความว่าจะส่งเงินทั้งหมดใน mixdepth นั้นโดยการรวมเข้าด้วยกัน:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



ที่นี่เราได้ส่งเงินทั้งหมดจาก mixdepth 0 (เราสามารถไม่ระบุได้เพราะนั่นคือค่าเริ่มต้น) ผสมกับคู่สัญญา 7 ราย



คำสั่ง sendpayment ใช้เพื่อย้ายเงินจาก joinMarket ไปยัง Wallet ภายนอกหรือเพื่อส่ง Satoshi ไปยังบุคคลโดยการเพิ่ม Layer ของความเป็นส่วนตัวระหว่างเราและเขา เพื่อให้ได้ระดับความเป็นส่วนตัวที่เพียงพอบน UTXO ของเรา การใช้คำสั่ง tumbler.py จะเหมาะสมกว่า ซึ่งเราจะอธิบายในคู่มือนี้ภายหลัง



## การเป็นผู้สร้าง



script ที่เราจะครอบคลุมในส่วนนี้คือ:



```bash
yg-privacyenhanced.py
```



โปรแกรมนี้ใช้เพื่อทำหน้าที่เป็นผู้สร้างใน joinMarket ซอฟต์แวร์จะเชื่อมต่อกับโหนด Bitcoin ของเราและตลาดภายในของแพลตฟอร์มซึ่งผู้สร้างจะนำเสนอตัวเองเป็นผู้เสนอราคาและผู้รับจะมองหาคู่สัญญา ในกรณีที่คุณต้องการใช้พันธบัตรความซื่อสัตย์คุณสามารถสร้างได้ด้วยรูปแบบนี้:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



ตัวอย่างเช่น:



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



ผลลัพธ์ที่จะถูกส่งกลับมาหาเราจะเป็นที่อยู่ Bitcoin (เช่น ที่อยู่ที่คุณจะต้องฝากเงินที่คุณต้องการจัดสรรให้กับ Fidelity)



**คำเตือน**: มีสองสิ่งที่ต้องให้ความสนใจอย่างใกล้ชิดหากคุณจะสร้างพันธบัตรความซื่อสัตย์ (หรือที่เรียกว่า FB);





- เมื่อเงินถูกฝากแล้ว จะไม่สามารถย้ายได้อีกจนกว่าจะหมดอายุ โปรดใส่ใจกับจำนวน Sats ที่คุณส่งไปยังที่อยู่และวิธีการจัดรูปแบบวันที่ ไม่อนุญาตให้เกิดข้อผิดพลาด!
- พันธบัตรความซื่อสัตย์สามารถระบุได้ง่ายบนเชน ดังนั้นจึงแนะนำให้ฝากเงินผ่าน CoinJoin และด้วยแหล่งที่มาไม่เกี่ยวข้องกับตัวตนของคุณ สิ่งเดียวกันนี้ยังแนะนำให้ทำเมื่อคุณต้องการย้ายพันธบัตรความซื่อสัตย์ที่หมดอายุออกจาก JoinMarket



สิ่งสำคัญคือต้องจำไว้ว่าสามารถโหลดพันธบัตรความซื่อสัตย์ใหม่ได้ด้วยธุรกรรมเพียงรายการเดียว ในกรณีของ UTXO หลายรายการ จะพิจารณาเฉพาะรายการที่ใหญ่ที่สุดเท่านั้นว่าใช้ได้สำหรับ FB



ตอนนี้ให้เราจัดการกับ script ที่กล่าวถึงในตอนต้นของย่อหน้านี้ เมื่อเราได้สร้างพันธบัตรความซื่อสัตย์ (ซึ่งเราจำได้ว่าเป็นทางเลือก) เราพร้อมที่จะเรียกใช้ไฟล์ปฏิบัติการเพื่อทำหน้าที่เป็นผู้สร้างใน joinMarket เมื่อ Satss ได้ถูกฝากที่ที่อยู่และ mixdepth ต่างๆ แล้ว เราสามารถเรียกใช้คำสั่ง:



```bash
python yg-privacyenhanced.py <wallet name>
```



จากจุดนี้เป็นต้นไป (หลังจากเชื่อมต่อกับเครือข่ายไม่กี่นาที) และจนกว่าเราจะหยุด script ลูกค้า JoinMarket ของเราจะปรากฏในรายชื่อผู้สร้างที่ใช้งานอยู่บนโปรโตคอลและเสนอความคล่องตัวของเราให้กับคู่สัญญาต่างๆ เพื่อสร้าง CoinJoin อย่าคาดหวังว่าจะมี CoinJoin หลายสิบรายการต่อวัน (เว้นแต่คุณจะมีความจงรักภักดีสูงและมีสภาพคล่องจำนวนมากฝากไว้ใน Wallet) นอกจากนี้โปรดจำไว้ว่าปัจจัยต่างๆ เช่น ค่าธรรมเนียมที่ต้องการและ Satoshi ที่ฝากไว้มีผลต่อความถี่ที่คุณจะเป็นผู้สร้าง



โดยการรันคำสั่งด้านล่างนี้ คุณจะสามารถดูประวัติของธุรกรรมทั้งหมดที่ทำบน Wallet และกำไร (หากคุณเป็นผู้สร้าง) หรือค่าใช้จ่ายค่าธรรมเนียม (หากคุณเป็นผู้รับ) ที่คุณมีตลอดอายุการใช้งานของ wallet



```bash
python wallet-tool.py <wallet name> history
```



เมื่อ Satoshi ของคุณสร้าง CoinJoin แล้ว พวกมันจะย้ายจาก mixdepth ไปยัง mixdepth จนกว่าจะถึงอันสุดท้าย เมื่อผ่านที่สี่ไปแล้ว พวกมันจะกลับไปที่ mixdepth 0 ขึ้นอยู่กับคุณว่าจะต้องการความเป็นส่วนตัวมากแค่ไหนก่อนที่จะย้ายพวกมันไปยัง Cold Wallet ขอแนะนำให้ทำรอบ Wallet ให้เสร็จสมบูรณ์



## ทัมเบลอร์



ในที่สุดเราก็มาถึงส่วนที่น่าตื่นเต้นที่สุดของ JoinMarket, tumbler! ถ้าคุณได้ฟังพอดแคสต์แล้ว คุณก็รู้แล้วว่านี่เกี่ยวกับอะไร ข้อแนะนำหนึ่งข้อก่อนที่เราจะเริ่ม: **ระวังค่าธรรมเนียม!** อย่าลืมตั้งค่าขีดจำกัดในไฟล์ joinmarket.cfg (ตามที่อธิบายไว้ในตอนต้น) และพิจารณาเรียกใช้โปรแกรมเฉพาะเมื่อค่าธรรมเนียมบนเครือข่ายต่ำ (ต่ำกว่า 10 Sats/vB)



ในการเปิดตัว tumbler จำเป็นต้องหยุด script จากผู้ผลิต (หากมันกำลังทำงานอยู่) หลังจากนั้นเราสามารถรันคำสั่ง:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



จำเป็นต้องป้อนที่อยู่เอาต์พุต **อย่างน้อย** 3 ที่สำหรับ tumbler: เพื่อให้มั่นใจในความเป็นส่วนตัวที่ดีและไม่สร้างลิงก์ที่ชัดเจนระหว่าง UTXO ตลอดกระบวนการ ตามปกติโดยการเพิ่ม `--help` ไปยังคำสั่ง คุณสามารถดูรายละเอียดเพิ่มเติมทั้งหมดได้ ไปดูตัวอย่างที่ซับซ้อนมากขึ้นด้วยกฎขั้นสูง:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



ในกรณีนี้เราได้เปิดตัว script ที่จะไม่ใช้จำนวนคู่เทียบเริ่มต้น (พารามิเตอร์ -N ระบุว่าเราต้องการคู่เทียบ 7 คู่ โดยมีความแปรปรวนสูงสุด 2 ดังนั้นจำนวนผู้ผลิตแบบสุ่มจะอยู่ระหว่าง 5 ถึง 9) และมีจำนวน CoinJoin ต่อ mixdepth มากขึ้น (โดยค่าเริ่มต้น script นี้จะสร้างจำนวน CoinJoin แบบสุ่มต่อส่วนของ Wallet ตั้งแต่ 1 ถึง 3 โดยใช้คำสั่ง -c 3 1 แทนจะเป็นจาก 2 ถึง 4) ด้วยวิธีนี้เราจะใช้ Sats ในค่าธรรมเนียมมากขึ้นแต่จะมีชุดนิรนามที่มากขึ้น



คุณยังสามารถเพิ่มที่อยู่ปลายทางได้มากเท่าที่คุณต้องการ (ขั้นต่ำ 3 ไม่มีสูงสุดนอกจากสามัญสำนึก) อย่างไรก็ตาม ไม่สามารถตัดสินใจได้ว่า Satoshi จะถูกแจกจ่ายอย่างไรในบรรดาที่อยู่ที่ระบุเป็นปลายทาง เนื่องจากปัญหาด้านความเป็นส่วนตัว



Tumbler เป็นกระบวนการที่ใช้เวลานานโดยเจตนา บางครั้งอาจเกิดเหตุการณ์ที่บางอย่างหยุดทำงาน ในกรณีส่วนใหญ่สิ่งนี้จะแก้ไขได้เองภายในไม่กี่ชั่วโมง ในกรณีที่เกิดการขัดข้องทั้งหมด เราสามารถพยายามรีสตาร์ทด้วยคำสั่ง:



```bash
python tumbler.py --restart
```



หรือเพียงแค่เริ่มคำสั่งการหมุนใหม่ นี่จะไม่เริ่มการจัดตารางของ tumbler ก่อนหน้า แต่จะเริ่มรอบการผสมใหม่ ในกรณีที่การปิด SSH terminal ไปยังโหนดของคุณยังหยุด script คุณสามารถใช้ประโยชน์จากโปรแกรม `TMUX` ที่สามารถติดตั้งได้ด้วยคำสั่ง:



```bash
sudo apt install tmux
```



การเปิดใช้งานจากเชลล์โดยการพิมพ์ `tmux` จะเปิดเทอร์มินัลให้คุณซึ่งจะยังคงทำงานอยู่ในพื้นหลังแม้ว่าคุณจะปิดการเชื่อมต่อระยะไกล เมื่อคุณเชื่อมต่อกลับไปยังโหนดของคุณด้วยคำสั่ง: `tmux attach` คุณจะเปิดเชลล์ที่ยังคงทำงานอยู่ในพื้นหลังอีกครั้ง



## บทสรุป



JoinMarket เป็นซอฟต์แวร์ที่ไร้ขีดจำกัดและปรับแต่งได้ ในคู่มือนี้เราได้ค้นพบฟังก์ชันหลักๆ เพื่อให้ทุกคนสามารถใช้งานได้ (หรืออย่างน้อยฉันก็พยายามแล้ว, ฉันรู้ว่าการใช้ซอฟต์แวร์นี้ไม่ใช่เรื่องง่าย) หนึ่งในปัญหาที่ใหญ่ที่สุดของ JoinMarket ก็คือจำนวนคนที่ใช้และเป็นผู้สร้าง หากมีผู้ใช้น้อยที่ใช้ประโยชน์จากซอฟต์แวร์นี้ ความเป็นส่วนตัวโดยรวม (anon-set) จะลดลง นั่นคือเหตุผลที่ฉันหวังว่าคู่มือนี้จะกระตุ้นการใช้งานและทำให้คุณดาวน์โหลดและติดตั้งซอฟต์แวร์ที่ฉันชื่นชอบเพื่อสร้าง CoinJoin ในกรณีที่คุณต้องการเจาะลึกในบางแง่มุม ฉันแนะนำให้คุณอ่านเอกสารเชิงลึกต่างๆ บน github ซึ่งทำได้ดีมากและคุณสามารถหาได้ที่นี่



สุขสันต์การผสมเต่า!🐢 💚



[Here](https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) คุณสามารถสนับสนุน Turtlecute