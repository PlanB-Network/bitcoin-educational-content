---
term: HASH160
---

Hàm mã hóa được sử dụng trong Bitcoin, đặc biệt là để tạo ra địa chỉ nhận Legacy và SegWit v0. Nó kết hợp hai hàm băm được thực hiện liên tiếp trên đầu vào: đầu tiên là SHA256, sau đó là RIPEMD160. Do đó, đầu ra của hàm này là 160 bit.

$$\text{HASH160}(x) = \text{RIPEMD160}(\text{SHA256}(x))$$