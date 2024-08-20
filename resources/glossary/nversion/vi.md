---
term: NVERSION
---

Trường `nVersion` trong một giao dịch Bitcoin được sử dụng để chỉ định phiên bản của định dạng giao dịch đang được sử dụng. Nó cho phép mạng lưới phân biệt giữa các phiên bản khác nhau của định dạng giao dịch theo thời gian và áp dụng các quy tắc tương ứng. Trường này không ảnh hưởng đến các quy tắc đồng thuận. Điều này có nghĩa là bất kỳ giá trị nào được gán cho trường này không dẫn đến việc giao dịch bị vô hiệu hóa. Tuy nhiên, trường `nVersion` có các quy tắc chuẩn hóa mà hiện tại chỉ chấp nhận các giá trị `1` và `2`. Cho đến nay, trường này chỉ hữu ích cho việc kích hoạt trường `nSequence`.