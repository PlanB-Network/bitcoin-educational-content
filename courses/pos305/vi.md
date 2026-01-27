---
name: Làm chủ BTC Pay Server
goal: Cấu hình một phiên bản BTC Pay Server cho doanh nghiệp địa phương
objectives:
- Hiểu các nguyên tắc cơ bản về vai trò của BTCPay Server trong xử lý thanh toán
- Thành thạo hoạt động bên trong của quy trình cấu hình BTCPay Server
- Triển khai BTCPay Server trên môi trường đám mây và dựa trên nút
- Trở thành người vận hành BTC Pay Server
---
# Hành Trình Đến Chủ Quyền Tài Chính

Niềm tin rất mong manh, đặc biệt khi liên quan đến tiền bạc. Khóa học giới thiệu này hướng dẫn bạn qua BTCPay Server, một công cụ mạnh mẽ cho phép bạn chấp nhận thanh toán Bitcoin mà không cần dựa vào bên thứ ba. Bạn sẽ học các kiến thức cơ bản để trở thành người vận hành BTCPay Server

Được tạo bởi Alekos và Bas, và chuyển thể bởi melontwist và asi0, khóa học này tiết lộ cách các cá nhân và doanh nghiệp đang xây dựng các giải pháp thay thế cho hệ thống thanh toán truyền thống. Cho dù bạn tò mò về Bitcoin hay sẵn sàng vận hành cơ sở hạ tầng thanh toán cho doanh nghiệp, bạn sẽ khám phá các kỹ năng thực tế thách thức hiện trạng. Sẵn sàng khám phá sự độc lập tài chính thực sự trông như thế nào chưa?
+++
# Giới thiệu


<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>


## Tổng quan về khóa học


<chapterId>785ed2bc-94ae-4962-a26a-edf5742a3c72</chapterId>


Chào mừng bạn đến với khóa học POS 305 về Máy chủ BTCPay!


Mục tiêu của khóa đào tạo này là hướng dẫn bạn cách cài đặt, cấu hình và sử dụng Máy chủ BTCPay trong doanh nghiệp hoặc tổ chức của mình. Máy chủ BTCPay là một giải pháp mã nguồn mở cho phép bạn xử lý thanh toán Bitcoin một cách tự động, an toàn và tiết kiệm chi phí. Khóa học này chủ yếu hướng đến những người dùng nâng cao muốn thành thạo việc tự lưu trữ Máy chủ BTCPay để tích hợp hoàn toàn vào hoạt động hàng ngày.


**Phần 1: Giới thiệu về Máy chủ BTCPay**

Chúng ta sẽ bắt đầu với phần giới thiệu chung về Máy chủ BTCPay, bao gồm màn hình đăng nhập, quản lý tài khoản người dùng và tạo cửa hàng mới. Phần giới thiệu này sẽ giúp bạn hiểu rõ hơn về Máy chủ BTCPay Interface và nắm bắt các tính năng cơ bản cần thiết để bắt đầu sử dụng công cụ này.


**Phần 2: Giới thiệu về Bảo mật Khóa Bitcoin**

Bảo mật tài khoản Bitcoin của bạn rất quan trọng. Trong phần này, chúng ta sẽ tìm hiểu cách tạo khóa mật mã, cách sử dụng ví phần cứng để bảo mật các khóa này và cách tương tác với khóa của bạn thông qua Máy chủ BTCPay. Bạn cũng sẽ tìm hiểu cách cấu hình Máy chủ BTCPay Lightning Wallet để tối ưu hóa giao dịch.


**Phần 3: Máy chủ BTCPay Interface**

Phần này sẽ hướng dẫn bạn sử dụng máy chủ BTCPay Interface. Bạn sẽ học cách điều hướng bảng điều khiển, cấu hình cài đặt cửa hàng và máy chủ, quản lý thanh toán và tận dụng các plugin tích hợp. Mục tiêu là cung cấp cho bạn các công cụ cần thiết để tùy chỉnh cài đặt theo nhu cầu cụ thể của bạn.


**Phần 4: Cấu hình máy chủ BTCPay**

Cuối cùng, chúng tôi sẽ tập trung vào việc cài đặt thực tế Máy chủ BTCPay trong nhiều môi trường khác nhau. Cho dù bạn đang sử dụng LunaNode, Voltage hay Umbrel node, bạn sẽ được học các bước thiết yếu để triển khai và cấu hình Máy chủ BTCPay, có tính đến đặc điểm cụ thể của từng môi trường.


Bạn đã sẵn sàng làm chủ BTCPay Server và phát triển doanh nghiệp của mình chưa? Bắt đầu thôi!


## Sự hoan nghênh của giới phê bình dành cho Bitcoin và Máy chủ BTCPay của Tác giả


<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>


Hãy bắt đầu bằng việc tìm hiểu BTCPay Server là gì và nguồn gốc của nó. Chúng tôi coi trọng tính minh bạch và các tiêu chuẩn nhất định để tạo dựng niềm tin trong không gian Bitcoin.

Một dự án trong lĩnh vực này đã phá vỡ những giá trị này. Nhà phát triển chính của BTCPay Server, Nicolas Dorier, đã coi đây là chuyện cá nhân và hứa sẽ loại bỏ chúng. Giờ đây, sau nhiều năm, chúng ta đang cùng nhau hướng tới tương lai này, hoàn toàn mã nguồn mở, mỗi ngày.


> Đây là lời nói dối, niềm tin của tôi vào anh đã tan vỡ, tôi sẽ khiến anh trở nên lỗi thời.
> Nicolas Dorier

Sau những lời Nicolas nói, đã đến lúc bắt đầu xây dựng. Rất nhiều công sức đã được bỏ ra cho cái mà chúng tôi hiện gọi là Máy chủ BTCPay. Nhiều người muốn đóng góp vào nỗ lực này. Những người nổi tiếng nhất là r0ckstardev, MrKukks, Pavlenex, và astupidmoose, thương gia đầu tiên sử dụng phần mềm này.


Nguồn mở có nghĩa là gì và một dự án như vậy bao gồm những gì?


FOSS là viết tắt của Free & Open-Source Software (Phần mềm Tự do & Nguồn mở). Thuật ngữ "Free & Open-Source" (FOSS) đề cập đến các điều khoản cho phép bất kỳ ai sao chép, chỉnh sửa và thậm chí phân phối các phiên bản (kể cả vì mục đích lợi nhuận) của phần mềm. Thuật ngữ "Free & Open-Source" (FOSS) đề cập đến việc chia sẻ mã nguồn một cách công khai, khuyến khích cộng đồng đóng góp và cải thiện nó.

Điều này thu hút những người dùng giàu kinh nghiệm, những người nhiệt tình đóng góp cho phần mềm mà họ đã sử dụng và nhận được giá trị từ đó, cuối cùng chứng minh được sự thành công hơn trong việc áp dụng so với phần mềm độc quyền. Điều này phù hợp với tinh thần của Bitcoin: "Thông tin khao khát được tự do". Nó tập hợp những người đam mê, tạo thành một cộng đồng và đơn giản là thú vị hơn. Giống như Bitcoin, FOSS là điều tất yếu.


### Trước khi chúng ta bắt đầu


Khóa học này bao gồm nhiều phần. Nhiều phần sẽ do giáo viên phụ trách, môi trường Demo mà bạn được phép truy cập, máy chủ lưu trữ cho riêng bạn và có thể là một tên miền. Nếu bạn tự học khóa học này, xin lưu ý rằng bạn sẽ không được sử dụng các môi trường được gắn nhãn DEMO.

Lưu ý: Nếu bạn học khóa học này tại lớp học, tên máy chủ có thể khác nhau tùy thuộc vào thiết lập lớp học. Do đó, các biến trong tên máy chủ có thể khác nhau.


### Cấu trúc khóa học


Mỗi chương đều có mục tiêu và bài đánh giá kiến thức. Trong khóa học này, chúng tôi sẽ đề cập đến từng mục tiêu và tóm tắt các điểm chính vào cuối mỗi khối bài học (tức là mỗi chương). Hình ảnh minh họa được sử dụng để cung cấp phản hồi trực quan và củng cố các khái niệm chính một cách trực quan. Mục tiêu được đặt ra ở đầu mỗi khối bài học. Những mục tiêu này không chỉ đơn thuần là một danh sách kiểm tra. Chúng cung cấp cho bạn hướng dẫn để tiếp cận một bộ kỹ năng mới. Bài đánh giá kiến thức sẽ ngày càng khó hơn khi quá trình thiết lập Máy chủ BTCPay của bạn hoàn tất.


### Học viên nhận được gì từ khóa học này?


Với Khóa học Máy chủ BTCPay, học viên có thể hiểu các nguyên tắc cơ bản, cả về mặt kỹ thuật lẫn phi kỹ thuật, của Bitcoin. Khóa đào tạo chuyên sâu về sử dụng Bitcoin thông qua Máy chủ BTCPay sẽ cho phép học viên vận hành cơ sở hạ tầng Bitcoin của riêng mình.


### Địa chỉ Web quan trọng hoặc Cơ hội liên hệ


Quỹ BTCPay Server, nơi đã cho phép Alekos và Bas viết khóa học này, có trụ sở tại Tokyo, Nhật Bản. Bạn có thể liên hệ với Quỹ BTCPay Server thông qua trang web được liệt kê.



- https://foundation.btcpayserver.org
- Tham gia kênh trò chuyện chính thức: https://chat.btcpayserver.org


## Giới thiệu về Bitcoin


<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>


### Hiểu Bitcoin thông qua bài tập trên lớp


Đây là bài tập trên lớp, vì vậy nếu bạn tự học, bạn không thể thực hiện được, nhưng bạn vẫn có thể làm bài tập này. Để hoàn thành bài tập này, cần tối thiểu 9 đến 11 người.


Bài tập bắt đầu sau khi xem phần giới thiệu “Cách thức hoạt động của Bitcoin và Blockchain” của BBC.


:::video id=c20b6df7-0c3a-4785-94b9-42ef59093acc:::

Bài tập này yêu cầu tối thiểu chín người tham gia. Bài tập này nhằm mục đích cung cấp hiểu biết thực tế về cách thức hoạt động của Bitcoin. Bằng cách đóng vai trò trong mạng lưới, bạn sẽ có được cách học tập tương tác và vui nhộn. Bài tập này không liên quan đến Lightning Network.


### Ví dụ: Cần 9/11 người


Các vai trò là:



- 1 Khách hàng
- 1 Thương gia
- 7 đến 9 nút Bitcoin


**Thiết lập như sau:**


Khách hàng mua sản phẩm tại cửa hàng bằng Bitcoin.


**Kịch bản 1 - Hệ thống ngân hàng truyền thống**



- Cài đặt:
  - Xem sơ đồ/giải thích trong Figjam đính kèm - [Sơ đồ hoạt động](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Chọn ba sinh viên tình nguyện đóng vai Khách hàng (Alice), Người bán (Bob) và Ngân hàng.
- Diễn tả lại chuỗi sự kiện:
  - Khách hàng duyệt cửa hàng trực tuyến và tìm thấy một mặt hàng có giá 25 đô la mà họ muốn và thông báo cho Người bán rằng họ muốn mua
  - Người bán hàng yêu cầu thanh toán.
  - Khách hàng- gửi thông tin thẻ cho Merchant
  - Người bán chuyển tiếp thông tin đến Ngân hàng (xác định cả thông tin của họ và danh tính/thông tin), yêu cầu thanh toán
  - Ngân hàng thu thập thông tin về Khách hàng và Người bán (Alice và Bob) và kiểm tra xem số dư của khách hàng có đủ không.
  - Trừ 25 đô la từ tài khoản của Alice, thêm 24 đô la vào tài khoản của Bob, lấy 1 đô la cho dịch vụ
  - Người bán nhận được xác nhận từ Ngân hàng và gửi hàng đến cho khách hàng.
- Bình luận:
  - Bob và Alice phải có mối quan hệ với một ngân hàng.
  - Ngân hàng thu thập thông tin nhận dạng về cả Bob và Alice.
  - Ngân hàng lấy một phần.
  - Ngân hàng phải được tin cậy để giữ quyền quản lý tiền của mỗi người tham gia mọi lúc.


**Kịch bản 2 - Hệ thống Bitcoin**



- Cài đặt:
  - Xem sơ đồ/giải thích trong Figjam đính kèm - [Sơ đồ hoạt động](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Thay thế Ngân hàng bằng chín sinh viên sẽ đóng vai trò là Máy tính (Nút Bitcoin/Thợ đào) trong mạng để thay thế Ngân hàng.
- Mỗi máy tính trong số 9 máy tính đều có hồ sơ lịch sử đầy đủ về tất cả các giao dịch đã từng được thực hiện (do đó có số dư chính xác không có giả mạo) cũng như một bộ quy tắc:
  - Xác minh giao dịch được ký đúng cách (thekeyfitsthelock)
  - Phát và nhận các giao dịch hợp lệ tới các đối tác trong mạng, loại bỏ các giao dịch không hợp lệ (bao gồm bất kỳ giao dịch nào cố gắng chi tiêu cùng một khoản tiền hai lần)
- Cập nhật/Thêm hồ sơ định kỳ với các giao dịch mới nhận được từ máy tính "ngẫu nhiên" với điều kiện tất cả nội dung đều hợp lệ (lưu ý: hiện tại, chúng tôi đang bỏ qua thành phần Proof of Work cho tất cả những điều này để đơn giản), nếu không, hãy từ chối những điều này và tiếp tục như trước cho đến khi máy tính "ngẫu nhiên" tiếp theo gửi bản cập nhật
  - Số tiền thưởng sẽ được trao nếu nội dung hợp lệ.
- Diễn tả lại chuỗi sự kiện:
  - Khách hàng duyệt cửa hàng trực tuyến và tìm thấy một mặt hàng có giá 25 đô la mà họ muốn và thông báo cho Người bán rằng họ muốn mua
  - Người bán yêu cầu thanh toán bằng cách gửi cho khách hàng Invoice/Address từ Wallet của họ.
  - Khách hàng - xây dựng giao dịch (gửi số BTC trị giá 25 đô la đến Address do Người bán cung cấp) và phát sóng giao dịch đó đến Mạng Bitcoin.
- Máy tính - tiếp nhận giao dịch và xác minh:
  - Có ít nhất 25 đô la BTC trong Address được gửi từ
  - Giao dịch được ký đúng cách (“đã được mở khóa” bởi khách hàng)
  - Nếu không, giao dịch sẽ không được truyền qua mạng và nếu có, giao dịch sẽ được truyền và giữ ở trạng thái chờ.
  - Người bán có thể kiểm tra xem giao dịch có đang chờ xử lý hay không.
- Một máy tính được chọn "ngẫu nhiên" để đề xuất hoàn tất giao dịch được đề xuất bằng cách phát "một khối" chứa giao dịch đó; nếu giao dịch thành công, máy tính đó sẽ nhận được phần thưởng BTC.
  - TÙY CHỌN/NÂNG CAO - thay vì chọn ngẫu nhiên một Máy tính, hãy mô phỏng Mining bằng cách để Máy tính tung xúc xắc cho đến khi có một số kết quả được xác định trước xảy ra (ví dụ: máy đầu tiên tung được hai mặt sáu sẽ được chọn)
  - Nó cũng có thể đưa ra kết quả nếu hai Máy tính chiến thắng gần như cùng một lúc, dẫn đến việc tách chuỗi.
  - Máy tính kiểm tra tính hợp lệ, cập nhật/thêm hồ sơ vào sổ cái nếu đáp ứng các quy tắc và phát khối giao dịch tới các đối tác.
  - Máy tính được chọn ngẫu nhiên sẽ nhận được phần thưởng khi đề xuất được một khối hợp lệ.
  - Người bán kiểm tra giao dịch đã hoàn tất; do đó, tiền đã được nhận và sản phẩm đã được gửi đến khách hàng.
- Bình luận:
  - Lưu ý rằng không cần phải có mối quan hệ ngân hàng trước đó.
  - Không cần bên thứ ba hỗ trợ; thay thế bằng mã/ưu đãi.
  - Không ai bên ngoài Exchange trực tiếp thu thập dữ liệu và chỉ trao đổi số lượng cần thiết giữa những người tham gia (ví dụ: vận chuyển Address).
  - Không cần sự tin tưởng giữa mọi người (ngoại trừ Người bán gửi hàng), giống như mua bằng tiền mặt theo nhiều cách.
  - Số tiền này do cá nhân trực tiếp sở hữu.
  - Bitcoin Ledger được biểu thị bằng đô la để đơn giản, nhưng thực tế, nó là BTC.
  - Chúng tôi mô phỏng một giao dịch duy nhất đang được phát sóng, nhưng trên thực tế, có nhiều giao dịch đang chờ xử lý trong mạng, và các khối chứa hàng nghìn giao dịch cùng một lúc. Các nút cũng xác minh rằng không có giao dịch chi tiêu gấp đôi nào đang chờ xử lý (trong trường hợp này, tôi sẽ loại bỏ tất cả trừ một giao dịch).
- Các tình huống gian lận:
  - Nếu khách hàng không có 25 BTC thì sao?
    - Họ sẽ không thể tạo giao dịch vì "mở khóa" và "Ownership" là một và máy tính kiểm tra xem giao dịch đã được ký đúng chưa; nếu không, chúng sẽ từ chối giao dịch.
  - Điều gì sẽ xảy ra nếu máy tính được chọn ngẫu nhiên cố gắng “thay đổi Ledger”?
    - Khối này sẽ bị từ chối vì mọi máy tính khác đều có lịch sử hoạt động đầy đủ và sẽ nhận thấy sự thay đổi, vi phạm một trong các quy tắc của chúng.
    - Máy tính ngẫu nhiên sẽ không nhận được phần thưởng và không có giao dịch nào từ khối của họ được hoàn tất.


## Đánh giá kiến thức


<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>


### Thảo luận lớp học KA


Thảo luận về một số cách đơn giản hóa quá mức trong bài tập trên lớp theo tình huống thứ hai và mô tả chi tiết hơn về chức năng thực tế của hệ thống Bitcoin.


### Ôn tập từ vựng KA


Định nghĩa các thuật ngữ chính sau đây được giới thiệu trong phần trước:



- Nút
- Mempool
- Mục tiêu khó khăn
- Khối


**Thảo luận ý nghĩa của một số thuật ngữ bổ sung theo nhóm:**


Blockchain, Giao dịch, Chi tiêu gấp đôi, Bài toán của các vị tướng Byzantine, Mining, Proof of Work (PoW), Hàm Hash, Block reward, Blockchain, Chuỗi dài nhất, Tấn công 51%, Đầu ra, Khóa đầu ra, Thay đổi, Satoshi, Khóa công khai/riêng tư, Address, Mật mã khóa công khai, Chữ ký số, Wallet


# Giới thiệu Máy chủ BTCPay


<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>


## Hiểu về màn hình đăng nhập Máy chủ BTCPay


<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>


### Làm việc với Máy chủ BTCPay


Mục tiêu của khối khóa học này là giúp bạn hiểu tổng quan về phần mềm BTCPay Server. Trong môi trường chia sẻ, bạn nên theo dõi phần trình bày của giảng viên và tham khảo Sách hướng dẫn về BTCPay Server để học cùng giảng viên. Bạn sẽ học cách tạo Wallet thông qua nhiều phương pháp. Ví dụ bao gồm thiết lập Hot, Wallet và ví phần cứng được kết nối thông qua BTCPay Server Vault. Các mục tiêu này được thực hiện trong môi trường Demo, được giảng viên trình bày và cấp quyền truy cập.


Nếu bạn tự học khóa học này, bạn có thể tìm thấy danh sách các máy chủ lưu trữ của bên thứ ba cho mục đích Demo tại https://directory.btcpayserver.org/filter/hosts. Chúng tôi khuyến cáo không nên sử dụng các tùy chọn của bên thứ ba này làm môi trường sản xuất; tuy nhiên, chúng phục vụ đúng mục đích giới thiệu việc sử dụng Bitcoin và BTCPay Server.


Là một học viên chuyên nghiệp của BTCPay Server, bạn có thể đã có kinh nghiệm thiết lập node Bitcoin. Khóa học này được thiết kế riêng cho nền tảng phần mềm BTCPay Server.


Nhiều tùy chọn trong BTCPay Server tồn tại ở dạng này hay dạng khác trong các phần mềm liên quan đến Bitcoin Wallet khác.


### Màn hình đăng nhập máy chủ BTCPay


Khi bạn được chào đón đến môi trường Demo, bạn sẽ được yêu cầu "Đăng nhập" hoặc "Tạo tài khoản". Quản trị viên máy chủ có thể tắt tính năng tạo tài khoản mới vì lý do bảo mật. Logo và màu sắc nút của Máy chủ BTCPay có thể được thay đổi vì Máy chủ BTCPay là Phần mềm Nguồn mở. Máy chủ bên thứ ba có thể gắn nhãn trắng cho phần mềm và thay đổi toàn bộ giao diện.


![image](assets/en/001.webp)


### Cửa sổ Tạo tài khoản


Để tạo tài khoản trên Máy chủ BTCPay cần phải có chuỗi Email Address hợp lệ; example@email.com sẽ là chuỗi hợp lệ cho Email.


Mật khẩu phải dài ít nhất 8 ký tự, bao gồm chữ cái, số và ký tự đặc biệt. Sau khi đặt mật khẩu một lần, bạn sẽ phải xác minh xem mật khẩu đó có giống với mật khẩu đã nhập ở ô mật khẩu đầu tiên không.


Khi cả hai trường Email và Mật khẩu đã được điền chính xác, hãy nhấp vào nút "Tạo Tài khoản". Thao tác này sẽ lưu Email và mật khẩu trên máy chủ BTCPay của giảng viên.


![image](assets/en/002.webp)


**!Ghi chú!**


Nếu bạn tự học khóa học này, việc tạo tài khoản này có thể sẽ được thực hiện trên máy chủ của bên thứ ba; do đó, chúng tôi xin nhấn mạnh lại rằng không nên sử dụng máy chủ này làm môi trường sản xuất mà chỉ dùng cho mục đích đào tạo.


### Tạo tài khoản bởi Quản trị viên máy chủ BTCPay


Quản trị viên của Phiên bản Máy chủ BTCPay cũng có thể tạo tài khoản cho Máy chủ BTCPay. Quản trị viên của Phiên bản Máy chủ BTCPay có thể nhấp vào "Cài đặt Máy chủ" (1), nhấp vào tab "Người dùng" (2) và nhấp vào nút "+ Thêm Người dùng" (3) ở góc trên bên phải của tab "Người dùng". Trong Mục tiêu (4.3), bạn sẽ tìm hiểu thêm về quyền kiểm soát của quản trị viên đối với Tài khoản.


![image](assets/en/003.webp)


Với tư cách là quản trị viên, bạn cần có Email Address của người dùng và đặt mật khẩu tiêu chuẩn. Vì lý do bảo mật, Quản trị viên nên thông báo cho người dùng thay đổi mật khẩu này trước khi sử dụng tài khoản. Nếu Quản trị viên không đặt Mật khẩu và SMTP đã được cấu hình trên máy chủ, người dùng sẽ nhận được email có liên kết mời tạo tài khoản và tự đặt mật khẩu.


### Ví dụ


Khi tham gia khóa học với giảng viên, hãy nhấp vào liên kết do giảng viên cung cấp và tạo tài khoản trên môi trường Demo. Đảm bảo email Address và mật khẩu của bạn được lưu trữ an toàn; bạn sẽ cần thông tin đăng nhập này cho các mục tiêu demo còn lại trong khóa học này.


Giảng viên của bạn có thể đã thu thập email Address trước và gửi liên kết lời mời trước bài tập này. Nếu được hướng dẫn, hãy kiểm tra email của bạn.


Khi tham gia khóa học mà không có người hướng dẫn, hãy tạo tài khoản của bạn bằng môi trường demo của BTCPay Server; hãy truy cập


https://Mainnet.demo.btcpayserver.org/login.


Tài khoản này chỉ được sử dụng cho mục đích trình diễn/đào tạo và không bao giờ được sử dụng cho mục đích kinh doanh.


### Tóm tắt kỹ năng


Trong phần này, bạn đã học những nội dung sau:



- Cách tạo tài khoản trên máy chủ lưu trữ thông qua Interface.
- Cách quản trị viên máy chủ có thể thêm người dùng theo cách thủ công vào cài đặt máy chủ.


### Đánh giá kiến thức


#### Đánh giá khái niệm KA


Đưa ra lý do tại sao sử dụng Máy chủ demo lại là một ý tưởng tồi cho mục đích sản xuất.


## Quản lý tài khoản người dùng


<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>


### Quản lý tài khoản trên máy chủ BTCPay


Sau khi chủ cửa hàng tạo tài khoản, họ có thể quản lý tài khoản ở góc dưới bên trái của giao diện máy chủ BTCPay. Bên dưới nút Tài khoản, có nhiều cài đặt cấp cao hơn.



- Chế độ Tối/Sáng.
- Ẩn nút chuyển đổi thông tin nhạy cảm.
- Quản lý tài khoản.


![image](assets/en/004.webp)


### Chế độ tối và sáng


Người dùng BTCPay Server có thể chọn giữa chế độ Sáng hoặc Tối của giao diện người dùng. Các trang dành cho khách hàng sẽ không thay đổi. Họ sử dụng cài đặt tùy chỉnh của khách hàng về chế độ tối hoặc sáng.


### Ẩn thông tin nhạy cảm Chuyển đổi


Nút Ẩn Thông tin Nhạy cảm cung cấp một giải pháp bảo mật Layer nhanh chóng và đơn giản. Bất cứ khi nào bạn cần vận hành Máy chủ BTCPay, nhưng có thể có người đang rình rập bạn ở nơi công cộng, hãy bật tính năng Ẩn Thông tin Nhạy cảm, và tất cả các giá trị trong Máy chủ BTCPay sẽ được ẩn đi. Người khác có thể nhìn qua vai bạn, nhưng không thể thấy các giá trị bạn đang xử lý nữa.


### Quản lý tài khoản


Sau khi tài khoản người dùng được tạo, đây là nơi quản lý mật khẩu, 2FA hoặc khóa API.


### Quản lý tài khoản - Tài khoản


Tùy chọn cập nhật tài khoản của bạn bằng một Email Address khác. Để đảm bảo email Address của bạn chính xác, BTCPay Server cho phép bạn gửi email xác minh. Nhấp vào lưu nếu người dùng thiết lập email Address mới và xác nhận việc xác minh đã thành công. Tên người dùng vẫn giữ nguyên như Email trước đó.


Người dùng có thể quyết định xóa toàn bộ tài khoản của mình bằng cách nhấp vào nút xóa trên tab Tài khoản.


![image](assets/en/005.webp)


**!Ghi chú!**


Sau khi thay đổi Email, tên người dùng của tài khoản sẽ không thay đổi. Email Address đã cung cấp trước đó sẽ vẫn là Tên đăng nhập.


### Quản lý tài khoản - Mật khẩu


Học viên có thể muốn thay đổi mật khẩu. Học viên có thể thực hiện việc này bằng cách vào tab Mật khẩu. Tại đây, học viên sẽ nhập mật khẩu cũ và có thể đổi sang mật khẩu mới.


![image](assets/en/006.webp)


### Xác thực hai yếu tố (2fa)


Để hạn chế hậu quả của việc đánh cắp mật khẩu, bạn có thể sử dụng xác thực hai yếu tố (2FA), một phương pháp bảo mật tương đối mới. Bạn có thể kích hoạt xác thực hai yếu tố thông qua mục Quản lý tài khoản và tab Xác thực hai yếu tố. Bạn phải hoàn tất bước thứ hai sau khi đăng nhập bằng tên người dùng và mật khẩu.


Máy chủ BTCPay hỗ trợ hai phương pháp để kích hoạt 2FA: 2FA dựa trên ứng dụng (Authy, Google, Microsoft Authenticators) hoặc thông qua các thiết bị bảo mật (FIDO2 hoặc LNURL Auth).


### Xác thực hai yếu tố - Dựa trên ứng dụng


Dựa trên Hệ điều hành của điện thoại di động (Android hoặc iOS), người dùng có thể chọn giữa các ứng dụng sau;


1. Tải xuống trình xác thực hai yếu tố.


   - Authy dành cho [Android](https://play.google.com/store/apps/details?id=com.authy.authy) hoặc [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator dành cho [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) hoặc [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator dành cho [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) hoặc [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)

2. Sau khi tải xuống và cài đặt ứng dụng Authenticator.


   - Quét mã QR do BTCPay Server cung cấp
   - Hoặc nhập thủ công khóa được BTCPay Server tạo ra vào ứng dụng Authenticator của bạn.

3. Ứng dụng Authenticator sẽ cung cấp cho bạn một mã duy nhất. Nhập mã duy nhất đó vào Máy chủ BTCPay để xác minh thiết lập và nhấp vào "Xác minh" để hoàn tất quy trình.


![image](assets/en/007.webp)


### Tóm tắt kỹ năng


Trong phần này, bạn đã học những nội dung sau:



- Các tùy chọn quản lý tài khoản và nhiều cách khác nhau để quản lý tài khoản trên phiên bản BTCPay Server.
- Cách thiết lập 2FA dựa trên ứng dụng.


### Đánh giá kiến thức


#### Đánh giá khái niệm KA


Mô tả cách 2FA dựa trên ứng dụng giúp bảo mật tài khoản của bạn.


## Tạo một cửa hàng mới


<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>


### Tạo trình hướng dẫn cửa hàng của bạn


Khi người dùng mới đăng nhập vào Máy chủ BTCPay, môi trường sẽ trống và cần một cửa hàng đầu tiên. Trình hướng dẫn giới thiệu của Máy chủ BTCPay sẽ cung cấp cho người dùng tùy chọn "Tạo cửa hàng" (1). Cửa hàng có thể được xem như một Trang chủ cho nhu cầu Bitcoin của bạn. Một Nút Máy chủ BTCPay mới sẽ bắt đầu bằng cách đồng bộ hóa Bitcoin Blockchain (2). Tùy thuộc vào cơ sở hạ tầng bạn đang chạy Máy chủ BTCPay, quá trình này có thể mất từ vài giờ đến vài ngày. Phiên bản hiện tại của phiên bản được hiển thị ở góc dưới bên phải của Giao diện người dùng Máy chủ BTCPay. Điều này rất hữu ích để tham khảo khi khắc phục sự cố.


![image](assets/en/008.webp)


### Tạo trình hướng dẫn cửa hàng của bạn


Khóa học này sẽ bắt đầu với một màn hình hơi khác so với trang trước. Vì giảng viên đã chuẩn bị môi trường Demo, Bitcoin và Blockchain đã được đồng bộ hóa trước đó, do đó, bạn sẽ không thấy trạng thái đồng bộ của các nút.


Người dùng có thể quyết định xóa toàn bộ tài khoản của mình bằng cách nhấp vào nút xóa trên tab Tài khoản.


![image](assets/en/009.webp)


**!Ghi chú!**


Tài khoản máy chủ BTCPay có thể tạo số lượng cửa hàng không giới hạn. Mỗi cửa hàng là một Wallet hoặc "nhà".


### Ví dụ


Bắt đầu bằng cách nhấp vào "Tạo cửa hàng của bạn".


![image](assets/en/010.webp)


Thao tác này sẽ tạo Trang chủ và bảng điều khiển đầu tiên của bạn để sử dụng Máy chủ BTCPay.


(1) Sau khi nhấp vào "Tạo cửa hàng", BTCPay Server sẽ yêu cầu bạn đặt tên cho cửa hàng; điều này có thể hữu ích với bạn.


![image](assets/en/011.webp)


(2) Tiếp theo, phải thiết lập loại tiền tệ lưu trữ mặc định, có thể là tiền pháp định hoặc tiền tệ có mệnh giá là Bitcoin hoặc Sats. Đối với môi trường demo, chúng tôi sẽ thiết lập là USD.


![image](assets/en/012.webp)


(3) Là tham số cuối cùng trong quá trình thiết lập cửa hàng, Máy chủ BTCPay yêu cầu bạn thiết lập "Nguồn giá ưu tiên" để so sánh giá của Bitcoin với giá tiền pháp định hiện tại, nhờ đó cửa hàng của bạn sẽ hiển thị đúng tỷ giá Exchange giữa Bitcoin và tiền pháp định do cửa hàng thiết lập. Chúng tôi sẽ giữ nguyên mặc định trong ví dụ Demo và đặt giá trị này là Kraken Exchange. Máy chủ BTCPay sử dụng API Kraken để kiểm tra tỷ giá Exchange.


![image](assets/en/013.webp)


(4) Bây giờ các tham số cửa hàng này đã được thiết lập, hãy nhấp vào nút Tạo và BTCPay Server sẽ tạo bảng điều khiển cho cửa hàng đầu tiên của bạn, nơi trình hướng dẫn sẽ tiếp tục.


![image](assets/en/014.webp)


Xin chúc mừng, bạn đã tạo được cửa hàng đầu tiên và đây là kết thúc bài tập này.


![image](assets/en/015.webp)


### Tóm tắt kỹ năng


Trong phần này, bạn đã học:



- Tạo cửa hàng và cấu hình loại tiền tệ mặc định, kết hợp với tùy chọn nguồn giá.
- Mỗi "Cửa hàng" là một ngôi nhà mới tách biệt với các cửa hàng khác trên máy chủ BTCPay này.


# Giới thiệu về Bảo mật Khóa Bitcoin


<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>


## Hiểu về thế hệ khóa Bitcoin


<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>


### Quá trình tạo khóa Bitcoin bao gồm những gì?


Ví Bitcoin, khi được tạo, sẽ tạo ra một cái gọi là "seed". Trong mục tiêu cuối cùng, bạn đã tạo ra một "seed". Chuỗi từ được tạo trước đó cũng được gọi là cụm từ Mnemonic. seed được sử dụng để tạo ra các Khóa Bitcoin riêng lẻ và được sử dụng để gửi hoặc nhận Bitcoin. Không bao giờ được chia sẻ cụm từ seed với bên thứ ba hoặc các đối tác không đáng tin cậy.


Việc tạo ra seed được thực hiện theo tiêu chuẩn công nghiệp được gọi là khuôn khổ "Xác định phân cấp" (HD).


![image](assets/en/016.webp)


### Địa chỉ


Máy chủ BTCPay được xây dựng để sử dụng generate cho Address mới. Điều này giúp giảm thiểu vấn đề tái sử dụng khóa công khai hoặc Address. Việc sử dụng cùng một khóa công khai giúp việc theo dõi toàn bộ lịch sử thanh toán của bạn trở nên rất dễ dàng. Việc coi khóa như một chứng từ sử dụng một lần sẽ cải thiện đáng kể quyền riêng tư của bạn. Chúng tôi cũng sử dụng Địa chỉ Bitcoin, vì vậy đừng nhầm lẫn chúng với Khóa công khai.


Address được lấy từ Khóa công khai thông qua "thuật toán băm". Tuy nhiên, hầu hết các ví và giao dịch sẽ hiển thị Địa chỉ thay vì các khóa công khai đó. Địa chỉ thường ngắn hơn khóa công khai và thường bắt đầu bằng `1`, `3` hoặc `bc1`, trong khi khóa công khai bắt đầu bằng `02`, `03` hoặc `04`.



- Địa chỉ bắt đầu bằng `1.....` vẫn là những địa chỉ rất phổ biến. Như đã đề cập trong chương "Tạo kho lưu trữ mới", đây là những địa chỉ cũ. Kiểu Address này dành cho các giao dịch P2PKH. P2Pkh sử dụng mã hóa Base58, khiến Address phân biệt chữ hoa chữ thường. Cấu trúc của nó dựa trên khóa công khai với một chữ số bổ sung làm mã định danh.



- Các địa chỉ bắt đầu bằng `bc1...` đang dần được chuyển sang các địa chỉ rất phổ biến. Chúng được gọi là Địa chỉ SegWit (gốc). Chúng cung cấp cấu trúc phí tốt hơn so với các địa chỉ đã đề cập khác. Địa chỉ SegWit gốc sử dụng mã hóa Bech32 và chỉ cho phép chữ thường.



- Địa chỉ bắt đầu bằng `3...` vẫn thường được các sàn giao dịch sử dụng làm địa chỉ gửi tiền. Những địa chỉ này được đề cập trong chương "Tạo kho lưu trữ mới", bao gồm các địa chỉ SegWit dạng đóng gói hoặc lồng nhau. Tuy nhiên, chúng cũng có thể hoạt động như "Multisig Address". Khi được sử dụng như SegWit Address, phí giao dịch sẽ được tiết kiệm, nhưng vẫn ít hơn so với SegWit gốc. Địa chỉ P2SH sử dụng mã hóa Base58. Điều này khiến nó phân biệt chữ hoa chữ thường, giống như Address cũ.



- Địa chỉ bắt đầu bằng `2...` là địa chỉ Testnet. Chúng được thiết kế để nhận Testnet Bitcoin (tBTC). Bạn không bao giờ nên nhầm lẫn và gửi Bitcoin đến các địa chỉ này. Để phát triển, bạn có thể generate thành Testnet Wallet. Có nhiều vòi trực tuyến để lấy Testnet Bitcoin. Đừng bao giờ mua Testnet Bitcoin. Testnet Bitcoin được đào. Đây có thể là lý do khiến các nhà phát triển sử dụng Regtest thay thế. Đây là một môi trường sân chơi cho các nhà phát triển, thiếu một số thành phần mạng nhất định. Tuy nhiên, Bitcoin rất hữu ích cho mục đích phát triển.


### Khóa công khai


Khóa công khai ngày nay ít được sử dụng hơn trong thực tế. Theo thời gian, người dùng Bitcoin đã dần thay thế chúng bằng Địa chỉ. Chúng vẫn tồn tại và đôi khi vẫn được sử dụng. Khóa công khai nhìn chung là những chuỗi dài hơn nhiều so với địa chỉ. Giống như địa chỉ, chúng bắt đầu bằng một mã định danh cụ thể.



- Đầu tiên, `02...` và `03...` là các mã định danh khóa công khai rất chuẩn được mã hóa theo định dạng SEC. Chúng có thể được xử lý và chuyển thành địa chỉ để nhận, dùng để tạo địa chỉ multi-sig hoặc để xác minh chữ ký. Các giao dịch Bitcoin ban đầu sử dụng khóa công khai như một phần của giao dịch P2PK.



- Tuy nhiên, ví HD sử dụng một cấu trúc khác. `xpub...`, `ypub...` hoặc `zpub...` được gọi là khóa công khai mở rộng, hay xpub. Các khóa này được sử dụng để tạo ra nhiều khóa công khai khác nhau như một phần của HD Wallet. Vì xpub lưu trữ toàn bộ lịch sử giao dịch của bạn, tức là các giao dịch trong quá khứ và tương lai, nên đừng bao giờ chia sẻ chúng với các bên không đáng tin cậy.


### Tóm tắt kỹ năng


Trong phần này, bạn đã học những nội dung sau:



- Sự khác biệt giữa địa chỉ và kiểu dữ liệu khóa công khai cũng như lợi ích của việc sử dụng địa chỉ thay vì khóa công khai.


### Đánh giá kiến thức


Mô tả lợi ích của việc sử dụng địa chỉ mới cho mỗi giao dịch so với phương pháp sử dụng lại Address hoặc phương pháp khóa công khai.


## Bảo mật chìa khóa bằng Hardware Wallet


<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>


### Lưu trữ Khóa Bitcoin


Sau khi tạo cụm từ seed, danh sách 12 - 24 từ được tạo trong sách này cần được sao lưu và bảo mật phù hợp, vì những từ này là cách duy nhất để khôi phục quyền truy cập vào Wallet. Cấu trúc của ví HD và cách nó tạo địa chỉ một cách xác định bằng một seed duy nhất có nghĩa là tất cả các địa chỉ bạn đã tạo sẽ được sao lưu bằng danh sách các từ Mnemonic này, đại diện cho seed hoặc cụm từ khôi phục của bạn.


Hãy giữ cụm từ khôi phục của bạn an toàn. Nếu bị ai đó truy cập, đặc biệt là với mục đích xấu, họ có thể di chuyển tiền của bạn. Hãy giữ cho seed an toàn và bảo mật, đồng thời lưu ý rằng việc này là quyền lợi chung của cả hai bên. Có một số phương pháp lưu trữ khóa riêng tư Bitcoin, mỗi phương pháp đều có những ưu và nhược điểm riêng về mặt bảo mật, quyền riêng tư, sự tiện lợi và lưu trữ vật lý. Do tầm quan trọng của khóa riêng tư, người dùng Bitcoin có xu hướng lưu trữ và bảo quản an toàn các khóa này trong "kho lưu trữ tự quản" thay vì sử dụng các dịch vụ "lưu trữ" như ngân hàng. Tùy thuộc vào người dùng, họ phải sử dụng giải pháp lưu trữ Cold hoặc Hot Wallet.


### Lưu trữ khóa Hot và Cold của Bitcoin


Thông thường, ví Bitcoin được định danh bằng Hot Wallet hoặc Cold Wallet. Hầu hết các đánh đổi đều nằm ở sự tiện lợi, dễ sử dụng và rủi ro bảo mật. Mỗi phương pháp này cũng có thể được thấy trong giải pháp lưu ký. Tuy nhiên, những đánh đổi ở đây chủ yếu dựa trên bảo mật và quyền riêng tư, và nằm ngoài phạm vi của khóa học này.


### Hot Wallet


Ví Hot là cách thuận tiện nhất để tương tác với Bitcoin thông qua phần mềm di động, web hoặc máy tính để bàn. Wallet luôn được kết nối với internet, cho phép người dùng gửi hoặc nhận Bitcoin. Tuy nhiên, đây cũng là điểm yếu của nó; vì luôn trực tuyến, Wallet giờ đây dễ bị tin tặc hoặc phần mềm độc hại tấn công hơn trên thiết bị của bạn. Trong BTCPay Server, ví Hot lưu trữ khóa riêng trên phiên bản. Bất kỳ ai truy cập vào kho BTCPay Server của bạn đều có khả năng đánh cắp tiền từ Address này nếu họ có ý đồ xấu. Khi BTCPay Server chạy trong môi trường được lưu trữ, bạn nên luôn cân nhắc điều này trong hồ sơ bảo mật của mình và tốt nhất là không sử dụng Hot Wallet trong trường hợp như vậy. Khi BTCPay Server được cài đặt trên phần cứng do bạn sở hữu và bảo mật, hồ sơ rủi ro sẽ giảm đáng kể, nhưng không bao giờ biến mất hoàn toàn.


### Cold Wallet


Người dùng thường chuyển Bitcoin của mình sang Cold vì nó có thể cô lập khóa riêng tư khỏi internet, do đó bảo vệ họ khỏi các mối đe dọa trực tuyến tiềm ẩn. Việc ngắt kết nối internet giúp giảm thiểu nguy cơ phần mềm độc hại, phần mềm gián điệp và việc hoán đổi SIM. Bộ nhớ Cold được cho là vượt trội hơn Hot về mặt bảo mật và quyền tự chủ, miễn là thực hiện các biện pháp phòng ngừa đầy đủ để tránh mất khóa riêng tư Bitcoin. Bộ nhớ Cold phù hợp nhất cho số lượng lớn Bitcoin, vốn không được sử dụng thường xuyên do thiết lập Wallet khá phức tạp.


Có nhiều phương pháp lưu trữ khóa Bitcoin trong bộ nhớ Cold, từ ví giấy đến ví não, ví phần cứng, hoặc ngay từ đầu là tệp Wallet. Hầu hết các ví đều sử dụng cụm từ BIP đến generate. Tuy nhiên, trong phần mềm Bitcoin core, vẫn chưa có sự đồng thuận về việc sử dụng nó. Phần mềm Bitcoin core vẫn sẽ lưu trữ tệp Wallet.dat, tệp này cần được lưu trữ ở một vị trí ngoại tuyến an toàn.


### Tóm tắt kỹ năng


Trong phần này, bạn đã học:



- Sự khác biệt giữa ví Hot và Cold về mặt chức năng và sự đánh đổi của chúng.


### Đánh giá kiến thức Đánh giá khái niệm



- Wallet là gì?



- Sự khác biệt giữa ví Hot và Cold là gì?



- Hãy mô tả ý nghĩa của cụm từ "tạo ra Wallet"?


## Sử dụng phím Bitcoin của bạn


<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>


### Máy chủ BTCPay Wallet


Máy chủ BTCPay bao gồm các tính năng Wallet tiêu chuẩn sau:



- Giao dịch
- Gửi
- Nhận được
- Quét lại
- Kéo thanh toán
- Thanh toán
- PSBT
- Cài đặt chung


### Giao dịch


Quản trị viên có thể xem các giao dịch đến và đi của On-Chain và Wallet được kết nối với cửa hàng cụ thể này trong chế độ xem giao dịch. Mỗi giao dịch có sự phân biệt giữa số tiền đã nhận và đã gửi. Giao dịch đã nhận sẽ là Green, và giao dịch đã gửi sẽ có màu đỏ. Trong chế độ xem giao dịch của Máy chủ BTCPay, quản trị viên cũng sẽ thấy một bộ nhãn tiêu chuẩn.


| Transaction Type | Description                                          |
| ---------------- | ---------------------------------------------------- |
| App              | Payment was received through an app-created invoice  |
| invoice          | Payment was received through an invoice              |
| payjoin          | Not paid, invoice timer still has not expired        |
| payjoin-exposed  | UTXO was exposed through an invoice payjoin proposal |
| payment-request  | Payment was received through a payment request       |
| payout           | Payment was sent through a payout or refund          |

### Cách gửi


Chức năng gửi của máy chủ BTCPay sẽ gửi giao dịch từ Máy chủ BTCPay On-Chain Wallet của bạn. Máy chủ BTCPay cho phép nhiều cách ký giao dịch để chi tiêu tiền. Giao dịch có thể được ký bằng:



- Hardware Wallet
- Ví hỗ trợ PSBT
- Khóa riêng tư HD hoặc hạt giống phục hồi.
- Hot Wallet


#### Hardware Wallet


Máy chủ BTCPay được tích hợp sẵn hỗ trợ Hardware Wallet, cho phép bạn sử dụng Hardware Wallet với BTCPay Vault mà không lo rò rỉ thông tin cho các ứng dụng hoặc máy chủ của bên thứ ba. Việc tích hợp Hardware Wallet trong Máy chủ BTCPay cho phép bạn nhập Hardware Wallet và chi tiêu số tiền nhận được chỉ với một xác nhận đơn giản trên thiết bị. Khóa riêng tư của bạn sẽ không bao giờ rời khỏi thiết bị, và tất cả số tiền đều được xác thực với Full node, đảm bảo không bị rò rỉ dữ liệu.


#### Ký kết với Wallet hỗ trợ PSBT


PSBT (Giao dịch Bitcoin đã ký một phần) là định dạng trao đổi cho các giao dịch Bitcoin vẫn cần được ký đầy đủ. PSBT được hỗ trợ trong Máy chủ BTCPay và có thể được ký bằng các ví phần cứng và phần mềm tương thích.


Việc xây dựng giao dịch Bitcoin được ký kết đầy đủ trải qua các bước sau:



- PSBT được xây dựng với các đầu vào và đầu ra cụ thể, nhưng không có chữ ký
- PSBT đã xuất có thể được nhập vào bằng Wallet hỗ trợ định dạng này
- Dữ liệu giao dịch có thể được kiểm tra và ký bằng Wallet
- Tệp PSBT đã ký được xuất từ Wallet và nhập bằng Máy chủ BTCPay
- Máy chủ BTCPay tạo ra giao dịch Bitcoin cuối cùng
- Bạn xác minh kết quả và phát nó lên mạng


#### Ký bằng Khóa riêng HD hoặc Mnemonic seed


Nếu bạn đã tạo Wallet trước khi sử dụng Máy chủ BTCPay, bạn có thể chi tiêu tiền bằng cách nhập khóa riêng vào trường thích hợp. Hãy thiết lập "AccountKeyPath" phù hợp trong Wallet> Cài đặt; nếu không, bạn sẽ không thể chi tiêu.


#### Ký kết với Hot Wallet


Nếu bạn tạo Wallet mới khi thiết lập cửa hàng và kích hoạt nó làm Hot Wallet, nó sẽ tự động sử dụng seed được lưu trữ trên máy chủ để ký.


### RBF (Replace-by-fee)


Replace-by-fee (RBF) là một tính năng của giao thức Bitcoin cho phép bạn thay thế một giao dịch đã được phát sóng trước đó (khi vẫn chưa được xác nhận). Tính năng này cho phép ngẫu nhiên hóa dấu vân tay giao dịch của Wallet hoặc thay thế bằng mức phí cao hơn để đưa giao dịch lên vị trí ưu tiên cao hơn trong hàng đợi xác nhận (Mining). Điều này sẽ thay thế hiệu quả giao dịch gốc vì mức phí cao hơn sẽ được ưu tiên, và sau khi được xác nhận, giao dịch gốc sẽ không còn hiệu lực (không bị chi tiêu trùng lặp).


Nhấn nút "Cài đặt nâng cao" để xem các tùy chọn của RBF.


![image](assets/en/017.webp)



- Ngẫu nhiên hóa để tăng tính riêng tư, cho phép tự động thay thế giao dịch để ngẫu nhiên hóa dấu vân tay giao dịch.
- Có, đánh dấu giao dịch cho RBF và được thay thế rõ ràng (Không thay thế theo mặc định, chỉ thay thế theo đầu vào)
- Không, không cho phép thay thế giao dịch.


### Lựa chọn Coin


Lựa chọn Coin là một tính năng nâng cao bảo mật, cho phép bạn chọn loại tiền bạn muốn chi tiêu khi thực hiện giao dịch. Ví dụ: thanh toán bằng tiền mới từ hỗn hợp tiền xu.


Tính năng chọn Coin hoạt động trực tiếp với tính năng dán nhãn Wallet. Tính năng này cho phép bạn dán nhãn các khoản tiền thu vào để quản lý và chi tiêu UTXO dễ dàng hơn.


Máy chủ BTCPay hỗ trợ BIP-329 để quản lý nhãn. Nếu bạn chuyển từ máy chủ Wallet hỗ trợ BIP-329 và đã thiết lập nhãn, Máy chủ BTCPay sẽ tự động nhận dạng và nhập chúng. Khi di chuyển máy chủ, thông tin này cũng có thể được xuất và nhập vào môi trường mới.


### Làm thế nào để nhận được


Khi nhấp vào nút nhận trên Máy chủ BTCPay, hệ thống sẽ tạo ra một mã Address chưa sử dụng, có thể dùng để nhận thanh toán. Quản trị viên cũng có thể generate một mã Address mới bằng cách tạo một mã “Invoice” mới.


Máy chủ BTCPay sẽ luôn nhắc bạn nhập generate vào Address khả dụng sau đây để tránh việc tái sử dụng Address. Sau khi nhấp vào "generate BTC khả dụng tiếp theo Address", Máy chủ BTCPay sẽ tạo một Address và mã QR mới. Nó cũng cho phép bạn trực tiếp đặt Nhãn cho Address để quản lý địa chỉ của bạn tốt hơn.


![image](assets/en/018.webp)


![image](assets/en/019.webp)


#### Quét lại


Tính năng Quét lại dựa trên "Scantxoutset" của Bitcoin core 0.17.0 để quét trạng thái hiện tại của Blockchain (gọi là Bộ UTXO) để tìm các đồng tiền thuộc sơ đồ phái sinh đã được cấu hình. Quét lại Wallet giải quyết hai vấn đề phổ biến mà người dùng Máy chủ BTCPay thường gặp phải.


1. Vấn đề giới hạn khoảng cách - Hầu hết các ví của bên thứ ba là ví nhẹ chia sẻ một nút giữa nhiều người dùng. Ví nhẹ và ví dựa trên Full node giới hạn số lượng (thường là 20) địa chỉ không có số dư mà chúng theo dõi trên Blockchain để ngăn chặn các vấn đề về hiệu suất. Máy chủ BTCPay tạo một Address mới cho mỗi Invoice. Với những điều trên, sau khi Máy chủ BTCPay tạo 20 hóa đơn chưa thanh toán liên tiếp, Wallet bên ngoài sẽ ngừng tìm nạp các giao dịch, giả sử không có giao dịch mới nào xảy ra. Wallet bên ngoài của bạn sẽ không hiển thị chúng sau khi các hóa đơn được thanh toán vào ngày 21, 22, v.v. Mặt khác, về mặt nội bộ, Máy chủ BTCPay Wallet theo dõi bất kỳ Address nào mà nó tạo ra, cùng với giới hạn khoảng cách cao hơn đáng kể. Nó không dựa vào bên thứ ba và luôn có thể hiển thị số dư chính xác.

2. Giải pháp giới hạn khoảng cách - Nếu [Wallet bên ngoài/hiện có](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-Wallet) của bạn cho phép cấu hình giới hạn khoảng cách, cách khắc phục dễ dàng là tăng giới hạn này. Tuy nhiên, phần lớn các ví không cho phép điều này. Các ví duy nhất hiện hỗ trợ cấu hình giới hạn khoảng cách mà chúng tôi biết là Electrum, Wasabi và Sparrow wallet. Thật không may, bạn có thể gặp phải sự cố với nhiều ví khác. Để có trải nghiệm người dùng và quyền riêng tư tốt nhất, hãy cân nhắc sử dụng Wallet nội bộ của Máy chủ BTCPay thay vì ví bên ngoài.


#### Máy chủ BTCPay sử dụng “mempoolfullrbf=1”


Máy chủ BTCPay sử dụng "mempoolfullrbf=1"; chúng tôi đã thêm tùy chọn này làm mặc định cho thiết lập Máy chủ BTCPay của bạn. Tuy nhiên, chúng tôi cũng đã thiết lập tính năng này thành một tính năng mà bạn có thể tự tắt. Nếu không có "mempoolfullrbf=1", nếu khách hàng chi tiêu hai lần một khoản thanh toán với giao dịch không báo hiệu RBF, Nhà cung cấp sẽ chỉ biết sau khi xác nhận.


Quản trị viên có thể muốn từ chối cài đặt này. Bạn có thể thay đổi cài đặt mặc định bằng chuỗi sau.


```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCL UDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i
```


### Cài đặt máy chủ BTCPay Wallet


Cài đặt Wallet trong Máy chủ BTCPay cung cấp tổng quan rõ ràng và súc tích về các thiết lập chung của Wallet. Tất cả các thiết lập này đều được điền sẵn nếu Wallet được tạo bằng Máy chủ BTCPay.


![image](assets/en/020.webp)


Cài đặt Wallet trong Máy chủ BTCPay cung cấp tổng quan rõ ràng và súc tích về cài đặt chung của Wallet. Tất cả các cài đặt này đều được điền sẵn nếu Wallet được tạo bằng Máy chủ BTCPay. Cài đặt Wallet của Máy chủ BTCPay bắt đầu bằng trạng thái Wallet. Đây là Chỉ xem hay Hot Wallet? Tùy thuộc vào loại Wallet, các hành động có thể khác nhau, bao gồm quét lại Wallet để tìm các giao dịch bị thiếu, xóa các giao dịch cũ khỏi lịch sử, đăng ký Wallet cho các liên kết thanh toán hoặc thay thế và xóa Wallet hiện tại được đính kèm vào cửa hàng. Trong cài đặt Wallet của Máy chủ BTCPay, quản trị viên có thể đặt Nhãn cho Wallet để quản lý Wallet tốt hơn. Tại đây, Quản trị viên cũng có thể xem Sơ đồ dẫn xuất, khóa tài khoản (xpub), Dấu vân tay và Đường dẫn khóa. Thanh toán trong cài đặt Wallet chỉ có hai cài đặt chính. Thanh toán sẽ không hợp lệ nếu giao dịch không được xác nhận trong vòng (số phút đã đặt) sau khi Invoice hết hạn. Invoice được coi là đã được xác nhận khi giao dịch thanh toán có X số lần xác nhận. Quản trị viên cũng có thể thiết lập nút chuyển đổi để hiển thị phí đề xuất trên màn hình thanh toán hoặc đặt mục tiêu xác nhận thủ công theo số khối.


![image](assets/en/021.webp)


**!Ghi chú!**


Nếu bạn tự học khóa học này, việc tạo tài khoản này có thể sẽ được thực hiện trên máy chủ của bên thứ ba. Do đó, chúng tôi một lần nữa khuyến nghị bạn không nên sử dụng những máy chủ này làm môi trường sản xuất mà chỉ nên dùng cho mục đích đào tạo.


### Ví dụ


#### Thiết lập Bitcoin Wallet trong Máy chủ BTCPay


Máy chủ BTCPay cung cấp hai phương pháp để thiết lập Wallet. Một là nhập Bitcoin Wallet hiện có. Việc nhập có thể được thực hiện bằng cách kết nối Hardware Wallet, nhập tệp Wallet, nhập khóa công khai mở rộng, quét mã QR của Wallet, hoặc, ít nhất là nhập thủ công seed khôi phục Wallet đã tạo trước đó. Trong Máy chủ BTCPay, bạn cũng có thể tạo Wallet mới. Có hai cách để cấu hình Máy chủ BTCPay khi tạo Wallet mới.


Tùy chọn Hot Wallet trong Máy chủ BTCPay cho phép các tính năng như 'PayJoin' hoặc 'Liquid'. Tuy nhiên, có một nhược điểm: mã seed khôi phục được tạo cho mã Wallet này sẽ được lưu trữ trên máy chủ, nơi bất kỳ ai có quyền quản trị đều có thể truy cập. Vì khóa riêng của bạn được lấy từ mã seed khôi phục, kẻ xấu có thể truy cập vào tài khoản hiện tại và tương lai của bạn!


Để giảm thiểu rủi ro này trên Máy chủ BTCPay, Quản trị viên có thể đặt giá trị trong mục Cài đặt Máy chủ > Chính sách > "Cho phép người dùng không phải quản trị viên tạo ví Hot cho cửa hàng của họ" thành "không", vì đây là giá trị mặc định. Để tăng cường bảo mật cho các ví Hot này, quản trị viên máy chủ nên bật xác thực 2 yếu tố (2FA) trên các tài khoản được phép sở hữu ví Hot. Việc lưu trữ khóa riêng trên máy chủ công cộng là một hành vi nguy hiểm và tiềm ẩn nhiều rủi ro. Một số rủi ro tương tự như rủi ro Lightning Network (xem chương tiếp theo về rủi ro Lightning Network).


Tùy chọn thứ hai mà BTCPay Server cung cấp để tạo Wallet mới là tạo Watch-only wallet. BTCPay Server sẽ generate khóa riêng của bạn một lần. Sau khi người dùng xác nhận đã ghi lại Cụm từ seed, BTCPay Server sẽ xóa khóa riêng khỏi máy chủ. Kết quả là, cửa hàng của bạn hiện đã có Watch-only wallet được kết nối. Để chi tiêu số tiền nhận được trên Watch-only wallet, hãy xem chương Cách gửi, bằng cách sử dụng BTCPay Server Vault, PSBT (Partially Signed Bitcoin Transaction), hoặc, ít được khuyến khích nhất, hãy tự cung cấp cụm từ seed của bạn.


Bạn đã tạo một 'Cửa hàng' mới ở phần trước. Trình hướng dẫn cài đặt sẽ tiếp tục bằng cách yêu cầu "Thiết lập Wallet" hoặc "Thiết lập nút Lightning". Trong ví dụ này, bạn sẽ làm theo quy trình hướng dẫn "Thiết lập Wallet" (1).


![image](assets/en/022.webp)


Sau khi nhấp vào "Thiết lập Wallet", trình hướng dẫn sẽ tiếp tục bằng cách yêu cầu bạn chọn cách tiếp tục; Máy chủ BTCPay hiện cung cấp tùy chọn kết nối Wallet hiện có với cửa hàng mới của bạn. Nếu bạn không có Wallet, Máy chủ BTCPay đề xuất tạo một Wallet mới. Ví dụ này sẽ làm theo các bước để "tạo Wallet mới" (2). Hãy làm theo các bước để tìm hiểu cách "Kết nối Wallet hiện có" (1).


![image](assets/en/023.webp)


**!Ghi chú!**


Nếu bạn học khóa học này trên lớp, xin lưu ý rằng ví dụ hiện tại và seed chúng tôi tạo ra chỉ nhằm mục đích giáo dục. Không bao giờ nên có bất kỳ lượng kiến thức đáng kể nào khác ngoài những kiến thức bắt buộc trong suốt các bài tập về địa chỉ này.


(1) Tiếp tục trình hướng dẫn “Wallet mới” bằng cách nhấp vào nút “Tạo Wallet mới”.


![image](assets/en/024.webp)


(2) Sau khi nhấp vào “Tạo Wallet mới”, cửa sổ tiếp theo trong trình hướng dẫn sẽ hiển thị các tùy chọn “Hot Wallet” và “Watch-only wallet”. Nếu bạn làm theo hướng dẫn của giảng viên, môi trường của bạn là một bản Demo dùng chung và bạn chỉ có thể tạo một Watch-only wallet. Lưu ý sự khác biệt giữa hai hình bên dưới. Khi bạn đang ở trong môi trường Demo, làm theo hướng dẫn của giảng viên, hãy tạo một "Watch-only wallet" và tiếp tục với trình hướng dẫn "Wallet mới".


![image](assets/en/025.webp)


![image](assets/en/026.webp)


(3) Tiếp tục trình hướng dẫn Wallet mới, giờ bạn đang ở phần Tạo BTC Watch-only wallet. Tại đây, chúng ta sẽ thiết lập "loại Address" cho Wallet. Máy chủ BTCPay cho phép bạn chọn loại Address mong muốn; tại thời điểm viết khóa học này, chúng tôi vẫn khuyến nghị sử dụng địa chỉ bech32. Bạn có thể tìm hiểu thêm về địa chỉ trong chương đầu tiên của phần này.



- SegWit (bech32)
  - Địa chỉ SegWit gốc bắt đầu bằng `bc1q`.
  - Ví dụ: `bc1qXXXXXXXXXXXXXXXXXXXXXXXX`
- Di sản
  - Địa chỉ kế thừa là địa chỉ bắt đầu bằng số `1`.
  - Ví dụ: `15e15hXXXXXXXXXXXXXXXXXXXXX`
- Taproot (Dành cho người dùng nâng cao)
  - Địa chỉ Taproot bắt đầu bằng `bc1p`.
  - Ví dụ: `bc1pXXXXXXXXXXXXXXXXXXXXXXXX`
- SegWit được bọc
  - Địa chỉ được gói theo SegWit bắt đầu bằng `3`.
  - Ví dụ: `37BBXXXXXXXXXXXXXXX`


Chọn SegWit (khuyến nghị) làm loại Wallet Address bạn ưa thích.


![image](assets/en/027.webp)


(4) Khi thiết lập tham số cho Wallet, Máy chủ BTCPay cho phép người dùng thiết lập passphrase tùy chọn thông qua BIP39; hãy đảm bảo xác nhận mật khẩu của bạn.


![image](assets/en/028.webp)


(5) Sau khi thiết lập loại Address của Wallet và có thể thiết lập một số tùy chọn nâng cao, hãy nhấp vào Tạo, và Máy chủ BTCPay sẽ tạo generate cho Wallet mới của bạn. Lưu ý rằng đây là bước cuối cùng trước khi tạo cụm từ seed. Đảm bảo bạn chỉ thực hiện việc này trong môi trường mà người khác không thể đánh cắp cụm từ seed bằng cách nhìn vào màn hình của bạn.


![image](assets/en/029.webp)


(6) Trong màn hình tiếp theo của trình hướng dẫn, Máy chủ BTCPay hiển thị cụm từ seed Khôi phục cho Wallet mới tạo của bạn; đây là các khóa để khôi phục Wallet và ký giao dịch. Máy chủ BTCPay tạo một cụm từ seed gồm 12 từ. Các từ này sẽ bị xóa khỏi máy chủ sau màn hình thiết lập này. Wallet này cụ thể là Watch-only wallet. Khuyến cáo không nên lưu trữ cụm từ seed này dưới dạng kỹ thuật số hoặc ảnh chụp. Người dùng chỉ có thể tiếp tục trong trình hướng dẫn nếu họ chủ động xác nhận rằng họ đã ghi lại cụm từ seed của mình.


![image](assets/en/030.webp)


(7) Sau khi nhấp vào Hoàn tất và bảo mật cụm từ Bitcoin seed mới được tạo, Máy chủ BTCPay sẽ cập nhật cửa hàng của bạn với Wallet mới được đính kèm và sẵn sàng nhận thanh toán. Trong Người dùng Interface, trong menu điều hướng bên trái, hãy chú ý cách Bitcoin hiện được tô sáng và kích hoạt trong Wallet.


![image](assets/en/031.webp)


### Ví dụ: Viết ra cụm từ seed


Đây là thời điểm đặc biệt an toàn để sử dụng Bitcoin. Như đã đề cập trước đó, chỉ bạn mới có quyền truy cập hoặc hiểu biết về cụm từ seed của mình. Khi bạn học cùng giảng viên và lớp học, seed được tạo ra chỉ nên được sử dụng trong khóa học này. Có quá nhiều yếu tố, bao gồm sự tò mò của bạn cùng lớp, hệ thống không an toàn, v.v., khiến những khóa này chỉ mang tính chất giáo dục và không đáng tin cậy. Tuy nhiên, các khóa được tạo ra vẫn nên được lưu trữ để làm ví dụ cho khóa học.


Phương pháp đầu tiên chúng tôi sẽ sử dụng trong tình huống này, cũng là phương pháp kém an toàn nhất, là viết lại cụm từ seed theo đúng thứ tự. Thẻ cụm từ seed có trong tài liệu khóa học được cung cấp cho học viên hoặc có thể tìm thấy trên GitHub của Máy chủ BTCPay. Chúng tôi sẽ sử dụng thẻ này để viết lại các từ được tạo ra ở bước trước. Hãy đảm bảo viết lại chúng theo đúng thứ tự. Sau khi viết xong, hãy kiểm tra lại với thứ tự được cung cấp bởi phần mềm để đảm bảo bạn đã viết đúng thứ tự. Sau khi viết xong, hãy nhấp vào hộp kiểm cho biết bạn đã viết lại cụm từ seed đúng cách.


### Ví dụ: Lưu trữ cụm từ seed trên Hardware Wallet


Trong khóa học này, chúng ta sẽ tìm hiểu về việc lưu trữ cụm từ seed trên Hardware Wallet. Việc học cùng giảng viên đôi khi có thể bao gồm một thiết bị như vậy. Trong khóa học, tài liệu hướng dẫn đã tổng hợp danh sách các ví phần cứng phù hợp cho bài tập này.


Trong ví dụ này, chúng tôi sẽ sử dụng kho lưu trữ BTCPay Server và Blockstream Jade Hardware Wallet.


Bạn cũng có thể làm theo hướng dẫn bằng video về cách kết nối Hardware Wallet.

:::video id=8e61664b-e0c0-416d-8ef9-b631bf28ec4d:::

Tải xuống BTCPay Server Vault: https://github.com/btcpayserver/BTCPayServer.Vault/releases


Hãy đảm bảo bạn tải xuống đúng tệp cho hệ thống cụ thể của mình. Người dùng Windows nên tải xuống gói [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe), người dùng Mac nên tải xuống gói [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg), và người dùng Linux nên tải xuống [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)


Sau khi cài đặt BTCPay Server Vault, hãy khởi động phần mềm bằng cách nhấp vào biểu tượng trên Màn hình nền. Khi BTCPay Server Vault được cài đặt đúng cách và khởi động lần đầu tiên, phần mềm sẽ yêu cầu quyền sử dụng với Ứng dụng Web. Phần mềm sẽ yêu cầu cấp quyền truy cập vào Máy chủ BTCPay cụ thể mà bạn đang sử dụng. Vui lòng chấp nhận các điều kiện này. BTCPay Server Vault sẽ tìm kiếm thiết bị Phần cứng. Khi tìm thấy thiết bị, Máy chủ BTCPay sẽ nhận ra rằng Vault đang chạy và đã tải thiết bị của bạn.


**!Ghi chú!**


Không cung cấp khóa SSH hoặc tài khoản quản trị máy chủ cho bất kỳ ai khác ngoài quản trị viên khi sử dụng Hot Wallet. Bất kỳ ai có quyền truy cập vào các tài khoản này đều có thể truy cập vào tiền trong Hot Wallet.


### Tóm tắt kỹ năng


Trong phần này, bạn đã học những nội dung sau:



- Góc nhìn giao dịch của Bitcoin Wallet và các phân loại khác nhau của nó.
- Có nhiều tùy chọn khác nhau khi gửi từ Bitcoin Wallet, từ phần cứng đến ví Hot.
- Vấn đề giới hạn khoảng cách gặp phải khi sử dụng hầu hết các ví và cách khắc phục.
- Cách sử dụng generate cho Bitcoin Wallet mới trong Máy chủ BTCPay, bao gồm lưu trữ khóa trong Hardware Wallet và sao lưu cụm từ khôi phục.


Trong mục tiêu này, bạn đã học cách generate một Bitcoin Wallet mới trong Máy chủ BTCPay. Chúng ta chưa đi sâu vào cách bảo mật hoặc sử dụng các khóa đó. Trong phần tổng quan nhanh về mục tiêu này, bạn đã học cách thiết lập cửa hàng đầu tiên. Bạn đã học cách generate một cụm từ Bitcoin Recovery seed.


### Đánh giá kiến thức Ôn tập thực hành


Mô tả phương pháp tạo khóa và sơ đồ bảo mật khóa, cùng với những đánh đổi/rủi ro của sơ đồ bảo mật.


## Máy chủ BTCPay Lightning Wallet


<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>


Khi quản trị viên máy chủ cung cấp phiên bản Máy chủ BTCPay mới, họ có thể thiết lập triển khai Lightning Network, chẳng hạn như LND, Core Lightning hoặc Eclair; xem Phần Cấu hình Máy chủ BTCPay để biết hướng dẫn cài đặt chi tiết hơn.


Nếu được thực hiện theo lớp học, việc kết nối một nút Lightning với Máy chủ BTCPay của bạn sẽ hoạt động thông qua một nút Tùy chỉnh. Người dùng không phải là quản trị viên máy chủ trên Máy chủ BTCPay sẽ không thể sử dụng nút Lightning nội bộ theo mặc định. Điều này nhằm bảo vệ chủ sở hữu máy chủ khỏi bị mất tiền. Quản trị viên máy chủ có thể cài đặt một plugin để cấp quyền truy cập vào nút Lightning của họ thông qua LNBank; điều này nằm ngoài phạm vi của cuốn sách này. Để biết thêm thông tin về LNBank, vui lòng tham khảo trang plugin chính thức.


### Kết nối nút nội bộ (quản trị viên máy chủ)


Quản trị viên Máy chủ có thể sử dụng Lightning Node nội bộ của Máy chủ BTCPay. Bất kể triển khai Lightning nào, việc kết nối với Lightning Node nội bộ đều giống nhau.


Truy cập kho lưu trữ thiết lập trước đó và nhấp vào "Lightning" Wallet trong menu bên trái. Máy chủ BTCPay cung cấp hai tùy chọn thiết lập: sử dụng nút Nội bộ (mặc định chỉ dành cho Quản trị viên Máy chủ) hoặc nút tùy chỉnh (kết nối bên ngoài). Quản trị viên máy chủ có thể nhấp vào tùy chọn "Sử dụng nút nội bộ". Không cần cấu hình thêm. Nhấp vào nút "Lưu" và chú ý thông báo "Nút BTC Lightning đã được cập nhật". Kho lưu trữ hiện đã có chức năng Lightning Network thành công.


### Kết nối nút bên ngoài (người dùng máy chủ/chủ cửa hàng)


Theo mặc định, chủ cửa hàng không được phép sử dụng Lightning Node của quản trị viên máy chủ. Kết nối cần được thực hiện với một node bên ngoài, có thể là node do chủ cửa hàng sở hữu trước khi thiết lập Máy chủ BTCPay, plugin LNBank nếu được quản trị viên máy chủ cung cấp, hoặc giải pháp lưu ký như Alby.


Truy cập cửa hàng đã thiết lập trước đó và nhấp vào "Lightning" bên dưới mục ví trong menu bên trái. Vì chủ cửa hàng không được phép sử dụng nút nội bộ theo mặc định, tùy chọn này sẽ bị mờ đi. Sử dụng nút tùy chỉnh là tùy chọn duy nhất khả dụng theo mặc định cho chủ cửa hàng.


Máy chủ BTCPay yêu cầu thông tin kết nối; giải pháp được thiết kế sẵn (hoặc giải pháp lưu ký) sẽ cung cấp thông tin này được thiết kế riêng cho việc triển khai Lightning. Trong Máy chủ BTCPay, chủ Cửa hàng có thể sử dụng các kết nối sau:



- C-lightning thông qua TCP hoặc Unixdomainsocketconnection.
- Sạc Lightning qua HTTPS
- Eclair qua HTTPS
- LND thông qua proxy REST
- LNDhub thông qua REST API


![image](assets/en/032.webp)


Nhấp vào "Kiểm tra kết nối" để đảm bảo bạn đã nhập đúng thông tin kết nối. Sau khi xác nhận kết nối tốt, hãy nhấp vào "Lưu" và Máy chủ BTCPay sẽ hiển thị cửa hàng đã được cập nhật Lightning Node.


### Quản lý nút Lightning nội bộ LND (Quản trị viên máy chủ)


Sau khi kết nối Lightning Node nội bộ, người quản trị máy chủ sẽ thấy các ô mới trên Bảng điều khiển dành riêng cho thông tin Lightning.



- Cân bằng sét
- BTC trong các kênh
  - Kênh mở cửa của BTC
  - Số dư BTC cục bộ
  - Số dư từ xa BTC
  - Kênh đóng BTC
- BTC On-Chain
  - BTC đã xác nhận
  - BTC chưa được xác nhận
  - BTC được bảo lưu
- Dịch vụ sét
  - Cưỡi Tia Chớp (RTL).


Bằng cách nhấp vào Logo Ride the Lightning trong ô "Dịch vụ Lightning" hoặc "Lightning" bên dưới ví ở menu bên trái, quản trị viên máy chủ có thể truy cập RTL để quản lý nút Lightning.


**Ghi chú!**


Kết nối Lightning Node nội bộ không thành công - Nếu kết nối nội bộ không thành công, hãy xác nhận:


1. Nút Bitcoin On-Chain được đồng bộ hóa hoàn toàn

2. Nút Lightning nội bộ được "Bật" trong "Lightning" > "Cài đặt" > "Cài đặt Lightning BTC"


Nếu bạn không thể kết nối với nút Lightning, bạn có thể thử khởi động lại máy chủ hoặc đọc thêm chi tiết trong tài liệu chính thức của BTCPay Server; https://docs.btcpayserver.org/Troubleshooting/. Bạn không thể chấp nhận thanh toán Lightning trong cửa hàng cho đến khi nút Lightning của bạn hiển thị "Trực tuyến". Hãy thử kiểm tra kết nối Lightning của bạn bằng cách nhấp vào liên kết "Thông tin Nút Công khai".


### Sét Wallet


Trong tùy chọn Lightning Wallet ở thanh menu bên trái, người quản trị máy chủ sẽ dễ dàng truy cập vào RTL, Thông tin nút công khai của họ và cài đặt Lightning dành riêng cho cửa hàng Máy chủ BTCPay của họ.


#### Thông tin nút nội bộ


Quản trị viên máy chủ có thể nhấp vào thông tin nút nội bộ để xem trạng thái máy chủ (Trực tuyến/Ngoại tuyến) và chuỗi kết nối cho Clearnet hoặc Tor.


![image](assets/en/033.webp)


#### Thay đổi kết nối


Để thay đổi nút Lightning bên ngoài, hãy vào "Cài đặt Lightning" và nhấp vào "Thay đổi kết nối" (bên cạnh "Thông tin nút công khai"). Thao tác này sẽ đặt lại thiết lập hiện tại. Nhập thông tin nút mới, nhấp vào Lưu và cửa hàng sẽ cập nhật tương ứng.


![image](assets/en/034.webp)


#### Dịch vụ


Nếu quản trị viên máy chủ quyết định cài đặt nhiều dịch vụ cho triển khai Lightning, chúng sẽ được liệt kê tại đây. Với triển khai LND tiêu chuẩn, quản trị viên sẽ có Ride The Lightning (RTL) làm công cụ chuẩn để quản lý nút.


#### Cài đặt BTC Lightning Wallet


Sau khi thêm nút Lightning vào cửa hàng ở bước trước, chủ cửa hàng vẫn có thể chọn tắt nút này cho cửa hàng của mình bằng cách sử dụng nút Bật/Tắt ở đầu cài đặt Lightning.


![image](assets/en/035.webp)


#### Tùy chọn thanh toán Lightning


Chủ cửa hàng có thể thiết lập các thông số sau để nâng cao trải nghiệm Lightning cho khách hàng của mình.



- Hiển thị số tiền thanh toán Lightning theo Satoshi.
- Thêm gợi ý chuyển hướng cho các kênh riêng tư vào Lightning Invoice.
- Hợp nhất URL thanh toán/mã QR On-Chain và Lightning khi thanh toán.
- Thiết lập mẫu mô tả cho hóa đơn nhanh.


#### LNURL


Chủ cửa hàng có thể chọn sử dụng hoặc không sử dụng LNURL. URL Lightning Network, hay LNURL, là một tiêu chuẩn được đề xuất cho tương tác giữa Người trả tiền và người thụ hưởng Lightning. Nói tóm lại, LNURL là một URL được mã hóa bech32 với tiền tố LNURL. Lightning Wallet dự kiến sẽ giải mã URL, liên hệ với URL và chờ một đối tượng JSON với các hướng dẫn bổ sung, đáng chú ý nhất là một thẻ xác định hành vi của LNURL.



- Kích hoạt LNURL
- Chế độ cổ điển LNURL
  - Để tương thích với Wallet, mã hóa Bech32 (cổ điển) so với URL văn bản thuần túy (sắp ra mắt)
- Cho phép người nhận tiền đưa ra bình luận.


### Ví dụ 1


#### Kết nối với Lightning bằng nút nội bộ (Quản trị viên)


Tùy chọn này chỉ khả dụng nếu bạn là Quản trị viên của phiên bản này hoặc nếu Quản trị viên đã thay đổi cài đặt mặc định để người dùng có thể sử dụng nút sét nội bộ.


Với tư cách là quản trị viên, hãy nhấp vào Lightning Wallet trên thanh menu bên trái. Máy chủ BTCPay sẽ yêu cầu bạn chọn một trong hai tùy chọn để kết nối Lightning Node: nút nội bộ hoặc nút bên ngoài tùy chỉnh. Nhấp vào "Sử dụng nút nội bộ" rồi nhấp vào "Lưu".


#### Quản lý nút Lightning (RTL) của bạn


Sau khi kết nối với nút Lightning nội bộ, Máy chủ BTCPay sẽ cập nhật và hiển thị thông báo "Nút Lightning BTC đã được cập nhật", xác nhận rằng bạn đã kết nối Lightning với cửa hàng của mình.


Quản lý nút sét là nhiệm vụ của quản trị viên máy chủ. Việc này bao gồm:


- Quản lý giao dịch
- Quản lý thanh khoản
  - Thanh khoản đầu vào
  - Thanh khoản đầu ra
- Quản lý các đồng nghiệp và kênh
  - Đồng nghiệp được kết nối
  - Phí kênh
  - Trạng thái kênh
- Thường xuyên sao lưu trạng thái kênh.
- Kiểm tra báo cáo định tuyến
- Ngoài ra, hãy sử dụng các dịch vụ như Loop.


Toàn bộ việc quản lý nút Lightning được thực hiện theo tiêu chuẩn với RTL (giả sử bạn đang chạy trên nền tảng LND). Quản trị viên có thể nhấp vào Lightning Wallet của mình trong Máy chủ BTCPay và tìm nút để mở RTL. Bảng điều khiển chính của Máy chủ BTCPay hiện đã được cập nhật với các ô Lightning Network, bao gồm quyền truy cập nhanh vào RTL.


### Ví dụ 2


#### Kết nối với sét với Alby


Khi kết nối với người giám hộ như Alby, chủ cửa hàng trước tiên phải tạo tài khoản và truy cập https://getalby.com/


![image](assets/en/036.webp)


Sau khi tạo tài khoản Alby, hãy vào cửa hàng BTCPay Server của bạn.


Bước 1: Nhấp vào 'Thiết lập nút Lightning' trên Bảng điều khiển hoặc 'Lightning' bên dưới ví.


![image](assets/en/037.webp)


Bước 2: Nhập thông tin đăng nhập kết nối Wallet do Alby cung cấp. Trên Bảng điều khiển của Alby, nhấp vào Wallet. Tại đây, bạn sẽ tìm thấy "Thông tin đăng nhập kết nối Wallet". Sao chép thông tin đăng nhập này. Dán thông tin đăng nhập từ Alby vào trường Cấu hình kết nối trên Máy chủ BTCPay.


![image](assets/en/038.webp)


Bước 3: Sau khi cung cấp thông tin kết nối cho Máy chủ BTCPay, hãy nhấp vào nút "Kiểm tra kết nối" để đảm bảo kết nối hoạt động bình thường. Lưu ý thông báo "Kết nối đến nút Lightning thành công" ở đầu màn hình. Điều này xác nhận rằng mọi thứ đang hoạt động bình thường.


![image](assets/en/039.webp)


Bước 4: Nhấp vào "Lưu" và cửa hàng của bạn hiện đã được kết nối với nút Lightning của Alby.


![image](assets/en/040.webp)


**!Ghi chú!**


Đừng bao giờ tin tưởng vào giải pháp Lightning của đơn vị giám sát có giá trị lớn hơn mức bạn sẵn sàng mất.


### Tóm tắt kỹ năng


Trong phần này, bạn đã học:



- Cách kết nối nút Lightning bên trong hoặc bên ngoài
- Nội dung và chức năng của nhiều ô liên quan đến Lightning trong Bảng điều khiển
- Cách cấu hình Lightning Wallet bằng Voltage Surge hoặc Alby


### Đánh giá kiến thức Ôn tập thực hành


Mô tả một số tùy chọn khác nhau để kết nối Lightning Wallet với cửa hàng của bạn.


# Máy chủ BTCPay Interface


<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>


## Tổng quan về bảng điều khiển


<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>


Máy chủ BTCPay là một gói phần mềm dạng mô-đun. Tuy nhiên, có những tiêu chuẩn mà mọi Máy chủ BTCPay phải tuân thủ, và những tiêu chuẩn này sẽ chi phối tương tác giữa Quản trị viên và người dùng. Bắt đầu với Bảng điều khiển. Đây là điểm truy cập chính của mọi Máy chủ BTCPay sau khi đăng nhập. Bảng điều khiển cung cấp tổng quan về hiệu suất của cửa hàng, số dư hiện tại của Wallet và các giao dịch trong 7 ngày qua. Vì đây là chế độ xem dạng mô-đun, các plugin có thể sử dụng chế độ xem này để tạo các ô riêng trên Bảng điều khiển. Trong khóa học này, chúng ta sẽ chỉ thảo luận về các plugin và ứng dụng tiêu chuẩn, cùng với chế độ xem tương ứng của chúng, trên toàn bộ Máy chủ BTCPay.


### Ô bảng điều khiển


Trong giao diện chính của bảng điều khiển Máy chủ BTCPay có một vài ô tiêu chuẩn. Các ô này được thiết kế để chủ cửa hàng hoặc Quản trị viên quản lý cửa hàng của mình nhanh chóng chỉ trong một cái nhìn tổng quan.



- Cân Wallet
- Hoạt động giao dịch
- Cân bằng Lightning (nếu Lightning được bật trên cửa hàng)
- Dịch vụ Lightning (nếu Lightning được bật trên cửa hàng)
- Giao dịch gần đây.
- Hóa đơn gần đây
- Các quỹ cộng đồng đang hoạt động hiện tại
- Hiệu suất cửa hàng / mặt hàng bán chạy nhất.


### Cân Wallet


Ô Số dư Wallet cung cấp tổng quan nhanh về nguồn vốn và hiệu suất hoạt động của Wallet. Bạn có thể xem số dư bằng BTC hoặc tiền pháp định trong biểu đồ Hàng tuần, Hàng tháng hoặc Hàng năm.


![image](assets/en/041.webp)


### Hoạt động giao dịch


Bên cạnh ô Số dư Wallet, Máy chủ BTCPay hiển thị tổng quan nhanh về các khoản thanh toán đang chờ xử lý, số lượng Giao dịch trong 7 ngày qua và liệu cửa hàng của bạn đã hoàn tiền hay chưa. Nhấp vào nút Quản lý sẽ đưa bạn đến phần quản lý các khoản thanh toán đang chờ xử lý (tìm hiểu thêm về các khoản thanh toán trong chương Máy chủ BTCPay - Thanh toán).


![image](assets/en/042.webp)


### Cân bằng sét


Tính năng này chỉ hiển thị khi Lightning được kích hoạt.


Khi Quản trị viên cho phép truy cập Lightning Network, bảng điều khiển Máy chủ BTCPay giờ đây sẽ có một ô mới hiển thị thông tin về nút Lightning của bạn. Số lượng BTC trong các kênh, cách thức cân bằng cục bộ hoặc từ xa (thanh khoản đến hoặc đi), các kênh đang đóng hay mở, và số lượng Bitcoin được giữ trên nút Lightning.


![image](assets/en/043.webp)


### Dịch vụ sét


Hiện tượng này chỉ có thể nhìn thấy khi có sét.


Bên cạnh việc xem số dư Lightning của bạn trên bảng điều khiển Máy chủ BTCPay, quản trị viên cũng sẽ thấy ô dành cho Dịch vụ Lightning. Tại đây, quản trị viên có thể tìm thấy các nút nhanh cho các công cụ họ sử dụng để quản lý nút Lightning; ví dụ: Ride the Lightning là một trong những công cụ tiêu chuẩn của Máy chủ BTCPay để quản lý nút Lightning.


![image](assets/en/044.webp)


### Giao dịch gần đây


Ô Giao dịch Gần đây hiển thị các giao dịch gần đây nhất của cửa hàng bạn. Chỉ với một cú nhấp chuột, Quản trị viên của phiên bản Máy chủ BTCPay giờ đây có thể xem giao dịch gần nhất và xem có cần chú ý đến giao dịch đó hay không.


![image](assets/en/045.webp)


### Hóa đơn gần đây


Ô Hóa đơn Gần đây hiển thị 6 hóa đơn gần nhất được tạo bởi Máy chủ BTCPay của bạn, bao gồm Trạng thái và số tiền Invoice. Ô này cũng bao gồm nút "Xem tất cả" để dễ dàng truy cập tổng quan đầy đủ về Invoice.


![image](assets/en/046.webp)


### Điểm bán hàng và huy động vốn cộng đồng


Vì BTCPay Server cung cấp một bộ plugin hoặc ứng dụng tiêu chuẩn, Point Of Sale và Crowdfund là hai plugin chính của BTCPay Server. Với mỗi cửa hàng và Wallet, người dùng BTCPay Server có thể generate bao nhiêu Point Of Sales hoặc Crowdfund tùy ý. Mỗi plugin sẽ tạo một ô bảng điều khiển mới hiển thị hiệu suất của plugin.


![image](assets/en/047.webp)


Lưu ý sự khác biệt nhỏ giữa ô Điểm bán hàng và ô Huy động vốn cộng đồng. Quản trị viên sẽ thấy các mặt hàng bán chạy nhất trong ô Điểm bán hàng. Trong ô Huy động vốn cộng đồng, mục này trở thành Ưu đãi hàng đầu. Cả hai ô đều có các nút nhanh để quản lý ứng dụng tương ứng và xem hóa đơn gần đây được tạo bởi các mặt hàng hoặc ưu đãi hàng đầu.


![image](assets/en/048.webp)


**!?Ghi chú!?**


Biểu đồ số dư và các giao dịch gần đây chỉ khả dụng cho phương thức thanh toán On-Chain. Thông tin về số dư và giao dịch Lightning Network nằm trong danh sách việc cần làm. Kể từ Máy chủ BTCPay Phiên bản 1.6.0, số dư Lightning Network cơ bản đã khả dụng.


### Tóm tắt kỹ năng


Trong phần này, bạn đã học những nội dung sau:



- Bố cục cốt lõi của các ô trên trang đích chính được gọi là Bảng điều khiển.
- Hiểu biết cơ bản về nội dung của từng ô.


### Đánh giá kiến thức


Liệt kê càng nhiều ô nhớ càng tốt từ Bảng điều khiển.


## Máy chủ BTCPay - Cài đặt cửa hàng


<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>


Trong phần mềm BTCPay Server, chúng tôi nhận thấy có hai loại cài đặt. Cài đặt dành riêng cho Cửa hàng của BTCPay Server, nút cài đặt nằm ở thanh menu bên trái bên dưới Bảng điều khiển, và cài đặt BTCPay Server, nằm ở cuối thanh menu, ngay phía trên Tài khoản. Chỉ quản trị viên Máy chủ mới có thể xem cài đặt dành riêng cho Máy chủ của BTCPay Server.


Cài đặt cửa hàng bao gồm nhiều tab để phân loại từng bộ cài đặt.



- Tổng quan
- Tỷ giá
- Giao diện thanh toán
- Mã thông báo truy cập
- Người dùng
- Vai trò
- Webhooks
- Bộ xử lý thanh toán
- Email
- Biểu mẫu


### Tổng quan


Trong tab Cài đặt Chung, chủ cửa hàng sẽ thiết lập mặc định thương hiệu và thanh toán. Khi thiết lập ban đầu cho cửa hàng, tên cửa hàng đã được đặt; tên này sẽ được hiển thị trong mục Cài đặt Chung bên dưới Tên Cửa hàng. Tại đây, chủ cửa hàng cũng có thể thiết lập trang web của mình trùng khớp với thương hiệu và ID Cửa hàng để Quản trị viên nhận diện trong cơ sở dữ liệu.


#### Xây dựng thương hiệu


Vì BTCPay Server là phần mềm nguồn mở (FOSS), chủ cửa hàng có thể tùy chỉnh thương hiệu để phù hợp với cửa hàng của mình. Bạn có thể thiết lập màu sắc thương hiệu, lưu trữ logo thương hiệu và thêm mã CSS tùy chỉnh cho các trang dành cho công chúng/khách hàng (Hóa đơn, Yêu cầu thanh toán, Thanh toán rút gọn).


#### Sự chi trả


Trong phần cài đặt thanh toán, chủ cửa hàng có thể đặt loại tiền tệ mặc định cho cửa hàng của mình (Bitcoin hoặc bất kỳ loại tiền tệ pháp định nào).


#### Cho phép bất kỳ ai tạo hóa đơn


Cài đặt này dành cho các nhà phát triển hoặc nhà xây dựng trên Máy chủ BTCPay. Khi cài đặt này được bật cho cửa hàng của bạn, nó cho phép bên ngoài tạo hóa đơn trên phiên bản Máy chủ BTCPay của bạn.


#### Thêm Phí bổ sung (phí mạng) vào hóa đơn


Một tính năng trong BTCPay giúp bảo vệ người bán khỏi các cuộc tấn công Dust hoặc bảo vệ khách hàng khỏi chi phí cao về sau khi người bán cần chuyển một lượng lớn Bitcoin cùng lúc. Ví dụ: khách hàng tạo một Invoice với giá 20 đô la và thanh toán một phần, thanh toán 1 đô la 20 lần cho đến khi Invoice được thanh toán đầy đủ. Giờ đây, người bán có một giao dịch lớn hơn, điều này sẽ làm tăng chi phí Mining nếu người bán quyết định chuyển số tiền đó sau này. Theo mặc định, BTCPay áp dụng thêm chi phí mạng vào tổng số tiền Invoice để trang trải chi phí đó cho người bán khi Invoice được thanh toán trong nhiều giao dịch. BTCPay cung cấp một số tùy chọn để tùy chỉnh tính năng bảo vệ này. Bạn có thể áp dụng phí mạng:



- Chỉ khi khách hàng thực hiện nhiều hơn một khoản thanh toán cho Invoice (Trong ví dụ trên, nếu khách hàng tạo Invoice với giá 20$ và thanh toán 1$, tổng số tiền Invoice phải trả hiện là 19$ + phí mạng. Phí mạng được áp dụng sau lần thanh toán đầu tiên)
- Với mỗi khoản thanh toán (bao gồm cả khoản thanh toán đầu tiên, trong ví dụ của chúng tôi, tổng số tiền sẽ là 20$ + phí mạng ngay lập tức, ngay cả trong khoản thanh toán đầu tiên)
- Không bao giờ thêm phí mạng (vô hiệu hóa hoàn toàn phí mạng)


Mặc dù điều này bảo vệ bạn khỏi các giao dịch Dust, nhưng nó cũng có thể gây ảnh hưởng tiêu cực đến doanh nghiệp nếu không được truyền đạt đúng cách. Khách hàng có thể có thêm thắc mắc và nghĩ rằng bạn đang tính phí quá cao.


#### Invoice sẽ hết hạn nếu số tiền đầy đủ chưa được thanh toán sau?


Bộ đếm thời gian Invoice được đặt mặc định là 15 phút. Bộ đếm thời gian này đóng vai trò như một cơ chế bảo vệ chống biến động, vì nó khóa số tiền Bitcoin theo tỷ giá quy đổi Bitcoin sang tiền pháp định Exchange. Nếu khách hàng không thanh toán Invoice trong thời hạn quy định, Invoice được coi là đã hết hạn. Invoice được coi là "đã thanh toán" ngay khi giao dịch hiển thị trên Blockchain (không có xác nhận nào), và "hoàn tất" khi đạt đến số xác nhận mà nhà cung cấp đã thiết lập (thường là 1-6). Bộ đếm thời gian có thể tùy chỉnh theo phút.


#### Hãy xem xét Invoice đã trả tiền ngay cả khi số tiền trả ít hơn X% so với dự kiến?


Khi khách hàng sử dụng Exchange, Wallet để thanh toán trực tiếp cho Invoice, Exchange sẽ thu một khoản phí nhỏ. Điều này có nghĩa là Invoice đó chưa được coi là đã hoàn tất thanh toán. Invoice được đánh dấu là "đã thanh toán một phần". Bạn có thể thiết lập tỷ lệ phần trăm tại đây nếu nhà cung cấp muốn chấp nhận các hóa đơn chưa thanh toán đầy đủ.


### Tỷ giá


Trong Máy chủ BTCPay, khi mã Invoice được tạo, nó luôn cần giá Bitcoin sang tiền pháp định mới nhất và chính xác nhất. Khi tạo cửa hàng mới trên Máy chủ BTCPay, quản trị viên được yêu cầu thiết lập nguồn giá ưu tiên. Sau khi cửa hàng được thiết lập, chủ cửa hàng có thể thay đổi nguồn giá trong tab này bất cứ lúc nào.


#### Viết kịch bản quy tắc tỷ giá nâng cao


Chủ yếu được sử dụng bởi người dùng chuyên nghiệp. Nếu bật, chủ cửa hàng có thể tạo tập lệnh về hành vi giá và cách tính phí cho khách hàng.


#### Kiểm tra


Một nơi kiểm tra nhanh các cặp tiền tệ ưa thích của bạn. Tính năng này cũng bao gồm khả năng kiểm tra các cặp tiền tệ mặc định thông qua truy vấn REST.


### Giao diện thanh toán


Tab Giao diện thanh toán bắt đầu bằng các cài đặt cụ thể của Invoice và phương thức thanh toán mặc định, đồng thời kích hoạt các phương thức thanh toán cụ thể khi đáp ứng các yêu cầu đã đặt.


#### Cài đặt Invoice


Phương thức thanh toán mặc định. Máy chủ BTCPay, trong cấu hình tiêu chuẩn, cung cấp ba tùy chọn.



- BTC (On-Chain)
- BTC (LNURL-trả tiền)
- BTC (off-chain & Lightning)


Chúng ta có thể thiết lập các tham số cho cửa hàng của mình, trong đó khách hàng sẽ chỉ tương tác với Lightning khi giá nhỏ hơn số tiền X và ngược lại đối với giao dịch On-Chain, khi X lớn hơn Y, luôn hiển thị tùy chọn thanh toán On-Chain.


![image](assets/en/049.webp)


#### Thanh toán


Kể từ phiên bản 1.7 của Máy chủ BTCPay, một tính năng Thanh toán Interface mới, Thanh toán V2, đã được giới thiệu. Kể từ khi phiên bản 1.9 được chuẩn hóa, quản trị viên và chủ cửa hàng vẫn có thể đặt lại quy trình thanh toán về phiên bản trước đó. Bằng cách sử dụng nút chuyển đổi "Sử dụng quy trình thanh toán cổ điển", chủ cửa hàng có thể khôi phục lại quy trình thanh toán trước đó. Máy chủ BTCPay cũng có một bộ cài đặt sẵn cho giao dịch trực tuyến hoặc trải nghiệm tại cửa hàng.


![image](assets/en/050.webp)


Khi khách hàng tương tác với cửa hàng và tạo mã Invoice, mã Invoice sẽ có thời hạn hiệu lực. Theo mặc định, Máy chủ BTCPay đặt thời hạn này là 5 phút và quản trị viên có thể điều chỉnh theo ý muốn. Trang thanh toán có thể được tùy chỉnh thêm bằng cách kiểm tra các thông số sau:



- Ăn mừng thanh toán bằng cách bắn pháo hoa
- Hiển thị tiêu đề cửa hàng (Tên và logo)
- Hiển thị nút "Thanh toán bằng Wallet"
- Hợp nhất URL/QR thanh toán On-Chain và off-chain
- Hiển thị số tiền thanh toán Lightning bằng Satoshi
- Tự động phát hiện ngôn ngữ khi thanh toán


![image](assets/en/051.webp)


Khi không cài đặt Tự động phát hiện ngôn ngữ, Máy chủ BTCPay sẽ mặc định hiển thị tiếng Anh. Chủ cửa hàng có thể thay đổi ngôn ngữ mặc định này sang ngôn ngữ ưa thích của mình.


![image](assets/en/052.webp)


Nhấp vào menu thả xuống và chủ cửa hàng có thể đặt tiêu đề HTML tùy chỉnh để hiển thị trên trang thanh toán.


![image](assets/en/053.webp)


Để đảm bảo khách hàng biết phương thức thanh toán của mình, chủ cửa hàng có thể thiết lập rõ ràng quy trình thanh toán để yêu cầu người dùng chọn phương thức thanh toán ưa thích. Sau khi thanh toán Invoice, Máy chủ BTCPay cho phép khách hàng quay lại cửa hàng trực tuyến. Chủ cửa hàng có thể thiết lập để quy trình chuyển hướng này tự động được áp dụng sau khi khách hàng thanh toán.


![image](assets/en/054.webp)


#### Biên lai công cộng


Trong cài đặt biên lai công khai, chủ cửa hàng có thể thiết lập các trang biên lai ở chế độ công khai, hiển thị danh sách thanh toán trên trang biên lai và mã QR để khách hàng dễ dàng truy cập.


![image](assets/en/055.webp)


### Mã thông báo truy cập


Mã thông báo truy cập được sử dụng để ghép nối với một số tích hợp thương mại điện tử hoặc tích hợp tùy chỉnh.


![image](assets/en/056.webp)


### Người dùng


Người dùng cửa hàng là nơi chủ cửa hàng có thể quản lý nhân viên, tài khoản của họ và quyền truy cập vào cửa hàng. Sau khi nhân viên tạo tài khoản, chủ cửa hàng có thể thêm người dùng cụ thể vào cửa hàng dưới dạng Người dùng khách hoặc Chủ cửa hàng. Để xác định rõ hơn vai trò của nhân viên, vui lòng tham khảo phần tiếp theo về "Cài đặt Cửa hàng Máy chủ BTCPay - Vai trò".


![image](assets/en/057.webp)


### Vai trò


Chủ cửa hàng có thể không thấy các vai trò tiêu chuẩn của người dùng đủ quan trọng. Trong phần cài đặt vai trò tùy chỉnh, chủ cửa hàng có thể xác định nhu cầu chính xác cho từng vai trò trong doanh nghiệp của mình.


(1) Để tạo vai trò mới, hãy nhấp vào nút "+ Thêm vai trò".


![image](assets/en/058.webp)


(2) Nhập tên Vai trò, ví dụ: "Thu ngân".


![image](assets/en/059.webp)


(3) Cấu hình các quyền riêng lẻ cho vai trò.



- Sửa đổi cửa hàng của bạn.
- Quản lý tài khoản Exchange được liên kết với cửa hàng của bạn.
  - Xem các tài khoản Exchange được liên kết với cửa hàng của bạn.
- Quản lý khoản thanh toán của bạn.
- Tạo thanh toán kéo.
  - Tạo các khoản thanh toán không được chấp thuận.
- Sửa đổi hóa đơn.
  - Xem hóa đơn.
  - Tạo Invoice.
  - Tạo hóa đơn từ các nút sét liên kết với cửa hàng của bạn.
- Xem cửa hàng của bạn.
  - Xem hóa đơn.
  - Xem yêu cầu thanh toán của bạn.
  - Sửa đổi webhook của cửa hàng.
- Sửa đổi yêu cầu thanh toán của bạn.
  - Xem yêu cầu thanh toán của bạn.
- Sử dụng các nút sét liên kết với cửa hàng của bạn.
  - Xem hóa đơn sét đánh liên quan đến cửa hàng của bạn.
  - Tạo hóa đơn từ các nút sét liên kết với cửa hàng của bạn.
- Gửi tiền vào tài khoản Exchange được liên kết với cửa hàng của bạn.
- Rút tiền từ tài khoản Exchange về cửa hàng của bạn.
- Giao dịch tiền trên tài khoản Exchange của cửa hàng bạn.


Khi vai trò được tạo, tên sẽ được cố định và không thể thay đổi sau khi ở chế độ chỉnh sửa.


![image](assets/en/060.webp)


### Webhooks


Trong BTCPay Server, việc tạo một "Webhook" mới khá dễ dàng. Trong tab "Cài đặt Cửa hàng" - Webhook của BTCPay Server, chủ cửa hàng có thể dễ dàng tạo một webhook mới bằng cách nhấp vào "+ Tạo Webhook". Webhook cho phép BTCPay Server gửi các sự kiện HTTP liên quan đến cửa hàng của bạn đến các máy chủ khác hoặc tích hợp thương mại điện tử.


![image](assets/en/061.webp)


Bây giờ bạn đang ở chế độ xem để tạo Webhook. Hãy đảm bảo bạn biết URL Payload của mình và dán URL này vào Máy chủ BTCPay. Khi bạn dán URL payload, bên dưới nó sẽ hiển thị bí mật webhook. Sao chép bí mật webhook và cung cấp nó trên điểm cuối. Khi mọi thứ đã được thiết lập, bạn có thể chuyển đổi trong Máy chủ BTCPay sang "Tự động phân phối lại". Máy chủ BTCPay sẽ cố gắng phân phối lại bất kỳ lần phân phối nào không thành công sau 10 giây, 1 phút và tối đa 6 lần sau 10 phút. Bạn có thể chuyển đổi giữa mọi sự kiện hoặc chỉ định các sự kiện theo nhu cầu của mình. Đảm bảo bật webhook và nhấn nút "Thêm webhook" để lưu.


![image](assets/en/062.webp)


Webhooks không được thiết kế để tương thích với API Bitpay. Có hai IPN riêng biệt (theo thuật ngữ của BitPay: "Thông báo Thanh toán Tức thì") trên Máy chủ BTCPay.



- Webhookp
- Thông báo


Chỉ sử dụng URL thông báo khi bạn tạo hóa đơn thông qua API Bitpay.


### Bộ xử lý thanh toán


Bộ xử lý thanh toán hoạt động cùng với khái niệm Thanh toán trong Máy chủ BTCPay. Đây là một bộ tổng hợp thanh toán để xử lý nhiều giao dịch và gửi chúng cùng một lúc. Với bộ xử lý thanh toán, chủ cửa hàng có thể tự động hóa việc thanh toán theo đợt. Máy chủ BTCPay cung cấp hai phương thức thanh toán tự động: On-Chain và off-chain (LN).


Chủ cửa hàng có thể nhấp và cấu hình riêng biệt cả hai bộ xử lý thanh toán. Chủ cửa hàng có thể chỉ muốn chạy bộ xử lý On-Chain một lần sau mỗi X giờ, trong khi bộ xử lý off-chain có thể chạy sau mỗi vài phút. Đối với On-Chain, bạn cũng có thể đặt mục tiêu khối nào sẽ được đưa vào. Theo mặc định, mục tiêu này được đặt thành 1 (hoặc khối tiếp theo khả dụng). Lưu ý rằng việc thiết lập bộ xử lý thanh toán off-chain chỉ có bộ đếm thời gian theo khoảng thời gian và không có mục tiêu khối. Thanh toán Lightning Network được thực hiện ngay lập tức.


![image](assets/en/063.webp)

![image](assets/en/064.webp)


Chủ cửa hàng chỉ có thể cấu hình bộ xử lý On-Chain nếu họ có Hot Wallet được kết nối với cửa hàng của mình.


![image](assets/en/065.webp)


Sau khi thiết lập Bộ xử lý thanh toán, bạn có thể nhanh chóng xóa hoặc sửa đổi bộ xử lý đó bằng cách quay lại tab Bộ xử lý thanh toán trong cài đặt Cửa hàng máy chủ BTCPay.


**Ghi chú**


Bộ xử lý thanh toán On-Chain - Bộ xử lý thanh toán On-Chain chỉ có thể hoạt động trên cửa hàng được cấu hình với Hot Wallet được kết nối. Nếu không có Hot Wallet nào được kết nối, Máy chủ BTCPay sẽ không giữ khóa Wallet và sẽ không thể xử lý thanh toán tự động.


### Email


Máy chủ BTCPay có thể sử dụng Email để thông báo hoặc, khi được thiết lập chính xác, để khôi phục tài khoản đã tạo trên phiên bản. Theo mặc định, Máy chủ BTCPay không gửi email khi mật khẩu bị mất, chẳng hạn.


![image](assets/en/066.webp)


Trước khi chủ cửa hàng có thể thiết lập quy tắc email để kích hoạt các sự kiện cụ thể trong cửa hàng, trước tiên họ phải thiết lập một số cài đặt email cơ bản. Máy chủ BTCPay yêu cầu các cài đặt này để gửi email cho các sự kiện liên quan đến cửa hàng của bạn hoặc để đặt lại mật khẩu.


Máy chủ BTCPay giúp việc điền thông tin này dễ dàng hơn bằng cách sử dụng Tùy chọn "Điền nhanh":



- Gmail.com
- Yahoo.com
- Súng thư
- Office365
- Gửi Lưới


Bằng cách sử dụng tùy chọn điền nhanh, Máy chủ BTCPay sẽ tự động điền sẵn các trường cho máy chủ SMTP và cổng. Giờ đây, chủ cửa hàng chỉ cần điền thông tin đăng nhập, bao gồm Email Address, Tên đăng nhập (thường bằng email Address của bạn) và mật khẩu. Tùy chọn nâng cao trong cài đặt email của Máy chủ BTCPay là Tắt kiểm tra bảo mật Chứng chỉ TLS; theo mặc định, tùy chọn này được bật.


![image](assets/en/067.webp)


Với Quy tắc email, chủ cửa hàng có thể thiết lập các sự kiện cụ thể để kích hoạt gửi email đến các địa chỉ email cụ thể.



- Invoice đã được tạo
- Invoice Đã nhận thanh toán
- Xử lý Invoice
- Invoice đã hết hạn
- Invoice Đã giải quyết
- Invoice Không hợp lệ
- Invoice Thanh toán đã được giải quyết


Nếu khách hàng đã cung cấp Email Address, các trình kích hoạt này cũng có thể gửi thông tin đến khách hàng. Chủ cửa hàng có thể điền trước dòng Tiêu đề để làm rõ lý do tại sao Email này được gửi đến và điều gì đã kích hoạt nó.


![image](assets/en/068.webp)


### Biểu mẫu


Vì BTCPay Server không thu thập bất kỳ dữ liệu nào, chủ cửa hàng có thể muốn thêm một biểu mẫu tùy chỉnh vào trải nghiệm thanh toán của mình; bằng cách này, chủ cửa hàng có thể thu thập thêm thông tin từ khách hàng. Trình tạo biểu mẫu của BTCPay Server bao gồm hai phần: chế độ xem trực quan và mã nâng cao hơn của biểu mẫu.


Khi tạo biểu mẫu mới, Máy chủ BTCPay sẽ mở một cửa sổ mới yêu cầu thông tin cơ bản về những gì bạn muốn biểu mẫu mới của mình hỏi. Trước tiên, chủ cửa hàng cần đặt tên rõ ràng cho biểu mẫu mới; tên này không thể thay đổi sau khi đã được đặt.


![image](assets/en/069.webp)


Sau khi chủ cửa hàng đặt tên cho biểu mẫu, bạn cũng có thể bật nút "Cho phép sử dụng biểu mẫu công khai" sang ON, và biểu mẫu sẽ chuyển thành Green. Điều này đảm bảo biểu mẫu được sử dụng tại mọi địa điểm tiếp xúc với khách hàng. Ví dụ: nếu chủ cửa hàng tạo một Invoice riêng biệt không thông qua Điểm bán hàng, họ vẫn có thể muốn thu thập thông tin từ khách hàng. Nút bật/tắt này cho phép thu thập thông tin đó.


![image](assets/en/070.webp)


Mỗi biểu mẫu đều bắt đầu bằng ít nhất 1 trường biểu mẫu mới. Chủ cửa hàng có thể chọn loại trường cho biểu mẫu đó.



- Chữ
- Con số
- Mật khẩu
- E-mail
- URL
- Số điện thoại
- Ngày
- Các trường ẩn
- Bộ trường
- Một vùng văn bản để bình luận mở.
- Bộ chọn tùy chọn


Mỗi loại đều có các tham số riêng để điền. Chủ cửa hàng có thể tùy chỉnh theo ý thích. Bên dưới trường đầu tiên được tạo, chủ cửa hàng có thể thêm các trường mới vào biểu mẫu này.


![image](assets/en/071.webp)


#### Biểu mẫu tùy chỉnh nâng cao


Máy chủ BTCPay cũng cho phép bạn xây dựng Biểu mẫu bằng mã, đặc biệt là JSON. Thay vì nhìn vào trình soạn thảo, chủ cửa hàng có thể nhấp vào nút MÃ (CODE) ngay bên cạnh trình soạn thảo và truy cập vào mã của Biểu mẫu. Trong định nghĩa trường, chỉ có thể thiết lập các trường sau; giá trị của các trường được lưu trữ trong siêu dữ liệu của Invoice:


| Field                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| .fields.constant      | If true, the .value must be set in the form definition, and the user will not be able to change the field's value. ( example: the form definition's version)                                                                                                                                                                                                                                                                                                       |
| .fields.type          | The HTML input type text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel                                                                                                                                                                                                                                                                                                |
| .fields.options       | If .fields.type is select, the list of selectable values                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.options.text  | The text displayed for this option                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.options.value | The value of the field if this option is selected                                                                                                                                                                                                                                                                                                                                                                                                                  |
| .fields.type=fieldset | Create a HTML fieldset around the children .fields.fields (see below)                                                                                                                                                                                                                                                                                                                                                                                              |
| .fields.name          | The JSON property name of the field as it will appear in the invoice's metadata                                                                                                                                                                                                                                                                                                                                                                                    |
| .fields.value         | The default value of the field                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| .fields.required      | if true, the field will be required                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .fields.label         | The label of the field                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| .fields.helpText      | Additional text to provide an explanation for the field.                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.fields        | You can organize your fields in a hierarchy, allowing child fields to be nested within the invoice’s metadata. This structure can help you better organize and manage the collected information, making it easier to access and interpret. For example, if you have a form that collects customer information, you can group the fields under a parent field called customer. Within this parent field, you might have child fields like name, Email, and address. |

Tên trường đại diện cho tên thuộc tính JSON lưu trữ giá trị do người dùng cung cấp trong siêu dữ liệu của Invoice. Một số tên phổ biến có thể được diễn giải và sửa đổi để điều chỉnh cài đặt của Invoice.


| Field name       | Description            |
| ---------------- | ---------------------- |
| invoice_amount   | The invoice's amount   |
| invoice_currency | The invoice's currency |

Bạn có thể tự động điền trước các trường của Invoice bằng cách thêm chuỗi truy vấn vào URL của biểu mẫu, chẳng hạn như "?your_field=value".


Sau đây là một số trường hợp sử dụng tính năng này:



- Hỗ trợ người dùng nhập liệu: Điền trước thông tin khách hàng đã biết vào các trường để giúp họ dễ dàng hoàn thành biểu mẫu hơn. Ví dụ: nếu bạn đã biết email của khách hàng là Address, bạn có thể điền trước trường email để tiết kiệm thời gian cho họ.
- Cá nhân hóa: Tùy chỉnh biểu mẫu dựa trên sở thích hoặc phân khúc khách hàng. Ví dụ: nếu bạn có nhiều cấp độ khách hàng khác nhau, bạn có thể điền sẵn dữ liệu liên quan vào biểu mẫu, chẳng hạn như cấp độ thành viên hoặc ưu đãi cụ thể của họ.
- Theo dõi: Theo dõi nguồn truy cập của khách hàng bằng các trường ẩn và giá trị được điền sẵn. Ví dụ: bạn có thể tạo liên kết với các giá trị utm_media được điền sẵn cho từng kênh tiếp thị (ví dụ: Twitter, Facebook, Email). Điều này giúp bạn phân tích hiệu quả của các nỗ lực tiếp thị.
- Kiểm tra A/B: Điền trước các trường bằng các giá trị khác nhau để kiểm tra các phiên bản biểu mẫu khác nhau, cho phép bạn tối ưu hóa trải nghiệm người dùng và tỷ lệ chuyển đổi.


### Tóm tắt kỹ năng


Trong phần này, bạn đã học những nội dung sau:



- Bố cục và chức năng của các tab trong Cài đặt Cửa hàng
- Nhiều tùy chọn để tinh chỉnh cách xử lý các mức thuế Exchange cơ bản, thanh toán một phần, thanh toán thiếu một chút, v.v.
- Tùy chỉnh giao diện thanh toán, bao gồm chuỗi chính phụ thuộc vào giá so với kích hoạt Lightning trên hóa đơn.
- Quản lý cấp độ truy cập và quyền hạn của cửa hàng trên các vai trò.
- Cấu hình email tự động và các kích hoạt của chúng
- Tạo biểu mẫu tùy chỉnh để thu thập thêm thông tin khách hàng khi thanh toán.


### Đánh giá kiến thức


#### Đánh giá KA


Sự khác biệt giữa Cài đặt cửa hàng và Cài đặt máy chủ là gì?


#### KA Giả thuyết


Mô tả một số tùy chọn bạn có thể chọn trong Giao diện thanh toán > Cài đặt Invoice và lý do.


## Máy chủ BTCPay - Cài đặt máy chủ


<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>


Máy chủ BTCPay bao gồm hai chế độ xem cài đặt khác nhau. Một chế độ dành riêng cho cài đặt Cửa hàng, và chế độ còn lại dành cho cài đặt Máy chủ. Chế độ sau chỉ dành cho quản trị viên máy chủ chứ không dành cho chủ cửa hàng. Quản trị viên máy chủ có thể thêm người dùng, tạo vai trò tùy chỉnh, cấu hình máy chủ email, thiết lập chính sách, chạy tác vụ bảo trì, kiểm tra tất cả các dịch vụ được kết nối với Máy chủ BTCPay, tải tệp lên máy chủ hoặc kiểm tra Nhật ký.


### Người dùng


Như đã đề cập ở phần trước, Quản trị viên máy chủ có thể mời người dùng vào máy chủ của mình bằng cách thêm họ vào tab Người dùng.


### Vai trò tùy chỉnh trên toàn máy chủ


Máy chủ BTCPay có hai loại vai trò tùy chỉnh: vai trò tùy chỉnh dành riêng cho cửa hàng và vai trò tùy chỉnh toàn máy chủ trong cài đặt Máy chủ BTCPay. Cả hai đều có bộ quyền tương tự nhau; tuy nhiên, nếu được thiết lập thông qua tab Cài đặt Máy chủ BTCPay - Vai trò, vai trò được áp dụng sẽ áp dụng cho toàn máy chủ và cho nhiều cửa hàng. Lưu ý thẻ "Toàn máy chủ" cho các vai trò tùy chỉnh trong cài đặt Máy chủ.


![image](assets/en/072.webp)


### Vai trò tùy chỉnh trên toàn máy chủ


Bộ quyền vai trò tùy chỉnh trên toàn máy chủ;



- Sửa đổi cửa hàng của bạn.
- Quản lý các tài khoản Exchange được liên kết với cửa hàng của bạn.
  - Xem các tài khoản Exchange được liên kết với cửa hàng của bạn.
- Quản lý khoản thanh toán của bạn.
- Tạo thanh toán kéo.
  - Tạo các khoản thanh toán không được chấp thuận.
- Sửa đổi hóa đơn.
  - Xem hóa đơn.
  - Tạo Invoice.
  - Tạo hóa đơn từ các nút sét liên kết với cửa hàng của bạn.
- Xem cửa hàng của bạn.
  - Xem hóa đơn.
  - Xem yêu cầu thanh toán của bạn.
  - Sửa đổi webhook của cửa hàng.
- Sửa đổi yêu cầu thanh toán của bạn.
  - Xem yêu cầu thanh toán của bạn.
- Sử dụng các nút sét liên kết với cửa hàng của bạn.
  - Xem hóa đơn sét đánh liên quan đến cửa hàng của bạn.
  - Tạo hóa đơn từ các nút sét liên kết với cửa hàng của bạn.
- Gửi tiền vào tài khoản Exchange được liên kết với cửa hàng của bạn.
- Rút tiền từ tài khoản Exchange về cửa hàng của bạn.
- Giao dịch tiền trên tài khoản Exchange của cửa hàng bạn.


**!?Ghi chú!?**


Khi vai trò được tạo, tên sẽ được cố định và không thể thay đổi sau khi ở chế độ chỉnh sửa.


### E-mail


Cài đặt Email toàn máy chủ trông tương tự như cài đặt email dành riêng cho Cửa hàng. Tuy nhiên, thiết lập này không chỉ xử lý các kích hoạt cho cửa hàng hoặc nhật ký quản trị viên mà còn cho các kích hoạt cho các sự kiện khác. Thiết lập Email này cũng cho phép khôi phục mật khẩu trên Máy chủ BTCPay khi Đăng nhập. Nó hoạt động tương tự như cài đặt dành riêng cho Cửa hàng; quản trị viên có thể nhanh chóng điền thông số Email và nhập thông tin đăng nhập email, cho phép máy chủ gửi email.


![image](assets/en/073.webp)


### Chính sách


Quản trị viên chính sách Máy chủ BTCPay có thể thiết lập nhiều cài đặt khác nhau cho các chủ đề như cài đặt Người dùng hiện tại, cài đặt Người dùng mới, cài đặt Thông báo và cài đặt Bảo trì. Những cài đặt này được thiết kế để đăng ký người dùng mới làm quản trị viên hoặc người dùng thường xuyên, hoặc để ẩn Máy chủ BTCPay khỏi các công cụ tìm kiếm bằng cách thêm nó vào tiêu đề máy chủ của bạn.


![image](assets/en/074.webp)


#### Cài đặt người dùng hiện tại


Các tùy chọn có sẵn ở đây tách biệt với các vai trò tùy chỉnh. Các quyền bổ sung này có thể khiến cửa hàng hoặc chủ sở hữu cửa hàng dễ bị tấn công. Các chính sách có thể được thêm vào cho người dùng hiện tại:



- Cho phép những người không phải quản trị viên sử dụng nút Lightning nội bộ trong cửa hàng của họ.
  - Điều này sẽ cho phép chủ cửa hàng sử dụng nút Lightning của Quản trị viên máy chủ và do đó, sử dụng được tiền của họ! Lưu ý, đây không phải là giải pháp để cấp quyền truy cập vào Lightning.
- Cho phép người dùng không phải quản trị viên tạo ví Hot cho cửa hàng của họ.
  - Điều này sẽ cho phép bất kỳ ai có tài khoản trên phiên bản Máy chủ BTCPay của bạn tạo ví Hot và lưu trữ ví seed phục hồi của họ trên máy chủ của Quản trị viên. Điều này có thể khiến Quản trị viên phải chịu trách nhiệm về việc nắm giữ tiền của bên thứ ba!
- Cho phép người dùng không phải quản trị viên nhập ví Hot vào cửa hàng của họ.
  - Tương tự như chủ đề trước về việc tạo ví Hot, chính sách này cho phép nhập Hot Wallet, với những nguy cơ tương tự được đề cập trong phần tạo ví Hot.


![image](assets/en/075.webp)


#### Cài đặt người dùng mới


Chúng ta có thể thiết lập một số cài đặt quan trọng để quản lý người dùng mới truy cập máy chủ. Chúng ta có thể thiết lập email xác nhận cho các đăng ký mới, vô hiệu hóa việc tạo người dùng mới thông qua màn hình đăng nhập và hạn chế quyền truy cập của người dùng không phải quản trị viên vào việc tạo người dùng qua API.



- Cần có email xác nhận để đăng ký.
  - Người quản trị máy chủ phải thiết lập máy chủ Email.
- Vô hiệu hóa đăng ký người dùng mới trên máy chủ
- Vô hiệu hóa quyền truy cập của người không phải quản trị viên vào điểm cuối API tạo người dùng.


Theo mặc định, Máy chủ BTCPay đã bật tùy chọn "Vô hiệu hóa đăng ký người dùng mới trên máy chủ" và tắt quyền truy cập của người dùng không phải quản trị viên vào điểm cuối API tạo người dùng. Điều này nhằm mục đích bảo mật, để những người lạ vô tình nhìn thấy thông tin đăng nhập BTCPay của bạn sẽ không thể tạo tài khoản.


![image](assets/en/076.webp)


#### Cài đặt thông báo


![image](assets/en/077.webp)


#### Cài đặt bảo trì


BTCPay Server là một dự án nguồn mở trên GitHub. Mỗi khi BTCPay Server phát hành phiên bản phần mềm mới, Quản trị viên có thể được thông báo về phiên bản mới. Quản trị viên cũng có thể muốn tránh các công cụ tìm kiếm (như Google, Yahoo và DuckDuckGo) lập chỉ mục tên miền BTCPay Server. Vì BTCPay Server là phần mềm nguồn mở (FOSS), các nhà phát triển trên toàn thế giới có thể muốn tạo ra các tính năng mới. BTCPay Server có một tính năng thử nghiệm, khi được bật, cho phép quản trị viên sử dụng các tính năng không dành cho sản xuất mà chỉ dành cho mục đích thử nghiệm.



- Kiểm tra bản phát hành trên GitHub và thông báo khi có phiên bản BTCPay Server mới.
- Không khuyến khích các công cụ tìm kiếm lập chỉ mục trang web này
- Bật tính năng thử nghiệm.


![image](assets/en/078.webp)


#### Các plugin


Máy chủ BTCPay có thể thêm Plugin và mở rộng bộ tính năng. Theo mặc định, các plugin được tải từ kho plugin-builder của Máy chủ BTCPay. Tuy nhiên, quản trị viên có thể chọn xem plugin ở trạng thái Tiền phát hành, và nếu nhà phát triển plugin cho phép, quản trị viên máy chủ giờ đây có thể cài đặt phiên bản beta của plugin.


![image](assets/en/079.webp)


##### Cài đặt tùy chỉnh


Việc triển khai Máy chủ BTCPay tiêu chuẩn sẽ có thể truy cập thông qua tên miền được thiết lập trong quá trình cài đặt. Tuy nhiên, quản trị viên máy chủ có thể ánh xạ lại tên miền gốc và hiển thị một trong những ứng dụng đã tạo từ một cửa hàng cụ thể. Quản trị viên Máy chủ cũng có thể ánh xạ các tên miền cụ thể với các ứng dụng cụ thể.



- Hiển thị ứng dụng trên gốc của trang web
  - Hiển thị danh sách các ứng dụng có thể hiển thị trên miền gốc.


![image](assets/en/080.webp)



- Ánh xạ các miền cụ thể tới các ứng dụng cụ thể.
  - Khi bạn nhấp để thiết lập một tên miền cụ thể cho các ứng dụng cụ thể, Quản trị viên có thể thiết lập bao nhiêu tên miền trỏ đến các ứng dụng cụ thể tùy theo nhu cầu.


![image](assets/en/081.webp)


#### Trình khám phá khối


Theo mặc định, Máy chủ BTCPay đi kèm với Mempool.space làm Block explorer cho các giao dịch. Khi Máy chủ BTCPay tạo Invoice mới và một giao dịch được liên kết với nó, chủ cửa hàng có thể nhấp để mở giao dịch. Theo mặc định, Máy chủ BTCPay sẽ trỏ đến Mempool.space làm Block explorer; tuy nhiên, Quản trị viên máy chủ có thể thay đổi tùy chọn này theo ý muốn.


![image](assets/en/082.webp)


### Dịch vụ


Tab "Cài đặt Máy chủ BTCPay: Dịch vụ" là phần tổng quan về các thành phần mà Máy chủ BTCPay của bạn sử dụng. Các dịch vụ mà Máy chủ BTCPay của bạn cung cấp có thể khác nhau tùy thuộc vào phương thức triển khai.


Quản trị viên máy chủ BTCPay có thể nhấp vào “Xem thông tin” phía sau mỗi dịch vụ để mở và thiết lập các cài đặt cụ thể.


![image](assets/en/083.webp)


#### LND (gRPC)


BTCPay cung cấp dịch vụ GRPC của LND cho bên ngoài; bạn sẽ tìm thấy thông tin kết nối trong menu cài đặt cụ thể này; các ví tương thích được liệt kê tại đây. Máy chủ BTCPay cũng cung cấp mã QR để kết nối, có thể quét và áp dụng cho thiết bị di động Wallet.


Quản trị viên máy chủ có thể mở thêm thông tin chi tiết để xem.



- Chi tiết máy chủ
- Sử dụng SSL
- Bánh macaron
- Quản trịMacaroon
- Hóa đơnMacaroon
- Chỉ đọcMacaroon
- Bộ mã hóa SSL GRPC (GRPC_SSL_CIPHER_SUITES)


#### LND (PHẦN CÒN LẠI)


BTCPay cung cấp dịch vụ REST của LND cho bên ngoài; bạn sẽ tìm thấy thông tin kết nối [tại đây](https://docs.btcpayserver.org/FAQ/LightningNetwork/#how-to-find-node-info-and-open-a-direct-channel-with-a-store-using-btcpay); các ví tương thích được liệt kê [tại đây](https://docs.btcpayserver.org/FAQ/Wallet/#can-i-use-a-hardware-wallet-with-btcpay-server). Trong số các ví tương thích có Joule, Alby và ZeusLN. Máy chủ BTCPay cung cấp mã QR để kết nối, có thể được quét và áp dụng vào Wallet tương thích.



- URI REST
- Bánh macaron
- AdminMacaroon
- Hóa đơnMacaroon
- Chỉ đọcMacaroon


#### LND seed Sao lưu


Bản sao lưu LND seed rất hữu ích để khôi phục tiền từ LND Wallet của bạn trong trường hợp máy chủ bị hỏng. Vì nút Lightning là Hot-Wallet, bạn có thể tìm thấy thông tin seed bí mật trên trang này.


LND ghi lại quá trình phục hồi. Xem tài liệu tại https://github.com/lightningnetwork/LND/blob/master/docs/recovery.md.


#### Cưỡi Tia Chớp


Ride the Lightning là một công cụ quản lý nút Lightning được xây dựng dưới dạng phần mềm nguồn mở. BTCPay Server sử dụng RTL làm thành phần quản lý nút Lightning trong ngăn xếp của nó. Quản trị viên BTCPay Server có thể truy cập RTL thông qua tab Cài đặt máy chủ - Dịch vụ hoặc bằng cách nhấp vào Lightning Wallet.


#### Full node P2P


Quản trị viên máy chủ có thể muốn kết nối nút Bitcoin của họ với Wallet di động. Trang này cung cấp thông tin về cách kết nối từ xa với Full node của bạn thông qua giao thức P2P. Tại thời điểm viết khóa học này, BTCPay Server liệt kê ví Blockstream Green và Wasabi là các ví tương thích. BTCPay Server cung cấp mã QR để kết nối, có thể được quét và áp dụng vào Wallet tương thích.


#### Full node RPC


Trang này cung cấp thông tin để kết nối từ xa với Full node của bạn thông qua giao thức RPC.


#### SSH


SSH được sử dụng cho mục đích bảo trì. Máy chủ BTCPay hiển thị lệnh kết nối ban đầu để đến Máy chủ của bạn và khóa công khai SSH được ủy quyền để kết nối với Máy chủ của bạn. Quản trị viên máy chủ có thể muốn tắt các thay đổi SSH thông qua Giao diện người dùng Máy chủ BTCPay.


#### DNS động


DNS động cho phép bạn có một tên DNS ổn định trỏ đến Máy chủ của mình, ngay cả khi địa chỉ IP Address của bạn thay đổi thường xuyên. Tính năng này được khuyến nghị nếu bạn đang lưu trữ Máy chủ BTCPay tại nhà và muốn có một tên miền clearnet để truy cập Máy chủ.


Lưu ý rằng bạn cần cấu hình đúng NAT và cài đặt Máy chủ BTCPay để nhận được chứng chỉ HTTPS.


### Chủ đề


Máy chủ BTCPay, theo mặc định, có hai giao diện: Sáng và Tối. Bạn có thể chuyển đổi giữa hai giao diện này bằng cách nhấp vào mục Tài khoản ở góc dưới bên trái và chọn giữa giao diện Tối và Sáng. Quản trị viên Máy chủ BTCPay có thể thêm giao diện riêng bằng cách cung cấp giao diện CSS tùy chỉnh.


Người quản trị có thể mở rộng chủ đề Sáng/Tối bằng cách thêm CSS tùy chỉnh của riêng họ hoặc đặt chủ đề tùy chỉnh của họ thành chủ đề tùy chỉnh đầy đủ.


![image](assets/en/084.webp)


#### Thương hiệu máy chủ


Quản trị viên máy chủ có thể thay đổi thương hiệu Máy chủ BTCPay bằng cách thiết lập thương hiệu toàn máy chủ cho công ty của bạn. Vì Máy chủ BTCPay là phần mềm nguồn mở (FOSS), quản trị viên máy chủ có thể gắn nhãn trắng cho phần mềm và tùy chỉnh giao diện cho phù hợp với doanh nghiệp của mình.


![image](assets/en/085.webp)


### BẢO TRÌ


Là quản trị viên máy chủ, người dùng mong đợi bạn chăm sóc Máy chủ chu đáo. Trong tab Bảo trì của Máy chủ BTCPay, quản trị viên có thể thực hiện một số bảo trì cần thiết. Đặt tên miền cho phiên bản Máy chủ BTCPay, Khởi động lại hoặc dọn dẹp Máy chủ. Có lẽ quan trọng nhất là chạy cập nhật.


Máy chủ BTCPay là một dự án Nguồn mở và được cập nhật thường xuyên. Mỗi bản phát hành mới đều được thông báo qua Thông báo Máy chủ BTCPay của bạn hoặc trên các Kênh chính thức mà Máy chủ BTCPay giao tiếp.


![image](assets/en/086.webp)


#### Tên miền


Sau khi Máy chủ BTCPay được thiết lập, quản trị viên có thể muốn thay đổi tên miền gốc. Trong tab Bảo trì, quản trị viên có thể thay đổi tên miền. Sau khi nhấp vào xác nhận và thiết lập bản ghi DNS phù hợp trên tên miền, Máy chủ BTCPay sẽ cập nhật và khởi động lại để trở về tên miền mới.


![image](assets/en/087.webp)


#### Khởi động lại


Khởi động lại Máy chủ BTCPay và các dịch vụ liên quan.


![image](assets/en/088.webp)


#### Lau dọn


Máy chủ BTCPay chạy với các thành phần Docker; sau khi cập nhật, có thể còn sót lại các hình ảnh Docker, tệp tạm thời, v.v. Quản trị viên máy chủ có thể giải phóng dung lượng bằng cách chạy tập lệnh Clean.


![image](assets/en/089.webp)


#### Cập nhật


Đây là tùy chọn quan trọng nhất trong tab Bảo trì. BTCPay Server được xây dựng bởi cộng đồng, do đó, chu kỳ cập nhật của nó thường xuyên hơn hầu hết các sản phẩm phần mềm khác. Khi BTCPay Server có bản phát hành mới, quản trị viên sẽ được thông báo trong trung tâm thông báo. Bằng cách nhấp vào nút cập nhật, BTCPay Server sẽ kiểm tra GitHub để tìm bản phát hành mới nhất, cập nhật Máy chủ và khởi động lại. Trước khi cập nhật, quản trị viên máy chủ luôn được khuyến cáo đọc kỹ các ghi chú phát hành được phân phối qua các kênh chính thức của BTCPay Server.


![image](assets/en/090.webp)


### Nhật ký


Đối mặt với vấn đề chưa bao giờ là điều dễ dàng. Tài liệu này phác thảo quy trình làm việc và các bước phổ biến nhất để xác định và giải quyết vấn đề của bạn một cách hiệu quả, dù là tự mình giải quyết hay với sự hỗ trợ của cộng đồng.


Việc xác định vấn đề là rất quan trọng.


#### Sao chép vấn đề


Trước tiên và quan trọng nhất, hãy cố gắng xác định thời điểm sự cố xảy ra. Hãy thử tái hiện sự cố. Hãy thử cập nhật và khởi động lại Máy chủ của bạn để xác minh rằng bạn có thể tái hiện sự cố. Nếu sự cố của bạn mô tả rõ hơn, hãy chụp ảnh màn hình.


##### Đang cập nhật máy chủ


Kiểm tra phiên bản Máy chủ BTCPay của bạn xem có cũ hơn nhiều so với [phiên bản mới nhất](https://github.com/btcpayserver/btcpayserver/releases) của Máy chủ BTCPay không. Việc cập nhật Máy chủ của bạn có thể giải quyết được sự cố.


##### Khởi động lại máy chủ


Khởi động lại Máy chủ là một cách dễ dàng để giải quyết nhiều sự cố thường gặp nhất của Máy chủ BTCPay. Bạn có thể cần SSH vào Máy chủ để khởi động lại.


##### Khởi động lại dịch vụ


Bạn có thể chỉ cần khởi động lại một dịch vụ cụ thể trong quá trình triển khai Máy chủ BTCPay của mình đối với một số sự cố, chẳng hạn như khởi động lại vùng chứa letsencrypt để gia hạn chứng chỉ SSL.


```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```


Sử dụng docker ps để tìm tên của dịch vụ khác mà bạn muốn khởi động lại.


#### Nhìn qua các bản ghi


Nhật ký có thể cung cấp một thông tin thiết yếu. Trong các đoạn sau, chúng tôi sẽ mô tả cách lấy thông tin nhật ký cho các phần khác nhau của BTCPay.


##### Nhật ký BTCPay


Kể từ phiên bản 1.0.3.8, bạn có thể dễ dàng truy cập nhật ký máy chủ BTCPay từ giao diện người dùng. Nếu bạn là quản trị viên máy chủ, hãy vào Cài đặt Máy chủ > Nhật ký và mở tệp nhật ký. Nếu bạn không biết lỗi cụ thể trong nhật ký nghĩa là gì, hãy đề cập đến lỗi đó khi khắc phục sự cố.


Nếu bạn muốn xem nhật ký chi tiết hơn và đang sử dụng triển khai Docker, bạn có thể xem nhật ký của các container Docker cụ thể bằng dòng lệnh. Xem [hướng dẫn ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) vào một phiên bản BTCPay đang chạy trên VPS.


Ở trang tiếp theo, danh sách chung về tên vùng chứa được sử dụng cho Máy chủ BTCPay.


Chạy các lệnh bên dưới để in nhật ký theo tên container. Thay thế tên container để xem nhật ký container khác.


```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```


| Logs for     | Container Name                    |
| ------------ | --------------------------------- |
| BTCPayServer | generated_btcpayserver_1          |
| NBXplorer    | generated_nbxplorer_1             |
| Bitcoind     | btcpayserver_bitcoind             |
| Postgres     | generated_postgres_1              |
| proxy        | letsencrypt-nginx-proxy-companion |
| Nginx        | nginx-gen                         |
| Nginx        | nginx                             |
| c-lightning  | btcpayserver_clightning_bitcoin   |
| LND          | btcpayserver_lnd_bitcoin          |
| RTL          | generated_lnd_bitcoin_rtl_1       |
| Thunderhub   | generated_bitcoin_thub_1          |
| LibrePatron  | librepatron                       |
| Tor          | tor-gen                           |
| Tor          | tor                               |

###### Lightning Network LND - Docker


Có một số cách để truy cập nhật ký LND của bạn khi sử dụng Docker. Đầu tiên, hãy đăng nhập với tư cách root:


```bash
sudo su -
Navigate to the correct directory:
cd btcpayserver-docker
# Find container name:
docker ps
Print logs by container name:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```


Ngoài ra, bạn có thể in nhật ký nhanh chóng bằng cách sử dụng ID vùng chứa (chỉ cần các ký tự ID duy nhất đầu tiên, chẳng hạn như hai ký tự ngoài cùng bên trái):


```bash
docker logs 'add your container ID'
```


Nếu vì lý do nào đó bạn cần thêm nhật ký


```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/\_data/logs/ bitcoin/mainnet/
ls
```


Bạn sẽ thấy một cái gì đó giống như


```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```


Để truy cập các bản ghi chưa nén của các bản ghi đó, hãy sử dụng `cat LND.log` hoặc nếu bạn muốn một bản ghi khác, hãy sử dụng `cat LND.log.15`.


Để truy cập nhật ký nén trong `.gzip`, hãy sử dụng `gzip -d LND.log.16.gz` (trong trường hợp này, chúng ta đang truy cập `LND.log.16.gz`). Lệnh này sẽ mở ra một tệp mới, nơi bạn có thể chạy lệnh `cat LND.log.16`. Trong trường hợp cách trên không hiệu quả, bạn có thể cần cài đặt gzip trước bằng lệnh `sudo apt-get install gzip`.


###### Lightning Network c-lightning - Docker


```bash
sudo su -
docker ps
# Find the c-lightning container ID.
docker logs 'add your container ID here'
```


Ngoài ra, bạn có thể sử dụng cách sau:


```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```


Bạn cũng có thể lấy thông tin nhật ký bằng lệnh c-lightning CLI.


```bash
bitcoin-lightning-cli.sh getlog
```


#### Nhật ký nút Bitcoin


Ngoài việc [xem nhật ký](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) của vùng chứa bitcoind, bạn cũng có thể sử dụng bất kỳ [lệnh bitcoin-cli](https://developer.Bitcoin.org/reference/RPC/index.html)


[(mở cửa sổ mới)](https://developer.Bitcoin.org/reference/RPC/index.html) để lấy thông tin từ nút Bitcoin của bạn. BTCPay bao gồm một tập lệnh cho phép bạn dễ dàng giao tiếp với nút Bitcoin của mình.


Bên trong thư mục btcpayserver-docker, hãy lấy thông tin Blockchain bằng nút của bạn:


```bash
bitcoin-cli.sh getblockchaininfo
```


### Tập tin


Máy chủ BTCPay có hệ thống tệp cục bộ, cho phép tải trực tiếp nội dung cửa hàng (sản phẩm), Logo và thương hiệu lên Máy chủ. Hệ thống tệp của máy chủ chỉ có thể được truy cập bởi Quản trị viên Máy chủ; chủ cửa hàng có thể tải logo hoặc thương hiệu của họ lên cấp cửa hàng.


Khi quản trị viên Máy chủ ở trong tab Lưu trữ tệp, bạn có thể tải trực tiếp lên Máy chủ hoặc thay đổi nhà cung cấp lưu trữ tệp thành Hệ thống tệp cục bộ hoặc Azure Blob Storage.


![image](assets/en/091.webp)


![image](assets/en/092.webp)


### Tóm tắt kỹ năng


Trong phần này, bạn đã học những nội dung sau:



- Sự khác biệt giữa cài đặt Cửa hàng và Máy chủ, đặc biệt là khi chúng liên quan đến Người dùng, Quyền và Email
- Đặt chính sách trên toàn máy chủ để sử dụng và tạo Lightning hoặc Bitcoin Hot Wallet, đăng ký người dùng mới và thông báo qua email.
- Cách thêm chủ đề tùy chỉnh (thay vì chỉ cung cấp các tùy chọn sáng/tối đơn giản) cũng như tạo logo tùy chỉnh
- Thực hiện các tác vụ bảo trì máy chủ đơn giản thông qua GUI được cung cấp
- Khắc phục sự cố, bao gồm việc tìm nạp thông tin chi tiết cho bất kỳ vùng chứa Docker nào hoặc nút của bạn
- Quản lý lưu trữ tệp


### Đánh giá kiến thức


#### Đánh giá khái niệm KA


Sự khác biệt giữa Vai trò được chỉ định thông qua Cài đặt Máy chủ và Cài đặt Cửa hàng là gì và cách sử dụng tiềm năng của cái này so với cái kia là gì?


#### Đánh giá thực tế KA


Mô tả một số trường hợp sử dụng có thể được bật trong tab Chính sách.


#### Đánh giá thực tế KA


Mô tả một số hành động mà người quản trị có thể thực hiện thường xuyên trong tab Bảo trì.


## Máy chủ BTCPay - Thanh toán


<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>


Invoice là tài liệu mà người bán cấp cho người mua để thu tiền.


Trong BTCPay Server, Invoice đại diện cho một chứng từ phải được thanh toán trong một khoảng thời gian xác định với mức giá cố định của Exchange. Hóa đơn có ngày hết hạn vì chúng khóa mức giá Exchange trong một khung thời gian cụ thể, bảo vệ người nhận khỏi biến động giá.


Cốt lõi của BTCPay Server là khả năng hoạt động như một hệ thống quản lý Bitcoin Invoice. Invoice là một công cụ thiết yếu để theo dõi và quản lý các khoản thanh toán đã nhận.


Trừ khi bạn sử dụng [Wallet](https://docs.btcpayserver.org/Wallet/) tích hợp sẵn để nhận thanh toán thủ công, tất cả các khoản thanh toán trong cửa hàng sẽ được hiển thị trên trang Hóa đơn. Trang này sắp xếp các khoản thanh toán theo ngày và đóng vai trò là nguồn tài nguyên trung tâm để quản lý Invoice và khắc phục sự cố thanh toán.


![image](assets/en/093.webp)


### Tổng quan


#### Trạng thái Invoice


Bảng dưới đây liệt kê và mô tả các trạng thái Invoice tiêu chuẩn trong BTCPay, cùng với các hành động phổ biến được đề xuất. Các hành động chỉ mang tính chất khuyến nghị. Người dùng tự xác định phương án hành động phù hợp nhất với trường hợp sử dụng và doanh nghiệp của mình.


| Invoice Status             | Description                                                                                                                             | Action                                                                                                                      |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| New                        | Not paid, invoice timer still has not expired                                                                                           | None                                                                                                                        |
| New (paidPartial)          | Paid, not in full, invoice timer still has not expired                                                                                  | None                                                                                                                        |
| Expired                    | Not paid, invoice timer expired                                                                                                         | None                                                                                                                        |
| Expired (paidPartial) \*\* | Paid, not in full amount, and expired                                                                                                   | Contact buyer to arrange a refund or ask for them to pay their due. Optionally mark the invoice as settled or invalid           |
| Expired (paidLate)         | Paid, in full amount, after the invoice timer has expired                                                                               | Contact buyer to arrange a refund or process order if late confirmations are acceptable.                                    |
| Settled (paidOver)         | Paid more than the invoice amount, settled, received sufficient amount of confirmations                                                 | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing                 | Paid in full, but has not received sufficient amount of confirmations specified in the store settings                                   | Contact buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you                         |
| Processing (paidOver)      | Paid more than the invoice amount, not received sufficient amount of confirmations                                                      | Wait to be settled, then contact the  buyer to arrange a refund for the extra amount, or optionally wait for buyer to contact you |
| Settled                    | Paid, in full, received sufficient amount of confirmations in store                                                                     | Fulfil the order                                                                                                            |
| Settled (marked)           | Status was manually changed to settled from a processing or invalid status                                                             | Store admin has marked the payment as settled                                                                               |
| Invalid\*                  | Paid, but failed to receive sufficient amount of confirmations within the time specified in store settings                              | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |
| Invalid (marked)           | Status was manually changed to invalid from a settled or expired status                                                                 | Store admin has marked the payment as invalid                                                                               |
| Invalid (paidOver)         | Paid more than the invoice amount, but failed to receive sufficient amount of confirmations within the time specified in store settings | Check the transaction on a blockchain explorer, if it received sufficient confirmations, mark as settled                    |

#### Chi tiết Invoice


Trang chi tiết về Invoice chứa tất cả thông tin liên quan đến Invoice.


Thông tin Invoice được tạo tự động dựa trên trạng thái Invoice, tỷ giá Exchange, v.v. Thông tin sản phẩm được tạo tự động nếu Invoice được tạo bằng thông tin sản phẩm, chẳng hạn như trong ứng dụng Điểm bán hàng.


#### Lọc Invoice


Hóa đơn có thể được lọc thông qua bộ lọc nhanh nằm cạnh nút tìm kiếm hoặc bộ lọc nâng cao, có thể được bật/tắt bằng cách nhấp vào liên kết (Trợ giúp) ở trên cùng. Người dùng có thể lọc hóa đơn theo cửa hàng, ID đơn hàng, ID mặt hàng, trạng thái hoặc ngày.


#### Xuất khẩu Invoice


Hóa đơn Máy chủ BTCPay có thể được xuất sang định dạng CSV hoặc JSON. Để biết thêm thông tin về xuất và kế toán Invoice.


#### Hoàn tiền cho Invoice


Nếu vì bất kỳ lý do gì bạn muốn hoàn lại tiền, bạn có thể dễ dàng tạo yêu cầu hoàn lại tiền từ chế độ xem Invoice.


#### Lưu trữ hóa đơn


Do tính năng không sử dụng lại Address của Máy chủ BTCPay, bạn thường thấy nhiều hóa đơn đã hết hạn trên trang Invoice của cửa hàng. Để ẩn chúng, hãy chọn chúng trong danh sách và đánh dấu là đã lưu trữ. Các hóa đơn đã được đánh dấu là đã lưu trữ sẽ không bị xóa. Thanh toán cho Invoice đã lưu trữ vẫn sẽ được Máy chủ BTCPay của bạn phát hiện (trạng thái paidLate). Bạn có thể xem hóa đơn đã lưu trữ của cửa hàng bất cứ lúc nào bằng cách chọn hóa đơn đã lưu trữ từ danh sách thả xuống của bộ lọc tìm kiếm.


#### Tiền tệ mặc định


Lưu trữ loại tiền tệ mặc định được thiết lập tại trình hướng dẫn tạo cửa hàng.


#### Cho phép bất kỳ ai tạo Invoice


Bạn nên bật tùy chọn này nếu muốn cho phép bên ngoài tạo hóa đơn trong cửa hàng của mình. Tùy chọn này chỉ hữu ích nếu bạn đang sử dụng nút thanh toán hoặc nếu bạn đang phát hành hóa đơn qua API hoặc trang web HTML của bên thứ ba. Ứng dụng PoS đã được ủy quyền trước và không yêu cầu bật cài đặt này để khách truy cập ngẫu nhiên có thể mở cửa hàng POS của bạn và tạo Invoice.


#### Thêm một khoản phí bổ sung (phí mạng) vào Invoice



- Chỉ khi khách hàng thực hiện nhiều hơn một khoản thanh toán cho Invoice
- Trên mỗi khoản thanh toán
- Không bao giờ thêm phí mạng


#### Invoice sẽ hết hạn nếu số tiền đầy đủ chưa được thanh toán sau .. Phút.


Bộ đếm thời gian Invoice được đặt mặc định là 15 phút. Bộ đếm thời gian này đóng vai trò như một cơ chế bảo vệ chống lại sự biến động, vì nó khóa số tiền điện tử dựa trên tỷ giá tiền điện tử sang tiền pháp định. Nếu khách hàng không thanh toán Invoice trong khoảng thời gian quy định, Invoice sẽ được coi là hết hạn. Invoice được coi là "đã thanh toán" ngay khi giao dịch hiển thị trên Blockchain (không có xác nhận nào), và được coi là "hoàn tất" khi đạt đến số xác nhận mà nhà cung cấp đã xác định (thường là 1-6). Bộ đếm thời gian có thể tùy chỉnh.


#### Hãy xem xét Invoice đã trả tiền ngay cả khi số tiền trả ít hơn ..% so với dự kiến.


Trong trường hợp khách hàng sử dụng Exchange Wallet để thanh toán trực tiếp cho Invoice, Exchange sẽ tính một khoản phí nhỏ. Điều này có nghĩa là Invoice đó chưa được coi là đã hoàn tất thanh toán. Invoice được đánh dấu là "đã thanh toán một phần". Nếu nhà cung cấp muốn chấp nhận các hóa đơn chưa thanh toán, bạn có thể đặt tỷ lệ phần trăm tại đây.


### Yêu cầu


Yêu cầu Thanh toán là một tính năng cho phép chủ cửa hàng BTCPay tạo hóa đơn dài hạn. Tiền được thanh toán theo yêu cầu thanh toán, sử dụng tỷ giá Exchange có hiệu lực tại thời điểm thanh toán. Tính năng này cho phép người dùng thanh toán theo ý muốn mà không cần phải thương lượng hoặc xác minh tỷ giá Exchange với chủ cửa hàng tại thời điểm thanh toán.


Người dùng có thể thanh toán từng phần cho các yêu cầu. Yêu cầu thanh toán sẽ vẫn có hiệu lực cho đến khi được thanh toán toàn bộ hoặc nếu chủ cửa hàng yêu cầu thời gian hết hạn. Địa chỉ không bao giờ được sử dụng lại. Một mã Address mới sẽ được tạo mỗi khi người dùng nhấp vào nút thanh toán để tạo mã Invoice cho yêu cầu thanh toán.


Chủ cửa hàng có thể in yêu cầu thanh toán (hoặc xuất dữ liệu Invoice) để lưu trữ hồ sơ và kế toán. BTCPay tự động gắn nhãn hóa đơn là Yêu cầu Thanh toán trong danh sách Invoice của cửa hàng bạn.


#### Tùy chỉnh yêu cầu thanh toán của bạn



- Số tiền Invoice - Đặt số tiền thanh toán được yêu cầu
- Mệnh giá - Hiển thị số tiền yêu cầu bằng tiền pháp định hoặc tiền điện tử
- Số lượng thanh toán - Chỉ cho phép thanh toán một lần hoặc thanh toán một phần
- Thời gian hết hạn - Cho phép thanh toán cho đến một ngày nhất định hoặc không hết hạn
- Mô tả - Trình soạn thảo văn bản, Bảng dữ liệu, Nhúng ảnh và video
- Giao diện - Màu sắc và Kiểu dáng với Chủ đề CSS


![image](assets/en/094.webp)


#### Tạo yêu cầu thanh toán


Trong menu bên trái, hãy vào Yêu cầu thanh toán và nhấp vào "Tạo yêu cầu thanh toán".


![image](assets/en/095.webp)


Cung cấp Tên yêu cầu, Số tiền, Mệnh giá hiển thị, Cửa hàng liên kết, Thời gian hết hạn & Mô tả (Tùy chọn)


Chọn tùy chọn Cho phép người nhận tạo hóa đơn theo mệnh giá của họ nếu bạn muốn cho phép thanh toán một phần.


Nhấp vào Lưu & Xem để xem lại yêu cầu thanh toán của bạn.


BTCPay tạo một URL cho yêu cầu thanh toán. Chia sẻ URL này để xem yêu cầu thanh toán của bạn. Cần nhiều yêu cầu giống nhau? Bạn có thể sao chép các yêu cầu thanh toán bằng tùy chọn Sao chép trong menu chính.


![image](assets/en/096.webp)


**CẢNH BÁO**


Yêu cầu thanh toán phụ thuộc vào cửa hàng, nghĩa là mỗi yêu cầu thanh toán được liên kết với một cửa hàng trong quá trình tạo. Hãy đảm bảo bạn đã kết nối Wallet với cửa hàng chứa yêu cầu thanh toán đó.


#### Yêu cầu trả phí


Người nhận tiền và người yêu cầu có thể xem trạng thái của yêu cầu thanh toán sau khi khoản thanh toán đã được gửi. Trạng thái sẽ hiển thị là Đã thanh toán nếu khoản thanh toán đã được nhận đầy đủ. Nếu chỉ thanh toán một phần, Số tiền phải trả sẽ hiển thị số dư còn lại.


![image](assets/en/097.webp)


#### Tùy chỉnh yêu cầu thanh toán


Nội dung mô tả có thể được chỉnh sửa bằng trình soạn thảo văn bản của yêu cầu thanh toán. Cả hai tùy chọn đều khả dụng nếu bạn muốn sử dụng thêm chủ đề màu hoặc tùy chỉnh kiểu CSS.


Người dùng không rành về kỹ thuật có thể sử dụng [giao diện bootstrap](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Có thể tùy chỉnh thêm bằng cách cung cấp thêm mã CSS, như minh họa bên dưới.


```css
:root {
--btcpay-font-family-base: "Source Sans Pro", -apple-system,
BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--btcpay-primary: #7d4698;
--btcpay-primary-accent: #59316b;
--btcpay-body-text: #333a41;
--btcpay-body-bg: #fff;
--btcpay-bg-tile: #f8f9fa;
}

#mainNav {
color: white;
background: linear-gradient(#59316b, #331840);
}

#mainNav .btn-link {
color: white;
}
```


### Kéo thanh toán


Theo truyền thống, người nhận chia sẻ Bitcoin Address của họ để thực hiện thanh toán Bitcoin, và sau đó người gửi sẽ gửi tiền đến Address này. Hệ thống này được gọi là thanh toán Đẩy (Push payment), vì người gửi khởi tạo thanh toán khi người nhận có thể không có mặt, đẩy khoản thanh toán đến người nhận.


Tuy nhiên, nếu đảo ngược vai trò thì sao?


Điều gì sẽ xảy ra nếu thay vì người gửi đẩy khoản thanh toán, người gửi cho phép người nhận rút khoản thanh toán vào thời điểm người nhận thấy phù hợp? Đây chính là khái niệm về thanh toán Kéo. Điều này cho phép một số ứng dụng mới, chẳng hạn như:



- Dịch vụ đăng ký (nơi người đăng ký cho phép dịch vụ rút tiền sau mỗi x khoảng thời gian)
- Hoàn tiền (nơi người bán cho phép khách hàng rút tiền hoàn lại vào tài khoản Wallet của họ khi họ thấy phù hợp)
- Thanh toán theo thời gian cho người làm việc tự do (trong đó người thuê cho phép người làm việc tự do rút tiền vào tài khoản Wallet của họ khi thời gian được báo cáo)
- Sự bảo trợ (nơi người bảo trợ cho phép người nhận rút tiền hàng tháng để tiếp tục hỗ trợ công việc của họ)
- Bán tự động (khách hàng của Exchange sẽ cho phép Exchange rút tiền từ Wallet của họ để bán tự động hàng tháng)
- Hệ thống rút tiền số dư (nơi dịch vụ khối lượng lớn cho phép người dùng yêu cầu rút tiền từ số dư của họ, sau đó dịch vụ có thể dễ dàng chuyển tất cả các khoản thanh toán cho nhiều người dùng theo các khoảng thời gian cố định)


### Thanh toán


Chức năng thanh toán được liên kết với tính năng [Thanh toán Rút](https://docs.btcpayserver.org/PullPayments/). Tính năng này cho phép bạn tạo các khoản thanh toán trong BTCPay của mình. Tính năng này cho phép bạn xử lý thanh toán rút (hoàn tiền, trả lương hoặc rút tiền).


#### Ví dụ 1: Hoàn tiền


Hãy bắt đầu với ví dụ về hoàn tiền. Khách hàng đã mua một mặt hàng trong cửa hàng của bạn, nhưng rất tiếc, họ phải trả lại. Họ muốn được hoàn tiền. Trong BTCPay, bạn có thể tạo [Hoàn tiền](https://docs.btcpayserver.org/Refund/) và cung cấp cho khách hàng liên kết để nhận tiền. Sau khi khách hàng cung cấp mẫu Address và nhận tiền, thông tin này sẽ được hiển thị trong phần Thanh toán.


Trạng thái đầu tiên là Đang chờ phê duyệt. Nhân viên cửa hàng có thể kiểm tra xem có nhiều đơn hàng đang chờ hay không, và sau khi chọn xong, bạn sử dụng nút Hành động.


Tùy chọn trên nút hành động



- Phê duyệt các khoản thanh toán đã chọn
- Phê duyệt và gửi các khoản thanh toán đã chọn
- Hủy các khoản thanh toán đã chọn


Bước tiếp theo là phê duyệt và gửi các khoản thanh toán đã chọn, vì chúng tôi muốn hoàn tiền cho khách hàng. Hãy kiểm tra mẫu Address của Khách hàng, trong đó hiển thị số tiền và liệu chúng tôi có muốn khấu trừ phí vào khoản hoàn tiền hay không. Sau khi hoàn tất việc kiểm tra, bước duy nhất còn lại là ký giao dịch.


Khách hàng hiện được cập nhật trên trang Yêu cầu bồi thường. Khách hàng có thể theo dõi giao dịch vì đã được cung cấp liên kết đến Block explorer và giao dịch của mình. Sau khi giao dịch được xác nhận, trạng thái của giao dịch sẽ chuyển sang "Hoàn tất".


#### Ví dụ 2: Lương


Bây giờ chúng ta hãy tìm hiểu về việc chi trả lương, vì việc này được thực hiện từ bên trong cửa hàng chứ không phải theo yêu cầu của Khách hàng. Khái niệm cơ bản vẫn như vậy; nó sử dụng phương thức thanh toán kéo. Tuy nhiên, thay vì tạo khoản hoàn tiền, chúng ta sẽ thực hiện [Thanh toán kéo](https://docs.btcpayserver.org/PullPayments/).


Vào tab "Thanh toán rút" trên máy chủ BTCPay của bạn. Ở góc trên bên phải, nhấp vào nút "Tạo Thanh toán rút".


Bây giờ chúng ta đang trong quá trình tạo Khoản thanh toán, hãy đặt tên và số tiền mong muốn bằng loại tiền tệ đã chọn. Điền Mô tả để nhân viên biết nội dung của khoản thanh toán. Phần tiếp theo tương tự như hoàn tiền. Nhân viên điền vào mẫu Điểm đến Address và số tiền muốn nhận từ Khoản thanh toán này. Nhân viên có thể quyết định nhận 2 khoản riêng biệt, đến các địa chỉ khác nhau, hoặc thậm chí yêu cầu một phần qua Lightning.


Nếu có nhiều khoản thanh toán đang chờ, bạn có thể nhóm các khoản thanh toán này lại để ký và gửi đi. Sau khi ký, các khoản thanh toán sẽ được chuyển đến tab Đang tiến hành và hiển thị Giao dịch. Khi được mạng lưới chấp nhận, khoản thanh toán sẽ được chuyển đến tab Đã hoàn tất. Tab Đã hoàn tất chỉ dành cho mục đích lịch sử. Tab này chứa các khoản thanh toán đã xử lý và các giao dịch thuộc về nó.


### Kéo thanh toán


#### Ý tưởng


Khi người gửi cấu hình thanh toán Pull, họ có thể cấu hình một số thuộc tính:



- Tên yêu cầu kéo
- Một số lượng giới hạn
- Một đơn vị (như BTC, SAT, USD)
- Phương thức thanh toán
  - BTC On-Chain
  - BTC off-chain
- Sự miêu tả
- CSS tùy chỉnh
- Ngày kết thúc (tùy chọn cho Lightning Network BOLT11)


Sau đó, người gửi có thể chia sẻ khoản thanh toán bằng liên kết với người nhận, cho phép người nhận tạo khoản thanh toán. Người nhận sẽ chọn khoản thanh toán của mình:



- Nên sử dụng phương thức thanh toán nào
- Gửi tiền ở đâu


Sau khi khoản thanh toán được tạo, nó sẽ được tính vào hạn mức thanh toán rút tiền cho kỳ hiện tại. Người gửi sau đó sẽ phê duyệt khoản thanh toán bằng cách thiết lập tỷ giá thanh toán và tiến hành thanh toán.


Đối với người gửi, chúng tôi cung cấp phương pháp dễ sử dụng để gộp nhiều khoản thanh toán từ [BTCPay Internal Wallet](https://docs.btcpayserver.org/Wallet/).


#### API Greenfield


BTCPay Server cung cấp API đầy đủ cho cả người gửi và người nhận, được ghi lại trong trang `/docs` của phiên bản của bạn (hoặc trên trang web tài liệu https://docs.btcpayserver.org)


Vì API của chúng tôi cung cấp đầy đủ khả năng thực hiện thanh toán nên người gửi có thể tự động hóa các khoản thanh toán theo nhu cầu của riêng họ.


### Tóm tắt kỹ năng


Trong phần này, bạn đã học những nội dung sau:



- Hiểu sâu về trạng thái Invoice của Máy chủ BTCPay cũng như các hành động có thể thực hiện trên chúng
- Tùy chỉnh và quản lý các cơ chế Invoice có tuổi thọ cao được gọi là Yêu cầu.
- Các khả năng thanh toán linh hoạt bổ sung được mở ra nhờ tính năng Pull Payment độc đáo của BTCPay Server, đặc biệt là trong việc xử lý hoàn tiền và thanh toán lương.


### Đánh giá kiến thức


#### Đánh giá khái niệm KA


Một số điểm khác biệt giữa hóa đơn và yêu cầu thanh toán là gì và lý do chính đáng để sử dụng yêu cầu thanh toán là gì?


#### Đánh giá khái niệm KA


Thanh toán kéo mở rộng những gì thường được thực hiện trong On-Chain như thế nào? Hãy mô tả một số trường hợp sử dụng mà chúng cho phép.


## Plugin mặc định của máy chủ BTCPay


<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>


### Plugin và ứng dụng mặc định


Máy chủ BTCPay đi kèm với một bộ Plugin (Ứng dụng) tiêu chuẩn có thể biến Máy chủ BTCPay thành một cổng thanh toán thương mại điện tử. Với việc bổ sung thêm Điểm bán hàng, nền tảng Crowdfund và nút Thanh toán dễ dàng, Máy chủ BTCPay trở thành một giải pháp dễ triển khai.


### Điểm bán hàng


Một trong những plugin tiêu chuẩn của BTCPay Server là Point of Sale (PoS). Với plugin PoS, chủ cửa hàng có thể tạo một cửa hàng trực tuyến ngay từ BTCPay Server; chủ cửa hàng không cần giải pháp thương mại điện tử của bên thứ ba để vận hành cửa hàng trực tuyến. Ứng dụng PoS trên nền tảng web cho phép người dùng có cửa hàng truyền thống dễ dàng tích hợp Bitcoin, miễn phí hoặc thông qua bên thứ ba, trực tiếp vào Wallet của họ. PoS có thể dễ dàng hiển thị trên máy tính bảng hoặc các thiết bị khác hỗ trợ duyệt web. Người dùng có thể dễ dàng tạo lối tắt trên màn hình chính để truy cập nhanh vào ứng dụng web.


#### Cách tạo Điểm bán hàng mới


Máy chủ BTCPay cho phép chủ cửa hàng nhanh chóng tạo điểm bán hàng (POS) với nhiều giao diện khác nhau. Máy chủ BTCPay hiểu rằng không phải cửa hàng nào cũng là thương mại điện tử, cũng như không phải cửa hàng nào cũng là quán bar hay nhà hàng, và nó đi kèm với nhiều thiết lập tiêu chuẩn cho POS của bạn.


Khi chủ Cửa hàng nhấp vào "Điểm bán hàng" trên thanh menu bên trái, Máy chủ BTCPay sẽ yêu cầu nhập tên; tên này sẽ hiển thị trên thanh menu bên trái. Nhấp vào Tạo để tạo Điểm bán hàng.


![image](assets/en/098.webp)


#### Cập nhật Điểm bán hàng mới tạo


Sau khi tạo PoS mới, màn hình sau sẽ cho phép bạn cập nhật Điểm bán hàng và thêm mặt hàng cho cửa hàng của mình.


##### Tên ứng dụng


Tên được đặt cho Điểm bán hàng của bạn ở đây sẽ hiển thị trong menu chính của Máy chủ BTCPay.


##### Hiển thị tiêu đề


Công chúng sẽ thấy tiêu đề hoặc tên cửa hàng của bạn khi truy cập. Theo mặc định, Máy chủ BTCPay đặt tên cửa hàng của bạn là "Tiệm trà". Hãy thay thế bằng tên cửa hàng của bạn.


![image](assets/en/099.webp)


#### Chọn phong cách điểm bán hàng


Máy chủ BTCPay có khả năng hiển thị Điểm bán hàng theo nhiều cách.



- Danh sách sản phẩm
  - Chế độ xem cửa hàng nơi khách hàng chỉ có thể mua 1 sản phẩm tại một thời điểm.
- Danh sách sản phẩm có giỏ hàng.
  - Chế độ xem cửa hàng nơi khách hàng có thể mua nhiều mặt hàng cùng lúc và xem tổng quan về giỏ hàng ở bên phải màn hình.
- Chỉ có bàn phím
  - Không có danh sách sản phẩm, chỉ có bàn phím để lập hóa đơn trực tiếp.
- Hiển thị bản in (Danh sách sản phẩm có thể in kèm mã QR)
  - Nếu bạn không thể luôn hiển thị danh sách sản phẩm dưới dạng kỹ thuật số, bạn cần một giải pháp "ngoại tuyến" cho sản phẩm; BTCPay Server có màn hình in để hoạt động như một cửa hàng ngoại tuyến.


![image](assets/en/100.webp)


#### Phong cách điểm bán hàng - Danh sách sản phẩm


![image](assets/en/101.webp)


#### Phong cách điểm bán hàng - Danh sách sản phẩm + Giỏ hàng


![image](assets/en/102.webp)


#### Kiểu điểm bán hàng - Chỉ có bàn phím


![image](assets/en/103.webp)


#### Phong cách điểm bán hàng - Hiển thị bản in


![image](assets/en/104.webp)


#### Tiền tệ


Chủ cửa hàng có thể đặt đơn vị tiền tệ khác cho Điểm bán hàng của mình so với đơn vị tiền tệ mặc định chung. Đơn vị tiền tệ mặc định của cửa hàng sẽ tự động điền vào trường này.


#### Sự miêu tả


Hãy giới thiệu cửa hàng của bạn với mọi người; bạn đang bán gì và với giá bao nhiêu? Mọi thông tin về cửa hàng của bạn sẽ được trình bày tại đây.


![image](assets/en/105.webp)


#### Các sản phẩm


Khi Điểm Bán Hàng được tạo, Máy chủ BTCPay tiêu chuẩn sẽ thêm một vài mặt hàng vào cửa hàng để tham khảo. Nhấp vào nút Chỉnh sửa trên bất kỳ mặt hàng tiêu chuẩn nào để hiểu rõ hơn về từng tùy chọn có thể có cho một mặt hàng.


Việc tạo sản phẩm mới trong cửa hàng của bạn bao gồm các trường sau;



- Tiêu đề
- Giá (cố định, tối thiểu hoặc tùy chỉnh)
- URL hình ảnh
- Sự miêu tả
- Hàng tồn kho
- NHẬN DẠNG
- Văn bản nút Mua.
- Bật/Tắt


Sau khi chủ cửa hàng đã điền đầy đủ thông tin vào tất cả các trường sản phẩm mới, hãy nhấp vào lưu và bạn sẽ thấy mục Sản phẩm trong Điểm bán hàng hiện đang được điền đầy đủ thông tin. Luôn lưu ở góc trên bên phải màn hình để tránh trường hợp chủ cửa hàng có thể mất tiến trình khi thêm sản phẩm.


Chủ cửa hàng cũng có thể sử dụng "Trình chỉnh sửa thô" để cấu hình sản phẩm. Trình chỉnh sửa thô yêu cầu hiểu biết cơ bản về cấu trúc JSON.


![image](assets/en/106.webp)


#### Thanh toán


Máy chủ BTCPay cho phép tùy chỉnh quy trình thanh toán PoS nhỏ. Chủ cửa hàng có thể đặt dòng chữ "Mua với giá x" hoặc yêu cầu dữ liệu khách hàng cụ thể bằng cách thêm vào biểu mẫu.


#### Mẹo


Chỉ một số cửa hàng cần tùy chọn "Tiền boa" cho doanh số bán hàng. Chủ cửa hàng có thể bật hoặc tắt tùy ý cho phù hợp với cửa hàng của mình. Nếu cửa hàng sử dụng tiền boa được bật, chủ cửa hàng có thể nhập nội dung vào trường "Tiền boa" mà họ muốn. Tiền boa của Máy chủ BTCPay hoạt động dựa trên số phần trăm. Chủ cửa hàng có thể thêm nhiều phần trăm, phân cách bằng dấu phẩy.


#### Giảm giá


Là chủ cửa hàng, bạn có thể muốn giảm giá tùy chỉnh cho khách hàng khi thanh toán; nút chuyển đổi Giảm giá sẽ có sẵn khi thanh toán tại cửa hàng của bạn. Tuy nhiên, khuyến cáo không nên sử dụng hệ thống tự thanh toán.


#### Thanh toán tùy chỉnh


Khi tùy chọn Thanh toán tùy chỉnh được bật, khách hàng có thể nhập mức giá cố định bằng hoặc cao hơn Invoice ban đầu do cửa hàng tạo ra.


#### Tùy chọn bổ sung


Sau khi thiết lập mọi thứ cho Điểm bán hàng, vẫn còn một số tùy chọn bổ sung. Chủ cửa hàng có thể dễ dàng nhúng POS của mình thông qua Iframe hoặc nhúng nút thanh toán liên kết đến một mặt hàng cụ thể trong cửa hàng. Để tạo phong cách cho cửa hàng PoS vừa tạo, chủ cửa hàng có thể thêm CSS tùy chỉnh vào cuối các tùy chọn bổ sung.


#### Xóa ứng dụng này


Nếu chủ cửa hàng muốn xóa hoàn toàn Điểm bán hàng khỏi Máy chủ BTCPay, ở cuối quá trình cập nhật PoS, chủ cửa hàng có thể nhấp vào nút "Xóa ứng dụng này" để xóa hoàn toàn ứng dụng PoS. Khi nhấp vào "Xóa ứng dụng này", Máy chủ BTCPay sẽ yêu cầu xác nhận bằng cách nhập `DELETE` và xác nhận bằng cách nhấp vào nút "Xóa". Sau khi xóa, chủ cửa hàng sẽ quay lại bảng điều khiển Máy chủ BTCPay.


### Máy chủ BTCPay - Crowdfund


Bên cạnh plugin Point of Sale, BTCPay Server còn có tùy chọn tạo quỹ cộng đồng. Giống như bất kỳ nền tảng Crowdfund nào khác, chủ cửa hàng có thể đặt mục tiêu, tạo đặc quyền cho các khoản đóng góp và tùy chỉnh theo nhu cầu của mình.


#### Cách thiết lập một quỹ cộng đồng mới


Nhấp vào plugin Crowdfund thông qua menu chính bên trái Máy chủ BTCPay của bạn, bên dưới phần Plugin. Máy chủ BTCPay sẽ yêu cầu tên cho Crowdfund; tên này cũng sẽ được hiển thị trên thanh menu bên trái.


![image](assets/en/107.webp)


#### Cập nhật Điểm bán hàng mới tạo


Sau khi đặt tên cho ứng dụng, màn hình tiếp theo sẽ là cập nhật ứng dụng để có ngữ cảnh.


#### Tên ứng dụng


Tên được đặt cho Crowdfund của bạn sẽ hiển thị trong menu chính của Máy chủ BTCPay.


#### Hiển thị tiêu đề


Tên gọi này được đặt cho Crowdfund dành cho công chúng.


#### Khẩu hiệu


Đưa ra một câu giới thiệu ngắn gọn để mọi người biết mục đích của hoạt động gây quỹ là gì.


![image](assets/en/108.webp)


#### URL hình ảnh nổi bật


Mỗi đợt gây quỹ cộng đồng đều có hình ảnh chính, một banner mà bạn dễ dàng nhận ra. Hình ảnh này có thể được lưu trữ trên máy chủ của bạn nếu bạn có quyền Quản trị. Quản trị viên có thể tải lên trong phần Cài đặt Máy chủ BTCPay - Tệp. Khi bạn là chủ Cửa hàng, hình ảnh phải được tải lên web thông qua máy chủ của bên thứ ba (ví dụ: Imgur).


#### Công khai Crowdfund


Nút chuyển đổi này sẽ giúp Crowdfund của bạn được công khai và hiển thị với bên ngoài. Để kiểm tra hoặc xem chủ đề của bạn đã được áp dụng đúng chưa, hãy giữ nút này ở trạng thái TẮT trong suốt quá trình xây dựng crowdfund.


#### Sự miêu tả


Hãy chia sẻ với mọi người về Quỹ cộng đồng của bạn. Bạn đang gây quỹ vì mục đích gì? Mọi thông tin về quỹ cộng đồng của bạn sẽ được đăng tải tại đây.


![image](assets/en/109.webp)


#### Mục tiêu gây quỹ cộng đồng


Đặt mục tiêu cho số tiền mà người gây quỹ sẽ kiếm được từ dự án và loại tiền tệ mà mục tiêu đó sẽ được tính theo. Đảm bảo rằng nếu mục tiêu của bạn được đặt ra trong khoảng thời gian nhất định, hãy đưa ngày mục tiêu và ngày kết thúc này vào phần Mục tiêu trong gây quỹ cộng đồng.


![image](assets/en/110.webp)


#### Quyền lợi


Ưu đãi có thể cải thiện đáng kể nỗ lực gây quỹ cộng đồng của bạn. Lý do là vì ưu đãi cho phép mọi người tham gia vào chiến dịch của bạn. Chúng khai thác cả động lực ích kỷ lẫn nhân đạo. Và chúng cho phép bạn tiếp cận chi tiêu của những người ủng hộ, chứ không chỉ là khoản tiền từ thiện của họ -- bạn có thể đoán được điều nào quan trọng hơn.


Để tạo một đặc quyền mới, bạn cần điền vào các trường sau.



- Tiêu đề
- Giá (cố định, tối thiểu hoặc tùy chỉnh)
- URL hình ảnh
- Sự miêu tả
- Hàng tồn kho
- NHẬN DẠNG
- Văn bản nút Mua.
- Bật/Tắt


Sau khi chủ cửa hàng đã điền đầy đủ thông tin cho tất cả các trường của đặc quyền mới, hãy nhấp vào lưu và bạn sẽ thấy phần Đặc quyền trong Crowdfunds hiện đang được điền đầy đủ thông tin.


![image](assets/en/111.webp)


### Máy chủ BTCPay - Điểm bán hàng


#### Đóng góp


Chủ cửa hàng có thể chọn cách hiển thị, cách sắp xếp hoặc thậm chí xếp hạng các đặc quyền này so với các đặc quyền khác. Tuy nhiên, khi đạt được mục tiêu gây quỹ cộng đồng, chủ cửa hàng có thể muốn ngừng nhận quyên góp cho chiến dịch gây quỹ này. Do đó, họ có thể bật tùy chọn "Không cho phép đóng góp thêm sau khi đạt được mục tiêu". Điều này sẽ ngăn Crowdfund chấp nhận quyên góp.


##### Hành vi huy động vốn cộng đồng


Tiêu chuẩn của Crowdfund chỉ tính các hóa đơn được tạo bằng Crowdfund vào mục tiêu. Tuy nhiên, có thể có những trường hợp chủ Cửa hàng muốn tất cả các hóa đơn được tạo trong cửa hàng này đều được tính vào quỹ gây quỹ cộng đồng.


#### Tùy chọn bổ sung để tùy chỉnh


Máy chủ BTCpay cung cấp một vài tùy chỉnh bổ sung. Thêm âm thanh, hình ảnh động hoặc thậm chí là chủ đề thảo luận vào Crowdfund. Chủ cửa hàng cũng có thể tùy chỉnh giao diện của Crowdfund bằng cách nhập mã CSS tùy chỉnh của riêng họ.


#### Xóa ứng dụng này


Nếu chủ cửa hàng muốn xóa hoàn toàn Crowdfund khỏi Máy chủ BTCPay, ở cuối quá trình cập nhật Crowdfund, họ có thể nhấp vào nút "Xóa ứng dụng này" để xóa hoàn toàn ứng dụng Crowdfund. Khi nhấp vào "Xóa ứng dụng này", Máy chủ BTCPay sẽ yêu cầu xác nhận bằng cách nhập `DELETE` và xác nhận bằng cách nhấp vào nút "Xóa". Sau khi xóa, chủ cửa hàng sẽ quay lại bảng điều khiển Máy chủ BTCPay.


### Máy chủ BTCPay - Nút thanh toán


HTML dễ dàng nhúng và các nút thanh toán có thể tùy chỉnh cao cho phép chủ cửa hàng nhận tiền boa và quyên góp. Trên thanh menu bên trái của Máy chủ BTCPay, bên dưới phần Plugin, chủ cửa hàng có thể nhấp vào "Nút Thanh toán" và nhấp vào Bật để tạo nút Thanh toán.


#### Cài đặt chung


Trong Cài đặt chung cho Nút thanh toán, chủ cửa hàng có thể thiết lập



- Giá tiêu chuẩn
- Tiền tệ mặc định
- Phương thức thanh toán mặc định
  - Sử dụng mặc định của cửa hàng
  - BTC On-Chain
  - BTC off-chain (Lightning)
  - BTC off-chain (LNURL-pay)
- Mô tả thanh toán
- Mã đơn hàng


#### Tùy chọn hiển thị


Nút Thanh toán của Máy chủ BTCPay có thể được cấu hình để phù hợp với nhiều phong cách khác nhau. Các nút có thể có số tiền cố định hoặc tùy chỉnh, được hiển thị bằng thanh trượt hoặc nút cộng và trừ.


#### Sử dụng Modal


Khi tạo nút thanh toán, chủ cửa hàng có thể chọn cách thức hoạt động của nút khi khách hàng nhấp vào và hiển thị nút đó dưới dạng cửa sổ bật lên hoặc trang mới.


**!?Ghi chú!?**


Cảnh báo: Nút Thanh toán chỉ nên được sử dụng để nhận tiền boa và quyên góp


Không khuyến khích sử dụng nút thanh toán cho tích hợp thương mại điện tử vì người dùng có thể sửa đổi thông tin liên quan đến đơn hàng. Đối với thương mại điện tử, bạn nên sử dụng API Greenfield của chúng tôi. Nếu cửa hàng này xử lý các giao dịch thương mại, chúng tôi khuyên bạn nên tạo một cửa hàng riêng trước khi sử dụng nút thanh toán.


#### Tùy chỉnh văn bản nút Thanh toán


Theo mặc định, nút thanh toán của Máy chủ BTCPay hiển thị "Thanh toán bằng BTCPay". Chủ cửa hàng có thể tùy chỉnh văn bản này theo ý muốn và thay đổi logo Máy chủ BTCPay thành logo của riêng họ. Hãy tùy chỉnh văn bản bằng cách sử dụng "Văn bản Nút Thanh toán" và dán URL hình ảnh bên dưới "URL Hình ảnh Nút Thanh toán".


##### Kích thước hình ảnh


Kích thước của hình ảnh trong nút chỉ có thể được thiết lập theo ba giá trị mặc định.



- 146x40px
- 168x46px
- 209x57px


#### Loại nút


Máy chủ BTCPay biết ba trạng thái của Nút thanh toán.



- Số tiền cố định
  - Giá đã đặt trước đó nằm trong phần cài đặt chung của nút.
- Số tiền tùy chỉnh
  - Nút Thanh toán của Máy chủ BTCPay có nút chuyển đổi + và - để đặt giá tùy chỉnh.
  - Khi sử dụng số tiền tùy chỉnh, Máy chủ BTCPay sẽ yêu cầu số tiền Tối thiểu, Tối đa và mức tăng dần như thế nào.
  - Các nút có thể được đặt thành “Sử dụng kiểu nhập đơn giản”. Thao tác này sẽ xóa nút chuyển đổi +/-.
  - Nút vừa vặn với vị trí nút và nút chuyển đổi xuất hiện trong dòng.
- Thanh trượt
  - Tuy nhiên, tương tự như số tiền tùy chỉnh, nhưng nó có sự khác biệt về mặt hình ảnh vì có thanh trượt thay vì nút chuyển đổi +/-.
  - Khi sử dụng Thanh trượt, Máy chủ BTCPay sẽ yêu cầu giá trị Min, Max và mức tăng dần như thế nào.


**!?Ghi chú!?**


Bạn có thể xóa nút Thanh toán ở đầu phần mô tả cảnh báo.


#### Thông báo thanh toán


IPN máy chủ (Thông báo thanh toán tức thì) được thiết kế cho webhooks và có thể được cấu hình bằng URL tới dữ liệu sau khi mua hàng.


#### Thông báo qua email


Bất cứ khi nào có khoản thanh toán được thực hiện, Máy chủ BTCPay có thể thông báo cho chủ cửa hàng.


#### Chuyển hướng trình duyệt


Khi khách hàng hoàn tất giao dịch mua hàng, họ sẽ được chuyển hướng đến liên kết này nếu được chủ cửa hàng thiết lập.


#### Tùy chọn nút thanh toán nâng cao


Chỉ định các tham số chuỗi truy vấn bổ sung cần được thêm vào trang thanh toán sau khi Invoice được tạo. Ví dụ: `lang=da-DK` sẽ tải trang thanh toán bằng tiếng Đan Mạch theo mặc định.


#### Sử dụng ứng dụng làm điểm cuối


Bạn có thể liên kết trực tiếp nút thanh toán với một mục trong một trong các ứng dụng PoS hoặc Crowdfund mà bạn đã sử dụng trước đó.


Chủ cửa hàng có thể nhấp vào menu thả xuống và chọn Ứng dụng mong muốn; sau khi chọn Ứng dụng, chủ cửa hàng có thể thêm mặt hàng cần liên kết.


#### Mã được tạo


Vì nút Thanh toán của Máy chủ BTCPay là mã HTML dễ nhúng nên Máy chủ BTCPay sẽ hiển thị mã đã tạo để sao chép vào trang web ở phía dưới sau khi cấu hình nút Thanh toán.


Chủ cửa hàng có thể sao chép mã đã tạo vào trang web của mình và nút Thanh toán từ Máy chủ BTCPay sẽ hoạt động trực tiếp trên trang web của họ.


#### Thông báo thanh toán


IPN máy chủ (Thông báo thanh toán tức thì) được thiết kế cho webhooks và có thể được cấu hình bằng URL để đăng dữ liệu mua hàng.


#### Thông báo qua email


Bất cứ khi nào có khoản thanh toán được thực hiện, Máy chủ BTCPay có thể thông báo cho chủ cửa hàng.


#### Chuyển hướng trình duyệt


Khi khách hàng hoàn tất giao dịch mua hàng, họ sẽ được chuyển hướng đến liên kết này nếu được chủ cửa hàng thiết lập.


#### Tùy chọn nút thanh toán nâng cao


Chỉ định các tham số chuỗi truy vấn bổ sung cần được thêm vào trang thanh toán sau khi tạo Invoice. Ví dụ: `lang=da-DK` sẽ tải trang thanh toán bằng tiếng Đan Mạch theo mặc định.


#### Sử dụng ứng dụng làm điểm cuối


Bạn có thể liên kết trực tiếp nút thanh toán với một mặt hàng trong một trong các ứng dụng PoS hoặc Crowdfund mà bạn đã sử dụng trước đó. Chủ cửa hàng có thể nhấp vào menu thả xuống và chọn ứng dụng mong muốn. Sau khi chọn ứng dụng, chủ cửa hàng có thể thêm mặt hàng cần liên kết.


#### Mã được tạo


Vì nút Thanh toán của Máy chủ BTCPay là một mã HTML dễ nhúng, Máy chủ BTCPay sẽ hiển thị mã đã tạo để sao chép vào trang web ở cuối trang sau khi cấu hình nút Thanh toán. Chủ cửa hàng có thể sao chép mã đã tạo vào trang web của mình, và nút Thanh toán từ Máy chủ BTCPay sẽ được kích hoạt trực tiếp trên trang web của họ.


### Tóm tắt kỹ năng


Trong phần này, bạn đã học:



- Cách sử dụng plugin PoS tích hợp của BTCPay Server để tạo cửa hàng tùy chỉnh dễ dàng
- Cách sử dụng plugin Crowdfund tích hợp của BTCPay Server để tạo ứng dụng crowdfund tùy chỉnh một cách dễ dàng
- Tạo mã cho nút thanh toán tùy chỉnh bằng plugin Nút thanh toán


### Đánh giá kiến thức


#### Đánh giá KA


Ba plugin tích hợp sẵn có trong BTCPay Server là gì? Hãy mô tả ngắn gọn cách sử dụng từng plugin.


# Cấu hình máy chủ BTCPay


<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>


## Hiểu biết cơ bản về việc cài đặt BTCPay Server trên môi trường LunaNode


<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>


### Cài đặt máy chủ BTCPay trên môi trường lưu trữ (LunaNode)


Các bước này sẽ cung cấp tất cả thông tin cần thiết để bắt đầu sử dụng BTCPay Server trên LunaNode. Có nhiều tùy chọn để triển khai phần mềm.

Bạn có thể tìm thấy mọi thông tin chi tiết về BTCPay Server tại https://docs.btcpayserver.org.


#### Chúng ta bắt đầu từ đâu?


Trong phần này, bạn sẽ làm quen với LunaNode với tư cách là nhà cung cấp dịch vụ lưu trữ, tìm hiểu những bước đầu tiên khi sử dụng Máy chủ BTCPay và cách sử dụng Lightning Network. Sau khi hoàn thành tất cả các bước, bạn có thể vận hành một cửa hàng trực tuyến hoặc nền tảng gây quỹ cộng đồng chấp nhận Bitcoin!


Đây là một trong nhiều cách triển khai Máy chủ BTCPay. Đọc tài liệu của chúng tôi để biết thêm chi tiết.


https://docs.btcpayserver.org.


### Máy chủ BTCPay - Triển khai LunaNode


#### Triển khai LunaNode


Trước tiên, hãy truy cập trang web LunaNode.com, tại đây chúng ta sẽ tạo một tài khoản mới. Nhấp vào nút Đăng ký ở góc trên bên phải hoặc sử dụng trình hướng dẫn Bắt đầu trên trang chủ của họ.


![image](assets/en/112.webp)


Sau khi bạn tạo tài khoản mới, LunaNode sẽ gửi email xác minh. Sau khi xác minh tài khoản, so với Voltage, bạn sẽ ngay lập tức được cung cấp tùy chọn nạp thêm tiền vào tài khoản. Số tiền này cần thiết để trang trải chi phí lưu trữ và không gian máy chủ.


![image](assets/en/113.webp)


#### Thêm tín dụng vào tài khoản LunaNode của bạn


Sau khi nhấp vào "Nạp tiền", bạn có thể thiết lập số tiền muốn nạp vào tài khoản và phương thức thanh toán. LunaNode và BTCPay Server có giá từ 10 đến 20 đô la mỗi tháng.

So với Voltage.cloud, bạn có toàn quyền truy cập vào Máy chủ Riêng Ảo (VPS) của mình, cho phép bạn kiểm soát máy chủ tốt hơn. Sau khi bạn tạo tài khoản mới, LunaNode sẽ gửi email xác minh.

Sau khi xác minh tài khoản, so với Voltage, bạn sẽ ngay lập tức được cung cấp tùy chọn nạp thêm tiền vào tài khoản. Số tiền này cần thiết để trang trải chi phí lưu trữ và dung lượng máy chủ.


#### Làm thế nào để triển khai máy chủ mới?


Trong hướng dẫn này, chúng tôi sẽ hướng dẫn bạn quy trình thiết lập bằng cách tạo một bộ khóa API và sử dụng trình khởi chạy BTCPay Server do LunaNode phát triển.


Trong bảng điều khiển LunaNode, hãy nhấp vào API ở góc trên bên phải. Thao tác này sẽ mở ra một trang mới. Chúng ta chỉ cần đặt Tên cho khóa API. Phần còn lại sẽ do LunaNode lo và không được đề cập trong hướng dẫn này. Nhấp vào nút Tạo Thông tin Xác thực API.

Sau khi tạo thông tin xác thực API, bạn sẽ nhận được một chuỗi dài các chữ cái và ký tự. Đây chính là khóa API của bạn.


![image](assets/en/114.webp)


#### Làm thế nào để triển khai máy chủ mới?


Thông tin đăng nhập này gồm hai phần: API key và API ID; chúng ta sẽ cần cả hai. Trước khi chuyển sang bước tiếp theo, hãy mở một tab thứ hai trên trình duyệt và truy cập https://launchbtcpay.lunanode.com/


Tại đây, bạn sẽ được yêu cầu cung cấp khóa API và ID API. Điều này cho bạn biết rằng bạn là người cung cấp máy chủ mới này. Khóa API vẫn sẽ được mở trong tab trước đó của bạn; nếu bạn cuộn xuống bảng bên dưới, bạn sẽ tìm thấy ID API.


Bạn có thể quay lại trang có Trình khởi chạy, điền vào các trường có khóa API và ID của bạn, rồi nhấp vào tiếp tục.


![image](assets/en/115.webp)


Ở bước tiếp theo, bạn có thể cung cấp tên miền. Nếu bạn đã sở hữu tên miền và muốn sử dụng tên miền này cho Máy chủ BTCPay, hãy đảm bảo bạn cũng thêm bản ghi DNS (gọi là bản ghi `A`) vào tên miền của mình. Nếu bạn không sở hữu tên miền, hãy sử dụng tên miền do LunaNode cung cấp (bạn có thể thay đổi tên miền này sau trong phần cài đặt Máy chủ BTCPay) và nhấp vào Tiếp tục.


Đọc thêm về cách thiết lập hoặc thay đổi bản ghi DNS cho Máy chủ BTCPay; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name


#### Khởi chạy máy chủ BTCPay trên LunaNode


Sau khi thực hiện các bước trên, chúng ta có thể thiết lập tất cả các tùy chọn cho máy chủ mới. Ở đây, chúng ta sẽ chọn Bitcoin (BTC) làm đơn vị tiền tệ được hỗ trợ. Chúng ta cũng có thể thiết lập email để nhận thông báo về chứng chỉ mã hóa cho mục đích gia hạn, tùy chọn này là tùy chọn.


Hướng dẫn này hướng đến việc thiết lập môi trường Mainnet (Bitcoin thực tế); tuy nhiên, LunaNode cũng cho phép bạn thiết lập môi trường này thành Testnet hoặc Regtest cho mục đích phát triển. Chúng tôi sẽ giữ nguyên tùy chọn Mainnet trong hướng dẫn này.


Bạn có thể chọn triển khai Lightning của mình. LunaNode cung cấp hai triển khai khác nhau: LND và Core Lightning. Trong hướng dẫn này, chúng tôi sẽ sử dụng LND. Có rất ít sự khác biệt giữa cả hai triển khai; để biết thêm thông tin, chúng tôi khuyên bạn nên đọc tài liệu chi tiết: https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln


![image](assets/en/116.webp)


LunaNode cung cấp nhiều gói Máy ảo (VM). Các gói này khác nhau về phạm vi giá và thông số kỹ thuật máy chủ. Trong hướng dẫn này, gói m2 là đủ; tuy nhiên, nếu bạn chọn nhiều loại tiền tệ hơn Bitcoin, hãy cân nhắc sử dụng ít nhất gói m4.


Tăng tốc quá trình đồng bộ hóa Blockchain ban đầu; tùy chọn này tùy thuộc vào nhu cầu của bạn. Có các tùy chọn nâng cao, chẳng hạn như đặt Biệt danh Lightning, trỏ đến một bản phát hành GitHub cụ thể hoặc đặt khóa SSH; hướng dẫn này sẽ không đề cập đến các tùy chọn này.


Sau khi điền vào biểu mẫu, bạn phải nhấp vào "Khởi chạy VM" và Lunanode sẽ bắt đầu tạo VM mới, bao gồm cả Máy chủ BTCPay được cài đặt trên đó. Quá trình này mất vài phút; khi máy chủ của bạn đã sẵn sàng, LunaNode sẽ cung cấp cho bạn liên kết đến Máy chủ BTCPay mới.


Sau quá trình tạo, hãy nhấp vào liên kết đến Máy chủ BTCPay của bạn; tại đây, bạn sẽ được yêu cầu tạo tài khoản Quản trị viên.


![image](assets/en/117.webp)


### Tóm tắt kỹ năng


Trong phần này, bạn đã học:



- Tạo và cấp vốn cho tài khoản trên LunaNode
- Sử dụng BTCPay Server Launcher để tạo máy chủ của riêng bạn


### Đánh giá kiến thức


#### Đánh giá khái niệm KA


Mô tả một số điểm khác biệt giữa việc chạy phiên bản BTCPay Server trên VPS so với việc tạo tài khoản trên phiên bản lưu trữ.


## Cài đặt BTCPay Server trên môi trường Voltage


<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>


Bạn sẽ làm quen với Voltage.cloud với tư cách là nhà cung cấp dịch vụ lưu trữ, tìm hiểu những bước đầu tiên khi sử dụng Máy chủ BTCPay và cách sử dụng Lightning Network. Sau khi chúng ta thực hiện xong tất cả các bước, bạn có thể vận hành một cửa hàng trực tuyến hoặc nền tảng gây quỹ cộng đồng chấp nhận Bitcoin!


Đây là một trong nhiều cách triển khai Máy chủ BTCPay. Đọc tài liệu của chúng tôi để biết thêm chi tiết.

https://docs.btcpayserver.org.


### Máy chủ BTCPay - Triển khai Voltage.cloud


Trước tiên, hãy truy cập trang web Voltage.cloud và đăng ký tài khoản mới. Khi tạo tài khoản, bạn có thể đăng ký dùng thử miễn phí 7 ngày. Nhấp vào nút Đăng ký ở góc trên bên phải hoặc sử dụng mục "Dùng thử miễn phí 7 ngày" trên trang chủ.


![image](assets/en/118.webp)


Sau khi tạo tài khoản, hãy nhấp vào nút `NODES` trên bảng điều khiển. Sau khi chọn Nodes và tạo một node mới, chúng ta sẽ thấy các ưu đãi Voltage có thể có của node đó. Vì hướng dẫn này cũng sẽ đề cập đến Lightning Network, tại Voltage, trước tiên chúng ta cần chọn triển khai Lightning trước khi tạo Máy chủ BTCPay. Nhấp vào LightningNode.


![image](assets/en/119.webp)


Tại đây, bạn sẽ phải chọn loại Lightning node bạn muốn. Voltage có nhiều tùy chọn cho thiết lập chiếu sáng của bạn. Điều này sẽ khác khi triển khai với LunaNode chẳng hạn. Với mục đích của hướng dẫn này, một Lite Node là đủ. Đọc thêm về sự khác biệt trong Voltage.cloud.


![image](assets/en/120.webp)


Đặt tên cho nút của bạn, đặt mật khẩu và bảo mật mật khẩu này. Nếu mật khẩu này bị mất, bạn sẽ mất quyền truy cập vào các bản sao lưu và Voltage không thể khôi phục lại. Hãy tạo nút và Voltage sẽ hiển thị tiến trình. Voltage đã tạo nút Lightning của bạn. Bây giờ chúng ta có thể tạo phiên bản Máy chủ BTCPay và truy cập trực tiếp vào Lightning Network.


Nhấp vào "Nút" ở góc trên bên trái bảng điều khiển. Tại đây, bạn có thể thiết lập phần tiếp theo cho phiên bản Máy chủ BTCPay của mình. Nhấp vào "tạo mới" khi bạn vào phần tổng quan về nút. Bạn sẽ thấy màn hình tương tự như trước. Bây giờ, thay vì Lightning Node, chúng ta chọn Máy chủ BTCPay.


Voltage hiển thị vị trí địa lý của Máy chủ BTCPay, được lưu trữ tại khu vực miền Tây Hoa Kỳ. Tại đây, bạn cũng sẽ thấy chi phí lưu trữ máy chủ. Nhấp vào Tạo và đặt tên cho Máy chủ BTCPay của bạn. Bật Lightning và Voltage sẽ hiển thị nút Lightning đã tạo ở bước trước. Nhấp vào Tạo và Voltage sẽ tạo một phiên bản Máy chủ BTCPay.


![image](assets/en/121.webp)


Sau khi nhấn tạo, Voltage sẽ hiển thị cho bạn tên người dùng và mật khẩu mặc định. Chúng tương tự như mật khẩu bạn đã đặt trước đó trong Voltage. Nhấp vào nút Đăng nhập vào Tài khoản để chuyển hướng bạn đến Máy chủ BTCPay.


Chào mừng bạn đến với phiên bản Máy chủ BTCPay mới của bạn. Vì chúng tôi đã thiết lập Lightning trong quá trình tạo, nên Lightning đã được kích hoạt!


### Tóm tắt kỹ năng


Trong chương này, bạn đã học:



- Tạo tài khoản trên Voltage.cloud
- Các bước để chạy Máy chủ BTCPay cùng với nút Lightning trên tài khoản


### Đánh giá kiến thức


#### Đánh giá khái niệm KA


Một số khác biệt chính giữa thiết lập Voltage và LunaNode là gì?


## Cài đặt Máy chủ BTCPay trên nút Umbrel


<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>


Sau khi hoàn tất các bước này, bạn có thể chấp nhận thanh toán Lightning cho cửa hàng BTCPay trên mạng cục bộ của mình. Quy trình này cũng áp dụng nếu bạn vận hành một nút mạng lưới (umbrel node) trong nhà hàng hoặc doanh nghiệp. Nếu bạn muốn kết nối cửa hàng này với một trang web công cộng, hãy làm theo bài tập Nâng cao để hiển thị nút mạng lưới của bạn cho công chúng.


https://umbrel.com/


![image](assets/en/122.webp)


### Máy chủ BTCPay - Triển khai Umbrel


Sau khi nút Umbrel của bạn đã đồng bộ hoàn toàn với Bitcoin Blockchain, hãy vào Umbrel App Store và tìm kiếm BTCPay Server trong mục Ứng dụng.


![image](assets/en/123.webp)


Nhấp vào Máy chủ BTCPay để xem chi tiết ứng dụng. Khi chi tiết về Máy chủ BTCPay được mở, góc dưới bên phải sẽ hiển thị các yêu cầu để ứng dụng chạy bình thường. Nó cho thấy ứng dụng yêu cầu nút Bitcoin và Lightning. Nếu bạn chưa cài đặt Lightning Node trên Umbrel, hãy nhấp vào Cài đặt. Quá trình này có thể mất vài phút.


![image](assets/en/124.webp)


Sau khi cài đặt Lightning Node của bạn:


1. Nhấp vào mở trong phần chi tiết ứng dụng hoặc trên Ứng dụng trong bảng điều khiển Umbrels.

2. Nhấp vào thiết lập một nút mới; bạn sẽ thấy 24 từ để khôi phục nút sét của mình.

3. Viết những điều này ra.


![image](assets/en/125.webp)


Umbrel sẽ yêu cầu xác minh các từ vừa viết. Sau khi nút Lightning được thiết lập, hãy quay lại Umbrel App Store và tìm Máy chủ BTCPay. Nhấp vào nút cài đặt, Umbrel sẽ hiển thị các thành phần cần thiết đã được cài đặt chưa và Máy chủ BTCPay có yêu cầu quyền truy cập vào các thành phần này hay không. Sau khi cài đặt, hãy nhấp vào nút Mở ở góc trên bên phải của phần Chi tiết ứng dụng hoặc mở Máy chủ BTCPay thông qua bảng điều khiển Umbrel của bạn.


Umbrel sẽ yêu cầu xác minh những từ vừa viết ra.


![image](assets/en/126.webp)


**!?Ghi chú!?**


Đảm bảo rằng bạn lưu trữ chúng ở một nơi an toàn, như đã tìm hiểu trước đó khi lưu trữ khóa.


Sau khi nút Lightning được thiết lập, hãy quay lại Umbrel App Store và tìm Máy chủ BTCPay. Nhấp vào nút cài đặt, Umbrel sẽ hiển thị các thành phần cần thiết đã được cài đặt chưa và Máy chủ BTCPay có yêu cầu quyền truy cập vào các thành phần này hay không.


![image](assets/en/127.webp)


Sau khi cài đặt, hãy nhấp vào Mở ở góc trên bên phải của phần thông tin chi tiết về Ứng dụng hoặc mở Máy chủ BTCPay thông qua bảng điều khiển Umbrels của bạn.


![image](assets/en/128.webp)


### Tóm tắt kỹ năng


Trong phần này, bạn đã học:



- Các bước cài đặt BTCPay Server với chức năng Lightning trên nút Umbrel


### Đánh giá kiến thức


#### Đánh giá khái niệm KA


Thiết lập trên Umbrel khác với hai tùy chọn lưu trữ trước đó như thế nào?


# Phần cuối


<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>




## Đánh giá & Xếp hạng

<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>

<isCourseReview>true</isCourseReview>

## Kết luận khóa học


<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

<isCourseConclusion>true</isCourseConclusion>