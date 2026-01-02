---
name: Lightning Smoke Machine
description: เรียกใช้งานเครื่องทำควันด้วยการชำระเงิน Lightning ผ่าน ESP32
---

![cover-lightning-smoke-machine](assets/cover.webp)



## บทนำ



เปลี่ยนเครื่องทำควันคลาสสิกให้เป็นอุปกรณ์ที่ชำระเงินได้ใน Bitcoin ผ่าน Lightning Network การชำระเงินแต่ละครั้งจะกระตุ้นให้เกิดควันพุ่งออกมาโดยอัตโนมัติ!





- ระดับ: ปานกลาง
- เวลาที่คาดการณ์: 2-3 ชั่วโมง
- กรณีการใช้งาน: งาน Bitcoin, การแสดงศิลปะ, การสาธิต Lightning, เอฟเฟกต์เวทีอัตโนมัติ



## ข้อกำหนดเบื้องต้น



### ความรู้





 - อิเล็กทรอนิกส์พื้นฐาน (การเดินสายไฟ, รีเลย์)
 - การเชื่อม (หรือการใช้ขั้วต่อ Dupont)
 - การกำหนดค่าเครือข่าย (WiFi, WebSocket)



### บัญชีที่จำเป็น





- BTCPay Server: อินสแตนซ์ที่ใช้งานได้ (โฮสต์เองหรือโฮสต์)
- Blink Wallet : บัญชี + เข้าถึง API



### การเข้าถึง





- การเข้าถึงผู้ดูแลระบบไปยัง BTCPay Server
- การเชื่อมต่อ WiFi สำหรับ ESP32



## วัสดุที่ต้องใช้



### ฮาร์ดแวร์ - ส่วนประกอบอิเล็กทรอนิกส์





- 1 ไมโครคอนโทรลเลอร์ - ESP32-WROOM-32


*ESP32-WROOM-32 เป็นไมโครคอนโทรลเลอร์ WiFi/Bluetooth ขนาดกะทัดรัด ราคาประหยัด สำหรับเชื่อมต่ออุปกรณ์อิเล็กทรอนิกส์กับอินเทอร์เน็ตและควบคุมจากระยะไกล*



![ESP32](assets/fr/1.webp)





- 1 รีเลย์โมดูล - 5V พร้อมออปโตคัปเปลอร์


*รีเลย์เปรียบเสมือนสวิตช์ที่ ESP32 สามารถใช้งานเพื่อเปิดหรือปิดเครื่องทำควัน*



![relay](assets/fr/2.webp)





- ~10 สาย Dupont - ชาย/ชาย และ ชาย/หญิง



![dupont-cables](assets/fr/3.webp)





- 1 แหล่งจ่ายไฟสำหรับ ESP32 - 5V USB หรือแบตเตอรี่ Li-Po



![battery](assets/fr/4.webp)





- สาย micro-USB 1 เส้น - การเชื่อมต่อระหว่าง ESP32 และแหล่งจ่ายไฟ



![micro-usb-cables](assets/fr/5.webp)





- เครื่องทำหมอก 220V 1 เครื่อง พร้อมรีโมทคอนโทรลแบตเตอรี่ 12V



![remote-and-smoke-machine](assets/fr/6.webp)





- 1 ขวดของเหลวที่เข้ากันได้กับเครื่องทำควันของคุณ



### ฮาร์ดแวร์ - เครื่องมือ





- หัวแร้งบัดกรี + ตะกั่ว (ถ้าบัดกรี)
- ไขควง
- มัลติมิเตอร์ (แนะนำ)



### ซอฟต์แวร์





- เฟิร์มแวร์ BitcoinSwitch : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- เว็บเบราว์เซอร์ที่รองรับ WebSerial (Chrome/Edge/Brave)
- BTCPay Server ถูกตั้งค่าแล้ว สำหรับข้อมูลเพิ่มเติมเกี่ยวกับการสร้างอินสแตนซ์ BTCPay Server โปรดเยี่ยมชมบทแนะนำนี้: https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc



## สถาปัตยกรรมระบบ



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **คำเตือนด้านความปลอดภัย - อ่านก่อนดำเนินการต่อ** **⚠️**



โครงการนี้เกี่ยวข้องกับเครื่องทำหมอกที่เชื่อมต่อกับ **แหล่งจ่ายไฟหลัก 220V** การใช้งานที่ไม่ถูกต้องอาจส่งผลให้เกิด **ไฟฟ้าช็อตถึงตาย** หรือ **ไฟไหม้**



**กฎที่ไม่สามารถต่อรองได้:**



1. **ตัดการเชื่อมต่อเครื่องทำควันจากแหล่งจ่ายไฟเสมอ** ก่อนเปิดรีโมทคอนโทรลหรือยุ่งเกี่ยวกับสายไฟ


2. **ถอดแบตเตอรี่ออกจากรีโมทคอนโทรล** ก่อนการจัดการ (เสี่ยงต่อการลัดวงจรและความเสียหายต่อส่วนประกอบ)


3. **ตรวจสอบว่าการเชื่อมต่อทั้งหมดของคุณถูกแยกออก** ก่อนที่จะเชื่อมต่อสิ่งใดใหม่


4. **อย่าเชื่อมต่อ 220V อีกครั้ง** จนกว่ากล่องควบคุมระยะไกลจะถูกปิดและยึดให้แน่น



หากคุณไม่สะดวกใจกับการจัดการแบบนี้ ให้พาคนที่สะดวกไปด้วย



---

## PART 1: การประกอบฮาร์ดแวร์



### ขั้นตอนที่ 1: การเตรียมรีโมทคอนโทรล



วัตถุประสงค์: เชื่อมต่อรีเลย์กับปุ่มเปิด/ปิดบนรีโมทคอนโทรล


1. เปิดรีโมทคอนโทรล




    - ระบุปุ่มเปิด/ปิด
    - คลายเกลียวเคสเพื่อเปิดรีโมทคอนโทรล


2. ค้นหาการเชื่อมต่อ




 - ค้นหาขั้ว + และ - ของ
 - ทดสอบความต่อเนื่องด้วยมัลติมิเตอร์ (ไม่บังคับ)



![smoke-machine-remote](assets/fr/8.webp)



3. การเดินสายปุ่ม (บัดกรีหรือขั้วต่อ)




    - บัดกรีสายสีดำเข้ากับขั้ว - ของปุ่ม
    - บัดกรีสายสีแดงเข้ากับขั้ว + ทั่วไป



![smoke-machine-remote](assets/fr/9.webp)



### ขั้นตอนที่ 2: การเชื่อมต่อกับโมดูลรีเลย์



**Reminder: Relay terminology



| **Terminal**         | **Description**           | **Fonction**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit ouvert par défaut | Se ferme quand le relais est activé |
| NC (Normally Closed) | Circuit fermé par défaut  | S'ouvre quand le relais est activé  |
| COM (Common)         | Terminal central          | Bascule entre NO et NC              |

**การเดินสายจากรีโมทคอนโทรลไปยังโมดูลรีเลย์:**




- สายสีดำจากปุ่มเปิด/ปิด **→** NO (Normally Open)
- สายสีแดง (common) **→** COM (Common)



**ตรรกะ:**


เมื่อ ESP32 เปิดใช้งานรีเลย์ มันจะเชื่อมต่อ COM และ NO ซึ่งเหมือนกับการกดปุ่มรีโมทคอนโทรลทุกประการ


เมื่อ ESP32 ตัดรีเลย์, COM และ NO แยกออกจากกัน, ซึ่งเทียบเท่ากับการปล่อยปุ่ม



![remote-relay](assets/fr/10.webp)



### ขั้นตอนที่ 3: การเชื่อมต่อ ESP32 กับโมดูลรีเลย์



**แผนผังการเดินสายไฟ:**



| **ESP32** | **→** | **Module relais** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |

**การยืนยัน:**




- VCC และ GND เชื่อมต่อกันดี (ขั้ว)
- GPIO 21 ใช้สำหรับสัญญาณควบคุม
- ไม่มีการลัดวงจรที่มองเห็นได้



![relay-esp32](assets/fr/11.webp)



**ฮาร์ดแวร์เช็คพอยต์**


ก่อนเปลี่ยนไปใช้ซอฟต์แวร์ ตรวจสอบ :




- รีโมทคอนโทรลที่เดินสายอย่างถูกต้อง
- โมดูลรีเลย์เชื่อมต่อกับ ESP32
- ไม่มีสายไฟเปลือยสัมผัสกับส่วนประกอบอื่น
- 220V ตัดการเชื่อมต่อเสมอ



![relay-esp32](assets/fr/12.webp)





---


## ส่วนที่ 2: การกำหนดค่าซอฟต์แวร์



เราจะใช้ *Blink* เป็นตัวอย่าง แต่ *BTCPay Server* ก็มี *Strike, Breez และ Boltz* หากคุณต้องการตัวเลือกอื่น



### ขั้นตอนที่ 1: ปลั๊กอิน, การติดตั้ง *BitcoinSwitch* + *Blink



1 - ไปที่ *BTCPay Server* อินสแตนซ์ของคุณด้วยบัญชีผู้ดูแลระบบ



2 - สร้างบลายด์แรกของคุณ



3 - ที่ด้านซ้ายมือของ *BTCPay Server* เลื่อนลงไปที่ด้านล่างและไปที่ *"Manage Plugins "*



![btcpay-plugins](assets/fr/13.webp)



4 - เราจะติดตั้งปลั๊กอิน *BitcoinSwitch* รวมถึง *Blink*



![btcpay-plugins](assets/fr/14.webp)



5 - เลื่อนลงในรายการปลั๊กอินและคลิกที่ *"Install "* : *BitcoinSwitch and Blink* (หรือ wallet ที่มีให้เลือก)



![btcpay-plugins](assets/fr/15.webp)



6 - เมื่อการติดตั้งเสร็จสิ้น ให้รีสตาร์ท *BTCPay Server* และรอ 1 นาทีเพื่อให้ instance รีสตาร์ท



![btcpay-plugins](assets/fr/16.webp)



7 - เมื่อคุณกลับไปที่ *"จัดการปลั๊กอิน"*, ตรวจสอบว่าทั้งสองปลั๊กอินได้ถูกติดตั้งแล้ว



![btcpay-plugins](assets/fr/17.webp)



### ขั้นตอนที่ 2: แบ็กเอนด์ : *BTCPay Server + Blink* การกำหนดค่า



**1 - สร้าง wallet *Blink***




- เยี่ยมชม https://www.blink.sv
- สร้างบัญชีของคุณ โปรดดูที่บทแนะนำ :



[https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd](https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - สร้างคีย์ API *Blink***




- เข้าถึงอินเทอร์เฟซ API: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)** และเข้าสู่ระบบด้วยบัญชีเดียวกับที่คุณใช้สร้าง wallet *Blink*



![blink-api](assets/fr/18.webp)





   - เมื่อเชื่อมต่อแล้ว ให้ไปที่แท็บ *API Keys*



![blink-api](assets/fr/19.webp)





   - คลิกที่ *" + "* ที่มุมขวาบนเพื่อเข้าถึงการตั้งค่าคีย์ API ของคุณ



![blink-api](assets/fr/20.webp)





   - ตั้งชื่อให้กับคีย์ API ของคุณและปล่อยให้การตั้งค่าเริ่มต้น จากนั้นในขั้นตอนที่สาม ให้จดบันทึกคีย์ API ของคุณ - คุณจะเห็นมันเพียงครั้งเดียว: `blink_mZ5KxxxxxxxxxxxxxNbmX`



![blink-api](assets/fr/21.webp)





   - เมื่อสร้างแล้ว ควรปรากฏในรายการคีย์ API ที่ใช้งานของคุณ



![blink-api](assets/fr/22.webp)



**3 - เชื่อมต่อ *Blink* กับ *BTCPay Server***




- เปิด *BTCPay Server* ของคุณ
- นำทางไปที่ : *Wallet* **→** *Lightning*



![btcpay-server](assets/fr/23.webp)





- คลิกที่ *ใช้โหนดที่กำหนดเอง*
- วางสตริงการเชื่อมต่อดังต่อไปนี้:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **Important** : สำคัญ




- Do not modify the first part: `type=blink;server=https://api.blink.sv/graphql`;
- แทนที่เฉพาะ :
    - api-key= *by your API Blink* key
    - wallet-id= *by your wallet Blink* ID
- จากนั้นคลิกที่ *ทดสอบการเชื่อมต่อ* แล้วคลิก *บันทึก*



![btcpay-server](assets/fr/24.webp)





 - ตรวจสอบว่าการเชื่อมต่อได้รับการสร้างขึ้นแล้ว (สถานะสีเขียว)



![btcpay-server](assets/fr/25.webp)



**4 - สร้างจุดขาย (PoS)**




- ใน BTCPay Server ไปที่แท็บ *Plugins* และคลิกที่ *Point of sale*



![btcpay-server](assets/fr/26.webp)





- ตั้งชื่อ PoS ของคุณแล้วคลิกที่ *Create*



![btcpay-server](assets/fr/27.webp)





- การกำหนดค่า PoS :
    - เลือกสไตล์จุดขาย = *แสดงผลการพิมพ์*
    - สกุลเงิน = *SATS*
    - คลิกที่ *บันทึก*



![btcpay-server](assets/fr/28.webp)





- การกำหนดค่าผลิตภัณฑ์ :
    - ลบสินค้าทั้งหมดที่ตั้งค่าเริ่มต้น
    - จากนั้นคลิกที่ *add item*



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- กำหนดค่าผลิตภัณฑ์:
    - ชื่อเรื่อง : *เครื่องทำหมอกควัน*
    - ราคา : *10 sats*
    - Bitcoin GPIO switch : 21
    - Bitcoin switch duration (in milliseconds) : 5000
    - คลิกที่ *Close* แล้วคลิก *Save* เพื่อบันทึกผลิตภัณฑ์ใหม่



![btcpay-server](assets/fr/31.webp)



### ขั้นตอนที่ 3: เฟิร์มแวร์: การแฟลช ESP32



**1 - ไปที่เว็บไซต์แฟลช




- ไปที่ : [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash เฟิร์มแวร์ BitcoinSwitch**




- เชื่อมต่อ ESP32 กับคอมพิวเตอร์ของคุณด้วยสาย USB/Micro-USB
- จากนั้นคลิกที่ *Connect to Device*
- หน้าต่างจะเปิดขึ้น ให้เลือกพอร์ต USB บน ESP32 ของคุณ จากนั้นคลิกที่ *Connect*



![bitcoinswitch-lnbits](assets/fr/33.webp)





- เมื่อเชื่อมต่อ ESP32 ของคุณแล้ว เราจะทำการแฟลชเฟิร์มแวร์ BitcoinSwitch ในส่วนของ *T-Display* ให้คลิกที่ *Upload Firmware* สำหรับเวอร์ชันล่าสุดที่มีอยู่ (ปัจจุบัน: *bitcoinSwitch T-Display v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- รอการอัปโหลด กระบวนการจะเสร็จสมบูรณ์เมื่อบันทึกแสดง *"Leaving... "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- ถอดปลั๊ก ESP32



**3 - ตรวจสอบการติดตั้งเฟิร์มแวร์ BitcoinSwitch




- โหลดหน้าใหม่: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- เชื่อมต่อ ESP32 กับคอมพิวเตอร์ของคุณอีกครั้งด้วยสาย USB/Micro-USB
- จากนั้นคลิกที่ *เชื่อมต่อกับอุปกรณ์
- เลือกพอร์ต USB บน ESP32 ของคุณ จากนั้นคลิกที่ *Connect* ตามที่อธิบายไว้ข้างต้น
- เมื่อเชื่อมต่อแล้ว ให้กดปุ่ม **RESET** บน ESP32
- ตรวจสอบในบันทึกว่าบรรทัดสุดท้ายแสดง :



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(นี่เป็นเรื่องปกติ หมายความว่ายังไม่มีการตั้งค่า แต่เฟิร์มแวร์ได้ถูกติดตั้งแล้ว)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - สร้าง WebSocket LNURL** URL



รูปแบบสุดท้ายที่คาดหวัง :



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



ขั้นตอนการสร้าง :




- เปิดอินสแตนซ์ BTCPay Server ของคุณ จากนั้นไปที่ PoS ที่เราสร้างขึ้นในภายหลัง
- จากนั้นคลิกที่ "View" เพื่อเปิด PoS ของคุณในเบราว์เซอร์



![btcpay-server-https](assets/fr/37.webp)





- คัดลอก URL ของหน้า ตัวอย่างเช่น :



![btcpay-server-https](assets/fr/38.webp)



มาวิเคราะห์ URL นี้กัน:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → โดเมนของอินสแตนซ์ BTCPay Server ของคุณ
- `46XXXXXXXXXXXXXXXXXXXXwFB` → ตัวระบุเฉพาะ PoS ของคุณ
- `/pos` → หมายถึง จุดขาย



แปลงมัน:




- แทนที่ `https://` ด้วย `wss://`
- เพิ่ม `/bitcoinswitch` ที่ท้ายสุด



ผลลัพธ์:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



เก็บ URL นี้ไว้สำหรับการกำหนดค่าในอนาคต เนื่องจากจะช่วยให้ ESP32 ของคุณสามารถสื่อสารแบบเรียลไทม์กับ BTCPay Server ได้ โปรโตคอล WebSocket (`wss://`) จะสร้างการเชื่อมต่อถาวรระหว่างทั้งสอง: ทันทีที่การชำระเงินด้วย Lightning ได้รับการยืนยันบน PoS ของคุณ BTCPay จะส่งข้อมูลไปยัง ESP32 ทันที ซึ่งสามารถกระตุ้นเครื่องทำควันของคุณได้



**5 - การกำหนดค่า WiFi และ WebSocket




- กลับไปที่หน้า: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/) พร้อมกับเชื่อมต่อ ESP32 ของคุณ
- ไปที่ *Configure Device* → *Wifi Settings*



แจ้ง :




- ชื่อเครือข่าย WiFi: ชื่อของเครือข่าย WiFi ของคุณ
- WiFi Password: your WiFi password



![bitcoinswitch-lnbits](assets/fr/39.webp)





- ในส่วน *LNbits Device URL* วาง URL ของ WebSocket ที่สร้างขึ้นในขั้นตอนก่อนหน้า
- คลิกที่ *อัปโหลดการกำหนดค่า*



![bitcoinswitch-lnbits](assets/fr/40.webp)





- รอให้การอัปโหลดเสร็จสิ้น; บันทึกควรแสดงพารามิเตอร์ที่คุณเพิ่งป้อน (SSID, รหัสผ่าน และ URL ของ WebSocket)



![bitcoinswitch-lnbits](assets/fr/41.webp)





- รอในขณะที่ ESP32 กำลังสร้างการเชื่อมต่อ WebSocket คุณควรเห็น:



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- คุณสามารถตัดการเชื่อมต่อ ESP32 ได้แล้ว



---
## เช็คพอยท์ ซอฟต์แวร์



ก่อนการทดสอบครั้งสุดท้าย ตรวจสอบ :





- Blink เชื่อมต่อกับ BTCPay
- สร้าง PoS ด้วยอย่างน้อย 1 รายการ
- ESP32 flashed with BitcoinSwitch
- WiFi ถูกตั้งค่าบน ESP32
- URL WebSocket ถูกต้อง
- บันทึก ESP32 ที่ไม่มีข้อผิดพลาด



---

## การทดสอบและการดีบัก



### ทำแบบทดสอบสุดท้ายให้เสร็จสิ้น



1. เสียบปลั๊กเครื่องทำควัน (220V) และเปิดเครื่อง


2. จ่ายไฟให้ ESP32 (แบตเตอรี่หรือ USB)


3. เปิด BTCPay PoS ของคุณในเบราว์เซอร์ของคุณ


4. สแกนรายการ "smoke-machine"


5. ชำระเงินด้วย wallet Lightning (Blink หรือ wallet อื่น ๆ)


6. สังเกต:




 - รีเลย์คลิก (เสียงที่ได้ยินและไฟ LED ของรีเลย์สว่างขึ้น)
 - เครื่องทำควันถูกเปิดใช้งาน
 - เกิดควัน!



### ปัญหาความเป็นธรรมและวิธีแก้ไข



| **Problème**                        | **Cause probable**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 ne se connecte pas            | Driver USB manquant             | Installer [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relais ne clique pas                | Mauvais câblage GPIO            | Vérifier GPIO 21 → IN                                                                        |
| Smoke machine ne réagit pas         | Télécommande mal câblée         | Vérifier NO/NC/COM                                                                           |
| WebSocket timeout                   | URL incorrecte                  | Vérifier wss:// et /bitcoinswitch                                                            |
| WiFi ne se connecte pas             | SSID/Password erroné            | Re-flasher la config WiFi                                                                    |
| Paiement reçu mais rien ne se passe | ESP32 non connecté au WebSocket | Vérifier les logs RESET                                                                      |

## ทรัพยากร



### ลิงก์ที่มีประโยชน์





- BitcoinSwitch Firmware: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- BTCPay Server Docs : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 Pinout : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### ชุมชนและการสนับสนุน





- BTCPay Server** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - Official Mattermost
- BTCPay Server Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - ชุมชนอย่างเป็นทางการ Telegram, ชุมชนที่มีความเคลื่อนไหว
- BitcoinSwitch (firmware bugs)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### ซอร์สโค้ด





- ซอร์สโค้ดเฟิร์มแวร์ BitcoinSwitch: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** สแต็ก sats สร้างควัน สนุกสนาน และถ่อมตน! **⚡**