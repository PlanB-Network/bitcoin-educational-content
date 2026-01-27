---
name: คู่มือการรันแพลตฟอร์ม Plan ₿ Academy ในเครื่อง
description: คุณจะเรียกใช้ Plan ₿ Academy ในสภาพแวดล้อมท้องถิ่นเพื่อทดสอบการมีส่วนร่วมของเนื้อหาหรือการพิสูจน์อักษร/การตรวจทานเนื้อหาการศึกษาใน Plan ₿ Academy ได้อย่างไร?
---
![github](assets/cover.webp)


## โดยสรุป


บทแนะนำนี้ให้คำแนะนำทีละขั้นตอนสำหรับการตั้งค่า Bitcoin Learning Management System จาก Plan ₿ Academy บนเครื่องท้องถิ่นของคุณโดยใช้ Docker, คีย์จำลอง, และการกำหนดค่าคลังเก็บที่กำหนดเอง


หากคุณไม่เข้าใจส่วนด้านบน ไม่ต้องกังวล—บทแนะนำนี้เหมาะสำหรับคุณ!


---

## **วิธีการรันระบบการจัดการการเรียนรู้ Bitcoin ในเครื่อง**


บทแนะนำนี้ให้ขั้นตอนโดยละเอียดในการตั้งค่าแพลตฟอร์ม จัดการคีย์จำลอง และปรับแต่งที่เก็บข้อมูล ทำตามขั้นตอนด้านล่างเพื่อหลีกเลี่ยงปัญหาทั่วไปและกำหนดค่าสภาพแวดล้อมในเครื่องของคุณอย่างถูกต้อง



**1. ข้อกำหนดเบื้องต้น**


- เครื่อง Linux ที่ติดตั้ง Docker และ Docker Compose (มีรายงานว่าใช้งานได้บน Windows ด้วย)
- เวอร์ชัน `nodejs` ที่เพียงพอ (ทดสอบแล้ว: 22.12.0)
- ติดตั้ง `pnpm` บนระบบของคุณแล้ว
- Git ถูกกำหนดค่าสำหรับการโคลนที่เก็บข้อมูลแล้ว



**2. โคลนที่เก็บข้อมูล**

คัดลอกที่เก็บไปยังเครื่องของคุณ:


git clone [https://github.com/PlanB-Network/bitcoin-learning-management-system](https://github.com/PlanB-Network/bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/bitcoin-learning-management-system￼cd) bitcoin-learning-management-system


```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```



**3. ตั้งค่าตัวแปรสภาพแวดล้อม**


1\. คัดลอกไฟล์ `.env.example`:


```bash
cp .env.example .env
```


1. แก้ไขไฟล์ `.env` โดยลบส่วน .example ออกจากชื่อ ตอนนี้คุณต้องใส่คีย์จำลองสำหรับตัวแปรที่จำเป็น ตัวอย่าง:


⚠️ นี่เป็นขั้นตอนบังคับ การข้ามขั้นตอนนี้จะส่งผลให้เกิดข้อผิดพลาด เช่น การปฏิเสธการเชื่อมต่อระหว่างบางคอนเทนเนอร์


อย่าลืมเพิ่ม Github PAT เฉพาะของคุณในไฟล์ด้วย



```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```


---

**4. ติดตั้งการพึ่งพา**


`Be sure` ที่จะติดตั้ง nodejs เวอร์ชันที่เหมาะสม ณ เดือน 2024-12, v22.12.0 (LTS) ได้รับการพิสูจน์แล้วว่าสามารถทำงานได้



⚠️ Ubuntu 22.04 repository nodejs version is 12.22.9: too old to allow you install pnpm



ในการติดตั้ง nodejs ค้นหาคำแนะนำ [ที่นี่](https://nodejs.org/en/download/package-manager); ตัวอย่างเช่น คุณอาจเลือกใช้วิธีการติดตั้ง `nvm`


---

ก่อนเริ่มขั้นตอนการติดตั้งแพ็คเกจที่จำเป็นด้วย pnpm โปรดตรวจสอบให้แน่ใจว่ามีการติดตั้ง dependencies ทั้งหมดแล้ว คุณสามารถทำได้โดยการรันคำสั่งต่อไปนี้:


```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```


---

ภายในโฟลเดอร์ `../bitcoin-learning-management-system/` ของคุณ ให้รันคำสั่งต่อไปนี้เพื่อติดตั้ง `pnpm`


```bash
pnpm install
```


__เคล็ดลับ:__อย่าลืมอัปเดตทั้ง dependencies และ pnpm เองเป็นระยะๆ



**5. รันคอนเทนเนอร์**

ภายในโฟลเดอร์ `../bitcoin-learning-management-system/` ของคุณ เริ่มต้นสภาพแวดล้อมการพัฒนาด้วย Docker:


```bash
docker compose up --build -V
```

คุณยังสามารถรันคำสั่งถัดไปนี้ในลักษณะนี้ได้ แต่คุณจะไม่เห็นบันทึกในเทอร์มินัลของคุณ

```bash
docker compose up -d --build -V
```


สิ่งนี้จะสร้างและเริ่มต้นคอนเทนเนอร์ทั้งหมดที่จำเป็นจาก dockers.


**6. เข้าถึงแอปพลิเคชัน**

เมื่อคอนเทนเนอร์ทำงานแล้ว เข้าถึงส่วนหน้าที่:

\[<http://localhost:8181](http://localhost:8181)>


![Plan ₿ Academy Local](assets/en/1.webp)


หมายเหตุ: แอปจะรีโหลดโดยอัตโนมัติหากคุณเปลี่ยนแปลงไฟล์ต้นฉบับใด ๆ



**7.** ตั้งค่าสคีมาฐานข้อมูลของคุณ


ในการรันครั้งแรก คุณจะต้องรันการย้ายข้อมูลของฐานข้อมูล (DB migrations)


ในการทำเช่นนั้น ให้รันสคริปต์การย้ายข้อมูล: `pnpm run dev:db:migrate`


```markdown
pnpm run dev:db:migrate
```


**8. นำเข้าข้อมูลจากที่เก็บข้อมูล**

ในการนำเข้าข้อมูลเข้าสู่ฐานข้อมูล ให้ทำการร้องขอไปยัง API:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


**9. แก้ไขปัญหาการเข้าถึงซิงค์โวลุ่ม**

หากคุณพบปัญหาในการเข้าถึง `cdn` และ `sync` volumes ให้รัน:


```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```


แล้วอีกครั้ง:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


![Plan ₿ Academy Local](assets/en/2.webp)



**10. ปรับแต่งที่เก็บ (ไม่บังคับ)**

หากคุณจำเป็นต้องใช้ fork หรือสาขาเฉพาะ:

1. แก้ไขไฟล์ `.env` เพื่ออัปเดตตัวแปรต่อไปนี้:


```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```


2\. รีสตาร์ท Docker:


```markdown
docker compose down -v
docker compose up --build -V
```


3\. ซิงค์ข้อมูลที่เก็บใหม่:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


บทแนะนำนี้ช่วยให้แน่ใจว่าแพลตฟอร์มถูกตั้งค่าอย่างถูกต้องด้วยคีย์จำลอง ติดตั้งการพึ่งพา และปรับแต่งที่เก็บตามต้องการ 🎉 โชคดีกับการตั้งค่าของคุณ!


**คำสั่งสำหรับความช่วยเหลือเพิ่มเติม**


หยุดคอนเทนเนอร์ทั้งหมด


```
docker compose down
```


ลบคอนเทนเนอร์และโวลุ่มที่มีอยู่ทั้งหมด


```
docker container prune -f
docker volume prune --all
```


สร้างคอนเทนเนอร์ใหม่ด้วยคำสั่งเดียวกันกับที่ใช้ในคู่มือทางการและเปิดใช้งานสคริปต์ซิงค์:


```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```