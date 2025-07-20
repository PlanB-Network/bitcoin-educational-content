---
term: ERLAY
---

Giao thức mạng được đề xuất để cải thiện hiệu quả chuyển tiếp các giao dịch chưa được xác nhận giữa các nút Bitcoin.


Hiện tại, mỗi giao dịch được truyền qua một hệ thống trong đó mỗi nút phát sóng giao dịch mà nó biết đến tất cả các nút ngang hàng của nó. Vấn đề là điều này dẫn đến rất nhiều sự dư thừa và sử dụng băng thông cho các bản sao. Nhiều giao dịch phát sóng là không cần thiết, vì người nhận đã biết về các giao dịch này và mỗi nút chỉ cần biết về mỗi giao dịch một lần. Erlay đề xuất giới hạn theo mặc định là 8 số lượng các nút ngang hàng mà một nút trực tiếp gửi các giao dịch mà nó biết đến, sau đó sử dụng quy trình đối chiếu dựa trên thư viện minisketch để chia sẻ các giao dịch bị thiếu hiệu quả hơn.


Erlay sẽ giảm mức tiêu thụ băng thông khoảng 40%, giúp hoạt động của Full node dễ tiếp cận hơn với người dùng có kết nối Internet hạn chế và do đó thúc đẩy phân cấp mạng tốt hơn. Giao thức này cũng sẽ duy trì mức tiêu thụ băng thông gần như không đổi khi số lượng kết nối tăng lên. Điều này có nghĩa là các nhà điều hành nút sẽ dễ dàng hơn nhiều khi chấp nhận một số lượng lớn kết nối từ các đối tác của họ, điều này sẽ tăng cường tính bảo mật của mạng Bitcoin bằng cách giảm nguy cơ phân vùng, dù là cố ý hay vô tình. Ngoài ra, Erlay sẽ khiến việc xác định nút gốc của giao dịch trở nên khó khăn hơn, do đó tăng tính bảo mật cho người dùng các nút không hoạt động theo Tor.


Erlay được đề xuất trong BIP330.