---
term: BIP66
---

Đã giới thiệu việc chuẩn hóa định dạng chữ ký trong các giao dịch. BIP này được đề xuất nhằm đáp ứng với sự khác biệt trong cách OpenSSL xử lý mã hóa chữ ký trên các hệ thống khác nhau. Sự đa dạng này tạo ra rủi ro chia rẽ blockchain. BIP66 đã chuẩn hóa định dạng chữ ký cho tất cả các giao dịch sử dụng mã hóa DER chặt chẽ (*Distinguished Encoding Rules*). Thay đổi này yêu cầu một soft fork. Để kích hoạt, BIP66 sau đó sử dụng cùng một cơ chế như BIP34, yêu cầu trường `nVersion` được tăng lên phiên bản 3, và từ chối tất cả các khối phiên bản 2 hoặc thấp hơn một khi ngưỡng 95% thợ mỏ được đạt tới. Ngưỡng này đã được vượt qua tại khối số 363,725 vào ngày 4 tháng 7 năm 2015.