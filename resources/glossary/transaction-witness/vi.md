---
term: CHỨNG NHÂN GIAO DỊCH
---

Đề cập đến một thành phần của giao dịch Bitcoin đã được di chuyển với bản cập nhật mềm SegWit để giải quyết vấn đề biến đổi giao dịch. Chứng nhân bao gồm các chữ ký và khóa công khai cần thiết để mở khóa bitcoin đã chi trong một giao dịch. Trong giao dịch Legacy, chứng nhân đại diện cho tổng `scriptSig` từ tất cả các đầu vào. Trong giao dịch SegWit, chứng nhân đại diện cho tổng `scriptWitness` cho mỗi đầu vào, và phần này của giao dịch giờ đây được chuyển vào một cây Merkle riêng biệt trong khối.

Trước SegWit, các chữ ký có thể được thay đổi một chút mà không bị vô hiệu hóa trước khi một giao dịch được xác nhận, điều này thay đổi mã định danh giao dịch. Điều này làm cho việc xây dựng các giao thức khác nhau trở nên khó khăn, vì một giao dịch chưa được xác nhận có thể thấy mã định danh của mình thay đổi. Bằng cách tách biệt các chứng nhân, SegWit làm cho giao dịch không thể biến đổi, vì bất kỳ sự thay đổi nào trong các chữ ký không còn ảnh hưởng đến mã định danh giao dịch (TXID), mà chỉ ảnh hưởng đến mã định danh chứng nhân (WTXID). Ngoài việc giải quyết vấn đề biến đổi, sự tách biệt này cho phép tăng khả năng chứa của mỗi khối.

> ► *Trong tiếng Anh, "témoin" được dịch là "witness".*