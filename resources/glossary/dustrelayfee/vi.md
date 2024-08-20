---
term: DUSTRELAYFEE
---

Quy tắc chuẩn hóa được sử dụng bởi các nút mạng để xác định họ coi giới hạn "bụi" là bao nhiêu. Tham số này thiết lập một mức phí theo sats cho mỗi kilobyte ảo (sats/kvB) phục vụ như một tham chiếu để tính toán nếu giá trị của một UTXO nhỏ hơn phí cần thiết để bao gồm nó trong một giao dịch. Thực tế, một UTXO được coi là "bụi" trên Bitcoin nếu nó yêu cầu nhiều phí hơn so với giá trị mà nó đại diện để được chuyển giao. Cách tính giới hạn này như sau:

```text
limit = (kích thước đầu vào + kích thước đầu ra) * tỷ lệ phí
```

Vì tỷ lệ phí cần thiết cho một giao dịch để được bao gồm trong một khối Bitcoin liên tục thay đổi, tham số `DustRelayFee` cho phép mỗi nút xác định tỷ lệ phí được sử dụng trong tính toán này. Theo mặc định, trên Bitcoin Core, giá trị này được thiết lập là 3,000 sats/kvB. Ví dụ, để tính giới hạn bụi cho một đầu vào và đầu ra P2PKH, có kích thước lần lượt là 148 và 34 byte, phép tính sẽ là:

```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```

Điều này có nghĩa là nút đó sẽ không chuyển tiếp các giao dịch bao gồm một UTXO được bảo vệ bởi P2PKH có giá trị nhỏ hơn 546 sats.