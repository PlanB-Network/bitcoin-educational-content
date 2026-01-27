---
name: Bitaxe
description: วิธีการตั้งค่า BitAxe?
---
![video](https://youtu.be/tvLSK8v0MK8)


## บทนำ


BitAxe เป็นโครงการโอเพนซอร์สที่สร้างโดย Skot และ [มีให้ใช้งานบน GitHub](https://github.com/skot/bitaxe) ซึ่งช่วยให้สามารถทดลอง mining ได้อย่างคุ้มค่า


มันได้ทำการย้อนกลับวิศวกรรมการทำงานของ Antminer S19 ที่มีชื่อเสียงโดย Bitmain ซึ่งเป็นผู้นำตลาดในด้าน ASICs เครื่องจักรเฉพาะทางสำหรับ bitcoin mining ตอนนี้สามารถใช้ชิปที่ทรงพลังเหล่านี้ในโครงการโอเพ่นซอร์สใหม่ ๆ ได้แล้ว ไม่เหมือนกับ Nerdminer, BitAxe มีพลังการประมวลผลเพียงพอที่จะเชื่อมต่อกับพูล mining ซึ่งจะช่วยให้คุณได้รับ satoshis เป็นประจำ ในทางกลับกัน Nerdminer สามารถเชื่อมต่อได้เฉพาะกับสิ่งที่เรียกว่า solopool ซึ่งทำงานเหมือนกับตั๋วลอตเตอรี่: คุณมีโอกาสน้อยที่จะชนะรางวัลบล็อกทั้งหมด


มีหลายเวอร์ชันของ BitAxe ที่มีชิปและประสิทธิภาพที่แตกต่างกัน:


| Bitaxe Model Series      | ASIC Chip | Used On                     | Expected Hash Rate          | Ideal For                                                                                                  |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Series 100)  | 1 x BM1397| Antminer Series 17          | 400 GH/s (up to 450 GH/s)   | Bitcoin mining beginners, offering a solid hash rate with moderate power consumption.                      |
| Bitaxe Ultra (Series 200)| 1 x BM1366| Antminer S19 XP and S19k Pro| 500 GH/s (up to 550 GH/s)   | Serious miners aiming to balance efficiency and higher hash rate.                                          |
| Bitaxe Hex (Series 300)  | 6 x BM1366| Antminer S19k Pro and S19 XP| 3.0 TH/s (up to 3.3 TH/s)   | Miners seeking scalability and high performance without sacrificing efficiency.                             |
| Bitaxe Supra (Series 400)| 1 x BM1368| Antminer S21                | 600 GH/s (up to 700 GH/s)   | Serious enthusiasts seeking the highest hash rates and efficiency.                                         |

ในบทแนะนำนี้ เราจะใช้ BitAxe Ultra 204 ที่ติดตั้งชิป BM1366 ซึ่งใช้สำหรับ Antminer S19XP อันนี้ได้รับการประกอบและแฟลชโดยผู้ค้าปลีกแล้ว


[รายชื่อผู้ค้าปลีกมีอยู่ในหน้านี้](https://bitaxe.org/legit.html)


![signup](assets/2.webp)


โดยทั่วไปแล้ว แหล่งจ่ายไฟจะขายพร้อมกับมัน หากไม่เป็นเช่นนั้น คุณจะต้องซื้อแหล่งจ่ายไฟที่มีสายแจ็ค 5V และอย่างน้อย 4A


![signup](assets/1.webp)


## การกำหนดค่า

เมื่อคุณเสียบ BitAxe ของคุณเป็นครั้งแรก มันจะพยายามเชื่อมต่อกับเครือข่าย Wi-Fi โดยค่าเริ่มต้น หลังจากพยายามห้าครั้ง มันจะแสดงชื่อเครือข่าย Wi-Fi ของตัวเองเพื่อให้คุณสามารถเชื่อมต่อและกำหนดค่าได้

ในการทำเช่นนี้ คุณสามารถใช้คอมพิวเตอร์หรือสมาร์ทโฟนใดก็ได้ ไปที่การตั้งค่า Wi-Fi ของคุณ ค้นหาเครือข่ายใหม่ แล้วคุณจะเห็น Wi-Fi ที่ชื่อว่า Bitaxe_XXXX ที่นี่คือ `Bitaxe_A859` เชื่อมต่อกับเครือข่าย Wi-Fi นี้ แล้วหน้าต่างจะเปิดขึ้นโดยอัตโนมัติ


![signup](assets/3.webp)


ในหน้าต่างนี้ ให้คลิกที่แถบแนวนอนเล็ก ๆ สามแถบที่มุมบนซ้าย จากนั้นคลิกที่ `Settings`


![signup](assets/4.webp)


คุณจะต้องป้อนข้อมูลเครือข่าย Wi-Fi ของคุณด้วยตนเอง เนื่องจากไม่มีระบบค้นหาอัตโนมัติ


![signup](assets/5.webp)


ดังนั้น ให้ระบุ SSID ของ Wi-Fi นั่นคือ ชื่อของเครือข่ายของคุณ รหัสผ่าน รวมถึงข้อมูลของกลุ่ม mining ที่คุณเลือก ระวังให้ดี ที่นี่ URL ของกลุ่มไม่ได้แสดงในรูปแบบเดียวกัน ตัวอย่างเช่น สำหรับ Braiins URL ของกลุ่มที่ให้มาคือ: `stratum+tcp://eu.stratum.braiins.com:3333`.


![signup](assets/6.webp)


ตามที่คุณเห็นบนหน้าจอ คุณจำเป็นต้องลบส่วน `stratum+tcp://` และ `:3333` ออก เหลือเพียง `eu.stratum.braiins.com` จากนั้น ในช่อง `Port` ให้ใส่ตัวเลข 4 หลักที่อยู่ท้าย URL ที่ให้โดยพูล แต่ไม่ต้องใส่ `:` ที่นี่จึงเป็น `3333`


ในบทแนะนำนี้ เรากำลังใช้ Braiins mining pool แต่คุณสามารถเลือกใช้ pool อื่นได้ คุณสามารถหาบทแนะนำของเราเกี่ยวกับ mining pools [บนเว็บไซต์ Plan ₿ Academy](https://planb.academy/en/tutorials/mining)


ถัดไป ใน `User` ป้อนตัวระบุของคุณแล้วตามด้วย `Password` โดยปกติจะเป็น `"x"` หรือ `"Anything123"`


การตั้งค่า `Core Voltage` ควรปล่อยไว้ที่ `1200` ตามค่าเริ่มต้น และสำหรับ `Frequency` ก็ให้ปล่อยค่าเริ่มต้นไว้เช่นกันในตอนแรก สามารถปรับการตั้งค่านี้ได้ในภายหลังเพื่อให้ได้พลังการประมวลผลมากขึ้น อย่างไรก็ตาม สิ่งสำคัญคือต้องมั่นใจว่าอุณหภูมิของชิปจะไม่เกิน 65-70°C เนื่องจาก BitAxe ไม่มีระบบลดประสิทธิภาพในกรณีที่เกิดความร้อนสูงเกินไป หากอุณหภูมิเกิน 65°C มากเกินไป อาจทำให้ BitAxe ของคุณเสียหายได้


![signup](assets/7.webp)


เมื่อคุณป้อนการตั้งค่าทั้งหมดถูกต้องแล้ว ให้คลิกปุ่ม `Save` ที่ด้านล่าง จากนั้นรีสตาร์ท BitAxe ของคุณโดยการถอดปลั๊กแล้วเสียบกลับเข้าไปใหม่

หากคุณป้อนข้อมูลของคุณถูกต้อง อุปกรณ์ควรเชื่อมต่อกับ Wi-Fi ของคุณอย่างรวดเร็ว จากนั้นเชื่อมต่อกับกลุ่ม mining และเริ่มแสดงข้อมูลบางอย่างบนหน้าจอขนาดเล็กของมัน อาจใช้เวลาสองสามนาทีกว่าที่มันจะปรากฏบนแดชบอร์ดของกลุ่ม mining

## แดชบอร์ดและหน้าจอ


หน้าจอแสดงผลสามแบบจะแสดงผลแบบเลื่อน ในหน้าที่สาม คุณจะเห็นข้อมูล `IP` ซึ่งเป็นที่อยู่ IP ที่อนุญาตให้คุณเชื่อมต่อกับแดชบอร์ด ที่นี่ ที่อยู่คือ `192.168.1.19`


![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)


ในการเข้าถึงแดชบอร์ด เพียงป้อนที่อยู่นี้ลงในเบราว์เซอร์อินเทอร์เน็ตของคุณ


บนแผงควบคุม คุณจะพบข้อมูลทั้งหมดที่แสดงบนหน้าจอขนาดเล็ก ซึ่งเราจะมาดูรายละเอียดกันตอนนี้


![signup](assets/11.webp)


| BitAxe Screen | Dashboard                                   | Description                                                                                                                                                                                                               |
| ------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gh            | Hashrate                                    | The current computing power, expressed in GigaHash/s                                                                                                                                                                      |
| W/THs         | Efficiency                                  | This is the efficiency of your BitAxe expressed in W/THs. It's the ratio between the electrical power consumed and the computing power produced.                                                                          |
| A/R           | Shares                                      | Quantity of `Shares` sent by your BitAxe to the pool, representing the amount of work provided.                                                                                                                          |
| UT            | Uptime                                      | Time since your BitAxe has been operating without interruption (available in the left menu under `Logs`).                                                                                                                |
| BD            | Best Difficulty                             | Maximum difficulty reached since the last restart. For comparison, the current network difficulty is about 85T.                                                                                                          |
| FAN           | FAN in the `Heat` box                       | Fan rotation speed, expressed in rotations per minute.                                                                                                                                                                    |
| Temp          | ASIC temperature in the `Heat` box          | Chip temperature, which should not exceed 65°C.                                                                                                                                                                           |
| Pwr           | Power                                       | Power in watts consumed. However, this information does not take into account the screen, the fan, or the power supply. For example, when it displays 11.7W, the total consumption is actually 15.8W.                    |
| mV mA         | Input Voltage Input Current                 | Voltage and current consumed by the machine. The power in watts is equal to the voltage multiplied by the current.                                                                                                        |
| FH            | Free Heap Memory (left menu -> `Logs`)      | The available memory.                                                                                                                                                                                                     |
| vCore         | ASIC Voltage (in the Performance box)       | Voltage measured on the ASIC chip.                                                                                                                                                                                        |
| IP            | NA                                          | IP Address.                                                                                                                                                                                                               |
| V2.1.0       | Version (left menu -> `Logs`)               | Firmware version.                                                                                                                                                                                                         |

คุณสามารถเปลี่ยนการตั้งค่า Wi-Fi หรือสระว่ายน้ำได้ตลอดเวลาโดยไม่มีปัญหาใดๆ

ขึ้นอยู่กับการระบายอากาศและอุณหภูมิของห้องของคุณ คุณอาจจำเป็นต้องเพิ่มหรืออาจต้องลดประสิทธิภาพเพื่อไม่ให้อุณหภูมิเกิน 65°C หากคุณเพิ่มประสิทธิภาพ คุณจะได้รับซาโตชิมากขึ้น แต่ BitAxe ของคุณก็จะใช้ไฟฟ้ามากขึ้นด้วย!