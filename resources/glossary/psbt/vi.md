---
term: PSBT
---

Viết tắt của "Partially Signed Bitcoin Transaction" (Giao dịch Bitcoin được ký một phần). Đây là một quy chuẩn được giới thiệu với BIP174 nhằm chuẩn hóa cách thức mà các giao dịch chưa hoàn thành được xây dựng trong phần mềm liên quan đến Bitcoin, như phần mềm ví. Một PSBT bao gồm một giao dịch mà các input có thể chưa được ký hoàn toàn. Nó bao gồm tất cả thông tin cần thiết cho một người tham gia để ký giao dịch mà không cần thông tin bổ sung. Do đó, một PSBT có thể có 3 hình thức khác nhau:
* Một giao dịch được xây dựng hoàn chỉnh, nhưng chưa được ký;
* Một giao dịch được ký một phần, nơi một số input đã được ký trong khi những input khác chưa;
* Hoặc một giao dịch Bitcoin đã được ký hoàn toàn, có thể được chuyển đổi để sẵn sàng phát sóng trên mạng.

Định dạng PSBT tạo điều kiện cho sự tương tác giữa các phần mềm ví và thiết bị ký số (ví cứng) khác nhau. Hiện tại, phiên bản 0 của PSBT được sử dụng, như được định nghĩa trong BIP174, nhưng phiên bản 2 đang được đề xuất thông qua BIP370.

> ► *Phiên bản 1 của PSBT không tồn tại. Vì phiên bản 0 là phiên bản đầu tiên, phiên bản thứ hai đã được gọi một cách không chính thức là phiên bản 2. Ava Chow, người đã viết BIP370, do đó đã quyết định gán số 2 cho phiên bản mới này để tránh nhầm lẫn.*