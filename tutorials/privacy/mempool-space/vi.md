---
name: Mempool
description: Khám phá toàn bộ hệ sinh thái Bitcoin.
---

![cover](assets/cover.webp)



Giao thức Bitcoin là một mạng phi tập trung, ẩn danh, mở cửa cho việc tham vấn. Các thành viên (nút), tức là các máy tính có phiên bản phần mềm Bitcoin, có quyền truy cập không hạn chế vào tất cả dữ liệu được công bố trên Bitcoin. Tuy nhiên, trong những năm đầu của Bitcoin, giao thức này không được truy cập rộng rãi như hiện nay.


Trong những ngày đầu của Bitcoin, cần phải chạy một nút Bitcoin để truy cập các công cụ thích hợp (bitcoin-cli) để thẩm vấn mạng từ dòng lệnh.



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

Do đó, các dự án đã được triển khai để mở rộng cộng đồng Bitcoin, giúp bất kỳ ai không sở hữu nút và/hoặc không có các kỹ năng kỹ thuật cần thiết đều có thể tiếp cận cộng đồng này dễ dàng hơn.



Trong hướng dẫn này, chúng ta sẽ xem xét dự án **Mempool.space**, các tính năng của dự án và tác động của dự án này đến hệ sinh thái Bitcoin.



## Mempool.space là gì?



**Mempool.space** là một trình khám phá mã nguồn mở cung cấp thông tin hữu ích về giao dịch, phí giao dịch, khối và thợ đào trên nhiều mạng giao thức Bitcoin. Ra mắt vào năm 2020, nó mang lại sự cải thiện đáng kể về trải nghiệm người dùng thông qua đồ họa đại diện, hoạt ảnh mượt mà và giao diện gọn gàng.



Để hiểu dự án, Mempool (nhóm bộ nhớ) là không gian ảo lưu trữ tất cả các giao dịch đang chờ xác nhận trên mạng Bitcoin. Mempool giống như "phòng chờ" nơi các giao dịch Bitcoin chờ được xác nhận. Mỗi máy tính trên mạng (nút) có phòng chờ riêng, điều này giải thích tại sao không phải tất cả các giao dịch đều hiển thị cho mọi người cùng một lúc.



Tác động chính của nền tảng trong hệ sinh thái Bitcoin là nó cho phép bạn truy cập thông tin đa dạng trong vùng bộ nhớ của hầu hết các nút có trên Bitcoin mà không cần phải chạy một nút nào. Mempool.space là kho lưu trữ để xem và tìm kiếm các mạng giao thức Bitcoin.



Việc sử dụng ngày càng rộng rãi trong hệ sinh thái và thực tế là Mempool.space là mã nguồn mở đã cho phép nó được tích hợp vào ngày càng nhiều hệ thống lưu trữ cá nhân. Bây giờ bạn có thể có phiên bản Mempool.space của riêng mình trực tiếp trên nút cá nhân của bạn. Xem hướng dẫn của chúng tôi về cách cấu hình Mempool.space trên nút Umbrel của bạn bên dưới.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Những điều cơ bản của Mempool.space



Như đã đề cập ở trên, [Mempool.space](https://Mempool.space) là trình khám phá giao thức Bitcoin cho phép bạn theo dõi các giao dịch và sự lan truyền của chúng trên mạng Bitcoin đã chọn theo thời gian thực, từ Interface đồ họa.



Mempool.space hỗ trợ nhiều mạng giao thức Bitcoin.


Trên thanh menu, bạn sẽ tìm thấy các mạng sau:




- **Mainnet**: Mạng Bitcoin chính nơi diễn ra các giao dịch Bitcoin thực tế.
- **Signet**: Một mạng thử nghiệm sử dụng chữ ký số để xác thực các khối mà không cần đến các tài nguyên mà mạng chính yêu cầu.
- **Testnet 3**: Mạng thử nghiệm và phát triển không rủi ro trên giao thức Bitcoin.
- **Testnet 4**: Phiên bản mới của Testnet 3 mang lại tính ổn định cao hơn và các quy tắc đồng thuận mới cho môi trường thử nghiệm.



![reseaux](assets/fr/01.webp)



Trên trang chủ, bên trái trong Green, bạn sẽ thấy các khối tương lai có thể (nhóm giao dịch) sẵn sàng để được xác thực và tích hợp (khai thác) vào mạng Bitcoin. Trung bình, một khối được khai thác cứ sau mười phút: hãy giữ thông tin này, vì nó sẽ hữu ích sau này trong quá trình phát triển của chúng tôi.


Ở phía bên phải, bạn sẽ thấy các khối màu tím được khai thác gần đây trên Bitcoin, với số khối được khai thác gần đây nhất thể hiện chiều cao hiện tại của mạng.



![blocs](assets/fr/02.webp)



Phần **Phí giao dịch** là công cụ ước tính phí giao dịch. Phí phân bổ cho giao dịch của bạn càng cao thì khả năng giao dịch của bạn được thêm vào khối tiếp theo sẵn sàng để khai thác càng cao.


Phí giao dịch là chi phí mà Miner sẽ lấy từ bạn để chèn giao dịch của bạn vào khối ứng viên cho Mining. Nó được xác định bằng tỷ lệ sat/vB (Satoshi/Byte ảo) biểu thị số satoshi bạn trả cho không gian mà giao dịch của bạn sẽ chiếm trong khối ứng viên.



⚠️ QUAN TRỌNG: Trong trường hợp bão hòa Mempool, thợ đào sẽ ưu tiên các giao dịch cung cấp tỷ lệ Satoshi/vByte tốt nhất. Giao dịch của bạn càng nặng (lớn) thì càng cần nhiều satoshi để đưa vào nhanh chóng.



![fees-visualizer](assets/fr/03.webp)



Phần **Kính Mempool** cho phép bạn hình dung không gian diễn ra giao dịch.



![mempool](assets/fr/04.webp)



Một khối được khai thác khoảng mười phút một lần do độ khó của Proof of Work mà thợ đào phải cung cấp để thêm khối ứng viên của họ vào chuỗi các khối đã khai thác. Độ khó này thay đổi sau mỗi **2016 khối**, tương đương với khoảng **2 tuần**. Bạn có thể xem sự tiến triển của độ khó này tại đây.



![difficulty](assets/fr/05.webp)



Việc thêm một khối mới vào chuỗi chính cho phép Miner của khối đã xác thực được hưởng phần thưởng bao gồm một phần cố định (giảm một nửa sau mỗi 210.000 khối**, tương đương với khoảng 4 năm** trong thời gian giảm một nửa) và phí giao dịch.



![halving](assets/fr/06.webp)



## Truy cập thông tin chi tiết giao dịch của bạn



Trong thanh tìm kiếm Mempool.space, bạn có thể nhập Bitcoin Address hoặc transaction ID của mình để tìm hiểu thêm về lịch sử của bạn.



![search](assets/fr/07.webp)



Trên trang chi tiết giao dịch, bạn sẽ tìm thấy thông tin chung về giao dịch của mình:




- **Trạng thái**: Đã xác nhận khi được thêm vào khối, chưa xác nhận khi chờ trong Mempool.
- **Phí giao dịch**.
- **Thời gian dự kiến đến (ETA)**: Thời gian ước tính để giao dịch của bạn được thêm vào một khối. Thời gian này được tính theo tỷ lệ cấu thành phí liên quan đến giao dịch này.



![general-txinfo](assets/fr/08.webp)



Phần **Luồng** hiển thị biểu đồ các thành phần giao dịch của bạn.



Đầu vào (UTXO trước đây) được sử dụng cho giao dịch của bạn và đầu ra cho phép người nhận có quyền sử dụng bitcoin từ mỗi đầu ra bằng cách xuất trình chữ ký cần thiết cho chi tiêu của họ.



![flow](assets/fr/09.webp)



Bạn có thể tìm thấy thông tin chi tiết hơn về các địa chỉ được sử dụng trong phần **Đầu vào & Đầu ra**.



![address](assets/fr/10.webp)



Khám phá các chương trình giao dịch Bitcoin khác nhau để tăng cường tính bảo mật của bạn.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Tăng tốc giao dịch của bạn



Trong hệ sinh thái Bitcoin, khía cạnh xác thực giao dịch của thợ đào có liên quan mật thiết đến phí giao dịch liên quan đến giao dịch đó. Thợ đào ưu tiên các giao dịch có tỷ lệ phí cao hơn (satoshi/vByte), điều này có thể ảnh hưởng đến tính hợp lệ của giao dịch nếu bạn không trả phí hợp lý mà thợ đào chấp nhận. Giao dịch của bạn sẽ bị kẹt trong Mempool khi chờ khối chấp nhận tỷ lệ phí của nó.



May mắn thay, có hai phương pháp khả dụng trên mạng Bitcoin để đẩy nhanh quá trình xác nhận giao dịch của bạn.





- **RBF** - Thay thế theo Phí: Một phương pháp cho phép bạn chi tiêu cùng một mục nhập như giao dịch phí thấp của bạn, nhưng lần này bằng cách tăng phí giao dịch để tăng tốc độ xác thực. Giao dịch mới của bạn sẽ được xác thực nhanh hơn và được đưa vào một khối, vô hiệu hóa giao dịch phí thấp.



Bạn có thể thực hiện hành động thay thế phí với các danh mục đầu tư chấp nhận cơ chế này. Ví dụ, hãy xem bài viết của chúng tôi về danh mục đầu tư Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- **CPFP** - Child pay for parent: Một cách tiếp cận lấy cảm hứng từ RBF, nhưng ở phía người nhận. Khi giao dịch mà bạn là người nhận bị chặn trong Mempool, bạn có tùy chọn chi tiêu các đầu ra (UTXO) của giao dịch này, mặc dù thực tế là giao dịch đó vẫn chưa được xác nhận, bằng cách phân bổ nhiều phí hơn cho giao dịch mới này để mức phí trung bình - của giao dịch mà bạn là người nhận và giao dịch được khởi tạo - khuyến khích thợ đào đưa cả hai giao dịch vào một khối.



⚠️ Giao dịch đầu tiên phải được đưa vào một khối để có thể xác nhận giao dịch thứ hai.



Nếu tất cả các thuật ngữ này có vẻ hơi quá kỹ thuật, tôi khuyên bạn nên [tham khảo bảng thuật ngữ của chúng tôi](https://planb.academy/resources/glossary), trong đó có định nghĩa về tất cả các thuật ngữ kỹ thuật liên quan đến Bitcoin và hệ sinh thái của nó.



Ngoài các phương pháp này, Mempool.space, nhờ kết nối với hơn 80% thợ đào có mặt trên mạng Bitcoin, còn cho phép bạn đẩy nhanh bất kỳ giao dịch **chưa xác nhận** nào của mình, ngay cả những giao dịch không kích hoạt RBF, bằng cách trả tiền cho thợ đào trong Exchange để đưa giao dịch chi phí thấp của bạn vào khối tiếp theo sẵn sàng để khai thác.



Trên trang chi tiết giao dịch, nhấp vào nút **Tăng tốc**, sau đó tiến hành thanh toán cho bên đối tác của bạn với thợ đào.



![accelerate-section](assets/fr/11.webp)


## Trẻ vị thành niên



Miner ám chỉ một người quản lý một mỏ, tức là một máy tính tham gia vào quy trình Mining, bao gồm việc tham gia vào Proof-of-Work. Miner nhóm các giao dịch đang chờ xử lý trong Mempool của mình để tạo thành một khối ứng viên. Sau đó, nó tìm kiếm một Hash hợp lệ, nhỏ hơn hoặc bằng mục tiêu, cho tiêu đề của khối này bằng cách sửa đổi các nonce khác nhau. Nếu anh ta tìm thấy một Hash hợp lệ, anh ta sẽ phát khối của mình đến mạng Bitcoin và bỏ túi phần thưởng tiền tệ liên quan, bao gồm trợ cấp khối (tạo ra bitcoin mới từ hư không) và phí giao dịch.



https://planb.academy/courses/ce272232-0d97-4482-884a-0f77a2ebc036

❗Thợ đào giống như "người xác thực" xác minh và nhóm các giao dịch thành các khối. Để thêm một khối mới vào mạng Bitcoin, họ phải giải một câu đố toán học phức tạp (Proof-of-Work). Miner đầu tiên giải được câu đố sẽ giành được phần thưởng Bitcoin (tiền thưởng khối + phí cho các giao dịch được bao gồm trong khối).



Độ khó của Proof of Work này được theo dõi, cho phép bạn hình dung sự tiến triển của sức mạnh tính toán cần thiết cho thợ mỏ. Bạn sẽ tìm thấy trong các phần bên dưới:





- Ước tính tổng phần thưởng mà thợ đào thu được trong lần điều chỉnh độ khó cuối cùng, cũng như ước tính Halving tiếp theo của khoản tài trợ khối, diễn ra sau mỗi 210.000 khối (khoảng 04 năm).



![rewards](assets/fr/12.webp)



Độ khó này được điều chỉnh sau mỗi 2016 khối (khoảng hai tuần). Nó tỷ lệ nghịch với thời gian trung bình mà thợ đào mất để đạt được Miner sau mỗi 2016 khối.


Khi thời gian trung bình của thợ đào ít hơn 10 phút, độ khó tăng lên, chứng tỏ thợ đào dễ dàng xác thực khối Miner hơn. Ngược lại, khi thời gian trung bình lớn hơn 10 phút, độ khó giảm xuống.



![mining-pool](assets/fr/13.webp)





- Nhóm thợ đào: Xét đến độ khó liên quan, một nhóm thợ đào hợp tác để giúp tìm Proof of Work trên Bitcoin, trong cái mà chúng tôi gọi là **pool**. Khi một khối được nhóm khai thác, phần thưởng thu được sẽ được phân phối theo tỷ lệ thành công trong mỗi lần tìm kiếm giải pháp một phần của Miner, tức là đóng góp vào sức mạnh tính toán trong quá trình tìm kiếm Proof-of-Work hoặc theo phương pháp trả công mà sự hợp tác đã thỏa thuận.





![mining](assets/fr/14.webp)



## Cơ sở hạ tầng Lightning Network



Mempool không chỉ cung cấp thông tin về cơ sở hạ tầng mạng của Bitcoin (chuỗi chính). Nó còn tích hợp các công cụ trực quan hóa và khám phá cho lớp phủ Lightning của Bitcoin.



Trong phần **Lightning**, bạn có thể xem tất cả các kết nối hiện có giữa các nút Lightning.



![network-stats](assets/fr/15.webp)



Interface này cung cấp thông tin về:





- Thống kê Lightning Network.



![distribution](assets/fr/16.webp)




⚠️ **QUAN TRỌNG**: Dung lượng của kênh thanh toán chỉ định số tiền tối đa mà một nút có thể gửi cho một nút khác trong giao dịch Lightning.





- Các nút Lightning được phân bổ theo nhà cung cấp dịch vụ Internet (dịch vụ lưu trữ) và tùy chọn theo dung lượng kênh thanh toán.



![distribution](assets/fr/17.webp)





- Lịch sử về tổng công suất của Lightning Network.


Bạn cũng sẽ tìm thấy thứ hạng của các nút này theo khả năng của kênh thanh toán của chúng.



![ranking](assets/fr/18.webp)



## Thêm đồ họa



Mempool.space là nền tảng lý tưởng để tận hưởng tương tác với mạng lưới giao thức Bitcoin. Các biểu đồ không chỉ cung cấp dữ liệu trực quan để giúp bạn quyết định thời điểm thực hiện giao dịch mà còn cung cấp các thông số chính xác cho phép bạn hình dung, theo thời gian thực, sức mạnh và tình trạng của mạng lưới Bitcoin và cơ sở hạ tầng Lightning liên quan.



Trong phần **Đồ họa**, bạn có thể xem dữ liệu cần thiết về mạng Bitcoin:




- Sự thay đổi kích thước Mempool: Bạn có thể quan sát cách kích thước của Mempool dao động, điều này có thể chỉ ra các giai đoạn hoạt động cao hoặc thấp trên mạng.



![graphs](assets/fr/19.webp)






- Sự phát triển của các giao dịch và phí giao dịch trên mạng đã chọn: Bằng cách theo dõi các biến thể trong giao dịch mỗi giây, bạn có thể dự đoán các giai đoạn tắc nghẽn hoặc hoạt động thấp và tối ưu hóa phí giao dịch của mình. Biểu đồ này cung cấp cho bạn góc nhìn về khả năng xử lý khối lượng giao dịch của mạng.



![graphs](assets/fr/20.webp)



Bây giờ bạn đã đến cuối hành trình của mình trên Mempool.space, hãy trở thành nhà thám hiểm của riêng bạn và theo dõi các giao dịch của bạn theo thời gian thực. Vui lòng xem bài viết bên dưới của chúng tôi về nhà thám hiểm Bitcoin **Public Pool**.



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1