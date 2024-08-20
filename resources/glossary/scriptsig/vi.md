---
term: SCRIPTSIG
---

Một phần tử trong giao dịch Bitcoin nằm ở đầu vào. `scriptSig` cung cấp dữ liệu cần thiết để thỏa mãn các điều kiện được đặt ra bởi `scriptPubKey` của giao dịch trước đó từ đó tiền được chi tiêu. Do đó, nó đóng vai trò bổ sung cho `scriptPubKey`. Thông thường, `scriptSig` chứa một chữ ký số và một khóa công khai. Chữ ký được tạo ra bởi chủ sở hữu của bitcoin sử dụng khóa riêng của họ và chứng minh rằng họ có quyền chi tiêu UTXO. Trong trường hợp này, `scriptSig` chứng minh rằng người giữ đầu vào sở hữu khóa riêng tương ứng với khóa công khai liên kết với địa chỉ được chỉ định trong `scriptPubKey` của giao dịch đi ra trước đó.

Khi giao dịch được xác minh, dữ liệu từ `scriptSig` được thực thi trong `scriptPubKey` tương ứng. Nếu kết quả hợp lệ, điều này có nghĩa là các điều kiện để chi tiêu tiền đã được đáp ứng. Nếu tất cả các đầu vào của giao dịch cung cấp một `scriptSig` xác thực `scriptPubKey` của chúng, giao dịch là hợp lệ và có thể được thêm vào một khối để thực thi.

Ví dụ, đây là một `scriptSig` P2PKH cổ điển:

```text
<signature> <public key>
```

`scriptPubKey` tương ứng sẽ là:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```

![](../../dictionnaire/assets/35.png)

> ► *`scriptSig` cũng đôi khi được gọi là "unlocking script" trong tiếng Anh.*