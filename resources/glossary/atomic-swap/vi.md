---
term: ATOMIC SWAP
---

Công nghệ cho phép trao đổi trực tiếp các loại tiền mã hóa giữa hai bên, mà không cần sự tin tưởng và không yêu cầu một trung gian. Những giao dịch này được gọi là "nguyên tử" vì chúng chỉ có thể dẫn đến hai kết quả:
* Hoặc là giao dịch thành công, và cả hai bên đều đã trao đổi tiền mã hóa của mình một cách hiệu quả;
* Hoặc giao dịch thất bại, và cả hai bên đều giữ lại tiền mã hóa ban đầu của mình.

Atomic Swaps có thể được thực hiện với cùng một loại tiền mã hóa, trong trường hợp đó nó còn được gọi là "*coinswap*," hoặc giữa các loại tiền mã hóa khác nhau. Về mặt lịch sử, chúng dựa vào "Hợp Đồng Khóa Thời Gian Băm" (Hash Time-Locked Contracts - HTLC), một hệ thống khóa thời gian đảm bảo việc hoàn thành hoặc hủy bỏ hoàn toàn giao dịch, từ đó bảo toàn tính toàn vẹn của quỹ của các bên liên quan. Phương pháp này yêu cầu các giao thức có khả năng xử lý cả kịch bản và khóa thời gian. Tuy nhiên, trong những năm gần đây, xu hướng đã chuyển sang sử dụng *Chữ Ký Điều Chỉnh*. Phương pháp thứ hai này có lợi thế là loại bỏ nhu cầu về kịch bản, từ đó giảm chi phí vận hành. Lợi ích lớn khác của nó là không yêu cầu sử dụng băm giống nhau cho cả hai phần của giao dịch, giúp tránh lộ liên kết giữa chúng.