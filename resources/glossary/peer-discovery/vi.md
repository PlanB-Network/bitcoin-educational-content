---
term: PEER DISCOVERY
---

Quá trình mà các nút trong mạng Bitcoin kết nối với các nút khác để thu thập thông tin. Khi một nút Bitcoin được khởi chạy lần đầu, nó không có thông tin về các nút khác trong mạng. Tuy nhiên, nó phải thiết lập kết nối để đồng bộ hóa với blockchain có lượng công việc tích lũy nhiều nhất. Một số cơ chế được sử dụng để khám phá các nút này, theo thứ tự ưu tiên:
* Nút bắt đầu bằng cách tham khảo tệp `peers.dat` của mình, lưu trữ thông tin về các nút mà nó đã tương tác trước đó. Nếu nút là mới, tệp này sẽ trống, và quá trình sẽ chuyển sang bước tiếp theo;
* Trong trường hợp không có thông tin trong tệp `peers.dat` (điều này là bình thường đối với một nút mới được khởi chạy), nút thực hiện truy vấn DNS tới các DNS seeds. Các máy chủ này cung cấp một danh sách địa chỉ IP của các nút được cho là đang hoạt động để thiết lập kết nối. Địa chỉ của các DNS seeds được mã hóa cứng trong mã của Bitcoin Core. Bước này thường đủ để hoàn thành việc khám phá các nút;
* Nếu các DNS seeds không phản hồi trong vòng 60 giây, nút có thể chuyển sang sử dụng các seed nodes. Đây là các nút Bitcoin công cộng được liệt kê trong một danh sách tĩnh gần một nghìn mục được tích hợp trực tiếp vào mã nguồn của Bitcoin Core. Nút mới sẽ sử dụng danh sách này để thiết lập kết nối đầu tiên với mạng và thu thập địa chỉ IP của các nút khác;
* Trong trường hợp cực kỳ hiếm gặp khi tất cả các phương pháp trước đó thất bại, người vận hành nút luôn có lựa chọn thêm thủ công địa chỉ IP của các nút để thiết lập kết nối đầu tiên.