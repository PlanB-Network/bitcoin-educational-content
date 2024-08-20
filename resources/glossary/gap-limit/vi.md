---
term: GAP LIMIT
---

Một tham số được sử dụng trong phần mềm ví Bitcoin để xác định số lượng địa chỉ không sử dụng liên tiếp tối đa được tạo ra trước khi dừng việc tìm kiếm các giao dịch bổ sung. Việc điều chỉnh tham số này thường là cần thiết khi khôi phục một ví để đảm bảo rằng tất cả các giao dịch được tìm thấy. Một Giới hạn Gap không đủ có thể dẫn đến việc bỏ sót một số giao dịch nếu các địa chỉ bị bỏ qua trong các giai đoạn phái sinh. Tăng Giới hạn Gap cho phép ví tìm kiếm xa hơn trong chuỗi địa chỉ, nhằm khôi phục tất cả các giao dịch liên quan.

Thực tế, một `xpub` đơn lẻ có thể lý thuyết phái sinh hơn 4 tỷ địa chỉ nhận (bao gồm cả địa chỉ nội bộ và địa chỉ bên ngoài). Tuy nhiên, phần mềm ví không thể phái sinh và kiểm tra tất cả chúng để xác định việc sử dụng mà không gặp phải chi phí hoạt động khổng lồ. Do đó, chúng tiến hành theo thứ tự chỉ mục, vì đây thường là thứ tự mà tất cả phần mềm ví tạo ra địa chỉ. Phần mềm ghi lại mỗi địa chỉ được sử dụng trước khi chuyển sang cái tiếp theo, và nó dừng tìm kiếm khi gặp một số lượng địa chỉ trống liên tiếp. Số lượng này chính là cái được gọi là Giới hạn Gap.

Nếu, ví dụ, Giới hạn Gap được thiết lập là `20`, và địa chỉ `m/84'/0'/0'/0/15/` trống, ví sẽ phái sinh địa chỉ đến `m/84'/0'/0'/0/34/`. Nếu phạm vi địa chỉ này vẫn không được sử dụng, việc tìm kiếm sẽ dừng lại ở đó. Do đó, một giao dịch sử dụng địa chỉ `m/84'/0'/0'/0/40/` sẽ không được phát hiện trong ví dụ này.