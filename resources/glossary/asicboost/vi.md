---
term: ASICBOOST
---

ASICBOOST là một phương pháp tối ưu hóa thuật toán được phát minh vào năm 2016, được thiết kế để tăng hiệu quả của việc đào Bitcoin khoảng 20% bằng cách giảm số lượng tính toán cần thiết cho mỗi lần thử hash của tiêu đề. Kỹ thuật này khai thác một tính năng của hàm băm SHA256, được sử dụng cho việc đào, phân chia dữ liệu thành các khối trước khi xử lý chúng. ASICBOOST giữ nguyên một trong những khối này qua nhiều lần thử hash, cho phép thợ mỏ chỉ cần thực hiện một phần công việc cho khối này qua nhiều lần thử. Việc chia sẻ dữ liệu này cho phép tái sử dụng kết quả từ các tính toán trước đó, do đó giảm tổng số lượng tính toán cần thiết để tìm ra một hash hợp lệ.

ASICBOOST có thể được sử dụng dưới hai hình thức: ASICBOOST Công khai và ASICBOOST Kín đáo. Hình thức ASICBOOST Công khai là có thể nhìn thấy bởi mọi người, vì nó liên quan đến việc sử dụng trường `nVersion` của khối như một nonce, và không thay đổi `Nonce` thực sự. Hình thức Kín đáo tìm cách ẩn những thay đổi này bằng cách sử dụng cây Merkle. Tuy nhiên, phương pháp thứ hai này đã trở nên kém hiệu quả hơn kể từ khi giới thiệu SegWit do cây Merkle thứ hai, làm tăng số lượng tính toán cần thiết để sử dụng nó.

Tóm lại, ASICBOOST cho phép thợ mỏ không phải thực hiện một SHA256 hoàn chỉnh thực sự cho tất cả các lần thử hash, vì một phần kết quả vẫn không thay đổi, điều này tăng tốc công việc của thợ mỏ.