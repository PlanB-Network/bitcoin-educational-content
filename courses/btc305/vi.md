---
name: Bitcoin và BTCPay Server
goal: Cài đặt BTCPay Server cho doanh nghiệp của bạn
objectives:
  - Hiểu BTCPay Server là gì.
  - Tự host và cấu hình BTCPay Server.
  - Sử dụng BTCPay Server trong kinh doanh hàng ngày.
---

test

# Bitcoin và BTCPay Server

Đây là một khóa học giới thiệu về Cách vận hành BTCPay Server được viết bởi Alekos và Bas, sau đó được điều chỉnh theo Định dạng Khóa học PlanB bởi melontwist và asi0.

MỘT CÂU CHUYỆN CHƯA KẾT THÚC

"Đây Là Dối Trá, Niềm Tin Của Tôi Nơi Bạn Đã Bị Phá Vỡ, Tôi Sẽ Làm Cho Bạn Trở Nên Lỗi Thời".

Sản xuất bởi Quỹ BTCPay Server

+++

# Giới thiệu

<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>

## Lời khen ngợi dành cho Tác giả của Bitcoin và BTCPay Server

<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>

Hãy bắt đầu với việc BTCPay Server là gì và nó xuất phát từ đâu. Chúng tôi coi trọng sự minh bạch và một số tiêu chuẩn nhất định để tạo dựng niềm tin trong không gian Bitcoin.
Một dự án trong lĩnh vực này đã phá vỡ những giá trị này. Nicolas Dorier, nhà phát triển chính của BTCPay Server, đã coi đó là chuyện cá nhân và hứa sẽ làm cho họ trở nên lỗi thời. Và đây chúng ta, nhiều năm sau, đang làm việc hướng tới tương lai đó, hoàn toàn mã nguồn mở, hàng ngày.

> Đây là dối trá, niềm tin của tôi nơi bạn đã bị phá vỡ, tôi sẽ làm cho bạn trở nên lỗi thời.
> Nicolas Dorier

Sau những lời nói của Nicolas, đã đến lúc bắt đầu xây dựng. Rất nhiều công sức đã được đổ vào cái mà chúng ta bây giờ gọi là BTCPay Server. Nhiều người muốn giúp đỡ với sự đẩy mạnh này. Những người dễ nhận biết nhất là r0ckstardev, MrKukks, Pavlenex, và người bán hàng đầu tiên sử dụng phần mềm này, astupidmoose.

Mã nguồn mở có nghĩa là gì, và điều gì đi vào một dự án như vậy?

FOSS là viết tắt của Free & Open-Source Software (Phần Mềm Miễn Phí và Mã Nguồn Mở). Cái đầu tiên ám chỉ các điều khoản cho phép bất kỳ ai cũng có thể sao chép, chỉnh sửa, và thậm chí phân phối các phiên bản của phần mềm (kể cả với mục đích lợi nhuận). Cái sau ám chỉ việc chia sẻ mã nguồn một cách công khai, khuyến khích công chúng đóng góp và cải thiện nó.
Điều này thu hút những người dùng có kinh nghiệm hứng thú với việc đóng góp vào phần mềm mà họ đã sử dụng và tạo ra giá trị từ đó, chứng minh theo thời gian sẽ chiến thắng trong việc áp dụng so với phần mềm độc quyền. Điều này phù hợp với tinh thần Bitcoin rằng “thông tin khao khát được tự do”. Nó đưa những người đam mê lại với nhau tạo thành một cộng đồng và đơn giản là vui vẻ hơn. Giống như Bitcoin, FOSS là điều không thể tránh khỏi.

### Trước khi chúng ta bắt đầu

Khóa học này bao gồm nhiều phần. Nhiều phần sẽ được giáo viên của bạn trong lớp học đảm nhận, môi trường thử nghiệm mà bạn có quyền truy cập, một máy chủ được host cho bạn, và có thể là một tên miền. Nếu bạn hoàn thành khóa học này một cách độc lập, xin lưu ý rằng các môi trường được ghi nhãn là DEMO sẽ không có sẵn cho bạn.
Lưu ý. Nếu bạn theo dõi khóa học này qua lớp học, tên máy chủ có thể khác nhau tùy thuộc vào cài đặt lớp học của bạn. Biến trong tên máy chủ có thể khác nhau do điều này.

### Cấu trúc Khóa học

Mỗi chương có mục tiêu và đánh giá kiến thức. Trong khóa học này, chúng tôi sẽ đề cập đến từng điều này và có một bản tóm tắt các tính năng chính tại mỗi khối bài học (tức là chương). Hình minh họa được sử dụng để cung cấp phản hồi trực quan và củng cố các khái niệm chính một cách trực quan. Mục tiêu được đặt ra ngay từ đầu mỗi khối bài học. Những mục tiêu này vượt ra ngoài một danh sách kiểm tra. Chúng cung cấp cho bạn một hướng dẫn vào một bộ kỹ năng mới. Đánh giá Kiến thức ngày càng trở nên thách thức hơn trong việc thiết lập BTCPay Server của bạn.

### Học viên nhận được gì từ khóa học?

Với Khóa học BTCPay Server, học viên có thể hiểu được các nguyên tắc cơ bản, kỹ thuật và phi kỹ thuật của Bitcoin. Việc đào tạo kỹ lưỡng trong việc sử dụng Bitcoin thông qua BTCPay Server sẽ cho phép học viên vận hành cơ sở hạ tầng Bitcoin của riêng họ.

### Địa chỉ Web quan trọng hoặc Cơ hội liên hệ

Quỹ BTCPay Server, đã cho phép Alekos và Bas viết khóa học này, đặt tại Tokyo, Nhật Bản. Quỹ BTCPay Server có thể được liên hệ thông qua trang web được liệt kê;

- https://foundation.btcpayserver.org
- tham gia các kênh chat chính thức: https://chat.btcpayserver.org

## Giới thiệu về Bitcoin

<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>

### Hiểu Bitcoin qua bài tập lớp học

Đây là bài tập lớp học nên nếu bạn tham gia khóa học này, bạn không thể thực hiện nó nhưng bạn vẫn có thể tìm hiểu qua bài tập này. Để hoàn thành nhiệm vụ này, số lượng người tối thiểu là từ 9 đến 11.

Bài tập bắt đầu sau khi xem giới thiệu "Làm thế nào Bitcoin và blockchain hoạt động" của BBC.

![how bitcoin and the blockchain works](https://youtu.be/mhE_vvwAiRc)

Bài tập này yêu cầu ít nhất chín người tham gia. Mục đích của bài tập này là để hiểu một cách trực quan về cách hoạt động của Bitcoin. Bằng cách đóng vai từng vai trò trong mạng lưới, bạn sẽ có một cách học tương tác và vui vẻ. Bài tập này không liên quan đến Lightning Network.

### Ví dụ; Yêu cầu 9 / 11 người

Các vai trò là:

- 1 Khách hàng
- 1 Người bán hàng
- 7 đến 9 nút Bitcoin

**Cài đặt như sau:**

Khách hàng mua một sản phẩm từ cửa hàng bằng Bitcoin.

**Kịch bản 1 - Hệ thống Ngân hàng Truyền thống**

- Thiết lập:
  - Xem sơ đồ/giải thích trong Figjam đính kèm - [Sơ đồ Hoạt động](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Chọn ba sinh viên tình nguyện đóng vai Khách hàng (Alice), Người bán hàng (Bob), và Ngân hàng.
- Diễn ra chuỗi sự kiện:
  - Khách hàng- duyệt cửa hàng trực tuyến và tìm thấy một mặt hàng giá $25 mà họ muốn, và thông báo cho Người bán hàng rằng họ muốn mua
  - Người bán hàng- yêu cầu thanh toán.
  - Khách hàng- gửi thông tin thẻ cho Người bán hàng
  - Người bán hàng- chuyển thông tin đến Ngân hàng (xác định cả danh tính của mình và thông tin/danh tính) yêu cầu thanh toán
  - Ngân hàng thu thập thông tin về Khách hàng và Người bán hàng (Alice và Bob) và kiểm tra xem số dư của khách hàng có đủ không.
  - Trừ \$25 từ tài khoản của Alice, cộng \$24 vào tài khoản của Bob, lấy \$1 cho dịch vụ
  - Người bán hàng nhận được sự đồng ý từ Ngân hàng và gửi hàng cho khách hàng.
- Nhận xét:
  - Bob và Alice phải có mối quan hệ với một ngân hàng.
  - Ngân hàng thu thập thông tin định danh về cả Bob và Alice.
  - Ngân hàng nhận một phần.
  - Ngân hàng phải được tin tưởng để giữ tiền của mỗi người tham gia mọi lúc.

**Kịch bản 2 - Hệ thống Bitcoin**

- Thiết lập:
  - Xem sơ đồ/giải thích trong Figjam đính kèm - [Sơ đồ Hoạt động](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
- Thay thế Ngân hàng bằng chín sinh viên sẽ đóng vai trò là Máy tính (Các nút/Thợ đào Bitcoin) trong mạng để thay thế Ngân hàng.
- Mỗi Máy tính trong số 9 máy này có bản ghi lịch sử đầy đủ về tất cả các giao dịch đã từng được thực hiện (do đó, số dư chính xác mà không có sự giả mạo), cũng như một bộ quy tắc:
  - Xác minh giao dịch được ký đúng cách (chìa khóa phù hợp với ổ khóa)
  - Phát sóng và nhận giao dịch hợp lệ từ các đối tác trong mạng, loại bỏ những giao dịch không hợp lệ (bao gồm cả những giao dịch cố gắng chi tiêu cùng một khoản tiền hai lần)
- Cập nhật/Thêm bản ghi định kỳ với các giao dịch mới nhận từ máy tính "ngẫu nhiên" miễn là tất cả nội dung đều hợp lệ (lưu ý: chúng tôi đang bỏ qua, cho đến nay, thành phần Chứng minh Công việc để đơn giản hóa), nếu không thì từ chối những giao dịch này và tiếp tục như trước cho đến khi máy tính "ngẫu nhiên" khác gửi một cập nhật
  - Số tiền thưởng đúng nếu nội dung hợp lệ.
- Diễn ra chuỗi sự kiện:
  - Khách hàng- duyệt cửa hàng trực tuyến và tìm thấy một mặt hàng trị giá $25 mà họ muốn, và thông báo cho Người bán họ muốn mua
  - Người bán- yêu cầu thanh toán bằng cách gửi khách hàng một hóa đơn/địa chỉ từ ví của họ.
  - Khách hàng- tạo một giao dịch (gửi $25 BTC đến địa chỉ do Người bán cung cấp) và phát sóng nó đến Mạng lưới Bitcoin.
- Máy tính- nhận giao dịch và xác minh:
  - Có ít nhất $25 BTC trong địa chỉ được gửi từ
  - Giao dịch được ký đúng cách (“mở khóa” bởi khách hàng)
  - Nếu không phải trường hợp đó, thì giao dịch sẽ không được lan truyền qua mạng, và nếu có, thì nó sẽ được lan truyền và được giữ chờ.
  - Người bán có thể kiểm tra rằng giao dịch đang chờ xử lý.
- Một máy tính được chọn “ngẫu nhiên” để đề xuất hoàn thành giao dịch được đề xuất bằng cách phát sóng “một khối” chứa nó; nếu nó được kiểm tra là hợp lệ, họ sẽ nhận được một phần thưởng BTC.
  - TÙY CHỌN/NÂNG CAO - thay vì chọn ngẫu nhiên Máy tính, mô phỏng việc đào bằng cách yêu cầu Máy tính lắc xúc xắc cho đến khi một kết quả được xác định trước xảy ra (ví dụ: người đầu tiên lắc được đôi sáu là người được chọn)
  - Nó cũng có thể diễn ra những gì sẽ xảy ra nếu hai Máy tính chiến thắng cùng một lúc, dẫn đến việc chia tách chuỗi.
  - Máy tính kiểm tra tính hợp lệ, cập nhật/thêm bản ghi vào sổ cái của họ nếu các quy tắc được đáp ứng, và phát sóng khối cho các đối tác.
  - Máy tính được chọn ngẫu nhiên nhận được phần thưởng cho việc đề xuất một khối hợp lệ.
  - Người bán kiểm tra giao dịch đã được hoàn tất; do đó, tiền đã được nhận, và mặt hàng đã được gửi cho khách hàng.
- Nhận xét:
  - Lưu ý rằng không cần có mối quan hệ ngân hàng trước đó.
  - Không cần bên thứ ba để hỗ trợ; thay thế bằng mã/code và các khoản khích lệ.
  - Không có việc thu thập dữ liệu bởi bất kỳ ai ngoài giao dịch trực tiếp và chỉ cần trao đổi số lượng thông tin cần thiết giữa các bên tham gia (ví dụ, địa chỉ giao hàng).
  - Không cần tin tưởng giữa các bên (ngoại trừ Người bán gửi mặt hàng), giống như một giao dịch tiền mặt theo nhiều cách.
  - Tiền được sở hữu trực tiếp bởi các cá nhân.
  - Sổ cái Bitcoin được biểu diễn bằng đô la cho đơn giản, nhưng thực tế, nó là BTC.
  - Chúng tôi mô phỏng một giao dịch đơn lẻ được phát sóng, nhưng thực tế, nhiều giao dịch đang chờ xử lý trong mạng, và các khối bao gồm hàng ngàn giao dịch cùng một lúc. Các nút cũng kiểm tra không có giao dịch chi tiêu kép nào đang chờ xử lý (tôi sẽ loại bỏ tất cả ngoại trừ một nếu đó là trường hợp).
- Các tình huống gian lận:
  - Nếu khách hàng không có $25 BTC?
    - Họ sẽ không thể tạo giao dịch vì “mở khóa” và “sở hữu” là một và cùng một thứ, và máy tính kiểm tra giao dịch được ký đúng cách; nếu không, họ sẽ từ chối nó.
- Nếu máy tính được chọn ngẫu nhiên cố gắng "thay đổi sổ cái"? - Khối sẽ bị từ chối, vì mọi máy tính khác đều có lịch sử đầy đủ và sẽ nhận ra sự thay đổi, vi phạm một trong những quy tắc của họ.
  - Máy tính Ngẫu nhiên sẽ không nhận được phần thưởng, và không có giao dịch nào từ khối của họ được hoàn tất.

## Đánh giá kiến thức

<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>

### Thảo luận tại lớp KA

Thảo luận về một số sự đơn giản hóa được thực hiện trong bài tập tại lớp dưới kịch bản thứ hai và mô tả chi tiết hơn về hệ thống Bitcoin thực tế.

### Ôn tập từ vựng KA

Định nghĩa các thuật ngữ chính được giới thiệu trong phần trước:

- Node
- Mempool
- Difficulty Target
- Block

**Thảo luận về ý nghĩa của một số thuật ngữ bổ sung nhóm:**

Blockchain, Transaction, Double-Spend, Vấn đề Tướng Byzantine, Mining, Proof of Work (PoW), Hàm Hash, Block Reward, Blockchain, Chuỗi Dài nhất, Tấn công 51%, Output, Output Lock, Change, Satoshis, Public/Private Key, Address, Public-Key Cryptography, Digital Signature, Wallet

# Giới thiệu về BTCPay Server

<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>

## Hiểu về màn hình đăng nhập BTCPay Server

<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>

### Làm việc với BTCPay Server

Mục tiêu của khối học này sẽ là hiểu chung về phần mềm BTCPay Server. Trong môi trường chia sẻ, bạn được khuyến khích theo dõi minh họa của giáo viên và theo dõi cùng với Sổ tay Khóa học BTCPay Server để theo dõi giáo viên. Bạn sẽ học cách tạo ví qua nhiều phương pháp. Ví dụ bao gồm cài đặt ví Hot và ví phần cứng kết nối qua BTCPay Server Vault. Những mục tiêu này diễn ra trong môi trường Demo, được hiển thị và cung cấp quyền truy cập bởi giáo viên khóa học của bạn.

Nếu bạn theo dõi khóa học này một mình, bạn có thể tìm danh sách các máy chủ của bên thứ ba cho mục đích Demo tại https://directory.btcpayserver.org/filter/hosts. Chúng tôi khuyến cáo không sử dụng các tùy chọn của bên thứ ba này làm môi trường sản xuất, nhưng chúng phục vụ đúng mục đích cho việc giới thiệu về việc sử dụng Bitcoin và BTCPay Server.

Là một tân binh BTCPay Server, bạn có thể đã có kinh nghiệm thiết lập một node Bitcoin trước đây. Khóa học này sẽ nói cụ thể về ngăn xếp phần mềm BTCPay Server.

Nhiều tùy chọn trong BTCPay Server tồn tại dưới một hình thức này hay khác trong phần mềm liên quan đến ví Bitcoin khác.

### Màn hình đăng nhập BTCPay Server

Khi bạn được chào đón vào môi trường Demo, bạn được yêu cầu ‘Đăng nhập’ hoặc ‘Tạo tài khoản mới’. Quản trị viên máy chủ có thể tắt tính năng tạo tài khoản mới vì lý do an ninh. Logo và màu sắc của nút BTCPay Server có thể được thay đổi vì BTCPay Server là Phần mềm Mã nguồn Mở. Một máy chủ của bên thứ ba có thể White-label phần mềm và thay đổi toàn bộ giao diện.

![image](assets/en/0.webp)

### Cửa sổ Tạo Tài khoản

Tạo tài khoản trên BTCPay Server yêu cầu chuỗi địa chỉ Email hợp lệ; ví dụ example@email.com sẽ là một chuỗi hợp lệ cho Email.

Mật khẩu cần ít nhất 8 ký tự, bao gồm chữ cái, số và ký tự. Sau khi thiết lập mật khẩu một lần, bạn sẽ phải xác minh lại mật khẩu đã nhập để đảm bảo nó chính xác với những gì đã được nhập trong lần đầu tiên.
Khi cả hai trường Email và Mật khẩu đã được điền đúng cách, nhấp vào nút ‘Tạo Tài Khoản’. Điều này sẽ lưu Email và mật khẩu trên phiên bản máy chủ BTCPay của giáo viên.
![image](assets/en/1.webp)

**!Lưu Ý!**

Nếu bạn tự học khóa học này, việc tạo tài khoản này có thể bạn sẽ thực hiện trên một máy chủ của bên thứ ba; do đó, một lần nữa, chúng tôi nhấn mạnh không bao giờ sử dụng chúng như môi trường sản xuất mà chỉ dùng cho mục đích đào tạo.

### Quản Lý Tạo Tài Khoản bởi Quản Trị Viên BTCPay Server

Quản trị viên của Phiên bản BTCPay Server cũng có thể tạo tài khoản cho BTCPay Server. Quản trị viên của phiên bản BTCPay Server có thể nhấp vào ‘Cài Đặt Máy Chủ’ (1), nhấp vào tab ‘Người Dùng’ (2), và nhấp vào nút “+ Thêm Người Dùng” (3) ở góc trên bên phải của tab Người Dùng. Trong Mục tiêu (4.3), bạn sẽ tìm hiểu thêm về quyền kiểm soát tài khoản của quản trị viên.

![image](assets/en/2.webp)

Là một quản trị viên, bạn sẽ cần địa chỉ Email của người dùng và thiết lập một mật khẩu chuẩn. Là Quản trị viên, bạn nên thông báo cho người dùng rằng họ nên thay đổi mật khẩu này trước khi sử dụng tài khoản vì lý do an ninh. Nếu Quản trị viên KHÔNG thiết lập Mật khẩu và SMTP đã được thiết lập trên máy chủ, người dùng sẽ nhận được một email với liên kết mời để tạo tài khoản và thiết lập mật khẩu của họ.

### Ví Dụ

Khi theo dõi khóa học qua giáo viên, hãy theo dõi liên kết do giáo viên cung cấp và tạo tài khoản của bạn trên môi trường Demo được cung cấp. Đảm bảo địa chỉ email và mật khẩu của bạn được lưu một cách an toàn; bạn sẽ cần thông tin đăng nhập này cho phần còn lại của các mục tiêu demo trong khóa học này.

Giáo viên của bạn có thể đã thu thập địa chỉ email trước và gửi một liên kết mời trước bài tập này. Nếu được hướng dẫn, kiểm tra Email của bạn.

Khi tham gia khóa học mà không có giáo viên, hãy tạo tài khoản của bạn sử dụng môi trường demo của BTCPay Server; truy cập

https://mainnet.demo.btcpayserver.org/login.

Tài khoản này chỉ nên được sử dụng cho mục đích trình diễn/đào tạo và không bao giờ dùng cho kinh doanh.

### Tóm Tắt Kỹ Năng

Trong phần này, bạn đã học được những điều sau:

- Cách tạo một tài khoản trên máy chủ được lưu trữ thông qua giao diện.
- Cách một quản trị viên máy chủ có thể thêm người dùng thủ công trong cài đặt máy chủ.

### Đánh Giá Kiến Thức

#### Đánh Giá Khái Niệm

Nêu lý do tại sao sử dụng Máy Chủ Demo là ý tưởng xấu cho mục đích sản xuất.

## Quản Lý Tài Khoản Người Dùng

<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>

### Quản Lý Tài Khoản trên BTCPay Server

Sau khi chủ cửa hàng đã tạo tài khoản của họ, họ có thể quản lý nó ở góc dưới bên trái của giao diện người dùng BTCPay Server. Dưới nút Tài Khoản, có nhiều cài đặt cấp cao hơn.

- Chế độ Tối/Sáng.
- Chuyển đổi Ẩn Thông Tin Nhạy Cảm.
- Quản Lý Tài Khoản.

![image](assets/en/3.webp)

### Chế độ Tối và Sáng

Người dùng của BTCPay Server có thể chọn giữa phiên bản giao diện người dùng Chế độ Tối hoặc Sáng. Các trang đối diện với khách hàng sẽ không thay đổi. Họ sử dụng cài đặt ưa thích của khách hàng về chế độ tối hoặc sáng.

### Chuyển đổi Ẩn Thông Tin Nhạy Cảm

Nút ẩn thông tin nhạy cảm mang lại một lớp bảo mật nhanh chóng và đơn giản. Bất cứ khi nào bạn cần vận hành máy chủ BTCPay của mình, nhưng có thể có người lén nhìn qua vai bạn ở không gian công cộng, hãy bật Ẩn Thông Tin Nhạy Cảm, và tất cả các giá trị trong BTCPay Server sẽ được ẩn đi. Người ta có thể nhìn qua vai bạn nhưng không thể thấy các giá trị bạn đang xử lý.

### Quản Lý Tài Khoản

Một khi tài khoản người dùng đã được tạo, đây là nơi để quản lý mật khẩu, xác thực hai yếu tố (2fa), hoặc khóa API.

### Quản lý Tài khoản - Tài khoản

Bạn có thể cập nhật tài khoản của mình bằng địa chỉ Email khác nếu muốn. Để đảm bảo rằng địa chỉ email của bạn chính xác, BTCPay Server cho phép bạn gửi một email xác nhận. Nhấn lưu nếu người dùng thiết lập một địa chỉ email mới và xác nhận việc xác minh thành công. Tên đăng nhập vẫn giữ nguyên như địa chỉ Email trước đó.

Người dùng có thể quyết định xóa toàn bộ tài khoản của mình. Điều này có thể được thực hiện bằng cách nhấn vào nút xóa trên tab Tài khoản.

![image](assets/en/4.webp)

**!Lưu ý!**

Sau khi thay đổi Email, tên đăng nhập cho tài khoản sẽ không thay đổi. Địa chỉ Email được cung cấp trước đó sẽ vẫn là tên đăng nhập.

### Quản lý Tài khoản - Mật khẩu

Một sinh viên có thể muốn thay đổi mật khẩu của mình. Anh ta có thể làm điều này bằng cách đi tới tab Mật khẩu. Tại đây, anh ta cần phải nhập mật khẩu cũ và có thể thay đổi thành một mật khẩu mới.

![image](assets/en/5.webp)

### Xác thực Hai Yếu tố (2fa)

Để hạn chế hậu quả của việc mất cắp mật khẩu, bạn có thể sử dụng xác thực hai yếu tố (2fa), một phương pháp bảo mật tương đối mới. Bạn có thể kích hoạt xác thực hai yếu tố thông qua Quản lý tài khoản và tab cho xác thực hai yếu tố. Bạn phải hoàn thành một bước thứ hai sau khi đăng nhập bằng tên đăng nhập và mật khẩu của mình.

BTCPay Server cho phép hai cách kích hoạt 2FA, 2FA dựa trên ứng dụng (Authy, Google, Microsoft authenticators) hoặc thông qua Thiết bị bảo mật (FIDO2 hoặc LNURL Auth).

### Xác thực Hai Yếu tố - Dựa trên ứng dụng

Dựa vào Hệ điều hành điện thoại di động của bạn (Android hoặc iOS), người dùng có thể chọn giữa các ứng dụng sau;

1. Tải xuống một ứng dụng xác thực hai yếu tố;
   - Authy cho [Android](https://play.google.com/store/apps/details?id=com.authy.authy) hoặc [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator cho [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) hoặc [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator cho [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) hoặc [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)
2. Sau khi tải xuống và cài đặt Ứng dụng Xác thực.
   - Quét mã QR được cung cấp bởi BTCPay Server
   - Hoặc nhập khóa được tạo bởi BTCPay Server vào ứng dụng Xác thực của bạn một cách thủ công.
3. Ứng dụng Xác thực sẽ cung cấp cho bạn một mã duy nhất. Nhập mã duy nhất vào BTCPay Server để xác minh cài đặt, và nhấn xác minh để hoàn tất quá trình.

![image](assets/en/6.webp)

### Tóm tắt Kỹ năng

Trong phần này, bạn đã học được những điều sau:

- Các tùy chọn quản lý tài khoản và các cách khác nhau để quản lý một tài khoản trên một thể hiện của BTCPay Server.
- Cách thiết lập 2FA dựa trên ứng dụng.

### Đánh giá Kiến thức

#### Đánh giá Khái niệm

Mô tả cách xác thực hai yếu tố dựa trên ứng dụng giúp bảo vệ tài khoản của bạn

## Tạo một cửa hàng mới

<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>
Khi một người dùng mới đăng nhập vào BTCPay Server, môi trường là trống trải và cần có một cửa hàng đầu tiên. Trình hướng dẫn giới thiệu của BTCPay Server sẽ cung cấp cho người dùng tùy chọn ‘Tạo cửa hàng của bạn’ (1). Một Cửa hàng có thể được coi là một Ngôi nhà cho nhu cầu Bitcoin của bạn. Một Node BTCPay Server mới sẽ bắt đầu với việc Đồng bộ hóa Blockchain Bitcoin (2). Tùy thuộc vào cơ sở hạ tầng bạn chạy BTCPay Server trên, điều này có thể mất từ vài giờ đến vài ngày. Phiên bản hiện tại của thể hiện được hiển thị ở góc dưới bên phải của giao diện người dùng BTCPay Server của bạn. Điều này hữu ích cho việc tham khảo khi khắc phục sự cố.
![hình ảnh](assets/en/7.webp)

### Trình hướng dẫn Tạo cửa hàng của bạn

Theo khóa học này sẽ bắt đầu với một màn hình hơi khác so với trang trước. Vì giáo viên của bạn đã chuẩn bị môi trường Demo, Blockchain Bitcoin đã được đồng bộ hóa trước, và do đó bạn sẽ không thấy trạng thái đồng bộ của các node.

Người dùng có thể quyết định xóa toàn bộ tài khoản của họ. Điều này có thể được thực hiện bằng cách nhấp vào nút xóa trên tab Tài khoản.

![hình ảnh](assets/en/8.webp)

**!Lưu ý!**

Tài khoản BTCPay Server có thể tạo số lượng không giới hạn các cửa hàng. Mỗi cửa hàng là một ví hoặc “ngôi nhà”.

### Ví dụ

Bắt đầu bằng cách nhấp vào "Tạo cửa hàng của bạn".

![hình ảnh](assets/en/9.webp)

Điều này sẽ tạo Ngôi nhà và bảng điều khiển đầu tiên của bạn để sử dụng BTCPay server.

(1) Sau khi nhấp vào "Tạo cửa hàng của bạn", BTCPay Server sẽ yêu cầu bạn đặt tên cho cửa hàng; điều này có thể là bất cứ thứ gì hữu ích cho bạn.

![hình ảnh](assets/en/10.webp)

(2) Tiếp theo, cần phải thiết lập một đơn vị tiền tệ mặc định cho cửa hàng, có thể là tiền tệ fiat hoặc được định giá theo tiêu chuẩn Bitcoin / Sats. Đối với môi trường demo, chúng tôi sẽ thiết lập nó thành USD.

![hình ảnh](assets/en/11.webp)

(3) Là tham số cuối cùng trong việc thiết lập cửa hàng, BTCPay Server yêu cầu bạn thiết lập một "Nguồn giá ưa thích" để so sánh giá Bitcoin với giá fiat hiện tại để cửa hàng của bạn hiển thị tỷ giá hối đoái chính xác giữa Bitcoin và tiền tệ fiat được thiết lập cho cửa hàng. Chúng tôi sẽ tuân theo mặc định trong ví dụ Demo và thiết lập điều này thành sàn giao dịch Kraken. BTCPay Server sử dụng API của Kraken để kiểm tra tỷ giá hối đoái.

![hình ảnh](assets/en/12.webp)

(4) Bây giờ, sau khi các tham số cửa hàng đã được thiết lập, nhấp vào nút Tạo, và BTCPay Server sẽ tạo bảng điều khiển cửa hàng đầu tiên của bạn, nơi trình hướng dẫn sẽ tiếp tục.

![hình ảnh](assets/en/13.webp)

Xin chúc mừng, bạn đã tạo cửa hàng đầu tiên của mình, và điều này kết thúc bài tập này.

![hình ảnh](assets/en/14.webp)

### Tóm tắt Kỹ năng

Trong phần này, bạn đã học:

- Tạo cửa hàng và cấu hình đơn vị tiền tệ mặc định kết hợp với sở thích nguồn giá.
- Mỗi "Cửa hàng" là một ngôi nhà mới tách biệt khỏi các cửa hàng khác trên cài đặt này của BTCPay Server.

# Giới thiệu về Bảo mật Khóa Bitcoin

<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>

## Hiểu biết về Sinh khóa Bitcoin

<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>

### Việc sinh khóa bitcoin bao gồm những gì?

Khi tạo ví Bitcoin, ví sẽ tạo ra một cái gọi là "hạt giống". Trong mục tiêu cuối cùng, bạn đã tạo ra một "hạt giống", Chuỗi các từ được tạo ra trước đó còn được biết đến như là cụm từ ghi nhớ. Hạt giống được sử dụng để sinh ra các Khóa Bitcoin riêng lẻ từ đó và được sử dụng để gửi hoặc nhận Bitcoin. Cụm từ hạt giống không bao giờ nên được chia sẻ với bên thứ ba hoặc các đối tác không đáng tin cậy.
Việc tạo seed được thực hiện theo tiêu chuẩn công nghiệp được biết đến với tên gọi là khung "Hierarchical Deterministic" (HD).
![image](assets/en/15.webp)

### Địa Chỉ

BTCPay Server được xây dựng để tạo ra một Địa Chỉ mới. Điều này giảm bớt vấn đề tái sử dụng công khai khóa hoặc Địa Chỉ. Sử dụng cùng một Khóa công khai làm cho việc theo dõi toàn bộ lịch sử thanh toán của bạn trở nên rất dễ dàng. Nghĩ về khóa như là phiếu sử dụng một lần sẽ cải thiện đáng kể quyền riêng tư của bạn. Chúng tôi cũng sử dụng Địa Chỉ Bitcoin, không nhầm lẫn chúng với Khóa công khai.

Một Địa Chỉ được tạo ra từ Khóa công khai thông qua một “thuật toán băm.” Tuy nhiên, hầu hết ví và giao dịch sẽ hiển thị Địa Chỉ thay vì những khóa công khai đó. Địa Chỉ, nói chung, ngắn hơn khóa công khai và thường bắt đầu bằng `1`, `3`, hoặc `bc1`, trong khi khóa công khai bắt đầu bằng `02`, `03`, hoặc `04`.

- Địa Chỉ bắt đầu bằng `1.....` vẫn là các địa chỉ rất phổ biến. Như đã đề cập trong chương Tạo một cửa hàng mới, đây là các địa chỉ cũ. Loại địa chỉ này dành cho giao dịch P2PKH. P2Pkh sử dụng mã hóa Base58, làm cho địa chỉ nhạy cảm với chữ hoa và chữ thường. Cấu trúc của nó dựa trên khóa công khai với một số định danh thêm vào.

- Địa Chỉ bắt đầu bằng `bc1...` đang dần trở thành các địa chỉ rất phổ biến. Đây được biết đến là Địa Chỉ SegWit (native). Chúng cung cấp một cấu trúc phí tốt hơn so với các Địa Chỉ khác đã đề cập. Địa Chỉ SegWit (native) sử dụng mã hóa Bech32 và chỉ cho phép sử dụng chữ thường.

- Địa Chỉ bắt đầu bằng `3...` thường được sử dụng bởi các sàn giao dịch cho địa chỉ nạp tiền. Địa chỉ này được đề cập trong chương Tạo một cửa hàng mới, là địa chỉ SegWit bọc hoặc lồng. Tuy nhiên, chúng cũng có thể hoạt động như một "Địa Chỉ Multisig". Khi được sử dụng như một địa chỉ SegWit, lại có một số tiết kiệm về phí giao dịch, ít hơn so với SegWit (native). Địa Chỉ P2SH sử dụng mã hóa Base58. Điều này làm cho nó nhạy cảm với chữ hoa và chữ thường, giống như địa chỉ cũ.

- Địa Chỉ bắt đầu bằng `2...` là địa chỉ Testnet. Chúng được dùng để nhận bitcoin testnet (tBTC). Bạn không bao giờ nên nhầm lẫn và gửi Bitcoin đến những địa chỉ này. Cho mục đích phát triển, bạn có thể tạo một ví testnet. Có nhiều nguồn cung cấp bitcoin testnet trực tuyến. Không bao giờ mua Bitcoin testnet. Bitcoin testnet được khai thác. Điều này có thể là lý do cho một nhà phát triển sử dụng Regtest thay thế. Đây là một môi trường thử nghiệm cho các nhà phát triển, thiếu một số thành phần mạng. Tuy nhiên, Bitcoin, cho mục đích phát triển, rất hữu ích.

### Khóa Công Khai

Khóa công khai ngày nay ít được sử dụng trong thực tế. Theo thời gian, người dùng bitcoin đã thay thế chúng bằng Địa Chỉ. Chúng vẫn tồn tại và đôi khi vẫn được sử dụng. Khóa công khai, nói chung, là chuỗi ký tự dài hơn nhiều so với địa chỉ. Giống như với địa chỉ, chúng bắt đầu với một định danh cụ thể.

- Đầu tiên, `02...` và `03...` là các định danh khóa công khai rất tiêu chuẩn được mã hóa trong định dạng SEC. Chúng có thể được xử lý và chuyển đổi thành địa chỉ để nhận, được sử dụng để tạo địa chỉ multi-sig, hoặc để xác minh chữ ký. Các giao dịch Bitcoin ngày đầu sử dụng khóa công khai là một phần của giao dịch P2PK.

- Tuy nhiên, ví HD sử dụng một cấu trúc khác. `xpub...`, `ypub...` hoặc `zpub...` được gọi là khóa công khai mở rộng hay còn gọi là xpubs. Những khóa này được sử dụng để tạo ra nhiều khóa công khai vì chúng là một phần của ví HD. Vì xpub của bạn giữ các bản ghi của toàn bộ lịch sử của bạn, nghĩa là các giao dịch trong quá khứ và tương lai, không bao giờ chia sẻ chúng với các bên không đáng tin cậy.

### Tóm Tắt Kỹ Năng

Trong phần này, bạn đã học được những điều sau:

- Sự khác biệt giữa địa chỉ và kiểu dữ liệu khóa công khai và lợi ích của việc sử dụng địa chỉ so với khóa công khai.

### Đánh giá kiến thức

Mô tả lợi ích của việc sử dụng địa chỉ mới cho mỗi giao dịch so với việc tái sử dụng địa chỉ hoặc phương pháp khóa công khai

## Bảo mật khóa với ví cứng

<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>

### Lưu trữ Khóa Bitcoin

Sau khi tạo ra cụm từ hạt giống, danh sách từ 12 - 24 từ được tạo ra trong cuốn sách này đòi hỏi phải được sao lưu và bảo mật đúng cách, vì những từ này là cách duy nhất để khôi phục quyền truy cập vào ví. Cấu trúc của ví HD và cách nó tạo ra địa chỉ một cách định trước sử dụng hạt giống đó, tất cả địa chỉ bạn tạo ra sẽ được sao lưu sử dụng danh sách từ gợi nhớ này đại diện cho cụm từ hạt giống hoặc cụm từ khôi phục của bạn.

Hãy giữ cụm từ khôi phục của bạn được bảo mật. Nếu ai đó, đặc biệt là với ý đồ xấu, truy cập được, họ có thể chuyển tiền của bạn. Việc giữ hạt giống an toàn và được bảo mật nhưng cũng nhớ nó là lẫn nhau. Có một số phương pháp để lưu trữ khóa riêng Bitcoin, mỗi phương pháp có lợi ích và nhược điểm, dù là về an ninh, riêng tư, tiện lợi, hay phương tiện vật lý. Do tầm quan trọng của khóa riêng, người dùng bitcoin thường lưu trữ và giữ an toàn những khóa này trong "tự quản" thay vì sử dụng dịch vụ "giữ hộ" như ngân hàng. Tùy thuộc vào người dùng, anh ta phải sử dụng giải pháp lưu trữ Lạnh hoặc ví Nóng.

### Lưu trữ khóa bitcoin Nóng và Lạnh

Thông thường, ví bitcoin được phân loại trong Ví Nóng hoặc Ví Lạnh. Hầu hết sự đánh đổi nằm ở sự tiện lợi, dễ sử dụng và rủi ro an ninh. Mỗi phương pháp này cũng có thể được thấy trong giải pháp giữ hộ. Tuy nhiên, sự đánh đổi ở đây chủ yếu dựa trên an ninh và riêng tư và vượt ra ngoài phạm vi của khóa học này.

### Ví Nóng

Ví Nóng là cách tiện lợi nhất để tương tác với Bitcoin qua điện thoại di động, web, hoặc phần mềm máy tính. Ví luôn kết nối với internet, cho phép người dùng gửi hoặc nhận Bitcoin. Tuy nhiên, đây cũng là điểm yếu của nó, ví, vì luôn trực tuyến, nay dễ bị tấn công bởi hacker hoặc malware trên thiết bị của bạn. Trong BTCPay Server, ví nóng lưu trữ khóa riêng trên instance. Bất kỳ ai truy cập vào cửa hàng BTCPay Server của bạn có thể ăn cắp tiền từ địa chỉ này nếu có ý đồ xấu. Khi BTCPay Server chạy trong môi trường được lưu trữ, bạn luôn nên xem xét điều này trong hồ sơ an ninh của mình và ưu tiên không sử dụng Ví Nóng trong trường hợp như vậy. Khi BTCPay Server được cài đặt trên phần cứng sở hữu, được bảo mật và tin cậy bởi bạn, hồ sơ rủi ro giảm đáng kể, nhưng nó không bao giờ biến mất!

### Ví Lạnh

Cá nhân chuyển Bitcoin của họ vào ví lạnh vì nó có thể cô lập khóa riêng khỏi internet. Loại bỏ kết nối internet khỏi phương trình giảm thiểu rủi ro của malware, spyware, và đổi SIM. Lưu trữ lạnh được tin là vượt trội hơn lưu trữ nóng về mặt an ninh và tự chủ, miễn là các biện pháp phòng ngừa thích hợp được thực hiện để tránh mất khóa riêng Bitcoin. Lưu trữ lạnh phù hợp nhất cho số lượng lớn Bitcoin, không dự định chi tiêu thường xuyên do sự phức tạp của cài đặt ví.

Có nhiều phương pháp để lưu trữ khóa Bitcoin trong lưu trữ lạnh, từ ví giấy đến ví não, ví cứng, hoặc, từ đầu, một tệp ví. Hầu hết ví sử dụng BIP 39 để tạo cụm từ hạt giống. Tuy nhiên, trong phần mềm Bitcoin core, vẫn chưa đạt được sự đồng thuận về việc sử dụng nó. Phần mềm Bitcoin Core vẫn sẽ tạo ra một tệp Wallet.dat bạn cần lưu trữ ở một vị trí ngoại tuyến an toàn.

### Tóm tắt Kỹ năng

Trong phần này, bạn đã học:

- Sự khác biệt giữa ví nóng và ví lạnh về chức năng và các sự đánh đổi của chúng.

### Đánh giá kiến thức Đánh giá Khái niệm

- Ví tiền là gì?
- Sự khác biệt giữa ví nóng và ví lạnh là gì?

- Mô tả ý nghĩa của "tạo ví"?

## Sử dụng khóa Bitcoin của bạn

<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>

### Ví BTCPay Server

BTCPay Server bao gồm các tính năng ví tiêu chuẩn sau:

- Giao dịch
- Gửi
- Nhận
- Quét lại
- Thanh toán kéo
- Thanh toán
- PSBT
- Cài đặt chung

### Giao dịch

Quản trị viên có thể xem các giao dịch đến và đi cho ví on-chain được kết nối với cửa hàng cụ thể này trong giao diện giao dịch. Mỗi giao dịch sẽ được phân biệt giữa nhận và gửi. Giao dịch nhận sẽ có màu xanh và giao dịch đi sẽ có màu đỏ. Trong giao diện giao dịch của BTCPay Server, quản trị viên cũng sẽ thấy một bộ nhãn tiêu chuẩn.

| Loại Giao Dịch  | Mô Tả                                                  |
| --------------- | ------------------------------------------------------ |
| App             | Thanh toán được nhận qua hóa đơn tạo bởi ứng dụng      |
| invoice         | Thanh toán được nhận qua hóa đơn                       |
| payjoin         | Chưa thanh toán, bộ đếm thời gian hóa đơn vẫn chưa hết |
| payjoin-exposed | UTXO được tiết lộ qua đề xuất payjoin của hóa đơn      |
| payment-request | Thanh toán được nhận qua yêu cầu thanh toán            |
| payout          | Thanh toán được gửi qua thanh toán hoặc hoàn tiền      |

### Cách Gửi

Chức năng gửi của máy chủ BTCPay gửi giao dịch từ ví on-chain của máy chủ BTCPay. BTCPay Server cho phép nhiều cách ký giao dịch để chi tiêu quỹ. Một giao dịch có thể được ký với;

- Ví Cứng
- Ví hỗ trợ PSBT
- Khóa riêng HD hoặc hạt giống khôi phục.
- Ví Nóng

#### Ví cứng

BTCPay Server có hỗ trợ ví cứng tích hợp cho phép bạn sử dụng ví cứng của mình với BTCPay Vault mà không tiết lộ thông tin cho ứng dụng hoặc máy chủ bên thứ ba. Tích hợp ví cứng trong BTCPay Server cho phép bạn nhập ví cứng của mình và chi tiêu quỹ đến với một xác nhận đơn giản trên thiết bị của bạn. Khóa riêng của bạn không bao giờ rời khỏi thiết bị, và tất cả quỹ đều được xác thực so với node đầy đủ của bạn, vì vậy không có rò rỉ dữ liệu.

#### Ký với ví hỗ trợ PSBT

PSBT (Partially Signed Bitcoin Transactions - Giao dịch Bitcoin được ký một phần) là một định dạng trao đổi cho các giao dịch Bitcoin cần được ký đầy đủ. PSBT được hỗ trợ trong BTCPay Server và có thể được ký với ví cứng và phần mềm tương thích.

Quy trình xây dựng một giao dịch Bitcoin được ký đầy đủ diễn ra qua các bước sau:

- Một PSBT được xây dựng với các đầu vào và đầu ra cụ thể nhưng không có chữ ký
- PSBT được xuất có thể được nhập bởi ví hỗ trợ định dạng này
- Dữ liệu giao dịch có thể được kiểm tra và ký bằng ví
- Tệp PSBT đã ký được xuất từ ví và nhập với BTCPay Server
- BTCPay Server tạo ra giao dịch Bitcoin cuối cùng
- Bạn xác minh kết quả và phát sóng nó lên mạng

#### Ký với Khóa Riêng HD hoặc hạt giống mnemonic

Nếu bạn đã tạo một ví trước đó sử dụng BTCPay Server, bạn có thể chi tiêu quỹ bằng cách nhập khóa riêng của mình vào một trường thích hợp. Đặt một "AccountKeyPath" phù hợp trong cài đặt ví; nếu không, bạn không thể chi tiêu.

#### Ký với ví nóng

Nếu bạn đã tạo một ví mới khi thiết lập cửa hàng của mình và kích hoạt nó như một ví nóng, nó sẽ tự động sử dụng hạt giống được lưu trữ trên máy chủ để ký.
Replace-By-Fee (RBF) là một tính năng của giao thức Bitcoin cho phép bạn thay thế một giao dịch đã được phát sóng trước đó (trong khi vẫn chưa được xác nhận). Điều này cho phép ngẫu nhiên hóa dấu vân tay giao dịch của ví hoặc thay thế nó bằng một mức phí cao hơn để di chuyển giao dịch lên cao hơn trong hàng đợi ưu tiên xác nhận (đào). Điều này sẽ hiệu quả thay thế giao dịch gốc vì mức phí cao hơn sẽ được ưu tiên, và một khi được xác nhận, sẽ làm vô hiệu giao dịch gốc (không double spend).
Nhấn vào nút "Cài Đặt Nâng Cao" để xem các tùy chọn RBF;

![image](assets/en/16.webp)

- Ngẫu nhiên hóa để tăng tính riêng tư, cho phép giao dịch được thay thế tự động để ngẫu nhiên hóa dấu vân tay giao dịch.
- Có, Đánh dấu giao dịch cho RBF và được thay thế một cách rõ ràng (Không được thay thế theo mặc định, chỉ qua nhập liệu)
- Không, Không cho phép giao dịch được thay thế.

### Lựa Chọn Coin

Lựa chọn coin là một tính năng nâng cao tăng cường quyền riêng tư cho phép bạn chọn các coin bạn muốn chi tiêu khi tạo một giao dịch. Ví dụ, thanh toán bằng các coin mới từ một lần trộn conjoin.

Lựa chọn coin hoạt động tự nhiên với tính năng nhãn ví. Điều này cho phép bạn gắn nhãn cho các khoản tiền đến để quản lý UTXO và chi tiêu một cách mượt mà hơn.

BTCpay Server cũng hỗ trợ BIP-329 cho quản lý nhãn. BIP-329 cho phép gắn nhãn lên; nếu bạn chuyển từ một ví hỗ trợ BIP cụ thể này và thiết lập nhãn, BTCPay Server sẽ nhận biết và nhập chúng. Khi chuyển đổi máy chủ, thông tin này cũng có thể được xuất và nhập vào môi trường mới.

### Cách Nhận

Khi nhấn vào nút nhận trong BTCPay Server, nó tạo ra một địa chỉ chưa sử dụng có thể được sử dụng để nhận thanh toán. Quản trị viên cũng có thể tạo ra một địa chỉ mới bằng cách tạo một “Hóa Đơn” mới.

BTCPay Server luôn yêu cầu tạo địa chỉ tiếp theo có sẵn để tránh tái sử dụng địa chỉ. Sau khi nhấn “Tạo địa chỉ BTC tiếp theo có sẵn”, BTCPay Server đã tạo ra một địa chỉ mới và QR. Nó cũng cho phép bạn trực tiếp thiết lập một Nhãn cho địa chỉ để quản lý địa chỉ của bạn tốt hơn.

![image](assets/en/17.webp)

![image](assets/en/18.webp)

#### Quét Lại

Tính năng Quét Lại dựa vào “Scantxoutset” của Bitcoin Core 0.17.0 để quét trạng thái hiện tại của blockchain (gọi là UTXO Set) để tìm các coin thuộc về lược đồ phát sinh được cấu hình. Quét lại ví giải quyết hai vấn đề mà người dùng BTCPay Server gặp phải.

1. Vấn đề giới hạn khoảng trống - Hầu hết các ví bên thứ ba là ví nhẹ chia sẻ một nút giữa nhiều người dùng. Ví nhẹ và ví dựa vào nút đầy đủ giới hạn số lượng (thường là 20) địa chỉ không có số dư mà chúng theo dõi trên blockchain để ngăn chặn vấn đề hiệu suất. BTCPay Server tạo ra một địa chỉ mới cho mỗi hóa đơn. Với điều này trong tâm trí, sau khi BTCPay Server tạo ra 20 hóa đơn chưa thanh toán liên tiếp, ví bên ngoài ngừng tìm kiếm các giao dịch, giả định rằng không có giao dịch mới nào xảy ra. Ví bên ngoài của bạn sẽ không hiển thị chúng một khi các hóa đơn được thanh toán trên lần thứ 21, 22, v.v. Ngược lại, ví của BTCPay Server theo dõi bất kỳ địa chỉ nào nó tạo ra cùng với một giới hạn khoảng trống lớn hơn nhiều. Nó không phụ thuộc vào bên thứ ba và luôn có thể hiển thị số dư chính xác.
2. Giải pháp giới hạn khoảng trống - Nếu [ví ngoại truy cập/ví hiện tại](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-wallet) của bạn cho phép cấu hình giới hạn khoảng trống, cách đơn giản là tăng nó lên. Tuy nhiên, đa số ví không cho phép làm điều này. Chỉ có một số ít ví cho phép cấu hình giới hạn khoảng trống mà chúng tôi biết đến là Electrum, Wasabi và Sparrow Wallet. Thật không may, bạn có thể gặp vấn đề với nhiều ví khác. Để có trải nghiệm người dùng tốt nhất và bảo mật, hãy cân nhắc từ bỏ ví ngoại truy cập và sử dụng ví nội bộ của BTCPay Server.

#### BTCPay Server sử dụng “mempoolfullrbf=1”

BTCPay Server sử dụng “mempoolfullrbf=1”; chúng tôi đã thêm mặc định này vào cài đặt BTCPay Server của bạn. Tuy nhiên, chúng tôi cũng đã tạo ra một phân đoạn mà bạn có thể tự tắt. Không có “mempoolfullrbf=1”, nếu một khách hàng thực hiện giao dịch gấp đôi mà không báo hiệu RBF, Người bán chỉ biết sau khi xác nhận.

Quản trị viên có thể muốn không sử dụng cài đặt này. Bằng chuỗi sau, bạn có thể thay đổi cài đặt mặc định.

```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCLUDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i**
```

### Cài đặt ví BTCPay Server

Cài đặt ví trong BTCPay Server cung cấp cái nhìn tổng quan rõ ràng và nhanh chóng về cài đặt chung của ví bạn. Tất cả các cài đặt này được điền trước nếu ví được tạo với BTCPay Server.

![image](assets/en/19.webp)

Cài đặt ví trong BTCPay Server cung cấp cái nhìn tổng quan rõ ràng và nhanh chóng về cài đặt chung của ví bạn. Cài đặt ví của BTCPay Server bắt đầu với trạng thái ví. Là ví Chỉ xem hay Ví nóng? Tùy thuộc vào loại ví, các hành động có thể khác nhau từ quét lại ví để tìm kiếm giao dịch bị thiếu, cắt bớt giao dịch cũ khỏi lịch sử, đăng ký ví cho liên kết thanh toán, hoặc thay thế và xóa ví hiện tại được gắn với cửa hàng. Trong cài đặt ví của BTCPay Server, quản trị viên có thể đặt Nhãn cho ví để quản lý ví tốt hơn. Tại đây, Quản trị viên cũng có thể thấy Sơ đồ Phát sinh, khóa tài khoản (xpub), Dấu vân tay, và Đường dẫn khóa. Cài đặt thanh toán trong cài đặt ví chỉ có 2 cài đặt chính. Thanh toán không hợp lệ nếu giao dịch không xác nhận trong (số phút đã đặt) sau khi hóa đơn hết hạn. Xem xét hóa đơn được xác nhận khi giao dịch thanh toán có X số lần xác nhận. Quản trị viên cũng có thể đặt một công tắc để hiển thị phí được đề xuất tại thanh toán hoặc đặt mục tiêu xác nhận thủ công theo số khối.

![image](assets/en/20.webp)

**!Lưu ý!**

Nếu bạn theo dõi khóa học này một mình, việc tạo tài khoản này có thể là điều bạn sẽ làm trên một máy chủ bên thứ ba, do đó, một lần nữa chúng tôi nhắc bạn không sử dụng những môi trường này cho mục đích sản xuất, mà chỉ dùng cho mục đích đào tạo.

### Ví dụ

#### Thiết lập ví Bitcoin trong BTCPay Server

BTCPay Server cho phép hai cách thiết lập ví. Một cách là nhập một ví Bitcoin đã tồn tại. Việc nhập có thể được thực hiện bằng cách kết nối ví cứng, nhập tệp ví, nhập khóa công cộng mở rộng, quét mã QR của ví, hoặc ít được ưa chuộng nhất, nhập bằng tay hạt giống khôi phục ví đã tạo trước đó. Trong BTCPay Server, cũng có thể tạo ví mới. Có hai cách có thể cấu hình BTCPay Server khi tạo ví mới.
Tùy chọn ví nóng trong BTCPay Server cho phép sử dụng các tính năng như 'Payjoin' hoặc 'Liquid'. Tuy nhiên, có một nhược điểm, seed khôi phục được tạo cho ví này sẽ được lưu trữ trên máy chủ, nơi bất kỳ ai có quyền kiểm soát Admin cũng có thể truy cập seed khôi phục. Vì khóa riêng của bạn được tạo từ seed khôi phục, một người có ý định xấu có thể truy cập vào số tiền hiện tại và tương lai của bạn!

Để giảm thiểu rủi ro này trong BTCPay Server, một Admin có thể thiết lập trong Cài đặt Máy chủ > Chính sách > "Cho phép người không phải là admin tạo ví nóng cho cửa hàng của họ" thành không, như mặc định. Để tăng cường bảo mật cho những ví nóng này, quản trị viên máy chủ nên kích hoạt xác thực 2FA cho các tài khoản được phép có ví nóng. Lưu trữ khóa riêng trên máy chủ công cộng là nguy hiểm và đi kèm với rủi ro. Một số rủi ro tương tự như rủi ro của Mạng Lưới Lightning (xem chương tiếp theo về rủi ro của Mạng Lưới Lightning).

Tùy chọn thứ hai mà BTCPay Server cung cấp trong việc tạo ví mới là tạo một ví Chỉ Xem. BTCPay Server sẽ tạo khóa riêng của bạn một lần. Sau khi người dùng xác nhận đã ghi lại Cụm từ Seed của họ, BTCPay Server sẽ xóa khóa riêng khỏi máy chủ. Kết quả là, cửa hàng của bạn giờ đây có một ví Chỉ Xem được kết nối với nó. Để chi tiêu số tiền nhận được trên ví Chỉ Xem của bạn, xem chương Cách Gửi, bằng cách sử dụng BTCPay Server Vault, PSBT (giao dịch bitcoin được ký một phần), hoặc ít được khuyến khích nhất, cung cấp thủ công cụm từ Seed của bạn.

Bạn đã tạo một 'Cửa hàng' mới trong phần cuối cùng. Trình hướng dẫn cài đặt sẽ tiếp tục bằng cách yêu cầu thiết lập ví hoặc thiết lập một nút Lightning. Trong ví dụ này, bạn sẽ theo quy trình hướng dẫn thiết lập ví (1).

![image](assets/en/21.webp)

Sau khi nhấp vào "Thiết lập ví", trình hướng dẫn sẽ tiếp tục bằng cách yêu cầu bạn muốn tiếp tục như thế nào; BTCPay Server hiện tại cung cấp tùy chọn kết nối ví Bitcoin hiện có với cửa hàng mới của bạn. Nếu bạn không có ví, BTCPay Server đề xuất tạo một ví mới. Ví dụ này sẽ theo các bước để “tạo một ví mới” (2). Theo dõi các bước để tìm hiểu cách "Kết nối ví hiện có (1).

![image](assets/en/22.webp)

**!Lưu ý!**

Nếu bạn tham gia khóa học này trong một lớp học, ví dụ hiện tại và seed chúng tôi tạo ra chỉ cho mục đích giáo dục. Không bao giờ nên có số tiền lớn nào khác ngoài số tiền yêu cầu qua các bài tập trên các địa chỉ này.

(1) Tiếp tục quy trình hướng dẫn "Ví mới" bằng cách nhấp vào nút "Tạo ví mới".

![image](assets/en/23.webp)

(2) Sau khi nhấp vào “Tạo ví mới”, cửa sổ tiếp theo trong quy trình hướng dẫn sẽ đưa ra các tùy chọn “Ví nóng” và “Ví chỉ xem”. Nếu bạn theo dõi cùng một giảng viên, môi trường của bạn là một Demo chung, và bạn chỉ có thể tạo một ví Chỉ Xem. Chú ý sự khác biệt giữa hai hình dưới đây. Khi bạn đang trong môi trường Demo và theo dõi cùng giảng viên, hãy tạo một "Ví chỉ xem" và tiếp tục với quy trình hướng dẫn "Ví mới".

![image](assets/en/24.webp)

![image](assets/en/25.webp)

(3) Tiếp tục quy trình hướng dẫn ví mới, bạn bây giờ đang ở phần Tạo ví BTC chỉ xem. Tại đây chúng ta có thể thiết lập "Loại địa chỉ" ví mà BTCPay Server cho phép bạn chọn loại địa chỉ ưa thích của mình; tính đến thời điểm viết khóa học này, vẫn được khuyến khích sử dụng địa chỉ bech32. Tìm hiểu chi tiết hơn về các loại địa chỉ trong chương đầu tiên của phần này.

- Segwit (bech32)
- Native SegWit là địa chỉ bắt đầu bằng `bc1q`.
  - Ví dụ: `bc1qXXXXXXXXXXXXXXXXXXXXXX`
- Legacy
  - Địa chỉ Legacy là địa chỉ bắt đầu bằng số `1`.
  - Ví dụ: `15e15hXXXXXXXXXXXXXXXXXXXX`
- Taproot (Dành cho người dùng nâng cao)
  - Địa chỉ Taproot bắt đầu bằng `bc1p`.
  - Ví dụ: `bc1pXXXXXXXXXXXXXXXXXXXXXXXX`
- Segwit wrapped
  - Địa chỉ Segwit wrapped bắt đầu bằng `3`.
  - Ví dụ: `37BBXXXXXXXXXXXXXXX`

Chọn segwit (được khuyến nghị) là loại địa chỉ ví ưa thích của bạn.

![image](assets/en/26.webp)

(4) Khi thiết lập tham số cho Ví, BTCPay Server cho phép người dùng thiết lập một cụm từ mật khẩu tùy chọn thông qua BIP39, hãy chắc chắn xác nhận mật khẩu của bạn.

![image](assets/en/27.webp)

(5) Sau khi thiết lập loại Địa chỉ Ví và có thể thiết lập một số tùy chọn nâng cao, nhấp vào Tạo, và BTCPay Server sẽ tạo Ví mới của bạn. Lưu ý rằng đây là bước cuối cùng trước khi tạo cụm từ Seed của bạn. Hãy chắc chắn chỉ thực hiện điều này trong một môi trường mà người khác không thể đánh cắp cụm từ Seed bằng cách nhìn vào màn hình của bạn.

![image](assets/en/28.webp)

(6) Trong màn hình tiếp theo của trình hướng dẫn, BTCPay Server hiển thị cho bạn cụm từ Seed phục hồi cho Ví mới tạo của bạn; đây là chìa khóa để khôi phục Ví và ký giao dịch. BTCPay Server tạo ra một cụm từ Seed gồm 12 từ. Những từ này sẽ được xóa khỏi máy chủ sau màn hình thiết lập này. Ví này cụ thể là một Ví chỉ xem. Khuyến nghị không lưu trữ cụm từ Seed này dưới dạng số hoặc hình ảnh. Người dùng chỉ có thể tiếp tục trong trình hướng dẫn nếu họ xác nhận rằng họ đã ghi chép cụm từ Seed của mình.

![image](assets/en/29.webp)

(7) Sau khi nhấp vào Hoàn tất và bảo vệ cụm từ Seed Bitcoin mới tạo, BTCPay Server sẽ cập nhật cửa hàng của bạn với Ví mới đính kèm và sẵn sàng nhận thanh toán. Trong Giao diện Người dùng, trong menu điều hướng bên trái, chú ý cách Bitcoin hiện được làm nổi bật và kích hoạt dưới mục Ví.

![image](assets/en/30.webp)

### Ví dụ: Ghi chép cụm từ Seed

Đây là một khoảnh khắc rất đặc biệt và an toàn để sử dụng Bitcoin. Như đã đề cập trước đó, chỉ bạn mới nên có quyền truy cập hoặc biết về cụm từ Seed của mình. Khi bạn theo dõi cùng một giáo viên và lớp học, cụm từ Seed được tạo ra chỉ nên được sử dụng trong khóa học này. Quá nhiều yếu tố, ánh mắt tò mò từ bạn cùng lớp, hệ thống không an toàn, và nhiều yếu tố khác làm cho những chìa khóa này chỉ mang tính giáo dục và không đáng tin cậy. Tuy nhiên, các chìa khóa được tạo ra vẫn nên được lưu trữ cho các ví dụ trong khóa học.

Phương pháp đầu tiên chúng ta sẽ sử dụng trong tình huống hiện tại, cũng là phương pháp ít an toàn nhất, là ghi chép cụm từ Seed theo đúng thứ tự. Một thẻ cụm từ Seed có trong tài liệu khóa học được cung cấp cho sinh viên hoặc tìm thấy trên GitHub của BTCPay Server. Chúng ta sẽ sử dụng thẻ này để ghi chép các từ được tạo ra ở bước trước. Hãy chắc chắn ghi chúng theo đúng thứ tự. Sau khi bạn đã ghi chép, kiểm tra lại với những gì được cung cấp bởi phần mềm để đảm bảo bạn đã ghi chép đúng thứ tự. Sau khi bạn đã ghi chép, nhấp vào hộp kiểm xác nhận bạn đã ghi chép cụm từ Seed của mình một cách chính xác.

### Ví dụ: Lưu trữ cụm từ Seed trên một Hardware Wallet

Trong khóa học này, chúng tôi đề cập đến việc lưu trữ cụm từ Seed trên một hardware wallet. Theo dõi khóa học này cùng một giáo viên có thể không luôn bao gồm thiết bị như vậy. Trong tài liệu hướng dẫn của khóa học, đã viết một danh sách các hardware wallet được cung cấp phù hợp với bài tập này.
Chúng ta sẽ sử dụng kho lưu trữ BTCPay Server và ví cứng Blockstream Jade trong ví dụ này.
Bạn cũng có thể theo dõi qua video để tham khảo cách kết nối ví cứng.
![BTCPay Server - Cách kết nối ví cứng của bạn với BTCPay Vault.](https://youtu.be/s4qbGxef43A)

Tải về kho lưu trữ BTCPay Server: https://github.com/btcpayserver/BTCPayServer.Vault/releases

Hãy chắc chắn bạn đã tải về các tệp đúng cho hệ thống của mình. Người dùng Windows nên tải gói [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe), người dùng Mac tải [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg), và người dùng Linux nên tải [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)

Sau khi cài đặt BTCPay Server Vault, khởi động phần mềm bằng cách nhấp vào biểu tượng trên Màn hình Desktop của bạn. Khi BTCPay Server Vault được cài đặt đúng cách và khởi động lần đầu tiên, nó sẽ yêu cầu quyền được sử dụng với Ứng dụng Web. Nó sẽ yêu cầu cấp quyền truy cập cho BTCPay Server cụ thể mà bạn làm việc. Chấp nhận các điều kiện này. BTCPay Server Vault giờ đây sẽ tìm kiếm thiết bị cứng. Một khi thiết bị được tìm thấy, BTCPay Server sẽ nhận ra rằng Vault đang chạy và đã tìm thấy thiết bị của bạn.

**!Lưu Ý!**

Không cung cấp khóa SSH hoặc tài khoản quản trị máy chủ cho bất kỳ ai khác ngoài các quản trị viên khi sử dụng ví nóng. Bất kỳ ai có quyền truy cập vào các tài khoản này sẽ có quyền truy cập vào các quỹ trong Ví Nóng.

### Tóm Tắt Kỹ Năng

Trong phần này, bạn đã học được những điều sau:

- Cách xem giao dịch của ví Bitcoin và các phân loại khác nhau của nó.
- Các lựa chọn khác nhau khi gửi từ ví Bitcoin, từ ví cứng đến ví nóng.
- Vấn đề giới hạn khoảng trống khi sử dụng hầu hết các ví và cách khắc phục.
- Cách tạo một ví Bitcoin mới trong BTCPay Server, bao gồm lưu trữ khóa trong ví cứng và sao lưu cụm từ khôi phục.

Trong mục tiêu này, bạn đã học cách tạo một ví Bitcoin mới trong BTCPay Server. Chúng ta chưa đi vào cách bảo mật hoặc sử dụng những khóa đó. Trong cái nhìn tổng quan nhanh về mục tiêu này, bạn đã học cách thiết lập cửa hàng đầu tiên. Bạn đã học cách tạo cụm từ Khôi phục Bitcoin.

### Đánh Giá Kiến Thức Thực Hành

Mô tả một phương pháp để tạo khóa và một kế hoạch bảo mật chúng, cùng với các sự đánh đổi/ rủi ro của kế hoạch bảo mật.

## Ví Lightning BTCPay Server

<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>

Khi một quản trị viên máy chủ thiết lập một thể hiện BTCPay Server mới, anh ta có thể thiết lập một triển khai mạng lưới Lightning, LND, Core Lightning, hoặc Eclair; xem Phần Cấu hình BTCPay Server để biết hướng dẫn cài đặt chi tiết hơn.
Nếu được áp dụng trong một lớp học, việc kết nối một node Lightning với BTCPay Server của bạn được thực hiện thông qua một Node tùy chỉnh. Người dùng không phải là quản trị viên máy chủ trên BTCPay Server sẽ không thể sử dụng node Lightning nội bộ mặc định. Điều này nhằm bảo vệ chủ sở hữu máy chủ khỏi việc mất tiền. Các quản trị viên máy chủ có thể cài đặt một Plugin để cung cấp quyền truy cập vào node Lightning của họ thông qua LNBank; điều này nằm ngoài phạm vi của cuốn sách này; đọc thêm về LNBank trên trang plugin chính thức.

### Kết nối node nội bộ (quản trị viên máy chủ)

Quản trị viên máy chủ có thể sử dụng Node Lightning nội bộ của BTCPay Server. Bất kể triển khai Lightning nào, việc kết nối với node Lightning nội bộ đều giống nhau.

Đi tới cửa hàng đã thiết lập trước đó và nhấp vào ví "Lightning" trong menu bên trái. BTCPay Server cung cấp hai khả năng thiết lập, sử dụng Node nội bộ (chỉ dành cho quản trị viên máy chủ theo mặc định) hoặc một node tùy chỉnh (kết nối bên ngoài). Các quản trị viên máy chủ có thể nhấp vào tùy chọn "Sử dụng node nội bộ". Không cần cấu hình thêm. Nhấp vào nút "lưu" và chú ý thông báo nói rằng, "Node Lightning BTC đã được cập nhật". Cửa hàng giờ đây đã thành công trong việc có khả năng mạng Lightning.

### Kết nối node bên ngoài (người dùng máy chủ/chủ cửa hàng)

Vì chủ cửa hàng theo mặc định không được phép sử dụng Node Lightning của quản trị viên máy chủ. Việc kết nối cần được thực hiện với một node bên ngoài, hoặc là node thuộc sở hữu của chủ cửa hàng trước khi thiết lập BTCPay Server, một plugin LNBank nếu được quản trị viên máy chủ cung cấp, hoặc một giải pháp giữ hộ như Alby.

Đi tới cửa hàng đã thiết lập trước đó và nhấp vào "Lightning" dưới ví trong menu bên trái. Vì chủ cửa hàng không được phép sử dụng node nội bộ theo mặc định, tùy chọn này bị vô hiệu hóa. Sử dụng một node tùy chỉnh là tùy chọn duy nhất mặc định có sẵn cho chủ cửa hàng.

BTCPay Server cần thông tin kết nối; thông tin cụ thể cho một triển khai Lightning sẽ được cung cấp bởi giải pháp đã thiết lập trước đó (hoặc giải pháp giữ hộ). Trong BTCPay Server, chủ cửa hàng có thể sử dụng các kết nối sau;

- C-lightning qua TCP hoặc Unix domain socket connection.
- Lightning Charge qua HTTPS
- Eclair qua HTTPS
- LND qua proxy REST
- LNDhub qua REST API

![image](assets/en/31.webp)

Nhấp vào "kiểm tra kết nối" để đảm bảo bạn đã nhập đúng chi tiết kết nối. Sau khi kết nối được xác nhận là tốt, nhấp lưu, và BTCPay Server hiển thị cửa hàng được cập nhật với Node Lightning.

### Quản lý node Lightning nội bộ LND (Quản trị viên máy chủ)

Sau khi kết nối Node Lightning nội bộ, các quản trị viên máy chủ sẽ nhận thấy các ô mới trên Bảng điều khiển cụ thể cho thông tin Lightning.

- Số dư Lightning
- BTC trong các kênh
  - BTC mở kênh
  - BTC số dư nội bộ
  - BTC số dư từ xa
  - BTC đóng kênh
- BTC On-chain
  - BTC đã xác nhận
  - BTC chưa xác nhận
  - BTC dự trữ
- Dịch vụ Lightning
  - Ride the Lightning (RTL).

Bằng cách nhấp vào biểu tượng Ride the Lightning trong ô "Dịch vụ Lightning" hoặc "Lightning" dưới ví trong menu bên trái, các quản trị viên máy chủ có thể truy cập RTL để quản lý node Lightning.

**Lưu ý!**

Kết nối Node Lightning nội bộ thất bại - Nếu kết nối nội bộ thất bại, xác nhận:

1. Node Bitcoin on-chain đã được đồng bộ hóa đầy đủ
2. Node Lightning nội bộ được "Kích hoạt" dưới "Lightning" > "Cài đặt" > "Cài đặt Lightning BTC"
   Nếu bạn không thể kết nối với node Lightning của mình, hãy thử khởi động lại máy chủ của bạn, hoặc đọc thêm chi tiết trong tài liệu chính thức của BTCPay Server tại đây; https://docs.btcpayserver.org/Troubleshooting/ . Bạn không thể chấp nhận thanh toán lightning trong cửa hàng của mình cho đến khi node Lightning của bạn hiển thị trạng thái "Online". Hãy thử kiểm tra kết nối Lightning của bạn bằng cách nhấp vào liên kết "Public Node Info"

### Ví Lightning

Trong tùy chọn ví Lightning ở thanh menu bên trái, các quản trị viên máy chủ sẽ tìm thấy quyền truy cập dễ dàng đến RTL, thông tin node công cộng của họ, và các cài đặt Lightning đặc biệt cho cửa hàng BTCPay Server của họ.

#### Thông tin node nội bộ

Các quản trị viên máy chủ có thể nhấp vào thông tin node nội bộ và xem qua trạng thái máy chủ (Online/ Offline) và chuỗi kết nối cho Clearnet hoặc Tor.

![image](assets/en/32.webp)

#### Thay đổi kết nối

Nếu chủ cửa hàng quyết định sử dụng thay đổi trong Cài đặt Lightning - Thay đổi kết nối.
Bên cạnh thông tin node công cộng, chủ cửa hàng có thể tìm thấy tùy chọn này. Nó sẽ quay trở lại cài đặt ban đầu cho kết nối node lightning bên ngoài, điền thông tin node Lightning mới, nhấp lưu và cập nhật cửa hàng với thông tin node mới.

![image](assets/en/33.webp)

#### Dịch vụ

Nếu quản trị viên máy chủ quyết định cài đặt nhiều dịch vụ cho việc triển khai Lightning, chúng sẽ được liệt kê ở đây. Với việc triển khai LND tiêu chuẩn, quản trị viên sẽ có Ride The Lightning (RTL) là công cụ quản lý node tiêu chuẩn.

#### Cài đặt ví BTC Lightning

Sau khi thêm node Lightning vào cửa hàng ở bước trước, trong cài đặt của ví Lightning, chủ cửa hàng vẫn có thể chọn vô hiệu hóa nó cho cửa hàng của họ bằng cách sử dụng Toggle ở đầu cài đặt Lightning.

![image](assets/en/34.webp)

#### Tùy chọn thanh toán Lightning

Chủ cửa hàng có thể thiết lập các tham số sau để nâng cao trải nghiệm Lightning cho khách hàng của họ.

- Hiển thị số lượng thanh toán Lightning bằng Satoshis.
- Thêm gợi ý nhảy cho các kênh riêng tư vào hóa đơn Lightning.
- Thống nhất URL/QR code thanh toán on-chain và Lightning tại điểm thanh toán.
- Thiết lập mẫu mô tả cho hóa đơn lightning.

#### LNURL

Chủ cửa hàng có thể chọn sử dụng hoặc không sử dụng LNURL. Một URL Mạng Lightning, hay LNURL, là một tiêu chuẩn đề xuất cho các tương tác giữa Người thanh toán Lightning và người nhận thanh toán. Nói ngắn gọn, một LNURL là một url được mã hóa bech32 có tiền tố là lnurl. Ví Lightning được mong đợi giải mã URL, liên hệ với URL, và chờ đợi một đối tượng JSON với hướng dẫn tiếp theo, đặc biệt là một thẻ xác định hành vi của lnurl.

- Kích hoạt LNURL
- Chế độ LNURL Cổ điển
  - Đối với sự tương thích ví, mã hóa Bech32 (cổ điển) so với URL văn bản rõ ràng (sắp tới)
- Cho phép người nhận thanh toán gửi bình luận.

### Ví dụ 1

#### Kết nối với Lightning bằng node nội bộ (Quản trị viên)

Tùy chọn này chỉ có sẵn nếu bạn là Quản trị viên của phiên bản này hoặc nếu Quản trị viên đã thay đổi cài đặt mặc định nơi người dùng có thể sử dụng node lightning nội bộ.

Là một quản trị viên, nhấp vào Ví Lightning trong thanh menu bên trái. BTCPay Server sẽ yêu cầu sử dụng một trong hai tùy chọn để kết nối một Node Lightning, một node nội bộ hoặc một node bên ngoài tùy chỉnh. Nhấp vào Sử dụng node nội bộ và nhấp lưu.

#### Quản lý node Lightning của bạn (RTL)

Sau khi kết nối với node lightning nội bộ, BTCPay Server sẽ cập nhật và hiển thị thông báo "BTC Lightning node đã được cập nhật", xác nhận bạn đã kết nối Lightning với cửa hàng của mình.

Quản lý node lightning là nhiệm vụ của Quản trị viên máy chủ. Điều này bao gồm:

- Quản lý giao dịch
- Quản lý thanh khoản
  - Thanh khoản đầu vào
  - Thanh khoản đầu ra
- Quản lý đối tác và kênh
  - Đối tác đã kết nối
  - Phí kênh
  - Trạng thái kênh
- Thực hiện sao lưu thường xuyên các trạng thái kênh.
- Kiểm tra báo cáo định tuyến.
- Hoặc sử dụng các dịch vụ như Loop.

Tất cả các công việc quản lý node Lightning đều được thực hiện thông qua RTL (giả sử bạn đang chạy trên triển khai LND). Quản trị viên có thể nhấp vào Lightning Wallet trong BTCPay Server và tìm nút để mở RTL. Bảng điều khiển chính của BTCPay Server giờ đây được cập nhật với các ô Lightning Network, bao gồm quyền truy cập nhanh đến RTL.

### Ví dụ 2

#### Kết nối với lightning qua Alby

Khi kết nối với một người giữ hộ như Alby, chủ cửa hàng trước tiên nên tạo một tài khoản, truy cập: https://getalby.com/

![hình ảnh](assets/en/35.webp)

Sau khi tạo tài khoản Alby, đi đến cửa hàng BTCPay Server của bạn.

Bước 1: Nhấp vào 'Set up a Lightning node' trên Bảng điều khiển hoặc 'Lightning' dưới mục ví.

![hình ảnh](assets/en/36.webp)

Bước 2: Nhập thông tin xác thực kết nối ví được cung cấp bởi Alby. Trên Bảng điều khiển của Alby, nhấp vào Ví. Tại đây bạn sẽ tìm thấy "Wallet Connection Credentials". Sao chép các thông tin này. Dán thông tin xác thực từ Alby vào trường cấu hình kết nối trong BTCPay Server.

![hình ảnh](assets/en/37.webp)

Bước 3: Sau khi cung cấp cho BTCPay Server các chi tiết kết nối, nhấp vào nút "Test Connection" để đảm bảo kết nối hoạt động đúng cách. Chú ý đến thông báo "Connection to lightning node successful" ở đầu màn hình của bạn. Điều này xác nhận mọi thứ hoạt động ổn định.

![hình ảnh](assets/en/38.webp)

Bước 4: Nhấp lưu, và cửa hàng của bạn giờ đây đã được kết nối với một node lightning qua Alby.

![hình ảnh](assets/en/39.webp)

**!Lưu ý!**

Không bao giờ tin tưởng một giải pháp Lightning giữ hộ với giá trị nhiều hơn bạn sẵn lòng mất.

### Tóm tắt Kỹ năng

Trong phần này bạn đã học:

- Cách kết nối một node Lightning nội bộ hoặc bên ngoài
- Nội dung và chức năng của các ô liên quan đến Lightning trên Bảng điều khiển
- Cách cấu hình ví Lightning sử dụng Voltage Surge hoặc Alby

### Đánh giá Kiến thức Thực hành

Mô tả một số lựa chọn khác nhau để kết nối ví Lightning với cửa hàng của bạn.

# Giao diện BTCPay Server

<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>

## Tổng quan Bảng điều khiển

<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>

BTCPay Server là một gói phần mềm có tính chất mô-đun. Tuy nhiên, có những tiêu chuẩn mà mọi BTCPay Server đều có và Quản trị viên/người dùng sẽ tương tác với. Bắt đầu với Bảng điều khiển. Điểm nhập chính của mọi BTCPay Server sau khi đăng nhập. Bảng điều khiển cung cấp cái nhìn tổng quan về hiệu suất của cửa hàng, số dư ví hiện tại, và các giao dịch cuối cùng trong 7 ngày qua. Vì đây là một cái nhìn có tính chất mô-đun, các Plugin có thể tận dụng cái nhìn này cho lợi ích của mình và tạo các ô của riêng họ trên Bảng điều khiển. Trong sách hướng dẫn này, chúng tôi chỉ nói về các plugin/ứng dụng tiêu chuẩn và các cái nhìn tương ứng của chúng qua BTCPay Server.

### Các ô Bảng điều khiển

Trong cái nhìn chính của bảng điều khiển BTCPay Server có một số ô tiêu chuẩn có sẵn. Các ô này dành cho Chủ cửa hàng hoặc Quản trị viên để nhanh chóng quản lý cửa hàng của mình trong một cái nhìn tổng quan.

- Số dư ví
- Hoạt động giao dịch
- Số dư Lightning (nếu Lightning được kích hoạt trên cửa hàng)
- Dịch vụ Lightning (nếu Lightning được kích hoạt trên cửa hàng)
- Giao dịch gần đây.
- Hóa đơn gần đây
- Các chiến dịch gây quỹ đang hoạt động
- Hiệu suất cửa hàng / các mặt hàng bán chạy nhất.
  Ô Số Dư Ví cung cấp cái nhìn tổng quan nhanh về quỹ và hiệu suất của ví bạn. Nó có thể được xem bằng BTC hoặc tiền tệ Fiat trong biểu đồ hàng tuần, hàng tháng, hoặc hàng năm.
  ![image](assets/en/40.webp)

### Hoạt động Giao dịch

Cạnh Ô Số Dư Ví, BTCPay Server hiển thị tổng quan nhanh về các khoản thanh toán đang chờ, số lượng Giao dịch trong 7 ngày qua, và nếu cửa hàng của bạn đã phát hành bất kỳ khoản hoàn tiền nào. Nhấn vào nút Quản lý sẽ đưa bạn vào quản lý cho các khoản thanh toán đang chờ (tìm hiểu thêm về thanh toán trong BTCPay Server - chương về Thanh toán).

![image](assets/en/41.webp)

### Số Dư Lightning

Chỉ hiển thị khi Lightning được kích hoạt.

Khi Quản trị viên đã cho phép truy cập mạng Lightning, bảng điều khiển BTCPay Server giờ đây có một ô mới với thông tin về nút Lightning của bạn. Bao nhiêu BTC trong các kênh, cách này được cân bằng cục bộ hay từ xa (dung lượng vào hoặc ra) nếu các kênh đang đóng hoặc mở, và bao nhiêu bitcoin được giữ trên chuỗi trên nút lightning.

![image](assets/en/42.webp)

### Dịch Vụ Lightning

Chỉ hiển thị khi lightning được kích hoạt.

Cạnh việc xem số dư Lightning trên bảng điều khiển BTCPay Server, các quản trị viên cũng sẽ thấy ô cho Dịch Vụ Lightning. Tại đây, các quản trị viên có thể tìm thấy các nút nhanh cho các công cụ họ sử dụng để quản lý nút Lightning của mình; ví dụ, Ride the Lightning là một trong những công cụ tiêu chuẩn với BTCPay Server cho quản lý nút Lightning.

![image](assets/en/43.webp)

### Giao dịch Gần Đây

Ô giao dịch gần đây sẽ hiển thị các giao dịch gần đây nhất của cửa hàng bạn. Chỉ với một cú nhấp, Quản trị viên của phiên bản BTCPay Server có thể xem giao dịch mới nhất và xem liệu có cần chú ý đến nó không.

![image](assets/en/44.webp)

### Hóa đơn Gần Đây

Ô hóa đơn gần đây hiển thị 6 hóa đơn mới nhất được tạo bởi BTCPay Server của bạn, bao gồm Trạng thái và số tiền hóa đơn. Ô cũng bao gồm một nút "Xem tất cả" để dễ dàng truy cập tổng quan hóa đơn đầy đủ.

![image](assets/en/45.webp)

### Điểm Bán Hàng và Quyên góp

Vì BTCPay Server cung cấp một bộ plugin tiêu chuẩn hoặc ứng dụng, Điểm Bán Hàng và Quyên góp là hai plugin chính của BTCPay Server. Với mỗi cửa hàng và ví, người dùng BTCPay Server có thể tạo bất kỳ Điểm Bán Hàng hoặc Quyên góp nào mà họ thấy phù hợp. Mỗi cái sẽ tạo một ô bảng điều khiển mới hiển thị hiệu suất của plugin.

![image](assets/en/46.webp)

Chú ý sự khác biệt nhỏ giữa ô Điểm Bán Hàng và Quyên góp. Quản trị viên thấy các mặt hàng bán chạy nhất trong ô Điểm Bán Hàng. Trong ô Quyên góp, điều này trở thành Top Perks. Cả hai ô đều có các nút nhanh để quản lý ứng dụng tương ứng và xem các hóa đơn gần đây được tạo bởi các mặt hàng hàng đầu hoặc top perks.

![image](assets/en/47.webp)

**!?Lưu Ý!?**

Biểu đồ số dư và giao dịch gần đây chỉ có sẵn cho phương thức thanh toán trên chuỗi. Thông tin về số dư và giao dịch Mạng Lightning đang trong danh sách công việc. Tính đến Phiên bản BTCPay Server 1.6.0, số dư Mạng Lightning cơ bản đã có sẵn.

### Tóm Tắt Kỹ Năng

Trong phần này, bạn đã học được những điều sau:

- Cấu trúc cơ bản của các ô trên trang chính được biết đến là Bảng Điều Khiển.
- Hiểu biết cơ bản về nội dung của mỗi ô.

### Đánh Giá Kiến Thức

Liệt kê càng nhiều ô từ Bảng Điều Khiển từ trí nhớ của bạn.

## BTCPay Server - Cài Đặt Cửa Hàng

<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>
Trong phần mềm BTCPay Server, chúng ta biết đến 2 loại cài đặt. Cài đặt cụ thể cho Cửa hàng BTCPay Server, nút cài đặt được tìm thấy ở thanh menu bên trái dưới Dashboard, và cài đặt BTCPay Server, được tìm thấy ở cuối thanh menu ngay trên Account. Cài đặt cụ thể cho Server BTCPay Server chỉ có thể được xem bởi các quản trị viên Server.
Cài đặt cửa hàng bao gồm nhiều tab để phân loại từng bộ cài đặt.

- General
- Rates
- Checkout Appearance
- Access Tokens
- Users
- Roles
- Webhooks
- Payout Processors
- Emails
- Forms

### General

Trong tab Cài đặt Chung, chủ cửa hàng thiết lập thương hiệu và mặc định thanh toán của họ. Tại thiết lập ban đầu của cửa hàng, một tên cửa hàng đã được đặt; điều này sẽ được phản ánh trong Cài đặt Chung dưới Store Name. Tại đây, chủ cửa hàng cũng có thể thiết lập trang web của họ để phù hợp với thương hiệu và một Store ID để Quản trị viên nhận biết trong cơ sở dữ liệu.

#### Branding

Vì BTCPay Server là FOSS, chủ cửa hàng có thể làm thương hiệu tùy chỉnh để phù hợp với cửa hàng của mình. Thiết lập màu sắc thương hiệu, lưu trữ logo của thương hiệu và thêm CSS tùy chỉnh cho các trang đối diện với khách hàng/công chúng (Hóa đơn, Yêu cầu Thanh toán, Rút tiền)

#### Payment

Trong cài đặt thanh toán, chủ cửa hàng thiết lập tiền tệ mặc định cho cửa hàng của họ (bằng Bitcoin hoặc bất kỳ tiền tệ fiat nào).

#### Cho phép bất kỳ ai tạo hóa đơn

Cài đặt này dành cho các nhà phát triển hoặc người xây dựng trên BTCPay Server. Với cài đặt này được bật cho cửa hàng của bạn, nó cho phép thế giới bên ngoài tạo hóa đơn trên thể hiện BTCPay Server của bạn.

#### Thêm phí bổ sung (phí mạng) vào hóa đơn

Một tính năng trong BTCPay để bảo vệ các nhà bán hàng khỏi các cuộc tấn công bụi hoặc khách hàng gây ra chi phí cao về phí sau này khi nhà bán hàng cần di chuyển một lượng lớn bitcoin cùng một lúc. Ví dụ, khách hàng tạo một hóa đơn 20$ và thanh toán một phần, trả 1$ 20 lần cho đến khi hóa đơn được thanh toán đầy đủ. Bây giờ nhà bán hàng có một giao dịch lớn hơn, làm tăng chi phí khai thác trong trường hợp nhà bán hàng quyết định di chuyển số tiền đó sau này. Mặc định, BTCPay áp dụng một chi phí mạng bổ sung vào tổng số tiền của hóa đơn để bao gồm chi phí đó cho nhà bán hàng khi hóa đơn được thanh toán bằng nhiều giao dịch. BTCPay cung cấp một số tùy chọn để tùy chỉnh tính năng bảo vệ này. Bạn có thể áp dụng phí mạng:

- Chỉ khi khách hàng thực hiện nhiều hơn một lần thanh toán cho hóa đơn (Trong ví dụ trên, nếu khách hàng tạo một hóa đơn 20\$ và trả 1\$, tổng số tiền hóa đơn còn nợ bây giờ là 19\$ + phí mạng. Phí mạng được áp dụng sau lần thanh toán đầu tiên)
- Trên mỗi lần thanh toán (bao gồm cả lần thanh toán đầu tiên, trong ví dụ của chúng ta, tổng số sẽ là 20\$ + phí mạng ngay lập tức, ngay cả trong lần thanh toán đầu tiên)
- Không bao giờ thêm phí mạng (vô hiệu hóa hoàn toàn phí mạng)

Mặc dù nó bảo vệ khỏi các giao dịch bụi, nhưng nó cũng có thể phản ánh tiêu cực đối với doanh nghiệp nếu không được thông báo đúng cách. Khách hàng có thể có thêm câu hỏi và nghĩ rằng bạn đang tính phí quá cao.

#### Hóa đơn hết hạn nếu số tiền đầy đủ không được thanh toán sau?

Bộ đếm thời gian của hóa đơn được thiết lập mặc định là 15 phút. Bộ đếm thời gian là một cơ chế bảo vệ chống lại sự biến động vì nó khóa số lượng Bitcoin theo tỷ giá Bitcoin so với tiền tệ fiat. Nếu khách hàng không thanh toán hóa đơn trong khoảng thời gian đã định, hóa đơn được coi là hết hạn. Hóa đơn được coi là "đã thanh toán" ngay khi giao dịch hiển thị trên blockchain (0-xác nhận) nhưng được coi là "hoàn thành" khi đạt được số lần xác nhận mà nhà bán hàng đã định (thường là 1-6). Bộ đếm thời gian có thể tùy chỉnh theo phút.

#### Xem xét hóa đơn đã thanh toán ngay cả khi số tiền thanh toán ít hơn X% so với dự kiến?

Khi khách hàng sử dụng ví giao dịch để trực tiếp thanh toán cho một hóa đơn, sàn giao dịch sẽ thu một khoản phí nhỏ. Điều này có nghĩa là hóa đơn đó không được coi là đã hoàn thành hoàn toàn. Hóa đơn sẽ nhận được trạng thái "đã thanh toán một phần". Bạn có thể thiết lập tỷ lệ phần trăm ở đây nếu một người bán hàng muốn chấp nhận hóa đơn thanh toán thiếu.

### Tỷ lệ

Trong BTCPay Server, khi một hóa đơn được tạo ra, nó luôn cần giá Bitcoin sang tiền tệ fiat chính xác và cập nhật nhất. Khi tạo một cửa hàng mới trong BTCPay Server, quản trị viên được yêu cầu thiết lập nguồn giá ưa thích của họ; sau khi cửa hàng được thiết lập, chủ sở hữu cửa hàng luôn có thể thay đổi nguồn giá của mình trong tab này.

#### Quy tắc tỷ lệ nâng cao

Chủ yếu được sử dụng bởi người dùng có kinh nghiệm. Nếu được bật, chủ sở hữu cửa hàng có thể tạo các kịch bản xung quanh hành vi giá và cách tính phí khách hàng của họ.

#### Kiểm tra

Một nơi kiểm tra nhanh cho các cặp tiền tệ ưa thích của bạn. Điều này cũng bao gồm tính năng kiểm tra các cặp tiền tệ mặc định qua truy vấn REST.

### Giao diện Thanh toán

Tab Giao diện Thanh toán bắt đầu với các cài đặt cụ thể cho hóa đơn và phương thức thanh toán mặc định, và kích hoạt các phương thức thanh toán cụ thể khi đáp ứng được các yêu cầu đã đặt.

#### Cài đặt hóa đơn

Phương thức thanh toán mặc định. BTCPay Server trong cấu hình tiêu chuẩn có ba lựa chọn.

- BTC (trên chuỗi)
- BTC (LNURL-pay)
- BTC (Ngoài chuỗi & Lightning)

Chúng ta có thể thiết lập các tham số cho cửa hàng của mình, nơi khách hàng chỉ tương tác với Lightning khi giá nhỏ hơn X số tiền và ngược lại cho giao dịch trên chuỗi khi X lớn hơn Y luôn hiển thị tùy chọn thanh toán trên chuỗi.

![image](assets/en/48.webp)

#### Thanh toán

Tính đến phiên bản phát hành 1.7 của BTCPay Server, một giao diện Thanh toán mới đã được giới thiệu, được gọi là Checkout V2. Kể từ phiên bản 1.9 được chuẩn hóa, quản trị viên và chủ sở hữu cửa hàng vẫn có thể thiết lập giao diện thanh toán về phiên bản trước. Bằng cách sử dụng chuyển đổi "Sử dụng giao diện thanh toán cổ điển", chủ sở hữu cửa hàng có thể đặt cửa hàng trở lại trải nghiệm thanh toán trước đó. BTCPay Server cũng có một bộ các cài đặt sẵn cho Thương mại Trực tuyến hoặc trải nghiệm tại cửa hàng.

![image](assets/en/49.webp)

Khi khách hàng tương tác với cửa hàng và tạo ra một hóa đơn, có một thời gian hết hạn cho hóa đơn. Theo mặc định, BTCPay Server thiết lập điều này là 5 phút, và Quản trị viên có thể thiết lập điều này theo như họ thấy phù hợp. Trang thanh toán có thể được tùy chỉnh thêm bằng cách kiểm tra các tham số sau:

- Kỷ niệm việc thanh toán bằng cách hiển thị confetti
- Hiển thị tiêu đề cửa hàng (Tên và logo)
- Hiển thị nút "Thanh toán trong ví"
- Thống nhất URL/QR của thanh toán trên chuỗi và ngoài chuỗi
- Hiển thị số lượng thanh toán Lightning bằng Satoshis
- Tự động phát hiện ngôn ngữ khi thanh toán

![image](assets/en/50.webp)

Khi Tự động phát hiện ngôn ngữ không được thiết lập, BTCPay Server, theo mặc định, sẽ hiển thị tiếng Anh. Chủ sở hữu cửa hàng có thể thay đổi mặc định này sang ngôn ngữ ưa thích của họ.

![image](assets/en/51.webp)

Nhấp vào Drop down và Chủ sở hữu cửa hàng có thể thiết lập một Tiêu đề HTML Tùy chỉnh để hiển thị trên trang thanh toán.

![image](assets/en/52.webp)

Để đảm bảo khách hàng biết phương thức thanh toán của mình, chủ sở hữu cửa hàng có thể rõ ràng thiết lập thanh toán của mình luôn yêu cầu người dùng chọn phương thức thanh toán ưa thích của họ. Khi hóa đơn được thanh toán, BTCPay Server cho phép khách hàng quay trở lại cửa hàng trực tuyến. Chủ sở hữu cửa hàng có thể thiết lập điều hướng này sau khi khách hàng đã thanh toán tự động.

![image](assets/en/53.webp)

#### Biên lai công khai

Trong cài đặt biên lai công khai, chủ sở hữu cửa hàng có thể thiết lập các trang biên lai thành công khai và hiển thị danh sách thanh toán trên trang biên lai cũng như mã QR của biên lai để khách hàng dễ dàng truy cập số hóa.
![image](assets/vi/54.webp)

### Token Truy Cập

Token truy cập được sử dụng để ghép nối với một số tích hợp thương mại điện tử hoặc tích hợp xây dựng tùy chỉnh.

![image](assets/vi/55.webp)

### Người Dùng

Người dùng cửa hàng là nơi chủ cửa hàng có thể quản lý nhân viên của mình, tài khoản của họ và quyền truy cập vào cửa hàng. Sau khi nhân viên tạo tài khoản của họ, chủ cửa hàng có thể thêm người dùng cụ thể vào cửa hàng dưới dạng Khách hoặc chủ sở hữu. Để xác định thêm vai trò của nhân viên, tham khảo phần tiếp theo về “Cài đặt Cửa hàng BTCPay Server - Vai trò.”

![image](assets/vi/56.webp)

### Vai Trò

Chủ cửa hàng có thể thấy vai trò tiêu chuẩn của người dùng không đủ quan trọng. Trong cài đặt vai trò tùy chỉnh, chủ cửa hàng có thể xác định nhu cầu cụ thể cho mỗi vai trò trong doanh nghiệp của mình.

(1) Để tạo một vai trò mới, nhấn vào nút "+ Thêm vai trò".

![image](assets/vi/57.webp)

(2) Nhập tên Vai trò, ví dụ, "Thu Ngân".

![image](assets/vi/58.webp)

(3) Cấu hình các quyền riêng lẻ cho vai trò.

- Chỉnh sửa cửa hàng của bạn.
- Quản lý tài khoản giao dịch liên kết với cửa hàng của bạn.
  - Xem tài khoản giao dịch liên kết với cửa hàng của bạn.
- Quản lý các khoản thanh toán kéo của bạn.
- Tạo các khoản thanh toán kéo.
  - Tạo các khoản thanh toán kéo không được phê duyệt.
- Chỉnh sửa hóa đơn.
  - Xem hóa đơn.
  - Tạo hóa đơn.
  - Tạo hóa đơn từ các nút lightning liên kết với cửa hàng của bạn.
- Xem cửa hàng của bạn.
  - Xem hóa đơn.
  - Xem các yêu cầu thanh toán của bạn.
  - Chỉnh sửa webhook của cửa hàng.
- Chỉnh sửa các yêu cầu thanh toán của bạn.
  - Xem các yêu cầu thanh toán của bạn.
- Sử dụng các nút lightning liên kết với cửa hàng của bạn.
  - Xem các hóa đơn lightning liên kết với cửa hàng của bạn.
  - Tạo hóa đơn từ các nút lightning liên kết với cửa hàng của bạn.
- Gửi tiền vào tài khoản giao dịch liên kết với cửa hàng của bạn.
- Rút tiền từ tài khoản giao dịch về cửa hàng của bạn.
- Giao dịch tiền trên tài khoản giao dịch của cửa hàng.

Khi vai trò được tạo, tên sẽ được cố định và không thể thay đổi sau khi ở chế độ chỉnh sửa.

![image](assets/vi/59.webp)

### Webhooks

Trong BTCPay Server, việc tạo một "Webhook" mới khá dễ dàng. Trong tab Cài đặt Cửa hàng BTCPay Server - Webhooks, chủ cửa hàng có thể dễ dàng tạo một webhook mới bằng cách nhấn vào "+ Tạo Webhook". Webhooks cho phép BTCPay Server gửi các sự kiện HTTP liên quan đến cửa hàng của bạn đến các máy chủ khác hoặc tích hợp thương mại điện tử.

![image](assets/vi/60.webp)

Bạn đang ở trong giao diện tạo Webhook. Đảm bảo bạn biết URL Payload của mình và dán nó vào BTCPay Server của bạn. Trong khi bạn đã dán URL Payload, phía dưới nó hiển thị bí mật webhook. Sao chép bí mật webhook và cung cấp nó trên điểm cuối. Khi mọi thứ đã được thiết lập, bạn có thể chuyển đổi trong BTCPay Server để Giao lại tự động. Chúng tôi sẽ cố gắng giao lại bất kỳ giao hàng nào thất bại sau 10 giây, 1 phút, và lên đến 6 lần sau 10 phút. Bạn có thể chuyển đổi giữa mọi sự kiện hoặc chỉ định các sự kiện theo nhu cầu của bạn. Hãy chắc chắn kích hoạt webhook và nhấn Thêm webhook để lưu nó.

![image](assets/vi/61.webp)

Webhooks không được thiết kế để tương thích với API Bitpay. Có hai IPN riêng biệt (trong thuật ngữ BitPay: "Thông báo Thanh toán Tức thì") trong BTCPay Server.

- Webhook
- Thông báo

Chỉ sử dụng URL Thông báo khi bạn tạo hóa đơn qua api Bitpay.

### Quy Trình Thanh Toán

Các bộ xử lý thanh toán hoạt động cùng với khái niệm Thanh toán trong BTCPay Server. Một trình tổng hợp thanh toán để gộp nhiều giao dịch và gửi chúng cùng một lúc. Với các bộ xử lý thanh toán, chủ cửa hàng có thể tự động hóa việc thanh toán gộp. BTCPay Server cung cấp hai phương thức thanh toán tự động, On-chain và Off-chain (LN).
Chủ cửa hàng có thể nhấp và cấu hình cả hai bộ xử lý thanh toán riêng biệt. Một chủ cửa hàng có thể chỉ muốn chạy bộ xử lý on-chain mỗi X giờ một lần, trong khi off-chain có thể diễn ra mỗi vài phút. Đối với On-chain, bạn cũng có thể thiết lập mục tiêu cho khối nào nó nên được bao gồm. Theo mặc định, điều này được thiết lập là 1 (hoặc khối tiếp theo có sẵn). Lưu ý rằng việc thiết lập bộ xử lý thanh toán Off-chain chỉ có bộ hẹn giờ và không có mục tiêu khối. Các khoản thanh toán qua mạng Lightning là tức thì.

![hình ảnh](assets/en/62.webp)
![hình ảnh](assets/en/63.webp)

Chủ cửa hàng chỉ có thể cấu hình bộ xử lý on-chain nếu họ có một Hot-wallet kết nối với cửa hàng của họ.

![hình ảnh](assets/en/64.webp)

Sau khi thiết lập một Bộ xử lý thanh toán, bạn có thể nhanh chóng loại bỏ hoặc chỉnh sửa nó bằng cách quay trở lại tab Bộ xử lý thanh toán trong cài đặt Cửa hàng BTCPay Server.

**!?Lưu Ý!?**

Bộ xử lý thanh toán on-chain - Bộ xử lý thanh toán onchain chỉ có thể hoạt động trên một cửa hàng được cấu hình với một Hot wallet đã kết nối. Nếu không có hot wallet được kết nối, BTCPay Server không giữ chìa khóa của ví và sẽ không thể tự động xử lý các khoản thanh toán.

### Emails

BTCPay Server có thể sử dụng Emails cho Thông báo hoặc, khi được thiết lập đúng cách, để khôi phục các tài khoản đã được tạo trên hệ thống, vì theo mặc định BTCPay Server không gửi email khi mật khẩu bị mất, ví dụ.

![hình ảnh](assets/en/65.webp)

Trước khi chủ cửa hàng có thể thiết lập các quy tắc Email để kích hoạt dựa trên các sự kiện cụ thể của cửa hàng mình, chúng ta phải thiết lập một số cài đặt email cơ bản. BTCPay Server cần những cài đặt này để gửi email cho các sự kiện dựa trên cửa hàng của bạn hoặc để đặt lại mật khẩu.

BTCPay Server đã làm cho việc điền thông tin này dễ dàng hơn bằng cách sử dụng tùy chọn "Điền Nhanh":

- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid

Bằng cách sử dụng tùy chọn điền nhanh, BTCPay Server sẽ tự động điền các trường cho máy chủ SMTP và cổng; bây giờ, chủ cửa hàng chỉ cần điền thông tin đăng nhập của mình vào địa chỉ Email, Đăng nhập (thường giống với địa chỉ email của bạn), và mật khẩu của bạn. Tùy chọn nâng cao mà BTCPay Server cung cấp trong cài đặt email là Vô hiệu hóa kiểm tra bảo mật Chứng chỉ TLS; theo mặc định, điều này được Bật.

![hình ảnh](assets/en/66.webp)

Với các quy tắc Email, chủ cửa hàng có thể thiết lập các sự kiện cụ thể để kích hoạt email đến các địa chỉ email cụ thể.

- Hóa đơn Đã Tạo
- Hóa đơn Nhận Thanh toán
- Hóa đơn Đang Xử lý
- Hóa đơn Hết hạn
- Hóa đơn Đã Giải quyết
- Hóa đơn Không hợp lệ
- Thanh toán Hóa đơn Đã Giải quyết

Nếu khách hàng đã cung cấp địa chỉ Email, những kích hoạt này cũng có thể gửi thông tin cho khách hàng. Chủ cửa hàng có thể tự điền dòng Chủ đề để làm rõ lý do tại sao Email này được gửi và kích hoạt nào đã gây ra nó.

![hình ảnh](assets/en/67.webp)

### Forms

Vì BTCPay Server không thu thập bất kỳ dữ liệu nào, chủ cửa hàng có thể muốn thêm một biểu mẫu tùy chỉnh vào trải nghiệm thanh toán của họ; theo cách này, chủ cửa hàng có thể thu thập thêm thông tin từ khách hàng của mình. Bộ xây dựng Form của BTCPay Server bao gồm hai phần, một cái nhìn trực quan và một cái nhìn mã nâng cao hơn về các biểu mẫu.
Khi tạo một biểu mẫu mới, BTCPay Server mở một cửa sổ mới yêu cầu thông tin cơ bản về những gì bạn muốn biểu mẫu mới của mình yêu cầu. Đầu tiên, chủ cửa hàng cần đặt một tên rõ ràng cho biểu mẫu mới của mình, tên này KHÔNG thể thay đổi sau khi đã được thiết lập.
![image](assets/en/68.webp)

Sau khi chủ cửa hàng đặt tên cho biểu mẫu, bạn cũng có thể chuyển công tắc "Cho phép biểu mẫu sử dụng công cộng" sang ON, và nó sẽ chuyển sang màu xanh. Điều này để biểu mẫu được sử dụng ở mọi nơi tiếp xúc với khách hàng. Ví dụ, nếu một chủ cửa hàng tạo 1 hóa đơn riêng biệt không qua Điểm Bán Hàng của mình, anh ta vẫn muốn thu thập thông tin từ khách hàng; việc chuyển sang ON cho phép thu thập thông tin đó.

![image](assets/en/69.webp)

Mỗi biểu mẫu bắt đầu với ít nhất 1 Trường biểu mẫu mới. Chủ cửa hàng có thể chọn loại trường nào nên là;

- Văn bản
- Số
- Mật khẩu
- Email
- URL
- Số điện thoại
- Ngày
- Trường ẩn
- Fieldset
- Một khu vực văn bản cho nhận xét mở.
- Bộ chọn tùy chọn

Mỗi loại đều đi kèm với các tham số để điền. Chủ cửa hàng có thể thiết lập theo ý mình. Dưới trường đầu tiên được tạo, chủ cửa hàng có thể tiếp tục thêm các trường mới vào biểu mẫu này.

![image](assets/en/70.webp)

#### Biểu mẫu tùy chỉnh nâng cao

BTCPay Server cũng cho phép bạn xây dựng Biểu mẫu trong mã. Cụ thể là JSON. Thay vì nhìn vào trình soạn thảo, chủ cửa hàng có thể nhấp vào nút CODE ngay cạnh trình soạn thảo và vào mã của Biểu mẫu của họ. Trong định nghĩa trường, chỉ có các trường sau có thể được thiết lập; giá trị của các trường được lưu trong metadata của hóa đơn:

| Trường                | Mô tả                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| .fields.constant      | Nếu đúng, .value phải được thiết lập trong định nghĩa biểu mẫu, và người dùng sẽ không thể thay đổi giá trị của trường. (ví dụ: phiên bản định nghĩa biểu mẫu)                                                                                                                                                                                                                                                                                                                                                |
| .fields.type          | Loại đầu vào HTML text, radio, checkbox, password, hidden, button, color, date, datetime-local, month, week, time, email, number, range, search, url, select, tel                                                                                                                                                                                                                                                                                                                                             |
| .fields.options       | Nếu .fields.type là select, danh sách các giá trị có thể chọn                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.options.text  | Văn bản hiển thị cho tùy chọn này                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| .fields.options.value | Giá trị của trường nếu tùy chọn này được chọn                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.type=fieldset | Tạo một HTML fieldset xung quanh các .fields.fields con (xem bên dưới)                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| .fields.name          | Tên thuộc tính JSON của trường như nó sẽ xuất hiện trong metadata của hóa đơn                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| .fields.value         | Giá trị mặc định của trường                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| .fields.required      | nếu đúng, trường sẽ được yêu cầu                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| .fields.label         | Nhãn của trường                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| .fields.helpText      | Văn bản bổ sung để cung cấp giải thích cho trường.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| .fields.fields        | Bạn có thể tổ chức các trường của mình theo một cấu trúc phân cấp, cho phép các trường con được lồng vào metadata của hóa đơn. Cấu trúc này có thể giúp bạn tổ chức và quản lý thông tin thu thập được một cách tốt hơn, làm cho việc truy cập và giải thích thông tin trở nên dễ dàng hơn. Ví dụ, nếu bạn có một biểu mẫu thu thập thông tin khách hàng, bạn có thể nhóm các trường dưới một trường cha có tên là khách hàng. Trong trường cha này, bạn có thể có các trường con như tên, Email, và địa chỉ. |

Tên trường đại diện cho tên thuộc tính JSON lưu trữ giá trị do người dùng cung cấp trong metadata của hóa đơn. Một số tên quen thuộc có thể được giải thích và thay đổi cài đặt của hóa đơn.

| Tên trường       | Mô tả               |
| ---------------- | ------------------- |
| invoice_amount   | Số tiền của hóa đơn |
| invoice_currency | Tiền tệ của hóa đơn |

Bạn có thể tự động điền trước các trường của hóa đơn bằng cách thêm chuỗi truy vấn vào URL của biểu mẫu, như "?your_field=value".

Dưới đây là một số trường hợp sử dụng cho tính năng này:

- Hỗ trợ nhập liệu của người dùng: Điền trước các trường với thông tin khách hàng đã biết để giúp họ hoàn thành biểu mẫu dễ dàng hơn. Ví dụ, nếu bạn đã biết địa chỉ email của một khách hàng, bạn có thể điền trước trường email để tiết kiệm thời gian cho họ.
- Cá nhân hóa: Tùy chỉnh biểu mẫu dựa trên sở thích hoặc phân loại khách hàng. Ví dụ, nếu bạn có các cấp độ khách hàng khác nhau, bạn có thể điền trước biểu mẫu với dữ liệu liên quan, như cấp độ thành viên của họ hoặc các ưu đãi cụ thể.
- Theo dõi: Theo dõi nguồn gốc của lượt truy cập của khách hàng sử dụng các trường ẩn và giá trị điền trước. Ví dụ, bạn có thể tạo liên kết với các giá trị utm_media được điền trước cho mỗi kênh tiếp thị (ví dụ, Twitter, Facebook, Email). Điều này giúp bạn phân tích hiệu quả của các nỗ lực tiếp thị của mình.
- Thử nghiệm A/B: Điền trước các trường với các giá trị khác nhau để thử nghiệm các phiên bản biểu mẫu khác nhau, cho phép bạn tối ưu hóa trải nghiệm người dùng và tỷ lệ chuyển đổi.

### Tóm Tắt Kỹ Năng

Trong phần này, bạn đã học được những điều sau:

- Bố cục và chức năng của các tab trong Cài Đặt Cửa Hàng
- Nhiều lựa chọn để điều chỉnh việc xử lý tỷ giá hối đoái cơ bản, thanh toán một phần, thanh toán thiếu một chút, và hơn nữa.
- Tùy chỉnh giao diện thanh toán, bao gồm việc kích hoạt chính chuỗi so với Lightning tùy thuộc vào giá trên hóa đơn.
- Quản lý cấp độ truy cập và quyền hạn của cửa hàng qua các vai trò.
- Cấu hình tự động gửi email và các kích hoạt của chúng
- Tạo biểu mẫu tùy chỉnh để thu thập thông tin khách hàng bổ sung khi thanh toán.

### Đánh Giá Kiến Thức

#### Đánh Giá KA

Sự khác biệt giữa Cài Đặt Cửa Hàng và Cài Đặt Máy Chủ là gì?

#### Giả Định KA

Mô tả một số lựa chọn bạn có thể chọn trong Giao Diện Thanh Toán > Cài Đặt Hóa Đơn, và lý do tại sao.

## BTCPay Server - Cài Đặt Máy Chủ

<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>

BTCPay Server bao gồm hai giao diện cài đặt khác nhau. Một dành cho Cài Đặt Cửa Hàng và một dành cho Cài Đặt Máy Chủ. Cài đặt máy chủ chỉ có sẵn nếu bạn là Quản trị viên Máy chủ và không dành cho chủ cửa hàng. Quản trị viên máy chủ có thể thêm người dùng, tạo vai trò tùy chỉnh, cấu hình máy chủ email, thiết lập chính sách, thực hiện các nhiệm vụ bảo trì, kiểm tra tất cả các dịch vụ gắn với BTCPay Server, tải tệp lên máy chủ, hoặc kiểm tra Nhật ký.

### Người dùng

Như đã đề cập trong phần trước, Quản trị viên Máy chủ có thể mời người dùng vào máy chủ của họ bằng cách thêm họ vào tab Người dùng.

### Vai trò tùy chỉnh trên toàn máy chủ

BTCPay Server biết hai loại vai trò tùy chỉnh, vai trò tùy chỉnh cụ thể của cửa hàng và vai trò Tùy chỉnh trên toàn máy chủ trong cài đặt BTCPay Server. Cả hai đều có một bộ quyền tương tự; tuy nhiên, nếu được thiết lập thông qua tab Cài Đặt BTCPay Server - Vai trò, vai trò áp dụng sẽ có phạm vi trên toàn máy chủ và áp dụng cho nhiều cửa hàng. Lưu ý một nhãn "Trên toàn máy chủ" đối với các vai trò tùy chỉnh trong Cài đặt Máy chủ.

### Các Vai Trò Tùy Chỉnh Trên Toàn Server

Bộ quyền của các vai trò tùy chỉnh trên toàn server:

- Chỉnh sửa cửa hàng của bạn.
- Quản lý các tài khoản giao dịch liên kết với cửa hàng của bạn.
  - Xem các tài khoản giao dịch liên kết với cửa hàng của bạn.
- Quản lý các khoản thanh toán kéo của bạn.
- Tạo các khoản thanh toán kéo.
  - Tạo các khoản thanh toán kéo không được phê duyệt.
- Chỉnh sửa hóa đơn.
  - Xem hóa đơn.
  - Tạo hóa đơn.
  - Tạo hóa đơn từ các nút lightning liên kết với cửa hàng của bạn.
- Xem cửa hàng của bạn.
  - Xem hóa đơn.
  - Xem các yêu cầu thanh toán của bạn.
  - Chỉnh sửa webhook của cửa hàng.
- Chỉnh sửa các yêu cầu thanh toán của bạn.
  - Xem các yêu cầu thanh toán của bạn.
- Sử dụng các nút lightning liên kết với cửa hàng của bạn.
  - Xem các hóa đơn lightning liên kết với cửa hàng của bạn.
  - Tạo hóa đơn từ các nút lightning liên kết với cửa hàng của bạn.
- Nạp tiền vào các tài khoản giao dịch liên kết với cửa hàng của bạn.
- Rút tiền từ các tài khoản giao dịch về cửa hàng của bạn.
- Giao dịch tiền trên các tài khoản giao dịch của cửa hàng.

**!?Lưu Ý!?**

Khi vai trò được tạo, tên sẽ được cố định và không thể thay đổi sau trong chế độ chỉnh sửa.

### Email

Cài đặt Email trên toàn server trông tương tự như cài đặt Email cụ thể của cửa hàng. Tuy nhiên, thiết lập này không chỉ xử lý các kích hoạt cho cửa hàng hoặc nhật ký quản trị viên. Thiết lập Email này cũng làm cho khả năng khôi phục mật khẩu trên BTCPay Server tại trang đăng nhập trở nên khả dụng. Nó hoạt động tương tự như cài đặt cụ thể của cửa hàng; quản trị viên có thể nhanh chóng điền vào các thông số Email của họ và nhập thông tin đăng nhập email, và server giờ đây có thể gửi email.

### Chính Sách

Các quản trị viên chính sách của BTCPay Server có thể thiết lập một số cài đặt về các chủ đề như Cài đặt Người Dùng Hiện Tại, Cài đặt Người Dùng Mới, Cài đặt Thông Báo, và Cài đặt Bảo Trì. Những cài đặt này dành cho việc đăng ký người dùng mới làm quản trị viên hoặc người dùng bình thường hoặc thậm chí ẩn BTCPay Server khỏi các công cụ tìm kiếm bằng cách thêm vào tiêu đề server của bạn.

#### Cài đặt Người Dùng Hiện Tại

Các tùy chọn có sẵn ở đây tách biệt từ các vai trò tùy chỉnh. Những quyền hạn bổ sung này có thể làm cho cửa hàng hoặc chủ cửa hàng dễ bị tấn công. Các chính sách có thể được thêm vào cho người dùng hiện tại:

- Cho phép người dùng không phải admin sử dụng nút Lightning nội bộ trong cửa hàng của họ.
  - Điều này sẽ cho phép chủ cửa hàng sử dụng nút Lightning của quản trị viên server và do đó, sử dụng tiền của anh ta! Hãy cẩn thận, đây không phải là giải pháp để cung cấp quyền truy cập vào Lightning.
- Cho phép người dùng không phải admin tạo ví nóng cho cửa hàng của họ.
  - Điều này sẽ cho phép bất kỳ ai có tài khoản trên phiên bản BTCPay Server của bạn tạo Ví nóng và lưu trữ hạt giống khôi phục trên server của Quản trị viên. Điều này có thể khiến Quản trị viên chịu trách nhiệm giữ tiền của bên thứ ba!
- Cho phép người dùng không phải admin nhập ví nóng cho cửa hàng của họ.
  - Tương tự như chủ đề tạo Ví nóng trước đó, chính sách này cho phép nhập một ví nóng, với những nguy hiểm đã được đề cập trong phần tạo Ví nóng.

#### Cài đặt Người Dùng Mới

Chúng ta có thể thiết lập một số cài đặt quan trọng để quản lý người dùng mới đến server. Chúng ta có thể thiết lập một email xác nhận cho đăng ký mới, Vô hiệu hóa việc tạo người dùng mới qua màn hình đăng nhập, và hạn chế quyền truy cập của người dùng không phải admin đến việc tạo người dùng qua API.

- Yêu cầu email xác nhận để đăng ký.
  - Quản trị viên server phải đã thiết lập một máy chủ Email!
- Vô hiệu hóa đăng ký người dùng mới trên server
- Vô hiệu hóa quyền truy cập của người dùng không phải admin đến điểm cuối API tạo người dùng.

Mặc định, BTCPay Server đã bật Vô hiệu hóa đăng ký người dùng mới và tắt quyền truy cập của người dùng không phải admin đến điểm cuối API tạo người dùng. Điều này xuất phát từ khía cạnh an ninh, nơi không có người lạ nào có thể tìm thấy trang đăng nhập BTCPay của server bạn và bắt đầu tạo tài khoản.

#### Cài Đặt Thông Báo

![image](assets/en/76.webp)

#### Cài Đặt Bảo Trì

BTCPay Server là một dự án mã nguồn mở tồn tại trên GitHub. Mỗi khi BTCPay Server phát hành một phiên bản mới của phần mềm, các Quản trị viên có thể được thông báo rằng một phiên bản mới đã sẵn sàng. Các quản trị viên cũng có thể muốn ngăn chặn các công cụ tìm kiếm (google, yahoo, duckduckgo) từ việc lập chỉ mục tên miền BTCPay Server. Vì BTCPay Server là FOSS, các nhà phát triển trên toàn thế giới có thể muốn tạo ra các tính năng mới; BTCPay Server có một tính năng thử nghiệm khi được bật, và một quản trị viên có thể sử dụng các tính năng không dành cho sản xuất mà chỉ dùng để thử nghiệm.

- Kiểm tra các bản phát hành trên GitHub và thông báo khi có phiên bản mới của BTCPay Server.
- Ngăn chặn các công cụ tìm kiếm lập chỉ mục trang web này
- Kích hoạt các tính năng thử nghiệm.

![image](assets/en/77.webp)

#### Plugins

BTCPay Server có thể thêm Plugins và mở rộng bộ tính năng của mình. Các plugin, theo mặc định, được tải từ kho lưu trữ plugin-builder của BTCPay Server. Tuy nhiên, một quản trị viên có thể chọn xem các plugin ở trạng thái Pre-release, và nếu nhà phát triển plugin cho phép, quản trị viên máy chủ có thể cài đặt các phiên bản beta của plugin.

![image](assets/en/78.webp)

##### Cài Đặt Tùy Chỉnh

Một triển khai BTCPay Server tiêu chuẩn sẽ có thể truy cập thông qua tên miền được thiết lập cho nó khi cài đặt. Tuy nhiên, một quản trị viên máy chủ có thể ánh xạ lại tên miền gốc và hiển thị một trong các ứng dụng đã tạo từ một cửa hàng cụ thể. Quản trị viên máy chủ cũng có thể ánh xạ các tên miền cụ thể cho các ứng dụng cụ thể.

- Hiển thị ứng dụng trên gốc của trang web
  - Hiển thị danh sách các ứng dụng có thể hiển thị trên tên miền gốc.

![image](assets/en/79.webp)

- Ánh xạ các tên miền cụ thể cho các ứng dụng cụ thể.
  - Khi bạn nhấp để thiết lập một tên miền cụ thể cho các ứng dụng cụ thể, Quản trị viên có thể thiết lập nhiều tên miền chỉ đến các ứng dụng cần thiết.

![image](assets/en/80.webp)

#### Công cụ khám phá khối

BTCPay Server, theo mặc định, sử dụng mempool.space làm công cụ khám phá khối cho các giao dịch. Khi BTCPay Server tạo một hóa đơn mới và có một giao dịch liên quan đến nó, chủ cửa hàng có thể nhấp để mở giao dịch; BTCPay Server sẽ chỉ đến mempool.space làm công cụ khám phá khối; một quản trị viên máy chủ có thể thay đổi điều này theo sở thích của mình.

![image](assets/en/81.webp)

### Dịch Vụ

Tab cài đặt BTCPay Server: Dịch vụ là một cái nhìn tổng quan về các thành phần mà BTCPay Server của bạn sử dụng. Các dịch vụ mà BTCPay Server của bạn cung cấp có thể thay đổi tùy thuộc vào phương pháp triển khai.

Một Quản trị viên BTCPay Server có thể nhấp vào “Xem thông tin” sau mỗi dịch vụ để mở nó và thiết lập các cài đặt cụ thể.

![image](assets/en/82.webp)

#### LND (gRPC)

BTCPay tiếp xúc dịch vụ gRPC của LND cho việc sử dụng bên ngoài; bạn sẽ tìm thấy thông tin kết nối trong menu cài đặt cụ thể này; ví tương thích được liệt kê ở đây. BTCPay Server cũng cung cấp mã QR để kết nối, quét và áp dụng trong ví di động.

Quản trị viên máy chủ có thể mở thêm chi tiết để xem;

- Chi tiết máy chủ
- Sử dụng SSL
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon
- Bộ mã hóa SSL GRPC (GRPC_SSL_CIPHER_SUITES)

#### LND (REST)

BTCPay tiếp xúc dịch vụ REST của LND cho việc sử dụng bên ngoài; bạn sẽ tìm thấy thông tin kết nối ở đây; ví tương thích được liệt kê ở đây. Trong số các ví tương thích có Joule, Alby, và ZeusLN. BTCPay Server cung cấp mã QR để kết nối, quét và áp dụng trong ví tương thích.

- Uri REST
- Macaroon
- AdminMacaroon - InvoiceMacaroon
- ReadonlyMacaroon

#### Sao Lưu Seed LND

Việc sao lưu seed LND hữu ích để khôi phục quỹ từ ví LND của bạn trong trường hợp máy chủ của bạn bị hỏng. Vì node Lightning là một ví Hot-wallet, bạn có thể tìm thấy thông tin seed bảo mật trên trang này.

LND tài liệu hóa quy trình khôi phục. Xem https://github.com/lightningnetwork/lnd/blob/master/docs/recovery.md để biết tài liệu.

#### Ride The Lightning

Ride the Lightning là một công cụ quản lý node Lightning được xây dựng dưới dạng phần mềm mã nguồn mở. BTCPay Server sử dụng RTL làm thành phần quản lý node Lightning trong ngăn xếp của mình. Quản trị viên BTCPay Server có thể truy cập RTL thông qua cài đặt máy chủ - tab Dịch vụ hoặc bằng cách nhấp vào ví Lightning.

#### Full node P2P

Quản trị viên máy chủ có thể muốn kết nối node Bitcoin của họ với ví di động. Trang này cung cấp thông tin để kết nối từ xa với full node của bạn qua giao thức P2P. Tính đến thời điểm viết cuốn sách này, BTCPay Server liệt kê Blockstream Green và Wasabi wallet là ví tương thích. BTCPay Server cung cấp mã QR để kết nối, quét và áp dụng trong ví tương thích.

#### Full node RPC

Trang này cung cấp thông tin để kết nối từ xa với full node của bạn qua giao thức RPC.

#### SSH

SSH được sử dụng cho mục đích bảo trì. BTCPay Server hiển thị lệnh kết nối ban đầu để truy cập máy chủ của bạn và khóa công khai SSH được ủy quyền để kết nối với máy chủ của bạn. Quản trị viên máy chủ có thể muốn tắt thay đổi SSH qua giao diện người dùng của BTCPay Server.

#### Dynamic DNS

Dynamic DNS cho phép bạn có một tên DNS ổn định trỏ đến máy chủ của bạn, ngay cả khi địa chỉ IP của bạn thay đổi thường xuyên. Điều này được khuyến khích nếu bạn lưu trữ BTCPay Server tại nhà và muốn có một tên miền clearnet để truy cập máy chủ của bạn.

Lưu ý rằng bạn cần cấu hình đúng NAT và cài đặt BTCPay Server của mình để nhận chứng chỉ HTTPS.

### Theme

BTCPay Server, theo mặc định, đi kèm với hai chủ đề: Chế độ Sáng và Tối. Bạn có thể chuyển đổi bằng cách Nhấp vào Tài khoản ở góc dưới bên trái và chuyển đổi giữa chủ đề Tối hoặc Sáng. Quản trị viên BTCPay Server có thể thêm chủ đề của riêng mình bằng cách cung cấp một chủ đề CSS tùy chỉnh.

Quản trị viên có thể mở rộng chủ đề Sáng/Tối bằng cách thêm CSS tùy chỉnh của riêng họ hoặc thiết lập chủ đề tùy chỉnh của họ làm một chủ đề tùy chỉnh hoàn toàn.

![image](assets/en/83.webp)

#### Branding Máy Chủ

Quản trị viên máy chủ có thể thay đổi branding của BTCPay Server bằng cách thiết lập branding toàn máy chủ của công ty bạn. Vì BTCPay Server là FOSS, quản trị viên máy chủ có thể white label phần mềm và thay đổi giao diện để phù hợp với doanh nghiệp của họ.

![image](assets/en/84.webp)

### Bảo Trì

Là một quản trị viên máy chủ, người dùng của bạn mong đợi bạn chăm sóc tốt máy chủ. Trong tab Bảo Trì của BTCPay Server, quản trị viên có thể thực hiện một số công việc bảo trì cơ bản. Thiết lập tên miền cho thể hiện BTCPay Server, Khởi động lại hoặc dọn dẹp máy chủ. Có lẽ quan trọng nhất, chạy cập nhật.

BTCPay Server là một dự án mã nguồn mở và thường xuyên cập nhật. Mỗi bản phát hành mới được thông báo qua Thông báo BTCPay Server của bạn hoặc trên các Kênh chính thức mà BTCPay Server giao tiếp qua.

![image](assets/en/85.webp)

#### Tên miền

Sau khi BTCPay Server được thiết lập, một quản trị viên có thể muốn thay đổi khỏi tên miền gốc của mình. Trong tab Bảo Trì, quản trị viên có thể thay đổi tên miền. Sau khi nhấp xác nhận và thiết lập các bản ghi DNS đúng trên tên miền, BTCPay Server cập nhật và khởi động lại để quay trở lại tên miền mới.

![image](assets/en/86.webp)

#### Khởi động lại

Khởi động lại BTCPay Server và các dịch vụ liên quan.

![image](assets/en/87.webp)

#### Dọn dẹp

BTCPay Server hoạt động với các thành phần Docker; với các bản cập nhật, có thể có những tệp ảnh Docker, tệp tạm, v.v. còn sót lại. Quản trị viên máy chủ có thể dọn dẹp những thứ này và thu hồi không gian trên môi trường của họ bằng cách chạy script Clean.
![image](assets/en/88.webp)

#### Cập nhật

Có lẽ là tùy chọn quan trọng nhất trong tab Bảo trì. BTCPay Server được xây dựng bởi cộng đồng, và do đó, chu kỳ cập nhật của nó thường xuyên hơn so với hầu hết các sản phẩm phần mềm khác. Khi BTCPay Server có một bản phát hành mới, quản trị viên sẽ được thông báo trong trung tâm thông báo của họ. Bằng cách nhấp vào nút cập nhật, BTCPay Server sẽ kiểm tra GitHub để tìm bản phát hành mới nhất, cập nhật Máy chủ và khởi động lại. Trước khi cập nhật, quản trị viên máy chủ luôn được khuyến khích đọc các ghi chú phát hành được phân phối qua các kênh chính thức của BTCPay Server.

![image](assets/en/89.webp)

### Logs

Đối mặt với một vấn đề không bao giờ là vui vẻ. Tài liệu này giải thích quy trình và các bước phổ biến nhất để xác định vấn đề của bạn một cách hiệu quả và tự giải quyết nó hoặc nhờ sự giúp đỡ của cộng đồng.

Việc xác định vấn đề là rất quan trọng.

#### Tái tạo vấn đề

Đầu tiên và quan trọng nhất, hãy cố gắng xác định khi nào vấn đề xảy ra. Hãy cố gắng tái tạo vấn đề. Cố gắng cập nhật và khởi động lại Máy chủ của bạn để xác nhận rằng bạn có thể tái tạo vấn đề của mình. Nếu nó mô tả vấn đề của bạn tốt hơn, hãy chụp một ảnh màn hình.

##### Cập nhật máy chủ

Kiểm tra phiên bản BTCPay Server của bạn nếu nó cũ hơn nhiều so với [phiên bản mới nhất](https://github.com/btcpayserver/btcpayserver/releases) của BTCPay Server. Cập nhật Máy chủ của bạn có thể giải quyết vấn đề.

##### Khởi động lại máy chủ

Khởi động lại Máy chủ của bạn là một cách dễ dàng để giải quyết nhiều vấn đề phổ biến nhất của BTCPay Server. Bạn có thể cần SSH vào Máy chủ của bạn để khởi động lại nó.

##### Khởi động lại một dịch vụ

Đối với một số vấn đề, bạn chỉ cần khởi động lại một dịch vụ cụ thể trong triển khai BTCPay Server của mình. Chẳng hạn như khởi động lại container lets encrypt để gia hạn chứng chỉ SSL.

```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```

Sử dụng docker ps để tìm tên của một dịch vụ khác mà bạn muốn khởi động lại.

#### Xem qua logs

Logs có thể cung cấp một phần thông tin quan trọng. Trong các đoạn văn sau, chúng tôi sẽ mô tả cách lấy thông tin log cho các phần khác nhau của BTCPay.

##### BTCPay Logs

Từ phiên bản v1.0.3.8, bạn có thể dễ dàng truy cập logs của BTCPay Server từ giao diện người dùng. Nếu bạn là quản trị viên máy chủ, hãy vào Server Settings > Logs và mở tệp logs. Nếu bạn không biết lỗi cụ thể trong logs có nghĩa là gì, hãy đề cập đến nó khi khắc phục sự cố.

Nếu bạn muốn xem logs chi tiết hơn và đang sử dụng triển khai Docker, bạn có thể xem logs của các container Docker cụ thể bằng dòng lệnh. Xem [hướng dẫn này để ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) vào một instance của BTCPay đang chạy trên VPS.

Trang tiếp theo, một danh sách tổng quát các tên container được sử dụng cho BTCPay Server.

Chạy các lệnh dưới đây để in logs theo tên container. Thay thế tên container để xem logs của các container khác.

```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```

| Logs cho     | Tên Container                     |
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

Có một số cách để truy cập vào nhật ký LND của bạn khi sử dụng Docker. Đầu tiên, đăng nhập với tư cách là root:

```bash
sudo su -
Di chuyển đến thư mục chính xác:
cd btcpayserver-docker
# Tìm tên container:
docker ps
In nhật ký bằng tên container:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```

Ngoài ra, bạn có thể nhanh chóng in nhật ký bằng cách sử dụng ID container (chỉ cần các ký tự ID duy nhất đầu tiên, như hai ký tự bên trái nhất):

```bash
docker logs 'thêm ID container của bạn'
```

Nếu vì lý do nào đó bạn cần thêm nhật ký

```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/_data/logs/bitcoin/mainnet/
ls
```

Bạn sẽ thấy một số tệp như

```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```

Để truy cập nhật ký không nén của những nhật ký này, hãy sử dụng `cat lnd.log` hoặc nếu bạn muốn một cái khác, sử dụng `cat lnd.log.15`.

Để truy cập nhật ký nén trong `.gzip`, sử dụng `gzip -d lnd.log.16.gz` (trong trường hợp này chúng ta đang truy cập `lnd.log.16.gz`). Điều này sẽ tạo ra một tệp mới, bạn có thể làm `cat lnd.log.16`. Trong trường hợp trên không hoạt động, bạn có thể cần cài đặt gzip trước với `sudo apt-get install gzip`.

###### Lightning Network c-lightning - Docker

```bash
sudo su -
docker ps
# Tìm ID container c-lightning.
docker logs 'thêm ID container của bạn ở đây'
```

hoặc sử dụng cách này

```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```

Bạn cũng có thể lấy thông tin nhật ký với lệnh cli c-lightning.

```bash
bitcoin-lightning-cli.sh getlog
```

#### Nhật Ký Node Bitcoin

Ngoài việc [xem nhật ký](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) của container Bitcoind của bạn, bạn cũng có thể sử dụng bất kỳ [lệnh bitcoin-cli](https://developer.bitcoin.org/reference/rpc/index.html) nào

[(mở cửa sổ mới)](https://developer.bitcoin.org/reference/rpc/index.html) để lấy thông tin từ node bitcoin của bạn. BTCPay bao gồm một script để cho phép bạn giao tiếp với node Bitcoin của mình một cách dễ dàng.

Trong thư mục btcpayserver-docker, lấy thông tin blockchain sử dụng node của bạn:

```bash
bitcoin-cli.sh getblockchaininfo
```

BTCPay Server có một hệ thống tệp tin địa phương và tải lên các tài sản của Cửa hàng (sản phẩm), Logo, và thương hiệu trực tiếp lên Máy chủ. Hệ thống tệp tin của Máy chủ chỉ có thể truy cập bởi Quản trị viên Máy chủ; chủ sở hữu cửa hàng có thể tải lên logo/thương hiệu của họ ở cấp độ cửa hàng.
Khi Quản trị viên Máy chủ đang ở trong tab Lưu trữ Tệp, có thể trực tiếp tải lên Máy chủ của bạn hoặc thay đổi nhà cung cấp lưu trữ tệp tin sang Hệ thống tệp tin Địa phương hoặc Azure Blob Storage.

![hình ảnh](assets/en/90.webp)

![hình ảnh](assets/en/91.webp)

### Tóm Tắt Kỹ Năng

Trong phần này, bạn đã học được những điều sau:

- Sự khác biệt giữa Cài đặt Cửa hàng và Cài đặt Máy chủ, đặc biệt là liên quan đến Người dùng, Vai trò, và Email
- Thiết lập các chính sách chung cho Máy chủ về việc sử dụng và tạo ví Lightning hoặc Bitcoin hot wallet, đăng ký người dùng mới, và thông báo email.
- Cách thêm các chủ đề tùy chỉnh (thay vì chỉ có tùy chọn sáng/tối đơn giản được cung cấp) cũng như tạo logo tùy chỉnh
- Thực hiện các nhiệm vụ bảo trì máy chủ đơn giản qua GUI được cung cấp
- Khắc phục sự cố, bao gồm lấy chi tiết cho bất kỳ container Docker nào hoặc node của bạn
- Quản lý lưu trữ tệp

### Đánh Giá Kiến Thức

#### Đánh Giá Khái Niệm

Sự khác biệt trong Vai trò được gán qua Cài đặt Máy chủ so với Cài đặt Cửa hàng là gì, và mô tả một sử dụng tiềm năng cho cái này hơn cái kia?

#### Đánh Giá Thực Hành

Mô tả một số trường hợp sử dụng có thể được kích hoạt trong tab Chính sách.

#### Đánh Giá Thực Hành

Mô tả một số hành động mà một quản trị viên có thể thường xuyên thực hiện trong tab Bảo trì.

## BTCPay Server - Thanh Toán

<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>

Hóa đơn là một tài liệu mà người bán phát hành cho người mua để thu tiền.

Trong BTCPay Server, một hóa đơn đại diện cho một tài liệu phải được thanh toán trong một khoảng thời gian xác định với tỷ giá cố định. Hóa đơn có thời hạn vì chúng khóa tỷ giá trong một khung thời gian xác định để bảo vệ người nhận khỏi sự biến động giá.

Cốt lõi của BTCPay Server là khả năng hoạt động như một hệ thống quản lý hóa đơn Bitcoin. Hóa đơn là một công cụ thiết yếu để theo dõi và quản lý việc thanh toán đã nhận.

Trừ khi bạn sử dụng [Ví](https://docs.btcpayserver.org/Wallet/) tích hợp để nhận thanh toán một cách thủ công, tất cả các thanh toán trong một cửa hàng sẽ được hiển thị trên trang Hóa đơn. Trang này sắp xếp tổng hợp các thanh toán theo ngày và là một phần trung tâm cho việc quản lý hóa đơn và khắc phục sự cố thanh toán.

![hình ảnh](assets/en/92.webp)

### Tổng Quan

#### Trạng thái hóa đơn

Bảng dưới đây liệt kê và mô tả các trạng thái hóa đơn tiêu chuẩn trong BTCPay và đề xuất các hành động phổ biến. Các hành động chỉ là khuyến nghị. Quyết định hành động tốt nhất cho trường hợp sử dụng và kinh doanh của họ là do người dùng quyết định.

| Trạng thái hóa đơn                    | Mô tả                                                                                                                     | Hành động                                                                                                                                             |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Mới                                   | Chưa thanh toán, bộ đếm thời gian hóa đơn vẫn chưa hết hạn                                                                | Không có                                                                                                                                              |
| Mới (đã thanh toán một phần)          | Đã thanh toán, không đủ, bộ đếm thời gian hóa đơn vẫn chưa hết hạn                                                        | Không có                                                                                                                                              |
| Hết hạn                               | Chưa thanh toán, bộ đếm thời gian hóa đơn đã hết hạn                                                                      | Không có                                                                                                                                              |
| Hết hạn (đã thanh toán một phần) \*\* | Đã thanh toán, không đủ số tiền, và đã hết hạn                                                                            | Liên hệ với người mua để sắp xếp hoàn tiền hoặc yêu cầu họ thanh toán số tiền còn thiếu. Tùy chọn đánh dấu hóa đơn là đã giải quyết hoặc không hợp lệ |
| Hết hạn (đã thanh toán muộn)          | Đã thanh toán, đủ số tiền, sau khi bộ đếm thời gian hóa đơn đã hết hạn                                                    | Liên hệ với người mua để sắp xếp hoàn tiền hoặc xử lý đơn hàng nếu việc xác nhận muộn được chấp nhận.                                                 |
| Đã Thanh Toán (trả quá số tiền)       | Trả nhiều hơn số tiền trên hóa đơn, đã thanh toán, nhận đủ số lượng xác nhận cần thiết                                    | Liên hệ với người mua để sắp xếp hoàn trả số tiền thừa, hoặc tùy chọn chờ người mua liên hệ với bạn                                                   |
| Đang Xử Lý                            | Đã trả đủ tiền, nhưng chưa nhận đủ số lượng xác nhận cần thiết theo cài đặt của cửa hàng                                  | Liên hệ với người mua để sắp xếp hoàn trả số tiền thừa, hoặc tùy chọn chờ người mua liên hệ với bạn                                                   |
| Đang Xử Lý (trả quá số tiền)          | Trả nhiều hơn số tiền trên hóa đơn, chưa nhận đủ số lượng xác nhận cần thiết                                              | Chờ được thanh toán sau đó liên hệ với người mua để sắp xếp hoàn trả số tiền thừa, hoặc tùy chọn chờ người mua liên hệ với bạn                        |
| Đã Thanh Toán                         | Đã trả đủ tiền, nhận đủ số lượng xác nhận cần thiết trong cửa hàng                                                        | Hoàn thành đơn hàng                                                                                                                                   |
| Đã Thanh Toán (được đánh dấu)         | Trạng thái đã được thay đổi thủ công thành đã thanh toán từ trạng thái đang xử lý hoặc không hợp lệ                       | Quản trị viên cửa hàng đã đánh dấu thanh toán là đã được thanh toán                                                                                   |
| Không Hợp Lệ\*                        | Đã trả tiền, nhưng không nhận đủ số lượng xác nhận cần thiết trong thời gian quy định của cài đặt cửa hàng                | Kiểm tra giao dịch trên trình duyệt blockchain, nếu nó nhận đủ xác nhận, đánh dấu là đã thanh toán                                                    |
| Không Hợp Lệ (được đánh dấu)          | Trạng thái đã được thay đổi thủ công thành không hợp lệ từ trạng thái đã thanh toán hoặc hết hạn                          | Quản trị viên cửa hàng đã đánh dấu thanh toán là không hợp lệ                                                                                         |
| Không Hợp Lệ (trả quá số tiền)        | Trả nhiều hơn số tiền trên hóa đơn, nhưng không nhận đủ số lượng xác nhận cần thiết trong thời gian quy định của cửa hàng | Kiểm tra giao dịch trên trình duyệt blockchain, nếu nó nhận đủ xác nhận, đánh dấu là đã thanh toán                                                    |

#### Chi tiết hóa đơn

Trang chi tiết hóa đơn chứa tất cả thông tin liên quan đến một hóa đơn.

Thông tin hóa đơn được tạo tự động dựa trên trạng thái hóa đơn, tỷ giá hối đoái, v.v. Thông tin sản phẩm được tạo tự động nếu hóa đơn được tạo với thông tin sản phẩm, như trong ứng dụng Point of Sale.

#### Lọc hóa đơn

Hóa đơn có thể được lọc qua các bộ lọc nhanh nằm cạnh nút tìm kiếm hoặc các bộ lọc nâng cao, có thể được chuyển đổi bằng cách nhấp vào liên kết (Trợ giúp) ở trên cùng. Người dùng có thể lọc hóa đơn theo cửa hàng, mã đơn hàng, mã mặt hàng, trạng thái, hoặc ngày.

#### Xuất hóa đơn

Hóa đơn BTCPay Server có thể được xuất dưới dạng CSV hoặc JSON. Để biết thêm thông tin về xuất hóa đơn và kế toán.

#### Hoàn trả hóa đơn

Nếu, vì bất kỳ lý do gì, bạn muốn thực hiện hoàn trả, bạn có thể dễ dàng tạo một hoàn trả từ giao diện xem hóa đơn.

#### Lưu trữ hóa đơn

Do tính năng không sử dụng lại địa chỉ của BTCPay Server, thường thấy nhiều hóa đơn hết hạn trên trang hóa đơn của cửa hàng. Để ẩn chúng khỏi giao diện của bạn, chọn chúng trong danh sách và đánh dấu là đã lưu trữ. Hóa đơn đã được đánh dấu là đã lưu trữ không bị xóa. Thanh toán cho một hóa đơn đã lưu trữ vẫn sẽ được BTCPay Server phát hiện (trạng thái trả muộn). Bạn có thể xem các hóa đơn đã lưu trữ của cửa hàng bất cứ lúc nào bằng cách chọn hóa đơn đã lưu trữ từ bộ lọc tìm kiếm.

#### Tiền tệ Mặc Định

Tiền tệ mặc định của cửa hàng, được thiết lập tại trình hướng dẫn tạo cửa hàng

#### Cho phép bất kỳ ai tạo hóa đơn

Bạn nên kích hoạt tùy chọn này nếu bạn muốn cho phép bên ngoài tạo hóa đơn trong cửa hàng của bạn. Tùy chọn này chỉ hữu ích nếu bạn đang sử dụng nút thanh toán hoặc nếu bạn đang phát hành hóa đơn qua API hoặc website HTML của bên thứ ba. Ứng dụng PoS được ủy quyền trước và không cần kích hoạt này cho một khách truy cập ngẫu nhiên mở cửa hàng PoS của bạn và tạo hóa đơn.

#### Thêm phí bổ sung (phí mạng) vào hóa đơn

- Chỉ khi khách hàng thực hiện nhiều hơn một lần thanh toán cho hóa đơn
- Trên mỗi lần thanh toán
- Không bao giờ thêm phí mạng

#### Hóa đơn sẽ hết hạn nếu số tiền đầy đủ không được thanh toán sau .. Phút.

Bộ đếm thời gian của hóa đơn được thiết lập mặc định là 15 phút. Bộ đếm thời gian là một cơ chế bảo vệ chống lại sự biến động giá cả vì nó khóa số lượng tiền điện tử theo tỷ giá hối đoái crypto sang fiat. Nếu khách hàng không thanh toán hóa đơn trong khoảng thời gian đã định, hóa đơn được coi là đã hết hạn. Hóa đơn được coi là "đã thanh toán" ngay khi giao dịch hiển thị trên blockchain (0-xác nhận) nhưng được coi là "hoàn thành" khi đạt được số lượng xác nhận mà người bán hàng đã định (thường là 1-6). Bộ đếm thời gian có thể tùy chỉnh.

#### Xem xét hóa đơn đã thanh toán ngay cả khi số tiền thanh toán ít hơn ..% so với dự kiến.

Trong trường hợp khách hàng sử dụng ví giao dịch để trực tiếp thanh toán cho một hóa đơn, giao dịch sẽ mất một lượng phí nhỏ. Điều này có nghĩa là hóa đơn đó không được coi là hoàn thành hoàn toàn. Hóa đơn nhận được trạng thái "đã thanh toán một phần". Nếu một người bán hàng muốn chấp nhận hóa đơn thanh toán thiếu, bạn có thể thiết lập tỷ lệ phần trăm ở đây.

### Yêu cầu

Yêu cầu Thanh toán là một tính năng cho phép chủ sở hữu cửa hàng BTCPay tạo hóa đơn lâu dài. Quỹ được thanh toán cho một yêu cầu thanh toán sử dụng tỷ giá hối đoái tại thời điểm thanh toán. Điều này cho phép người dùng thực hiện thanh toán theo sự tiện lợi của họ mà không cần thương lượng hoặc xác minh tỷ giá hối đoái với chủ cửa hàng tại thời điểm thanh toán.

Người dùng có thể thanh toán các yêu cầu bằng cách thanh toán một phần. Yêu cầu thanh toán sẽ còn hiệu lực cho đến khi nó được thanh toán đầy đủ hoặc nếu chủ cửa hàng yêu cầu một thời gian hết hạn. Địa chỉ không bao giờ được tái sử dụng. Một địa chỉ mới được tạo ra mỗi lần người dùng nhấp vào thanh toán để tạo hóa đơn cho yêu cầu thanh toán.

Chủ cửa hàng có thể in yêu cầu thanh toán (hoặc xuất dữ liệu hóa đơn) để lưu trữ và kế toán. BTCPay tự động gắn nhãn hóa đơn là Yêu cầu Thanh toán trong danh sách hóa đơn của cửa hàng bạn.

#### Tùy chỉnh Yêu cầu Thanh toán của Bạn

- Số Tiền Hóa Đơn - Thiết lập Số Tiền Thanh toán Được Yêu cầu
- Đơn vị Tiền tệ - Hiển thị Số Tiền Được Yêu cầu bằng Fiat hoặc Tiền điện tử
- Số Lượng Thanh toán - Chỉ cho phép thanh toán một lần hoặc thanh toán một phần
- Thời Gian Hết Hạn - Cho phép thanh toán cho đến một ngày hoặc không hết hạn
- Mô Tả - Trình Soạn Thảo Văn Bản, Bảng Dữ Liệu, Nhúng Ảnh & Video
- Hình Thức - Màu sắc và Kiểu dáng với Chủ đề CSS

![image](assets/en/93.webp)

#### Tạo Yêu cầu Thanh toán

Trong menu bên trái, đi đến Yêu cầu Thanh toán và nhấp vào "Tạo Yêu cầu Thanh toán".

![image](assets/en/94.webp)

Cung cấp Tên Yêu cầu, Số Tiền, Đơn vị Tiền tệ Hiển thị, Cửa hàng Liên kết, Thời Gian Hết Hạn & Mô Tả (Tùy chọn)

Chọn tùy chọn Cho phép người thanh toán tạo hóa đơn theo đơn vị tiền tệ của họ nếu bạn muốn cho phép thanh toán một phần.

Nhấp vào Lưu & Xem để xem lại yêu cầu thanh toán của bạn.

BTCPay tạo một URL cho yêu cầu thanh toán. Chia sẻ URL này để xem yêu cầu thanh toán của bạn. Cần nhiều yêu cầu giống nhau? Bạn có thể nhân bản yêu cầu thanh toán sử dụng tùy chọn Clone trong menu chính.

![image](assets/en/95.webp)

**CẢNH BÁO**

Yêu cầu thanh toán phụ thuộc vào cửa hàng, nghĩa là mỗi yêu cầu thanh toán được liên kết với một cửa hàng khi được tạo. Hãy chắc chắn rằng bạn có một ví được kết nối với cửa hàng mà yêu cầu thanh toán thuộc về.

#### Yêu cầu Đã Thanh toán

Người thanh toán và người yêu cầu có thể xem trạng thái của yêu cầu thanh toán sau khi gửi thanh toán. Trạng thái sẽ hiển thị là Đã Giải Quyết nếu thanh toán đã được nhận đầy đủ. Nếu chỉ có thanh toán một phần, Số Tiền Còn Nợ sẽ hiển thị số dư còn lại.

![image](assets/en/96.webp)

#### Tùy chỉnh Yêu cầu Thanh toán

Nội dung mô tả có thể được chỉnh sửa sử dụng trình soạn thảo văn bản của yêu cầu thanh toán. Cả hai tùy chọn đều có sẵn nếu bạn muốn sử dụng thêm chủ đề màu sắc hoặc tùy chỉnh CSS.
Người dùng không chuyên kỹ thuật có thể sử dụng [bootstrap theme](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Việc tùy chỉnh thêm có thể được thực hiện bằng cách cung cấp thêm mã CSS, như được hiển thị dưới đây.

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

### Thanh toán kéo

Truyền thống, người nhận chia sẻ địa chỉ Bitcoin của họ để thực hiện thanh toán Bitcoin, và sau đó người gửi chuyển tiền vào địa chỉ này. Hệ thống như vậy được gọi là Thanh toán đẩy, vì người gửi khởi xướng thanh toán trong khi người nhận có thể không có mặt, đẩy thanh toán đến người nhận.

Tuy nhiên, nếu đảo ngược vai trò thì sao?

Nếu thay vì người gửi đẩy thanh toán, người gửi cho phép người nhận kéo thanh toán vào thời điểm người nhận thấy phù hợp? Đây là khái niệm của Thanh toán kéo. Điều này cho phép nhiều ứng dụng mới, như:

- Dịch vụ đăng ký (nơi người đăng ký cho phép dịch vụ kéo tiền mỗi x khoảng thời gian)
- Hoàn tiền (nơi người bán cho phép khách hàng kéo tiền hoàn lại vào ví của họ khi họ thấy phù hợp)
- Thanh toán dựa trên thời gian cho freelancer (nơi người thuê cho phép freelancer kéo tiền vào ví của họ khi thời gian được báo cáo)
- Tài trợ (nơi người tài trợ cho phép người nhận kéo tiền hàng tháng để tiếp tục hỗ trợ công việc của họ)
- Bán hàng tự động (nơi khách hàng của một sàn giao dịch cho phép sàn giao dịch kéo tiền từ ví của họ để bán hàng tự động hàng tháng)
- Hệ thống rút tiền dựa trên số dư (nơi một dịch vụ có lượng giao dịch cao cho phép người dùng yêu cầu rút tiền từ số dư của họ, dịch vụ sau đó có thể dễ dàng tổ chức tất cả các khoản thanh toán cho nhiều người dùng vào các khoảng thời gian cố định)

### Thanh toán

Chức năng thanh toán được tích hợp vào [Thanh toán kéo](https://docs.btcpayserver.org/PullPayments/). Tính năng này cho phép bạn tạo thanh toán trong BTCPay của mình. Tính năng này cho phép bạn xử lý thanh toán kéo (hoàn tiền, thanh toán lương, hoặc rút tiền).

#### Ví dụ 1: Hoàn tiền

Hãy bắt đầu với ví dụ về hoàn tiền. Khách hàng đã mua một mặt hàng trong cửa hàng của bạn nhưng không may phải trả lại mặt hàng. Họ muốn được hoàn tiền. Trong BTCPay, bạn có thể tạo một [Hoàn tiền](https://docs.btcpayserver.org/Refund/) và cung cấp cho khách hàng liên kết để yêu cầu tiền của họ. Khi khách hàng đã cung cấp địa chỉ của họ và yêu cầu tiền, nó sẽ được hiển thị trong Thanh toán.

Trạng thái đầu tiên là Đang chờ Phê duyệt. Nhân viên cửa hàng có thể kiểm tra nếu có nhiều khoản đang chờ, và sau khi lựa chọn, bạn sử dụng nút Hành động.

Tùy chọn trên nút hành động

- Phê duyệt các khoản thanh toán đã chọn
- Phê duyệt & gửi các khoản thanh toán đã chọn
- Hủy các khoản thanh toán đã chọn

Bước tiếp theo là Phê duyệt & gửi các khoản thanh toán đã chọn vì chúng ta muốn hoàn tiền cho khách hàng. Kiểm tra Địa chỉ của Khách hàng, hiển thị số tiền và nếu chúng ta muốn phí được trừ từ số tiền hoàn lại hay không. Sau khi bạn đã kiểm tra, chỉ còn lại việc ký giao dịch.
Khách hàng giờ đây được cập nhật trên trang Yêu cầu Thanh toán. Anh ta có thể theo dõi giao dịch vì được cung cấp một liên kết đến trình duyệt khối và giao dịch của mình. Một khi giao dịch được xác nhận và trạng thái thay đổi thành Hoàn thành.

#### Ví dụ 2: Lương

Bây giờ, chúng ta hãy nói về việc thanh toán lương, vì điều này được thực hiện từ bên trong cửa hàng và không theo yêu cầu của Khách hàng. Cơ bản là giống nhau; nó sử dụng các khoản thanh toán kéo. Nhưng thay vì tạo một khoản hoàn tiền, chúng tôi sẽ tạo một [Khoản Thanh Toán Kéo](https://docs.btcpayserver.org/PullPayments/).

Đi đến tab Khoản Thanh Toán Kéo trong máy chủ BTCPay của bạn. Ở góc trên bên phải, nhấp vào nút Tạo Khoản Thanh Toán Kéo.

Bây giờ chúng ta đang trong quá trình tạo Khoản Thanh Toán, đặt tên cho nó và số tiền mong muốn trong đơn vị tiền tệ mong muốn, điền vào Mô tả, để nhân viên biết nó là về cái gì. Phần tiếp theo tương tự như hoàn tiền. Nhân viên điền vào địa chỉ Đích và số tiền anh ta muốn yêu cầu từ Khoản Thanh Toán này. Anh ta có thể quyết định làm 2 yêu cầu riêng biệt, đến các địa chỉ khác nhau, hoặc thậm chí yêu cầu một phần qua lightning.

Nếu có nhiều Khoản Thanh Toán đang chờ, bạn có thể gộp chúng lại để được ký và gửi đi. Một khi đã ký, các khoản thanh toán chuyển sang tab Đang tiến hành và hiển thị Giao dịch. Khi được mạng lưới chấp nhận, khoản thanh toán chuyển sang tab Hoàn thành. Tab Hoàn thành chỉ mang mục đích lịch sử. Nó giữ các Khoản Thanh Toán đã xử lý và giao dịch thuộc về nó.

### Khoản Thanh Toán Kéo

#### Khái niệm

Khi người gửi cấu hình một Khoản Thanh Toán Kéo, họ có thể cấu hình một số thuộc tính:

- Tên Yêu cầu Thanh Toán Kéo
- Một số tiền giới hạn
- Đơn vị (như BTC, SAT, USD)
- Phương thức Thanh toán
  - BTC Trên chuỗi
  - BTC Ngoài chuỗi
- Mô tả
- CSS Tùy chỉnh
- Ngày kết thúc (tùy chọn cho Lightning Network BOLT11)

Sau đó, người gửi có thể chia sẻ khoản thanh toán kéo bằng một liên kết với người nhận, cho phép người nhận tạo một khoản thanh toán. Người nhận sẽ chọn khoản thanh toán của mình:

- Phương thức thanh toán nào để sử dụng
- Gửi tiền đến đâu

Một khi một khoản thanh toán được tạo, nó sẽ được tính vào giới hạn của khoản thanh toán kéo cho kỳ hiện tại. Người gửi sau đó sẽ phê duyệt khoản thanh toán bằng cách thiết lập tỷ lệ mà khoản thanh toán sẽ được gửi và tiến hành thanh toán.

Đối với người gửi, chúng tôi cung cấp một cách dễ dàng để gộp thanh toán của nhiều khoản thanh toán từ [Ví Nội Bộ BTCPay](https://docs.btcpayserver.org/Wallet/).

#### Greenfield API

Máy chủ BTCPay cung cấp một API đầy đủ cho cả người gửi và người nhận được tài liệu hóa trong trang `/docs` của phiên bản của bạn. (hoặc trên trang web tài liệu https://docs.btcpayserver.org)

Vì API của chúng tôi tiết lộ toàn bộ khả năng của khoản thanh toán kéo, người gửi có thể tự động hóa các khoản thanh toán theo nhu cầu của mình.

### Tóm tắt Kỹ năng

Trong phần này, bạn đã học được những điều sau:

- Hiểu sâu về các trạng thái hóa đơn của Máy chủ BTCPay cũng như các hành động có thể thực hiện trên chúng
- Tùy chỉnh và quản lý các cơ chế hóa đơn kéo dài cuộc sống được biết đến là Yêu cầu.
- Các khả năng thanh toán linh hoạt bổ sung mở ra với tính năng Khoản Thanh Toán Kéo độc đáo của Máy chủ BTCPay, đặc biệt là cách xử lý hoàn tiền và thanh toán lương.

### Đánh giá Kiến thức

#### Đánh giá Khái niệm

Những điểm khác biệt nào giữa hóa đơn và yêu cầu thanh toán, và lý do tốt nào để sử dụng cái sau?

#### Đánh giá Khái niệm

Khoản thanh toán kéo mở rộng như thế nào so với những gì thường có thể được thực hiện trên chuỗi? Mô tả một số trường hợp sử dụng mà chúng kích hoạt.

## Plugin mặc định của máy chủ BTCPay

<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>

### Plugin và Ứng dụng Mặc định

Máy chủ BTCPay đi kèm với một bộ Plugin (Ứng dụng) tiêu chuẩn có thể biến Máy chủ BTCPay thành một cổng thanh toán thương mại điện tử. Với sự bổ sung của Điểm bán hàng, Nền tảng gây quỹ, và nút Thanh toán dễ dàng, Máy chủ BTCPay trở thành giải pháp dễ dàng triển khai.

### Điểm Bán Hàng

Một trong những Plugin tiêu chuẩn của Máy chủ BTCPay là Điểm bán hàng (PoS). Với plugin PoS, chủ cửa hàng có thể tạo một Webshop trực tiếp từ Máy chủ BTCPay, chủ cửa hàng không cần giải pháp thương mại điện tử của bên thứ ba để vận hành Webshop. Ứng dụng PoS dựa trên web cho phép người dùng với cửa hàng truyền thống dễ dàng chấp nhận Bitcoin, không qua phí hoặc bên thứ ba, trực tiếp vào ví của họ. PoS có thể được hiển thị dễ dàng trên máy tính bảng hoặc các thiết bị khác hỗ trợ duyệt web. Người dùng có thể dễ dàng tạo một lối tắt màn hình chính để truy cập ứng dụng web nhanh chóng.

#### Cách tạo mới Điểm Bán Hàng

Máy chủ BTCPay cho phép chủ cửa hàng tạo một Điểm Bán Hàng trong nhiều bố cục nhanh chóng. Máy chủ BTCPay nhận ra rằng không phải mọi cửa hàng đều là thương mại điện tử, và không phải mọi cửa hàng là quán bar hay nhà hàng, và nó đi kèm với nhiều thiết lập tiêu chuẩn cho PoS của bạn.

Khi chủ cửa hàng nhấp vào "Điểm Bán Hàng" trong thanh menu bên trái của mình, Máy chủ BTCPay sẽ yêu cầu một tên; tên này sẽ được hiển thị trong thanh menu bên trái. Nhấp Tạo để tạo PoS.

![image](assets/en/97.webp)

#### Cập nhật Điểm Bán Hàng mới tạo

Sau khi tạo một PoS mới, màn hình tiếp theo sẽ là để cập nhật Điểm Bán Hàng của bạn và thêm các mặt hàng cho cửa hàng của bạn.

##### Tên ứng dụng

Tên được đặt ở đây cho Điểm Bán Hàng của bạn sẽ được hiển thị trong menu chính của Máy chủ BTCPay.

##### Tiêu đề hiển thị

Công chúng sẽ thấy tiêu đề công khai hoặc tên khi ghé thăm cửa hàng của bạn. Máy chủ BTCPay theo tiêu chuẩn đặt tên cửa hàng của bạn là “Tiệm trà” Thay thế điều này bằng tên cửa hàng của bạn.

![image](assets/en/98.webp)

#### Chọn Kiểu Điểm Bán Hàng

Máy chủ BTCPay có khả năng hiển thị Điểm Bán Hàng của mình theo nhiều cách.

- Danh sách sản phẩm
  - Một giao diện cửa hàng nơi khách hàng chỉ có thể mua 1 sản phẩm mỗi lần.
- Danh sách sản phẩm với giỏ hàng.
  - Một giao diện cửa hàng nơi khách hàng có thể mua nhiều mặt hàng cùng một lúc và có được tổng quan giỏ hàng ở bên phải màn hình của họ.
- Chỉ bàn phím
  - Không có danh sách sản phẩm, chỉ có bàn phím cho việc lập hóa đơn trực tiếp.
- Hiển thị in (Danh sách sản phẩm có thể in với QR)
  - Nếu bạn không thể luôn hiển thị danh sách sản phẩm của mình một cách kỹ thuật số, bạn cần một giải pháp "ngoại tuyến" cho sản phẩm; Máy chủ BTCPay có chức năng hiển thị in để hoạt động như một cửa hàng Ngoại tuyến.

![image](assets/en/99.webp)

#### Kiểu Điểm Bán Hàng - Danh sách sản phẩm

![image](assets/en/100.webp)

#### Kiểu Điểm Bán Hàng - Danh sách sản phẩm + Giỏ hàng

![image](assets/en/101.webp)

#### Kiểu Điểm Bán Hàng - Chỉ bàn phím

![image](assets/en/102.webp)

#### Kiểu Điểm Bán Hàng - Hiển thị in

![image](assets/en/103.webp)

#### Tiền tệ

Chủ cửa hàng có thể đặt một loại tiền tệ khác cho Điểm Bán Hàng của mình so với loại tiền tệ mặc định đã được thiết lập. Loại tiền tệ mặc định của cửa hàng sẽ tự động điền vào trường này.

#### Mô tả

Hãy kể cho thế giới biết về cửa hàng của bạn; bạn đang bán gì và với giá bao nhiêu? Mọi thứ giải thích về cửa hàng của bạn đều được viết ở đây.

#### Sản Phẩm

Khi một Điểm Bán Hàng được tạo ra, một máy chủ BTCPay chuẩn sẽ thêm một vài mặt hàng vào cửa hàng để tham khảo. Nhấn vào nút Chỉnh sửa trên bất kỳ mặt hàng chuẩn nào để hiểu rõ hơn về từng tùy chọn có thể có cho một mặt hàng.

Việc tạo một sản phẩm mới trong cửa hàng của bạn bao gồm các trường sau;

- Tiêu đề
- Giá (cố định, tối thiểu, hoặc tùy chỉnh)
- URL Hình ảnh
- Mô tả
- Tồn kho
- ID
- Văn bản Nút Mua.
- Bật/Tắt

Sau khi chủ cửa hàng đã điền tất cả các trường sản phẩm mới, nhấn vào lưu, và bạn sẽ nhận thấy rằng mục Sản Phẩm trong Điểm Bán Hàng bây giờ đang được điền vào. Luôn đảm bảo lưu ở góc trên bên phải của màn hình để tránh việc chủ cửa hàng có thể mất tiến độ khi thêm sản phẩm.

Chủ cửa hàng cũng có thể sử dụng "Trình Chỉnh sửa Thô" để cấu hình sản phẩm của họ. Trình chỉnh sửa thô yêu cầu một hiểu biết cơ bản về cấu trúc JSON.

#### Thanh Toán

Máy chủ BTCPay cho phép tùy chỉnh thanh toán cụ thể cho PoS nhỏ. Chủ cửa hàng có thể thiết lập văn bản "Mua với x" hoặc yêu cầu dữ liệu khách hàng cụ thể bằng cách thêm vào biểu mẫu.

#### Tiền Bo

Không phải tất cả các cửa hàng đều cần tùy chọn cho Tiền Bo trên doanh số bán hàng của họ. Chủ cửa hàng có thể bật hoặc tắt tùy chọn này tùy theo nhu cầu của cửa hàng. Nếu cửa hàng sử dụng tiền bo được bật, chủ cửa hàng có thể thiết lập văn bản trong trường cho tiền bo mà họ thích. Tiền bo trên máy chủ BTCPay hoạt động dựa trên một số tiền phần trăm. Chủ cửa hàng có thể thêm nhiều phần trăm với sự phân cách bằng dấu phẩy.

#### Giảm Giá

Là một chủ cửa hàng, bạn có thể muốn cung cấp cho khách hàng một giảm giá tùy chỉnh khi thanh toán; nút bật/tắt cho Giảm Giá sẽ có sẵn tại thanh toán của cửa hàng bạn. Tuy nhiên, điều này được khuyến khích không sử dụng cho hệ thống tự thanh toán.

#### Thanh Toán Tùy Chỉnh

Khi tùy chọn Thanh Toán Tùy Chỉnh được bật, khách hàng có thể nhập giá của họ tương đương hoặc cao hơn hóa đơn gốc được tạo bởi cửa hàng.

#### Tùy Chọn Bổ Sung

Sau khi thiết lập mọi thứ cho Điểm Bán Hàng của bạn, còn một số tùy chọn bổ sung. Chủ cửa hàng có thể dễ dàng Nhúng PoS của họ thông qua một Iframe hoặc nhúng một nút thanh toán liên kết đến một mặt hàng cụ thể của cửa hàng. Để tạo phong cách cho cửa hàng PoS vừa được tạo, chủ cửa hàng có thể thêm CSS tùy chỉnh ở cuối các tùy chọn bổ sung.

#### Xóa ứng dụng này

Nếu chủ cửa hàng muốn hoàn toàn xóa Điểm Bán Hàng khỏi máy chủ BTCPay của mình, ở cuối cập nhật PoS, chủ cửa hàng có thể Nhấn vào nút Xóa ứng dụng này để hoàn toàn phá hủy ứng dụng PoS của họ. Khi nhấn "Xóa ứng dụng này", máy chủ BTCPay sẽ yêu cầu xác nhận bằng cách gõ `DELETE` và xác nhận bằng cách nhấn vào nút Xóa. Sau khi xóa, chủ cửa hàng trở lại bảng điều khiển máy chủ BTCPay.

### Máy chủ BTCPay - Gây Quỹ

Bên cạnh plugin Điểm Bán Hàng, máy chủ BTCPay cũng có tùy chọn để tạo một chiến dịch gây quỹ. Giống như bất kỳ nền tảng Gây Quỹ nào khác, chủ cửa hàng có thể thiết lập mục tiêu, tạo ưu đãi cho các đóng góp, và tùy chỉnh theo nhu cầu của họ.

#### Cách thiết lập một chiến dịch gây quỹ mới

Nhấn vào plugin Gây Quỹ thông qua menu chính ở bên trái của máy chủ BTCPay của bạn, dưới mục Plugin. Máy chủ BTCPay bây giờ sẽ yêu cầu một tên cho Gây Quỹ; tên này cũng sẽ được hiển thị trong thanh menu bên trái.
Tiêu đề được trao cho việc Gây quỹ cộng đồng cho công chúng.

#### Dòng Tagline

Đưa ra một câu slogan ngắn gọn để mọi người nhận biết đợt gây quỹ này về điều gì.

![hình ảnh](assets/en/107.webp)

#### URL Hình Ảnh Nổi Bật

Mỗi đợt gây quỹ đều có hình ảnh chính của mình, đó là banner mà bạn có thể nhận ra ngay lập tức. Hình ảnh này có thể được lưu trữ trên máy chủ của bạn nếu bạn có quyền Quản trị, Quản trị viên có thể tải lên trong phần cài đặt máy chủ BTCPay Server - Files. Khi bạn là chủ sở hữu cửa hàng, hình ảnh phải được tải lên web thông qua một bên thứ ba (ví dụ như imgur)

#### Công Khai Gây Quỹ

Công tắc này khiến cho đợt gây quỹ của bạn trở nên công khai và do đó có thể được thế giới bên ngoài nhìn thấy. Đối với mục đích kiểm tra hoặc để xem giao diện của bạn được áp dụng đúng cách, bạn có thể muốn giữ nó ở chế độ TẮT trong thời gian xây dựng đợt gây quỹ.

#### Mô Tả

Hãy kể cho thế giới biết về đợt gây quỹ của bạn, bạn đang gây quỹ cho điều gì? Mọi thứ giải thích về đợt gây quỹ của bạn đều được viết ở đây.

![hình ảnh](assets/en/108.webp)

#### Mục Tiêu Gây Quỹ

Đặt một mục tiêu cho số tiền mà đợt gây quỹ nên kiếm được cho dự án và đơn vị tiền tệ của mục tiêu nên được định giá. Đảm bảo rằng nếu mục tiêu của bạn được đặt giữa các ngày, bao gồm những ngày mục tiêu và kết thúc dưới phần Mục tiêu trong gây quỹ.

![hình ảnh](assets/en/109.webp)

#### Quyền Lợi

Quyền lợi giúp ích rất nhiều cho việc gây quỹ của bạn. Điều này là bởi vì quyền lợi cung cấp cho mọi người một cách tham gia vào chiến dịch của bạn. Chúng tác động đến động cơ ích kỷ cũng như động cơ nhân ái. Và chúng cho phép bạn tiếp cận với việc chi tiêu của những người ủng hộ, không chỉ là túi từ thiện của họ - bạn có thể đoán xem cái nào quan trọng hơn.

Tạo một quyền lợi mới bao gồm các trường sau:

- Tiêu đề
- Giá (cố định, tối thiểu, hoặc tùy chỉnh)
- URL Hình ảnh
- Mô tả
- Tồn kho
- ID
- Văn bản Nút Mua.
- Bật/Tắt

Một khi chủ cửa hàng đã điền đầy đủ tất cả các trường của quyền lợi mới để tạo, nhấn vào lưu, và bạn sẽ thấy rằng phần Quyền lợi trong gây quỹ bây giờ đang được điền vào.

![hình ảnh](assets/en/110.webp)

### BTCPay Server - Điểm Bán Hàng

#### Đóng Góp

Chủ cửa hàng có thể chọn cách hiển thị Quyền lợi, chúng được sắp xếp như thế nào, hoặc thậm chí được xếp hạng so với các quyền lợi khác. Tuy nhiên, một khi mục tiêu Gây quỹ được đạt, chủ cửa hàng có thể muốn ngừng việc đóng góp vào đợt gây quỹ này. Do đó, anh ta có thể bật "Không cho phép đóng góp thêm sau khi đạt mục tiêu". Điều này sẽ ngăn chặn Gây quỹ từ việc chấp nhận đóng góp.

##### Hành vi Gây Quỹ

Chỉ có hóa đơn được tạo với Gây quỹ mới được tính vào mục tiêu. Tuy nhiên, có thể có trường hợp chủ cửa hàng muốn tất cả hóa đơn được tạo trong cửa hàng này đều được tính vào gây quỹ.

#### Tùy Chọn Bổ Sung cho Việc Tùy Chỉnh

BTCPay Server cung cấp một số tùy chỉnh bổ sung. Thêm âm thanh, hoạt ảnh, hoặc thậm chí là luồng thảo luận vào Gây quỹ. Chủ cửa hàng cũng có thể thay đổi giao diện của Gây quỹ bằng cách nhập CSS tùy chỉnh của riêng mình.

#### Xóa Ứng Dụng này

Nếu chủ cửa hàng muốn hoàn toàn xóa Gây quỹ khỏi BTCPay Server của mình, ở cuối cập nhật Gây quỹ chủ cửa hàng có thể Nhấn vào nút “Xóa ứng dụng này” để hoàn toàn hủy bỏ ứng dụng Gây quỹ của mình. Khi nhấn "Xóa ứng dụng này", BTCPay Server sẽ yêu cầu xác nhận bằng cách gõ `DELETE` và xác nhận bằng cách nhấn vào nút Xóa. Sau khi xóa, chủ cửa hàng trở lại bảng điều khiển BTCPay Server.

### BTCPay Server - Nút Thanh Toán

Các nút thanh toán HTML dễ tích hợp và có thể tùy chỉnh cao cho phép chủ cửa hàng nhận được tiền tip và quyên góp. Trong thanh menu bên trái của BTCPay Server, dưới mục Plugins, chủ cửa hàng có thể nhấp vào “Pay Button” và nhấp Enable để tạo một Nút thanh toán.

#### Cài đặt Chung

Trong phần Cài đặt Chung cho Nút Thanh toán, chủ cửa hàng có thể thiết lập

- Giá tiêu chuẩn
- Tiền tệ mặc định
- Phương thức thanh toán mặc định
  - Sử dụng mặc định của cửa hàng
  - BTC trên chuỗi
  - BTC ngoài chuỗi (Lightning)
  - BTC ngoài chuỗi (LNURL-pay)
- Mô tả thanh toán
- ID đơn hàng

#### Tùy chọn Hiển thị

Nút thanh toán của BTCPay Server có thể được cấu hình để phù hợp với các phong cách khác nhau. Các nút có thể có một số tiền cố định hoặc tùy chỉnh, hiển thị bằng cách sử dụng thanh trượt hoặc các nút cộng và trừ.

#### Sử dụng Modal

Khi tạo nút thanh toán, chủ cửa hàng có thể chọn hành vi của nó khi khách hàng nhấp vào và hiển thị trong một modal hoặc trên một trang mới.

**!?Lưu Ý!?**

Cảnh báo: Nút thanh toán chỉ nên được sử dụng cho tiền tip và quyên góp

Sử dụng nút thanh toán cho tích hợp thương mại điện tử không được khuyến khích vì thông tin liên quan đến đơn hàng có thể được người dùng chỉnh sửa. Đối với thương mại điện tử, bạn nên sử dụng Greenfield API của chúng tôi. Nếu cửa hàng này xử lý các giao dịch thương mại, chúng tôi khuyên bạn nên tạo một cửa hàng riêng biệt trước khi sử dụng nút thanh toán.

#### Tùy chỉnh Văn bản Nút Thanh toán

Mặc định, nút thanh toán của BTCPay Server hiển thị "Pay With BTCPay". Chủ cửa hàng có thể thiết lập văn bản này theo ý muốn và thay đổi logo BTCPay Server bằng logo của riêng họ. Thiết lập văn bản bằng cách sử dụng "Pay Button Text" và dán URL hình ảnh dưới "Pay Button Image URL".

##### Kích thước Hình ảnh

Kích thước của hình ảnh trong nút chỉ có thể được thiết lập thành ba kích cỡ mặc định.

- 146x40px
- 168x46px
- 209x57px

#### Loại Nút

BTCPay Server biết đến ba trạng thái cho Nút Thanh toán.

- Số tiền Cố định
  - Giá đã được thiết lập trước trong cài đặt chung của nút.
- Số tiền Tùy chỉnh
  - Nút thanh toán của BTCPay Server có các nút + và - để thiết lập một giá tùy chỉnh.
  - Khi sử dụng số tiền tùy chỉnh, BTCPay Server sẽ yêu cầu một Min, Max và mức độ tăng dần.
  - Các nút có thể được thiết lập để “Sử dụng kiểu nhập đơn giản”. Điều này loại bỏ các nút +/-.
  - Phù hợp nút inline nơi nút và các nút điều chỉnh hiển thị cùng một dòng.
- Thanh trượt
  - Tương tự như số tiền tùy chỉnh, tuy nhiên, khác biệt về mặt hình ảnh vì nó có thanh trượt thay vì các nút +/-.
  - Khi sử dụng Thanh trượt, BTCPay Server sẽ yêu cầu một Min, Max và mức độ tăng dần.

**!?Lưu Ý!?**

Xóa Nút thanh toán có thể được thực hiện ở phía trên trong mô tả cảnh báo.

#### Thông báo Thanh toán

Server IPN (Instant Payment Notification) dành cho webhooks và có thể được điền bằng URL để đăng dữ liệu sau mua hàng.

#### Thông báo qua Email

Bất cứ khi nào có thanh toán, BTCPay Server có thể thông báo cho chủ cửa hàng.

#### Chuyển hướng Trình duyệt

Khi khách hàng hoàn thành việc mua hàng, anh ta sẽ được chuyển hướng đến liên kết này nếu được chủ cửa hàng thiết lập.

#### Tùy chọn Nút Thanh toán Nâng cao

Chỉ định các tham số chuỗi truy vấn bổ sung nên được thêm vào trang thanh toán một khi hóa đơn được tạo. Ví dụ, `lang=da-DK` sẽ tải trang thanh toán bằng tiếng Đan Mạch theo mặc định.

#### Sử dụng Ứng dụng làm Điểm cuối

Liên kết trực tiếp nút thanh toán với một mặt hàng trong một trong các ứng dụng PoS hoặc Crowdfund trước đó.
Các chủ cửa hàng có thể nhấp vào menu thả xuống và chọn Ứng dụng mong muốn; sau khi Ứng dụng được chọn, chủ cửa hàng có thể thêm mục cần được liên kết.

#### Mã Được Tạo

Vì nút Thanh toán của BTCPay Server là HTML dễ nhúng, BTCPay Server hiển thị mã được tạo để sao chép vào một trang web ở phía dưới sau khi cấu hình Nút Thanh toán.

Các chủ cửa hàng có thể sao chép mã được tạo vào trang web của họ, và Nút Thanh toán từ BTCPay Server sẽ trực tiếp hoạt động trên trang web của họ.

#### Thông Báo Thanh toán

IPN (Thông Báo Thanh toán Tức thì) của Máy chủ dành cho webhook và có thể được điền bằng URL để đăng dữ liệu mua hàng.

#### Thông Báo qua Email

Bất cứ khi nào một khoản thanh toán được thực hiện, BTCPay Server có thể thông báo cho chủ cửa hàng.

#### Chuyển hướng Trình duyệt

Khi khách hàng hoàn tất việc mua hàng, họ sẽ được chuyển hướng đến liên kết này nếu được chủ cửa hàng thiết lập.

#### Tùy chọn Nút Thanh toán Nâng cao

Chỉ định các tham số chuỗi truy vấn bổ sung nên được thêm vào trang thanh toán một khi hóa đơn được tạo. Ví dụ, `lang=da-DK` sẽ tải trang thanh toán bằng tiếng Đan Mạch theo mặc định.

#### Sử dụng Ứng dụng như Điểm cuối

Liên kết trực tiếp nút thanh toán với một mục trong một trong các ứng dụng PoS hoặc Crowdfund trước đó. Các chủ cửa hàng có thể nhấp vào menu thả xuống và chọn ứng dụng mong muốn, sau khi ứng dụng được chọn, chủ cửa hàng có thể thêm mục cần được liên kết.

#### Mã Được Tạo

Vì nút Thanh toán của BTCPay Server là HTML dễ nhúng, BTCPay Server hiển thị mã được tạo để sao chép vào một trang web ở phía dưới sau khi cấu hình Nút Thanh toán. Các chủ cửa hàng có thể sao chép mã được tạo vào trang web của họ và Nút Thanh toán từ BTCPay Server sẽ trực tiếp hoạt động trên trang web của họ.

### Tóm tắt Kỹ năng

Trong phần này bạn đã học:

- Cách sử dụng plugin PoS tích hợp của BTCPay Server để dễ dàng tạo một cửa hàng tùy chỉnh
- Cách sử dụng plugin Crowdfund tích hợp của BTCPay Server để dễ dàng tạo một ứng dụng gây quỹ tùy chỉnh
- Tạo mã cho nút thanh toán tùy chỉnh sử dụng plugin Nút Thanh toán

### Đánh giá Kiến thức

#### Đánh giá KA

Ba plugin tích hợp có sẵn với BTCPay Server là gì? Mô tả ngắn gọn cách mỗi plugin có thể được sử dụng.

# Cấu hình BTCPay Server

<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>

## Hiểu biết cơ bản về việc cài đặt BTCPay Server trên môi trường LunaNode

<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>

### Cài đặt BTCPay Server trên Môi trường Được lưu trữ (LunaNode)

Những bước này sẽ cung cấp tất cả thông tin cần thiết để bắt đầu sử dụng BTCPay Server trên LunaNode. Có nhiều lựa chọn về cách triển khai phần mềm.
Bạn có thể tìm tất cả chi tiết của BTCPay Server tại https://docs.btcpayserver.org.

#### Bắt đầu từ đâu?

Trong phần này, bạn sẽ làm quen với LunaNode là nhà cung cấp dịch vụ lưu trữ, tìm hiểu về những bước đầu tiên khi sử dụng BTCPay Server của bạn, và tìm hiểu cách tiếp tục với Lightning Network. Sau khi chúng ta đã đi qua tất cả các bước, bạn có thể vận hành một cửa hàng trực tuyến hoặc nền tảng gây quỹ chấp nhận Bitcoin!

Đây là một trong nhiều cách để triển khai BTCPay Server. Đọc tài liệu của chúng tôi để biết thêm chi tiết,

https://docs.btcpayserver.org.

### Triển khai BTCPay Server - LunaNode

Đầu tiên, hãy truy cập vào trang web của LunaNode.com, nơi chúng ta sẽ tạo một tài khoản mới. Nhấp vào "Sign Up" ở góc trên bên phải hoặc sử dụng trình hướng dẫn "Get Started" trên trang chủ của họ.
![image](assets/en/111.webp)

Sau khi bạn đã tạo tài khoản mới, LunaNode sẽ gửi một email xác nhận. Một khi bạn xác nhận tài khoản, so với Voltage, bạn ngay lập tức được yêu cầu nạp tiền vào số dư tài khoản của mình. Số dư này cần thiết để thanh toán chi phí không gian máy chủ và hosting.

![image](assets/en/112.webp)

#### Nạp tiền vào tài khoản LunaNode của bạn

Khi bạn nhấp vào "Deposit credit", bạn sẽ được thiết lập số tiền muốn nạp vào tài khoản và phương thức thanh toán. LunaNode và BTCPay Server sẽ có chi phí từ 10$USD đến 20$USD hàng tháng.
So với Voltage.cloud, bạn sẽ có quyền truy cập đầy đủ vào Máy chủ Ảo Riêng của mình (VPS từ đây trở đi) và do đó có thêm một số quyền kiểm soát đối với máy chủ của mình. Sau khi bạn đã tạo tài khoản mới, LunaNode sẽ gửi một email xác nhận.
Một khi bạn xác nhận tài khoản, so với Voltage, bạn ngay lập tức được yêu cầu nạp tiền vào số dư tài khoản của mình. Số dư này cần thiết để thanh toán chi phí không gian máy chủ và hosting.

#### Cách triển khai một máy chủ mới?

Trong hướng dẫn này, chúng ta sẽ đi qua quá trình thiết lập bằng cách tạo một bộ khóa API và sử dụng trình khởi chạy BTCPay Server do LunaNode tạo ra.

Trong bảng điều khiển LunaNode của bạn, nhấp vào API ở góc trên bên phải. Điều này mở ra một trang mới. Chúng ta chỉ cần thiết lập Tên cho khóa API. Phần còn lại sẽ được LunaNode xử lý và sẽ không được đề cập trong hướng dẫn này. Nhấp vào nút "Create API Credential".
Sau khi tạo xong thông tin xác thực API, bạn sẽ nhận được một chuỗi dài các chữ cái và ký tự. Đây là khóa API của bạn.

![image](assets/en/113.webp)

#### Cách triển khai một máy chủ mới?

Có 2 phần cho thông tin xác thực này, khóa API và ID API; chúng ta sẽ cần cả hai. Trước khi chúng ta tiếp tục bước tiếp theo, hãy mở một tab mới trong trình duyệt và truy cập vào https://launchbtcpay.lunanode.com/

Tại đây, bạn sẽ được yêu cầu cung cấp khóa API và ID API của mình. Điều này để xác minh rằng chính bạn là người thiết lập máy chủ mới này. Khóa API vẫn nên được mở trong tab trước đó của bạn; nếu bạn cuộn xuống bảng bên dưới, bạn sẽ tìm thấy ID API.

Quay lại trang với Launcher, điền các trường với khóa API và ID của bạn, và nhấp vào tiếp tục.

![image](assets/en/114.webp)

Trong bước tiếp theo, bạn có thể cung cấp tên miền. Nếu bạn đã sở hữu một tên miền và muốn sử dụng nó cho BTCPay Server, hãy đảm bảo bạn cũng thêm bản ghi DNS (Gọi là bản ghi `A`) vào tên miền của mình. Nếu bạn không sở hữu một tên miền, hãy sử dụng tên miền do LunaNode cung cấp thay thế (bạn có thể thay đổi điều này sau trong cài đặt BTCPay Server) và nhấp vào Tiếp tục.

Đọc thêm về cách thiết lập hoặc thay đổi bản ghi DNS cho BTCPay Server; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name

#### Khởi chạy BTCPay Server trên LunaNode

Sau khi thực hiện các bước trước, chúng ta có thể thiết lập tất cả các tùy chọn cho máy chủ mới của mình. Tại đây chúng ta sẽ chọn Bitcoin (BTC) là đồng tiền được hỗ trợ; chúng ta có thể thiết lập email để nhận thông báo về việc gia hạn chứng chỉ mã hóa; điều này không bắt buộc.
Hướng dẫn này nhằm mục đích thiết lập một môi trường Mainnet (Bitcoin thực tế); tuy nhiên, LunaNode cũng cho phép bạn thiết lập này cho Testnet hoặc Regtest cho mục đích phát triển. Chúng tôi sẽ giữ tùy chọn Mainnet cho hướng dẫn này.
Chọn triển khai Lightning của bạn. LunaNode cung cấp hai triển khai khác nhau, LND và Core Lightning. Đối với hướng dẫn này, chúng tôi sẽ chọn LND. Có những khác biệt nhỏ nhưng thực sự giữa cả hai triển khai; để biết thêm về điều này, chúng tôi khuyên bạn đọc kỹ tài liệu mở rộng; https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln

![hình ảnh](assets/en/115.webp)

LunaNode cung cấp nhiều kế hoạch Máy Ảo (VM) khác nhau. Những kế hoạch này khác nhau về phạm vi giá và thông số kỹ thuật của máy chủ. Đối với hướng dẫn này, một kế hoạch m2 sẽ đủ; tuy nhiên, nếu bạn đã chọn nhiều hơn chỉ Bitcoin làm tiền tệ, hãy xem xét sử dụng ít nhất m4.

Tăng tốc độ đồng bộ hóa blockchain ban đầu; điều này là tùy chọn và phụ thuộc vào nhu cầu của bạn. Có các tùy chọn nâng cao như thiết lập một Lightning Alias, chỉ định một phiên bản GitHub cụ thể, hoặc thiết lập khóa SSH; không có tùy chọn nào trong số này được đề cập trong hướng dẫn này.

Sau khi điền vào mẫu, bạn phải nhấp vào Launch VM, và Lunanode sẽ bắt đầu tạo VM mới của bạn, bao gồm cả việc cài đặt BTCPay Server trên đó. Quá trình này mất vài phút; một khi máy chủ của bạn sẵn sàng, LunaNode sẽ cung cấp cho bạn liên kết đến BTCPay Server mới của bạn.

Sau quá trình tạo, nhấp vào liên kết đến BTCPay Server của bạn; tại đây, bạn sẽ được yêu cầu tạo một tài khoản Quản trị viên.

![hình ảnh](assets/en/116.webp)

### Tóm Tắt Kỹ Năng

Trong phần này bạn đã học:

- Tạo và nạp tiền vào tài khoản trên LunaNode
- Sử dụng BTCPay Server Launcher để tạo máy chủ của riêng bạn

### Đánh Giá Kiến Thức

#### Đánh Giá Khái Niệm

Mô tả một số sự khác biệt giữa việc chạy một phiên bản của BTCPay Server trên một VPS so với việc tạo một tài khoản trên một phiên bản được lưu trữ.

## Cài Đặt BTCPay Server trên môi trường Voltage

<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>

Bạn sẽ làm quen với Voltage.cloud là nhà cung cấp dịch vụ lưu trữ, tìm hiểu về các bước đầu tiên khi sử dụng BTCPay Server của mình, và học cách tiếp tục với Lightning Network. Sau khi chúng ta đã đi qua tất cả các bước, bạn có thể chạy một cửa hàng trực tuyến hoặc nền tảng gây quỹ chấp nhận Bitcoin!

Đây là một trong nhiều cách để triển khai BTCPay Server. Đọc tài liệu của chúng tôi để biết thêm chi tiết,
https://docs.btcpayserver.org.

### BTCPay Server - Triển khai Voltage.cloud

Đầu tiên, truy cập website Voltage.cloud và đăng ký một tài khoản mới. Khi tạo tài khoản, bạn có thể đăng ký một thử nghiệm miễn phí 7 ngày. Hoặc nhấp vào Sign Up ở góc phải trên cùng hoặc sử dụng "Try a free 7 day trial" trên trang chủ của họ.

![hình ảnh](assets/en/117.webp)

Sau khi bạn đã tạo một tài khoản, nhấp vào nút `NODES` trên bảng điều khiển của bạn. Một khi chúng tôi đã chọn Nodes và tạo một node mới, chúng tôi được giới thiệu với các node mà Voltage cung cấp. Vì hướng dẫn này cũng sẽ đi qua LightningNetwork, tại Voltage, chúng tôi đầu tiên phải chọn triển khai Lightning của mình trước khi tạo một BTCPay Server. Nhấp vào LightningNode.

![hình ảnh](assets/en/118.webp)
Tại đây, bạn sẽ phải chọn loại Lightning node mà bạn muốn. Voltage cung cấp nhiều lựa chọn cho cấu hình lighting của bạn. Điều này khác biệt khi triển khai với, ví dụ như, LunaNode. Đối với mục đích của hướng dẫn này, một Lite Node sẽ đủ. Đọc thêm về sự khác biệt tại Voltage.cloud.
![image](assets/en/119.webp)

Đặt tên cho node của bạn, thiết lập một mật khẩu và bảo vệ mật khẩu này. Nếu mất mật khẩu này, bạn sẽ mất quyền truy cập vào các bản sao lưu, và Voltage không thể khôi phục nó. Tạo node, và Voltage sẽ hiển thị tiến trình. Voltage đã tạo Lightning Node của bạn. Bây giờ chúng ta có thể tạo instance BTCPay Server và truy cập trực tiếp vào Lightning Network.

Nhấp vào Nodes ở góc trên bên trái của bảng điều khiển của bạn. Tại đây bạn có thể thiết lập phần tiếp theo của instance BTCPay Server của mình. Nhấp vào "create new" một khi bạn ở trong tổng quan nodes. Bạn sẽ nhận được một màn hình tương tự như trước. Bây giờ thay vì Lightning Node, chúng ta chọn BTCPay Server.

Voltage hiển thị vị trí địa lý của BTCPay Server của bạn, voltage lưu trữ ở khu vực Tây nước Mỹ. Tại đây bạn cũng sẽ thấy chi phí lưu trữ server. Nhấp vào Create và đặt tên cho BTCPay Server của bạn. Kích hoạt Lightning và Voltage sẽ hiển thị Lightning node được tạo trong bước trước. Nhấp vào Create, và Voltage sẽ tạo một instance BTCPay Server.

![image](assets/en/120.webp)

Sau khi bạn nhấp vào create, Voltage sẽ cung cấp cho bạn tên người dùng và mật khẩu mặc định. Chúng tương tự như mật khẩu bạn đã thiết lập trước đó trong Voltage. Nhấp vào nút Login to Account để được chuyển hướng đến BTCPay Server của bạn.

Chào mừng đến với instance BTCPay Server mới của bạn. Vì chúng tôi đã thiết lập Lightning trong quá trình tạo, nó sẽ hiển thị Lightning đã được kích hoạt!

### Tóm tắt Kỹ năng

Trong chương này bạn đã học:

- Tạo một tài khoản trên Voltage.cloud
- Các bước để vận hành BTCPay Server cùng với một Lightning node trên tài khoản

### Đánh giá Kiến thức

#### Đánh giá Khái niệm

Những điểm khác biệt chính giữa cài đặt Voltage và LunaNode là gì?

## Cài đặt BTCPay Server trên một node Umbrel

<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>

Sau những bước này, bạn có thể chấp nhận thanh toán lightning cho cửa hàng BTCPay của mình trên mạng nội bộ. Quy trình này cũng áp dụng nếu bạn vận hành một node umbrel trong một nhà hàng hoặc doanh nghiệp. Nếu bạn muốn kết nối cửa hàng này với một website công cộng, theo dõi bài tập Nâng cao để phơi bày node umbrel của bạn ra công chúng.

https://umbrel.com/

![image](assets/en/121.webp)

### BTCPay Server - Triển khai Umbrel

Sau khi node Umbrel của bạn đã đồng bộ hoàn toàn với blockchain Bitcoin, đi đến Umbrel App Store, và tìm kiếm BTCPay Server dưới mục Apps.

![image](assets/en/122.webp)

Nhấp vào BTCPay Server để xem chi tiết App. Khi chi tiết của BTCPay Server được mở, phía dưới bên phải hiển thị các yêu cầu để App hoạt động đúng cách. Nó cho thấy nó yêu cầu Bitcoin và Lightning node. Nếu bạn chưa cài đặt Lightning Node trên Umbrel của mình, nhấp vào Install. Quá trình này có thể mất vài phút.

![image](assets/en/123.webp)

Sau khi cài đặt Lightning Node của bạn:

1. Nhấp mở trong chi tiết app hoặc trên App trong bảng điều khiển Umbrels.
2. Nhấp vào thiết lập một node mới; bạn sẽ được hiển thị 24 từ cho việc khôi phục lightning node của mình.
3. Ghi chúng lại.

![image](assets/en/124.webp)
Umbrel sẽ yêu cầu xác minh các từ vừa được ghi lại. Sau khi cài đặt nút Lightning, quay lại Umbrel App Store và tìm BTCPay Server. Nhấn vào nút cài đặt, và Umbrel sẽ hiển thị nếu các thành phần cần thiết đã được cài đặt và BTCPay Server yêu cầu quyền truy cập vào các thành phần này. Sau khi cài đặt, nhấn Mở ở góc trên bên phải của chi tiết Ứng dụng hoặc mở BTCPay Server qua bảng điều khiển của Umbrel.

Umbrel sẽ yêu cầu xác minh các từ vừa được ghi lại.

![hình ảnh](assets/en/125.webp)

**!?Lưu Ý!?**

Hãy chắc chắn lưu trữ chúng ở một vị trí thích hợp như bạn đã được học khi lưu trữ khóa.

Sau khi cài đặt nút Lightning, quay lại Umbrel App Store và tìm BTCPay Server. Nhấn vào nút cài đặt, và Umbrel sẽ hiển thị nếu các thành phần cần thiết đã được cài đặt và BTCPay Server yêu cầu quyền truy cập vào các thành phần này.

![hình ảnh](assets/en/126.webp)

Sau khi cài đặt, nhấn Mở ở góc trên bên phải của chi tiết Ứng dụng hoặc mở BTCPay Server qua bảng điều khiển của Umbrel.

![hình ảnh](assets/en/127.webp)

### Tóm Tắt Kỹ Năng

Trong phần này bạn đã học:

- Các bước để cài đặt BTCPay Server với chức năng Lightning trên một nút Umbrel

### Đánh Giá Kiến Thức

#### Đánh Giá Khái Niệm

Cài đặt trên Umbrel khác với hai lựa chọn được lưu trữ trước đó như thế nào?

# Kết Luận

<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>


## Cho chúng tôi biết phản hồi của bạn về khóa học này
<chapterId>b7d7c8a7-ef23-bfa0-3618-26f5a7ea467d</chapterId>
<isCourseReview>true</isCourseReview>

## Kết Luận Khóa Học

<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

![hình ảnh](assets/en/128.webp)

Bạn cũng nên có một hiểu biết tổng quan về Bitcoin là gì, nó hoạt động như thế nào, và nó có thể mở rộng như thế nào với các lớp thứ hai như Lightning Network. Trong khóa học này, chúng tôi đã đề cập đến việc sử dụng BTCPay Server một cách toàn diện, từ việc cài đặt ban đầu đến việc tạo cửa hàng và quản lý hóa đơn phức tạp, để trở thành một cá nhân hoặc doanh nghiệp tự chủ về tài chính.

Xin chúc mừng bạn đã hoàn thành khóa học này. Chúng tôi hy vọng bạn đã thích nội dung và tiếp tục sử dụng và khám phá BTCPay Server, và cảm thấy phấn khích về tương lai hứa hẹn mà Bitcoin và cộng đồng ngày càng phát triển của các nhà xây dựng và người tham gia sẽ mang lại như chúng tôi.

> **FOSS là điều không thể tránh khỏi.**

### Từ Vựng

| Thuật Ngữ                               | Định Nghĩa                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 51% Attack                              | Hành động xây dựng một chuỗi khối mới dài nhất để thay thế các khối trong blockchain. Điều này cho phép bạn thay thế các giao dịch đã được khai thác vào blockchain. Loại tấn công này dễ thực hiện nhất khi bạn có đa số sức mạnh khai thác, đó là lý do tại sao nó được gọi là “Tấn công Đa Số” hoặc “Tấn công 51%”.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| AccountKey                              | Khóa tài khoản để rebase                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| AccountKeyPath                          | Đường dẫn từ gốc đến khóa tài khoản được tiền tố bởi dấu vân tay khóa công khai chính.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Địa Chỉ                                 | Địa chỉ Bitcoin mã hóa gọn gàng thông tin cần thiết để thanh toán cho người nhận. Một địa chỉ hiện đại bao gồm một chuỗi các chữ cái và số bắt đầu với bc1 và trông giống như bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4. Địa chỉ là cách viết tắt cho script khóa của người nhận, có thể được người gửi sử dụng để chuyển tiền cho người nhận. Hầu hết các địa chỉ hoặc là đại diện cho khóa công khai của người nhận hoặc một số hình thức script định nghĩa các điều kiện chi tiêu phức tạp hơn. Ví dụ trước đây là một địa chỉ bech32 mã hóa một chương trình chứng nhận khóa tiền vào hash của một khóa công khai (Xem Pay-to-Witness-Public-Key-Hash). Cũng có các định dạng địa chỉ cũ hơn bắt đầu với 1 hoặc 3 sử dụng mã hóa địa chỉ Base58Check để đại diện cho hash của khóa công khai hoặc hash của script. |
| Loại Địa Chỉ                            | Một địa chỉ có thể đại diện cho nhiều script khác nhau. Địa chỉ được mã hóa và có tiền tố để truyền đạt loại script của chúng. Địa chỉ di sản sử dụng Base58, và khi một địa chỉ di sản là hash của một khóa công khai, một địa chỉ P2PKH, nó bắt đầu với ‘1’. Ít thường xuyên hơn, một địa chỉ di sản là hash của một script, trong trường hợp đó nó sẽ bắt đầu với ‘3’. Hiện tại, tất cả địa chỉ SegWit được mã hóa trong Bech32 và bắt đầu với tiền tố ‘bc1’.                                                                                                                                                                                                                                                                                                                                                        |
| Ứng Dụng                                | BTCPay Server có các plugin có thể hoạt động như một ứng dụng độc lập.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| BIP 329                                 | Xuất/nhập nhãn ví                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| BIP49                                   | Định nghĩa lược đồ phái sinh cho ví HD sử dụng định dạng serialization P2WPKH-nested-in-P2SH (BIP 141) cho các giao dịch chứng nhận chia tách.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Địa Chỉ Bitcoin                         | Chuỗi ký tự chữ và số nơi bạn gửi bitcoin của mình, vì vậy nó “sống” ở đó bây giờ là một dạng nhận dạng, bao gồm một chuỗi khoảng 33 chữ cái và số kết hợp. Trong phiên bản giao thức hiện tại, một địa chỉ bắt đầu với 1, 3, hoặc b. Có địa chỉ của người nhận là một phần cần thiết để khởi tạo giao dịch bitcoin. Địa chỉ Bitcoin được tạo từ khóa công khai và nhiều địa chỉ có thể được tạo từ một bộ khóa công khai để cải thiện sự riêng tư. Địa chỉ Bitcoin hoạt động giống như địa chỉ email, nếu bạn muốn gửi một tin nhắn bạn cần biết nó đang đi đâu, tương tự như với bitcoin. Trước khi gửi một giao dịch bitcoin, bạn cần đảm bảo rằng địa chỉ của người nhận chính xác vì giao dịch bitcoin không thể đảo ngược và bạn có thể đang gửi bitcoin đến địa chỉ không thuộc về người nhận.                   |
| bitcoin so với Bitcoin                  | Bitcoin là mạng tiền tệ, và bitcoin (viết thường) là đơn vị tiền tệ trên mạng Bitcoin. Bạn sử dụng tiền tệ bitcoin hoặc token để giao dịch trên mạng Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Khối                                    | Một khối là cấu trúc dữ liệu trong blockchain Bitcoin bao gồm một tiêu đề và một phần thân của các giao dịch Bitcoin. Khối được đánh dấu với dấu thời gian và cam kết với một khối tiền nhiệm (khối cha) cụ thể. Khi được băm, tiêu đề khối cung cấp bằng chứng công việc làm cho blockchain trở nên không thể thay đổi theo xác suất. Các khối phải tuân thủ các quy tắc được thực thi bởi sự đồng thuận của mạng để mở rộng blockchain. Khi một khối được thêm vào blockchain, các giao dịch bao gồm được coi là đã có xác nhận đầu tiên.                                                                                                                                                                                                                                                                             |
| Trình Duyệt Khối                        | Một công cụ trực tuyến cho phép bạn tìm kiếm thông tin thời gian thực và lịch sử về một blockchain, bao gồm dữ liệu liên quan đến khối, giao dịch, địa chỉ, và nhiều hơn nữa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Mã Hash Khối                            | Mã hash của một khối là mã hash SHA-256 của dữ liệu khối, thường được biểu diễn dưới dạng hệ thập lục phân. Mã hash khối có thể được hiểu như một số rất lớn. Để đáp ứng yêu cầu Chứng minh Công việc (Proof-of-Work), mã hash của một khối phải nằm dưới một ngưỡng nhất định. Do đó, tất cả mã hash khối bắt đầu bằng một chuỗi các số không theo sau là một chuỗi ký tự chữ và số. Một số khối có tới hai mươi số không đứng đầu, trong khi các khối trước đây có ít như tám số không. Số lượng số không yêu cầu phản ánh sơ bộ về độ khó của việc khai thác vào thời điểm khối được công bố.                                                                                                                                                                                                                        |
| Chiều Cao Khối                          | Mỗi khối được đánh số theo thứ tự tăng dần, bắt đầu từ số không.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Phần Thưởng Khối                        | Bao gồm phần thưởng khối (bitcoin mới được tạo) và tổng số phí giao dịch từ các giao dịch được bao gồm trong khối.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Kích Thước Khối                         | Mỗi khối có một lượng dữ liệu giới hạn có thể chứa. Dữ liệu không vừa vào một khối nhất định sẽ được ghi lại trong một trong số các khối tiếp theo. Đối với các khối bitcoin, trước đây có kích thước khối là 1mb, tuy nhiên sau một soft fork kích thước khối có thể chứa lên đến 4mb dữ liệu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Phần Thưởng Phụ Khối                    | Lượng bitcoin mới được tạo ra trong mỗi khối. Mỗi khối được sản xuất và thêm vào blockchain cho phép người tạo khối đúc một lượng bitcoin mới nhất định. Phần thưởng bắt đầu từ 50 BTC mỗi khối, và được cắt giảm một nửa sau mỗi 210,000 khối hoặc khoảng 4 năm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Blockchain                              | Một nhật ký phân tán, hoặc cơ sở dữ liệu, của tất cả giao dịch Bitcoin. Giao dịch được nhóm trong các cập nhật rời rạc gọi là khối, giới hạn lên đến 4 triệu đơn vị trọng lượng. Các khối được sản xuất khoảng mỗi 10 phút thông qua một quá trình ngẫu nhiên gọi là khai thác. Mỗi khối bao gồm một "chứng minh công việc" đòi hỏi tính toán phức tạp. Yêu cầu chứng minh công việc được sử dụng để điều chỉnh khoảng thời gian giữa các khối và bảo vệ blockchain khỏi các cuộc tấn công nhằm viết lại lịch sử: kẻ tấn công cần phải vượt qua chứng minh công việc hiện có để thay thế các khối đã được công bố, làm cho mỗi khối có tính bất biến theo xác suất khi nó được chôn dưới các khối tiếp theo.                                                                                                            |
| BTCPay Server Vault                     | Để cân bằng tối ưu giữa sự tiện lợi, an toàn và riêng tư, nên sử dụng Ví BTCPay Server với một ví cứng. BTCPay Vault được xây dựng để kết nối Ví Cứng và BTCPay Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Vấn Đề Các Tướng Byzantine              | Một vấn đề trong lý thuyết trò chơi mô tả khó khăn mà các bên phi tập trung gặp phải khi đạt được sự đồng thuận mà không cần dựa vào một bên trung tâm đáng tin cậy. Tên gọi xuất phát từ tình huống của một số tướng bao vây Byzantium. Họ đã bao vây thành phố, nhưng họ phải quyết định cùng nhau thời điểm tấn công. Nếu tất cả các tướng tấn công cùng một lúc, họ sẽ chiến thắng, nhưng nếu họ tấn công vào các thời điểm khác nhau, họ sẽ thua. Các tướng không có kênh liên lạc an toàn với nhau vì bất kỳ thông điệp nào họ gửi hoặc nhận có thể đã bị chặn hoặc gửi một cách lừa đảo bởi những người bảo vệ Byzantium. Làm thế nào các tướng có thể tổ chức tấn công cùng một lúc?                                                                                                                            |
| Kiểm Duyệt                              | Kiểm soát thông tin nào có thể được truyền đến quần chúng. Khi nói đến bitcoin, kiểm duyệt là về khả năng ngăn chặn giao dịch bởi bên thứ ba.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Tiền Thối                               | Phần của UTXOs được trả lại vào ví của người gửi, thường qua một địa chỉ khác. Bằng cách tính tổng số đầu vào trừ đi số tiền đã chi và phí giao dịch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Child Pays For Parent (CPFP)            | Kỹ thuật tăng phí giao dịch, trong đó người dùng chi tiêu một đầu ra từ một giao dịch chưa xác nhận có mức phí thấp trong một giao dịch con với mức phí cao nhằm khuyến khích các thợ mỏ bao gồm cả hai giao dịch trong một khối.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Coinbase Transaction                    | Giao dịch đầu tiên trong mỗi khối, phân phối phần thưởng khối và phí giao dịch cho người đã khai thác khối đó.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Coincidence of Wants                    | Hiện tượng kinh tế khi hai bên mỗi bên sở hữu một mặt hàng mà bên kia mong muốn, vì vậy họ trao đổi những mặt hàng này trực tiếp mà không qua trung gian tiền tệ.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Cold Storage                            | Cách quản lý dữ liệu mà không cần kết nối internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Cold Wallet                             | Loại ví bitcoin lưu trữ khóa riêng của bạn ngoại tuyến, thường trên một thiết bị vật lý. Còn được biết đến như một ví cứng, và nó bảo vệ bitcoin số của bạn khỏi hacker trực tuyến bằng cách sử dụng thiết bị giống như ổ đĩa flash không kết nối internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Command Line Interface (CLI)            | Tương tác với thiết bị hoặc chương trình máy tính bằng các lệnh từ người dùng hoặc khách hàng, và phản hồi từ thiết bị hoặc chương trình, dưới dạng các dòng văn bản.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Commitment Transaction                  | Giao dịch cam kết là một giao dịch Bitcoin, được ký bởi cả hai đối tác kênh, mã hóa số dư mới nhất của một kênh. Mỗi khi một khoản thanh toán mới được thực hiện hoặc chuyển tiếp sử dụng kênh, số dư kênh sẽ được cập nhật, và một giao dịch cam kết mới sẽ được ký bởi cả hai bên. Quan trọng, trong một kênh giữa Alice và Bob, cả Alice và Bob giữ phiên bản của riêng mình về giao dịch cam kết, cũng được ký bởi bên kia. Bất kỳ lúc nào, kênh có thể được đóng bởi Alice hoặc Bob nếu họ nộp giao dịch cam kết của mình lên blockchain Bitcoin. Nộp một giao dịch cam kết cũ (lỗi thời) được coi là gian lận (tức là, vi phạm giao thức) trong Lightning Network và có thể bị phạt bởi bên kia, tuyên bố tất cả các quỹ trong kênh cho mình, thông qua một giao dịch phạt.                                       |
| Confirmation                            | Một khi giao dịch được bao gồm trong một khối, nó có một xác nhận. Ngay khi một khối khác được khai thác trên blockchain, giao dịch có hai xác nhận, và cứ thế tiếp tục. Sáu xác nhận trở lên được coi là bằng chứng đủ để chứng minh rằng giao dịch không thể được đảo ngược.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Crowdfund (CF)                          | Một plugin mặc định của BTCPay Server cho phép chủ cửa hàng dễ dàng tạo một trang web gây quỹ điển hình. Họ có thể dễ dàng đặt mục tiêu, tạo ưu đãi cho các đóng góp, và tùy chỉnh theo nhu cầu của mình.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Cryptography                            | Một hệ thống đặc biệt, nơi thông điệp gốc được thay đổi sao cho chỉ những người nhận dự định mới có thể nhận được.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Dashboard                               | Trang chính của BTCPay Server. Nó cung cấp một cái nhìn tổng quan về tất cả hoạt động cho một cửa hàng, hiển thị qua nhiều ô tóm tắt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Demo                                    | Đề cập đến môi trường ảo mà các bản demo phần mềm diễn ra.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Deployment                              | Triển khai phần mềm là tất cả các hoạt động làm cho một hệ thống phần mềm sẵn sàng để sử dụng. Quá trình triển khai chung bao gồm nhiều hoạt động liên quan với các chuyển tiếp có thể xảy ra giữa chúng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Đường Dẫn Phái Sinh                     | Một dữ liệu chỉ ra cho ví Phân Cấp Xác Định (HD) cách phái sinh một khóa cụ thể trong một cây khóa. Đường dẫn phái sinh được sử dụng như một tiêu chuẩn Bitcoin và được giới thiệu cùng với ví HD như một phần của BIP 32.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Điều Chỉnh Độ Khó                       | Điều chỉnh mục tiêu độ khó, cứ sau 2016 khối (khoảng hai tuần) để cố gắng đảm bảo rằng các khối được khai thác mỗi 10 phút một lần trung bình. Do đó, nó tạo ra một khoảng thời gian nhất quán giữa các khối và một lượng phát hành bitcoin mới nhất quán vào mạng (thông qua phần thưởng khối).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Mục Tiêu Độ Khó                         | Trong khai thác, đây là một số mà hash của khối phải thấp hơn để khối được thêm vào blockchain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Chữ Ký Số                               | Chữ ký số là một phương pháp toán học để xác minh tính xác thực và toàn vẹn của các thông điệp hoặc tài liệu số. Nó có thể được coi là một cam kết mật mã trong đó thông điệp không bị ẩn giấu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Có Thể Chia Nhỏ                         | Tính chất của một hàng hóa có thể được chia nhỏ thành các lượng nhỏ hơn mà không mất giá trị. Bởi vì các giao dịch kinh tế thường xảy ra với các lượng khác nhau, một loại tiền tệ phải có thể chia nhỏ để được sử dụng rộng rãi trong nền kinh tế.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Docker                                  | Phần mềm đóng gói phần mềm vào các đơn vị tiêu chuẩn gọi là container chứa mọi thứ phần mềm cần để chạy bao gồm thư viện, công cụ hệ thống, mã và thời gian chạy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Gấp Đôi Chi Tiêu                        | Kết quả của việc chi tiêu thành công một số tiền hơn một lần. Bitcoin bảo vệ chống lại việc chi tiêu gấp đôi bằng cách xác minh rằng mỗi giao dịch được thêm vào blockchain tuân thủ các quy tắc đồng thuận; điều này có nghĩa là kiểm tra xem các đầu vào cho giao dịch chưa được chi tiêu trước đó.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Bền Vững                                | Tính chất của tiền, trong đó tiền tệ có thể duy trì trạng thái ban đầu theo thời gian và chịu được sử dụng lặp đi lặp lại. Một đồng tiền bền vững phải có khả năng sống sót trước các tổn thương tiềm ẩn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Electrum                                | Electrum là một trong những ví Bitcoin phổ biến nhất, được tạo ra vào năm 2011.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Khóa Công Khai Mở Rộng (Xpub)           | Khóa công khai mở rộng còn được biết đến là Xpub, một khóa công khai hoạt động như một khóa cha cho các khóa được phái sinh từ Xpub như một tính năng của ví HD. Xpub là một tiêu chuẩn được giới thiệu trong BIP 32. Ví sử dụng nó một cách ẩn danh để phái sinh các khóa công khai. Việc chia sẻ Xpub không được khuyến khích, tài sản của bạn sẽ không có nguy cơ bị di chuyển trực tiếp, Xpub không thể phái sinh các khóa riêng tư. Lợi ích của việc chia sẻ một Xpub có thể là cho mục đích gây quỹ trong BTCPay Server. Xpub được chia sẻ thông qua phương tiện trực tuyến, trong khi các khóa riêng tư vẫn ở ngoại tuyến trên một HWW.                                                                                                                                                                          |
| F.U.D.                                  | Viết tắt của Fear, uncertainty and doubt (Sợ hãi, không chắc chắn và nghi ngờ); Thường được gợi lên một cách có chủ ý nhằm đặt một đối thủ vào tình thế bất lợi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Phí                                     | Trong bối cảnh của Lightning Network, các nút sẽ thu phí định tuyến cho việc chuyển tiếp các khoản thanh toán của người dùng khác. Các nút cá nhân có thể thiết lập chính sách phí của riêng mình, được tính toán dựa trên tổng số của một phí cơ bản cố định và một tỷ lệ phí phụ thuộc vào số tiền thanh toán. Trong bối cảnh của Bitcoin, người gửi của một giao dịch trả một phí giao dịch cho các thợ mỏ để bao gồm giao dịch trong một khối. Phí giao dịch Bitcoin không bao gồm phí cơ bản và phụ thuộc tuyến tính vào trọng lượng của giao dịch, nhưng không phụ thuộc vào số tiền.                                                                                                                                                                                                                             |
| Fiat                                    | Đồng tiền do chính phủ phát hành không được bảo chứng bởi một hàng hóa như vàng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Finite                                  | Ám chỉ nguồn cung Bitcoin được giới hạn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Fork                                    | Sự thay đổi đối với một giao thức hoặc một đoạn mã. Fork thường được giới thiệu để nâng cấp một dự án. Trong cộng đồng mã nguồn mở, fork tồn tại bởi vì nhiều cá nhân chọn tải xuống và chạy cùng một phần mềm vào các thời điểm khác nhau và không phải lúc nào cũng cập nhật. Nếu hai người dùng tải xuống và chạy phiên bản 1 của một phần mềm, và chỉ một người dùng nâng cấp khi phiên bản 2 được phát hành, người dùng đã cập nhật đang chạy một fork của phiên bản 1.                                                                                                                                                                                                                                                                                                                                            |
| Funding Transaction                     | Giao dịch được sử dụng để mở một kênh thanh toán. Giá trị (bằng bitcoin) của giao dịch tài trợ chính xác là khả năng của kênh thanh toán. Đầu ra của giao dịch tài trợ là một kịch bản chữ ký đa dạng 2-trong-2 (multisig) nơi mỗi đối tác kênh kiểm soát một khóa. Do bản chất multisig của nó, nó chỉ có thể được chi tiêu bằng sự đồng thuận giữa các đối tác kênh. Nó cuối cùng sẽ được chi tiêu bởi một trong các giao dịch cam kết hoặc bởi giao dịch đóng.                                                                                                                                                                                                                                                                                                                                                       |
| Fungible                                | Là cái gì đó (như tiền tệ hoặc hàng hóa) có tính chất đến mức một phần hoặc lượng nhất định có thể được thay thế bằng một phần hoặc lượng bằng nhau trong việc thanh toán nợ hoặc giải quyết một tài khoản                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Gap Limit                               | Ám chỉ số lượng địa chỉ công cộng tiêu chuẩn được kiểm tra để tìm giao dịch trong blockchain nhằm tính toán số dư của một tài khoản. Giao dịch nhận được trên một địa chỉ vượt quá giới hạn khoảng cách địa chỉ không được phát hiện.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Genesis Block                           | Khối đầu tiên trong chuỗi khối Bitcoin. Satoshi Nakamoto, người tạo ra Bitcoin, đã khai thác khối Genesis vào ngày 3 tháng 1 năm 2009 và đã bao gồm tiêu đề của Financial Times ngày hôm đó, “Chancellor on brink of second bailout for banks.”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Github                                  | Một nền tảng và dịch vụ dựa trên đám mây cho phát triển phần mềm và kiểm soát phiên bản sử dụng Git, cho phép các nhà phát triển lưu trữ và quản lý mã của họ.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Gossip Protocol                         | Các nút LN gửi và nhận thông tin về cấu trúc của Lightning Network thông qua các tin nhắn gossip được trao đổi với các đối tác. Giao thức gossip chủ yếu được định nghĩa trong BOLT #7 và định nghĩa định dạng của các tin nhắn node_announcement, channel_announcement, và channel_update. Để ngăn chặn spam, tin nhắn thông báo nút chỉ được chuyển tiếp nếu nút đã có một kênh, và tin nhắn thông báo kênh chỉ được chuyển tiếp nếu giao dịch tài trợ của kênh đã được xác nhận bởi mạng Bitcoin. Thông thường, các nút Lightning kết nối với các đối tác kênh của họ, nhưng cũng có thể kết nối với bất kỳ nút Lightning nào khác để xử lý tin nhắn gossip.                                                                                                                                                         |
| Gresham's Law                           | Luật nói rằng “tiền xấu đẩy tiền tốt ra khỏi lưu thông”. Nói cách khác, trong một nền kinh tế nơi hai loại tiền tệ được sử dụng, cá nhân sẽ chi tiêu tiền xấu, loại tiền này liên tục mất giá, và giữ tiền tốt, loại tiền giữ được giá trị của mình. Do đó, tiền xấu sẽ chiếm ưu thế về mặt lưu thông và sử dụng trong các giao dịch hàng ngày, trong khi tiền tốt sẽ chiếm ưu thế về mặt tiết kiệm và đầu tư dài hạn.                                                                                                                                                                                                                                                                                                                                                                                                  |
| Halving                                 | Sự kiện giảm tỷ lệ phát hành bitcoin đi một nửa sau mỗi 210,000 khối (khoảng bốn năm).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Hard Fork                               | Sự thay đổi đồng thuận không tương thích ngược. Tính không tương thích ngược xảy ra khi một hành vi trước đây không hợp lệ được chấp nhận là hợp lệ. Để duy trì đồng thuận qua một hard fork, tất cả các nút đều phải nâng cấp. Nếu không, các nút cũ sẽ từ chối giao dịch hoặc khối dưới quy tắc cũ, trong khi các nút đã nâng cấp sẽ chấp nhận chúng là hợp lệ. Vì lý do này, hard fork được tránh bằng mọi giá trong Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                        |
| Hardware Wallet (HWW)                   | Một loại ví Bitcoin đặc biệt lưu trữ khóa riêng của người dùng trong một thiết bị phần cứng an toàn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Hash Function                           | Một hàm băm mật mã là một thuật toán toán học ánh xạ dữ liệu kích thước tùy ý thành một chuỗi bit có kích thước cố định (một băm) và được thiết kế để là một hàm một chiều, tức là, một hàm không thể đảo ngược. Cách duy nhất để tái tạo dữ liệu đầu vào từ đầu ra của một hàm băm mật mã lý tưởng là thử nghiệm tìm kiếm vét cạn các đầu vào có thể để xem chúng có tạo ra kết quả khớp không.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Hash Rate                               | Một đo lường về số lượng băm mà các thợ mỏ tạo ra mỗi giây trên mạng Bitcoin. Một băm đơn lẻ là một nỗ lực tạo ra Bằng chứng Công việc cho một khối.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Hot Wallet                              | Một thiết bị có kết nối bên ngoài, đặc biệt là kết nối internet. Một hot wallet là một ví Bitcoin kết nối với internet. Những ví này tiện lợi hơn cho việc chi tiêu hàng ngày, nhưng không an toàn bằng các lựa chọn lưu trữ lạnh vì chúng tương tác với internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Initial Block Download (IBD)            | Quá trình xây dựng toàn bộ blockchain Bitcoin từ đầu. Khi một nút mới được thiết lập và tham gia vào mạng, nó kết nối với các nút khác và yêu cầu họ gửi các khối. Nút mới này xử lý các khối này và xây dựng blockchain cho đến khi nó bắt kịp và đồng bộ với mạng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Invoice                                 | Một tài liệu thương mại do người bán phát hành cho người mua liên quan đến một giao dịch bán hàng và chỉ ra các sản phẩm, số lượng, và giá đã thỏa thuận cho các sản phẩm hoặc dịch vụ mà người bán đã cung cấp cho người mua.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Know Your Customer (KYC)                | Các luật nhằm ngăn chặn việc sử dụng các tổ chức tài chính cho việc chuyển tiền bất hợp pháp bằng cách yêu cầu tất cả các tài khoản tài chính phải được xác định cho cá nhân hoặc tổ chức.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Layer 2                                 | Một mạng được xây dựng trên cơ sở một blockchain, ví dụ, Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Legacy Address                          | Địa chỉ legacy sử dụng Base58, và khi một địa chỉ legacy là băm của một khóa công khai, một địa chỉ P2PKH, nó bắt đầu bằng ‘1’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Lightning Network                       | Một giao thức trên Bitcoin. Nó tạo ra một mạng của các kênh thanh toán cho phép chuyển tiền không cần tin cậy qua mạng với sự giúp đỡ của HTLCs và onion routing. Các thành phần khác của Lightning Network bao gồm giao thức gossip, tầng vận chuyển, và yêu cầu thanh toán.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Liquidity                               | Đo lường một số đặc điểm của sổ lệnh của một tài sản cụ thể trong một thị trường nhất định. Liquidity là một chỉ số cho biết ảnh hưởng của một lệnh lớn đến giá của một tài sản sẽ như thế nào. Một tài sản có liquidity cao có độ sâu sổ lệnh lớn hơn. Điều này có nghĩa là nó có thể hấp thụ nhiều lệnh hơn với sự biến động giá nhỏ hơn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Chuỗi Dài Nhất                          | Chuỗi các khối mất nhiều công sức nhất để xây dựng. Được đặt tên như vậy vì theo trực giác, một blockchain có nhiều khối hơn sẽ mất nhiều năng lượng hơn để xây dựng so với một chuỗi có ít khối hơn, nhưng chính xác hơn, đó là chuỗi đòi hỏi nhiều công việc hơn để sản xuất, vì vậy một tên tốt hơn có thể là "chuỗi nặng nhất."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Chuỗi Chính                             | Trong bối cảnh của Lightning Network, đây là mạng lưới Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Phương Tiện Trao Đổi                    | Một loại hàng hóa giúp tạo điều kiện cho việc trao đổi các hàng hóa và dịch vụ khác trong một nền kinh tế. Trong lịch sử, các vật phẩm như vỏ sò, hạt, và vàng đã được sử dụng như một phương tiện trao đổi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Mempool                                 | Viết tắt của "memory pool," là nơi lưu trữ tạm thời cho các giao dịch đã được một nút nhận.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Thợ Mỏ                                  | Một nút tham gia vào quá trình xây dựng blockchain bằng cách thêm các khối mới thông qua quá trình băm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Đào Mỏ                                  | Quá trình xây dựng một khối từ các giao dịch Bitcoin gần đây và sau đó giải quyết một vấn đề tính toán được yêu cầu như bằng chứng công việc. Đây là quá trình mà qua đó sổ cái bitcoin chung (tức là, blockchain Bitcoin) được cập nhật và qua đó các giao dịch mới được bao gồm trong sổ cái. Đây cũng là quá trình mà qua đó bitcoin mới được phát hành. Mỗi khi một khối mới được tạo ra, nút đào mỏ sẽ nhận được bitcoin mới được tạo trong giao dịch coinbase của khối đó.                                                                                                                                                                                                                                                                                                                                        |
| Đa Chữ Ký (multisig)                    | Một script yêu cầu nhiều hơn một chữ ký để ủy quyền chi tiêu. Các kênh thanh toán luôn được mã hóa dưới dạng địa chỉ multisig yêu cầu một chữ ký từ mỗi đối tác của kênh thanh toán. Trong trường hợp tiêu chuẩn của một kênh thanh toán hai bên, một địa chỉ multisig 2-trong-2 được sử dụng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Nút                                     | Một máy tính tham gia vào một mạng lưới. Cụ thể là mạng lưới Bitcoin hoặc Lightning.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Output                                  | Gói bitcoins được tạo trong một giao dịch bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Khóa Output                             | Một tập hợp các yêu cầu đặt ra cho một output. Các yêu cầu này phải được đáp ứng để có thể sử dụng output trong một giao dịch. Ví dụ phổ biến nhất là yêu cầu đơn giản về việc có khóa riêng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Địa Chỉ P2SH                            | Địa chỉ P2SH là mã hóa Base58Check của hash 20-byte của một script. Địa chỉ P2SH bắt đầu bằng "3." Địa chỉ P2SH ẩn tất cả sự phức tạp, sao cho người gửi một khoản thanh toán không thấy script.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Địa Chỉ P2WPKH                          | Định dạng địa chỉ "native SegWit v0", địa chỉ P2WPKH được mã hóa bech32 và bắt đầu bằng "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Địa Chỉ P2WSH                           | Định dạng địa chỉ script "native Segwit v0", địa chỉ P2WSH được mã hóa bech32 và bắt đầu bằng "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Giao Dịch Bitcoin Đã Ký Một Phần (PSBT) | Một tiêu chuẩn Bitcoin giúp tạo điều kiện cho việc di chuyển giao dịch chưa ký, cho phép nhiều bên dễ dàng ký cùng một giao dịch. Điều này rất hữu ích khi nhiều bên muốn thêm input vào cùng một giao dịch. PSBT được giới thiệu bởi BIP 174, và cho phép người dùng dễ dàng hơn trong việc ký giao dịch trên một thiết bị lưu trữ lạnh và sau đó phát sóng giao dịch đã ký từ một thiết bị kết nối với internet.                                                                                                                                                                                                                                                                                                                                                                                                      |
| Tìm Đường                               | Quá trình tìm kiếm một lộ trình cho việc thanh toán từ nguồn đến điểm đến trong Mạng Lưới Lightning.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Pay-to-Public-Key-Hash (P2PKH)          | P2PKH là một loại đầu ra khóa bitcoin vào hash của một khóa công khai. Một đầu ra được khóa bởi một script P2PKH có thể được mở khóa (chi tiêu) bằng cách trình bày khóa công khai phù hợp với hash và chữ ký số được tạo bởi khóa riêng tương ứng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Pay-to-Script-Hash (P2SH)               | P2SH là một loại đầu ra linh hoạt cho phép sử dụng các Bitcoin Scripts phức tạp. Với P2SH, script phức tạp chi tiết các điều kiện để chi tiêu đầu ra (redeem script) không được trình bày trong script khóa. Thay vào đó, giá trị được khóa vào hash của một script, script này phải được trình bày và thỏa mãn để chi tiêu đầu ra.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Pay-to-Taproot (P2TR)                   | Được kích hoạt vào tháng 11 năm 2021, Taproot là một loại đầu ra mới khóa bitcoin vào một cây của các điều kiện chi tiêu, hoặc một điều kiện gốc duy nhất.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Pay-to-Witness-Public-Key-Hash (P2WPKH) | P2WPKH là phiên bản SegWit của P2PKH, sử dụng một chứng nhân tách biệt. Chữ ký để chi tiêu một đầu ra P2WPKH được đặt trong cây chứng nhân thay vì trường ScriptSig.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Pay-to-Witness-Script-Hash (P2WSH)      | P2WSH là phiên bản SegWit của P2SH, sử dụng một chứng nhân tách biệt. Chữ ký và script để chi tiêu một đầu ra P2WSH được đặt trong cây chứng nhân thay vì trường ScriptSig.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Payjoin                                 | Một loại giao dịch Bitcoin đặc biệt nơi cả người gửi và người nhận đều đóng góp đầu vào để phá vỡ giả định sở hữu đầu vào chung, một giả định được sử dụng để loại bỏ quyền riêng tư của người dùng bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Kênh Thanh Toán                         | Một mối quan hệ tài chính giữa hai nút trên Mạng Lưới Lightning, được tạo ra bằng cách sử dụng một giao dịch bitcoin thanh toán cho một địa chỉ đa chữ ký. Các đối tác kênh có thể sử dụng kênh để gửi bitcoin qua lại cho nhau mà không cần phải ghi lại tất cả các giao dịch lên blockchain Bitcoin. Trong một kênh thanh toán điển hình chỉ có hai giao dịch, giao dịch tài trợ và giao dịch cam kết, được thêm vào blockchain. Các khoản thanh toán được gửi qua kênh không được ghi lại trong blockchain và được cho là xảy ra "ngoài chuỗi."                                                                                                                                                                                                                                                                      |
| Yêu Cầu Thanh Toán                      | Một tính năng cho phép chủ cửa hàng BTCPay tạo hóa đơn lâu dài. Các khoản tiền thanh toán cho một yêu cầu thanh toán sử dụng tỷ giá hối đoái tại thời điểm thanh toán. Điều này cho phép người dùng thực hiện các khoản thanh toán theo sự tiện lợi của họ mà không cần phải thương lượng hoặc xác minh tỷ giá hối đoái với chủ cửa hàng tại thời điểm thanh toán.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Thanh Toán                              | Chức năng thanh toán được liên kết với Pull Payments. Tính năng này cho phép bạn xử lý thanh toán kéo (hoàn tiền, thanh toán lương, hoặc rút tiền).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Plugin                                  | Một phần mềm bổ sung được cài đặt trên một chương trình, tăng cường khả năng của nó.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Điểm Bán Hàng (PoS)                     | Một plugin mặc định của BTCPay Server cho phép chủ cửa hàng tạo một cửa hàng trực tuyến trực tiếp từ BTCPay Server. Chủ cửa hàng không cần bất kỳ giải pháp thương mại điện tử bên thứ ba nào để vận hành một cửa hàng trực tuyến.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Di động                                 | Khả năng của một hàng hóa được vận chuyển dễ dàng qua không gian. Tính di động là một đặc điểm quan trọng của tiền tệ tốt; để một loại tiền được chấp nhận rộng rãi, và do đó có thể sử dụng, nó phải có thể di chuyển qua biên giới, giữa các cá nhân, và qua những khoảng cách dài một cách tương đối dễ dàng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Proof Of Work (PoW)                     | Dữ liệu yêu cầu tính toán đáng kể để tìm ra, và có thể được dễ dàng xác minh bởi bất kỳ ai để chứng minh lượng công việc đã được yêu cầu để sản xuất nó. Trong Bitcoin, các miner phải tìm ra một giải pháp số cho thuật toán SHA-256 phù hợp với một mục tiêu chung của mạng, gọi là mục tiêu khó khăn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Pseudonym                               | Một tên giả được cá nhân sử dụng để bảo vệ danh tính của họ hoặc xây dựng danh tiếng riêng biệt từ danh tính thực của họ. Khóa công khai được sử dụng để cho phép người dùng Bitcoin nhận bitcoin trong khi vẫn giữ ẩn danh với blockchain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Public-Key Cryptography                 | Bao gồm một cặp khóa được biết đến là khóa công khai và khóa riêng tư, liên quan đến một thực thể cần xác thực danh tính của mình điện tử hoặc để ký hoặc mã hóa dữ liệu. Khóa công khai được công bố và khóa riêng tư tương ứng được giữ bí mật. Dữ liệu được mã hóa bằng khóa công khai chỉ có thể được giải mã bằng khóa riêng tư tương ứng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Public/Private Key                      | Cặp khóa được sử dụng trong mã hóa khóa công khai. Khóa công khai được chia sẻ với người khác một cách công khai, và có thể được coi là một số tài khoản, trong khi khóa riêng tư được giữ bí mật và có thể được coi là một mật khẩu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Pull Payment                            | Truyền thống, để thực hiện một khoản thanh toán Bitcoin, người nhận chia sẻ địa chỉ bitcoin của họ và sau đó người gửi gửi tiền đến địa chỉ này. Hệ thống như vậy được gọi là thanh toán đẩy vì người gửi khởi xướng việc thanh toán trong khi người nhận có thể không có mặt, thực tế đẩy khoản thanh toán cho người nhận. Thay vì kịch bản điển hình của người gửi "đẩy" khoản thanh toán, người gửi cho phép người nhận kéo khoản thanh toán vào thời điểm người nhận thấy phù hợp.                                                                                                                                                                                                                                                                                                                                  |
| Rabbit Hole                             | Một tham chiếu đến Alice In Wonderland nơi người hùng bắt đầu một cuộc phiêu lưu bằng cách nhập vào một lỗ thỏ. Trong Bitcoin, nó ám chỉ những chủ đề dường như không bao giờ kết thúc mà một người khám phá và thấy trong một ánh sáng mới một khi họ đã bắt đầu hiểu về Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Receive                                 | Quá trình nhận bitcoin được gửi đến địa chỉ được cung cấp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Register                                | Quá trình tạo một tài khoản hoặc đăng ký dịch vụ thường được thực hiện bằng cách chọn một tên người dùng và mật khẩu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Replace By Fee (RBF)                    | Một giao dịch Bitcoin có thể được chỉ định là RBF để cho phép người gửi thay thế giao dịch này bằng một giao dịch tương tự khác trả phí cao hơn. Cơ chế này tồn tại để cho phép người dùng phản ứng nếu mạng trở nên tắc nghẽn và phí tăng đột ngột.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Repository                              | Trong các hệ thống kiểm soát phiên bản, một repository là một cấu trúc dữ liệu lưu trữ metadata cho một tập hợp các tệp hoặc cấu trúc thư mục. Tùy thuộc vào việc hệ thống kiểm soát phiên bản đang sử dụng là phân tán, như Git hoặc Mercurial, hay tập trung, như Subversion, CVS, hoặc Perforce, toàn bộ thông tin trong repository có thể được sao chép trên hệ thống của mỗi người dùng hoặc được duy trì trên một máy chủ duy nhất. Một số metadata mà một repository chứa bao gồm, trong số các thứ khác, một bản ghi lịch sử của các thay đổi trong repository, một tập hợp các đối tượng commit, và một tập hợp các tham chiếu đến các đối tượng commit, gọi là heads.                                                                                                                                         |
| Rescan                                  | Quá trình quét lại trạng thái hiện tại của bộ UTXO để tìm kiếm các đồng tiền thuộc về một lược đồ phái sinh đã được cấu hình trước.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Revokation Key                          | Mỗi Hợp đồng Chuỗi Độ Trưởng Thời gian Có thể Thu hồi (RSMC) chứa hai khóa thu hồi. Mỗi đối tác kênh biết một khóa thu hồi. Biết cả hai khóa thu hồi, đầu ra của RSMC có thể được chi tiêu trong khoảng thời gian đã định trước. Trong quá trình thương lượng trạng thái kênh mới, các khóa thu hồi cũ được chia sẻ, từ đó "thu hồi" trạng thái cũ. Khóa thu hồi được sử dụng để ngăn chặn các đối tác kênh phát sóng trạng thái kênh cũ.                                                                                                                                                                                                                                                                                                                                                                               |
| Routing                                 | Quá trình sử dụng đường dẫn của Lightning Network để thực hiện thanh toán.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Routing Fees                            | Trong Lightning Network, phí được tính cho việc chuyển tiếp thanh toán của người dùng khác. Các nút cá nhân có thể thiết lập chính sách phí của riêng mình, được tính là tổng của một base_fee cố định và một fee_rate tùy thuộc vào số tiền thanh toán.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Salability                              | Khả năng dễ dàng bán một hàng hóa trên thị trường bất cứ khi nào người nắm giữ mong muốn, với tổn thất ít nhất về giá của nó.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Satoshi (sat)                           | Satoshi là đơn vị nhỏ nhất (đơn vị tiền tệ) của bitcoin có thể được ghi lại trên blockchain. Một satoshi bằng 1/100 triệu (0.00000001) bitcoin và được đặt theo tên của người tạo ra Bitcoin, Satoshi Nakamoto.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Satoshi Nakamoto                        | Tên được sử dụng bởi cá nhân hoặc nhóm người đã thiết kế Bitcoin và tạo ra bản triển khai tham chiếu ban đầu của nó. Là một phần của việc triển khai, họ cũng đã phát minh ra cơ sở dữ liệu blockchain đầu tiên. Trong quá trình đó, họ là người đầu tiên giải quyết vấn đề chi tiêu gấp đôi cho tiền tệ số. Danh tính thực sự của họ vẫn còn là một bí ẩn.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Satoshi Per Byte                        | Đơn vị đo độ ưu tiên của giao dịch, được xác định bởi phí giao dịch bằng satoshi chia cho kích thước của giao dịch bằng byte.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Satoshi Per Verabyte                    | Khái niệm tương tự như Satoshi Per Byte, nhưng dành cho địa chỉ mới sử dụng Segwit. Bằng với kích thước giao dịch tính bằng đơn vị Trọng lượng chia cho 4. Đơn vị Trọng lượng được tính bằng cách lấy kích thước giao dịch (không bao gồm chứng từ) nhân với 3, cộng với kích thước giao dịch bao gồm chứng từ.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Scarcity                                | Tính chất của một hàng hóa không thể được sao chép mà không tốn kém. Sự khan hiếm không phụ thuộc vào số lượng đơn vị hiện có của một hàng hóa, mà phụ thuộc vào chi phí để sản xuất thêm đơn vị.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Script                                  | Bitcoin sử dụng một hệ thống kịch bản cho giao dịch gọi là Bitcoin Script. Giống như ngôn ngữ lập trình Forth, nó đơn giản, dựa trên stack và được xử lý từ trái sang phải. Nó cố ý không hoàn chỉnh Turing, không có vòng lặp hay đệ quy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Seed Phrase                             | Một danh sách các từ lưu trữ tất cả thông tin cần thiết để khôi phục quỹ Bitcoin trên chuỗi. Phần mềm ví thường tạo ra một cụm từ hạt giống và hướng dẫn người dùng viết nó ra giấy. Nếu máy tính của người dùng hỏng hoặc ổ cứng bị hỏng, họ có thể tải lại phần mềm ví tương tự và sử dụng bản sao giấy để lấy lại bitcoin của mình.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Segregated Witness (SegWit)             | Segregated Witness (SegWit) là một nâng cấp của giao thức Bitcoin được giới thiệu vào năm 2017, bổ sung một trường chứng nhận mới cho chữ ký và các bằng chứng ủy quyền giao dịch khác. Trường chứng nhận mới này được miễn từ việc tính toán ID giao dịch, giải quyết hầu hết các loại biến đổi giao dịch bởi bên thứ ba. Segregated Witness được triển khai dưới dạng một soft fork và là một thay đổi kỹ thuật làm cho quy tắc giao thức của Bitcoin trở nên hạn chế hơn.                                                                                                                                                                                                                                                                                                                                            |
| Self-Sovereignty                        | Một mô hình quản lý danh tính số mà trong đó cá nhân hoặc doanh nghiệp có quyền sở hữu độc lập đối với khả năng kiểm soát tài khoản và dữ liệu cá nhân của họ.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Send                                    | Quá trình chuyển bitcoin đến một địa chỉ.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Sensitivity Mode                        | Được kích hoạt qua một nút chuyển đổi trong cài đặt cửa hàng, kích hoạt làm cho các giá trị số (ví dụ, số lượng bitcoin) bị ẩn đi trong tất cả các giao diện.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Server Settings                         | Cài đặt trong BTCPay Server áp dụng cho toàn bộ máy chủ (khác với Store Settings chỉ áp dụng cho một cửa hàng duy nhất).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SHA-256                                 | Một hàm băm mật mã. Là một thành viên của gia đình hàm băm Secure Hashing Algorithm (SHA).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Shopify                                 | Một công ty đa quốc gia về thương mại điện tử có trụ sở tại Ottawa, Ontario, Canada. Shopify là tên của nền tảng thương mại điện tử độc quyền của họ cho các cửa hàng trực tuyến và hệ thống bán lẻ tại điểm bán hàng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| SMTP                                    | Simple Mail Transfer Protocol là một giao thức truyền thông tiêu chuẩn của Internet dành cho việc truyền tải thư điện tử.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Soft Fork                               | Một nâng cấp giao thức tương thích với phiên bản cũ và mới, cho phép cả node cũ và node mới tiếp tục sử dụng cùng một chuỗi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Software Stack                          | Trong lĩnh vực máy tính, một solution stack hoặc software stack là một tập hợp các hệ thống phụ trợ hoặc thành phần phần mềm cần thiết để tạo ra một nền tảng hoàn chỉnh sao cho không cần thêm phần mềm nào khác để hỗ trợ các ứng dụng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Store                                   | Một cửa hàng trong BTCPay Server có thể được coi là "Nhà" của một ví bitcoin cụ thể, mở rộng với tất cả các tính năng của BTCPay Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Store Settings                          | Cài đặt trong BTCPay Server đặc biệt cho một cửa hàng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Taproot                                 | Nâng cấp cho Bitcoin sẽ giới thiệu một số tính năng mới. Nâng cấp được mô tả trong các BIPs 340, 341, và 342, và giới thiệu lược đồ chữ ký Schnorr, Taproot, và Tapscript. Cùng nhau, những nâng cấp này giới thiệu các cách mới, hiệu quả hơn, linh hoạt hơn, và riêng tư hơn trong việc chuyển giao bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Thier's Law                             | Luật nói rằng tiền tốt sẽ đẩy tiền xấu ra khỏi lưu thông.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Third-Party Host                        | Khi một trang web của cá nhân hoặc công ty được vận hành trên máy chủ thuộc sở hữu và quản lý của một doanh nghiệp khác. Lựa chọn khác là tự bạn lưu trữ trang web trên máy chủ của mình trong trung tâm dữ liệu của mình.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Timelock                                | Một loại ràng buộc ngăn cản việc chi tiêu một số bitcoin cho đến một thời điểm hoặc độ cao khối cụ thể trong tương lai. Timelock đóng vai trò quan trọng trong nhiều hợp đồng Bitcoin, bao gồm các kênh thanh toán và HTLCs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Topology                                | Topology của Lightning Network mô tả hình dạng của Lightning Network như một đồ thị toán học. Các nút của đồ thị là các nút Lightning (người tham gia/máy chủ ngang hàng trong mạng). Các cạnh của đồ thị là các kênh thanh toán. Topology của Lightning Network được công bố công khai nhờ vào giao thức gossip, ngoại trừ các kênh không được công bố. Điều này có nghĩa là Lightning Network có thể lớn hơn nhiều so với số lượng kênh và nút được công bố. Việc biết topology đặc biệt quan trọng trong quá trình định tuyến dựa trên nguồn của các giao dịch thanh toán, trong đó người gửi tìm ra một lộ trình.                                                                                                                                                                                                   |
| Transaction                             | Giao dịch là các cấu trúc dữ liệu được Bitcoin sử dụng để chuyển bitcoin từ một địa chỉ này sang địa chỉ khác. Hàng ngàn giao dịch được tổng hợp trong một khối, sau đó được ghi (đào) lên blockchain. Giao dịch đầu tiên trong mỗi khối, gọi là giao dịch coinbase, tạo ra bitcoin mới.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Transaction ID                          | Một chuỗi các chữ cái và số lượng xác định một giao dịch cụ thể trên blockchain. Chuỗi này đơn giản là băm SHA-256 kép của một giao dịch. Băm này có thể được sử dụng để tra cứu một giao dịch trên một nút hoặc trình duyệt khối.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Two Factor Authentication (2FA)         | Phương pháp bảo mật quản lý danh tính và truy cập yêu cầu hai hình thức xác thực để truy cập vào tài nguyên và dữ liệu, thường kèm theo một thiết bị phụ bên cạnh mật khẩu đăng nhập tiêu chuẩn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Uncensorable                            | Tính chất mà không có thực thể nào có khả năng đảo ngược một giao dịch Bitcoin hoặc đưa một ví hoặc địa chỉ vào danh sách đen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Unconfiscatable                         | Tính chất mà không có thực thể nào có thể lấy bitcoin từ một thực thể khác mà không có sự đồng ý của họ.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Unspent Transaction Outputs (UTXO)      | Các đầu ra chưa được tiêu, do đó có sẵn để được sử dụng trong các giao dịch mới.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| User Experience (UX)                    | Cách một người dùng tương tác và trải nghiệm một sản phẩm, hệ thống hoặc dịch vụ. Nó bao gồm nhận thức của một người về tính hữu ích, dễ sử dụng và hiệu quả.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| User Interface (UI)                     | Điểm của tương tác và giao tiếp giữa con người và máy tính trong một thiết bị.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Vefitiable                              | Tính chất của một hàng hóa có thể dễ dàng phân biệt với hàng giả mạo và hàng nhái.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Virtual                                 | Tồn tại trên hoặc được mô phỏng trên máy tính hoặc mạng máy tính.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Virtual machine (VM)                    | Trong lĩnh vực máy tính, máy ảo là sự ảo hóa hoặc mô phỏng của một hệ thống máy tính. Máy ảo dựa trên kiến trúc máy tính và cung cấp chức năng của một máy tính vật lý. Các triển khai của chúng có thể liên quan đến phần cứng chuyên dụng, phần mềm, hoặc sự kết hợp của cả hai.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Virtual Private Server                  | Một máy chủ ảo riêng là một máy ảo được bán dưới dạng dịch vụ bởi một dịch vụ lưu trữ Internet. Thuật ngữ "máy chủ ảo dành riêng" cũng có ý nghĩa tương tự. Một máy chủ ảo riêng chạy bản sao của hệ điều hành riêng, và khách hàng có thể có quyền truy cập cấp độ superuser đối với thể hiện hệ điều hành đó, vì vậy họ có thể cài đặt gần như bất kỳ phần mềm nào chạy trên hệ điều hành đó.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Volatility                              | Đo lường mức độ biến động của giá tài sản theo thời gian. Các tài sản trải qua những thay đổi lớn về giá một cách thường xuyên có tính biến động cao, trong khi các tài sản có giá ổn định hơn có tính biến động thấp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Ví                                      | Ví Bitcoin giữ chìa khóa của người dùng, cho phép người dùng nhận bitcoin, ký giao dịch và kiểm tra số dư tài khoản của họ. Chìa khóa riêng và chìa khóa công khai được giữ trong ví Bitcoin đảm nhận hai chức năng riêng biệt nhưng được liên kết với nhau khi tạo ra. Ví Bitcoin chứa chìa khóa của người dùng, không phải bitcoin thực sự của họ. Về mặt khái niệm, ví giống như một móc khóa trong ý nghĩa nó giữ nhiều cặp chìa khóa riêng và công khai. Những chìa khóa này được sử dụng để ký giao dịch, cho phép người dùng chứng minh họ sở hữu các đầu ra giao dịch trên blockchain, tức là bitcoin của họ. Tất cả bitcoin được ghi lại trên blockchain dưới dạng đầu ra giao dịch.                                                                                                                           |
| Wasabi Wallet                           | Một ví Bitcoin tập trung vào quyền riêng tư, mã nguồn mở, không giữ tiền cho Desktop thực hiện CoinJoin không cần tin cậy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Ví Chỉ Xem                              | Ví Bitcoin cho phép bạn theo dõi bitcoin của mình trong lưu trữ lạnh mà vẫn vô hiệu hóa khả năng chi tiêu quỹ. Điều này là bởi vì ví chỉ xem không lưu trữ hoặc sử dụng chìa khóa riêng và do đó không thể ủy quyền bất kỳ khoản chi tiêu nào thay mặt cho người dùng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Whale (Cá Voi)                          | Trong bối cảnh của Bitcoin, một cá voi là người nắm giữ một lượng lớn bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| White-Label                             | Một sản phẩm hoặc dịch vụ white-label là sản phẩm hoặc dịch vụ được sản xuất bởi một công ty mà các công ty khác tái thương hiệu để làm cho nó trông như thể họ đã tạo ra nó.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Whitepaper                              | Giới thiệu một ý tưởng mới hoặc chủ đề để thảo luận. Whitepaper Bitcoin giới thiệu Bitcoin như một “Hệ thống tiền mặt điện tử ngang hàng” mà “không cần bên thứ ba đáng tin cậy”. Satoshi Nakamoto phát hành whitepaper vào ngày 31 tháng 10 năm 2008 cho một danh sách email của các nhà mật mã học và cypherpunks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Wrapped Segwit                          | Một triển khai thiết kế được bao gồm trong nâng cấp SegWit nhằm mục đích giúp ví và phần mềm Bitcoin khác dễ dàng hỗ trợ SegWit hơn. Để đạt được điều này, hai kịch bản SegWit gốc, P2WPKH và P2WSH, được sử dụng như là “redeemScript” của một giao dịch P2SH, tạo ra các loại kịch bản SegWit được bọc là P2SH-P2WPKH và P2SH-P2WSH tương ứng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

![image](assets/en/129.webp)
