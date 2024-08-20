---
term: COINBASE (GIAO DỊCH)
---

Giao dịch coinbase là một giao dịch đặc biệt và duy nhất được bao gồm trong mỗi khối của blockchain Bitcoin. Nó đại diện cho giao dịch đầu tiên của một khối và được tạo bởi người đào đã thành công tìm ra header xác thực công việc chứng minh (*Proof-of-Work*), tức là, nhỏ hơn hoặc bằng mục tiêu.

Giao dịch coinbase chủ yếu phục vụ hai mục đích: trao thưởng khối cho người đào và thêm các đơn vị bitcoin mới vào lượng tiền lưu thông. Phần thưởng khối, là động lực kinh tế để người đào tham gia vào công việc chứng minh, bao gồm các phí tích lũy cho các giao dịch được bao gồm trong khối và một lượng bitcoin mới được tạo ra từ không (subsidy khối). Số lượng này, ban đầu được thiết lập là 50 bitcoin cho mỗi khối vào năm 2009, được giảm một nửa sau mỗi 210,000 khối (khoảng mỗi 4 năm) trong một sự kiện được gọi là "halving."

Giao dịch coinbase khác biệt so với các giao dịch thông thường ở một số điểm. Đầu tiên, nó không có đầu vào, nghĩa là không có đầu ra giao dịch hiện có (UTXO) nào được tiêu thụ bởi nó. Tiếp theo, script chữ ký (`scriptSig`) cho giao dịch coinbase thường chứa một trường tùy ý cho phép kết hợp thêm dữ liệu, như thông điệp tùy chỉnh hoặc thông tin phiên bản phần mềm đào. Cuối cùng, các bitcoin được tạo ra bởi giao dịch coinbase phải trải qua một thời gian chờ đợi 100 khối (101 xác nhận) trước khi chúng có thể được tiêu, để ngăn chặn khả năng chi tiêu các bitcoin không tồn tại trong trường hợp tái tổ chức chuỗi.

> ► *Không có bản dịch cho "Coinbase" trong tiếng Pháp. Do đó, việc sử dụng trực tiếp thuật ngữ này được chấp nhận.*