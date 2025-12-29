---
name: การเพิ่มพอดแคสต์ไปยัง Plan ₿ Academy
description: วิธีเพิ่มพอดแคสต์ใหม่ใน Plan ₿ Academy?
---
![podcast](assets/cover.webp)


ภารกิจของ PlanB คือการจัดหาทรัพยากรการศึกษาชั้นนำเกี่ยวกับ Bitcoin ในหลายภาษามากที่สุดเท่าที่จะเป็นไปได้ เนื้อหาทั้งหมดที่เผยแพร่บนเว็บไซต์เป็นโอเพ่นซอร์สและโฮสต์บน GitHub ทำให้ทุกคนสามารถมีส่วนร่วมในการพัฒนาแพลตฟอร์มได้


คุณกำลังมองหาวิธีเพิ่มพอดแคสต์ Bitcoin ไปยังเว็บไซต์ Plan ₿ Academy และเพิ่มการมองเห็นให้กับรายการของคุณ แต่ไม่รู้ว่าจะทำอย่างไรใช่ไหม? บทแนะนำนี้เหมาะสำหรับคุณ!

![podcast](assets/01.webp)


- ก่อนอื่น คุณจำเป็นต้องมีบัญชี GitHub หากคุณไม่ทราบวิธีการสร้างบัญชี เราได้จัดทำบทแนะนำโดยละเอียดเพื่อแนะนำคุณแล้ว


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- ไปที่ [ที่เก็บ GitHub ของ PlanB ที่อุทิศให้กับข้อมูล](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/podcasts) ในส่วน `resources/podcasts/`:

![podcast](assets/02.webp)


- คลิกที่มุมขวาบนที่ปุ่ม `Add file` จากนั้นคลิกที่ `Create new file`:

![podcast](assets/03.webp)


- หากคุณไม่เคยมีส่วนร่วมในเนื้อหาของ Plan ₿ Academy มาก่อน คุณจะต้องสร้าง fork ของที่เก็บต้นฉบับ การ Fork ที่เก็บหมายถึงการสร้างสำเนาของที่เก็บนั้นในบัญชี GitHub ของคุณเอง ทำให้คุณสามารถทำงานในโครงการได้โดยไม่กระทบต่อที่เก็บต้นฉบับ คลิกที่ปุ่ม `Fork this repository`:

![podcast](assets/04.webp)


- จากนั้นคุณจะไปถึงหน้าการแก้ไข GitHub:

![podcast](assets/05.webp)


- สร้างโฟลเดอร์สำหรับพอดแคสต์ของคุณ ในช่อง `Name your file...` ให้เขียนชื่อพอดแคสต์ของคุณเป็นตัวพิมพ์เล็กและใช้ขีดกลางแทนช่องว่าง ตัวอย่างเช่น หากรายการของคุณชื่อ "Super Podcast Bitcoin" คุณควรเขียน `super-podcast-bitcoin`:

![podcast](assets/06.webp)


- ในการยืนยันการสร้างโฟลเดอร์ เพียงแค่เพิ่มเครื่องหมายทับหลังชื่อพอดแคสต์ของคุณในช่องเดียวกัน เช่น: `super-podcast-bitcoin/` การเพิ่มเครื่องหมายทับจะสร้างโฟลเดอร์โดยอัตโนมัติแทนที่จะเป็นไฟล์:

![podcast](assets/07.webp)


- ในโฟลเดอร์นี้ คุณจะสร้างไฟล์ YAML แรกชื่อ `podcast.yml`:

![podcast](assets/08.webp)


- กรอกข้อมูลเกี่ยวกับพอดแคสต์ของคุณโดยใช้เทมเพลตนี้:


```yaml
name:
host:
language:
links:
podcast:
twitter:
website:
description: |

tags:
-
-
contributors:
-
```


นี่คือรายละเอียดที่ต้องกรอกในแต่ละช่อง:



- `name`**: ระบุชื่อพอดแคสต์ของคุณ
- `host`**: ระบุชื่อหรือนามแฝงของผู้พูดหรือผู้ดำเนินรายการของพอดแคสต์ แต่ละชื่อควรคั่นด้วยเครื่องหมายจุลภาค
- `language`**: ระบุรหัสภาษาของภาษาที่พูดในพอดแคสต์ของคุณ ตัวอย่างเช่น สำหรับภาษาอังกฤษ ให้ระบุ `en` สำหรับภาษาอิตาลี `it`...



- `links`**: ให้ลิงก์ไปยังเนื้อหาของคุณ คุณมีสองตัวเลือก:
 - `podcast`: ลิงก์ไปยังพอดแคสต์ของคุณ,
 - `twitter`: ลิงก์ไปยังโปรไฟล์ Twitter ของพอดแคสต์หรือองค์กรที่ผลิต,
 - `website`: ลิงก์ไปยังเว็บไซต์ของพอดแคสต์หรือองค์กรที่ผลิตพอดแคสต์นั้น



- `description`**: เพิ่มย่อหน้าสั้น ๆ ที่อธิบายพอดแคสต์ของคุณ คำอธิบายต้องเป็นภาษาเดียวกับที่ระบุในช่อง `language:`



- `tags`**: เพิ่มแท็กสองแท็กที่เกี่ยวข้องกับพอดแคสต์ของคุณ ตัวอย่าง:
    - `บิตคอยน์`
    - `เทคโนโลยี`
    - `เศรษฐกิจ`
    - `การศึกษา`...



- `contributors`**: ระบุ ID ผู้สนับสนุนของคุณหากคุณมี


ตัวอย่างเช่น ไฟล์ YAML ของคุณอาจมีลักษณะดังนี้:


```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
twitter: https://twitter.com/decouvrebitcoin
website: https://decouvrebitcoin.fr
description: |
Super Podcast Bitcoin is a technical LIVE session held once a week on Twitter to delve deep into the Bitcoin protocol, layer two solutions, and all things that blow minds. Our hosts Lounes, Pantamis, Loïc, and Sosthene will answer your questions and offer the most technical show on Bitcoin in the world.

tags:
- bitcoin
- technology
contributors:
- rabbit-hole
```


![podcast](assets/09.webp)



- เมื่อคุณทำการเปลี่ยนแปลงไฟล์นี้เสร็จแล้ว ให้บันทึกโดยคลิกที่ปุ่ม `Commit changes...`:

![podcast](assets/10.webp)


- เพิ่มชื่อเรื่องสำหรับการเปลี่ยนแปลงของคุณ รวมถึงคำอธิบายสั้น ๆ:

![podcast](assets/11.webp)


- คลิกที่ปุ่ม `Propose changes` สีเขียว:

![podcast](assets/12.webp)


- จากนั้นคุณจะไปถึงหน้าที่สรุปการเปลี่ยนแปลงทั้งหมดของคุณ:

![podcast](assets/13.webp)


- คลิกที่รูปโปรไฟล์ GitHub ของคุณที่มุมขวาบน จากนั้นคลิกที่ `Your Repositories`:

![podcast](assets/14.webp)


- เลือก fork ของที่เก็บ Plan ₿ Academy ของคุณ:

![podcast](assets/15.webp)


- คุณควรเห็นการแจ้งเตือนที่ด้านบนของหน้าต่างพร้อมกับสาขาใหม่ของคุณ อาจจะเรียกว่า `patch-1` คลิกที่มัน:

![podcast](assets/16.webp)


- คุณอยู่ในสาขาการทำงานของคุณ:

![podcast](assets/17.webp)


- กลับไปที่โฟลเดอร์ `resources/podcast/` และเลือกโฟลเดอร์พอดแคสต์ที่คุณเพิ่งสร้างในคอมมิตก่อนหน้า: ![podcast](assets/18.webp)
- ในโฟลเดอร์พอดแคสต์ของคุณ คลิกที่ปุ่ม `Add file` จากนั้นคลิกที่ `Create new file`:

![podcast](assets/19.webp)


- ตั้งชื่อโฟลเดอร์ใหม่นี้ว่า `assets` และยืนยันการสร้างโดยการเพิ่มเครื่องหมายทับ `/` ที่ท้าย:

![podcast](assets/20.webp)


- ในโฟลเดอร์ `assets` นี้ สร้างไฟล์ชื่อ `.gitkeep`:

![podcast](assets/21.webp)


- คลิกที่ปุ่ม `Commit changes...`:

![podcast](assets/22.webp)


- ปล่อยชื่อคอมมิตไว้ตามค่าเริ่มต้น และตรวจสอบให้แน่ใจว่าได้ทำเครื่องหมายที่ช่อง `Commit directly to the patch-1 branch` แล้ว จากนั้นคลิกที่ `Commit changes`:

![podcast](assets/23.webp)


- กลับไปที่โฟลเดอร์ `assets`:

![podcast](assets/24.webp)


- คลิกที่ปุ่ม `Add file` จากนั้นคลิกที่ `Upload files`:

![podcast](assets/25.webp)


- หน้าต่างใหม่จะเปิดขึ้น ลากและวางโลโก้พอดแคสต์ของคุณลงในพื้นที่ ภาพนี้จะแสดงบนเว็บไซต์ Plan ₿ Academy:

![podcast](assets/26.webp)


- โปรดระวัง ภาพต้องเป็นสี่เหลี่ยมจัตุรัส เพื่อให้พอดีกับเว็บไซต์ของเรา:

![podcast](assets/27.webp)


- เมื่ออัปโหลดภาพแล้ว ให้ตรวจสอบว่าได้เลือกช่อง `Commit directly to the patch-1 branch` แล้ว จากนั้นคลิกที่ `Commit changes`:

![podcast](assets/28.webp)


- ระวัง ชื่อไฟล์รูปภาพของคุณต้องเป็น `logo` และต้องอยู่ในรูปแบบ `.webp` ดังนั้นชื่อไฟล์เต็มควรเป็น: `logo.webp`:

![podcast](assets/29.webp)


- กลับไปที่โฟลเดอร์ `assets` ของคุณและคลิกที่ไฟล์ตัวกลาง `.gitkeep`:

![podcast](assets/30.webp)


- เมื่ออยู่ในไฟล์แล้ว ให้คลิกที่จุดเล็ก ๆ สามจุดที่มุมขวาบน จากนั้นคลิกที่ `Delete file`:

![podcast](assets/31.webp)


- ตรวจสอบว่าคุณยังคงอยู่บนสาขาการทำงานเดียวกัน จากนั้นคลิกที่ปุ่ม `Commit changes`:

![podcast](assets/32.webp)


- เพิ่มชื่อและคำอธิบายให้กับการคอมมิตของคุณ จากนั้นคลิกที่ `Commit changes`:

![podcast](assets/33.webp)


- กลับไปที่รากของที่เก็บข้อมูลของคุณ:

![podcast](assets/34.webp)


- คุณควรเห็นข้อความที่ระบุว่าสาขาของคุณมีการเปลี่ยนแปลง คลิกที่ปุ่ม `Compare & pull request`:

![podcast](assets/35.webp)


- เพิ่มชื่อและคำอธิบายที่ชัดเจนให้กับ PR ของคุณ:

![podcast](assets/36.webp)


- คลิกที่ปุ่ม `Create pull request`:

![podcast](assets/37.webp)

ขอแสดงความยินดี! PR ของคุณได้ถูกสร้างขึ้นเรียบร้อยแล้ว ขณะนี้ผู้ดูแลระบบจะทำการตรวจสอบ และหากทุกอย่างเรียบร้อยดี จะทำการรวมเข้ากับที่เก็บหลักของ Plan ₿ Academy คุณควรจะเห็นพอดแคสต์ของคุณปรากฏบนเว็บไซต์ในอีกไม่กี่วันถัดไป


โปรดตรวจสอบความคืบหน้าของ PR ของคุณ ผู้ดูแลระบบอาจแสดงความคิดเห็นเพื่อขอข้อมูลเพิ่มเติม ตราบใดที่ PR ของคุณยังไม่ได้รับการตรวจสอบ คุณสามารถดูได้ในแท็บ `Pull requests` บนที่เก็บ GitHub ของ Plan ₿ Academy:

![podcast](assets/38.webp)

ขอบคุณมากสำหรับการมีส่วนร่วมที่มีค่าของคุณ! :)