---
term: OP_CHECKSIGADD (0XBA)
---

Lấy ba giá trị hàng đầu từ ngăn xếp: một `public key`, một `CScriptNum` `n`, và một `signature`. Nếu chữ ký không phải là vector rỗng và không hợp lệ, script sẽ kết thúc với một lỗi. Nếu chữ ký hợp lệ hoặc là vector rỗng (`OP_0`), hai kịch bản được trình bày:
* Nếu chữ ký là vector rỗng: một `CScriptNum` với giá trị của `n` được đẩy lên ngăn xếp, và việc thực thi tiếp tục;
* Nếu chữ ký không phải là vector rỗng và vẫn hợp lệ: một `CScriptNum` với giá trị của `n + 1` được đẩy lên ngăn xếp, và việc thực thi tiếp tục.
Để đơn giản, `OP_CHECKSIGADD` thực hiện một hoạt động tương tự như `OP_CHECKSIG`, nhưng thay vì đẩy true hoặc false lên ngăn xếp, nó thêm `1` vào giá trị thứ hai ở đỉnh của ngăn xếp nếu chữ ký hợp lệ, hoặc giữ nguyên giá trị này nếu chữ ký đại diện cho vector rỗng. `OP_CHECKSIGADD` cho phép tạo ra các chính sách đa chữ ký giống như với `OP_CHECKMULTISIG` và `OP_CHECKMULTISIGVERIFY` nhưng theo cách có thể xác minh hàng loạt, nghĩa là nó loại bỏ quá trình tìm kiếm trong việc xác minh một multisig truyền thống và do đó tăng tốc độ xác minh trong khi giảm tải hoạt động trên CPU của các nút. Mã lệnh này được thêm vào Tapscript đặc biệt cho nhu cầu của Taproot.