---
name: BTCPay Server - USDT
description: ขั้นตอนการกำหนดค่า USDT ปลั๊กอิน
---

⚠️ **การแจ้งเตือนความปลอดภัยขั้นวิกฤต (7 สิงหาคม 2026):** ขณะนี้มีช่องโหว่ร้ายแรงที่ส่งผลกระทบต่อ BTCPay Server ซึ่งกำลังถูกโจมตีอย่างต่อเนื่องและอาจทำให้สูญเสียเงินทุนได้ กรุณาอัปเดตอินสแตนซ์ของคุณเป็น **version 2.4.2** ทันทีผ่าน `Admin Dashboard > Server > Maintenance > Update` จากนั้นตรวจสอบว่าส่วนท้ายหน้า (footer) แสดงเป็น `2.4.2` หากคุณไม่สามารถอัปเดตได้ในทันที ให้ปิดการทำงานของ BTCPay Server ของคุณ เมื่ออัปเดตเสร็จแล้ว คุณยังต้องสร้าง macaroons และ `macaroons.db` ขึ้นใหม่ทั้งหมด สร้างสตริงการยืนยันตัวตนของ Lightning backend อื่น ๆ ขึ้นใหม่ทั้งหมด และหากคุณสร้างกระเป๋าเงินแบบ hot on-chain ไว้ภายใน BTCPay Server ให้ย้ายเงินออกจากกระเป๋านั้นและสร้างกระเป๋าใหม่ ผู้ที่ทำการเชื่อมต่อระบบ (integrators) ควรอัปเดต NBXplorer เป็น version 2.6.10 ด้วย แหล่งที่มา: [บันทึกการเผยแพร่ BTCPay Server 2.4.2](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2)

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b
![cover](assets/cover.webp)


ในวิดีโอนี้ คุณจะได้เรียนรู้วิธีการตั้งค่า USDT plugin บน BTCPay Server สำหรับร้านค้าออนไลน์ของคุณ คุณจะได้เรียนรู้วิธีการติดตั้งปลั๊กอินผ่านตัวจัดการปลั๊กอิน การกำหนดค่าเซิร์ฟเวอร์เพื่อเพิ่มความพร้อมใช้งานโดยใช้โหนดเฉพาะ และการตั้งค่ากระเป๋าเงินของคุณเพื่อรับการชำระเงินอย่างปลอดภัย



![BTCPay-Tether](https://youtu.be/hAymYr6YDMY)