---
name: การเพิ่มโครงการ
description: วิธีเสนอการเพิ่มโครงการใหม่บน Plan ₿ Academy?
---
![project](assets/cover.webp)


ภารกิจของ PlanB คือการจัดหาทรัพยากรการศึกษาชั้นนำเกี่ยวกับ Bitcoin ในหลายภาษามากที่สุดเท่าที่จะเป็นไปได้ เนื้อหาทั้งหมดที่เผยแพร่บนเว็บไซต์เป็นโอเพ่นซอร์สและโฮสต์บน GitHub ซึ่งช่วยให้ทุกคนสามารถมีส่วนร่วมในการพัฒนาแพลตฟอร์มได้


คุณต้องการเพิ่ม "โครงการ" Bitcoin ใหม่ไปยังไซต์ Plan ₿ Academy และให้ความชัดเจนแก่บริษัทหรือซอฟต์แวร์ของคุณ แต่ไม่รู้ว่าจะทำอย่างไรใช่ไหม? บทแนะนำนี้เหมาะสำหรับคุณ!

![project](assets/01.webp)


- ก่อนอื่น คุณจำเป็นต้องมีบัญชี GitHub หากคุณไม่ทราบวิธีการสร้างบัญชี เราได้จัดทำบทแนะนำอย่างละเอียดเพื่อแนะนำคุณแล้ว


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- ไปที่ [ที่เก็บ GitHub ของ PlanB ที่อุทิศให้กับข้อมูล](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/projects) ในส่วน `resources/project/`:

![project](assets/02.webp)


- คลิกที่มุมขวาบนที่ปุ่ม `Add file` จากนั้นคลิกที่ `Create new file`:

![project](assets/03.webp)


- หากคุณไม่เคยมีส่วนร่วมในเนื้อหาของ Plan ₿ Academy มาก่อน คุณจะต้องสร้าง fork ของที่เก็บต้นฉบับ การ Fork ที่เก็บหมายถึงการสร้างสำเนาของที่เก็บนั้นในบัญชี GitHub ของคุณเอง ซึ่งช่วยให้คุณทำงานในโครงการโดยไม่กระทบต่อที่เก็บต้นฉบับ คลิกที่ปุ่ม `Fork this repository`:

![project](assets/04.webp)


- จากนั้นคุณจะไปถึงหน้าการแก้ไข GitHub:

![project](assets/05.webp)


- สร้างโฟลเดอร์สำหรับบริษัทของคุณ ในช่อง `Name your file...` ให้เขียนชื่อบริษัทของคุณเป็นตัวพิมพ์เล็กและใช้ขีดกลางแทนช่องว่าง ตัวอย่างเช่น หากบริษัทของคุณชื่อ "Bitcoin Baguette" คุณควรเขียน `bitcoin-baguette`:

![project](assets/06.webp)


- ในการยืนยันการสร้างโฟลเดอร์ เพียงแค่เพิ่มเครื่องหมายทับหลังชื่อของคุณในช่องเดียวกัน เช่น: `bitcoin-baguette/` การเพิ่มเครื่องหมายทับจะสร้างโฟลเดอร์โดยอัตโนมัติแทนที่จะเป็นไฟล์:

![project](assets/07.webp)


- ในโฟลเดอร์นี้ คุณจะสร้างไฟล์ YAML แรกชื่อ `project.yml`:

![project](assets/08.webp)


- กรอกไฟล์นี้ด้วยข้อมูลเกี่ยวกับบริษัทของคุณโดยใช้เทมเพลตนี้:


```yaml
name:

address_line_1:
address_line_2:
address_line_3:

language:
-

links:
website:
twitter:
Github:
youtube:
nostr:

tags:
-
-

category:
```


นี่คือสิ่งที่ต้องกรอกสำหรับแต่ละคีย์:


- `name`: ชื่อบริษัทของคุณ (จำเป็น);
- `address` : ที่ตั้งของธุรกิจของคุณ (ไม่บังคับ);
- `language` : ประเทศที่ธุรกิจของคุณดำเนินการอยู่หรือภาษาที่รองรับ (ไม่บังคับ);
- `links` : ลิงก์ทางการต่างๆ ของธุรกิจของคุณ (ไม่บังคับ);
- `แท็ก` : 2 คำที่อธิบายธุรกิจของคุณ (จำเป็น);
- `category` : หมวดหมู่ที่อธิบายถึงสาขาที่ธุรกิจของคุณดำเนินการได้ดีที่สุดจากตัวเลือกต่อไปนี้:
 - `wallet`,
 - `โครงสร้างพื้นฐาน`,
 - `แลกเปลี่ยน`,
 - `การศึกษา`,
 - `service`,
 - `ชุมชน`,
 - `การประชุม`,
 - `ความเป็นส่วนตัว`,
 - `การลงทุน`,
 - `node`,
 - `mining`,
 - `ข่าว`,
 - `ผู้ผลิต`.


ตัวอย่างเช่น ไฟล์ YAML ของคุณอาจมีลักษณะดังนี้:


```yaml
name: Bitcoin Baguette

address_line_1: Paris, France
address_line_2:
address_line_3:

language:
- fr
- en

links:
website: https://bitcoin-baguette.com
twitter: https://twitter.com/bitcoinbaguette
Github:
youtube:
nostr:

tags:
- bitcoin
- education

category: education
```


![project](assets/09.webp)


- เมื่อคุณทำการเปลี่ยนแปลงไฟล์นี้เสร็จแล้ว ให้บันทึกโดยคลิกที่ปุ่ม `Commit changes...`:

![project](assets/10.webp)


- เพิ่มชื่อเรื่องสำหรับการเปลี่ยนแปลงของคุณ พร้อมคำอธิบายสั้น ๆ:

![project](assets/11.webp)


- คลิกที่ปุ่ม `Propose changes` สีเขียว:

![project](assets/12.webp)


- จากนั้นคุณจะไปถึงหน้าที่สรุปการเปลี่ยนแปลงทั้งหมดของคุณ:

![project](assets/13.webp)


- คลิกที่รูปโปรไฟล์ GitHub ของคุณที่มุมขวาบน จากนั้นคลิกที่ `Your Repositories`:

![project](assets/14.webp)


- เลือก fork ของที่เก็บ Plan ₿ Academy:

![project](assets/15.webp)


- คุณควรเห็นการแจ้งเตือนที่ด้านบนของหน้าต่างพร้อมกับสาขาใหม่ของคุณ น่าจะเรียกว่า `patch-1` คลิกที่มัน:

![project](assets/16.webp)


- คุณอยู่ในสาขาการทำงานของคุณแล้ว (**ตรวจสอบให้แน่ใจว่าคุณอยู่ในสาขาเดียวกันกับการแก้ไขก่อนหน้านี้ของคุณ นี่เป็นสิ่งสำคัญ!**):

![project](assets/17.webp)


- กลับไปที่โฟลเดอร์ `resources/projects/` และเลือกโฟลเดอร์ของธุรกิจของคุณที่คุณเพิ่งสร้างในคอมมิตก่อนหน้า:

![project](assets/18.webp)


- ในโฟลเดอร์ธุรกิจของคุณ คลิกที่ปุ่ม `Add file` จากนั้นคลิกที่ `Create new file`:

![project](assets/19.webp)


- ตั้งชื่อโฟลเดอร์ใหม่นี้ว่า `assets` และยืนยันการสร้างโดยใส่เครื่องหมายทับ `/` ที่ท้าย:

![project](assets/20.webp)


- ในโฟลเดอร์ `assets` นี้ สร้างไฟล์ชื่อ `.gitkeep`:

![project](assets/21.webp)


- คลิกที่ปุ่ม `Commit changes...`:

![project](assets/22.webp)


- ปล่อยชื่อคอมมิตไว้เป็นค่าเริ่มต้น และตรวจสอบให้แน่ใจว่าได้เลือกช่อง `Commit directly to the patch-1 branch` แล้ว จากนั้นคลิกที่ `Commit changes`: ![project](assets/23.webp)
- กลับไปที่โฟลเดอร์ `assets`:

![project](assets/24.webp)


- คลิกที่ปุ่ม `Add file` จากนั้นคลิกที่ `Upload files`:

![project](assets/25.webp)


- หน้าต่างใหม่จะเปิดขึ้น ลากและวางภาพของบริษัทหรือซอฟต์แวร์ของคุณลงในพื้นที่ ภาพนี้จะแสดงบนเว็บไซต์ Plan ₿ Academy:

![project](assets/26.webp)


- มันสามารถเป็นโลโก้หรือไอคอน:

![project](assets/27.webp)


- เมื่ออัปโหลดภาพแล้ว ให้ตรวจสอบว่าได้ทำเครื่องหมายที่ช่อง `Commit directly to the patch-1 branch` แล้ว จากนั้นคลิกที่ `Commit changes`:

![project](assets/28.webp)


- ระวัง ภาพของคุณต้องเป็นสี่เหลี่ยมจัตุรัส ต้องตั้งชื่อว่า `logo` และต้องอยู่ในรูปแบบ `.webp` ดังนั้นชื่อไฟล์เต็มควรเป็น: `logo.webp`:

![project](assets/29.webp)


- กลับไปที่โฟลเดอร์ `assets` ของคุณและคลิกที่ไฟล์กลาง `.gitkeep`:

![project](assets/30.webp)


- เมื่ออยู่ในไฟล์แล้ว ให้คลิกที่จุดเล็ก ๆ สามจุดที่มุมขวาบน จากนั้นคลิกที่ `Delete file`:

![project](assets/31.webp)


- ยืนยันว่าคุณยังคงอยู่บนสาขาการทำงานเดียวกัน จากนั้นคลิกที่ปุ่ม `Commit changes`:

![project](assets/32.webp)


- เพิ่มชื่อและคำอธิบายให้กับการคอมมิตของคุณ จากนั้นคลิกที่ `Commit changes`:

![project](assets/33.webp)


- กลับไปที่โฟลเดอร์ของบริษัทคุณ:

![project](assets/34.webp)


- คลิกที่ปุ่ม `Add file` จากนั้นคลิกที่ `Create new file`:

![project](assets/35.webp)


- สร้างไฟล์ YAML ใหม่โดยตั้งชื่อไฟล์ด้วยตัวบ่งชี้ของภาษาพื้นเมืองของคุณ ไฟล์นี้จะถูกใช้สำหรับคำอธิบายของโครงการ ตัวอย่างเช่น หากฉันต้องการเขียนคำอธิบายของฉันเป็นภาษาอังกฤษ ฉันจะตั้งชื่อไฟล์นี้ว่า `en.yml`:

![project](assets/36.webp)


- กรอกไฟล์ YAML นี้โดยใช้เทมเพลตนี้:

```yaml
description: |

contributors:
-
```



- สำหรับคีย์ `contributors` คุณสามารถเพิ่มรหัสผู้สนับสนุนของคุณไปที่ Plan ₿ Academy ได้หากคุณมี หากไม่มี ให้เว้นช่องนี้ว่างไว้
- สำหรับคีย์ `description` คุณเพียงแค่ต้องเพิ่มย่อหน้าสั้น ๆ ที่อธิบายเกี่ยวกับบริษัทหรือซอฟต์แวร์ของคุณ คำอธิบายต้องเป็นภาษาเดียวกับชื่อไฟล์ คุณไม่จำเป็นต้องแปลคำอธิบายนี้เป็นทุกภาษาที่เว็บไซต์รองรับ เนื่องจากทีม PlanB จะทำการแปลโดยใช้โมเดลของพวกเขา ตัวอย่างเช่น นี่คือสิ่งที่ไฟล์ของคุณอาจมีลักษณะดังนี้:

```yaml
description: |
Founded in 2017, Bitcoin Baguette is a Paris-based association dedicated to organizing Bitcoin meetups and technical workshops. We bring together enthusiasts, experts, and curious minds to explore and discuss the intricacies of Bitcoin technology. Our events provide a platform for knowledge sharing, networking, and fostering a deeper understanding of Bitcoin's inner workings. Join us at Bitcoin Baguette to be a part of Paris's Bitcoin community and stay updated with the latest advancements in the field.

contributors:
-
```

![project](assets/37.webp)


- คลิกที่ปุ่ม `Commit changes`:

![project](assets/38.webp)


- ตรวจสอบให้แน่ใจว่าได้เลือกช่อง `Commit directly to the patch-1 branch` แล้ว เพิ่มชื่อเรื่อง จากนั้นคลิกที่ `Commit changes`:

![project](assets/39.webp)


- โฟลเดอร์บริษัทของคุณควรมีลักษณะดังนี้:

![project](assets/40.webp)


- หากทุกอย่างเป็นที่พอใจของคุณ ให้กลับไปที่รากของ fork ของคุณ:

![project](assets/41.webp)


- คุณควรเห็นข้อความที่ระบุว่าสาขาของคุณมีการเปลี่ยนแปลง คลิกที่ปุ่ม `Compare & pull request`:

![project](assets/42.webp)


- เพิ่มชื่อและคำอธิบายที่ชัดเจนให้กับ PR ของคุณ:

![project](assets/43.webp)


- คลิกที่ปุ่ม `Create pull request`:

![project](assets/44.webp)

ขอแสดงความยินดี! PR ของคุณถูกสร้างขึ้นเรียบร้อยแล้ว ขณะนี้ผู้ดูแลระบบจะตรวจสอบและหากทุกอย่างเรียบร้อย จะรวมเข้ากับที่เก็บหลักของ Plan ₿ Academy คุณควรเห็นโปรไฟล์โครงการของคุณปรากฏบนเว็บไซต์ในอีกไม่กี่วันต่อมา


อย่าลืมติดตามความคืบหน้าของ PR ของคุณ ผู้ดูแลระบบอาจแสดงความคิดเห็นเพื่อขอข้อมูลเพิ่มเติม ตราบใดที่ PR ของคุณยังไม่ได้รับการตรวจสอบ คุณสามารถตรวจสอบได้ในแท็บ `Pull requests` บนที่เก็บ GitHub ของ Plan ₿ Academy:

![project](assets/45.webp)

ขอบคุณมากสำหรับการมีส่วนร่วมที่มีค่าของคุณ! :)