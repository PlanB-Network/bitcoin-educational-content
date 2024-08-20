---
term: INITIAL BLOCK DOWNLOAD (IBD)
---

Đề cập đến quá trình mà một nút (node) tải xuống và xác minh blockchain từ khối Genesis, và đồng bộ hóa với các nút khác trong mạng Bitcoin. IBD phải được thực hiện khi khởi chạy một full node mới. Tại thời điểm bắt đầu quá trình đồng bộ hóa ban đầu này, nút không có thông tin về các giao dịch trước đó. Do đó, nó tải xuống từng khối từ các nút khác trong mạng, xác minh tính hợp lệ của nó, và sau đó thêm nó vào phiên bản blockchain địa phương của mình. Đáng chú ý là IBD có thể mất nhiều thời gian và tốn nhiều tài nguyên do kích thước của blockchain và bộ UTXO ngày càng tăng. Tốc độ thực hiện của nó phụ thuộc vào khả năng tính toán của máy tính chủ nút, dung lượng RAM, tốc độ của thiết bị lưu trữ, và băng thông. Để bạn có một ý tưởng, nếu bạn có một kết nối internet mạnh mẽ, và nút được chủ trì trên MacBook mới nhất với nhiều RAM, IBD chỉ mất vài giờ. Ngược lại, nếu bạn sử dụng một microcomputer như Raspberry Pi, IBD có thể mất một tuần hoặc hơn.

> ► *Trong tiếng Pháp, người ta thường chấp nhận trực tiếp tham chiếu đến một IBD. Bản dịch đôi khi được sử dụng là "synchronisation initiale", hoặc "téléchargement initial des blocs".*