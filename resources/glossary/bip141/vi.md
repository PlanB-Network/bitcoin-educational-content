---
term: BIP141
---

Giới thiệu khái niệm Segregated Witness (SegWit) đã đặt tên cho SegWit soft fork. BIP141 đưa ra một sửa đổi lớn đối với giao thức Bitcoin nhằm giải quyết vấn đề biến đổi giao dịch. SegWit tách dữ liệu chứng thực (dữ liệu chữ ký) ra khỏi phần còn lại của dữ liệu giao dịch. Sự tách biệt này được thực hiện bằng cách chèn các chứng thực vào một cấu trúc dữ liệu riêng biệt, được cam kết trong một cây Merkle mới, cây này lại được tham chiếu trong block thông qua giao dịch coinbase, làm cho SegWit tương thích với các phiên bản cũ hơn của giao thức.