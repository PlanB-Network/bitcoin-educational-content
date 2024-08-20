---
term: IP_ASN.MAP
---

Tệp được sử dụng trong Bitcoin Core để lưu trữ ASMAP, giúp cải thiện việc phân loại (tức là nhóm) các địa chỉ IP bằng cách dựa vào Số Hệ Thống Tự Trị (ASN). Thay vì nhóm các kết nối ra bằng tiền tố mạng IP (/16), tệp này cho phép đa dạng hóa các kết nối bằng cách thiết lập một bản đồ địa chỉ IP tới các ASN, là những bộ nhận dạng duy nhất cho mỗi mạng trên Internet. Ý tưởng là cải thiện an ninh và cấu trúc mạng của Bitcoin bằng cách đa dạng hóa các kết nối để bảo vệ chống lại một số cuộc tấn công (đáng chú ý là cuộc tấn công Erebus).