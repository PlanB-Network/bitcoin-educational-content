---
term: OP_NOP (0X61)
---

Không tạo ra bất kỳ tác động nào lên stack hay trạng thái của script. Nó không thực hiện bất kỳ di chuyển, kiểm tra, hay chỉnh sửa nào. Nó đơn giản không làm gì cả trừ khi quyết định khác thông qua một soft fork. Thực tế, kể từ khi được Satoshi Nakamoto sửa đổi vào năm 2010, các lệnh `OP_NOP` (`OP_NOP1` (`0XB0`) đến `OP_NOP10` (`0XB9`)) được sử dụng để thêm mới các opcode dưới hình thức của một soft fork.

Do đó, `OP_NOP2` (`0XB1`) và `OP_NOP3` (`0XB2`) đã được sử dụng để triển khai `OP_CHECKLOCKTIMEVERIFY` và `OP_CHECKSEQUENCEVERIFY` tương ứng. Chúng được sử dụng kết hợp với `OP_DROP` để loại bỏ các giá trị thời gian tạm thời khỏi stack, cho phép việc thực thi script tiếp tục, bất kể node có được cập nhật hay không. Các lệnh `OP_NOP`, do đó, cho phép việc chèn một điểm gián đoạn trong script để kiểm tra các điều kiện bổ sung đã tồn tại hoặc có thể được thêm vào với các soft fork trong tương lai. Kể từ Tapscript, việc sử dụng `OP_NOP` đã được thay thế bằng `OP_SUCCESS` hiệu quả hơn.