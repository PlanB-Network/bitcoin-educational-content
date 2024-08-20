---
term: HÀM BĂM
---

Là một hàm toán học nhận đầu vào có kích thước biến đổi (gọi là thông điệp) và tạo ra đầu ra có kích thước cố định (gọi là băm, mã hóa băm, tóm tắt, hoặc dấu vân tay). Hàm băm được sử dụng rộng rãi trong lĩnh vực mật mã học. Chúng thể hiện các tính chất đặc biệt làm cho chúng phù hợp để sử dụng trong các ngữ cảnh an toàn:
* Kháng ảnh ngược: phải rất khó để tìm ra một thông điệp tạo ra một băm cụ thể, tức là, tìm một ảnh ngược $m$ cho một băm $h$ sao cho $h = H(m)$, nơi $H$ là hàm băm;
* Kháng ảnh ngược thứ hai: cho một thông điệp $m_1$, phải rất khó để tìm một thông điệp khác $m_2$ (khác với $m_1$) sao cho $H(m_1) = H(m_2)$;
* Kháng va chạm: phải rất khó để tìm hai thông điệp riêng biệt $m_1$ và $m_2$ sao cho $H(m_1) = H(m_2)$;
* Kháng can thiệp: những thay đổi nhỏ trong đầu vào phải gây ra những thay đổi đáng kể và không dự đoán được trong đầu ra.

Trong bối cảnh của Bitcoin, hàm băm được sử dụng cho một số mục đích, bao gồm cơ chế chứng minh công việc (*Proof-of-Work*), định danh giao dịch, tạo địa chỉ, tính toán checksum, và tạo ra các cấu trúc dữ liệu như cây Merkle. Về phía giao thức, Bitcoin sử dụng độc quyền hàm `SHA256d`, còn được gọi là `HASH256`, bao gồm một băm `SHA256` kép. `HASH256` cũng được sử dụng trong việc tính toán một số checksum, đặc biệt là cho các khóa mở rộng (`xpub`, `xprv`...). Về phía ví, cũng sử dụng các hàm sau:
* `SHA256` đơn giản cho checksum của cụm từ ghi nhớ;
* `SHA512` trong các thuật toán `HMAC` và `PBKDF2` được sử dụng trong quá trình tạo ra ví xác định và phân cấp;
* `HASH160`, mô tả việc sử dụng liên tiếp một `SHA256` và một `RIPEMD160`. `HASH160` được sử dụng trong quá trình tạo ra địa chỉ nhận (trừ P2PK và P2TR) và trong việc tính toán dấu vân tay khóa cha cho các khóa mở rộng.

> ► *Trong tiếng Anh, nó được gọi là "hash function".*