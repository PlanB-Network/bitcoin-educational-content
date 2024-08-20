---
term: SCRIPTPUBKEY
---

Một script nằm trong phần output của một giao dịch Bitcoin, định nghĩa các điều kiện mà UTXO liên quan có thể được chi tiêu. Script này do đó bảo vệ bitcoin. Trong hình thức phổ biến nhất, `scriptPubKey` chứa một điều kiện yêu cầu giao dịch tiếp theo phải cung cấp bằng chứng về việc sở hữu khóa riêng tương ứng với địa chỉ Bitcoin được chỉ định. Điều này thường được thực hiện bởi một script yêu cầu chữ ký tương ứng với khóa công khai liên kết với địa chỉ được sử dụng để bảo vệ số tiền này. Khi một giao dịch cố gắng sử dụng UTXO này làm input, nó phải cung cấp một `scriptSig` mà, khi kết hợp với `scriptPubKey`, đáp ứng các điều kiện đã đặt và tạo ra một script hợp lệ.

Ví dụ, đây là một `scriptPubKey` P2PKH cổ điển:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <địa chỉ> OP_EQUALVERIFY OP_CHECKSIG
```

`scriptSig` tương ứng sẽ là:

```text
<chữ ký> <khóa công khai>
```

![](../../dictionnaire/assets/35.png)

> ► *Script này đôi khi cũng được gọi là "locking script" trong tiếng Anh.*