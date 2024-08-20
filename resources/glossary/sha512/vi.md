---
term: SHA512
---

Thuật ngữ viết tắt cho "*Secure Hash Algorithm 512 bits*" (Thuật toán Băm An toàn 512 bit). Đây là một hàm băm mật mã tạo ra một đoạn băm 512-bit. Nó được thiết kế bởi *Cơ quan An ninh Quốc gia* (NSA) vào đầu những năm 2000. Đối với Bitcoin, hàm `SHA512` không được sử dụng trực tiếp trong giao thức, nhưng nó được sử dụng trong bối cảnh sinh khóa con ở cấp độ ứng dụng, theo BIP32 và BIP39. Trong những quy trình này, nó được sử dụng nhiều lần trong thuật toán `HMAC`, cũng như trong hàm sinh khóa `PBKDF2`. Hàm `SHA512` là một phần của gia đình SHA 2, giống như `SHA256`. Cách hoạt động của nó rất giống với hàm sau.