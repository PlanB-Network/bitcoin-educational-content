---
term: VOUT
---

Một phần tử cụ thể của một giao dịch Bitcoin quy định điểm đến của số tiền được gửi. Một giao dịch có thể bao gồm nhiều đầu ra, mỗi đầu ra được xác định duy nhất bởi sự kết hợp của mã định danh giao dịch (`txid`) và một chỉ số gọi là `vout`. Chỉ số này, bắt đầu từ `0`, đánh dấu vị trí của đầu ra trong chuỗi các đầu ra của giao dịch. Do đó, đầu ra đầu tiên sẽ được chỉ định bởi `"vout": 0`, đầu ra thứ hai bởi `"vout": 1`, và cứ thế tiếp tục.

Mỗi `vout` chủ yếu bao gồm hai phần thông tin:
* giá trị, được biểu thị bằng bitcoin, đại diện cho số lượng tiền được gửi;
* một kịch bản khóa (`scriptPubKey`) quy định các điều kiện cần thiết để số tiền có thể được chi tiêu lại trong một giao dịch tương lai.

Sự kết hợp của `txid` và `vout` của một phần tử cụ thể tạo thành cái gọi là UTXO, ví dụ:

```text
txid: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf
vout: 0
outpoint: 4c160086e39a940c2459f03bb7cfe5b768fc78373c9960dc2cf2fa61b57d0adf:0
```