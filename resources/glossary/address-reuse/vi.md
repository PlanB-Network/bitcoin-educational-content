---
term: TÁI SỬ DỤNG ĐỊA CHỈ
---

Tái sử dụng địa chỉ là việc sử dụng cùng một địa chỉ nhận để khóa nhiều UTXO, đôi khi trong nhiều giao dịch khác nhau. Bitcoin thường được khóa bằng một cặp khóa mã hóa tương ứng với một địa chỉ duy nhất. Vì blockchain là công khai, nên việc xác định địa chỉ nào liên kết với bao nhiêu bitcoin là dễ dàng. Trong trường hợp tái sử dụng cùng một địa chỉ cho nhiều khoản thanh toán, có thể hình dung rằng tất cả các UTXO liên quan đều thuộc về cùng một thực thể. Do đó, tái sử dụng địa chỉ gây ra vấn đề cho quyền riêng tư của người dùng. Nó cho phép liên kết xác định giữa nhiều giao dịch và UTXO, cũng như duy trì việc theo dõi quỹ trên chuỗi. Satoshi Nakamoto đã đề cập đến vấn đề này trong Bản Trắng của mình:

> "*Như một biện pháp phòng thủ bổ sung, một cặp khóa mới có thể được sử dụng cho mỗi giao dịch để giữ chúng không bị liên kết với một chủ sở hữu chung.*" - Nakamoto, S. (2008). "Bitcoin: Hệ thống Tiền tệ Điện tử Ngang hàng". Tham khảo tại https://bitcoin.org/bitcoin.pdf.

Để bảo vệ quyền riêng tư tối thiểu, việc sử dụng mỗi địa chỉ nhận chỉ một lần được khuyến nghị mạnh mẽ. Đối với mỗi khoản thanh toán mới, việc tạo ra một địa chỉ mới là phù hợp. Đối với các đầu ra thay đổi, một địa chỉ mới cũng nên được sử dụng. May mắn thay, nhờ vào ví xác định và phân cấp, việc sử dụng nhiều địa chỉ đã trở nên rất dễ dàng. Tất cả các cặp khóa liên kết với một ví có thể được tái tạo dễ dàng từ hạt giống. Đây cũng là lý do tại sao phần mềm ví luôn tạo ra một địa chỉ mới, khác nhau khi bạn nhấp vào nút “Nhận”.

> ► *Trong tiếng Anh, nó được gọi là "Address Reuse".*