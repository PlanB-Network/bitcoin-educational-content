---
term: STAMPS
---

Một giao thức cho phép tích hợp dữ liệu hình ảnh đã được định dạng trực tiếp vào blockchain Bitcoin thông qua các giao dịch đa chữ ký thô (P2MS). Stamps mã hóa nội dung nhị phân của một hình ảnh dưới dạng base 64 và thêm nó vào các khóa của một P2MS 1/3. Một khóa là thực và được sử dụng để chi tiêu các khoản tiền, trong khi hai khóa còn lại là khóa giả (khóa riêng tương ứng không được biết) dùng để lưu trữ dữ liệu. Bằng cách mã hóa dữ liệu trực tiếp dưới dạng khóa công khai thay vì sử dụng đầu ra `OP_RETURN`, hình ảnh được lưu trữ bằng giao thức Stamps đặc biệt tạo ra khối lượng công việc nặng nề cho các nút. Phương pháp này đáng chú ý tạo ra nhiều UTXO, làm tăng kích thước của bộ UTXO và gây ra vấn đề cho các nút đầy đủ.