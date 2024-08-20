---
term: UTXO SET
---

Ám chỉ tập hợp tất cả các UTXO hiện có tại bất kỳ thời điểm nào. Nói cách khác, đây là một danh sách lớn gồm tất cả các phần khác nhau của bitcoin đang chờ được chi tiêu. Nếu bạn cộng dồn số lượng của tất cả các UTXO trong tập UTXO, bạn sẽ nhận được tổng khối lượng tiền tệ của bitcoin đang lưu thông. Mỗi nút trong mạng Bitcoin duy trì bộ UTXO của riêng mình theo thời gian thực. Nó được cập nhật khi các khối mới hợp lệ được xác nhận, với các giao dịch mà chúng bao gồm, tiêu thụ một số UTXO từ tập UTXO và tạo ra những cái mới để đáp lại.

Bộ UTXO này được mỗi nút giữ lại để nhanh chóng xác minh xem các UTXO được chi tiêu trong giao dịch có thực sự hợp lệ hay không. Điều này cho phép họ phát hiện và từ chối các nỗ lực chi tiêu gấp đôi. Bộ UTXO thường là trung tâm của những lo ngại về sự phân cấp của Bitcoin, vì kích thước của nó tự nhiên tăng lên rất nhanh. Vì một phần của nó phải được giữ trong RAM để xác minh giao dịch trong một khoảng thời gian hợp lý, bộ UTXO có thể dần dần làm cho việc vận hành một nút đầy đủ trở nên quá tốn kém. Bộ UTXO cũng có ảnh hưởng đáng kể đến IBD (*Initial Block Download*). Càng nhiều bộ UTXO có thể được đặt trong RAM, quá trình IBD càng nhanh. Trên Bitcoin Core, bộ UTXO được lưu trữ trong thư mục có tên `/chainstate`.

> ► *Trong tiếng Anh, "UTXO set" có thể được dịch là "bộ UTXO".*