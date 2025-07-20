---
term: THANH TOÁN ĐA ĐƯỜNG (MPP)
---

Thuật ngữ chung cho tất cả các kỹ thuật thanh toán trên Lightning cho phép chia nhỏ giao dịch thành nhiều phần nhỏ hơn và định tuyến qua các tuyến đường khác nhau. Nói cách khác, mỗi phần thanh toán sẽ đi qua một đường dẫn nút khác nhau. Điều này giúp có thể bỏ qua các giới hạn thanh khoản trên một kênh duy nhất trong tuyến đường.


Thanh toán đa đường cũng mang lại một số lợi thế nhỏ về mặt bảo mật, vì người quan sát sẽ khó liên kết từng đoạn thanh toán với toàn bộ giao dịch hơn. Tuy nhiên, trong phiên bản cơ bản, tất cả các đoạn đều chia sẻ cùng một bí mật cho HTLC, điều này có thể khiến giao dịch có thể truy xuất được nếu người quan sát có mặt trên nhiều tuyến. Hơn nữa, vì bí mật là duy nhất cho tất cả các phần của thanh toán, nên nó không phải là nguyên tử. Điều này có nghĩa là một số phần của thanh toán có thể được thực hiện thành công, trong khi những phần khác có thể không thành công. Những nhược điểm này được khắc phục bằng "Thanh toán đa đường nguyên tử".