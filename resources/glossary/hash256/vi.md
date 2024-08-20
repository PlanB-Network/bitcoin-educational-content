---
term: HASH256
---

Hàm mật mã được sử dụng cho nhiều ứng dụng trên Bitcoin. Nó bao gồm việc áp dụng hàm SHA256 hai lần lên dữ liệu đầu vào. Thông điệp được truyền qua SHA256 một lần, và kết quả của thao tác này được sử dụng làm dữ liệu đầu vào cho một lần truyền qua SHA256 thứ hai. Do đó, đầu ra của hàm này là 256 bit.

$$\text{HASH256}(x) = \text{SHA256}(\text{SHA256}(x))$$