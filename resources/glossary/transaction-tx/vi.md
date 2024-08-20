---
term: GIAO DỊCH (TX)
---

Trong bối cảnh của Bitcoin, một giao dịch (viết tắt là "TX") là một hoạt động được ghi lại trên blockchain, chuyển quyền sở hữu của bitcoins từ một hoặc nhiều đầu vào (inputs) sang một hoặc nhiều đầu ra (outputs). Mỗi giao dịch sử dụng Đầu Ra Giao Dịch Chưa Tiêu (UTXOs) làm đầu vào, đây là các đầu ra từ các giao dịch trước đó, và tạo ra UTXOs mới làm đầu ra, có thể được sử dụng làm đầu vào trong các giao dịch tương lai.

Mỗi đầu vào bao gồm một tham chiếu đến một đầu ra hiện có cùng với một kịch bản chữ ký (`scriptSig`) thỏa mãn điều kiện chi tiêu (`scriptPubKey`) được thiết lập bởi đầu ra mà nó tham chiếu. Đây là cách mà bitcoins được mở khóa. Các đầu ra định nghĩa điều kiện chi tiêu mới (`scriptPubKey`) cho bitcoins được chuyển giao, thường dưới dạng một khóa công khai hoặc một địa chỉ mà bitcoins giờ đây được liên kết.