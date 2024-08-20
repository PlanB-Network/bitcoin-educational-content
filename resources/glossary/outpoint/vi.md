---
term: OUTPOINT
---

Một tham chiếu duy nhất đến một đầu ra giao dịch chưa được tiêu (UTXO). Nó bao gồm hai yếu tố:
* `txid`: mã định danh của giao dịch đã tạo ra đầu ra;
* `vout`: chỉ số của đầu ra trong giao dịch.

Sự kết hợp của hai yếu tố này xác định chính xác một UTXO. Ví dụ, nếu một giao dịch có `txid` là `abc...123` và chỉ số đầu ra là `0`, outpoint sẽ được ghi như sau:

```text
abc...123:0
```

Outpoint được sử dụng trong các đầu vào (`vin`) của một giao dịch mới để chỉ ra UTXO nào đang được tiêu.

> ► *Thuật ngữ "outpoint" thường được sử dụng đồng nghĩa với "UTXO."*