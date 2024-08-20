---
term: OP_2 ĐẾN OP_16 (0X52 ĐẾN 0X60)
---

Các mã vận hành từ `OP_2` đến `OP_16` đẩy các giá trị số tương ứng từ 2 đến 16 vào ngăn xếp. Chúng được sử dụng để đơn giản hóa các kịch bản bằng cách cho phép chèn các giá trị số nhỏ. Loại mã vận hành này thường được sử dụng trong các kịch bản đa chữ ký. Dưới đây là một ví dụ về `scriptPubKey` cho một đa chữ ký 2/3:

```text
OP_2
<Public Key A>
<Public Key B>
<Public Key C>
OP_3
OP_CHECKMULTISIG
```

> ► *Tất cả các mã vận hành này đôi khi cũng được gọi là OP_PUSHNUM_N.*