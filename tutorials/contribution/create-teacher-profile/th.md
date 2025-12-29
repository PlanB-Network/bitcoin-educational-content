---
name: ศาสตราจารย์ Plan ₿ Academy
description: ฉันจะเพิ่มหรือแก้ไขโปรไฟล์ครูของฉันบน Plan ₿ Academy ได้อย่างไร?
---
![cover](assets/cover.webp)


หากคุณวางแผนที่จะมีส่วนร่วมใน Plan ₿ Academy โดยการเขียนบทแนะนำหรือหลักสูตรใหม่ คุณจะต้องมีโปรไฟล์ครู โปรไฟล์นี้จะช่วยให้คุณได้รับเครดิตที่เหมาะสมสำหรับเนื้อหาที่คุณมีส่วนร่วมในแพลตฟอร์ม


สำหรับผู้ที่มีส่วนร่วมในการสร้างเนื้อหาการศึกษาใน Plan ₿ Academy อยู่แล้ว คุณอาจมีโปรไฟล์ครูอยู่แล้ว คุณสามารถค้นหาได้ในโฟลเดอร์ `/professors` [บนที่เก็บ GitHub ของเรา](https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors) หากโปรไฟล์ของคุณมีอยู่แล้ว ให้ค้นหาการเข้าสู่ระบบของคุณในไฟล์ `professor.yml`


หากต้องการเปลี่ยนแปลงโปรไฟล์ของคุณ ไปที่ส่วน "แก้ไขโปรไฟล์ครูของคุณ" ที่ท้ายบทแนะนำนี้


## เพิ่มครูใหม่ด้วยซอฟต์แวร์ของเรา


วิธีที่ง่ายที่สุดในการสร้างโปรไฟล์ครูของคุณบน Plan ₿ Academy คือการใช้เครื่องมือ Python ที่เรารวมไว้ นี่คือวิธีการทำงาน


### 1 - กำหนดค่าการตั้งค่าสภาพแวดล้อมในเครื่องของคุณ


คุณต้องมี Fork ของคุณเองจาก [Plan ₿ Academy repository on GitHub](https://github.com/PlanB-Network/Bitcoin-educational-content).


ซิงโครไนซ์สาขาหลัก (`dev`) ของ Fork ของคุณกับที่เก็บต้นทาง


อัปเดตโคลนในเครื่องของคุณ


```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<username>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```


### 2 - สร้างสาขาใหม่


ตรวจสอบให้แน่ใจว่าคุณอยู่บนสาขา `dev` สร้างสาขาใหม่ด้วยชื่อที่อธิบายได้ (เช่น `add-professor-loic-morel`)


เผยแพร่สาขานี้บน Fork ออนไลน์ของคุณ


```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```


### 3 - สร้างโปรไฟล์ครูของคุณ


ไปที่โฟลเดอร์ `scripts/tutorial-related/data-creator/` บนโคลนในเครื่องของคุณ ตรวจสอบให้แน่ใจว่าคุณได้ติดตั้งการพึ่งพาทั้งหมดที่จำเป็นสำหรับซอฟต์แวร์แล้ว โดยได้ติดตั้ง Python ก่อน:


```bash
pip install -r requirements.txt
```


จากนั้นเปิดซอฟต์แวร์ด้วยคำสั่ง:


```bash
python3 main.py
```


เมื่ออยู่ที่หน้าแรก ให้ป้อนเส้นทางในเครื่องไปยังโคลนที่เก็บของคุณ ภาษาที่คุณกำลังเขียน และ GitHub ID ของคุณ หากคุณกำลังสร้างโปรไฟล์นี้ให้กับผู้อื่นและมีโปรไฟล์ของศาสตราจารย์อยู่แล้ว ให้ป้อน ID ของคุณในช่อง "*Plan ₿ Academy Professor's ID*" หากคุณกำลังสร้างโปรไฟล์ของคุณเอง คุณจะยังไม่มี Professor's ID เนื่องจากคุณกำลังอยู่ในกระบวนการสร้าง ดังนั้นให้เว้นช่องนี้ว่างไว้


จากนั้นคลิกที่ปุ่ม "*New Professor*"


![Image](assets/fr/01.webp)


กรอกข้อมูลที่จำเป็น (โปรดทราบว่าข้อมูลทั้งหมดนี้จะเป็นสาธารณะบนแพลตฟอร์มของเราและบน GitHub):




- ชื่อไฟล์ครูของคุณ (ใช้ชื่อและนามสกุลของคุณหรือใช้นามแฝงเป็นตัวพิมพ์เล็ก) ;
- ชื่อหรือนามแฝงของคุณ ;
- เว็บไซต์และโปรไฟล์ X (ถ้ามี) ;
- ที่อยู่ Lightning สำหรับรับบริจาคจากผู้อ่าน (ไม่บังคับ) ;
- เลือก 2 หรือ 3 แท็กจากรายการ;
- คลิกที่ "*Select Image*" เพื่อเลือกภาพโปรไฟล์จากโฟลเดอร์ในเครื่องของคุณ (สามารถใช้ชื่อและรูปแบบใดก็ได้สำหรับภาพ และซอฟต์แวร์จะปรับให้โดยอัตโนมัติ เพียงแค่ตรวจสอบให้แน่ใจว่าภาพเป็นสี่เหลี่ยมจัตุรัส);
- เขียนคำอธิบายสั้น ๆ เกี่ยวกับโปรไฟล์ของคุณ


คลิกที่ "*Create Professor*" เพื่อเสร็จสิ้นการสร้าง ระบบจะทำการ generate ไฟล์ทั้งหมดที่จำเป็นสำหรับโปรไฟล์ของคุณโดยอัตโนมัติ


![Image](assets/fr/02.webp)


บันทึกการเปลี่ยนแปลงของคุณในเครื่องโดยการสร้าง commit พร้อมข้อความอธิบาย ดันการเปลี่ยนแปลงไปยัง GitHub Fork ของคุณ


```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```


เมื่อเสร็จสิ้น ให้สร้างคำขอการดึง (PR) บน GitHub เพื่อเสนอการรวมการแก้ไขของคุณ เพิ่มชื่อและคำอธิบายสั้น ๆ ให้กับ PR


### 4 - การพิสูจน์อักษรและการรวม


รอการตรวจสอบหรือข้อเสนอแนะจากผู้ดูแลระบบ หากจำเป็นให้ทำการแก้ไขและส่งคอมมิตใหม่


```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```


เมื่อ PR ถูกรวมแล้ว คุณสามารถลบสาขาการทำงานของคุณได้


## แก้ไขโปรไฟล์ครูของคุณ


หากคุณเชี่ยวชาญการใช้ Git แล้ว ให้แก้ไขโปรไฟล์ครูของคุณโดยการสร้างสาขาใหม่และแก้ไขไฟล์ที่เกี่ยวข้องโดยตรงในโฟลเดอร์ที่มีอยู่ของคุณ การเปลี่ยนแปลงสามารถทำได้ทั้งในไฟล์ `professor.yml` หรือในไฟล์ markdown ขึ้นอยู่กับข้อมูลที่ต้องการแก้ไข เมื่อคุณทำการเปลี่ยนแปลงในเครื่องแล้ว ให้ส่งไปยัง Fork ของคุณและส่ง PR


สำหรับผู้เริ่มต้น ฉันแนะนำให้ทำการแก้ไขโดยตรงผ่านเว็บ Interface ของ GitHub ตรวจสอบให้แน่ใจว่าคุณมีบัญชี GitHub หากคุณไม่ทราบวิธีสร้างบัญชี ให้ทำตามบทช่วยสอนนี้:


https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
ไปที่ [ที่เก็บ GitHub ของ Plan ₿ Academy ที่อุทิศให้กับข้อมูล](https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors)


![Image](assets/fr/03.webp)


คลิกที่โฟลเดอร์ "*professors*" จากนั้นไปที่โฟลเดอร์ส่วนตัวของคุณ


![Image](assets/fr/04.webp)


หากต้องการเปลี่ยนแปลงข้อมูลเมตาของโปรไฟล์ เช่น ที่อยู่ Lightning ชื่อ หรือ ลิงก์ ให้เลือกไฟล์ "*professor.yml*" หากต้องการเปลี่ยนคำอธิบาย ให้คลิกที่ไฟล์ YAML สำหรับภาษาของคุณ (เช่น "*en.yml*" หรือ "*fr.yml*")


หากคุณแก้ไขคำอธิบายของคุณ อย่าลืมลบคำแปลที่ล้าสมัยทั้งหมด จากนั้นคุณสามารถจัดการแปลคำอธิบายของคุณเป็นภาษาอื่นๆ ด้วยความช่วยเหลือของ LLM หรือปล่อยให้มีเพียงคำอธิบายในภาษาของคุณและระบุในคำขอ Pull ของคุณว่าคำอธิบายของคุณต้องการการแปลโดยทีมของเรา


![Image](assets/fr/05.webp)


เมื่ออยู่ในไฟล์ที่คุณต้องการแก้ไข ให้คลิกที่ไอคอนรูปดินสอ


![Image](assets/fr/06.webp)


หากคุณยังไม่มี Fork จากที่เก็บ Plan ₿ Academy, GitHub จะแนะนำให้คุณสร้างหนึ่งอัน คลิกที่ "*Fork this repository*"


![Image](assets/fr/07.webp)


ทำการเปลี่ยนแปลงที่ต้องการในไฟล์ เมื่อเสร็จแล้ว คลิกที่ "*Commit changes*"


![Image](assets/fr/08.webp)


ป้อนข้อความอธิบายการเปลี่ยนแปลงของคุณ จากนั้นเลือก "*เสนอการเปลี่ยนแปลง*".


![Image](assets/fr/09.webp)


สรุปการเปลี่ยนแปลงของคุณจะแสดงขึ้น หากคุณต้องการเปลี่ยนแปลงโปรไฟล์เพิ่มเติม คุณสามารถกลับไปที่โฟลเดอร์และทำการคอมมิตเพิ่มเติมได้ เมื่อเสร็จสิ้น ให้คลิกที่ "*Create pull request*"


คำขอการดึง (Pull Request) คือคำขอที่ทำเพื่อรวมการเปลี่ยนแปลงจากสาขาของคุณเข้าสู่สาขาหลักของที่เก็บ Plan ₿ Academy ซึ่งช่วยให้สามารถตรวจสอบและอภิปรายเกี่ยวกับการเปลี่ยนแปลงก่อนที่จะถูกรวมเข้าด้วยกัน


![Image](assets/fr/10.webp)


ตรวจสอบให้แน่ใจว่า ที่ด้านบนของ Interface สาขาที่คุณกำลังทำงานอยู่ได้ถูกรวมเข้ากับสาขา `dev` ของที่เก็บ Plan ₿ Academy (ซึ่งเป็นสาขาหลัก) แล้ว


ใส่ชื่อเรื่องที่สรุปการเปลี่ยนแปลงที่คุณต้องการรวมเข้ากับที่เก็บข้อมูลต้นทาง เพิ่มความคิดเห็นสั้น ๆ ที่อธิบายการเปลี่ยนแปลงเหล่านี้ จากนั้นคลิกที่ปุ่มสีเขียว "*Create pull request*" เพื่อยืนยันการดึงคำขอ:


![Image](assets/fr/11.webp)


PR ของคุณจะปรากฏในแท็บ "*Pull Request*" ของที่เก็บหลัก Plan ₿ Academy สิ่งที่คุณต้องทำตอนนี้คือรอให้ผู้ดูแลระบบรวมการแก้ไขของคุณ


![Image](assets/fr/12.webp)


หากคุณพบปัญหาทางเทคนิคในการส่งการเปลี่ยนแปลงของคุณ โปรดอย่าลังเลที่จะขอความช่วยเหลือใน [กลุ่ม Telegram ของเราที่อุทิศให้กับการมีส่วนร่วม](https://t.me/PlanBNetwork_ContentBuilder) ขอบคุณมาก!