---
term: ECDSA
---

Thuật ngữ viết tắt cho "Elliptic Curve Digital Signature Algorithm" (Thuật toán Chữ ký Số dựa trên Đường cong Elliptic). Đây là một thuật toán chữ ký số dựa trên mật mã học đường cong elliptic (ECC). Nó là một biến thể của DSA (Digital Signature Algorithm - Thuật toán Chữ ký Số). ECDSA sử dụng các tính chất của đường cong elliptic để cung cấp các mức độ bảo mật tương đương với những thuật toán khóa công khai truyền thống, như RSA, trong khi sử dụng kích thước khóa đáng kể nhỏ hơn. ECDSA cho phép tạo ra các cặp khóa (khóa công khai và khóa riêng tư) cũng như tạo và xác minh chữ ký số.

Trong bối cảnh của Bitcoin, ECDSA được sử dụng để tạo ra khóa công khai từ khóa riêng tư. Nó cũng được sử dụng để ký các giao dịch, nhằm thỏa mãn một script để mở khóa bitcoin và chi tiêu chúng. Đường cong elliptic được sử dụng trong ECDSA của Bitcoin là `secp256k1`, được định nghĩa bởi phương trình $y^2 = x^3 + 7$. Thuật toán này đã được sử dụng kể từ khi Bitcoin ra đời vào năm 2009. Ngày nay, nó chia sẻ vị trí của mình với giao thức Schnorr, một thuật toán chữ ký số khác được giới thiệu với Taproot vào năm 2021.