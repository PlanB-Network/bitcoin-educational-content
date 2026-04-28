---
name: Coinjoin Coordinator - WabiSabi
description: วิธีการตั้งค่าและรันผู้ประสานงาน coinjoin ตามโปรโตคอล WabiSabi (ใช้ใน Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## บทนำ 👋


ในคู่มือผู้เชี่ยวชาญนี้ เราจะช่วยคุณตั้งค่าผู้ประสานงาน coinjoin ซึ่งเป็นเซิร์ฟเวอร์ที่รวบรวมผู้ที่ต้องการประหยัดค่าธรรมเนียมการทำธุรกรรมหรือเพิ่มความเป็นส่วนตัวบนเชนในการทำธุรกรรมร่วมกัน เนื่องจากไม่มีผู้ประสานงานที่ดำเนินการโดยบริษัทที่รวมอยู่กับ Wasabi Wallet อีกต่อไป ผู้ใช้จึงต้องค้นหาและเลือกเซิร์ฟเวอร์ผู้ประสานงานที่ตนต้องการเอง มีเพียงไม่กี่ผู้ประสานงานที่แสดงความต้องการค่าธรรมเนียมการประสานงาน 0% ดังนั้นนักพัฒนาของ Wasabi Wallet จึงทำงานอย่างหนักเพื่อให้ง่ายที่สุดในการเริ่มต้นใช้งานผู้ประสานงานชุมชนของคุณเอง (บนฮาร์ดแวร์ที่เล็กเท่ากับ Raspberry Pi5!) ผู้ประสานงานที่ใช้งานอยู่ในปัจจุบันที่ขอค่าธรรมเนียมการประสานงาน 0% สามารถพบได้ที่ [LiquiSabi](https://liquisabi.com) และที่สำคัญกว่านั้นที่ [nostr](https://github.com/Kukks/WasabiNostr)


## ข้อกำหนด 🫴



- VPS (โฮสต์โหนด) หรือ คอมพิวเตอร์/เซิร์ฟเวอร์ (โหนดที่โฮสต์เอง)
- Pruned/Full Bitcoin Core node (tested with v29.0)


ตัวเลือก:


- การส่งต่อทราฟฟิก (sub)Domain ไปยังโหนด (เช่น coinjoin.[yourdomain].io)


ขอแนะนำให้มีประสบการณ์กับพรอมต์บรรทัดคำสั่งและ bash บ้าง เนื่องจากไม่สามารถทำให้ทุกขั้นตอนเป็นอัตโนมัติได้


ในด้านฮาร์ดแวร์ แนะนำให้มีระบบที่มี:


- 4 คอร์
- 16 GB RAM
- 2 TB SSD หรือ NVMe (สำหรับ full-node) / 128 GB SSD (สำหรับ pruned-node)


ข้อกำหนดดังกล่าวสามารถจัดหาได้โดย Raspberry Pi 5 ในราคาเพียง 120 $ โดยไม่รวมที่เก็บข้อมูลซึ่งมีราคาประมาณ 100 $ สำหรับ NVMe stick ขนาด 2TB


VPS ราคาถูกมักจะมาพร้อมกับเพียง 1 คอร์และ RAM 4GB ซึ่งฉันพบว่าน้อยเกินไปที่จะซิงค์และยืนยัน bitcoin blockchain ทั้งหมดที่ blockheight 911817


ในแง่ของการจัดเก็บข้อมูล โหนดเต็มจะต้องการพื้นที่จัดเก็บดิสก์อย่างน้อย 2TB โดยควรเป็นประเภท SSD หรือ NVMe เมื่อทำการตัดแต่ง blockchain สามารถใช้ไดรฟ์จัดเก็บข้อมูลที่มีขนาดเล็กกว่ามากได้ (เช่น SSD ขนาด 128GB)


หากคุณตั้งใจที่จะรันผู้ประสานงานสำหรับการรวมเหรียญขนาดใหญ่ (300+ อินพุต) ขอแนะนำให้เลือกระบบที่มีแกนประมวลผลที่เร็วกว่า/ใหม่กว่า ซึ่งมีประสิทธิภาพสูงขึ้นสำหรับการตรวจสอบลายเซ็นทั้งหมด


## การติดตั้ง 🛠️


บนโหนดเราต้องการดาวน์โหลดและติดตั้งเวอร์ชันล่าสุดที่ปล่อยออกมาของ Wasabi Wallet ซึ่งรวมถึง backend และ coordinator เป็นไฟล์ปฏิบัติการแบบสแตนด์อโลนถัดจาก wallet


ค้นหาเวอร์ชันล่าสุด: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) และตรวจสอบลายเซ็น PGP ของการปล่อยด้วยคีย์: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


รายละเอียดการปรับใช้จะแตกต่างกันไปขึ้นอยู่กับฮาร์ดแวร์ (สถาปัตยกรรม CPU) และการเลือก OS ด้านล่างนี้คือรายละเอียดต่างๆ สำหรับ Raspberry Pi (ARM-64) โดยมี Debian-based RaspiBlitz เป็นจุดเริ่มต้น ข้ามไปข้างหน้าสำหรับการปรับใช้ OS Ubuntu (X86-64) โดยใช้ Nix


ค้นหาคำแนะนำการติดตั้งได้ที่นี่: [Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### RaspiBlitz/Debian deployment


สำหรับโหนด RaspiBlitz (ทดสอบกับ v1.11) การปรับใช้ script ที่สร้างจากซอร์สโค้ดสามารถใช้ได้: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### การปรับใช้ที่ง่าย


สำหรับการปรับใช้ขั้นต่ำ คุณเพียงแค่ต้องการแยกไฟล์ปฏิบัติการสำหรับแพลตฟอร์มของคุณในโฟลเดอร์

ตัวอย่างโค้ดบรรทัดคำสั่งสำหรับ Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


นี่ควรส่งผลให้เกิดข้อความลายเซ็นที่ถูกต้องดังต่อไปนี้:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


และคุณสามารถดำเนินการติดตั้งแพ็คเกจที่ดาวน์โหลดมา:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## การกำหนดค่า 🧾


ก่อนที่จะเรียกใช้ผู้ประสานงาน คุณจำเป็นต้องแก้ไขไฟล์ Config.json ด้วย:


- Bitcoin RPC ข้อมูลประจำตัว
- พารามิเตอร์รอบที่ต้องการ
- คีย์สาธารณะขยายของผู้ประสานงาน (สร้าง SegWit wallet ใหม่สำหรับรับฝุ่นที่รวบรวม)

**คำเตือน**: Taproot wallet จะทำให้เกิด UTXO ที่ไม่สามารถใช้จ่ายได้! ใช้ Native Segwit wallet ที่นี่


- ประเภทที่อยู่ที่อนุญาตให้ป้อนและส่งออก
- การกำหนดค่าผู้ประกาศสำหรับการเผยแพร่ผ่าน nostr (ชื่อ, คำอธิบาย, Uri, อินพุตขั้นต่ำ, nostr relay, nostr private key)


คุณสามารถเรียกใช้ผู้ประสานงานที่เข้าถึงได้เฉพาะผ่านที่อยู่ .onion หรือใช้โดเมน clearnet ที่คุณกำหนดเอง


ค้นหาหรือสร้างไฟล์ config ในเส้นทางนี้:


`~/.walletwasabi/coordinator/Config.json`


แก้ไขด้วยคำสั่ง:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


ดูตัวอย่าง Config.json นี้:


```
{
"Network": "Main",
"MainNetBitcoinRpcUri": "http://localhost:8332",
"TestNetBitcoinRpcUri": "http://localhost:48332",
"RegTestBitcoinRpcUri": "http://localhost:18443",
"BitcoinRpcConnectionString": "your_bitcoin_rpcuser:your_bitcoin_rpcpassword",
"ConfirmationTarget": 21,
"DoSSeverity": "0.02",
"DoSMinTimeForFailedToVerify": "1d 21h 0m 0s",
"DoSMinTimeForCheating": "1d 0h 0m 0s",
"DoSPenaltyFactorForDisruptingConfirmation": 0.2,
"DoSPenaltyFactorForDisruptingSignalReadyToSign": 1.0,
"DoSPenaltyFactorForDisruptingSigning": 1.0,
"DoSPenaltyFactorForDisruptingByDoubleSpending": 3.0,
"DoSMinTimeInPrison": "0d 0h 20m 0s",
"MinRegistrableAmount": "0.000021",
"MaxRegistrableAmount": "1000.00",
"AllowNotedInputRegistration": true,
"StandardInputRegistrationTimeout": "0d 0h 21m 0s",
"BlameInputRegistrationTimeout": "0d 0h 3m 0s",
"ConnectionConfirmationTimeout": "0d 0h 1m 0s",
"OutputRegistrationTimeout": "0d 0h 1m 0s",
"TransactionSigningTimeout": "0d 0h 1m 0s",
"FailFastOutputRegistrationTimeout": "0d 0h 3m 0s",
"FailFastTransactionSigningTimeout": "0d 0h 1m 0s",
"RoundExpiryTimeout": "0d 0h 5m 0s",
"MaxInputCountByRound": 100,
"MinInputCountByRoundMultiplier": 0.21,
"MinInputCountByBlameRoundMultiplier": 0.21,
"RoundDestroyerThreshold": 375,
"CoordinatorExtPubKey": "xpub_fill_in_your_new_wallet_here",
"CoordinatorExtPubKeyCurrentDepth": 0,
"MaxSuggestedAmountBase": "100.00",
"RoundParallelization": 1,
"CoordinatorIdentifier": "CoinJoinCoordinatorIdentifier",
"AllowP2wpkhInputs": true,
"AllowP2trInputs": true,
"AllowP2wpkhOutputs": true,
"AllowP2trOutputs": true,
"AllowP2pkhOutputs": true,
"AllowP2shOutputs": true,
"AllowP2wshOutputs": true,
"DelayTransactionSigning": false,
"AnnouncerConfig": {
"CoordinatorName": "Your Coordinator Name",
"IsEnabled": true,
"CoordinatorDescription": "Privacy is a human right!",
"CoordinatorUri": "https://coinjoin.yourdomain/",
"AbsoluteMinInputCount": 21,
"ReadMoreUri": "https://coinjoin.yourdomain/",
"RelayUris": [
"wss://relay.primal.net"
],
"Key": "nsec_your_coordinator_nostr_privatekey"
},
"PublishAsOnionService": true,
"OnionServicePrivateKey": your_onion_service_private_key
}
```

### การกำหนดค่า Tor 🧅


ในการกรอก OnionServicePrivateKey ของคุณ คุณอาจจำเป็นต้องสร้างคีย์ขึ้นมาก่อน


Wasabi Wallet จะสร้างคีย์ส่วนตัวให้คุณหากคุณรันมันครั้งแรกโดยตั้งค่า ```"PublishAsOnionService": true,``` ในไฟล์ Config.json


เรียกใช้ผู้ประสานงานหนึ่งครั้งด้วยคำสั่ง:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


หากต้องการดูที่อยู่ Onion hidden service ของคุณ ให้ตรวจสอบบันทึกของผู้ประสานงานด้วย:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


และคุณจะพบสิ่งที่คล้ายกับ:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


URL ที่ยาวซึ่งลงท้ายด้วย .onion คือที่อยู่บริการที่ซ่อนอยู่ของคุณหรือ CoordinatorUri.


หรือตรวจสอบไฟล์การกำหนดค่าผู้ประสานงานของคุณอีกครั้งด้วย:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


ซึ่งควรจะถูกกรอกโดยอัตโนมัติในขณะนี้


## วิ่ง ⚡


เมื่อกำหนดค่าพารามิเตอร์ทั้งหมดแล้ว คุณสามารถเรียกใช้บริการผู้ประสานงานและเริ่มประกาศรอบแรกของคุณ 🕶️


เพียงเริ่มต้นผู้ประสานงานด้วยคำสั่ง:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


คุณสามารถตรวจสอบรอบปัจจุบันและจำนวน UTXO's/เหรียญที่ลงทะเบียนได้โดยตรวจสอบ (ใน Tor browser สำหรับ .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### ตัวเลือก: การดีบักเซิร์ฟเวอร์ผู้ประสานงาน


คุณสามารถตรวจสอบปัญหาหรือข้อผิดพลาดใด ๆ ในไฟล์บันทึกได้ที่ ```~/.walletwasabi/backend/Logs.txt```


ปัญหาทั่วไปประกอบด้วยปัญหาการเชื่อมต่อ RPC ซึ่งต้องเปิดใช้งานใน ```~/.bitcoin/bitcoin.conf``` ด้วย:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### ไม่บังคับ: การรันเซิร์ฟเวอร์แบ็กเอนด์


ร่วมกับผู้ประสานงาน คุณยังสามารถจัดหาเซิร์ฟเวอร์แบ็กเอนด์สำหรับผู้ใช้ที่ไม่มีโหนดบิตคอยน์ของตนเองเพื่อเชื่อมต่อสำหรับการประมาณค่าธรรมเนียมและตัวกรองบล็อกได้อีกด้วย


เริ่มบริการนี้ด้วยคำสั่ง:


```
wbackend
```


## เชิญผู้ใช้ Wasabi มาที่ผู้ประสานงานของคุณ 🫂


สำหรับผู้ใช้รายอื่นที่จะค้นหาบริการของคุณ คุณสามารถพึ่งพา nostr announcer หรือแชร์ลิงก์วิเศษกับโดเมนของคุณ (clearnet) หรือบริการที่ซ่อนอยู่ (.onion link) และพารามิเตอร์รอบเช่นนี้:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


เมื่อผู้ใช้คัดลอกลิงก์เวทมนตร์และเปิด Wasabi Wallet ของพวกเขา ซอฟต์แวร์จะเปิดแสดงกล่องโต้ตอบผู้ประสานงานโดยอัตโนมัติพร้อมโดเมนและพารามิเตอร์ของคุณ


![detected](assets/en/02.webp)


💚🍣 ขอแสดงความยินดีที่ทำให้ความเป็นส่วนตัวของบิทคอยน์เป็นแบบกระจายศูนย์ 🕶️


จำการฝึกของคุณ [wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet ใช้สำหรับการป้องกันเท่านั้น 🛡️