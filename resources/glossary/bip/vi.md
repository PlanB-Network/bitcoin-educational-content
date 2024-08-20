---
term: BIP
---

Viết tắt của "Bitcoin Improvement Proposal" (Đề xuất Cải tiến Bitcoin). Một Đề xuất Cải tiến Bitcoin (BIP) là một quy trình chính thức để đề xuất và ghi chép các cải tiến và thay đổi đối với giao thức Bitcoin và các tiêu chuẩn của nó. Do Bitcoin không có một thực thể trung ương nào quyết định các cập nhật, BIP cho phép cộng đồng đề xuất, thảo luận và thực hiện cải tiến một cách có cấu trúc và minh bạch. Mỗi BIP chi tiết mục tiêu của cải tiến đề xuất, lý do biện hộ, tác động tiềm năng đối với khả năng tương thích, cũng như các ưu và nhược điểm. BIP có thể được viết bởi bất kỳ thành viên nào của cộng đồng, nhưng phải được các nhà phát triển khác và các biên tập viên, những người duy trì cơ sở dữ liệu GitHub của Bitcoin Core chấp thuận: Bryan Bishop, Jon Atack, Luke Dashjr, Mark Erhardt (Murch), Olaoluwa Osuntokun và Ruben Somsen. Tuy nhiên, quan trọng là phải hiểu rằng vai trò của những cá nhân này trong việc chỉnh sửa BIP không có nghĩa là họ kiểm soát Bitcoin. Nếu ai đó đề xuất một cải tiến không được chấp nhận trong khuôn khổ BIP chính thức, họ vẫn có thể trình bày trực tiếp cho cộng đồng Bitcoin hoặc thậm chí tạo ra một nhánh bao gồm sửa đổi của mình. Lợi ích của quy trình BIP nằm ở tính chính thức và tập trung của nó, giúp thúc đẩy cuộc tranh luận để tránh sự chia rẽ giữa người dùng Bitcoin, tìm cách thực hiện cập nhật một cách đồng thuận. Cuối cùng, nguyên tắc đa số kinh tế quyết định động lực quyền lực trong giao thức.

BIP được phân loại thành ba danh mục chính:
* *Standards Track BIPs*: Liên quan đến các sửa đổi ảnh hưởng trực tiếp đến các triển khai Bitcoin, như quy tắc xác thực giao dịch và khối;
* *Informational BIPs*: Cung cấp thông tin hoặc khuyến nghị mà không đề xuất thay đổi trực tiếp đối với giao thức;
* *Process BIPs*: Mô tả các thay đổi trong các quy trình xung quanh Bitcoin, như quy trình quản trị.

Standards Track và Informational BIPs cũng được phân loại theo "Layer":
* *Consensus Layer*: BIPs ở lớp này liên quan đến các quy tắc đồng thuận của Bitcoin, như sửa đổi quy tắc xác thực khối hoặc giao dịch. Những đề xuất này có thể là soft forks (sửa đổi tương thích ngược) hoặc hard forks (sửa đổi không tương thích ngược). Ví dụ, các BIP cho SegWit và Taproot thuộc về danh mục này;
* *Peer Services*: Lớp này liên quan đến hoạt động của mạng nút Bitcoin, tức là cách các nút tìm và giao tiếp với nhau trên Internet.
* *API/RPC*: Các BIP của lớp này liên quan đến các Giao diện Lập trình Ứng dụng (API) và Cuộc gọi Thủ tục từ xa (RPC) cho phép phần mềm Bitcoin tương tác với các nút;
* *Applications Layer*: Lớp này liên quan đến các ứng dụng được xây dựng trên nền tảng Bitcoin. Các BIP trong danh mục này thường xử lý các sửa đổi ở cấp độ tiêu chuẩn ví Bitcoin.

Quy trình nộp một BIP bắt đầu với việc khái niệm hóa và thảo luận ý tưởng trên danh sách gửi thư *Bitcoin-dev*. Nếu ý tưởng có triển vọng, tác giả soạn thảo một BIP theo một định dạng cụ thể và nộp nó qua một Pull Request trên kho lưu trữ Core GitHub. Các biên tập viên xem xét đề xuất này để xác minh rằng nó đáp ứng tất cả các tiêu chí. BIP phải khả thi về mặt kỹ thuật, có lợi cho giao thức, tuân thủ định dạng yêu cầu và phù hợp với triết lý của Bitcoin. Nếu BIP đáp ứng những điều kiện này, nó chính thức được tích hợp vào kho lưu trữ GitHub của BIPs. Sau đó, nó được gán một số. Số này thường được quyết định bởi biên tập viên, thường là Luke Dashjr, và được gán một cách có lý lẽ: BIPs xử lý các chủ đề tương tự thường nhận được các số liên tiếp.

BIPs sau đó trải qua các trạng thái khác nhau trong suốt vòng đời của chúng. Trạng thái hiện tại được chỉ định trong tiêu đề của mỗi BIP:
* Draft: Đề xuất vẫn đang trong giai đoạn soạn thảo và thảo luận;
* Đề xuất: BIP được coi là hoàn chỉnh và sẵn sàng để được cộng đồng xem xét;
* Hoãn lại: BIP được tạm hoãn cho đến sau này bởi người đề xuất hoặc một biên tập viên;
* Từ chối: Một BIP được phân loại là từ chối nếu nó không có hoạt động nào trong 3 năm. Tác giả của nó có thể chọn để tiếp tục sau này, điều này sẽ cho phép nó quay trở lại trạng thái bản thảo;
* Rút lại: BIP đã được tác giả rút lại;
* Cuối cùng: BIP được chấp nhận và được triển khai rộng rãi trên Bitcoin;
* Hoạt động: Chỉ dành cho các BIP về quy trình, trạng thái này được gán khi một sự đồng thuận nhất định được đạt tới;
* Đã thay thế / Lỗi thời: BIP không còn áp dụng hoặc đã được thay thế bởi một đề xuất mới hơn làm cho nó trở nên không cần thiết.

> ► *BIP là từ viết tắt của "Bitcoin Improvement Proposal". Trong tiếng Pháp, nó có thể được dịch là "Proposition d'amélioration de Bitcoin". Tuy nhiên, hầu hết các văn bản tiếng Pháp trực tiếp sử dụng từ viết tắt "BIP" như một danh từ chung, đôi khi là nữ, đôi khi là nam.*