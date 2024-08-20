---
term: SEED NODES
---

Danh sách cố định các nút Bitcoin công cộng, được tích hợp trực tiếp vào mã nguồn của Bitcoin Core (`bitcoin/src/chainparamsseeds.h`). Danh sách này đóng vai trò như các điểm kết nối cho các nút Bitcoin mới khi tham gia vào mạng lưới, nhưng chỉ được sử dụng nếu các DNS seeds không cung cấp phản hồi trong vòng 60 giây kể từ khi yêu cầu được gửi đi. Trong trường hợp này, nút Bitcoin mới sẽ kết nối với các seed nodes để thiết lập kết nối đầu tiên với mạng lưới và yêu cầu địa chỉ IP của các nút khác. Mục tiêu cuối cùng là thu thập thông tin cần thiết để thực hiện Initial Block Download (IBD) và đồng bộ hóa với chuỗi có lượng công việc tích lũy nhiều nhất. Danh sách các seed nodes bao gồm gần 1000 nút, được xác định theo tiêu chuẩn do BIP155 thiết lập. Do đó, seed nodes đại diện cho phương thức thứ ba để kết nối với mạng lưới cho một nút Bitcoin, sau khả năng sử dụng tệp `peers.dat`, được chính nút tạo ra, và việc yêu cầu thông tin từ DNS seeds.

> ► *Lưu ý, seed nodes không nên bị nhầm lẫn với "DNS seeds," là phương thức thứ hai để thiết lập các kết nối.*