---
term: VẤN ĐỀ CÁC TƯỚNG BYZANTINE
---

Vấn đề này được Leslie Lamport, Robert Shostak và Marshall Pease đưa ra lần đầu trong tạp chí chuyên ngành *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["Vấn Đề Các Tướng Byzantine"](https://lamport.azurewebsites.net/pubs/byz.pdf) vào tháng 7 năm 1982. Ngày nay, nó được sử dụng để minh họa những thách thức về quyết định khi một hệ thống phân tán không thể tin tưởng bất kỳ bên nào.

Trong phép ẩn dụ này, một nhóm các tướng Byzantine và quân đội của họ đang cắm trại xung quanh một thành phố mà họ muốn tấn công hoặc bao vây. Các tướng được tách biệt về mặt địa lý và phải giao tiếp qua sứ giả để phối hợp chiến lược của họ. Việc họ tấn công hay rút lui không quan trọng, miễn là tất cả các tướng đạt được sự đồng thuận.

Do đó, chúng ta có thể xem xét các yêu cầu sau:
* Mỗi tướng phải đưa ra quyết định: tấn công hay rút lui (có hoặc không);
* Một khi quyết định được đưa ra, nó không thể thay đổi;
* Tất cả các tướng phải đồng ý với cùng một quyết định và thực hiện nó một cách đồng bộ.

Hơn nữa, một tướng chỉ có thể giao tiếp với tướng khác thông qua tin nhắn được truyền đi bởi một sứ giả, có thể bị trì hoãn, phá hủy, thay đổi hoặc mất. Và ngay cả khi một tin nhắn được giao thành công, một hoặc nhiều tướng có thể chọn (vì bất kỳ lý do gì) phản bội sự tin tưởng đã được thiết lập và gửi một tin nhắn gian lận, gieo rắc hỗn loạn.

Áp dụng điều này vào bối cảnh của blockchain Bitcoin, mỗi tướng đại diện cho một nút trong mạng, cần đạt được sự đồng thuận về trạng thái của hệ thống. Nói cách khác, đa số các bên tham gia trong một mạng phân tán phải đồng ý và thực hiện cùng một hành động để tránh thất bại hoàn toàn. Cách duy nhất để đạt được sự đồng thuận trong loại hệ thống phân tán này là phải có ít nhất 2/3 số nút mạng đáng tin cậy và trung thực. Do đó, nếu đa số mạng quyết định hành động một cách ác ý, hệ thống sẽ dễ bị tổn thương.

> ► *Dilemma này đôi khi còn được gọi là "Vấn Đề Phát Sóng Đáng Tin Cậy."*