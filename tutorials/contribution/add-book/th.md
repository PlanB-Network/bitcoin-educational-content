---
name: เพิ่มหนังสือใน Plan ₿ Academy
description: วิธีเพิ่มหนังสือใหม่ใน Plan ₿ Academy?
---
![book](assets/cover.webp)


ภารกิจของ PlanB คือการจัดหาทรัพยากรการศึกษาชั้นนำเกี่ยวกับ Bitcoin ในหลายภาษามากที่สุดเท่าที่จะเป็นไปได้ เนื้อหาทั้งหมดที่เผยแพร่บนเว็บไซต์เป็นโอเพ่นซอร์สและโฮสต์บน GitHub ทำให้ทุกคนสามารถมีส่วนร่วมในการพัฒนาแพลตฟอร์มได้


**คุณต้องการเพิ่มหนังสือที่เกี่ยวข้องกับ Bitcoin บนเว็บไซต์ Plan ₿ Academy และเพิ่มการมองเห็นของงานของคุณ แต่ไม่รู้ว่าจะทำอย่างไร? บทแนะนำนี้เหมาะสำหรับคุณ!**

![book](assets/01.webp)


- ก่อนอื่น คุณจำเป็นต้องมีบัญชี GitHub หากคุณไม่ทราบวิธีการสร้างบัญชี เราได้จัดทำบทแนะนำอย่างละเอียดเพื่อแนะนำคุณแล้ว


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- ไปที่ [ที่เก็บ GitHub ของ PlanB ที่อุทิศให้กับข้อมูล](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/books) ในส่วน `resources/books/`:

![book](assets/02.webp)


- คลิกที่มุมขวาบนที่ปุ่ม `Add file` จากนั้นคลิกที่ `Create new file`:

![book](assets/03.webp)


- หากคุณไม่เคยมีส่วนร่วมในเนื้อหาของ Plan ₿ Academy มาก่อน คุณจะต้องสร้าง fork ของที่เก็บต้นฉบับ การ Fork ที่เก็บหมายถึงการสร้างสำเนาของที่เก็บนั้นในบัญชี GitHub ของคุณเอง ทำให้คุณสามารถทำงานในโครงการได้โดยไม่กระทบต่อที่เก็บต้นฉบับ คลิกที่ปุ่ม `Fork this repository`:

![book](assets/04.webp)


- จากนั้นคุณจะไปถึงหน้าการแก้ไข GitHub:

![book](assets/05.webp)


- สร้างโฟลเดอร์สำหรับหนังสือของคุณ ในช่อง `Name your file...` ให้เขียนชื่อหนังสือของคุณเป็นตัวพิมพ์เล็กทั้งหมดและใช้ขีดกลางแทนช่องว่าง ตัวอย่างเช่น ถ้าหนังสือของคุณชื่อ "*My Bitcoin Book*" คุณควรเขียนว่า `my-bitcoin-book`:

![book](assets/06.webp)


- ในการตรวจสอบการสร้างโฟลเดอร์ เพียงแค่เพิ่มเครื่องหมายทับหลังชื่อหนังสือของคุณในช่องเดียวกัน เช่น: `my-bitcoin-book/` การเพิ่มเครื่องหมายทับจะสร้างโฟลเดอร์โดยอัตโนมัติแทนที่จะเป็นไฟล์:

![book](assets/07.webp)


- ในโฟลเดอร์นี้ คุณจะสร้างไฟล์ YAML แรกที่ชื่อว่า `book.yml`:

![book](assets/08.webp)


- กรอกไฟล์นี้ด้วยข้อมูลเกี่ยวกับหนังสือของคุณโดยใช้เทมเพลตนี้:


```yaml
author:
level:
tags:
-
-
```


นี่คือรายละเอียดสำหรับกรอกในแต่ละช่อง:


- `ผู้เขียน`**: ระบุชื่อผู้เขียนหนังสือ
- `level`**: ระบุระดับที่จำเป็นในการอ่านและเข้าใจหนังสือได้ดี เลือกระดับจากตัวเลือกต่อไปนี้:
 - `ผู้เริ่มต้น`
 - `ระดับกลาง`
- `ขั้นสูง` - `ผู้เชี่ยวชาญ`
- `tags`**: เพิ่มแท็กสองหรือสามแท็กที่เกี่ยวข้องกับหนังสือของคุณ ตัวอย่างเช่น:
    - `บิตคอยน์`
    - `ประวัติศาสตร์`
    - `เทคโนโลยี`
    - `เศรษฐกิจ`
    - `การศึกษา`...


ตัวอย่างเช่น ไฟล์ YAML ของคุณอาจมีลักษณะดังนี้:


```yaml
author: Loïc Morel
level: beginner
tags:
- bitcoin
- technology
```


![book](assets/09.webp)


- เมื่อคุณทำการเปลี่ยนแปลงไฟล์นี้เสร็จแล้ว ให้บันทึกโดยคลิกที่ปุ่ม `Commit changes...`:

![book](assets/10.webp)


- เพิ่มชื่อเรื่องสำหรับการเปลี่ยนแปลงของคุณ รวมถึงคำอธิบายสั้น ๆ:

![book](assets/11.webp)


- คลิกที่ปุ่ม `Propose changes` สีเขียว:

![book](assets/12.webp)


- จากนั้นคุณจะไปถึงหน้าที่สรุปการเปลี่ยนแปลงทั้งหมดของคุณ:

![book](assets/13.webp)


- คลิกที่รูปโปรไฟล์ GitHub ของคุณที่มุมขวาบน จากนั้นคลิกที่ `Your Repositories`:

![book](assets/14.webp)


- เลือก fork ของที่เก็บ Plan ₿ Academy ของคุณ:

![book](assets/15.webp)


- คุณควรเห็นการแจ้งเตือนที่ด้านบนของหน้าต่างพร้อมกับสาขาใหม่ของคุณ อาจจะเรียกว่า `patch-1` คลิกที่มัน:

![book](assets/16.webp)


- คุณอยู่ในสาขาการทำงานของคุณ:

![book](assets/17.webp)


- กลับไปที่โฟลเดอร์ `resources/books/` และเลือกโฟลเดอร์ของหนังสือของคุณที่คุณเพิ่งสร้างในคอมมิตก่อนหน้า:

![book](assets/18.webp)


- ในโฟลเดอร์ของหนังสือของคุณ คลิกที่ปุ่ม `Add file` จากนั้นคลิกที่ `Create new file`:

![book](assets/19.webp)


- ตั้งชื่อโฟลเดอร์ใหม่นี้ว่า `assets` และยืนยันการสร้างโดยใส่เครื่องหมายทับ `/` ที่ท้าย:

![book](assets/20.webp)


- ในโฟลเดอร์ `assets` นี้ สร้างไฟล์ชื่อ `.gitkeep`:

![book](assets/21.webp)


- คลิกที่ปุ่ม `Commit changes...`:

![book](assets/22.webp)


- ปล่อยชื่อคอมมิตไว้ตามค่าเริ่มต้น และตรวจสอบให้แน่ใจว่าได้ทำเครื่องหมายที่ช่อง `Commit directly to the patch-1 branch` แล้ว จากนั้นคลิกที่ `Commit changes`:

![book](assets/23.webp)


- กลับไปที่โฟลเดอร์ `assets`:

![book](assets/24.webp)


- คลิกที่ปุ่ม `Add file` จากนั้นคลิกที่ `Upload files`:

![book](assets/25.webp)


- หน้าต่างใหม่จะเปิดขึ้น ลากและวางภาพหน้าปกหนังสือของคุณลงในพื้นที่ ภาพนี้จะแสดงบนเว็บไซต์ Plan ₿ Academy:

![book](assets/26.webp)


- โปรดระวัง รูปภาพต้องอยู่ในรูปแบบของหนังสือ เพื่อให้เหมาะสมที่สุดกับเว็บไซต์ของเรา เช่น:

![book](assets/27.webp)


- เมื่ออัปโหลดภาพแล้ว ให้ตรวจสอบให้แน่ใจว่าได้เลือกช่อง `Commit directly to the patch-1 branch` แล้ว จากนั้นคลิกที่ `Commit changes`:

![book](assets/28.webp)- Please note, your image must be named `cover_en` if the cover is in English and must be in `.webp` format. Therefore, the complete file name should be `cover_en.webp`, `cover_fr.webp`, `cover_it.webp`, etc. If you wish to use a different cover image for each language, for example in the case of a book translation, you can place them in the same location in the `assets` folder:

![book](assets/29.webp)


- กลับไปที่โฟลเดอร์ `assets` ของคุณและคลิกที่ไฟล์ตัวกลาง `.gitkeep`:

![book](assets/30.webp)


- เมื่ออยู่ในไฟล์แล้ว ให้คลิกที่จุดเล็ก ๆ 3 จุดที่มุมขวาบน จากนั้นคลิกที่ `Delete file`:

![book](assets/31.webp)


- ตรวจสอบให้แน่ใจว่าคุณยังคงอยู่บนสาขาการทำงานเดียวกัน จากนั้นคลิกที่ปุ่ม `Commit changes...`:

![book](assets/32.webp)


- เพิ่มชื่อและคำอธิบายให้กับการคอมมิตของคุณ จากนั้นคลิกที่ `Commit changes`:

![book](assets/33.webp)


- กลับไปที่โฟลเดอร์หนังสือของคุณ:

![book](assets/34.webp)


- คลิกที่ปุ่ม `Add file` จากนั้นคลิกที่ `Create new file`:

![book](assets/35.webp)


- สร้างไฟล์ YAML ใหม่โดยตั้งชื่อไฟล์ด้วยตัวบ่งชี้ภาษาของหนังสือ ไฟล์นี้จะถูกใช้สำหรับคำอธิบายของหนังสือ ตัวอย่างเช่น ถ้าต้องการเขียนคำอธิบายเป็นภาษาอังกฤษ จะตั้งชื่อไฟล์นี้ว่า `en.yml`:

![book](assets/36.webp)


- กรอกไฟล์ YAML นี้โดยใช้เทมเพลตนี้:

```yaml
title: ""
publication_year:
cover: cover_en.webp
original: true
description: |

contributors:
-
```


นี่คือรายละเอียดสำหรับกรอกในแต่ละช่อง:


- `title`**: ระบุชื่อหนังสือในเครื่องหมายอัญประกาศ
- `publication_year`**: ระบุปีที่หนังสือได้รับการตีพิมพ์
- `cover`**: ระบุชื่อไฟล์ที่สอดคล้องกับภาพปกตามภาษาของไฟล์ YAML ที่คุณกำลังแก้ไขอยู่ ตัวอย่างเช่น หากคุณกำลังแก้ไขไฟล์ `en.yml` และคุณได้เพิ่มภาพปกภาษาอังกฤษที่มีชื่อว่า `cover_en.webp` ไว้ก่อนหน้านี้ ให้ระบุ `cover_en.webp` ในช่องนี้
- `description`**: เพิ่มย่อหน้าสั้นๆ ที่อธิบายเกี่ยวกับหนังสือ คำอธิบายต้องเป็นภาษาเดียวกับที่ระบุในชื่อไฟล์ YAML
- `contributors`**: เพิ่มรหัสผู้สนับสนุนของคุณหากคุณมี


ตัวอย่างเช่น ไฟล์ YAML ของคุณอาจมีลักษณะดังนี้:


```yaml
title: "My Bitcoin Book"
publication_year: 2021
cover: cover_en.webp
original: true
description: |
Discover the groundbreaking world of Bitcoin with this comprehensive guide tailored for beginners. My Bitcoin Book demystifies the complexities of Bitcoin, providing a clear and concise introduction to how the protocol works. From its revolutionary technology to its potential impact on the global economy, this book offers invaluable insights and practical knowledge. Perfect for those new to Bitcoin, it covers the basics, security tips, and the future of digital finance. Dive into the future of money and empower yourself with the knowledge to navigate the digital age confidently.

contributors:
- pretty-private
```



![book](assets/37.webp)


- คลิกที่ปุ่ม `Commit changes...`:

![book](assets/38.webp)


- ตรวจสอบให้แน่ใจว่าได้เลือกช่อง `Commit directly to the patch-1 branch` แล้ว เพิ่มชื่อเรื่อง จากนั้นคลิกที่ `Commit changes`:

![book](assets/39.webp)


- โฟลเดอร์หนังสือควรมีลักษณะดังนี้:

![book](assets/40.webp)


- หากทุกอย่างดูดีสำหรับคุณ ให้กลับไปที่รากของ fork ของคุณ:

![book](assets/41.webp)


- คุณควรเห็นข้อความที่ระบุว่าสาขาของคุณได้รับการแก้ไขแล้ว คลิกที่ปุ่ม `Compare & pull request`:

![book](assets/42.webp)


- เพิ่มชื่อเรื่องที่ชัดเจนและคำอธิบายให้กับ PR ของคุณ:

![book](assets/43.webp)


- คลิกที่ปุ่ม `Create pull request`:

![book](assets/44.webp)



ขอแสดงความยินดี! PR ของคุณถูกสร้างขึ้นเรียบร้อยแล้ว ขณะนี้ผู้ดูแลระบบจะทำการตรวจสอบ และหากทุกอย่างเรียบร้อย จะทำการรวมเข้ากับที่เก็บหลักของ Plan ₿ Academy คุณควรจะเห็นหนังสือของคุณปรากฏบนเว็บไซต์ในอีกไม่กี่วันถัดไป


อย่าลืมติดตามความคืบหน้าของ PR ของคุณ ผู้ดูแลระบบอาจแสดงความคิดเห็นขอข้อมูลเพิ่มเติม ตราบใดที่ PR ของคุณยังไม่ได้รับการตรวจสอบ คุณสามารถดูได้ในแท็บ `Pull requests` บนที่เก็บ GitHub ของ Plan ₿ Academy:

![book](assets/45.webp)

ขอบคุณมากสำหรับการมีส่วนร่วมที่มีค่าของคุณ! :)