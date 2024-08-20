---
term: P2SH
---

P2SH là viết tắt của *Pay to Script Hash*. Đây là một mô hình script chuẩn được sử dụng để thiết lập các điều kiện chi tiêu cho một UTXO. Khác với các script P2PK và P2PKH, nơi các điều kiện chi tiêu được định sẵn, P2SH cho phép tích hợp các điều kiện chi tiêu tùy ý và các chức năng bổ sung trong một script giao dịch.

Về mặt kỹ thuật, trong một giao dịch P2SH, `scriptPubKey` chứa hash mật mã của một `redeemScript`, thay vì các điều kiện chi tiêu cụ thể. Hash này được thu được bằng cách sử dụng hash `SHA256`. Khi gửi bitcoin đến một địa chỉ P2SH, `redeemScript` cơ bản không được tiết lộ. Chỉ có hash của nó được bao gồm trong giao dịch. Địa chỉ P2SH được mã hóa trong `Base58Check` và bắt đầu với số `3`. Khi người nhận muốn chi tiêu bitcoin đã nhận, họ phải cung cấp một `redeemScript` phù hợp với hash có trong `scriptPubKey`, cùng với dữ liệu cần thiết để thỏa mãn các điều kiện của `redeemScript` này. Ví dụ, trong một script đa chữ ký P2SH, script có thể yêu cầu chữ ký từ nhiều khóa riêng.

Việc sử dụng P2SH mang lại nhiều linh hoạt hơn, vì nó cho phép xây dựng các script tùy ý mà không cần người gửi biết chi tiết. P2SH được giới thiệu vào năm 2012 với BIP16.