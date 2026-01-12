---
name: การเพิ่มการเล่นซ้ำของการประชุม
description: วิธีเพิ่มการเล่นซ้ำของการประชุมบน Plan ₿ Academy?
---
![conference](assets/cover.webp)


ภารกิจของ PlanB คือการจัดหาทรัพยากรการศึกษาชั้นนำเกี่ยวกับ Bitcoin ในหลายภาษามากที่สุดเท่าที่จะเป็นไปได้ เนื้อหาทั้งหมดที่เผยแพร่บนเว็บไซต์เป็นโอเพ่นซอร์สและโฮสต์บน GitHub ทำให้ทุกคนสามารถมีส่วนร่วมในการพัฒนาแพลตฟอร์มได้


คุณต้องการเพิ่มการเล่นซ้ำของการประชุม Bitcoin บนเว็บไซต์ Plan ₿ Academy และให้ความสำคัญกับเหตุการณ์นี้ แต่ไม่รู้ว่าจะทำอย่างไร? บทแนะนำนี้เหมาะสำหรับคุณ!


อย่างไรก็ตาม หากคุณต้องการเพิ่มการประชุมที่จะเกิดขึ้นในอนาคต ฉันแนะนำให้คุณอ่านบทแนะนำอื่นนี้ซึ่งเราอธิบายวิธีการเพิ่มกิจกรรมใหม่ลงในเว็บไซต์


https://planb.academy/tutorials/contribution/resource/add-event-1d3df554-c2d8-4e93-853f-58f672c5e097


![conference](assets/01.webp)


- ก่อนอื่น คุณจำเป็นต้องมีบัญชีบน GitHub หากคุณไม่ทราบวิธีการสร้างบัญชี เราได้จัดทำบทแนะนำอย่างละเอียดเพื่อแนะนำคุณแล้ว


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



- ไปที่ [ที่เก็บ GitHub ของ PlanB ที่อุทิศให้กับข้อมูล](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/conference) ในส่วน `resources/conference/`:

![conference](assets/02.webp)


- คลิกที่มุมขวาบนที่ปุ่ม `Add file` จากนั้นคลิกที่ `Create new file`:

![conference](assets/03.webp)


- หากคุณไม่เคยมีส่วนร่วมในเนื้อหาของ Plan ₿ Academy มาก่อน คุณจะต้องสร้าง fork ของที่เก็บต้นฉบับ การ Fork ที่เก็บหมายถึงการสร้างสำเนาของที่เก็บนั้นในบัญชี GitHub ของคุณเอง ซึ่งช่วยให้คุณทำงานในโครงการโดยไม่กระทบต่อที่เก็บต้นฉบับ คลิกที่ปุ่ม `Fork this repository`:

![conference](assets/04.webp)


- จากนั้นคุณจะไปถึงหน้าการแก้ไข GitHub:

![conference](assets/05.webp)


- สร้างโฟลเดอร์สำหรับการประชุมของคุณ ในช่อง `Name your file...` ให้เขียนชื่อการประชุมของคุณเป็นตัวพิมพ์เล็กและใช้ขีดกลางแทนช่องว่าง ตัวอย่างเช่น หากการประชุมของคุณชื่อ "Paris Bitcoin Conference" คุณควรเขียนว่า `paris-bitcoin-conference` และเพิ่มปีของการประชุมของคุณ เช่น: `paris-bitcoin-conference-2024`:

![conference](assets/06.webp)


- ในการยืนยันการสร้างโฟลเดอร์ เพียงแค่ใส่เครื่องหมายทับหลังชื่อของคุณในช่องเดียวกัน เช่น: `paris-bitcoin-conference-2024/` การใส่เครื่องหมายทับจะสร้างโฟลเดอร์โดยอัตโนมัติแทนที่จะเป็นไฟล์:

![conference](assets/07.webp)


- ในโฟลเดอร์นี้ คุณจะสร้างไฟล์ YAML แรกชื่อ `conference.yml`:

![conference](assets/08.webp)

กรอกไฟล์นี้ด้วยข้อมูลที่เกี่ยวข้องกับการประชุมของคุณโดยใช้เทมเพลตนี้:

```yaml
year:
name:
project:
location:
language:
-
links:
website:
twitter:
tags:
-
-
```


ตัวอย่างเช่น ไฟล์ YAML ของคุณอาจมีลักษณะดังนี้:


```yaml
year: 2024-08
name: Paris Bitcoin Conference 2024
project: Paris Bitcoin Conference
location: Paris, France
language:
- fr
- en
links:
website: https://paris.bitcoin.fr/conference
twitter: https://twitter.com/ParisBitcoinConference
tags:
- International
- All Public
```


![conference](assets/09.webp)


หากคุณยังไม่มีรหัส "*project*" สำหรับองค์กรของคุณ คุณสามารถเพิ่มได้โดยทำตามบทแนะนำอื่นนี้


https://planb.academy/tutorials/contribution/resource/add-builder-b5834c46-6dcc-4064-8d68-1ef529991d3d




- เมื่อคุณทำการเปลี่ยนแปลงไฟล์นี้เสร็จแล้ว ให้บันทึกโดยคลิกที่ปุ่ม `Commit changes...`:

![conference](assets/10.webp)


- เพิ่มชื่อเรื่องสำหรับการเปลี่ยนแปลงของคุณ รวมถึงคำอธิบายสั้น ๆ:

![conference](assets/11.webp)


- คลิกที่ปุ่ม `Propose changes` สีเขียว:

![conference](assets/12.webp)


- จากนั้นคุณจะไปถึงหน้าที่สรุปการเปลี่ยนแปลงทั้งหมดของคุณ:

![conference](assets/13.webp)


- คลิกที่รูปโปรไฟล์ GitHub ของคุณที่มุมขวาบน จากนั้นคลิกที่ `Your Repositories`:

![conference](assets/14.webp)


- เลือก fork ของที่เก็บ Plan ₿ Academy ของคุณ:

![conference](assets/15.webp)


- คุณควรเห็นการแจ้งเตือนที่ด้านบนของหน้าต่างพร้อมกับสาขาใหม่ของคุณ ซึ่งอาจจะเรียกว่า `patch-1` คลิกที่มัน:

![conference](assets/16.webp)


- คุณอยู่ในสาขาการทำงานของคุณ:

![conference](assets/17.webp)


- กลับไปที่โฟลเดอร์ `resources/conference/` และเลือกโฟลเดอร์ของการประชุมของคุณที่คุณเพิ่งสร้างในคอมมิตก่อนหน้า:

![conference](assets/18.webp)


- ในโฟลเดอร์ของการประชุมของคุณ คลิกที่ปุ่ม `Add file` จากนั้นคลิกที่ `Create new file`:

![conference](assets/19.webp)


- ตั้งชื่อโฟลเดอร์ใหม่นี้ว่า `assets` และยืนยันการสร้างโดยใส่เครื่องหมายทับ `/` ที่ท้าย:

![conference](assets/20.webp)


- ในโฟลเดอร์ `assets` นี้ สร้างไฟล์ชื่อ `.gitkeep`:

![conference](assets/21.webp)


- คลิกที่ปุ่ม `Commit changes...`:

![conference](assets/22.webp)


- ปล่อยชื่อคอมมิตไว้เป็นค่าเริ่มต้น และตรวจสอบให้แน่ใจว่าได้ทำเครื่องหมายที่ช่อง `Commit directly to the patch-1 branch` แล้ว จากนั้นคลิกที่ `Commit changes`:

![conference](assets/23.webp)


- กลับไปที่โฟลเดอร์ `assets`:

![conference](assets/24.webp)


- คลิกที่ปุ่ม `Add file` จากนั้นคลิกที่ `Upload files`:

![conference](assets/25.webp)


- หน้าต่างใหม่จะเปิดขึ้น ลากและวางภาพที่แสดงถึงการประชุมของคุณและจะแสดงบนเว็บไซต์ Plan ₿ Academy: ![conference](assets/26.webp)
- อาจเป็นโลโก้, ภาพขนาดย่อ, หรือแม้แต่โปสเตอร์:

![conference](assets/27.webp)


- เมื่ออัปโหลดภาพแล้ว ให้ตรวจสอบว่าได้ทำเครื่องหมายที่ช่อง `Commit directly to the patch-1 branch` แล้ว จากนั้นคลิกที่ `Commit changes`:

![conference](assets/28.webp)


- ระวัง ชื่อภาพของคุณต้องเป็น `thumbnail` และต้องอยู่ในรูปแบบ `.webp` ดังนั้นชื่อไฟล์เต็มควรเป็น: `thumbnail.webp`:

![conference](assets/29.webp)


- กลับไปที่โฟลเดอร์ `assets` ของคุณและคลิกที่ไฟล์ตัวกลาง `.gitkeep`:

![conference](assets/30.webp)


- เมื่ออยู่ในไฟล์ ให้คลิกที่จุดเล็ก ๆ 3 จุดที่มุมขวาบน จากนั้นคลิกที่ `Delete file`:

![conference](assets/31.webp)


- ตรวจสอบให้แน่ใจว่าคุณยังคงอยู่ในสาขาการทำงานเดียวกัน จากนั้นคลิกที่ปุ่ม `Commit changes`:

![conference](assets/32.webp)


- เพิ่มชื่อและคำอธิบายให้กับการคอมมิตของคุณ จากนั้นคลิกที่ `Commit changes`:

![conference](assets/33.webp)


- กลับไปที่โฟลเดอร์การประชุมของคุณ:

![conference](assets/34.webp)


- คลิกที่ปุ่ม `Add file` จากนั้นคลิกที่ `Create new file`:

![conference](assets/35.webp)


- สร้างไฟล์ markdown (.md) ใหม่โดยตั้งชื่อไฟล์ด้วยตัวบ่งชี้ของภาษาพื้นเมืองของคุณ ไฟล์นี้จะถูกใช้สำหรับการเล่นซ้ำของการประชุมของคุณ ตัวอย่างเช่น หากฉันต้องการเขียนคำอธิบายของการประชุมเป็นภาษาอังกฤษ ฉันจะตั้งชื่อไฟล์นี้ว่า en.md:

![conference](assets/36.webp)


- กรอกไฟล์มาร์กดาวน์นี้โดยใช้เทมเพลตนี้ที่คุณสามารถปรับให้เข้ากับการกำหนดค่าของการประชุมของคุณ:


```markdown
---
name: Paris Bitcoin Conference 2024
description: The largest Bitcoin conference in France with over 8,000 participants each year!
---

# Main Stage

## Friday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Friday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday morning

![video](https://youtu.be/XXXXXXXXXXXX)

## Saturday afternoon

![video](https://youtu.be/XXXXXXXXXXXX)

# Workshop Room

## The Future of Bitcoin Mining: Challenges and Innovations

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto

## Is Privacy Still Possible On Bitcoin?

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto

## Bitcoin Core: Deep Dive into the Codebase

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto

## Building and Securing Bitcoin Wallets With Miniscript

![video](https://youtu.be/XXXXXXXXXXXX)

Speaker: Satoshi Nakamoto
```


![conference](assets/37.webp)


- ที่จุดเริ่มต้นของเอกสารของคุณ ในส่วน "front matter" ให้กรอกข้อมูลในช่อง `name:` ด้วยชื่อของการประชุมของคุณและปีของการเล่นซ้ำ ในช่อง `description:` ให้เขียนคำอธิบายสั้น ๆ ของงานของคุณในภาษาของไฟล์ ตัวอย่างเช่น สำหรับไฟล์ที่ชื่อว่า `en.md` คำอธิบายควรเป็นภาษาอังกฤษ ทีม Plan ₿ Academy จะดูแลการแปลคำอธิบายของคุณโดยใช้โมเดลของพวกเขา
- หัวข้อระดับแรกที่ทำเครื่องหมายด้วย `#` ใช้เพื่อจัดระเบียบการประชุมตามฉาก ตัวอย่างเช่น `# Main Stage` สำหรับเวทีหลักและ `# Workshop Room` สำหรับเวทีที่จัดไว้สำหรับการประชุมเชิงปฏิบัติการ



- หัวข้อระดับสองที่ทำเครื่องหมายด้วย `##` สองครั้ง ใช้เพื่อแยกวิดีโอการเล่นซ้ำที่แตกต่างกัน หากการประชุมถูกถ่ายทำอย่างต่อเนื่องตลอดครึ่งวัน ให้ระบุ เช่น `## เช้าวันศุกร์` หากการประชุมถูกถ่ายทำและออกอากาศเป็นรายบุคคล ให้ตั้งชื่อการประชุมโดยตรงด้วยหัวข้อระดับสอง



- ภายใต้แต่ละชื่อระดับที่สอง ให้แทรกลิงก์ไปยังวิดีโอรีเพลย์ที่สอดคล้องกัน ไวยากรณ์ควรเป็น: `![video](https://youtu.be/XXXXXXXXXXXX)` โดยแทนที่ `XXXXXXXXXXXX` ด้วยลิงก์วิดีโอจริง



- หากรูปแบบอนุญาต (การประชุมแต่ละรายการ) คุณสามารถเพิ่มชื่อของผู้บรรยายได้ ในการทำเช่นนี้ ให้เพิ่มฟิลด์ `Speaker:` ตามด้วยชื่อหรือนามแฝงของผู้บรรยายใต้ลิงก์วิดีโอ ในกรณีที่มีผู้บรรยายหลายคน ให้แยกแต่ละชื่อด้วยเครื่องหมายจุลภาค เช่นนี้เป็นตัวอย่าง: `Speaker: Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto, Satoshi Nakamoto`.


---


- เมื่อคุณแก้ไขไฟล์นี้เสร็จสิ้น ให้บันทึกโดยคลิกที่ปุ่ม `Commit changes...`:

![conference](assets/38.webp)


- เพิ่มชื่อเรื่องสำหรับการแก้ไขของคุณ รวมถึงคำอธิบายสั้น ๆ:

![conference](assets/39.webp)


- คลิกที่ `Commit changes`:

![conference](assets/40.webp)


- โฟลเดอร์การประชุมของคุณควรมีลักษณะดังนี้:

![conference](assets/41.webp)


- หากทุกอย่างเป็นที่น่าพอใจของคุณ ให้กลับไปที่รากของ fork ของคุณ:

![conference](assets/42.webp)


- คุณควรเห็นข้อความที่ระบุว่าสาขาของคุณได้มีการแก้ไขแล้ว คลิกที่ปุ่ม `Compare & pull request`:

![conference](assets/43.webp)


- เพิ่มชื่อและคำอธิบายที่ชัดเจนสำหรับ PR ของคุณ:

![conference](assets/44.webp)


- คลิกที่ปุ่ม `Create pull request`:

![conference](assets/45.webp)

ขอแสดงความยินดี! PR ของคุณได้ถูกสร้างขึ้นเรียบร้อยแล้ว ขณะนี้ผู้ดูแลระบบจะทำการตรวจสอบ และหากทุกอย่างเรียบร้อย จะทำการรวมเข้ากับที่เก็บหลักของ Plan ₿ Academy คุณควรจะเห็นการเล่นซ้ำของการประชุมของคุณปรากฏบนเว็บไซต์ในอีกไม่กี่วันถัดไป


โปรดตรวจสอบความคืบหน้าของ PR ของคุณ อาจเป็นไปได้ว่าผู้ดูแลระบบอาจแสดงความคิดเห็นเพื่อขอข้อมูลเพิ่มเติม ตราบใดที่ PR ของคุณยังไม่ได้รับการตรวจสอบ คุณสามารถดูได้ภายใต้แท็บ `Pull requests` ในที่เก็บ GitHub ของ Plan ₿ Academy:

![conference](assets/46.webp)


ขอบคุณมากสำหรับการมีส่วนร่วมที่มีค่าของคุณ! :)