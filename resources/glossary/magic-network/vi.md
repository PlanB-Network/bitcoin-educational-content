---
term: MAGIC NETWORK
---

Các hằng số được sử dụng trong giao thức Bitcoin để xác định mạng cụ thể (mainnet, testnet, regtest...) của một thông điệp được trao đổi giữa các nút. Những giá trị này được ghi vào đầu mỗi thông điệp để giúp dễ dàng nhận diện chúng trong dòng dữ liệu. Magic Networks được thiết kế để hiếm khi xuất hiện trong dữ liệu giao tiếp thông thường. Thực tế, 4 byte này hiếm khi xuất hiện trong ASCII, không hợp lệ trong UTF-8, và tạo ra một số nguyên 32-bit rất lớn, bất kể định dạng lưu trữ dữ liệu. Các Magic Networks (định dạng little-endian) bao gồm:
* Mainnet:

```text
f9beb4d9
```

* Testnet:

```text
0b110907
```

* Regtest:

```text
fabfb5da
```

> ► *4 byte này đôi khi cũng được gọi là "Magic Number," "Magic Bytes," hoặc "Start String."*