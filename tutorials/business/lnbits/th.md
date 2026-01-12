---
name: LNbits

description: แพลตฟอร์มการบัญชีสำหรับพ่อค้า
---

![presentation](assets/cover.webp)

## ระบบบัญชี


LNbits เต็มไปด้วยเครื่องมือมากมายเพื่อควบคุมและจัดการเงินที่เข้ามาและออกไปของคุณ เชื่อมต่อร้านค้าออนไลน์หรือแม้แต่อุปกรณ์ต่างๆ เช่น ฮาร์ดแวร์ wallet หรือ ATM ที่คุณสร้างขึ้นเอง ประเภทผู้ใช้ประกอบด้วย:


- เจ้าของ Wallet ที่ต้องการใช้ LNbits เป็นอินเทอร์เฟซสำหรับการจัดการกองทุนของพวกเขารวมถึงคุณสมบัติเพิ่มเติม
- ผู้ค้าออนไลน์และออฟไลน์หรือผู้ให้บริการที่ต้องการรับชำระเงิน Bitcoin onchain และ Lightning Network
- นักพัฒนาที่ต้องการสร้างแอปพลิเคชัน Lightning Network
- ผู้ดำเนินการโหนดที่ต้องการรวมโหนดของตนเข้ากับระบบ LNbits เพื่อวัตถุประสงค์ทางบัญชี
- ทั้งหมดนี้มีความต้องการที่แตกต่างกัน เราสร้าง LNbits ในรูปแบบโมดูลาร์เพื่อให้ผู้ใช้ทุกคนสามารถใช้คุณสมบัติของเราในแบบที่เหมาะสมที่สุดสำหรับคุณ


## Wallet ผู้จัดการ


LNbits เป็นระบบบัญชีที่ฟรีและโอเพ่นซอร์ส - ไม่ใช่ตัวจัดการโหนด การจัดการช่องทางเป็นหน้าที่ของโหนด Lightning ที่เชื่อมต่อกับ LNbits ในฐานะแหล่งเงินทุน เช่น LND หรือ c-lightning ผู้ใช้ Superuser หรือ Admin ในระบบ LNbits มีหน้าที่รับผิดชอบในการจัดการการเข้าถึงและการกำหนดค่าของฟีเจอร์บัญชีและส่วนขยายภายในโดยรวม


LNbits ทำหน้าที่เป็นตัวเชื่อมระหว่างผู้ใช้และโหนด Lightning โดยให้วิธีการที่ง่ายและเป็นมิตรกับผู้ใช้ในการจัดการและโต้ตอบกับเครือข่ายการชำระเงิน


คิดว่า LNbits เป็นเหมือน “กรอบงานโมดูลาร์ของ WordPress” สำหรับโหนดของคุณ แพลตฟอร์มที่จัดการได้ง่าย โดยอิงจากส่วนขยายที่คุณสามารถรวมกันเพื่อใช้ในกรณีต่างๆ ได้มากมาย


คิดว่า LNbits เป็นซอฟต์แวร์การจัดการการเงินธนาคารของคุณเอง โหนดของคุณเสนอช่องทางในการชำระเงินผ่านและ LNbits ขยายโหนดของคุณให้สามารถรันมากกว่า wallet สายฟ้าที่โหนดของคุณมาพร้อมกับ กระเป๋าเงินเหล่านี้ไม่จำเป็นต้องเป็นของคุณเอง ลองนึกภาพว่าคุณ ในฐานะผู้ดำเนินการโหนด LN มีสภาพคล่องของช่องทางและเงินทุนเพียงพอแล้ว และตอนนี้คุณต้องการเสนอบริการธนาคารบิตคอยน์ให้กับเพื่อน ครอบครัว ร้านค้าของคุณเอง หรือพ่อค้าอื่นๆ ที่เป็นประจำ


คุณจะเสนอวิธีง่ายๆ ให้พวกเขาเปิด "บัญชีธนาคาร" บนโหนดของคุณโดยไม่ต้องเข้าถึงกระเป๋าเงินอื่นๆ บนโหนดของคุณและสภาพคล่องทั้งหมดของโหนดของคุณ แต่เฉพาะส่วนของพวกเขาเท่านั้น โหนดของคุณ (ธนาคาร) ทำหน้าที่เป็นเพียงผู้ให้บริการขนส่งสำหรับการชำระเงินของพวกเขา (เข้า/ออก)


หมายเหตุ: เงินทั้งหมดที่ "ลูกค้า" ของคุณฝากเข้าบัญชีธนาคาร LNbits บนโหนดของคุณ จะถูกส่งตรงไปยังช่องทาง LN ของโหนดคุณ นั่นหมายความว่า คุณคือเจ้าของที่แท้จริงของเงินเหล่านั้น คุณจะมีความรับผิดชอบอย่างมากต่อเงินของพวกเขา อย่าทำตัวเลวและหนีไปพร้อมกับเงิน อย่าทำตัวเลวและคิดค่าธรรมเนียมสูง เราต้องการจัดการกับธนาคารฟิอัต ไม่ใช่จัดการกันเอง (ผู้ใช้บิตคอยน์)


## แพลตฟอร์มสาธิต


สามารถดูการสาธิตได้ที่ [https://legend.lnbits.com](https://legend.lnbits.com) ซึ่งสามารถใช้งานได้เต็มรูปแบบและสามารถใช้เพื่อเรียนรู้เกี่ยวกับ Lightning Network และคุณสมบัติของ LNbits และ LNURL โดยทั่วไป แม้ว่าเราจะไม่สามารถป้องกันคุณจากการใช้งานได้ แต่เราขอให้คุณไม่ใช้มันสำหรับการตั้งค่าการผลิตของคุณ ไม่เพียงแต่เรากำลังทำงานบนเซิร์ฟเวอร์บ่อยครั้งเพื่อทดสอบคุณสมบัติใหม่ ๆ แต่เรายังต้องการสนับสนุนให้คุณเรียกใช้โหนดของคุณเองและ LNbits ในวิธีที่เป็นอิสระ หากคุณคิดว่าการเรียกใช้โหนดเป็นเรื่องที่มากเกินไปในขณะนี้ คุณสามารถเชื่อมต่อ LNbits กับบริการการระดมทุนผู้ดูแลในคลาวด์ เช่น Opennode, Luna หรือ Votage หรือกับ Lightning Tipbot บน Telegram เพียงเพื่อยกตัวอย่างบางส่วน


## LNbits ใบปลิว


ต้องการส่งมอบข้อมูลพื้นฐานให้กับพ่อค้าหรือเพื่อนที่ทำงานก่อสร้างของคุณหรือไม่? เรามีความยินดีที่จะประกาศแผ่นพับแรกของเราให้ทุกคนได้ใช้ ขนาดเป็นรูปแบบแผ่นพับที่เป็นมาตรฐานสากล มี 6 หน้า (พับ 2 ครั้ง) และมีความกว้าง 3508 และความสูง 2480px.


LNbits สำหรับผู้ค้า: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)


LNbits สำหรับผู้สร้าง: [EN](/assets/lnbits-builders-en.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)


## พื้นฐานบางประการ


LNbits ทำงานบนโปรโตคอล LNURL ซึ่งหมายความว่าคำขอจะถูกต้องในสองรูปแบบ: ไม่ว่าจะเป็นลิงก์ https://clearnet (ไม่อนุญาตให้ใช้ใบรับรองที่ลงนามด้วยตนเอง) หรือเป็นลิงก์ http://v2/v3 onion เพื่อให้บริการ LNbits เช่น LNURLp/w รหัส QR หรือบัตร NFC ที่สามารถใช้ในที่สาธารณะได้ คุณจะต้องเปิด LNbits ไปยัง clearnet (https)


ก่อนที่คุณจะติดตั้ง LNbits โปรดตรวจสอบให้แน่ใจว่าคุณได้อ่านและเข้าใจคู่มือทั่วไปต่อไปนี้เกี่ยวกับว่า LNbits คืออะไรและมีความเป็นไปได้ใดบ้างที่มันจะปลดปล่อยให้คุณ



- [LND Guide](https://docs.lightning.engineering/) | การติดตั้ง LND
- [LND Config Example](https://github.com/lightningnetwork/lnd/blob/master/sample-lnd.conf) | การตั้งค่า LND
- [คู่มือ CLN](https://docs.corelightning.org/docs/installation) | การติดตั้ง CLN
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips)  Nostr Spec
- [เรียกใช้หอคอยเฝ้าระวัง](https://docs.lightning.engineering/lightning-network-tools/lnd/watchtower) | สำคัญมาก!


คำแนะนำที่ละเอียดมากขึ้นเกี่ยวกับการใช้ LNbits ในสถานการณ์การใช้งานเฉพาะที่นี่:



- [เริ่มต้นกับ LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | คู่มือ Substack
- [ToDos for your safety with LNbits](https://youtu.be/i5FQf96e6zg) | Youtube Video
- [Private Banks on Lightning Network](https://darthcoin.substack.com/p/bitcoin-private-banks-over-lightning) | คู่มือ Substack
- [เรียกใช้กระเป๋าเงินผู้ดูแลสำหรับเพื่อนและครอบครัวของคุณ](https://darthcoin.substack.com/p/the-bank-of-lnbits) | คู่มือ Substack
- [LNbits สำหรับร้านอาหาร / โรงแรมขนาดเล็ก](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | คู่มือ Substack
- [Using LNbits Streamer copilot](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | คู่มือ Substack
- [เริ่มต้นตลาด NOSTR ของคุณด้วย LNbits](https://darthcoin.substack.com/p/lnbits-nostr-market) | คู่มือ Substack
- [การใช้ LNbits สำหรับโครงการโรงเรียนหรือกิจกรรมเทศกาล](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) คู่มือ Substack



## ติดตั้ง LNbits


### คู่มือการติดตั้งพื้นฐาน


LNbits สามารถติดตั้งบนเครื่อง Linux OS ใดก็ได้ ไม่จำเป็นต้องใช้เครื่องหรือเซิร์ฟเวอร์ที่มีประสิทธิภาพสูง เพียงแค่มีหน่วยความจำ RAM เพียงพอและพื้นที่ดิสก์สำหรับฐานข้อมูล สามารถรันแยกจากโหนด BTC/LN (PC ท้องถิ่นหรือ VPS ระยะไกล) หรือรันร่วมกันบนเครื่องเดียวกับโหนดหรือเครื่องซอฟต์แวร์โหนดที่ติดตั้งไว้แล้วในรูปแบบบันเดิล


คุณสามารถเลือกใช้ตัวจัดการแพ็คเกจที่พบได้บ่อยที่สุด เช่น poetry และ nix โดยค่าเริ่มต้น LNbits จะใช้ SQLite เป็นฐานข้อมูล คุณยังสามารถใช้ PostgreSQL ซึ่งแนะนำสำหรับแอปพลิเคชันที่มีการโหลดสูง [นี่คือคู่มือสำหรับการติดตั้งพื้นฐานโดยใช้ poetry หรือ nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md)


สำหรับทุกคนที่ใหม่กับสิ่งนี้ คุณจะพบคำแนะนำทีละขั้นตอนที่ละเอียดมากขึ้นสำหรับการใช้งาน LNbits ของคุณในสภาพแวดล้อมเฉพาะ:


- [LNbits on clearnet](https://ereignishorizont.xyz/lnbits-server/en/) โดย Axel
- [LNbits on a VPS](https://github.com/TrezorHannes/vps-lnbits) โดย Hannes
- [LNbits on cloudflare](https://www.nodeacademy.org/lnbits) โดย Leo


คุณยังสามารถค้นหาวิดีโอเกี่ยวกับ [การตั้งค่าแบบ dockerised บน VPS ด้วย PostgreSQ, LightningTipBot เป็นแหล่งเงินทุนโดยใช้ nginx](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)


[สถานการณ์การติดตั้งเพิ่มเติมที่นี่](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).


สำหรับโหนดซอฟต์แวร์แบบรวม โปรดดูเอกสารเฉพาะเกี่ยวกับ LNbits: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)


### LNbits SaaS


เมื่อคุณไม่สนใจเรื่องเทคนิคและไม่ต้องการโฮสต์แหล่งเงินทุนหรือ lnbits ด้วยตัวเอง มี [LNbits SaaS version](https://saas.lnbits.com) (Software-as-a-service) ที่คุณสามารถใช้ได้ มันเหมือนกับ LNbits ในคลาวด์ แต่คุณสามารถกำหนดแหล่งเงินทุน (เช่น Node ของคุณ, LNbits wallet, LNtipbot, fakewallet ฯลฯ) และตัวแปรสภาพแวดล้อมได้ด้วยตัวเอง ซึ่งส่วนใหญ่ไม่สามารถทำได้ในโซลูชันคลาวด์อื่น ๆ


[Here is a detailed guide how to use LNbits SaaS for specific use cases](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).


### แหล่งเงินทุน


LNbits ไม่ใช่ซอฟต์แวร์การจัดการโหนดแต่เป็นระบบบัญชีที่เน้น LN บนแหล่งเงินทุน LND หรือ CLN หลังจากการติดตั้งครั้งแรกคุณสามารถเยี่ยมชม LNbits ของคุณได้ที่ http://localhost:5000/


หากต้องการแก้ไขแหล่งเงินทุน ให้ไปที่ super-user-URL ของคุณและเลือกแหล่งเงินทุนภายใน "Manage Server" หรือแก้ไขไฟล์ .env โดยการแก้ไข `LNBITS_BACKEND_WALLET_CLASS` ให้เป็นแหล่งที่คุณต้องการหากคุณตั้งค่า `adminUI=TRUE` ใน `.env`.


คุณจะพบไฟล์ .env ภายในโฟลเดอร์ lnbits/ หรือ lnbits/apps/data โดยการขยายคำสั่งเพื่อแสดงรายการไฟล์ในไดเรกทอรีของคุณโดยใช้ `ls -a`


คุณอาจจำเป็นต้องติดตั้งแพ็กเกจเพิ่มเติมหรือดำเนินการขั้นตอนการตั้งค่าเพิ่มเติม โดยเลือกแหล่งเงินทุนที่ต้องการ หลังจากรีสตาร์ท การตั้งค่าใหม่ของคุณจะใช้งานได้


แหล่งเงินทุนใดบ้างที่ฉันสามารถใช้สำหรับ LNbits?


LNbits สามารถทำงานร่วมกับแหล่งเงินทุนของเครือข่ายสายฟ้าได้หลายแห่ง ปัจจุบันมีการรองรับ CoreLightning, LND, LNbits, LNPay, OpenNode และมีการเพิ่มแหล่งใหม่ๆ อย่างต่อเนื่อง

สิ่งสำคัญคือต้องเลือกแหล่งที่มีสภาพคล่องดีและมีเพื่อนร่วมงานที่ดีเชื่อมต่ออยู่ หากคุณใช้ LNbits สำหรับบริการสาธารณะ การชำระเงินของผู้ใช้ของคุณจะสามารถไหลได้อย่างราบรื่นในทั้งสองทิศทาง


สามารถกำหนดค่า backend wallet (แหล่งเงินทุน) โดยใช้ตัวแปรสภาพแวดล้อม LNbits ต่อไปนี้ในไฟล์ `.env` หรือภายในบัญชีผู้ใช้ระดับสูงของคุณภายใต้ส่วน Manage-Server

หากคุณต้องการใช้เวอร์ชัน .env คุณสามารถค้นหาพารามิเตอร์ได้ที่นี่:



#### CoreLightning


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /file/path/lightning-rpc
- Spark (c-lightning)
  - `LNBITS_BACKEND_WALLET_CLASS`: **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/rpc
   - `SPARK_TOKEN`: secret_access_key

#### Lightning Network Daemon


- LND (REST)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /file/path/tls.cert
  - `LND_REST_MACAROON`: /file/path/admin.macaroon หรือ Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndWallet**
  - `LND_GRPC_ENDPOINT`: ip_address
  - `LND_GRPC_PORT`: พอร์ต
  - `LND_GRPC_CERT`: /file/path/tls.cert
  - `LND_GRPC_MACAROON`: /file/path/admin.macaroon หรือ Bech64/Hex

คุณยังสามารถใช้มาการูนที่เข้ารหัสด้วย AES (ข้อมูลเพิ่มเติม) แทนโดยใช้


  - `LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

หากต้องการเข้ารหัสมาการูนของคุณ ให้รัน `./venv/bin/python lnbits/wallets/macaroon/macaroon.py`


#### LNbits (อีกกรณีหนึ่งของ LNbits)



- LNbits อินสแตนซ์โฮสต์บนเซิร์ฟเวอร์คลาวด์หรือเซิร์ฟเวอร์ภายในบ้านของคุณเอง
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- LNbits Legend Demo Server (!! ห้ามใช้เซิร์ฟเวอร์นี้สำหรับการผลิต / วัตถุประสงค์ทางการค้า ใช้สำหรับการทดสอบเท่านั้น !!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

#### Lightning TipBot


ในการเชื่อมต่อ [Lightning Tipbot](https://t.me/LightningTipBot) จาก Telegram คุณจะต้องตั้งค่าพารามิเตอร์ต่อไปนี้:


  - `LNBITS_BACKEND_WALLET_CLASS`: **LnTipsWallet**
  - `LNBITS_ENDPOINT`: https://ln.tips
  - `LNBITS_KEY`: ในการรับคีย์ คุณจะต้องเรียกใช้ /api ในการแชทส่วนตัวกับ LightningTipbot บน Telegram หนึ่งครั้ง


ดูบทแนะนำนี้เกี่ยวกับวิธีการติดตั้ง [LNbits with LightningTipBot via vps](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)


#### IBEX HUB


ลงทะเบียน [ที่นี่](https://ibexpay.ibexmercado.com/onboard) จากนั้นรับคีย์/โทเค็นของคุณจากที่นั่น, จุดเชื่อมต่อคือ https://ibexpay-api.ibexmercado.com.

ข้อมูลเพิ่มเติมดู [IBEX API-Documentation](https://ibexpay-api.readme.io/reference/getting-started-with-your-api).


#### LNPay

สำหรับการทำงานของ invoice listener คุณต้องมี URL ที่เข้าถึงได้สาธารณะใน LNbits ของคุณและต้องตั้งค่า [LNPay webhook](https://dashboard.lnpay.co/webhook/) ชี้ไปที่ `<your LNbits host>/wallet/webhook` พร้อมกับเหตุการณ์ "Wallet Receive" และไม่มีการให้ secret การตั้งค่า `https://mylnbits/wallet/webhook` จะเป็น endpoint url ที่ได้รับการแจ้งเตือนเกี่ยวกับการชำระเงินใด ๆ


  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey


#### OpenNode

สำหรับใบแจ้งหนี้ที่จะใช้งานได้ คุณจำเป็นต้องมี URL ที่เข้าถึงได้สาธารณะใน LNbits ของคุณ การตั้งค่า webhook เป็นทางเลือก


  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey


#### Alby


Alby เป็นส่วนขยายของเบราว์เซอร์ที่มีฟังก์ชันการทำงานของ LN wallet และบัญชี LNDHUB ที่สามารถใช้เป็นแหล่งเงินทุนสำหรับ LNbits ได้ [รายละเอียดเพิ่มเติมที่นี่](https://getalby.com/).


สำหรับใบแจ้งหนี้ที่จะใช้งานได้ คุณต้องมี URL ที่เข้าถึงได้สาธารณะใน LNbits ของคุณ ไม่จำเป็นต้องตั้งค่า webhook ด้วยตนเอง คุณสามารถเข้าถึง generate และ Alby token ได้ที่นี่: https://getalby.com/developer/access_tokens/new



- `LNBITS_BACKEND_WALLET_CLASS`: AlbyWallet
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken


### คู่มือเพิ่มเติม / การแก้ไขปัญหา


นี่คือคำแนะนำเพิ่มเติมในกรณีที่คุณต้องการ คลิกที่ลูกศรเพื่อขยายคำอธิบาย


#### The Killswitch 🚨


เมื่อเร็ว ๆ นี้มีบั๊กที่อันตรายมากมายไม่เพียงแต่ในพื้นที่ทั้งหมดแต่ยังใน LNbits ด้วย เราจึงตัดสินใจทำบางอย่างเกี่ยวกับเรื่องนี้ ตอนนี้คุณสามารถเลือกที่จะรับการเตือนและ/หรือดำเนินการโดยตรงเมื่อเกิดช่องโหว่หรือบั๊กที่อาจนำไปสู่การสูญเสียเงินอีกครั้ง


![killswitchn](assets/lnbits-killswitch.webp)


หากเปลี่ยนไปใช้ void-wallet ผู้ใช้ทุกประเภทในอินสแตนซ์จะเห็นแบนเนอร์สีเหลืองในตำแหน่งที่คุณมักจะพบประกาศ "LNbits is in Beta" ถัดจากพื้นที่ธีม/ภาษาไปทางขวา - และเป็นคำใบ้ที่ชัดเจนที่สุดว่ามีบางอย่างเกิดขึ้น ลองดูที่แท็บเซิร์ฟเวอร์ใหม่ของคุณที่ถูกเน้นด้วยสีเขียวในส่วนซ้ายของหน้าต่าง


มันทำงานอย่างไร? เมื่อเปิดใช้งาน killswitch แล้ว จะมีการตรวจสอบที่เก็บข้อมูลลับของ GitHub ซึ่งมีเฉพาะทีมหลักของ LNbits เท่านั้นที่สามารถเข้าถึงได้ในช่วงเวลาที่กำหนด (ซึ่งสามารถระบุได้) หากมีการเผยแพร่บั๊กที่มีช่องโหว่ในที่เก็บนี้ จะทำหน้าที่เป็นสัญญาณที่กระตุ้น killswitch ในการติดตั้งทั้งหมดที่สมัครไว้และเปลี่ยนอินสแตนซ์ lnbits ของคุณให้ใช้ void wallet หากเมฆได้เคลียร์แล้วและคุณได้ติดตั้งการอัปเดตความปลอดภัย คุณสามารถตั้งค่าแหล่งเงินทุนของคุณไปยังโหนดของคุณ, wallet หรืออะไรก็ตามที่คุณใช้อีกครั้งผ่านทางส่วนจัดการเซิร์ฟเวอร์ วิกินี้มีส่วนเกี่ยวกับการเปลี่ยนแหล่งเงินทุนหากคุณไม่ทราบว่าจะกำหนดค่าอะไร



#### ความแตกต่างระหว่างผู้ดูแลระบบและผู้ใช้ระดับสูง


LNbits Admin UI ช่วยให้คุณเปลี่ยนการตั้งค่า LNbits ผ่านทางส่วนหน้าของ LNbits โดยค่าเริ่มต้นจะถูกปิดใช้งาน และครั้งแรกที่คุณตั้งค่าตัวแปรสภาพแวดล้อม `LNBITS_ADMIN_UI=true` ในไฟล์ `.env` การตั้งค่าจะถูกเริ่มต้นและจะถูกใช้งาน จากนั้นการตั้งค่าที่เกี่ยวข้องจากฐานข้อมูลจะถูกใช้แทนที่การตั้งค่าในไฟล์ .env


#### ซุปเปอร์ยูสเซอร์


ด้วย Admin UI เราได้แนะนำ super user ซึ่งมีสิทธิ์เข้าถึงเซิร์ฟเวอร์ ดังนั้นสามารถเปลี่ยนการตั้งค่าที่อาจทำให้เซิร์ฟเวอร์ขัดข้องหรือไม่ตอบสนองผ่าน frontend และ api เช่น การเปลี่ยนแหล่งเงินทุน super user จะถูกเก็บไว้เฉพาะในตารางการตั้งค่าของฐานข้อมูลเท่านั้น หลังจากที่การตั้งค่า "รีเซ็ตเป็นค่าเริ่มต้น" และเริ่มต้นใหม่ super user ใหม่จะถูกสร้างขึ้น เราได้เพิ่มตัวตกแต่งสำหรับเส้นทาง API เพื่อตรวจสอบการมีอยู่ของ super user ID ของมันจะไม่ถูกส่งผ่าน api และ frontend และจะได้รับเพียงค่า bool (ใช่/ไม่ใช่) ว่าคุณเป็น super user หรือไม่


เฉพาะผู้ใช้ระดับสูงเท่านั้นที่ได้รับอนุญาตให้ brrrr satoshis ไปยังวอลเล็ตต่าง ๆ ผ่านส่วน "เติมเงิน"


คุณสามารถโพสต์ผู้ใช้ระดับสูงผ่าน webhook ไปยังบริการอื่นเมื่อมันถูกสร้างขึ้น ข้อมูลเพิ่มเติมที่นี่ https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`


ในส่วนหน้าของคุณ คุณจะพบกับความสามารถในการเปลี่ยนภาพร้านค้าที่แสดงในหน้า "สร้าง wallet" โดยการเปิดส่วนจัดการเซิร์ฟเวอร์และเลือก ธีม -> โลโก้ที่กำหนดเอง


#### ผู้ดูแลระบบ


ตัวแปรสภาพแวดล้อม: `LNBITS_ADMIN_USERS`, รายการ ID ผู้ใช้ที่คั่นด้วยเครื่องหมายจุลภาค ผู้ดูแลระบบสามารถเปลี่ยนการตั้งค่าในอินเทอร์เฟซผู้ดูแลระบบ - ยกเว้นการตั้งค่าแหล่งเงินทุน เนื่องจากจะต้องรีสตาร์ทเซิร์ฟเวอร์และอาจทำให้เซิร์ฟเวอร์ไม่สามารถเข้าถึงได้ นอกจากนี้พวกเขายังสามารถเข้าถึงส่วนขยายทั้งหมดที่อุทิศให้กับพวกเขาใน `LNBITS_ADMIN_EXTENSIONS`


#### ผู้ใช้ที่ได้รับอนุญาต


ตัวแปรสภาพแวดล้อม: `LNBITS_ALLOWED_USERS`, รายการ ID ผู้ใช้ที่คั่นด้วยเครื่องหมายจุลภาค โดยการกำหนดผู้ใช้เหล่านี้ LNbits จะไม่สามารถใช้งานได้โดยสาธารณะ ผู้ใช้ที่กำหนดและผู้ดูแลระบบเท่านั้นที่สามารถเข้าถึงส่วนหน้าของ LNbits ได้




##### อัปเดต LNbits

การอัปเดตปกติของอินสแตนซ์ LNbits ในเครื่องของคุณทำได้ง่ายๆ โดยการคัดลอกและวางคำสั่ง CLI ต่อไปนี้:


```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```


หากคุณใช้ Raspiblitz หรือ MyNode คุณอาจต้องการเพิ่มเติม

```
sudo systemctl restart lnbits
```

ในตอนท้าย เพราะมันรัน LNbits เป็นบริการ


บน Umbrel/Citadel คำสั่งจะเป็น

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```


##### การย้ายข้อมูลจาก SQLite ไปยัง PostgreSQL


หากคุณได้ติดตั้งและใช้งาน LNbits บนฐานข้อมูล SQLite แล้ว เราขอแนะนำอย่างยิ่งให้ย้ายไปใช้ Postgres หากคุณวางแผนที่จะใช้งาน LNbits ในขนาดใหญ่


มีสคริปต์ที่รวมอยู่ซึ่งสามารถทำการย้ายข้อมูลได้อย่างง่ายดาย คุณจำเป็นต้องติดตั้ง Postgres ไว้แล้วและควรมีรหัสผ่านสำหรับผู้ใช้ (ดูคู่มือการติดตั้ง Postgres ด้านบน) นอกจากนี้ อินสแตนซ์ LNbits ของคุณจำเป็นต้องรันบน postgres หนึ่งครั้งเพื่อดำเนินการโครงสร้างฐานข้อมูลก่อนที่การย้ายข้อมูลจะทำงานได้:


```
# STOP LNbits

# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit

# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

หวังว่าตอนนี้ทุกอย่างจะทำงานและถูกย้ายข้อมูล... เปิดตัว LNbits อีกครั้งและตรวจสอบว่าทุกอย่างทำงานอย่างถูกต้องหรือไม่



##### การสำรองและกู้คืนฐานข้อมูล


โปรดดู [คู่มือที่ละเอียดมากเกี่ยวกับกระบวนการสำรองและกู้คืน](https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore)



##### การระดมทุน LNbits wallet จากโหนดของฉันไม่ทำงาน


หากคุณต้องการส่ง sats จากโหนดเดียวกันที่เป็นแหล่งเงินทุนของ LNbits ของคุณ คุณจะต้องแก้ไขไฟล์ lnd.conf


พารามิเตอร์ที่จะรวมคือ: `allow-circular-route=1`


โปรดทำเช่นนั้นในส่วนตัวเลือกการใช้งานของ lnd.conf ของคุณ ในบางโหนดรวมการเริ่มต้นของ LND อาจล้มเหลวหากไม่ทำเช่นนั้น


หมายเหตุ: ขอแนะนำให้ใช้ส่วนขยาย adminUI ใหม่พร้อมตัวเลือก "TopUp" เพื่อเพิ่มเงินในบัญชี LNbits แทน


##### ข้อผิดพลาด 426

ฉันได้รับข้อผิดพลาด: "lnurl needs to be delivered over publically accessible https domain or tor. 426 upgrade required"


ข้อผิดพลาดนี้มักเกิดขึ้นเนื่องจาก LNbits ของคุณที่อยู่เบื้องหลัง ngnix tunnel ไม่ได้ส่งต่อที่อยู่ LNURL อย่างถูกต้อง หยุด LNbits ของคุณและแก้ไขไฟล์ .env โดยเพิ่มบรรทัดนี้:

`FORWARDED_ALLOW_IPS=*`


นอกจากนี้หากคุณใช้การตั้งค่า ngnix อย่าลืมใส่ headers เหล่านี้ใน config ของ ngnix:


```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```


##### ข้อผิดพลาดของเครือข่าย

ฉันได้รับ "https error", "network error" หรือข้อผิดพลาดอื่นๆ เมื่อสแกน QR</summary>


ข่าวร้าย นี่เป็นข้อผิดพลาดในการกำหนดเส้นทางที่อาจมีสาเหตุหลายประการ ก่อนอื่นตรวจสอบ LNURL ของ QR ด้วย [Lightning Decoder](https://lightningdecoder.com/) ว่าคุณสามารถหาสิ่งที่แปลกในนั้นได้หรือไม่ ลองมาดูปัญหาที่เป็นไปได้มากที่สุดและวิธีแก้ไขของพวกมันกันเถอะ


LNbits กำลังทำงานผ่าน Tor เท่านั้น คุณไม่สามารถเปิดมันบนโดเมนสาธารณะเช่น lnbits.yourdomain.com



- เนื่องจากคุณต้องการให้การตั้งค่าของคุณคงอยู่เช่นนี้ ให้เปิด LNbits wallet ของคุณโดยใช้ .onion URI และสร้างมันขึ้นมาใหม่ ด้วยวิธีนี้ QR จะถูกสร้างขึ้นเพื่อให้สามารถเข้าถึงได้ผ่าน .onion URI ดังนั้นจึงผ่าน tor เท่านั้น อย่า generate QR นั้นจาก .local URI เพราะมันจะไม่สามารถเข้าถึงได้ผ่านอินเทอร์เน็ต - เฉพาะจากภายใน home-LAN ของคุณเท่านั้น
- เปิดแอป LN wallet ของคุณที่คุณใช้สแกน QR นั้น และคราวนี้ให้ใช้ tor (ดูการตั้งค่าแอป wallet) หากแอปไม่รองรับ tor คุณสามารถใช้ Orbot (Android) แทนได้ ดูส่วนการติดตั้งสำหรับคำแนะนำโดยละเอียดเกี่ยวกับวิธีเปิด LNbits ของคุณสำหรับ clearnet/https



##### ป้องกันผู้อื่นจากการสร้างกระเป๋าเงินบน LNbits ของฉัน


เมื่อคุณใช้งาน LNbits ของคุณใน clearnet โดยพื้นฐานแล้วทุกคนสามารถ generate a wallet บนมันได้ เนื่องจากเงินทุนของโหนดของคุณถูกผูกกับกระเป๋าเงินเหล่านี้ คุณอาจต้องการป้องกันสิ่งนั้น มีสองวิธีในการทำเช่นนั้น:


กำหนดค่าผู้ใช้และส่วนขยายที่อนุญาตในไฟล์ `.env` ([ดูตัวอย่าง env ที่นี่](https://github.com/lnbits/lnbits/blob/main/.env.example)) สิ่งนี้จะทำงานได้เฉพาะเมื่อคุณใช้การตั้งค่า `adminUI=FALSE` ใน .env มิฉะนั้นคุณจำเป็นต้องทำในส่วนจัดการเซิร์ฟเวอร์ -> ผู้ใช้ -> ผู้ใช้ที่อนุญาต ทุกคนอื่นจะไม่ได้รับอนุญาตหลังจากนั้น




##### ปรับแต่งระยะเวลาหมดอายุของใบแจ้งหนี้


ตอนนี้คุณสามารถ generate ใบแจ้งหนี้พร้อมวันหมดอายุที่กำหนดเองได้แล้ว เข้ากันได้กับแบ็กเอนด์: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet จนถึงตอนนี้!


คุณสามารถตั้งค่า `LIGHTNING_INVOICE_EXPIRY` ในไฟล์ .env ของคุณหรือใช้ AdminUI เพื่อเปลี่ยนค่าเริ่มต้นสำหรับใบแจ้งหนี้ทั้งหมด นอกจากนี้ยังมีฟิลด์ใหม่ใน endpoint /api/v1/payments ที่คุณสามารถตั้งค่าหมดอายุในข้อมูล JSON ได้อีกด้วย




### Wallet-URL ถูกลบ


#### Wallet บนเซิร์ฟเวอร์สาธิต legend.lnbits


โปรดบันทึกสำเนาของ wallet-URL, Export2phone-QR หรือ LNDhub สำหรับกระเป๋าเงินของคุณในที่ปลอดภัยเสมอ LNbits ไม่สามารถช่วยคุณกู้คืนได้เมื่อสูญหาย


#### Wallet บนแหล่งเงินทุน/โหนดของคุณเอง

Always save a copy of your wallet-URL, Export2phone-QR or LNDhub for your own wallets in a safe place. You can find all LNbits users and wallet-IDs in your LNbits user manager extension or in your sqlite database. To edit or read the LNbits database, go to the LNbits /data folder and look for the file called sqlite.db. You can open and edit it with excel or with a dedicated SQL-Editor like [SQLite browser](https://sqlitebrowser.org/).


คุณยังสามารถดัมพ์กระเป๋าเงินผ่าน cli และดูทุก wallet ภายในฐานข้อมูลของคุณได้


```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```


เอาต์พุตจะมีลักษณะประมาณนี้


```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

และคุณต้องการใส่ค่าเหล่านี้ลงใน URL เช่นนี้


```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```


โดยที่คุณแทนที่ f8a43fc363ea428db5c53b3559935f1f ด้วยค่าที่มาก่อนชื่อ (ในตัวอย่างของเรา f8a43fc363ea428db5c53b3559935f1f) และ 1280ff5910a9c485a782a2376f338b6c คือผู้ใช้ของคุณและควรกลายเป็นค่าที่แสดงหลังชื่อ ในการออกจาก sqlite3 ให้ใส่


```
.quit
```

##### LNURL สำหรับที่อยู่ lightning ตรงกันข้าม


ลองใช้ [encoder](https://lnurl-codec.netlify.app/) จาก fiatjaf หรือ [อันนี้](https://lightningdecoder.com/). สำหรับการจ่ายหรือเช็ค LNURLp คุณสามารถใช้ [LNurlpay](https://wwww.lnurlpay.com/) ได้เช่นกัน ควรระบุว่าเป็น HTTPS ไม่ใช่ HTTP.



##### กำหนดความคิดเห็นที่ผู้คนจะเห็นเมื่อชำระเงินไปยัง LNURLp QR ของฉัน

เมื่อคุณสร้าง LNURL-p โดยค่าเริ่มต้นกล่องความคิดเห็นจะไม่ถูกเติม นั่นหมายความว่าไม่อนุญาตให้แนบความคิดเห็นกับการชำระเงิน


เพื่อให้สามารถแสดงความคิดเห็นได้ ให้เพิ่มความยาวของกล่องตัวอักษร ตั้งแต่ 1 ถึง 250 เมื่อคุณใส่ตัวเลขลงไป กล่องแสดงความคิดเห็นจะปรากฏในกระบวนการชำระเงิน คุณยังสามารถแก้ไข LNURL-p ที่สร้างไว้แล้วและเพิ่มตัวเลขนั้นได้


![lnbits comments](assets/lnbits-comments.webp)


##### ฝาก BTC บนเชนไปยัง LNbits

มีสองวิธีในการแลกเปลี่ยน sats จาก onchain BTC เป็น LN BTC (หรือ LNbits)


###### ผ่านบริการแลกเปลี่ยนภายนอก


ผู้ใช้รายอื่นที่ไม่มีสิทธิ์เข้าถึง LNb ของคุณสามารถใช้บริการแลกเปลี่ยนเช่น [Boltz](https://boltz.exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) หรือ [ZigZag](https://zigzag.io/) ได้ นี่เป็นประโยชน์หากคุณให้เฉพาะใบแจ้งหนี้ LNURL/LN จากอินสแตนซ์ LNbits ของคุณ แต่ผู้ชำระเงินมีเพียง onchain sats ดังนั้นพวกเขาจะต้องแลกเปลี่ยน sats เหล่านั้นก่อนในฝั่งของพวกเขา ขั้นตอนง่าย ๆ: ผู้ใช้ส่ง btc onchain ไปยังบริการแลกเปลี่ยนและให้ใบแจ้งหนี้ LNURL / LN จาก LNbits เป็นปลายทางของการแลกเปลี่ยน


###### ใช้ส่วนขยาย Onchain และ Boltz LNbits


โปรดทราบว่านี่คือ wallet แยกต่างหาก ไม่ใช่ LN btc ที่แสดงโดย LNbits ว่าเป็น "wallet ของคุณ" บนแหล่งเงินทุน LN ของคุณ wallet บนเชนนี้ยังสามารถใช้เพื่อสลับ LN btc ไปยัง (เช่น hardwarewallet ของคุณ) โดยใช้ส่วนขยาย LNbits Boltz หรือ Deezy หากคุณดำเนินการเว็บช็อปที่เชื่อมโยงกับ LNbits ของคุณสำหรับการชำระเงิน LN จะเป็นประโยชน์มากในการระบาย sats ทั้งหมดจาก LN เป็นประจำเข้าสู่บนเชน ซึ่งจะนำไปสู่พื้นที่เพิ่มเติมในช่อง LN ของคุณเพื่อให้สามารถรับ sats ใหม่สดได้


ขั้นตอนสำหรับผู้ที่ไม่มีฮาร์ดแวร์บิตคอยน์ wallet:



- ใช้ Electrum หรือ Sparrow wallet เพื่อสร้าง wallet ใหม่บนเชนและบันทึกสำรอง seed ในที่ปลอดภัย
- ไปที่ข้อมูล wallet และคัดลอก xpub.
- ไปที่ LNbits - ส่วนขยาย Onchain และสร้าง wallet แบบ watch-only ใหม่ด้วย xpub นั้น
- ไปที่ LNbits - ส่วนขยาย Tipjar และสร้าง Tipjar ใหม่ เลือกตัวเลือก onchain นอกเหนือจาก LN wallet
- ตัวเลือก - ไปที่ LNbits - ส่วนขยาย SatsPay และสร้างการเรียกเก็บเงินใหม่สำหรับ onchain btc คุณสามารถเลือกได้ระหว่าง onchain และ LN หรือทั้งสองอย่าง จากนั้นจะสร้างใบแจ้งหนี้ที่สามารถแชร์ได้
- ไม่บังคับ - หากคุณใช้ LNbits ของคุณที่เชื่อมโยงกับหน้า Wordpress + Woocommerce เมื่อคุณสร้าง/เชื่อมโยง wallet แบบดูอย่างเดียวกับร้านค้า btc LN ของคุณ ลูกค้าจะมีตัวเลือกทั้งสองในการชำระเงินบนหน้าจอเดียวกัน


เมื่อคุณได้รับการชำระเงินใน LNbits บันทึกธุรกรรมจะแสดงเฉพาะประเภทที่สรุปของธุรกรรมเท่านั้น


![lnbits payment details](assets/lnbits-payment-details.webp)


ในภาพรวมการทำธุรกรรมของคุณ คุณจะพบลูกศรสีเขียวเล็ก ๆ สำหรับเงินที่ได้รับและลูกศรสีแดงสำหรับเงินที่ถูกส่งออกไป


หากคุณคลิกที่ลูกศรเหล่านั้น หน้าต่างป๊อปอัพรายละเอียดจะแสดงข้อความที่แนบมารวมถึงชื่อผู้ส่งหากมีการระบุไว้


ในการกำหนดชื่อให้ปรากฏภายในการชำระเงิน ใน LNbits ขณะนี้ยังไม่สามารถทำได้ - แต่สามารถรับได้ ซึ่งจะเป็นไปได้ก็ต่อเมื่อ LN wallet ของผู้ส่งรองรับ [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) เช่น [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents)


จากนั้นคุณจะเห็นนามแฝง/ชื่อปลอมในส่วนรายละเอียดของธุรกรรม LNbits ของคุณ (คลิกที่ลูกศร) โปรดทราบว่าคุณสามารถใส่ชื่อใดก็ได้ที่นั่น และอาจไม่เกี่ยวข้องกับชื่อผู้ส่งจริงหากคุณได้รับเช่นนั้น


![lnbits namedesc](assets/lnbits-namedesc.webp)


ในการนำเข้าบัญชี LNbits ของคุณในแอป wallet ให้เปิด LNbits ของคุณด้วยบัญชี / wallet ที่คุณต้องการใช้ ไปที่ "จัดการส่วนขยาย" และเปิดใช้งานส่วนขยาย LNDHUB เปิดส่วนขยาย LNDHUB เลือก wallet ที่คุณต้องการใช้และสแกน QR "admin" หรือ "invoice only" ขึ้นอยู่กับระดับความปลอดภัยที่คุณต้องการสำหรับ wallet นั้น


คุณสามารถใช้ [Zeus](https://zeusln.app/) หรือ [Bluewallet](https://bluewallet.io/) เป็นแอป wallet สำหรับบัญชี lndhub โดยที่ BW รองรับ wallet มากกว่าหนึ่งบัญชี


เมื่อทำเช่นนี้ เราแนะนำให้ตั้งค่า LN network URI ให้เป็นของโหนดของคุณเองด้วย หากอินสแตนซ์ LNbits ของคุณเป็น Tor เท่านั้น คุณจะต้องใช้แอปเหล่านั้นโดยเปิดใช้งาน Tor ด้วย ในกรณีนี้คุณจำเป็นต้องเปิดหน้า LNbits ผ่านที่อยู่ Tor .onion ของคุณ


หากคุณพบข้อผิดพลาด "unsupported hash type" เมื่อใช้ ypub ในส่วนขยาย On-chain ให้ตรวจสอบว่าอินสแตนซ์ LNbits ของคุณใช้ python 3.10 หรือไม่ อาจได้รับผลกระทบจาก [ปัญหานี้](https://stackoverflow.com/questions/72409563/unsupported-hash-type-ripemd160-with-hashlib-in-python) แก้ไข openssl.cnf ตามที่อธิบายไว้ในคำตอบของ stackoverflow และรีสตาร์ท LNbits ของคุณ



### เครื่องมือและการสร้างด้วย LNbits


LNbits มี [open APIs](https://legend.lnbits.com/docs) และเครื่องมือต่าง ๆ สำหรับการเขียนโปรแกรมและเชื่อมต่อกับอุปกรณ์หลากหลายประเภทสำหรับการใช้งานที่หลากหลายมากมาย


เมื่อคุณเริ่มต้นสร้างใหม่ ให้เริ่มต้นด้วย [MakerBits presentations](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) จาก Ben Arc เกี่ยวกับการสร้างอุปกรณ์ตาม LNbits


#### สำคัญ:


- LNbits ทำงานตามโปรโตคอล LNURL ซึ่งคำขอจะถูกต้องในสองรูปแบบ: ไม่ว่าจะเป็นลิงก์ https://clearnet (ไม่อนุญาตให้ใช้ใบรับรองที่ลงนามด้วยตนเอง) หรือเป็นลิงก์ http://v2/v3 onion หากต้องการให้บริการ LNbits เช่น LNURLp/w รหัส QR หรือบัตร NFC ที่สามารถใช้ในที่สาธารณะได้ คุณจะต้องเปิด LNbits ไปยัง clearnet (https)
- ใช้เฉพาะสาย DATA-Cables เพื่อจ่ายไฟให้กับ esp32 ของคุณ ไม่ใช่ทุกสายที่รองรับข้อมูลนอกเหนือจากการจ่ายไฟให้กับ esp คุณจะไม่ใช่คนแรกหากสายที่มาพร้อมกับ esp เป็นสายที่จ่ายไฟเท่านั้น
- อย่าใช้ USB-Hub ร่วมกับอุปกรณ์อื่น ๆ ที่เชื่อมต่ออยู่ เพราะอาจทำให้เกิดผลกระทบแปลก ๆ ที่ยากต่อการแก้ไข (เช่น ไม่เริ่มต้นหรือหยุดทำงาน)
- ในการใช้งานโครงการ esp กับ MacOS คุณจะต้องมี UART Bridge Driver หากคุณมีปัญหากับไดรเวอร์บนระบบ Mac หรือ Linux คุณสามารถหาได้ที่นี่ หรือหากมีการใช้ TTGO Display ให้ใช้ตัวนี้ หากคุณใช้ Windows และมีปัญหาในการเชื่อมต่อ ให้แน่ใจว่าดาวน์โหลดเวอร์ชันเก่า 11.1.0 เพราะเวอร์ชันใหม่ไม่ทำงาน! คุณยังสามารถหา serial terminal ได้ที่นี่เพื่อตรวจสอบการเชื่อมต่อของคุณ - ตั้งค่าเป็น baudrate 115200
- แม้ว่าจะสะดวกสบายกว่ามากในการใช้ Platform.io (เช่น การติดตั้ง dependencies จะทำโดยอัตโนมัติ) เราขอแนะนำให้ใช้ Arduino สำหรับทุกคนที่เริ่มต้นสร้างใหม่
- TT-Go Display S3: สีของแท็บบนฟิล์มกันรอยหน้าจอจะบอกคุณว่าคอนโทรลเลอร์ตัวไหน (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ..) ถูกใช้ในการสร้างมันขึ้นมา เก็บไว้เพื่อให้สามารถดีบักได้หากคุณเขียนโปรแกรมเองและหน้าจอไม่แสดงกราฟิกอย่างถูกต้อง เช่น สีผิด ภาพสะท้อน หรือพิกเซลหลงที่ขอบ หากคุณจำเป็นต้องทำเช่นนี้ มีคู่มือที่ยอดเยี่ยมเกี่ยวกับการปรับสำหรับหน้าจอที่แตกต่างกัน
- ใช้ lnurl239xx ตัวพิมพ์เล็กเสมอแทนที่จะเป็น LNURLl239xx
- การเพิ่ม lightning:lnurl1234xyz จะสร้าง QR ที่ร้องขอให้เปิด wallet ของผู้ใช้สำหรับใบแจ้งหนี้นี้เมื่อสแกน (แอป lightning ที่ติดตั้งล่าสุดบน iOS, การตั้งค่าใน Android)
- หากคุณกำลังแฟลช esp32 ผ่านเว็บจะทำงานได้เฉพาะกับเบราว์เซอร์เหล่านี้ (TL:DR Chrome, Edge & Opera)
- โปรดทราบข้อมูลอ้างอิง PIN-OUT สำหรับ esp
- เมื่อคุณใช้ FOSSoftware หรือ FOSGuides กรุณาเชื่อมโยงผู้เขียนเสมอ ทุกคนชอบที่จะเห็นผลงานของพวกเขาเติบโตขึ้น และมันยังเริ่มต้นห่วงโซ่การสร้างที่น่าทึ่งให้ได้ชมอีกด้วย :)


มาเข้าร่วม [Makerbits Telegram Group](https://t.me/makerbits) หากคุณต้องการความช่วยเหลือเกี่ยวกับโปรเจกต์ - เราพร้อมช่วยคุณ!


![lnbits hackathlon](assets/lnbits-hackathlon.webp)


นี่คือหมวดหมู่โครงการที่คุณสามารถสร้างด้วย LNbits:



- [Nostr Signing Device](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [เครื่องอาร์เคด](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Nostr Zap Lamp](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware Wallet](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-switch)
- [เครื่องจำหน่ายสินค้าอัตโนมัติ](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora and Mesh Networking](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)



- [HELPERS & RESOURCES](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [ตัวอย่างเพิ่มเติมของโครงการ "Powered by LNbits" ที่นี่](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [Use cases for LNbits](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)