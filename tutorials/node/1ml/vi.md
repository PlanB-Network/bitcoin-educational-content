---
name: 1ML
description: Hãy tìm hiểu cách sử dụng công cụ khám phá 1ML để hiểu và phân tích mạng Lightning của Bitcoin.
---
![cover](assets/cover.webp)



## Giới thiệu



Lightning Network là giải pháp thanh toán nhanh chóng, chi phí thấp được xây dựng trên nền tảng Bitcoin, cho phép thực hiện các giao dịch tức thời và an toàn. Quan sát mạng lưới này rất cần thiết để hiểu cách thức hoạt động, cấu trúc liên kết và trạng thái của các nút tạo nên nó. Một trình khám phá Lightning, như 1ML, được sử dụng để trực quan hóa dữ liệu công khai của mạng, bao gồm các nút đang hoạt động, các kênh mở và dung lượng khả dụng, cung cấp cái nhìn tổng quan có giá trị cho người dùng, nhà phát triển và người vận hành nút.



## Truy cập 1ML và tìm hiểu trang chủ.



Để truy cập 1ML, chỉ cần mở trình duyệt web và nhập [https://1ml.com](https://1ml.com). Điều này sẽ đưa bạn đến trang chủ, đóng vai trò là bảng điều khiển toàn cầu của Lightning Network.



![capture](assets/fr/03.webp)



Trang này hiển thị một số thống kê quan trọng ở đầu màn hình, bao gồm:





- **Tổng số nút hoạt động** trên mạng, tức là các máy tính tham gia vào việc gửi và nhận thanh toán Lightning.
- Số lượng kênh mở, tương ứng với các kết nối giữa các nút này cho phép chuyển tiền.
- **Tổng dung lượng mạng**, được biểu thị bằng bitcoin (BTC), cho biết tổng dung lượng của tất cả các kênh công cộng.



Những số liệu này được cập nhật thường xuyên để phản ánh tình trạng hiện tại của mạng lưới. Chúng cho thấy quy mô, tốc độ tăng trưởng và độ ổn định của mạng lưới.



![capture](assets/fr/04.webp)



Ngay bên dưới, trang này cung cấp các danh sách xếp hạng:





- Các **nút có nhiều kết nối nhất** là những nút có nhiều kênh mở nhất đến các nút khác.
- **Dung lượng cao nhất** trên các nút, cho biết nút nào có thể truyền tải lượng dữ liệu lớn nhất.
- Các kênh quan trọng nhất về mặt dung lượng.



Bạn cũng có thể sử dụng bộ lọc để tinh chỉnh các danh sách này theo vị trí địa lý hoặc các tiêu chí khác.



Trang này là điểm khởi đầu lý tưởng để khám phá Lightning Network và hiểu cấu trúc tổng quát của nó.



![capture](assets/fr/05.webp)



![capture](assets/fr/06.webp)



## Khám phá các nút Lightning



Để khám phá một nút trên 1ML, hãy bắt đầu bằng cách sử dụng thanh tìm kiếm ở đầu trang. Bạn có thể nhập **ID nút**, tức là mã định danh duy nhất của nút, hoặc **bí danh** của nó, một tên dễ nhớ hơn.



Sau khi quá trình tìm kiếm hoàn tất, hãy nhấp vào nút tương ứng để truy cập trang chi tiết của nó.



![capture](assets/fr/07.webp)



Trên trang này, một số thông tin quan trọng được hiển thị:





- Mã định danh nút**: Mã định danh duy nhất này là một chuỗi ký tự dài cho phép xác định chính xác nút đó trong toàn bộ mạng.



![capture](assets/fr/08.webp)





- Tên bí danh**: đây là tên do chủ sở hữu nút chọn để đại diện cho nút đó trước công chúng.



![capture](assets/fr/09.webp)





- **Số lượng kênh** cho biết số lượng kết nối mà nút đó đang mở với các nút khác, trong khi **tổng dung lượng** thể hiện tổng số bitcoin hiện có trong các kênh này. Một nút có số lượng kênh lớn và dung lượng cao thường được kết nối tốt và có khả năng chuyển một lượng lớn tiền nhanh chóng trên toàn mạng.



![capture](assets/fr/10.webp)





- **Thời gian hoạt động**, hay độ khả dụng, đo lường thời gian một nút duy trì hoạt động và có thể truy cập trực tuyến, phản ánh độ tin cậy của nó. Mặt khác, **tuổi đời** của nút cho biết thời gian nó đã có mặt trên mạng, phản ánh tính ổn định và kinh nghiệm của nó trong Lightning Network.



![capture](assets/fr/11.webp)



Dữ liệu này giúp bạn hiểu được tầm quan trọng và độ tin cậy của một nút trong Lightning Network. Ví dụ, một nút có số lượng kênh lớn, dung lượng cao và thời gian hoạt động liên tục cao thường là một thành phần quan trọng trong mạng lưới.



## Khám phá các kênh sét



### Kênh Lightning là gì?



Kênh Lightning là kết nối trực tiếp giữa hai nút mạng. Nó cho phép hai nút này trao đổi các khoản thanh toán tức thời, chi phí thấp mà không cần thông qua chuỗi chính Bitcoin cho mỗi giao dịch. Các kênh này là nền tảng giúp Lightning Network hoạt động nhanh và có khả năng mở rộng.



### Đọc thông tin kênh trên 1ML



Trên 1ML, mỗi kênh đều có trang riêng hoặc bảng mô tả chứa một số dữ liệu quan trọng:



Từ trang của một nút, bạn có thể truy cập danh sách các kênh của nó. Bằng cách nhấp vào một kênh, 1ML sẽ hiển thị một trang riêng với một số thông tin quan trọng.



![capture](assets/fr/12.webp)



![capture](assets/fr/13.webp)



Các dữ liệu chính có thể nhìn thấy như sau:





- Các nút đối tác**: mỗi kênh liên kết hai nút. 1ML hiển thị cả định danh và tên gọi khác tương ứng của chúng.



![capture](assets/fr/14.webp)





- Dung lượng kênh**: Đây là tổng số bitcoin bị khóa trong kênh này. Dung lượng này thể hiện giới hạn tối đa của các khoản thanh toán có thể được chuyển qua kênh này.



![capture](assets/fr/15.webp)





- Tuổi kênh**: cho biết kênh đã được mở trong bao lâu. Một kênh lâu năm thường là dấu hiệu của mối quan hệ ổn định giữa hai nút.



![capture](assets/fr/16.webp)



### Giới hạn khả năng hiển thị kênh



Điều quan trọng cần hiểu là 1ML chỉ hiển thị **một phần** của Lightning Network. Trình khám phá chỉ hiển thị **các kênh công khai**, tức là những kênh đã được công bố trên mạng. Các kênh riêng tư, thường được sử dụng vì lý do bảo mật hoặc chiến lược, không được hiển thị. Hơn nữa, 1ML không hiển thị sự phân bổ chính xác của tiền ở mỗi bên của một kênh, cũng như các khoản thanh toán đã thực hiện, hoặc tính thanh khoản thực tế có sẵn tại một thời điểm nhất định. Do đó, thông tin được hiển thị có thể được sử dụng để phân tích **cấu trúc chung của mạng lưới**, nhưng không thể hiện hoạt động tài chính thực tế hoặc tình trạng thanh khoản chi tiết của nó.



## Khám phá Lightning Network theo địa điểm



### Các nút theo quốc gia và khu vực



1ML cho phép bạn khám phá Lightning Network theo **phân chia địa lý**. Từ trang chủ hoặc thông qua các phần chuyên dụng, bạn có thể hiển thị các nút theo quốc gia hoặc khu vực. Tính năng này dựa trên thông tin vị trí do người vận hành nút khai báo.


Trên thanh điều hướng, bạn sẽ thấy liên kết **Vị trí**. Trên trang này, các nút được nhóm theo châu lục, quốc gia và thành phố.



![capture](assets/fr/17.webp)



Bằng cách chọn một quốc gia, 1ML sẽ hiển thị danh sách các nút liên kết, cùng với các số liệu thống kê tổng hợp như số lượng nút và tổng dung lượng khả dụng cho khu vực địa lý đó.



#### Điều này nói lên điều gì về việc áp dụng luật địa phương?





- **Mức độ áp dụng công nghệ**: Số lượng lớn các nút trong một khu vực cho thấy người dùng, công ty hoặc dịch vụ Bitcoin đang tích cực áp dụng Lightning Network. Điều này thể hiện sự trưởng thành về công nghệ và sự sẵn sàng tận dụng những lợi ích của Lightning (giao dịch nhanh, chi phí thấp hơn).
- Hệ sinh thái kinh tế**: Mật độ dày đặc các nút mạng cũng có thể là dấu hiệu của một mạng lưới kinh tế địa phương xung quanh Bitcoin: các thương nhân chấp nhận thanh toán bằng Lightning, các công ty khởi nghiệp phát triển công cụ, các sự kiện cộng đồng, v.v.
- Bảo mật và khả năng phục hồi**: Phân bố địa lý đa dạng giúp tăng cường khả năng phục hồi của mạng lưới khi gặp sự cố hoặc hạn chế cục bộ. Các nút càng phân tán, mạng lưới càng phi tập trung và càng khó bị kiểm duyệt.
- Chính sách và quy định**: Một số quốc gia có thể chứng kiến tốc độ áp dụng nhanh hơn nhờ khung pháp lý thuận lợi hoặc cộng đồng chủ động. Ngược lại, ở những khu vực có quy định nghiêm ngặt hoặc hà khắc, số lượng nút sẽ thấp hơn.



#### Những hạn chế của dữ liệu địa lý



Tuy nhiên, cần lưu ý rằng vị trí địa lý của các nút Lightning có những hạn chế và sai lệch nhất định:





- Vị trí IP gần đúng**: 1ML thường sử dụng địa chỉ IP công cộng của các nút để ước tính vị trí của chúng. Tuy nhiên, phương pháp này có thể bị sai lệch do việc sử dụng VPN, máy chủ đám mây (AWS, Google Cloud) hoặc lưu trữ ở các quốc gia khác với nơi cư trú thực tế của chủ sở hữu nút.
- Các nút ảo**: Một số nhà điều hành lưu trữ các nút của họ trên máy chủ từ xa vì lý do độ tin cậy và tính khả dụng, điều này có thể tạo ra cảm giác sai lệch về vị trí vật lý.
- Tính di động của người dùng**: Người vận hành nút có thể thay đổi vị trí, di chuyển cơ sở hạ tầng hoặc mở nhiều nút ở các khu vực khác nhau, khiến việc đọc dữ liệu trở nên phức tạp hơn.
- **Tính ẩn danh của các nút riêng tư**: Một số nút không công bố địa chỉ IP của chúng hoặc sử dụng các phương pháp để che giấu vị trí, khiến việc định vị địa lý trở nên bất khả thi.



## Các trường hợp sử dụng bê tông 1ML



### Hiểu về cấu trúc mạng



1ML cho phép bạn hình dung **cấu trúc tổng thể của Lightning Network**. Bằng cách quan sát các kết nối giữa các nút, số lượng kênh và dung lượng tổng thể, bạn có thể hiểu được mạng lưới được tổ chức như thế nào, nút nào đóng vai trò trung tâm và về mặt lý thuyết, dòng tiền thanh toán có thể lưu thông ra sao.



Việc hiểu rõ điều này là rất cần thiết nếu chúng ta muốn hiểu cách thức hoạt động của Lightning Network, chứ không chỉ đơn thuần là để sử dụng trong danh mục đầu tư.



### Xác định các nút quan trọng



Nhờ vào bảng xếp hạng do 1ML cung cấp (số lượng node kết nối nhiều nhất, dung lượng cao nhất, tuổi đời), người ta có thể xác định được các node chiếm vị trí quan trọng trong mạng lưới. Các node này thường đóng vai trò là cổng chính cho các giao dịch thanh toán Lightning.



![capture](assets/fr/18.webp)



### Kiểm tra khả năng hiển thị công khai của một nút.



Đối với người vận hành nút, 1ML cho phép bạn kiểm tra xem nút của mình có được **quảng cáo công khai** trên Lightning Network hay không. Nếu một nút xuất hiện trên 1ML, điều này có nghĩa là nó hiển thị và có thể truy cập được bởi các nút khác để mở các kênh công khai.


Điều này có thể hữu ích để chẩn đoán các vấn đề về khả năng hiển thị hoặc kết nối.



### Theo dõi sự phát triển của Lightning Network theo thời gian.



Bằng cách so sánh số liệu thống kê toàn cầu qua các giai đoạn khác nhau, 1ML cho phép chúng ta quan sát sự tiến hóa của Lightning Network: sự tăng hoặc giảm số lượng nút, sự biến đổi về tổng dung lượng hoặc sự thay đổi trong phân bố địa lý.


Những quan sát này mang đến một góc nhìn thú vị về sự phát triển, trưởng thành và xu hướng của Lightning Network.



## Các thực tiễn tốt nhất và hạn chế của 1ML



### Dữ liệu công khai không đồng nghĩa với toàn bộ thực tế.



1ML chỉ dựa trên dữ liệu **được công bố công khai** về Lightning Network. Điều này có nghĩa là công cụ này chỉ thể hiện một phần thực tế. Nhiều kênh có thể là kênh riêng tư, một số nút có thể không được quảng cáo và tính thanh khoản thực tế có sẵn trong các kênh không hiển thị. Do đó, điều cần thiết là sử dụng 1ML như một công cụ phân tích tổng quan, chứ không phải là một mô tả đầy đủ về mạng lưới.



### Quyền riêng tư và Tia chớp



Lightning Network được thiết kế với trọng tâm chính là **bảo mật thanh toán**. Các giao dịch riêng lẻ không hiển thị trên 1ML, và số dư kênh chính xác không được công khai. Hạn chế này không phải là lỗi của trình khám phá, mà là một tính năng cơ bản của Lightning Network, được thiết kế để bảo vệ quyền riêng tư của người dùng.



### Đừng vội kết luận.



Một nút mạng có dung lượng cao hoặc nhiều kênh không nhất thiết "đáng tin cậy" hay "hiệu quả" hơn trong mọi trường hợp. Tương tự, sự sụt giảm tạm thời về dung lượng mạng tổng thể không nhất thiết có nghĩa là có vấn đề về cấu trúc. Các số liệu luôn cần được xem xét lại và đặt trong bối cảnh cụ thể.



### Tính bổ sung với các công cụ khác



1ML là điểm khởi đầu tuyệt vời để khám phá Lightning Network, nhưng tốt nhất nên sử dụng nó kết hợp với các công cụ khác như danh mục Lightning, giao diện quản lý nút và các trình khám phá khác. Cách tiếp cận này cung cấp cái nhìn toàn diện và chi tiết hơn về mạng lưới.



## Tùy chọn kết nối 1ML (chức năng nâng cao)



1ML cung cấp tùy chọn **đăng nhập/tạo tài khoản**, hiển thị trên trang web, nhưng điều này **không cần thiết** để xem dữ liệu Lightning Network. Tất cả các tính năng đã được thảo luận trong hướng dẫn này đều có thể sử dụng **mà không cần tài khoản**.



Kết nối này chủ yếu hướng đến **các nhà điều hành nút Lightning**. Cụ thể, nó cho phép liên kết một nút với tài khoản 1ML để quản lý một số thông tin công khai nhất định, chẳng hạn như hình thức hiển thị của nút, liên kết liên hệ và các siêu dữ liệu khác. Tính năng này được thiết kế để cải thiện khả năng hiển thị và nhận dạng của một nút trong trình khám phá.



Điều quan trọng cần lưu ý là 1ML **không phải là dịch vụ lưu ký**. Việc tạo tài khoản không cấp quyền truy cập vào tiền, kênh hoặc khoản thanh toán của một node. Nó chỉ phục vụ mục đích tương tác với trình khám phá từ góc độ khai báo và cung cấp thông tin.



Trong bối cảnh học tập hoặc khám phá Lightning Network, tùy chọn này do đó có thể được coi là **tùy chọn bổ sung** và dành cho người dùng nâng cao hơn.



## Phần kết luận



1ML là một công cụ hữu ích để quan sát và hiểu Lightning Network dựa trên dữ liệu công khai của nó. Nó cho phép bạn khám phá cấu trúc mạng, phân tích các nút và kênh, và theo dõi sự phát triển tổng thể của việc áp dụng Lightning Network theo thời gian. Không cần tài khoản hay quản lý tiền bạc, 1ML cung cấp một cổng truy cập dễ dàng cho bất kỳ ai muốn hiểu sâu hơn về cách thức hoạt động của Lightning.


Nếu bạn muốn tìm hiểu sâu hơn về Lightning Network, tôi khuyên bạn nên tham gia khóa học Giới thiệu về Lightning Network đầy đủ:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb