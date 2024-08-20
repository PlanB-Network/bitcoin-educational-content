---
term: RECURSIVE (COVENANT)
---

Một covenant đệ quy trên Bitcoin là một loại hợp đồng thông minh áp đặt các điều kiện không chỉ cho giao dịch hiện tại mà còn cho các giao dịch tương lai sử dụng các đầu ra của giao dịch này. Điều này cho phép tạo ra chuỗi giao dịch, trong đó mỗi giao dịch phải tuân theo một số quy tắc được định nghĩa bởi giao dịch đầu tiên trong chuỗi. Tính đệ quy tạo ra một chuỗi các giao dịch, trong đó mỗi giao dịch kế thừa các hạn chế từ giao dịch mẹ của nó. Điều này sẽ cho phép kiểm soát phức tạp và lâu dài đối với cách bitcoins có thể được chi tiêu, nhưng cũng sẽ giới thiệu rủi ro liên quan đến tự do chi tiêu và tính thay thế.

Tóm lại, một covenant không đệ quy chỉ giới hạn bản thân nó với giao dịch ngay lập tức theo sau giao dịch đã thiết lập các quy tắc. Ngược lại, một covenant đệ quy có khả năng áp đặt các điều kiện cụ thể lên một bitcoin một cách vô thời hạn. Các giao dịch có thể theo sau nhau, nhưng bitcoin đó sẽ luôn giữ các điều kiện ban đầu gắn liền với nó. Về mặt kỹ thuật, việc thiết lập một covenant không đệ quy xảy ra khi `scriptPubKey` của một UTXO định nghĩa các hạn chế đối với `scriptPubKey` của các đầu ra của một giao dịch chi tiêu UTXO đó. Mặt khác, việc thiết lập một covenant đệ quy xảy ra khi `scriptPubKey` của một UTXO định nghĩa các hạn chế đối với `scriptPubKey` của các đầu ra của một giao dịch chi tiêu UTXO đó, và đối với tất cả các `scriptPubKey` sẽ theo sau việc chi tiêu UTXO này.

Một cách tổng quát hơn, trong lĩnh vực máy tính, "đệ quy" là khả năng của một hàm gọi chính nó, tạo ra một loại vòng lặp.