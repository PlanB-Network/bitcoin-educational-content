---
term: TÌM ĐƯỜNG
---

Quy trình được một nút sử dụng để xác định đường dẫn tối ưu để định tuyến thanh toán qua mạng lưới kênh Lightning. Pathfinding được thực hiện bởi nút thanh toán, nút này phải chọn các nút trung gian phù hợp nhất để tiếp cận người nhận. Lựa chọn này dựa trên một số tiêu chí, chẳng hạn như phí, dung lượng kênh và khóa thời gian.


Thuật toán tìm đường xây dựng đồ thị về cấu trúc mạng từ dữ liệu tin đồn và đánh giá các tuyến đường có thể có giữa nút trả tiền và nút nhận tiền. Các tuyến đường này được xếp hạng từ tốt nhất đến tệ nhất theo nhiều tiêu chí khác nhau. Sau đó, nút sẽ kiểm tra các tuyến đường này cho đến khi thành công trong việc thanh toán trên một trong số chúng.