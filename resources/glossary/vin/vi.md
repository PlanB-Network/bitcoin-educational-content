---
term: VIN
---

Một phần tử cụ thể của một giao dịch Bitcoin chỉ ra nguồn gốc của quỹ được sử dụng để thỏa mãn các đầu ra. Mỗi `vin` tham chiếu đến một đầu ra chưa được tiêu (UTXO) từ một giao dịch trước đó. Một giao dịch có thể chứa nhiều đầu vào, mỗi đầu vào được xác định bởi sự kết hợp của `txid` (mã định danh của giao dịch gốc) và `vout` (chỉ số của đầu ra trong giao dịch đó).

Mỗi `vin` bao gồm các thông tin sau:
* `txid`: mã định danh của giao dịch trước đó chứa đầu ra được sử dụng ở đây như một đầu vào;
* `vout`: chỉ số của đầu ra trong giao dịch trước đó;
* `scriptSig` hoặc `scriptWitness`: một kịch bản mở khóa cung cấp dữ liệu cần thiết để thỏa mãn các điều kiện đặt ra bởi `scriptPubKey` của giao dịch trước đó mà quỹ đang được tiêu, thường bằng cách cung cấp một chữ ký mật mã;
* `nSequence`: một trường cụ thể được sử dụng để chỉ ra cách đầu vào này được khóa thời gian, cũng như các tùy chọn khác như RBF.