---
name: Lightning Watchtower
description: การทำความเข้าใจและการใช้ Watchtower บนโหนด Lightning ของคุณ
---
![cover](assets/cover.webp)



## หอคอยเฝ้าระวังทำงานอย่างไร?



ส่วนสำคัญของระบบนิเวศ Lightning Network, _Watchtowers_ มอบระดับการป้องกันเพิ่มเติมสำหรับช่องทาง Lightning ของผู้ใช้ บทบาทหลักของพวกเขาคือการตรวจสอบสถานะของช่องทางและแทรกแซงหากฝ่ายหนึ่งของช่องทางพยายามฉ้อโกงอีกฝ่าย



Watchtower จะสามารถระบุได้อย่างไรว่าช่องทางถูกละเมิดหรือไม่? มันได้รับข้อมูลจากลูกค้า (หนึ่งในฝ่ายของช่องทาง) ที่จำเป็นในการระบุและจัดการกับการละเมิดใด ๆ อย่างถูกต้อง ข้อมูลนี้รวมถึงรายละเอียดของธุรกรรมล่าสุด สถานะปัจจุบันของช่องทาง และองค์ประกอบที่จำเป็นในการสร้างธุรกรรมลงโทษ ก่อนที่จะส่งข้อมูลนี้ไปยัง Watchtower ลูกค้าสามารถเข้ารหัสข้อมูลเพื่อรักษาความลับได้ ดังนั้น แม้ว่า Watchtower จะได้รับข้อมูล มันจะไม่สามารถถอดรหัสได้จนกว่าจะเกิดการละเมิดจริง กลไกการเข้ารหัสนี้ปกป้องความเป็นส่วนตัวของลูกค้าและป้องกันไม่ให้ Watchtower เข้าถึงข้อมูลที่ละเอียดอ่อนโดยไม่ได้รับอนุญาต



ในบทแนะนำนี้ เราจะมาดู 3 วิธีในการใช้ **Watchtower** :




- ก่อนอื่น วิธีการดิบแบบคลาสสิกผ่าน LND,
- จากนั้นใช้วิธีการอื่นด้วย Eye of Satoshi,
- และสุดท้าย การกำหนดค่าที่เรียบง่ายของ Watchtower บนโหนด Lightning ของคุณที่โฮสต์ด้วย Umbrel



## 1 - การกำหนดค่า Watchtower หรือไคลเอนต์ผ่าน LND



*บทแนะนำนี้นำมาจาก [เอกสารทางการของ LND](https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md) อาจมีการเปลี่ยนแปลงบางอย่างจากเวอร์ชันต้นฉบับ



ตั้งแต่ v0.7.0, `LND` สนับสนุนการดำเนินการของ Watchtower ที่มีความเอื้อเฟื้อเผื่อแผ่ในฐานะระบบย่อยที่ผสานรวมอย่างเต็มที่ของ `LND` หอคอยเฝ้าระวังให้การป้องกันชั้นที่สองต่อสถานการณ์การละเมิดที่เป็นอันตรายหรือโดยบังเอิญเมื่อโหนดของลูกค้าออฟไลน์หรือไม่สามารถตอบสนองในเวลาที่เกิดการละเมิด ซึ่งให้ระดับความปลอดภัยที่เพิ่มขึ้นสำหรับเงินทุนในช่องทาง



ต่างจาก _หอคอยเฝ้าระวังแบบให้รางวัล_ ซึ่งต้องการส่วนแบ่งจากเงินทุนของช่องทางเพื่อแลกกับการให้บริการ _หอคอยเฝ้าระวังแบบเสียสละ_ จะคืนเงินทั้งหมดของเหยื่อ (หักค่าธรรมเนียม On-Chain) โดยไม่คิดค่าคอมมิชชั่น หอคอยเฝ้าระวังแบบให้รางวัลจะถูกเปิดใช้งานในเวอร์ชันถัดไป; ขณะนี้ยังอยู่ในขั้นตอนการทดสอบและปรับปรุง



นอกจากนี้ `LND` สามารถกำหนดค่าให้ทำงานเป็น _watchtower client_ ได้แล้ว โดยจะบันทึกธุรกรรมการแก้ไขการละเมิดที่เข้ารหัส (เรียกว่า "justice transactions") จาก watchtowers ที่มีความเสียสละอื่น ๆ Watchtower จะเก็บ blobs ที่เข้ารหัสขนาดคงที่และสามารถถอดรหัสและเผยแพร่ธุรกรรมความยุติธรรมได้หลังจากที่ฝ่ายที่กระทำผิดได้เผยแพร่สถานะ Commitment ที่ถูกเพิกถอนแล้ว การสื่อสารระหว่างลูกค้า ↔ Watchtower จะถูกเข้ารหัสและรับรองความถูกต้องโดยใช้คู่กุญแจชั่วคราว ซึ่งจำกัดความสามารถของ Watchtower ในการติดตามลูกค้าผ่านข้อมูลประจำตัวระยะยาว



โปรดทราบว่าเราได้เลือกที่จะปรับใช้ในรุ่นนี้ด้วยชุดคุณสมบัติที่จำกัดซึ่งให้ความปลอดภัยที่สำคัญสำหรับผู้ใช้ `LND` คุณสมบัติอื่นๆ ที่เกี่ยวข้องกับหอคอยหลายอย่างใกล้จะเสร็จสมบูรณ์หรือก้าวหน้าไปมากแล้ว เราจะดำเนินการส่งมอบต่อไปเมื่อเราทดสอบพวกเขา และทันทีที่พวกเขาถูกพิจารณาว่าปลอดภัย



หมายเหตุ: ในขณะนี้ หอคอยเฝ้าระวังจะบันทึกเฉพาะเอาต์พุต `to_local` และ `to_remote` ของข้อผูกพันที่ถูกเพิกถอน; การบันทึกเอาต์พุต HTLC จะถูกนำมาใช้ในเวอร์ชันอนาคต เนื่องจากโปรโตคอลสามารถขยายเพื่อรวมข้อมูลลายเซ็นเพิ่มเติมในบล็อบที่เข้ารหัสได้



### กำลังตั้งค่า Watchtower



ในการตั้งค่า Watchtower ผู้ใช้บรรทัดคำสั่งจำเป็นต้องคอมไพล์เซิร์ฟเวอร์ย่อย `watchtowerrpc` ซึ่งเป็นทางเลือก ซึ่งช่วยให้สามารถโต้ตอบกับ Watchtower ผ่าน gRPC หรือ `lncli` ไฟล์ไบนารีที่เผยแพร่จะรวมเซิร์ฟเวอร์ย่อย `watchtowerrpc` โดยค่าเริ่มต้น



การกำหนดค่าขั้นต่ำเพื่อเปิดใช้งาน Watchtower คือ `Watchtower.active=1`.



คุณสามารถดึงข้อมูลการกำหนดค่า Watchtower ของคุณได้ด้วย `lncli tower info` :



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



ชุดตัวเลือกการกำหนดค่า Watchtower ทั้งหมดสามารถดูได้ผ่าน `LND -h` :



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### อินเทอร์เฟซการฟัง



ตามค่าเริ่มต้น Watchtower จะฟังที่ `:9911` ซึ่งสอดคล้องกับพอร์ต `9911` บนอินเทอร์เฟซที่มีอยู่ทั้งหมด ผู้ใช้สามารถกำหนดอินเทอร์เฟซการฟังของตนเองผ่านตัวเลือก `--Watchtower.listen=` คุณสามารถตรวจสอบการกำหนดค่าของคุณในฟิลด์ `"listeners"` ของ `lncli tower info` หากคุณมีปัญหาในการเชื่อมต่อกับ Watchtower ให้แน่ใจว่า `<port>` เปิดอยู่หรือพร็อกซีของคุณถูกกำหนดค่าอย่างถูกต้องไปยัง Interface ที่ใช้งานอยู่



#### ที่อยู่ IP ภายนอก



ผู้ใช้ยังสามารถระบุที่อยู่ IP ภายนอกของ Watchtower ด้วย `Watchtower.externalip=` ซึ่งจะเปิดเผย URI เต็มรูปแบบของ Watchtower (pubkey@host:port) ผ่านทาง RPC หรือ `lncli tower info` :



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



Watchtower URIs สามารถสื่อสารให้ลูกค้าเชื่อมต่อและใช้งานได้ด้วยคำสั่งต่อไปนี้:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



หากลูกค้า Watchtower ต้องการเข้าถึงจากระยะไกล โปรดตรวจสอบให้แน่ใจว่า :




- เปิดพอร์ต 9911 (หรือพอร์ตที่กำหนดผ่าน `Watchtower.listen`)
- ใช้พร็อกซีเพื่อเปลี่ยนเส้นทางการรับส่งข้อมูลจากพอร์ตที่เปิดไปยังที่อยู่รับฟังของ Watchtower



#### บริการซ่อนเร้นของ Tor



หอคอยเฝ้าระวังสนับสนุนบริการที่ซ่อนของ Tor และสามารถ generate ได้โดยอัตโนมัติเมื่อเริ่มต้นด้วยตัวเลือกต่อไปนี้:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



ที่อยู่ .onion จะปรากฏในฟิลด์ `"uris"` ระหว่างการสอบถาม `lncli tower info`:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



หมายเหตุ: คีย์สาธารณะ Watchtower แตกต่างจากคีย์สาธารณะของโหนด `LND` ในขณะนี้ มันทำหน้าที่เป็น "soft whitelist" เนื่องจากลูกค้าจำเป็นต้องทราบคีย์สาธารณะของ Watchtower เพื่อใช้เป็นข้อมูลสำรอง รอการพัฒนากลไกการอนุญาตขั้นสูงเพิ่มเติม เราแนะนำว่าอย่าเปิดเผยคีย์สาธารณะนี้อย่างเปิดเผย เว้นแต่คุณจะเตรียมพร้อมที่จะเปิดเผย Watchtower ของคุณต่ออินเทอร์เน็ตทั้งหมด._



#### ไดเรกทอรีฐานข้อมูล Watchtower



ฐานข้อมูล Watchtower สามารถย้ายได้โดยใช้ตัวเลือก `Watchtower.towerdir=` โปรดทราบว่าจะมีการเพิ่มคำต่อท้าย `/Bitcoin/Mainnet/Watchtower.db` ไปยังเส้นทางที่เลือกเพื่อแยกฐานข้อมูลตามสตริง ดังนั้น การตั้งค่า `Watchtower.towerdir=/path/to/towerdir` จะสร้างฐานข้อมูลที่ `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`



ภายใต้ระบบ Linux ตัวอย่างเช่น ฐานข้อมูลเริ่มต้นของ Watchtower จะอยู่ที่ :


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### กำลังกำหนดค่าลูกค้า Watchtower



ในการกำหนดค่าไคลเอนต์ Watchtower คุณต้องมีสองรายการ:





- เปิดใช้งานไคลเอนต์ Watchtower ด้วยตัวเลือก `--wtclient.active`



```shell
$  lnd --wtclient.active
```





- URI ของ Watchtower ที่ใช้งานอยู่



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



คุณสามารถกำหนดค่าหอคอยเฝ้าระวังหลายแห่งในลักษณะนี้ได้



#### อัตราค่าธรรมเนียมสำหรับธุรกรรมทางกฎหมาย



ผู้ใช้สามารถตั้งค่าอัตราค่าธรรมเนียมสำหรับการทำธุรกรรมยุติธรรมได้โดยใช้ตัวเลือก `wtclient.sweep-fee-rate` ซึ่งรับค่าเป็น sat/byte ค่าเริ่มต้นคือ 10 sat/byte แต่สามารถตั้งค่าให้สูงขึ้นเพื่อให้ได้ความสำคัญสูงขึ้นในช่วงที่มีการใช้งานสูง การเปลี่ยนแปลง `sweep-fee-rate` จะมีผลกับการอัปเดตใหม่ทั้งหมดหลังจากการรีสตาร์ท daemon



#### การกำกับดูแล



ด้วยคำสั่ง `lncli wtclient` ผู้ใช้สามารถโต้ตอบโดยตรงกับไคลเอนต์ Watchtower เพื่อรับหรือแก้ไขข้อมูลเกี่ยวกับหอคอยเฝ้าระวังที่ลงทะเบียนทั้งหมดได้



ตัวอย่างเช่น ด้วยคำสั่ง `lncli wtclient tower` คุณสามารถตรวจสอบจำนวนเซสชันที่กำลังเจรจาอยู่กับ Watchtower ที่เพิ่มเข้ามาข้างต้น และตรวจสอบว่ามันถูกใช้สำหรับการสำรองข้อมูลหรือไม่ด้วยฟิลด์ `active_session_candidate`



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



หากต้องการรับข้อมูลเกี่ยวกับเซสชัน Watchtower ให้ใช้ตัวเลือก `--include_sessions`



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



ตัวเลือกการกำหนดค่าลูกค้าทั้งหมดของ Watchtower สามารถเข้าถึงได้ผ่าน `lncli wtclient -h` :



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - การติดตั้ง Eye of Satoshi ของคุณเอง



*บทแนะนำนี้ถูกดัดแปลงบางส่วนจากบทความบน [Summer of Bitcoin Blog](https://blog.summerofbitcoin.org/). มีการแก้ไขจากเวอร์ชันต้นฉบับ*



The Eye of Satoshi ([Rust-TEOS](https://github.com/talaia-labs/Rust-teos)) เป็น Watchtower Lightning ที่ไม่ใช่สถาบันการเงิน สอดคล้องกับ [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org) ซึ่งประกอบด้วยสองส่วนหลัก:





- teos**: รวมถึงบรรทัดคำสั่ง Interface (CLI) และคุณสมบัติของเซิร์ฟเวอร์ที่จำเป็นของ Watchtower ไฟล์ไบนารีสองไฟล์ - **teosd** และ **teos-CLI** - จะถูกสร้างขึ้นเมื่อ _crate_ นี้ถูกคอมไพล์





- teos-common**: รวมฟังก์ชันการทำงานที่ใช้ร่วมกันระหว่างฝั่งเซิร์ฟเวอร์และฝั่งไคลเอนต์ (มีประโยชน์สำหรับการสร้างไคลเอนต์)



ในการรัน Watchtower อย่างถูกต้อง คุณจำเป็นต้องรัน **bitcoind** ก่อนที่จะเปิดตัว Watchtower ด้วยคำสั่ง **teosd** ก่อนที่จะรันคำสั่งทั้งสองนี้ คุณจำเป็นต้องกำหนดค่าไฟล์ **Bitcoin.conf** ของคุณ นี่คือวิธีการทำ:





- ติดตั้ง Bitcoin core จากซอร์สหรือดาวน์โหลด หลังจากดาวน์โหลดแล้ว ให้วางไฟล์ **Bitcoin.conf** ในไดเรกทอรีผู้ใช้ของ Bitcoin core ดูลิงก์นี้สำหรับข้อมูลเพิ่มเติมเกี่ยวกับตำแหน่งที่จะวางไฟล์ เนื่องจากขึ้นอยู่กับระบบปฏิบัติการที่ใช้





- เมื่อระบุตำแหน่งแล้ว ให้เพิ่มตัวเลือกต่อไปนี้:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- เซิร์ฟเวอร์**: สำหรับคำขอ RPC





- rpcuser** และ **rpcpassword**: ยืนยันตัวตนลูกค้า RPC กับเซิร์ฟเวอร์





- regtest**: ไม่จำเป็น แต่มีประโยชน์หากคุณวางแผนการพัฒนา



ค่าสำหรับ **rpcuser** และ **rpcpassword** จะต้องถูกเลือกโดยคุณ ต้องเขียนโดยไม่มีเครื่องหมายอัญประกาศ ตัวอย่างเช่น:



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



ตอนนี้ ถ้าคุณรัน **bitcoind** โหนดควรจะเริ่มทำงาน





- สำหรับชิ้นส่วน Watchtower คุณต้องติดตั้ง **teos** จากซอร์สก่อน ทำตามคำแนะนำที่ให้ไว้ในลิงก์นี้





- เมื่อคุณติดตั้ง **teos** บนระบบของคุณสำเร็จและรันการทดสอบแล้ว คุณสามารถดำเนินการขั้นตอนสุดท้าย: การตั้งค่าไฟล์ **teos.toml** ในไดเรกทอรีผู้ใช้ teos ไฟล์ควรถูกวางไว้ในโฟลเดอร์ชื่อ **.teos** (สังเกตจุด) ภายใต้ไดเรกทอรีหลักของคุณ ตัวอย่างเช่น **/home//.teos** บน Linux เมื่อพบตำแหน่งแล้ว ให้สร้างไฟล์ **teos.toml** และตั้งค่าตัวเลือกเหล่านี้ให้สอดคล้องกับการเปลี่ยนแปลงที่ทำบน **bitcoind** :



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



โปรดทราบว่าที่นี่ ชื่อผู้ใช้และรหัสผ่านจะต้องเขียน **ภายในเครื่องหมายอัญประกาศ** โดยใช้ตัวอย่างก่อนหน้านี้ :



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



เมื่อดำเนินการเสร็จสิ้น คุณควรพร้อมที่จะเปิดตัว Watchtower เนื่องจากเรากำลังทำงานบน **regtest** เป็นไปได้ว่าไม่มีบล็อกใดถูกขุดบนเครือข่ายทดสอบ Bitcoin ของเราเมื่อ Watchtower เชื่อมต่อครั้งแรก (ถ้ามี แสดงว่ามีบางอย่างผิดปกติ) Watchtower จะสร้างแคชภายในของบล็อก 100 บล็อกสุดท้ายของ **bitcoind**; ดังนั้น ในการเปิดตัวครั้งแรก คุณอาจได้รับข้อผิดพลาดต่อไปนี้:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



เนื่องจากเราใช้ **regtest** เราสามารถ Miner บล็อกได้โดยการออกคำสั่ง RPC โดยไม่ต้องรอความล่าช้าเฉลี่ย 10 นาทีที่พบในเครือข่ายอื่น ๆ (เช่น Mainnet หรือ Testnet) ดูความช่วยเหลือ **bitcoin-cli** สำหรับรายละเอียดเกี่ยวกับวิธีการ Miner บล็อก



![Image](assets/fr/01.webp)



นั่นคือทั้งหมด: คุณได้ทำการรัน Watchtower สำเร็จแล้ว ยินดีด้วยนะ 🎉




## 3 - การกำหนดค่า Watchtower บน Umbrel



บน Umbrel การเชื่อมต่อกับ Watchtower เพื่อปกป้องโหนด Lightning ของคุณนั้นง่ายมาก เนื่องจากทุกอย่างทำผ่านกราฟิก Interface หลังจากเชื่อมต่อกับโหนดของคุณจากระยะไกลแล้ว ให้เปิดแอปพลิเคชัน "**Lightning Node**"



![Image](assets/fr/02.webp)



คลิกที่จุดเล็ก ๆ สามจุดที่มุมขวาบนของ Interface จากนั้นเลือก "**การตั้งค่าขั้นสูง**"



![Image](assets/fr/03.webp)



ในเมนู "**Watchtower**" มีสองตัวเลือกที่สามารถใช้ได้:





- Watchtower Service**: ตัวเลือกนี้ช่วยให้คุณใช้งาน Watchtower ได้ ซึ่งเป็นบริการที่ตรวจสอบช่องทางของโหนดอื่นๆ เพื่อค้นหาความพยายามในการฉ้อโกงใดๆ ในกรณีที่เกิดการละเมิด Watchtower ของคุณจะเผยแพร่ธุรกรรมบน Blockchain ทำให้ผู้ใช้สามารถกู้คืนเงินที่ถูกล็อกไว้ได้ เมื่อเปิดใช้งานแล้ว URI ของ Watchtower ของคุณจะปรากฏขึ้นและสามารถสื่อสารไปยังโหนดอื่นๆ เพื่อให้พวกเขาสามารถเพิ่มลงในไคลเอนต์ Watchtower ของพวกเขาได้





- Watchtower Client**: ตัวเลือกนี้ช่วยให้คุณเชื่อมต่อกับหอคอยเฝ้าระวังภายนอกเพื่อปกป้องช่องทางของคุณเอง เมื่อเปิดใช้งาน คุณสามารถเพิ่มบริการ Watchtower ที่โหนดของคุณจะส่งข้อมูลที่จำเป็นเกี่ยวกับช่องทางของมันไปยังบริการเหล่านี้ หอคอยเฝ้าระวังเหล่านี้จะตรวจสอบสถานะของช่องทางและแทรกแซงในกรณีที่มีการพยายามฉ้อโกง



แน่นอนว่าลำดับความสำคัญสำหรับคุณคือการเปิดใช้งาน *Watchtower Client* เพื่อปกป้องโหนดของคุณ แต่ฉันยังแนะนำให้คุณเปิดใช้งาน *Watchtower Service* เพื่อมีส่วนร่วมในการรักษาความปลอดภัยของผู้ใช้อื่น ๆ เป็นการตอบแทนด้วย



![Image](assets/fr/04.webp)



จากนั้นคลิกที่ปุ่ม "**บันทึกและรีสตาร์ทโหนด**" สีเขียว LND ของคุณจะรีสตาร์ท



ในเมนูเดียวกันนี้ คุณจะพบ URI ของบริการ Watchtower ของคุณหากคุณได้เปิดใช้งานแล้ว คุณยังสามารถเพิ่ม URI ของ Watchtower ภายนอกเพื่อปกป้องช่องของคุณได้อีกด้วย คลิกที่ "**ADD**" เพื่อยืนยัน



![Image](assets/fr/05.webp)



มีหอคอยเฝ้าระวังหลายแห่งที่สามารถเข้าถึงได้ทางออนไลน์ ตัวอย่างเช่น, [LN+ และ Voltage เสนอ Watchtower ที่มีความเอื้อเฟื้อ](https://lightningnetwork.plus/Watchtower) ที่คุณสามารถเชื่อมต่อได้:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



อีกทางเลือกหนึ่งคือการแลกเปลี่ยน Watchtower URI ของคุณกับเพื่อนบิตคอยน์ เพื่อให้แต่ละคนปกป้องโหนดของกันและกัน



ฉันยังแนะนำให้คุณตั้ง Watchtowers หลาย ๆ แห่งเพื่อลดความเสี่ยงในกรณีที่หนึ่งในนั้นไม่สามารถใช้งานได้



ในที่สุด คุณสามารถปรับพารามิเตอร์ "**Watchtower Client Sweep Fee Rate**" ได้ ซึ่งจะกำหนดอัตราค่าธรรมเนียมสูงสุดที่คุณยินดีจ่ายสำหรับธุรกรรมการลงโทษการออกอากาศ Watchtower เพื่อให้รวมอยู่ในบล็อก ตรวจสอบให้แน่ใจว่าคุณตั้งค่าที่สูงเพียงพอ ซึ่งปรับให้เหมาะสมกับจำนวนเงินที่ล็อกไว้ในช่องของคุณ