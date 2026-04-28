---
name: Blockstream Explorer
description: Khám phá lớp chính của Bitcoin và Liquid Network
---

![cover](assets/cover.webp)



Blockstream Explorer là một dự án hỗ trợ việc khám phá các giao dịch và trạng thái toàn cầu của giao thức Bitcoin, cũng như [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) Liquid do công ty Blockstream phát triển.



Được khởi xướng vào năm 2014 bởi Blockstream, một công ty do Adam Back thành lập, trình khám phá [blockstream.info](https://blockstream.info) nhằm mục đích cung cấp cơ sở hạ tầng mạnh mẽ cho Bitcoin, đảm bảo khả năng tương tác và theo dõi giao dịch giữa các lớp (on-chain và Liquid), đồng thời tăng cường bảo mật và quyền riêng tư của người dùng.



Trong hướng dẫn này, chúng ta sẽ xem xét những điểm khác biệt, các dịch vụ của nó và cách nó cung cấp khả năng giám sát liền mạch các hoạt động và trạng thái của các lớp on-chain và Liquid của Bitcoin.



## Bắt đầu với Blockstream Explorer



### Điều hướng kênh chính



Khi bạn truy cập trình khám phá Blockstream.info, trên "**Bảng điều khiển**", chuỗi chính của giao thức Bitcoin được chọn theo mặc định. Từ giao diện này, bạn có thể xem tổng quan về:





- Kích thước chuỗi chính: Các khối được khai thác gần đây.



![blocks](assets/fr/01.webp)



Phần này cung cấp thông tin về các khối gần đây đã được khai thác, dấu thời gian, số lượng giao dịch được bao gồm trong mỗi khối, kích thước tính bằng kilobyte (kB) và phép đo của mỗi khối theo đơn vị trọng lượng (**WU** = *Đơn vị Trọng lượng*). Phép đo cuối cùng này rất hữu ích, vì nó cho phép chúng tôi đánh giá mức độ tối ưu hóa của khối, với điều kiện mỗi khối của chuỗi chính bị giới hạn ở `4.000.000 WU`, hay `4.000 kWU`.





- Giao dịch gần đây.



![transactions](assets/fr/02.webp)



Phần giao dịch cung cấp thông tin về mã định danh duy nhất của giao dịch, giá trị bitcoin liên quan, kích thước tính bằng byte ảo (vB) - đại diện cho tổng của tất cả dữ liệu (đầu vào và đầu ra) - và mức phí liên quan. Ví dụ: một giao dịch có kích thước `153 vB` với mức phí `2 sat/vB` sẽ phải chịu mức phí `306 satoshi`.



### Khám phá chất lỏng



Từ menu "**Khối**", bạn có thể theo dõi lịch sử của toàn bộ chuỗi chính trở lại khối cuối cùng được khai thác.



![blocs](assets/fr/03.webp)



Bằng cách nhấp vào một khối cụ thể, bạn có thể biết thêm chi tiết về thông tin và giao dịch có trong khối đó. Ví dụ: đối với khối 919330: bạn sẽ thấy mã băm của khối đó. Bạn cũng có thể điều hướng đến khối trước đó, vì mỗi khối được khai thác (ngoại trừ khối Genesis) đều được liên kết với khối trước đó, giữ nguyên mã băm của khối tiền nhiệm.



![metadata](assets/fr/04.webp)



Bằng cách nhấp vào nút **"Chi tiết"**, bạn có thể biết thêm thông tin về khối này, chẳng hạn như trạng thái của khối, xác nhận rằng khối đã được thêm vào chuỗi chính được giữ lại và lan truyền. Bạn cũng sẽ thấy độ khó của khối này: độ khó này thể hiện sức mạnh tính toán cần thiết để giải quyết bài toán mật mã của mining và được điều chỉnh sau mỗi 2016 khối (khoảng 2 tuần).



![details](assets/fr/05.webp)



Bên dưới phần chi tiết này, chúng ta sẽ tìm thấy tất cả các giao dịch có trong khối này.



Giao dịch đầu tiên trong khối được gọi là **giao dịch coinbase**. Giao dịch này được sử dụng để phân bổ phần thưởng mining của thợ đào (tất cả các khoản phí liên quan đến các giao dịch được bao gồm trong khối và khoản thưởng khối). Số bitcoin được tạo ra từ giao dịch này chỉ có thể được sử dụng sau khi 100 khối liên tiếp khác được đào. Nói cách khác, để có thể sử dụng chúng, thợ đào sẽ phải chờ khối **919430** được tạo ra. Khoảng thời gian này được gọi là [*"thời hạn đáo hạn"*](https://planb.academy/fr/resources/glossary/maturity-period).



Coinbase là một giao dịch đặc biệt: đây là giao dịch duy nhất không có dữ liệu đầu vào thực sự vì nó không chi bất kỳ bitcoin nào từ giao dịch trước đó.




![coinbase](assets/fr/06.webp)



Tất cả các giao dịch khác được chia thành hai phần: đầu vào và đầu ra.



Để bitcoin được sử dụng làm dữ liệu đầu vào trong một giao dịch mới, người khởi tạo giao dịch phải chứng minh quyền sở hữu của mình bằng cách cung cấp chữ ký tương ứng với một tập lệnh cụ thể. Mỗi phần bitcoin (UTXO) chứa một tập lệnh thường yêu cầu chữ ký cụ thể mà chỉ khóa riêng của người nắm giữ mới có thể cung cấp. Các tập lệnh này là ***scriptSig*** (trong ASM), được viết bằng Bitcoin Script, và có thể thuộc nhiều loại khác nhau. Trong ví dụ này, chúng ta có thể thấy rằng các UTXO được sử dụng thuộc loại P2SH và đầu ra thuộc loại P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Bạn có thể theo dõi lịch sử của một UTXO cụ thể bằng phương pháp heuristic. Chúng tôi mời bạn khám phá các phương pháp heuristic khác nhau của Bitcoin và các cách tăng cường tính bảo mật cho các giao dịch của bạn trên Bitcoin:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Hãy lấy ví dụ về chi phí đầu ra của giao dịch này. Khi nhấp vào mã giao dịch, chúng ta sẽ được chuyển hướng đến phần **Giao dịch** trên trang chi tiết giao dịch.



![transaction](assets/fr/08.webp)



Từ trang này, bạn có thể tìm hiểu giao dịch được bao gồm trong khối nào. Tùy thuộc vào loại địa chỉ được sử dụng, giao dịch có thể tối ưu hóa dữ liệu (*byte ảo*) và do đó trả ít phí giao dịch hơn. Ví dụ, giao dịch này đã tiết kiệm được 53% phí bằng cách sử dụng định dạng địa chỉ SegWit Bech32 gốc bắt đầu bằng `bc1q`.



![trx_details](assets/fr/09.webp)



## Lớp Liquid



Liquid Network là một [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) và là giải pháp mã nguồn mở cấp độ 2 cho giao thức Bitcoin. Đặc biệt, nó cho phép giao dịch bitcoin nhanh hơn và bảo mật hơn.



Trên trình khám phá Blockstream.info, nhấp vào nút **"Liquid"** để chuyển sang mạng Liquid.



![liquid](assets/fr/10.webp)



Khi nhấp vào một trong các giao dịch chúng tôi muốn theo dõi, chúng tôi thấy số lượng khối bitcoin được thay thế bằng dòng chữ "**Bí mật**". Trên mạng lưới này, các giao dịch có thể được bảo mật, vì vậy chúng tôi không thể xem số tiền của từng UTXO, dù trong hay ngoài giao dịch.



![liquid_trx](assets/fr/11.webp)



Tuy nhiên, chúng tôi lưu ý rằng các nguyên tắc và cơ chế hiện diện trên lớp chính của giao thức Bitcoin là giống nhau: tập lệnh khóa bitcoin và khả năng truy xuất nguồn gốc UTXO.



![liquid_details](assets/fr/12.webp)



Liquid Network cũng cung cấp tài sản kỹ thuật số phi lưu ký mà các tổ chức có thể sử dụng. Trong menu **"Tài sản"**, bạn sẽ tìm thấy danh sách các tài sản đã đăng ký, tổng số tài sản và tên miền liên quan.



![assets](assets/fr/13.webp)



Đối với mỗi tài sản, bạn có thể theo dõi lịch sử phát hành và giao dịch đốt (xóa tổng số tài sản đang lưu hành).



![assets_trxs](assets/fr/14.webp)




## Thêm tùy chọn



Trình khám phá Blockstream.info cũng bao gồm hình ảnh trực quan và theo dõi các giao dịch trên Testnet, Bitcoin, on-chain và Liquid Network.



![testnet](assets/fr/15.webp)



Khi bạn truy cập mạng Testnet, bạn không sử dụng bitcoin thật, nhưng bạn có tất cả các tính năng được mô tả ở trên.



![liquid_testnet](assets/fr/16.webp)



Mạng này có chiều dài chuỗi khác nhau, bạn có thể kết nối và kiểm tra hoạt động của cơ chế Bitcoin và Liquid.





- Phần API dành riêng cho bất kỳ ai muốn tích hợp một số chức năng Explorer nhất định vào ứng dụng của riêng mình. Thông qua API này, bạn có thể truy vấn chuỗi chính của các lớp khác nhau (on-chain và Liquid), theo dõi giao dịch và tìm ra mức phí trung bình cho các giao dịch trong một khối, chẳng hạn.



![api](assets/fr/17.webp)



Giờ đây, bạn đã sẵn sàng khai thác toàn bộ tiềm năng của Blockstream Explorer để truy vấn blockchain trên các lớp on-chain và Liquid. Chúng tôi hy vọng bạn thấy hướng dẫn này hữu ích và xin giới thiệu hướng dẫn của chúng tôi về một trình khám phá Bitcoin khác:



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f