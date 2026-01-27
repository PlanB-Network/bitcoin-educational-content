---
name: RGB Lightning Node
description: ฉันจะเปิดตัวโหนด Lightning ที่เข้ากันได้กับ RGB ด้วย RLN ได้อย่างไร?
---
![cover](assets/cover.webp)


ในบทแนะนำทีละขั้นตอนนี้ คุณจะได้เรียนรู้วิธีการตั้งค่าโหนด Lightning RGB ในสภาพแวดล้อม Regtest เราจะดูวิธีการสร้างโทเค็น RGB และหมุนเวียนพวกมันในช่องทางต่างๆ


## โครงการ RLN


ทีม Bitfinex ของ RGB ได้ทำงานมาตั้งแต่ปี 2022 เพื่อเสริมสร้างระบบนิเวศของ RGB โดยการพัฒนาเทคโนโลยีสแต็กที่สมบูรณ์ แทนที่จะมุ่งเน้นไปที่ผลิตภัณฑ์เชิงพาณิชย์เพียงอย่างเดียว ความพยายามของพวกเขามุ่งเน้นไปที่การทำให้ซอฟต์แวร์โอเพ่นซอร์สพร้อมใช้งาน การมีส่วนร่วมในข้อกำหนดของโปรโตคอล RGB และการสร้างการอ้างอิงการใช้งาน


หนึ่งในผลงานที่โดดเด่นของ Bitfinex ต่อระบบนิเวศ RGB คือ [ไลบรารี *RGBlib*](https://github.com/RGB-Tools/rgb-lib) ซึ่งเขียนใน Rust และสามารถเข้าถึงได้ผ่านการเชื่อมต่อใน Kotlin และ Python ซึ่งช่วยให้การพัฒนาแอปพลิเคชัน RGB ง่ายขึ้นอย่างมากโดยการห่อหุ้มกลไกการตรวจสอบและการมีส่วนร่วมที่ซับซ้อน


ทีม Bitfinex ยังได้ออกแบบ wallet บนมือถือ RGB ที่เรียกว่า "[*Iris Wallet*](https://iriswallet.com/)" ซึ่งมีให้บริการบน Android wallet นี้รวมการใช้เซิร์ฟเวอร์พร็อกซี RGB เพื่อจัดการการแลกเปลี่ยนข้อมูล off-chain (*consignments*) สำหรับ *Client-side Validation* บน RGB ได้อย่างง่ายดาย


Bitfinex ยังได้พัฒนาโครงการ `rgb-lightning-node` (RLN) ซึ่งเป็น Rust daemon ที่อิงจาก fork ของ `rust-lightning` (LDK) โดยมีการปรับเปลี่ยนเพื่อคำนึงถึงการมีอยู่ของสินทรัพย์ RGB ในช่องทาง เมื่อมีการเปิดช่องทาง การมีอยู่ของโทเค็น RGB สามารถระบุได้ และทุกครั้งที่มีการอัปเดตสถานะช่องทาง จะมีการสร้างการเปลี่ยนแปลงสถานะที่สะท้อนถึงการกระจายของโทเค็นในเอาต์พุต Lightning สิ่งนี้ทำให้สามารถ :




- เปิดช่องทาง Lightning ใน USDT, ตัวอย่างเช่น;
- กำหนดเส้นทางโทเค็นเหล่านี้ผ่านเครือข่าย โดยมีเงื่อนไขว่าเส้นทางการกำหนดเส้นทางมีสภาพคล่องเพียงพอ;
- ใช้ประโยชน์จากการลงโทษและตรรกะการล็อกเวลา (timelock) ของ Lightning โดยไม่ต้องแก้ไข: เพียงแค่ยึดการเปลี่ยนผ่าน RGB ในเอาต์พุตเพิ่มเติมของ commitment transaction


รหัส RLN ยังคงอยู่ในขั้นตอนอัลฟ่า: เราแนะนำให้ใช้ใน **regtest** หรือบน **testnet** เท่านั้น


## การแจ้งเตือนโปรโตคอล RGB


RGB เป็นโปรโตคอลที่ทำงานบน Bitcoin และจำลองการทำงานของสมาร์ทคอนแทรคและการจัดการสินทรัพย์ดิจิทัล โดยไม่ทำให้บล็อกเชนที่เป็นฐานหนักเกินไป แตกต่างจากสมาร์ทคอนแทรค on-chain แบบดั้งเดิม (เช่น บน Ethereum) RGB พึ่งพาระบบ "*การตรวจสอบฝั่งไคลเอนต์*" ซึ่งข้อมูลและประวัติสถานะส่วนใหญ่จะถูกแลกเปลี่ยนและจัดเก็บโดยผู้เข้าร่วมที่เกี่ยวข้องเท่านั้น ในขณะที่บล็อกเชน Bitcoin จะเก็บเฉพาะคำมั่นสัญญาทางเข้ารหัสขนาดเล็ก (ผ่านกลไกเช่น *Tapret* หรือ *Opret*) ในโปรโตคอล RGB บล็อกเชน Bitcoin จึงทำหน้าที่เป็นเซิร์ฟเวอร์ประทับเวลาและระบบป้องกัน double-spending เท่านั้น


สัญญา RGB ถูกจัดโครงสร้างเหมือนเครื่องสถานะวิวัฒนาการ มันเริ่มต้นด้วย Genesis ที่กำหนดสถานะเริ่มต้น (อธิบาย, ตัวอย่างเช่น, การจัดหา, ตั๋วหรือข้อมูลเมตาอื่น ๆ) ตาม Schema ที่ถูกพิมพ์และคอมไพล์อย่างเคร่งครัด การเปลี่ยนสถานะและ, หากจำเป็น, การขยายสถานะจะถูกนำมาใช้เพื่อปรับเปลี่ยนหรือขยายสถานะนี้ แต่ละการดำเนินการ, ไม่ว่าจะเป็นการโอนสินทรัพย์ที่สามารถแลกเปลี่ยนได้ (RGB20) หรือการสร้างสินทรัพย์ที่ไม่ซ้ำกัน (RGB21), เกี่ยวข้องกับ *ตราประทับใช้ครั้งเดียว* สิ่งเหล่านี้เชื่อมโยง UTXOs ของ Bitcoin กับสถานะของ off-chain และป้องกันการใช้จ่ายซ้ำซ้อน, ในขณะที่ยังคงรักษาความลับและความสามารถในการขยายตัว


หากต้องการเรียนรู้เพิ่มเติมเกี่ยวกับวิธีการทำงานของโปรโตคอล RGB ฉันขอแนะนำให้คุณเข้ารับการฝึกอบรมที่ครอบคลุมนี้:


https://planb.academy/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

## การติดตั้งโหนด Lightning ที่รองรับ RGB


ในการคอมไพล์และติดตั้งไบนารี `rgb-lightning-node` เราเริ่มต้นด้วยการโคลนที่เก็บและซับโมดูล จากนั้นเรารัน :


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RLN](assets/fr/01.webp)




- ตัวเลือก `--recurse-submodules` ยังทำการโคลนซับดีไวซ์ที่จำเป็น (รวมถึงเวอร์ชันที่แก้ไขของ `rust-lightning`);
- ตัวเลือก `--shallow-submodules` จำกัดความลึกของการโคลนเพื่อเร่งความเร็วในการดาวน์โหลด ในขณะที่ยังคงให้การเข้าถึงคอมมิตที่จำเป็น


จากรูทของโปรเจกต์ ให้รันคำสั่งต่อไปนี้เพื่อคอมไพล์และติดตั้งไบนารี :


```bash
cargo install --locked --debug --path .
```


![RLN](assets/fr/02.webp)




- `--locked` รับรองว่ารุ่นของการพึ่งพาจะได้รับการเคารพ;
- `--debug` ไม่จำเป็นต้องใช้ แต่สามารถช่วยให้คุณมีสมาธิ (คุณสามารถใช้ `--release` หากคุณต้องการ) ;
- `--path .` บอกให้ `cargo install` ติดตั้งจากไดเรกทอรีปัจจุบัน


เมื่อสิ้นสุดคำสั่งนี้ จะมีไฟล์ปฏิบัติการ `rgb-lightning-node` อยู่ใน `$CARGO_HOME/bin/` ของคุณ ตรวจสอบให้แน่ใจว่าเส้นทางนี้อยู่ใน `$PATH` ของคุณเพื่อให้คุณสามารถเรียกใช้คำสั่งจากไดเรกทอรีใดก็ได้


## ข้อกำหนดเบื้องต้น


ในการทำงาน `rgb-lightning-node` daemon จำเป็นต้องมีการปรากฏและการกำหนดค่าของ :




- โหนด **`bitcoind`**


แต่ละอินสแตนซ์ RLN จะต้องสื่อสารกับ `bitcoind` เพื่อกระจายและตรวจสอบธุรกรรม on-chain ของมัน การยืนยันตัวตน (login/password) และ URL (host/port) จะต้องถูกจัดเตรียมให้กับ daemon




- **ตัวจัดทำดัชนี** (Electrum หรือ Esplora)


daemon จะต้องสามารถแสดงรายการและสำรวจธุรกรรม on-chain โดยเฉพาะอย่างยิ่งเพื่อค้นหา UTXO ที่ทรัพย์สินได้ถูกยึดไว้ คุณจะต้องระบุ URL ของเซิร์ฟเวอร์ Electrum หรือ Esplora ของคุณ




- พร็อกซี่ **RGB**


พร็อกซีเซิร์ฟเวอร์เป็นส่วนประกอบ (ไม่บังคับ แต่แนะนำอย่างยิ่ง) เพื่อให้ง่ายต่อการแลกเปลี่ยน *consignments* RGB ระหว่างเพื่อน Lightning อีกครั้งหนึ่ง ต้องระบุ URL


ID และ URL จะถูกป้อนเมื่อ daemon ถูก *ปลดล็อก* ผ่าน API


## เปิดตัว Regtest


สำหรับการใช้งานที่ง่าย มีสคริปต์ `regtest.sh` ที่จะเริ่มต้นชุดของบริการโดยอัตโนมัติผ่าน Docker: `bitcoind`, `electrs` (indexer), `rgb-proxy-server`.


![RLN](assets/fr/03.webp)


สิ่งนี้ช่วยให้คุณเปิดใช้งานสภาพแวดล้อมที่แยกออกมาและกำหนดค่าไว้ล่วงหน้าได้ มันจะสร้างและทำลายคอนเทนเนอร์และไดเรกทอรีข้อมูลในแต่ละครั้งที่รีบูต เราจะเริ่มต้นด้วยการเริ่มต้น:


```bash
./regtest.sh start
```


สคริปต์นี้จะ :




- สร้างไดเรกทอรี `docker/` เพื่อจัดเก็บ ;
- เรียกใช้ `bitcoind` ใน regtest รวมถึง indexer `electrs` และ `rgb-proxy-server` ;
- รอจนกว่าทุกอย่างจะพร้อมใช้งาน


![RLN](assets/fr/04.webp)


ถัดไป เราจะเปิดตัวโหนด RLN หลายตัว ในเชลล์แยกกัน ให้รันตัวอย่างเช่น (เพื่อเปิดตัวโหนด RLN 3 โหนด) :


```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```


![RLN](assets/fr/05.webp)




- พารามิเตอร์ `--network regtest` บ่งบอกถึงการใช้การกำหนดค่าของ regtest;
- `--daemon-listening-port` ระบุพอร์ต REST ที่โหนด Lightning จะฟังสำหรับการเรียก API (JSON);
- `--ldk-peer-listening-port` ระบุพอร์ต Lightning p2p ที่จะรับฟัง;
- `dataldk0/`, `dataldk1/` เป็นเส้นทางไปยังไดเรกทอรีจัดเก็บข้อมูล (แต่ละโหนดเก็บข้อมูลของตนเองแยกกัน)


ตอนนี้คุณสามารถดำเนินการคำสั่งบน RLN nodes ของคุณจากเบราว์เซอร์ได้แล้ว ต้องขอบคุณ API โดยเฉพาะอย่างยิ่ง นี่คือที่ที่คุณสามารถ *ปลดล็อก* daemons ได้ เพียงเปิดเบราว์เซอร์บนคอมพิวเตอร์เครื่องเดียวกับ nodes ของคุณ และป้อน URL :


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


สำหรับโหนดที่จะเปิดช่องสัญญาณ มันจะต้องมีบิตคอยน์ในที่อยู่ที่สร้างขึ้นด้วยคำสั่งต่อไปนี้ (สำหรับโหนดหมายเลข 1, ตัวอย่างเช่น):


```bash
curl -X POST http://localhost:3001/address
```


คำตอบจะให้ที่อยู่แก่คุณ


![RLN](assets/fr/06.webp)


บน `bitcoind` Regtest เราจะทำการขุดบิทคอยน์จำนวนหนึ่ง รัน :


```bash
./regtest.sh mine 101
```


![RLN](assets/fr/07.webp)


ส่งเงินไปยังที่อยู่โหนดที่สร้างขึ้นด้านบน:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RLN](assets/fr/08.webp)


จากนั้นขุดบล็อกเพื่อยืนยันการทำธุรกรรม:


```bash
./regtest.sh mine 1
```


![RLN](assets/fr/09.webp)


## เปิดตัว Testnet (โดยไม่ใช้ Docker)


หากคุณต้องการทดสอบสถานการณ์ที่สมจริงมากขึ้น คุณสามารถเปิดตัวโหนด RLN บน Testnet แทนที่จะเป็นใน Regtest โดยชี้ไปที่บริการสาธารณะหรือบริการที่คุณควบคุม:


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


ตามค่าเริ่มต้น หากไม่พบการกำหนดค่า daemon จะพยายามใช้:




- `bitcoind_rpc_host`: `electrum.iriswallet.com`
- `bitcoind_rpc_port`: `18332`
- indexer_url`: `ssl://electrum.iriswallet.com:50013`
- `proxy_endpoint`: `rpcs://proxy.iriswallet.com/0.2/json-rpc`


ด้วยการเข้าสู่ระบบ :




- `bitcoind_rpc_username`: `user`
- `bitcoind_rpc_username`: `password`


คุณยังสามารถปรับแต่งองค์ประกอบเหล่านี้ผ่าน `init`/`unlock` API ได้อีกด้วย


## ออก RGB token


ในการออก token เราจะเริ่มต้นด้วยการสร้าง UTXOs ที่ "colorable":


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```


![RLN](assets/fr/10.webp)


แน่นอนว่าคุณสามารถปรับลำดับได้ เพื่อยืนยันการทำธุรกรรม เราจะทำการขุด a :


```bash
./regtest.sh mine 1
```


เราสามารถสร้างสินทรัพย์ RGB ได้แล้ว คำสั่งจะขึ้นอยู่กับประเภทของสินทรัพย์ที่คุณต้องการสร้างและพารามิเตอร์ของมัน ที่นี่ฉันกำลังสร้าง NIA (*Non Inflatable Asset*) token ชื่อ "Plan ₿ Academy" โดยมีจำนวน 1000 หน่วย `precision` ช่วยให้คุณกำหนดความสามารถในการแบ่งหน่วยได้


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "Plan ₿ Academy",
"name": "Plan ₿ Academy",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```


![RLN](assets/fr/11.webp)


การตอบกลับจะรวมถึง ID ของสินทรัพย์ที่สร้างขึ้นใหม่ อย่าลืมจดบันทึกตัวระบุนี้ ในกรณีของฉันคือ:


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RLN](assets/fr/12.webp)


จากนั้นคุณสามารถโอนมันไปที่ on-chain หรือจัดสรรในช่องทาง Lightning นั่นคือสิ่งที่เราจะทำในส่วนถัดไป


## เปิดช่องทางและโอนสินทรัพย์ RGB


คุณต้องเชื่อมต่อโหนดของคุณกับเพียร์บนเครือข่าย Lightning โดยใช้คำสั่ง `/connectpeer` ในตัวอย่างของฉัน ฉันควบคุมทั้งสองโหนด ดังนั้นฉันจะดึงคีย์สาธารณะของโหนด Lightning ที่สองของฉันด้วยคำสั่งนี้:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


คำสั่งนี้จะส่งคืนกุญแจสาธารณะของโหนดหมายเลข 2 ของฉัน:


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RLN](assets/fr/13.webp)


ถัดไป เราจะเปิดช่องโดยระบุสินทรัพย์ที่เกี่ยวข้อง (`Plan ₿ Academy`) คำสั่ง `/openchannel` ช่วยให้คุณกำหนดขนาดของช่องในหน่วย satoshis และเลือกที่จะรวมสินทรัพย์ RGB ได้ ขึ้นอยู่กับสิ่งที่คุณต้องการสร้าง แต่ในกรณีของฉัน คำสั่งคือ :


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```


ค้นหาข้อมูลเพิ่มเติมได้ที่นี่:




- `peer_pubkey_and_opt_addr`: ตัวระบุของเพียร์ที่เราต้องการเชื่อมต่อด้วย (คีย์สาธารณะที่เราพบก่อนหน้านี้);
- `capacity_sat`: ความจุช่องสัญญาณทั้งหมดในหน่วยซาโตชิ ;
- `push_msat`: จำนวนในหน่วย millisatoshis ที่ถูกโอนไปยังเพื่อนเมื่อช่องทางถูกเปิด (ที่นี่ฉันโอน 10,000 sats ทันทีเพื่อให้เขาสามารถทำการโอน RGB ได้ในภายหลัง) ;
- `asset_amount`: จำนวนสินทรัพย์ RGB ที่จะถูกผูกมัดกับช่อง ;
- `asset_id` : ตัวระบุเฉพาะของสินทรัพย์ RGB ที่มีส่วนร่วมในช่อง;
- `public`: ระบุว่าช่องทางควรถูกทำให้เป็นสาธารณะสำหรับการกำหนดเส้นทางบนเครือข่ายหรือไม่


![RLN](assets/fr/14.webp)


ในการยืนยันธุรกรรม จะมีการขุด 6 บล็อก:


```bash
./regtest.sh mine 6
```


![RLN](assets/fr/15.webp)


ช่อง Lightning เปิดอยู่ในขณะนี้และยังมีโทเค็น `Plan ₿ Academy` จำนวน 500 โทเค็นในฝั่งของโหนด n°1 หากโหนด n°2 ต้องการรับโทเค็น `Plan ₿ Academy` จะต้อง generate ใบแจ้งหนี้ นี่คือวิธีการทำ:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```


ด้วย:




- `amt_msat`: Invoice จำนวนในหน่วย millisatoshis (ขั้นต่ำ 3000 sats) ;
- `expiry_sec` : Invoice เวลาหมดอายุในหน่วยวินาที ;
- `asset_id` : ตัวระบุของสินทรัพย์ RGB ที่เกี่ยวข้องกับใบแจ้งหนี้ ;
- `asset_amount`: จำนวนสินทรัพย์ RGB ที่จะโอนด้วยใบแจ้งหนี้นี้


ในการตอบกลับ คุณจะได้รับใบแจ้งหนี้ RGB:


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RLN](assets/fr/16.webp)


เราจะชำระใบแจ้งหนี้นี้จากโหนดแรก ซึ่งมีเงินสดที่จำเป็นด้วย `Plan ₿ Academy` token:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RLN](assets/fr/17.webp)


การชำระเงินได้ดำเนินการแล้ว สามารถตรวจสอบได้โดยการเรียกใช้คำสั่ง :


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RLN](assets/fr/18.webp)


ต่อไปนี้คือวิธีการปรับใช้โหนด Lightning ที่ได้รับการแก้ไขเพื่อรองรับสินทรัพย์ RGB การสาธิตนี้อ้างอิงจาก :




- สภาพแวดล้อม regtest (ผ่าน `./regtest.sh`) หรือ testnet ;
- โหนด Lightning (`rgb-lightning-node`) ที่ใช้ `bitcoind`, ตัวจัดทำดัชนี และ `rgb-proxy-server` ;
- ชุดของ JSON REST APIs สำหรับการเปิด/ปิดช่องทาง, การออกโทเค็น, การโอนสินทรัพย์ผ่าน Lightning, เป็นต้น


ขอบคุณสำหรับกระบวนการนี้ :




- ธุรกรรมการมีส่วนร่วมของ Lightning รวมถึงเอาต์พุตเพิ่มเติม (OP_RETURN หรือ Taproot) พร้อมกับการยึดของการเปลี่ยนผ่าน RGB;
- การโอนเงินทำในลักษณะเดียวกับการชำระเงินแบบ Lightning แบบดั้งเดิม แต่มีการเพิ่ม RGB token;
- สามารถเชื่อมโยงโหนด RLN หลายตัวเพื่อกำหนดเส้นทางและทดลองกับการชำระเงินผ่านโหนดหลายตัวได้ หากมีสภาพคล่องเพียงพอทั้งในบิตคอยน์และสินทรัพย์ RGB บนเส้นทาง


หากคุณพบว่าบทแนะนำนี้มีประโยชน์ ฉันจะรู้สึกขอบคุณมากหากคุณกดนิ้วโป้งสีเขียวด้านล่าง โปรดอย่าลังเลที่จะแบ่งปันบทความนี้บนเครือข่ายสังคมของคุณ ขอบคุณมาก!


ฉันยังแนะนำบทแนะนำอื่นนี้ซึ่งฉันอธิบายวิธีการใช้เครื่องมือ RGB CLI ที่พัฒนาโดยสมาคม LNP/BP เพื่อสร้างสัญญา RGB:


https://planb.academy/tutorials/node/others/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4