---
term: TXID (TRANSACTION IDENTIFIER)
---

Một định danh duy nhất liên kết với mỗi giao dịch Bitcoin. Nó được tạo ra bằng cách tính toán băm `SHA256d` của dữ liệu giao dịch. TXID phục vụ như một tham chiếu để tìm kiếm một giao dịch cụ thể trong blockchain. Nó cũng được sử dụng để tham chiếu đến một UTXO, về cơ bản là sự kết hợp của TXID của giao dịch trước đó và chỉ số của đầu ra được chỉ định (còn được gọi là "vout"). Đối với các giao dịch sau SegWit, TXID không còn tính đến chứng từ giao dịch, điều này loại bỏ tính biến đổi.