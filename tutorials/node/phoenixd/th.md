---
name: ฟีนิกซ์
description: ปรับใช้โหนด Lightning แบบมินิมอลของคุณเองด้วย Phoenixd
---

![cover](assets/cover.webp)



อิสรภาพทางการเงินยังหมายถึงการควบคุมโครงสร้างพื้นฐาน Lightning ของคุณ สำหรับนักพัฒนาและบริษัทที่ต้องการผสานรวม Bitcoin Lightning เข้ากับแอปพลิเคชันของพวกเขา **Phoenixd** เป็นโซลูชันที่เหมาะสมที่สุด: โหนด Lightning ที่เรียบง่ายและเชี่ยวชาญพร้อมการจัดการสภาพคล่องอัตโนมัติ



Phoenixd เป็นเซิร์ฟเวอร์ Lightning ที่พัฒนาโดย ACINQ ออกแบบมาเฉพาะสำหรับการส่งและรับการชำระเงินผ่าน Lightning ผ่าน HTTP API ซึ่งแตกต่างจากการใช้งานที่มีฟีเจอร์ครบครันเช่น LND หรือ Core Lightning, Phoenixd ช่วยลดความซับซ้อนของการจัดการช่องทางในขณะที่ยังคงรักษาการป้องกันตนเองของเงินทุนของคุณ



ในบทแนะนำนี้ เราจะมาดูวิธีการติดตั้ง กำหนดค่า และใช้ Phoenixd เพื่อพัฒนาแอปพลิเคชัน Lightning ด้วยโครงสร้างพื้นฐานที่โฮสต์เองและ API ที่ใช้งานง่าย



## Phoenixd คืออะไร?



Phoenixd เป็นโหนด Lightning ที่มีความเรียบง่ายและเฉพาะทาง พัฒนาโดย ACINQ เป็นโซลูชันที่ออกแบบมาสำหรับนักพัฒนาและองค์กรที่ต้องการผสานรวม Lightning เข้ากับแอปพลิเคชันของพวกเขาโดยไม่ต้องมีความซับซ้อนในการจัดการของ full node



### หลักการทำงาน



**Phoenixd เป็นโหนด Lightning แบบมินิมอลที่ใช้ ACINQ เป็น LSP (ผู้ให้บริการ Lightning) สำหรับสภาพคล่องอัตโนมัติ เมื่อคุณได้รับการชำระเงินผ่าน Lightning มันจะเปิดช่องทางกับโหนด ACINQ โดยอัตโนมัติเพื่อจัดสรรความจุขาเข้าที่จำเป็น สภาพคล่อง "ทันที" นี้จะถูกคิดค่าบริการที่ **1% + mining ค่าธรรมเนียม** ของจำนวนเงินที่ได้รับ**



**การจัดการอัตโนมัติ:** ระบบจัดการองค์ประกอบสำคัญสามประการ:




- ช่องทาง** Lightning: เปิด ปิด และจัดการโดยอัตโนมัติตามความจำเป็น
- สภาพคล่องขาเข้า/ขาออก**: การจัดเตรียมอัตโนมัติผ่านการแยกและการเปิดช่องทาง
- เครดิตค่าธรรมเนียม** : การชำระเงินขนาดเล็กที่ไม่เพียงพอที่จะสร้างช่องทางจะถูกเก็บไว้เป็นการสำรองสำหรับค่าใช้จ่ายในอนาคต



### Phoenixd benefits



**คุณควบคุมกุญแจส่วนตัวของคุณ (12-word seed) และเงินทุนของคุณ Phoenixd สร้าง wallet ของคุณในเครื่องโดยไม่เคยแชร์กุญแจของคุณเลย



**โครงสร้างพื้นฐานส่วนบุคคล:** Phoenixd ทำงานบนเซิร์ฟเวอร์ของคุณ ให้คุณเข้าถึงบันทึกรายละเอียด การกำหนดค่า และการควบคุม API คุณไม่ต้องพึ่งพาบริการของบุคคลที่สามในการเข้าถึงเงินทุนของคุณอีกต่อไป



**Integrated API:** Phoenixd มีคุณสมบัติ HTTP API สำหรับการรวมเข้ากับบริการอื่น ๆ รองรับ LNURL โดยธรรมชาติและการพัฒนาแอปพลิเคชันที่กำหนดเอง



**ความง่ายในการผสานรวม:** ด้วย REST API ที่เรียบง่าย Phoenixd สามารถผสานรวมเข้ากับแอปพลิเคชันหรือบริการใด ๆ ที่ต้องการการชำระเงินผ่าน Lightning ได้



**หมายเหตุสำคัญ:** สภาพคล่องอัตโนมัติยังคงมาจาก ACINQ ในฐานะ LSP (ผู้ให้บริการสายฟ้าแลบ) Phoenixd ใช้กลไกเดียวกันกับ Phoenix มือถือสำหรับการจัดการช่องทางอัตโนมัติ



## การติดตั้ง Phoenixd



### ข้อกำหนดเบื้องต้น



Phoenixd ต้องการสภาพแวดล้อม Linux (แนะนำ Ubuntu/Debian) พร้อมทักษะพื้นฐานในการใช้คำสั่งบรรทัดคำสั่ง สำหรับประสิทธิภาพสูงสุด คุณจะต้องการ:





- เซิร์ฟเวอร์ Linux**: VPS หรือเครื่องท้องถิ่นที่มีการเชื่อมต่อที่เสถียร
- OpenJDK 21** : สภาพแวดล้อมรันไทม์ของ Java
- การเชื่อมต่ออินเทอร์เน็ตที่เสถียร**: สำหรับการซิงโครไนซ์กับเครือข่าย Lightning
- ชื่อโดเมน** (ไม่บังคับ) : สำหรับการเข้าถึง HTTPS ที่ปลอดภัยไปยัง API



### ดาวน์โหลดและติดตั้ง



**1. ดาวน์โหลด Phoenixd**



ไปที่หน้า [GitHub releases](https://github.com/ACINQ/phoenixd/releases) และดาวน์โหลดเวอร์ชันล่าสุดที่ตรงกับสถาปัตยกรรมของคุณ:



```bash
# For Linux x86_64
# Replace with the latest release
wget https://github.com/ACINQ/phoenixd/releases/download/v0.6.1/phoenixd-0.6.1-linux-x64.zip
unzip -j phoenixd-0.6.1-linux-x64.zip
chmod +x phoenixd phoenix-cli
```



**2. เริ่มต้นครั้งแรก



เริ่มต้น Phoenixd สำหรับการเริ่มต้น:



```bash
./phoenixd
```



เมื่อเปิดใช้งานครั้งแรก คุณจะถูกขอให้ยืนยันสองขั้นตอนสำคัญโดยการพิมพ์ "I understand" :



**ข้อความ 1 - สำรองข้อมูล:**


```
This software is self-custodial, you have full control and responsibility over your funds.
Your 12-words seed is located in /home/<user>/.phoenix, make sure to do a backup or you risk losing your funds.
Do not share the same seed with other phoenix instances (mobile or server), it will cause issues and channel force closes.
```



**บันทึกคำ 12 คำนี้** - เป็นการรับประกันการกู้คืนของคุณเพียงอย่างเดียว



**ข้อความ 2 - สภาพคล่องอัตโนมัติ:**


```
Continuous liquidity
Liquidity management is fully automated.
When receiving a Lightning payment that doesn't fit in your existing channel:
- If the payment amount is large enough to cover mining fees and service fees for automated liquidity,
then your channel will be created or enlarged right away.
- If the payment is too small, then the full amount is added to your fee credit,
and will be used later to pay for future fees. The fee credit is non-refundable.
```



พิมพ์ `I understand` สำหรับการยืนยันแต่ละครั้ง



![Premier démarrage](assets/fr/01.webp)



*Phoenixd เริ่มต้นครั้งแรก: การยืนยันการสำรองข้อมูลและสภาพคล่องอัตโนมัติ*



**3. การกำหนดค่าขณะใช้งาน** (เฉพาะภาษาฝรั่งเศส)



สำหรับการทำงานอย่างต่อเนื่อง ให้สร้าง systemd :



```bash
sudo nano /etc/systemd/system/phoenixd.service
```



```ini
[Unit]
Description=Phoenixd - Minimalist Lightning node
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user
ExecStart=/home/your_user/phoenixd
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```



```bash
sudo systemctl daemon-reload
sudo systemctl enable phoenixd
sudo systemctl start phoenixd
```



![Service systemd](assets/fr/02.webp)



*บริการ Phoenixd ทำงานและปฏิบัติการผ่าน systemd และ `auto-liquidity` ที่ 2m sat*



## การกำหนดค่าและความปลอดภัย



### ไฟล์การกำหนดค่า



Phoenixd สร้างไฟล์ `~/.phoenix/phoenix.conf` โดยอัตโนมัติพร้อมพารามิเตอร์ที่จำเป็น:



```conf
# Network (mainnet by default)
chain=mainnet

# Size of automatic channels and requested liquidity amount (in satoshis)
auto-liquidity=2000000

# API configuration
http-bind-address=127.0.0.1
http-bind-port=9740
http-password=auto_generated_password
http-password-limited-access=limited_password
```



**พารามิเตอร์หลัก:**




- `auto-liquidity`: ขนาดของช่องทางที่เปิดโดยอัตโนมัติ (ค่าเริ่มต้น: 2M Sats)
- รหัสผ่าน-http`: รหัสผ่านผู้ดูแลระบบสำหรับ API (การสร้างใบแจ้งหนี้และการส่งการชำระเงิน)
- http-password-limited-access`: รหัสผ่านจำกัด (เฉพาะการสร้างใบแจ้งหนี้)



### เข้าถึงอย่างปลอดภัยด้วย HTTPS



โดยค่าเริ่มต้น Phoenixd API สามารถเข้าถึงได้เฉพาะผ่านทาง HTTP ภายใน (`http://127.0.0.1:9740`) หากต้องการใช้โหนดของคุณจากภายนอก (แอปพลิเคชันมือถือ, เซิร์ฟเวอร์อื่น ๆ, การผสานเว็บ) คุณจำเป็นต้องกำหนดค่าการเข้าถึง HTTPS ที่ปลอดภัย



**หลักการพร็อกซีย้อนกลับ:**


```
Internet → nginx (port 443 HTTPS) → Phoenixd (port 9740 HTTP local)
```



**Nginx** ทำหน้าที่เป็น **reverse proxy**: มันฟังคำขอ HTTPS จากอินเทอร์เน็ตที่พอร์ต 443 แล้วเปลี่ยนเส้นทางไปยัง Phoenixd ในเครื่อง (พอร์ต 9740) จากนั้นส่งการตอบกลับที่เข้ารหัสกลับไปยังไคลเอนต์



**ใบรับรอง SSL/TLS** เป็นไฟล์ดิจิทัลที่ :




- พิสูจน์ตัวตนของเซิร์ฟเวอร์ของคุณ** (ป้องกันการโจมตีแบบคนกลาง)
- เปิดใช้งานการเข้ารหัส HTTPS**: ข้อมูลทั้งหมด รวมถึงรหัสผ่าน API ของคุณ จะถูกเข้ารหัสระหว่างการส่งข้อมูล
- ออกให้ฟรี** โดย Let's Encrypt ผ่านเครื่องมือ certbot



การกำหนดค่านี้ช่วยให้คุณสามารถ:




- เข้าถึง API จากอินเทอร์เน็ตอย่างปลอดภัย**
- เข้ารหัสรหัสผ่าน API** ของคุณระหว่างการส่งข้อมูล (เพื่อป้องกันไม่ให้ถูกส่งในรูปแบบข้อความที่อ่านได้)
- รวม Phoenixd** เข้ากับแอปพลิเคชันภายนอกที่ต้องการ HTTPS
- การปฏิบัติตามมาตรฐานความปลอดภัย**สำหรับ API ทางการเงิน



กำหนดค่า HTTPS reverse proxy นี้ด้วย nginx :



**1. Nginx** configuration



```bash
sudo apt install nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/phoenixd.conf
```



```nginx
server {
listen 80;
server_name phoenixd.your-domain.com;

location / {
proxy_pass http://127.0.0.1:9740;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header Host $host;
}
}
```



```bash
sudo ln -s /etc/nginx/sites-available/phoenixd.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```



**2. ใบรับรอง SSL**



```bash
sudo certbot --nginx -d phoenixd.your-domain.com
```



### ทดสอบฟังก์ชัน



ตรวจสอบว่า Phoenixd ทำงานอย่างถูกต้อง:



```bash
./phoenix-cli getinfo
./phoenix-cli getbalance
```



คำสั่งเหล่านี้ควรส่งคืนข้อมูล JSON เกี่ยวกับสถานะของโหนดและยอดคงเหลือ (เริ่มต้นว่างเปล่า)



![Commandes CLI](assets/fr/03.webp)



*คำสั่ง getinfo และ getbalance เพื่อตรวจสอบสถานะของโหนด*



## การใช้ API



### การทดสอบการต้อนรับครั้งแรก



**1. สร้างใบแจ้งหนี้ Lightning**



ใช้ API เพื่อสร้างใบแจ้งหนี้แรกของคุณ:



```bash
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='First test' \
-d amountSat=100000
```



### การทำความเข้าใจกลไกสภาพคล่องอัตโนมัติ



**หลักการพื้นฐาน:** เมื่อคุณได้รับการชำระเงินผ่าน Lightning บางครั้ง Phoenixd จำเป็นต้องเปิดช่องทางใหม่เพื่อให้สามารถรับการชำระเงินได้ การเปิดช่องทางนี้มีค่าใช้จ่ายซึ่งจะถูก **หักโดยอัตโนมัติ** จากจำนวนเงินที่ได้รับ



**ตัวอย่างคอนกรีตกับ 100,000 Sats:**



![Premier test de réception](assets/fr/04.webp)



*การทดสอบการยอมรับครั้งแรก: Sats ได้รับ 100k ยอดคงเหลือสุดท้ายของ Sats 75.561 หลังจากหักค่าใช้จ่ายด้านสภาพคล่อง*



```bash
# Payment received: 100,000 sats
# Channel created: 2,115,000 sats total capacity
# Liquidity fee: 24,439 sats
# Final balance: 75,561 sats
```



**การคำนวณค่าธรรมเนียม:**




- ค่าบริการ**: 1% ของความจุช่องสัญญาณ (2,115,000 Sats) = 21,150 Sats
- Mining fees**: ~3,289 Sats (for On-Chain transaction)
- รวม**: 24,439 Sats หักโดยอัตโนมัติ



**การตรวจสอบด้วยคำสั่ง CLI:**


```bash
# View details of all channels
./phoenix-cli listchannels

# Important output:
# "toLocal": 75561000 (your balance in milli-sats)
# "toRemote": 2039439000 (ACINQ's balance)
# Total channel: 2,115,000 sats
```



![Nouveau solde après paiement](assets/fr/05.webp)



*ยอดคงเหลือสุดท้ายหลังจากการชำระเงิน: 257 Sats เหลือหลังจากการจัดส่ง Lightning*



**เครดิตค่าธรรมเนียมสำหรับการชำระเงินขนาดเล็ก:** หากคุณได้รับการชำระเงินที่มีขนาดเล็กเกินกว่าที่จะเปิดช่องทางได้ (< ประมาณ 25k Sats) การชำระเงินเหล่านั้นจะถูกเก็บไว้ในรูปแบบ "เครดิตค่าธรรมเนียม" ที่ไม่สามารถขอคืนได้ เครดิตนี้จะถูกใช้เพื่อชำระค่าธรรมเนียมช่องทางในอนาคตเมื่อคุณได้รับจำนวนเงินที่เพียงพอ



**2. ติดตามการเปิดช่อง**



ดูบันทึก Phoenixd:



```bash
journalctl -u phoenixd -f
```



คุณจะเห็นการเปิดช่องทางและการหักค่าธรรมเนียมสภาพคล่องโดยอัตโนมัติ ค่าธรรมเนียมจะแตกต่างกันไปตามเงื่อนไข Mempool Bitcoin แต่จะรวมค่าบริการ 1% เสมอ บวกกับค่าธรรมเนียม mining ปัจจุบัน



**3. ตรวจสอบช่อง**



```bash
./phoenix-cli listchannels
```



คำสั่งนี้จะแสดงช่องทางที่ใช้งานอยู่ของคุณพร้อมสถานะและยอดคงเหลือ



### ดำเนินการ API ให้เสร็จสิ้น



Phoenixd เปิดเผย REST API บนพอร์ต 9740 ทำให้สามารถ:



**การดำเนินการพื้นฐาน:**


```bash
# Create an invoice
curl -X POST http://localhost:9740/createinvoice \
-u :your_password \
-d description='Test payment' \
-d amountSat=100000

# Send a payment (routing fee 0.4%)
curl -X POST http://localhost:9740/payinvoice \
-u :your_password \
-d invoice='lnbc...'

# Check balance
curl http://localhost:9740/getbalance \
-u :your_password

# Send on-chain funds (in case of channel closure)
./phoenix-cli sendtoaddress \
--address bc1q... \
--amountSat 50000 \
--feerateSatByte 12
```



**สำคัญเกี่ยวกับค่าใช้จ่าย:**




- ใบเสร็จ**: ค่าธรรมเนียม 1% + mining สำหรับสภาพคล่องอัตโนมัติ
- การจัดส่ง**: ค่าธรรมเนียมการกำหนดเส้นทาง 0.4% บนเครือข่าย Lightning



**Webhooks:** Webhooks ช่วยให้ Phoenixd สามารถ **แจ้งเตือนอัตโนมัติ** ไปยังแอปพลิเคชันของคุณเมื่อมีเหตุการณ์เกิดขึ้น (ได้รับการชำระเงิน, ใบแจ้งหนี้ที่ชำระแล้ว, ช่องทางที่เปิดแล้ว, ฯลฯ) แทนที่จะถามอัปเดตจาก Phoenixd ตลอดเวลา แอปพลิเคชันของคุณจะได้รับการแจ้งเตือน HTTP ทันที



**ร้านค้าออนไลน์ของคุณจะได้รับการแจ้งเตือนโดยอัตโนมัติเมื่อมีลูกค้าชำระเงินสำหรับการสั่งซื้อ ทำให้สามารถตรวจสอบความถูกต้องของธุรกรรมได้ทันที



การกำหนดค่าใน `phoenix.conf` :


```conf
webhook-url=https://your-app.com/webhook-phoenixd
webhook-secret=votre_secret_de_verification
```



## แอปพลิเคชันขั้นสูง



### การผสานรวม LNURL



Phoenixd รองรับโปรโตคอล LNURL โดยเนทีฟสำหรับการผสานรวมขั้นสูง:



**LNURL-Pay:** ชำระเงินสำหรับบริการที่รองรับ LNURL


```bash
curl -X POST http://localhost:9740/lnurlpay \
-u :your_password \
-d lnurl=LNURL1DP68GURN8GHJ7MRWW4EXCTN... \
-d amountSat=100
```



**LNURL-Withdraw :** ดึงเงินจากบริการ LNURL


```bash
curl -X POST http://localhost:9740/lnurlwithdraw \
-u :your_password \
-d lnurl=lightning:LNURL1DP68GURN8GHJ7MRW...
```



**LNURL-Auth:** การยืนยันตัวตนผ่าน Lightning เพื่อเข้าถึงบริการ


```bash
curl -X POST http://localhost:9740/lnurlauth \
-u :your_password \
-d lnurl=lnurl1dp68gurn8ghj7um5v93kket...
```



### การผสานรวมกับ LNbits



LNbits สามารถใช้ Phoenixd เป็นแหล่งเงินทุนได้ตาม [เอกสารอย่างเป็นทางการ](https://docs.lnbits.org/guide/wallets.html):



**LNbits configuration:**


```bash
LNBITS_BACKEND_WALLET_CLASS=PhoenixdWallet
PHOENIXD_API_ENDPOINT=http://localhost:9740/
PHOENIXD_API_PASSWORD=your_password_phoenixd
```



การผสานรวมนี้ช่วยให้คุณสามารถสร้างบัญชีย่อย LNbits ที่ขับเคลื่อนโดยโหนด Phoenixd ของคุณ โดยให้บริการ Interface บนเว็บสำหรับจัดการกระเป๋าเงิน Lightning หลายรายการ



### แอปพลิเคชันที่กำหนดเอง



ขอบคุณ REST API ที่ครอบคลุม คุณสามารถพัฒนา :



**อีคอมเมิร์ซ:** การผสานรวมการชำระเงินด้วย Lightning เข้ากับร้านค้าของคุณโดยตรง


**บริการบริจาค:** ระบบบริจาคพร้อมใบแจ้งหนี้และเว็บฮุคอัตโนมัติ


**บอทเครือข่ายสังคม:** Telegram/บอท Discord พร้อมฟังก์ชันการให้ทิป


**Paywall Lightning:** เนื้อหาระดับพรีเมียมที่สามารถเข้าถึงได้ด้วยค่าธรรมเนียม Lightning



## ความปลอดภัยและแนวทางปฏิบัติที่ดีที่สุด



### การป้องกันการเข้าถึง



**API รหัสผ่าน:** รหัสผ่านที่สร้างขึ้นโดยอัตโนมัติคือกุญแจสู่คลัง Lightning ของคุณ อย่าแชร์รหัสผ่านเหล่านี้ และเปลี่ยนรหัสผ่านหากมีข้อสงสัย



**ไฟร์วอลล์:** อย่าปล่อยให้พอร์ต 9740 เปิดตรงไปยังอินเทอร์เน็ต ควรใช้ nginx กับ HTTPS เสมอ



**การยืนยันตัวตนที่เพิ่มขึ้น:** พิจารณาใช้ VPN หรือ Tailscale เพื่อจำกัดการเข้าถึงเซิร์ฟเวอร์ของคุณเฉพาะอุปกรณ์ที่ได้รับอนุญาตเท่านั้น



### การสำรองข้อมูลที่จำเป็น



**seed recovery:** เก็บ 12 คำของคุณไว้ในที่ปลอดภัย นอกเซิร์ฟเวอร์ นี่คือการรับประกันเดียวของคุณในการกู้คืน



*~/.phoenix directory:** สำรองข้อมูลโฟลเดอร์นี้เป็นประจำ (หลังจากที่ Phoenixd ถูกปิดลง) เพื่อรักษาสถานะของช่องและเร่งความเร็วในการกู้คืน



**รหัสการกู้คืนบริการ:** เก็บรหัสสำรองสำหรับบริการทั้งหมดที่คุณเปิดใช้งาน 2FA ด้วย Phoenix ของคุณด้วย



### การตรวจสอบและบำรุงรักษา



**การตรวจสอบบันทึก:**


```bash
journalctl -u phoenixd -f  # Real-time logs
./phoenix-cli getinfo      # Node status
```



**อัปเดต:** ติดตาม [GitHub releases](https://github.com/ACINQ/phoenixd/releases) สำหรับเวอร์ชันใหม่ การอัปเดตทำได้ง่ายเพียงแค่แทนที่ไฟล์ไบนารีและเริ่มบริการใหม่



## การเปรียบเทียบกับทางเลือกอื่น



### ฟีนิกซ์ vs มาตรฐาน Phoenix



**Phoenix standard (mobile) :**




- ✅ การติดตั้งทันที ไม่ต้องกำหนดค่า
- ✅ Interface มือถือใช้งานง่าย
- ✅ การบันทึกอัตโนมัติแบบเดียวกับ Phoenixd
- ❌ ไม่มี API สำหรับนักพัฒนา
- ❌ ไม่มีการเข้าถึงบันทึกรายละเอียด



**Phoenixd (server) :**




- ✅ HTTP API สำหรับการผสานรวม
- ✅ เข้าถึงบันทึกได้เต็มรูปแบบ
- ✅ โครงสร้างพื้นฐานส่วนบุคคล
- ❌ ต้องการทักษะทางเทคนิค
- ❌ จำเป็นต้องบำรุงรักษาเซิร์ฟเวอร์



**ทั้งสองใช้ ACINQ เป็น LSP สำหรับสภาพคล่องอัตโนมัติ



### Phoenixd vs LND/Core Lightning



**LND/Core Lightning :**




- ✅ การควบคุมทั้งหมด, โปรโตคอล Lightning เต็มรูปแบบ
- ✅ ชุมชนขนาดใหญ่ ระบบนิเวศที่เติบโตเต็มที่
- ❌ การจัดการสภาพคล่องด้วยตนเองที่ซับซ้อน
- ❌ เส้นโค้งการเรียนรู้ที่สูง



**Phoenixd :**




- ✅ การจัดการสภาพคล่องอัตโนมัติ (เช่น Phoenix mobile)
- ✅ API สำหรับนักพัฒนา
- ✅ การกำหนดค่าที่ง่ายขึ้น
- ❌ ใช้ ACINQ เป็น LSP (ไม่มีการกำหนดเส้นทางอิสระ)
- ❌ ยืดหยุ่นน้อยกว่าปมที่สมบูรณ์



## การแก้ปัญหาทั่วไป



### ปัญหาการเข้าถึง API



ข้อผิดพลาด "การตรวจสอบสิทธิ์ล้มเหลว"


1. ตรวจสอบรหัสผ่านในไฟล์ `~/.phoenix/phoenix.conf`


2. ตรวจสอบรูปแบบการยืนยันตัวตน `-u:password`


3. ตรวจสอบให้แน่ใจว่า Phoenixd กำลังทำงานอยู่ (`./phoenix-CLI getinfo`)



**การหมดเวลาการเชื่อมต่อ:**




- ตรวจสอบว่า Phoenixd กำลังฟังอยู่บนพอร์ตที่ถูกต้อง (9740)
- ทดสอบการเข้าถึงภายในก่อนการกำหนดค่า HTTPS
- ตรวจสอบบันทึก: `journalctl -u phoenixd -f`



### ปัญหาสภาพคล่อง



**การชำระเงินไม่มาถึง :**


1. ตรวจสอบว่าจำนวนเงินเกินเกณฑ์ขั้นต่ำ (~30k Sats)


2. ตรวจสอบบันทึกเพื่อระบุข้อผิดพลาดของช่องทาง


3. รีสตาร์ท Phoenixd หากจำเป็น



**ยอดคงเหลือใน "เครดิตค่าใช้จ่าย":**


การชำระเงินขนาดเล็กจะถูกเก็บไว้เป็นการสำรอง รับจำนวนเงินที่มากขึ้นเพื่อกระตุ้นการเปิดช่องทางและปล่อยเงินเหล่านี้



## บทสรุป



Phoenixd เป็นการประนีประนอมที่ยอดเยี่ยมระหว่างความง่ายในการใช้งานและอธิปไตยทางเทคนิคสำหรับนักพัฒนา มันนำเสนอ Lightning API ที่เรียบง่ายแต่ทรงพลังพร้อมการจัดการสภาพคล่องอัตโนมัติ ซึ่งช่วยขจัดความซับซ้อนของโหนด Lightning แบบดั้งเดิม



โซลูชันนี้เหมาะอย่างยิ่งสำหรับนักพัฒนาและบริษัทที่ต้องการ:




- ผสานรวม Bitcoin Lightning เข้ากับแอปพลิเคชันของคุณ
- หลีกเลี่ยงความซับซ้อนของการจัดการช่องทาง Lightning
- ได้รับประโยชน์จากโครงสร้างพื้นฐานที่โฮสต์ด้วยตนเอง
- API ที่เรียบง่ายและเชื่อถือได้



ด้วย Phoenixd คุณสามารถสร้างโครงสร้างพื้นฐาน Lightning ส่วนตัวของคุณเองด้วย REST API ที่ทันสมัยและการจัดการด้านเทคนิคอัตโนมัติ เป็นโซลูชันที่เหมาะสมสำหรับการทำให้การรวม Lightning ในโครงการของคุณเป็นประชาธิปไตย



## แหล่งข้อมูลที่มีประโยชน์



### เอกสารอย่างเป็นทางการ




- GitHub Phoenixd** : [github.com/ACINQ/phoenixd](https://github.com/ACINQ/phoenixd) - ซอร์สโค้ดและการเผยแพร่
- เซิร์ฟเวอร์ Phoenix** เว็บไซต์: [phoenix.acinq.co/server](https://phoenix.acinq.co/server) - เอกสารประกอบฉบับเต็ม
- คำถามที่พบบ่อย Phoenixd** : [phoenix.acinq.co/server/faq](https://phoenix.acinq.co/server/faq) - คำถามที่พบบ่อย



### การสนับสนุนจากชุมชน




- GitHub Issues** : [github.com/ACINQ/phoenixd/issues](https://github.com/ACINQ/phoenixd/issues) - การสนับสนุนทางเทคนิค
- Twitter ACINQ** : [@ACINQ_co](https://twitter.com/ACINQ_co) - ข่าวสารและประกาศ