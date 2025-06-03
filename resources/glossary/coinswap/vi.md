---
term: TRAO ĐỔI TIỀN
---

Giao thức chuyển giao bí mật Ownership giữa những người dùng. Phương pháp này nhằm mục đích chuyển giao quyền sở hữu bitcoin từ người này sang người khác và ngược lại, mà không cần Exchange này phải hiển thị rõ ràng trên Blockchain. Coinwap sử dụng hợp đồng thông minh để thực hiện chuyển giao mà không cần sự tin tưởng giữa các bên.


Hãy tưởng tượng một ví dụ ngây thơ (không hiệu quả) với Alice và Bob. Alice giữ 1 BTC được bảo mật bằng khóa riêng $A$ và Bob cũng giữ 1 BTC được bảo mật bằng khóa riêng $B$. Về mặt lý thuyết, họ có thể Exchange khóa riêng của mình thông qua kênh truyền thông bên ngoài để thực hiện chuyển khoản bí mật. Tuy nhiên, phương pháp ngây thơ này có rủi ro cao về mặt tin cậy. Không có gì ngăn cản Alice giữ một bản sao của khóa riêng $A$ sau Exchange và sử dụng nó sau này để đánh cắp bitcoin, một khi khóa đã nằm trong tay Bob. Hơn nữa, không có gì đảm bảo rằng Alice sẽ không nhận được khóa riêng $B$ của Bob và không bao giờ chuyển khóa riêng $A$ của cô ấy trong Exchange. Do đó, Exchange này dựa vào sự tin tưởng quá mức giữa các bên và không hiệu quả trong việc đảm bảo chuyển khoản Ownership an toàn, bí mật.


Để giải quyết những vấn đề này và cho phép trao đổi tiền xu giữa các bên không tin tưởng lẫn nhau, chúng ta sẽ sử dụng hệ thống Smart contract khiến Exchange trở nên "nguyên tử". Chúng có thể là HTLC (*Hash Time-Locked Contracts*) hoặc PTLC (*Point Time-Locked Contracts*). Hai giao thức này hoạt động theo cách tương tự nhau, sử dụng hệ thống khóa thời gian đảm bảo rằng Exchange được hoàn thành thành công hoặc bị hủy hoàn toàn, do đó bảo vệ tính toàn vẹn của tiền của cả hai bên. Sự khác biệt chính giữa HTLC và PTLC là HTLC sử dụng hàm băm và ảnh trước để bảo mật giao dịch, trong khi PTLC sử dụng Chữ ký bộ điều hợp.


Trong kịch bản trao đổi tiền xu sử dụng HTLC hoặc PTLC giữa Alice và Bob, Exchange diễn ra theo cách an toàn: hoặc thành công và mỗi bên nhận được BTC của bên kia, hoặc thất bại và mỗi bên giữ BTC của riêng mình. Điều này khiến không bên nào có thể gian lận hoặc đánh cắp BTC của bên kia.


Việc sử dụng Adaptor Signatures đặc biệt thú vị trong bối cảnh này, vì nó giúp loại bỏ các tập lệnh truyền thống (một cơ chế đôi khi được gọi là "_scriptless scripts_"). Điều này làm giảm chi phí liên quan đến Exchange. Một lợi thế lớn khác của Adaptor Signatures là chúng không yêu cầu sử dụng Hash chung cho cả hai bên tham gia giao dịch, do đó tránh được nhu cầu tiết lộ liên kết trực tiếp giữa chúng trong một số loại Exchange.