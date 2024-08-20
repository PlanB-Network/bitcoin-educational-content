---
term: BLOCKS/REV*.DAT
---

Tên của các tệp tin trong Bitcoin Core chứa thông tin cần thiết để có thể đảo ngược các thay đổi đã được thực hiện đối với bộ UTXO bởi các khối đã được thêm vào trước đó. Mỗi tệp tin được xác định bởi một số duy nhất tương ứng với tệp blk*.dat mà nó tương ứng. Các tệp rev*.dat chứa dữ liệu đảo ngược tương ứng với các khối được lưu trữ trong các tệp blk*.dat. Dữ liệu này cơ bản là danh sách tất cả các UTXO đã được sử dụng làm đầu vào trong một khối. Những tệp đảo ngược này cho phép nút quay trở lại trạng thái trước đó trong trường hợp của một tái tổ chức blockchain khiến cho các khối đã được xác thực trước đó phải bị loại bỏ.