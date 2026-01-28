---
name: เพิ่มกิจกรรมบน Plan ₿ Academy
description: ฉันจะเสนอให้เพิ่มกิจกรรมใหม่บน Plan ₿ Academy ได้อย่างไร?
---
![event](assets/cover.webp)


ภารกิจของ PlanB คือการจัดหาทรัพยากรการศึกษาชั้นนำเกี่ยวกับ Bitcoin ในหลายภาษามากที่สุดเท่าที่จะเป็นไปได้ เนื้อหาทั้งหมดที่เผยแพร่บนเว็บไซต์เป็นโอเพ่นซอร์สและโฮสต์บน GitHub เปิดโอกาสให้ทุกคนมีส่วนร่วมในการพัฒนาแพลตฟอร์มนี้


หากคุณต้องการเพิ่มการประชุม Bitcoin ไปยังไซต์ Plan ₿ Academy และเพิ่มการมองเห็นสำหรับงานของคุณ แต่ไม่รู้ว่าจะทำอย่างไร? บทแนะนำนี้เหมาะสำหรับคุณ!

![event](assets/01.webp)


- ก่อนอื่น คุณจำเป็นต้องมีบัญชีบน GitHub หากคุณไม่ทราบวิธีการสร้างบัญชี เราได้จัดทำบทแนะนำอย่างละเอียดเพื่อแนะนำคุณแล้ว


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- ไปที่ [GitHub repository ของ PlanB ที่อุทิศให้กับข้อมูล](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) ในส่วน `resources/conference/`:

![event](assets/02.webp)


- คลิกที่มุมขวาบนที่ปุ่ม `Add file` จากนั้นคลิกที่ `Create new file`:

![event](assets/03.webp)


- หากคุณไม่เคยมีส่วนร่วมในเนื้อหาของ Plan ₿ Academy มาก่อน คุณจะต้องสร้าง fork ของที่เก็บต้นฉบับ การ Fork ที่เก็บหมายถึงการสร้างสำเนาของที่เก็บนั้นในบัญชี GitHub ของคุณเอง ทำให้คุณสามารถทำงานในโครงการได้โดยไม่กระทบต่อที่เก็บต้นฉบับ คลิกที่ปุ่ม `Fork this repository`:

![event](assets/04.webp)


- จากนั้นคุณจะไปถึงหน้าการแก้ไข GitHub:

![event](assets/05.webp)


- สร้างโฟลเดอร์สำหรับการประชุมของคุณ ในช่อง `ตั้งชื่อไฟล์ของคุณ...` ให้เขียนชื่อการประชุมของคุณเป็นตัวพิมพ์เล็กและใช้ขีดกลางแทนช่องว่าง ตัวอย่างเช่น หากการประชุมของคุณชื่อ "Paris Bitcoin Conference" คุณควรเขียนว่า `paris-bitcoin-conference` นอกจากนี้ให้เพิ่มปีของการประชุมของคุณ เช่น: `paris-bitcoin-conference-2024`:

![event](assets/06.webp)


- ในการยืนยันการสร้างโฟลเดอร์ เพียงแค่ใส่เครื่องหมายทับหลังจากชื่อของคุณในช่องเดียวกัน ตัวอย่างเช่น: `paris-bitcoin-conference-2024/` การใส่เครื่องหมายทับจะสร้างโฟลเดอร์โดยอัตโนมัติแทนที่จะเป็นไฟล์:

![event](assets/07.webp)


- ในโฟลเดอร์นี้ คุณจะสร้างไฟล์ YAML แรกชื่อ `events.yml`:

![event](assets/08.webp)


- กรอกไฟล์นี้ด้วยข้อมูลเกี่ยวกับการประชุมของคุณโดยใช้เทมเพลตนี้:


```yaml
start_date:
end_date:
address_line_1:
address_line_2:
address_line_3:
name:
project:
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description:
language:
-
links:
website:
replay_url:
live_url :
tags:
-
```


ตัวอย่างเช่น ไฟล์ YAML ของคุณอาจมีลักษณะดังนี้:


```yaml
start_date: 2024-08-15
end_date: 2024-08-18
address_line_1: Paris, France
address_line_2:
address_line_3:
name: Paris Bitcoin Conference 2024
project: Paris Bitcoin Conference
type: conference
book_online: false
book_in_person: false
price_dollars: 0
description: The largest Bitcoin conference in France with over 8,000 participants each year!
language:
- fr
- en
- es
- it
links:
website: https://paris.bitcoin.fr/conference
replay_url:
live_url :
tags:
- Bitcoiner
- General
- International
```

![event](assets/09.webp)

หากคุณยังไม่มีรหัส "*project*" สำหรับองค์กรของคุณ คุณสามารถเพิ่มได้โดยทำตามบทแนะนำอื่นนี้


https://planb.academy/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- เมื่อคุณทำการเปลี่ยนแปลงไฟล์นี้เสร็จแล้ว ให้บันทึกโดยคลิกที่ปุ่ม `Commit changes...`:

![event](assets/10.webp)


- เพิ่มชื่อเรื่องสำหรับการเปลี่ยนแปลงของคุณ รวมถึงคำอธิบายสั้น ๆ:

![event](assets/11.webp)


- คลิกที่ปุ่ม `Propose changes` สีเขียว:

![event](assets/12.webp)


- จากนั้นคุณจะไปถึงหน้าที่สรุปการเปลี่ยนแปลงทั้งหมดของคุณ:

![event](assets/13.webp)


- คลิกที่รูปโปรไฟล์ GitHub ของคุณที่มุมขวาบน จากนั้นคลิกที่ `Your Repositories`:

![event](assets/14.webp)


- เลือก fork ของที่เก็บ Plan ₿ Academy ของคุณ:

![event](assets/15.webp)


- คุณควรเห็นการแจ้งเตือนที่ด้านบนของหน้าต่างพร้อมกับสาขาใหม่ของคุณ อาจจะเรียกว่า `patch-1` คลิกที่มัน:

![event](assets/16.webp)


- คุณอยู่ในสาขาการทำงานของคุณ:

![event](assets/17.webp)


- กลับไปที่โฟลเดอร์ `resources/conference/` และเลือกโฟลเดอร์ของการประชุมของคุณที่คุณเพิ่งสร้างในคอมมิตก่อนหน้า:

![event](assets/18.webp)


- ในโฟลเดอร์ของการประชุมของคุณ คลิกที่ปุ่ม `Add file` จากนั้นคลิกที่ `Create new file`:

![event](assets/19.webp)


- ตั้งชื่อโฟลเดอร์ใหม่นี้ว่า `assets` และยืนยันการสร้างโดยใส่เครื่องหมายทับ `/` ที่ท้าย:

![event](assets/20.webp)


- ในโฟลเดอร์ `assets` นี้ สร้างไฟล์ชื่อ `.gitkeep`:

![event](assets/21.webp)


- คลิกที่ปุ่ม `Commit changes...`:

![event](assets/22.webp)


- ปล่อยชื่อคอมมิตไว้ตามค่าเริ่มต้น และตรวจสอบให้แน่ใจว่าได้ทำเครื่องหมายที่ช่อง `Commit directly to the patch-1 branch` แล้ว จากนั้นคลิกที่ `Commit changes`:

![event](assets/23.webp)


- กลับไปที่โฟลเดอร์ `assets`:

![event](assets/24.webp)


- คลิกที่ปุ่ม `Add file` จากนั้นคลิกที่ `Upload files`: ![event](assets/25.webp)
- หน้าต่างใหม่จะเปิดขึ้น ลากและวางภาพที่แสดงถึงการประชุมของคุณและจะแสดงบนเว็บไซต์ Plan ₿ Academy:

![event](assets/26.webp)


- อาจเป็นโลโก้ รูปขนาดย่อ หรือแม้แต่โปสเตอร์:

![event](assets/27.webp)


- เมื่ออัปโหลดภาพแล้ว ให้ตรวจสอบว่าได้ทำเครื่องหมายที่ช่อง `Commit directly to the patch-1 branch` แล้ว จากนั้นคลิกที่ `Commit changes`:

![event](assets/28.webp)


- ระวัง ชื่อภาพของคุณต้องเป็น `thumbnail` และต้องอยู่ในรูปแบบ `.webp` ดังนั้นชื่อไฟล์เต็มควรเป็น: `thumbnail.webp`:

![event](assets/29.webp)


- กลับไปที่โฟลเดอร์ `assets` ของคุณและคลิกที่ไฟล์ตัวกลาง `.gitkeep`:

![event](assets/30.webp)


- เมื่ออยู่ในไฟล์แล้ว ให้คลิกที่จุดเล็ก ๆ 3 จุดที่มุมขวาบน จากนั้นคลิกที่ `Delete file`:

![event](assets/31.webp)


- ตรวจสอบว่าคุณยังคงอยู่บนสาขาการทำงานเดียวกัน จากนั้นคลิกที่ปุ่ม `Commit changes`:

![event](assets/32.webp)


- เพิ่มชื่อเรื่องและคำอธิบายให้กับการคอมมิตของคุณ จากนั้นคลิกที่ `Commit changes`:

![event](assets/33.webp)


- กลับไปที่รากของที่เก็บของคุณ:

![event](assets/34.webp)


- คุณควรเห็นข้อความที่ระบุว่าสาขาของคุณมีการเปลี่ยนแปลง คลิกที่ปุ่ม `Compare & pull request`:

![event](assets/35.webp)


- เพิ่มชื่อเรื่องที่ชัดเจนและคำอธิบายให้กับ PR ของคุณ:

![event](assets/36.webp)


- คลิกที่ปุ่ม `Create pull request`:

![event](assets/37.webp)

ขอแสดงความยินดี! PR ของคุณได้ถูกสร้างขึ้นเรียบร้อยแล้ว ขณะนี้ผู้ดูแลระบบจะตรวจสอบและหากทุกอย่างเรียบร้อย จะทำการรวมเข้ากับที่เก็บหลักของ Plan ₿ Academy คุณควรเห็นกิจกรรมของคุณปรากฏบนเว็บไซต์ในอีกไม่กี่วันต่อมา


อย่าลืมติดตามความคืบหน้าของ PR ของคุณ ผู้ดูแลระบบอาจแสดงความคิดเห็นเพื่อขอข้อมูลเพิ่มเติม ตราบใดที่ PR ของคุณยังไม่ได้รับการตรวจสอบ คุณสามารถตรวจสอบได้ในแท็บ `Pull requests` บนที่เก็บ GitHub ของ Plan ₿ Academy:

![event](assets/38.webp)

ขอบคุณมากสำหรับการมีส่วนร่วมที่มีค่าของคุณ! :)