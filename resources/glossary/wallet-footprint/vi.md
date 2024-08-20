---
term: DẤU VẾT VÍ
---

Một tập hợp các đặc điểm nổi bật có thể quan sát được trong các giao dịch do cùng một ví Bitcoin thực hiện. Những đặc điểm này có thể bao gồm sự tương đồng trong việc sử dụng các loại script, việc tái sử dụng địa chỉ, thứ tự của UTXOs, vị trí của các output thay đổi, việc báo hiệu RBF (*Replace-by-Fee*), số phiên bản, trường `nSequence`, và trường `nLockTime`.

Dấu vết ví được các nhà phân tích sử dụng để truy vết hoạt động của một thực thể cụ thể trên blockchain bằng cách xác định các mô hình lặp lại trong các giao dịch của nó. Ví dụ, một người dùng thường xuyên gửi tiền lẻ của họ đến các địa chỉ P2TR (`bc1p…`) tạo ra một dấu vết đặc trưng có thể được sử dụng để theo dõi các giao dịch tương lai của họ.

Như LaurentMT giải thích trong Space Kek #19 (một podcast nói tiếng Pháp), tính hữu ích của dấu vết ví trong phân tích chuỗi tăng lên đáng kể theo thời gian. Thực vậy, số lượng loại script ngày càng tăng và việc triển khai dần dần các tính năng mới này bởi phần mềm ví làm nổi bật các sự khác biệt. Thậm chí, có thể xác định chính xác phần mềm được thực thể đang được truy vết sử dụng. Do đó, quan trọng là phải hiểu rằng việc nghiên cứu dấu vết của một ví đặc biệt liên quan đến các giao dịch gần đây, hơn là những giao dịch được khởi xướng vào đầu những năm 2010.