---
name: Bitcoin và BTCPay Server
goal: Cài đặt BTCPay Server cho doanh nghiệp của bạn
objectives:
  - Hiểu rõ về BTCPay Server.
  - Self-host và cấu hình cho BTCPay Server.
  - Sử dụng BTCPay Server trong hoạt động kinh doanh hàng ngày.
---


# Bitcoin và BTCPay Server

Đây là một khóa học giới thiệu về Cách vận hành của BTCPay Server được viết bởi Alekos và Bas, sau đó được điều chỉnh theo định dạng một khóa học trên Plan ₿ bởi melontwist và asi0.

MỘT CÂU CHUYỆN CHƯA CÓ HỒI KẾT - AN UNFINSHED STORY

"Đây là sự dối trá, niềm tin của tôi dành cho bạn đã bị phá vỡ, tôi sẽ làm cho bạn trở nên lỗi thời". - "This Is Lies, My Trust In You Is Broken, I Will Make You Obsolete".

Sản phẩm của BTCPay Server Foundation

+++

# Giới thiệu

<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>

## Lời ngợi ca dành cho cha đẻ của Bitcoin và cha đẻ của BTCPay Server

<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>

BTCPay Server là gì và nó ra đời từ đâu? Chúng ta hãy bắt đầu từ câu hỏi này. Chúng ta đề cao sự minh bạch và một số tiêu chuẩn nhất định để tạo dựng niềm tin trong không gian Bitcoin.
Một dự án trong lĩnh vực này đã phá vỡ những giá trị này. Nicolas Dorier, nhà phát triển chính của BTCPay Server, đã coi đó là chuyện cá nhân và hứa sẽ làm cho những giá trị đó trở nên lỗi thời. Và sau nhiều năm, chúng ta đang hàng ngày nỗ lực để hướng tới tương lai đó, hoàn toàn mã nguồn mở.

> Đây là sự dối trá, niềm tin của tôi dành cho bạn đã bị phá vỡ, tôi sẽ làm cho bạn trở nên lỗi thời.
> Nicolas Dorier

Sau những lời nói của Nicolas, đã đến lúc bắt đầu xây dựng, kiến tạo. Rất nhiều công sức đã được đổ vào thứ mà chúng ta bây giờ gọi là BTCPay Server. Nhiều người đã hỗ trợ thúc đẩy sáng kiến này. Những người được công nhận nhất là r0ckstardev, MrKukks, Pavlenex, và người bán hàng đầu tiên sử dụng phần mềm này, astupidmoose.

Mã nguồn mở có nghĩa là gì, và điều gì tạo nên một dự án như vậy?

FOSS là viết tắt của Free & Open-Source Software (Phần mềm miễn phí và mã nguồn mở). Cái đầu tiên (Free) ám chỉ các điều khoản cho phép bất kỳ ai cũng có thể sao chép, chỉnh sửa, và thậm chí phân phối các phiên bản của phần mềm (kể cả với mục đích lợi nhuận). Cái sau (Open-Source) ám chỉ việc chia sẻ mã nguồn một cách công khai, khuyến khích công chúng đóng góp và cải thiện nó.
Điều này thu hút những người dùng có kinh nghiệm hứng thú với việc đóng góp vào phần mềm mà họ đã sử dụng và tạo ra giá trị từ đó. Theo thời gian, phần mềm dạng này được chứng minh sẽ chiến thắng về phạm vi áp dụng so với phần mềm độc quyền. Điều này phù hợp với tinh thần của Bitcoin là “thông tin luôn khát khao được tự do”. Nó tập hợp những con người đam mê lại với nhau tạo thành một cộng đồng và đơn giản là tạo ra nhiều niềm vui hơn. Giống như Bitcoin, FOSS là tất yếu.

### Trước khi chúng ta bắt đầu

Khóa học này bao gồm nhiều phần. Nhiều phần sẽ được giáo viên của bạn trong lớp học đảm nhận, môi trường thử nghiệm mà bạn có quyền truy cập vào, một máy chủ được host cho chính bạn, và có thể là một tên miền. Nếu bạn hoàn thành khóa học này một cách độc lập, xin lưu ý rằng các môi trường được ghi nhãn là DEMO sẽ không có sẵn cho bạn.
Lưu ý. Nếu bạn theo dõi khóa học này qua lớp học, tên máy chủ có thể khác nhau tùy thuộc vào cài đặt lớp học của bạn. Các biến trong tên máy chủ có thể khác nhau do điều này.

### Cấu trúc Khóa học

Mỗi chương đều có mục tiêu và đánh giá kiến thức. Trong khóa học này, chúng ta sẽ đề cập đến từng điều này và có một bản tóm tắt các tính năng chính tại mỗi khối bài học (tức là chương). Hình minh họa được sử dụng để cung cấp phản hồi và củng cố các khái niệm chính một cách trực quan. Mục tiêu được đặt ra ngay từ đầu mỗi khối bài học. Những mục tiêu này vượt ra ngoài phạm vi của một danh sách. Chúng cung cấp cho bạn một hướng dẫn để bước vào một bộ kỹ năng mới. Phần đánh giá iến thức ngày càng trở nên thách thức hơn trong việc thiết lập BTCPay Server của bạn.

### Học viên nhận được gì từ khóa học?

Với Khóa học BTCPay Server, học viên có thể hiểu được các nguyên tắc cơ bản, kỹ thuật và phi kỹ thuật của Bitcoin. Được đào tạo chuyên sâu về việc sử dụng Bitcoin thông qua BTCPay Server sẽ cho phép học viên vận hành cơ sở hạ tầng Bitcoin của riêng họ.

### Địa chỉ Web quan trọng hoặc liên hệ

BTCPay Server Foundation, đã cho phép Alekos và Bas viết khóa học này, đặt tại Tokyo, Nhật Bản. Bạn có thể liên hệ với BTCPay Server Foundation thông qua:

- https://foundation.btcpayserver.org
- Tham gia các kênh chat chính thức: https://chat.btcpayserver.org

## Giới thiệu về Bitcoin

<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>

### Hiểu về Bitcoin thông qua một bài tập

Đây là bài tập trong lớp học nên nếu bạn tự tham gia khóa học này, bạn không thể thực hiện nó nhưng bạn vẫn có thể tìm hiểu qua bài tập này. Để hoàn thành nhiệm vụ này, số lượng người tối thiểu là từ 9 đến 11.

Bài tập bắt đầu sau khi xem xong video giới thiệu "Làm thế nào Bitcoin và blockchain hoạt động" của BBC.

![how bitcoin and the blockchain works](https://youtu.be/mhE_vvwAiRc)

Bài tập này yêu cầu ít nhất chín người tham gia. Mục đích của bài tập này là để hiểu trực quan về cách hoạt động của Bitcoin. Bằng cách nhập vào từng vai những thành phần tham gia vào mạng lưới, bạn sẽ có một cách học tương tác và vui vẻ. Bài tập này không liên quan đến Lightning Network.

### Ví dụ; Yêu cầu 9 / 11 người

Các vai trò là:

- 1 Khách hàng - Customer
- 1 Người bán hàng - Merchant
- 7 đến 9 node Bitcoin - Bitcoin Nodes

**Thiết lập trò chơi như sau:**

Khách hàng mua một sản phẩm từ cửa hàng bằng Bitcoin.

**Kịch bản 1 - Hệ thống ngân hàng truyền thống**

- Thiết lập:
  - Xem sơ đồ minh hoạ trong Figjam đính kèm - [Sơ đồ Hoạt động](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Chọn ba học viên tình nguyện đóng các vai Khách hàng (Alice), Người bán hàng (Bob), và Ngân hàng.
- Chuỗi sự kiện diễn ra:
  - Khách hàng - tìm kiếm cửa hàng trực tuyến và tìm thấy một mặt hàng giá $25 mà họ muốn, sau đó thông báo cho Người bán hàng rằng họ muốn mua
  - Người bán hàng- yêu cầu thanh toán.
  - Khách hàng- gửi thông tin thẻ cho Người bán hàng
  - Người bán hàng- chuyển thông tin đến Ngân hàng (xác định cả danh tính của mình và thông tin/danh tính) yêu cầu thanh toán
  - Ngân hàng thu thập thông tin về Khách hàng và Người bán hàng (Alice và Bob) và kiểm tra xem số dư của khách hàng có đủ không.
  - Trừ $25 từ tài khoản của Alice, cộng $24 vào tài khoản của Bob, lấy $1 cho phí dịch vụ
  - Người bán hàng nhận được sự tín hiệu thành công từ Ngân hàng và gửi hàng cho khách hàng.
- Nhận xét:
  - Bob và Alice phải có mối quan hệ với một ngân hàng.
  - Ngân hàng thu thập thông tin định danh về cả Bob và Alice.
  - Ngân hàng lấy một phần của khoản thanh toán làm phí.
  - Ngân hàng phải được tin tưởng để giữ tiền của mỗi người tham gia ở bất cứ thời điểm nào.

**Kịch bản 2 - Hệ thống Bitcoin**

- Thiết lập:
  - Xem sơ đồ minh hoạ trong Figjam đính kèm - [Sơ đồ Hoạt động](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Thay thế Ngân hàng bằng chín sinh viên sẽ đóng vai trò là Máy tính (Các node/Thợ đào Bitcoin) trong mạng lưới.
- Mỗi Máy tính trong số 9 máy này có bản ghi lịch sử đầy đủ về tất cả các giao dịch đã từng được thực hiện (do đó, số dư chính xác mà không có sự giả mạo), cũng như một bộ quy tắc:
  - Xác minh giao dịch được ký đúng cách (chìa khóa phù hợp với ổ khóa)
  - Phát sóng và nhận giao dịch hợp lệ từ các đối tác ngang hàng trong mạng lưới, loại bỏ những giao dịch không hợp lệ (bao gồm cả những giao dịch lặp chi - tiêu một đồng tiền hai lần)
- Cập nhật/Thêm bản ghi định kỳ với các giao dịch mới nhận từ máy tính "ngẫu nhiên" miễn là tất cả nội dung đều hợp lệ (lưu ý: cho đến hiện tại, chúng ta đang bỏ qua phần Bằng chứng công việc - POW để đơn giản hóa), nếu không thì từ chối những giao dịch này và tiếp tục như trước cho đến khi máy tính "ngẫu nhiên" khác gửi một bản cập nhật.
  - Một lượng tiền nhất định sẽ được thưởng cho thợ đào nếu nội dung hợp lệ.
- Tiến trình sự kiện:
  - Khách hàng- tìm kiếm cửa hàng trực tuyến và tìm thấy một mặt hàng trị giá $25 mà họ muốn, sau đó thông báo cho Người bán hàng rằng họ muốn mua
  - Người bán- yêu cầu thanh toán bằng cách gửi khách hàng một hóa đơn/địa chỉ từ ví của họ.
  - Khách hàng- tạo một giao dịch (gửi số BTC trị giá $25 đến địa chỉ do Người bán cung cấp) và phát sóng  giao dịch đó lên mạng lưới Bitcoin.
- Máy tính- nhận giao dịch và xác minh:
  - Địa chỉ ví gửi có ít nhất đủ lượng BTC trị giá $25.
  - Giao dịch được ký đúng cách (“được mở khóa” bởi khách hàng)
  - Nếu không, thì giao dịch sẽ không được lan truyền trên mạng, và nếu có, thì nó sẽ được lan truyền và được giữ ở trạng thái chờ.
  - Người bán có thể kiểm tra rằng giao dịch đang chờ xử lý.
- Một máy tính được chọn “ngẫu nhiên” để xử lý giao dịch được đề xuất bằng cách phát đi “một khối” chứa nó; nếu nó được kiểm tra là hợp lệ, họ sẽ nhận được một phần thưởng theo BTC.
  - TÙY CHỌN/NÂNG CAO - thay vì chọn ngẫu nhiên một Máy tính, mô phỏng việc đào bằng cách yêu cầu các Máy tính lắc xúc xắc cho đến khi một kết quả được xác định từ trước xảy ra (ví dụ: người đầu tiên lắc được đôi sáu là người được chọn)
  - Nó cũng có thể xảy ra trường hợp hai Máy tính chiến thắng cùng một lúc, dẫn đến việc chia tách chuỗi.
  - Các máy tính kiểm tra tính hợp lệ, cập nhật/thêm bản ghi vào sổ cái của họ nếu các quy tắc được đáp ứng, và phát tán khối tới các đối tác.
  - Máy tính được chọn ngẫu nhiên nhận được phần thưởng cho việc đề xuất một khối hợp lệ.
  - Người bán kiểm tra giao dịch đã được hoàn tất; do đó, tiền đã được nhận, và mặt hàng được gửi cho khách hàng.
- Nhận xét:
  - Lưu ý rằng ở kịch bản này chúng ta không cần có mối quan hệ sẵn với ngân hàng.
  - Không cần bên thứ ba để hỗ trợ; thay thế bằng mã/code và các khoản khích lệ.
  - Không có việc thu thập dữ liệu bởi bất kỳ ai ngoài giao dịch trực tiếp và chỉ cần trao đổi số lượng thông tin cần thiết giữa các bên tham gia (ví dụ, địa chỉ giao hàng).
  - Không cần sự tin tưởng giữa các bên (ngoại trừ tin tưởng vào việc Người bán sẽ gửi hàng), giống như một giao dịch tiền mặt theo nhiều cách.
  - Tiền được sở hữu trực tiếp bởi các cá nhân.
  - Sổ cái Bitcoin được biểu diễn bằng đô la cho đơn giản, nhưng thực tế, đơn vị của nó là BTC.
  - Chúng tôi mô phỏng một giao dịch đơn lẻ được phát sóng, nhưng thực tế, có nhiều giao dịch đang chờ xử lý trên mạng lưới Bitcoin, và mỗi khối bao gồm hàng ngàn giao dịch cùng một lúc. Các node cũng kiểm tra để đảm bảo không có giao dịch lặp chi nào đang chờ xử lý.
- Các tình huống gian lận:
  - Nếu khách hàng không có đủ lượng BTC trị giá $25
    - Họ sẽ không thể tạo giao dịch vì “mở khóa” và “sở hữu” là một và cùng một thứ, và máy tính kiểm tra giao dịch được ký đúng cách; nếu không, họ sẽ từ chối nó.
- Nếu máy tính được chọn ngẫu nhiên cố gắng "thay đổi sổ cái"? - Khối sẽ bị từ chối, vì mọi máy tính khác đều có lịch sử đầy đủ và sẽ nhận ra sự thay đổi, vi phạm một trong những quy tắc của họ.
  - Máy tính Ngẫu nhiên sẽ không nhận được phần thưởng, và không có giao dịch nào từ khối của họ được hoàn tất.

## Đánh giá kiến thức

<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>

### Đánh giá kiến thức thảo luận tại lớp học

Thảo luận về một số sự đơn giản hóa được áp dụng trong bài tập tại lớp theo kịch bản thứ hai và mô tả chi tiết hơn về hệ thống Bitcoin thực tế.

### Đánh giá kiến thức ôn tập từ vựng

Định nghĩa các thuật ngữ chính được giới thiệu trong phần trước:

- Node
- Mempool
- Difficulty Target - Mục tiêu độ khó
- Block

**Thảo luận về ý nghĩa của một số thuật ngữ bổ sung:**

Blockchain, Transaction - Giao dịch, Double-Spend - Lặp chi, Byzantine Generals' Problem - Bài toán các vị tướng Byzantine, Mining - Đào coin, Proof of Work (PoW) - Bằng chứng công việc, Hash Function - Hàm băm, Block Reward - Phần thưởng khối, Longest Chain - Chuỗi dài nhất, 51% Attack - Tấn công 51%, Output - Đầu ra, Output Lock - Khoá đầu ra, Change - Tiền thối, Satoshis - Sat, Public/Private Key - Khoá công khai / riêng tư, Address - Địa chỉ, Public-Key Cryptography - Mật mã khoá công khai, Digital Signature - Chữ ký số, Wallet - Ví.

# Giới thiệu về BTCPay Server

<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>

## Hiểu về màn hình đăng nhập BTCPay Server

<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>

### Làm việc với BTCPay Server

Mục tiêu của  bài học này sẽ là hiểu chung về phần mềm BTCPay Server. Trong môi trường chia sẻ, bạn được khuyến khích theo dõi minh họa của giáo viên và bám theo Sổ tay Khóa học BTCPay Server. Bạn sẽ học cách tạo ví qua nhiều phương pháp. Ví dụ bao gồm cài đặt ví nóng (Hot Wallet) và ví phần cứng kết nối qua BTCPay Server Vault. Những điều này diễn ra trong môi trường Demo, được hiển thị và cung cấp quyền truy cập bởi giáo viên khóa học của bạn.

Nếu bạn theo dõi khóa học này một mình, bạn có thể tìm danh sách các máy chủ của bên thứ ba cho mục đích Demo tại https://directory.btcpayserver.org/filter/hosts. Chúng tôi khuyến cáo không sử dụng các tùy chọn của bên thứ ba này làm môi trường kinh doanh sản xuất thực, nhưng chúng phục vụ tốt cho mục đích giới thiệu về việc sử dụng Bitcoin và BTCPay Server.

Là một người mới BTCPay Server, bạn có thể đã có kinh nghiệm thiết lập một node Bitcoin trước đây. Khóa học này sẽ nói cụ thể về các lớp của phần mềm BTCPay Server.

Nhiều tùy chọn trong BTCPay Server tồn tại dưới dạng này hay dạng khác trong các phần mềm liên quan đến ví Bitcoin khác.

### Màn hình đăng nhập BTCPay Server

Khi tới với môi trường thử nghiệm - Demo, bạn được yêu cầu ‘Login - Đăng nhập’ hoặc ‘Create your accounr - Tạo tài khoản mới’. Quản trị viên máy chủ có thể tắt tính năng tạo tài khoản mới vì một số lý do an ninh. Logo và màu sắc của nút BTCPay Server có thể được thay đổi vì BTCPay Server là Phần mềm mã nguồn mở. Một máy chủ của bên thứ ba có thể gán nhãn trắng phần mềm và thay đổi toàn bộ giao diện.

![image](assets/en/0.webp)

### Cửa sổ tạo tài khoản

Tạo tài khoản trên BTCPay Server yêu cầu chuỗi địa chỉ Email hợp lệ; ví dụ example@email.com sẽ là một chuỗi hợp lệ cho Email.

Password - mật khẩu cần ít nhất 8 ký tự, bao gồm chữ cái, số và ký tự. Sau khi thiết lập mật khẩu một lần, bạn sẽ phải xác minh lại mật khẩu (Confirm password) đã nhập để đảm bảo nó chính xác với những gì đã được nhập trong lần đầu tiên.
Khi cả hai trường Email và Mật khẩu đã được điền đúng cách, nhấp vào nút ‘Create account - Tạo tài khoản’. Điều này sẽ lưu Email và mật khẩu trên BTCPay Server thử nghiệm của giáo viên.
![image](assets/en/1.webp)

**!Lưu Ý!**

Nếu bạn tự học khóa học này, có thể bạn sẽ thực hiện việc tạo tài khoản này trên một máy chủ của bên thứ ba; do đó, một lần nữa, chúng tôi nhấn mạnh không bao giờ sử dụng chúng như môi trường sản xuất - kinh doanh thật mà chỉ dùng cho mục đích đào tạo.

### Quản trị viên của BTCPay Server tạo tài khoản

Quản trị viên của BTCPay Server thử nghiệm cũng có thể tạo tài khoản cho BTCPay Server. Quản trị viên của BTCPay Server thử nghiệm có thể nhấp vào ‘Cài đặt máy chủ - Server Settings’ (1), nhấp vào tab ‘Người dùng - Users’ (2), và nhấp vào nút “+ Thêm người dùng - Add User” (3) ở góc trên bên phải của tab Người dùng - User. Trong Mục (4.3), bạn sẽ tìm hiểu thêm về quyền kiểm soát tài khoản của quản trị viên.

![image](assets/en/2.webp)

Là một quản trị viên, bạn sẽ cần địa chỉ Email của người dùng và thiết lập một mật khẩu chuẩn. Là Quản trị viên, bạn nên thông báo cho người dùng rằng họ nên thay đổi mật khẩu này trước khi sử dụng tài khoản vì lý do bảo mật. Nếu Quản trị viên KHÔNG thiết lập Mật khẩu và SMTP đã được thiết lập trên máy chủ, người dùng sẽ nhận được một email với đường link mời để tạo tài khoản và thiết lập mật khẩu của họ.

### Ví Dụ

Khi theo dõi khóa học thông qua sự hướng dẫn của giáo viên, hãy theo đường link do giáo viên cung cấp và tạo tài khoản của bạn trên môi trường Demo được cung cấp. Đảm bảo địa chỉ email và mật khẩu của bạn được lưu một cách an toàn; bạn sẽ cần thông tin đăng nhập này cho phần còn lại của các mục tiêu Demo trong khóa học này.

Giáo viên của bạn có thể đã thu thập địa chỉ email trước và gửi một liên kết mời trước bài tập này. Nếu được hướng dẫn, kiểm tra Email của bạn.

Khi tham gia khóa học mà không có giáo viên, hãy tạo tài khoản của bạn sử dụng môi trường Demo của BTCPay Server; truy cập

https://mainnet.demo.btcpayserver.org/login.

Tài khoản này chỉ nên được sử dụng cho mục đích trình diễn/đào tạo và không bao giờ dùng cho kinh doanh.

### Tóm Tắt Kỹ Năng

Trong phần này, bạn đã học được những điều sau:

- Cách tạo một tài khoản trên máy chủ được lưu trữ thông qua giao diện của nó.
- Cách một quản trị viên máy chủ có thể thêm người dùng thủ công trong cài đặt máy chủ.

### Đánh giá kiến thức

#### Đánh giá kiến thức lý thuyết

Nêu lý do tại sao việc sử dụng Máy chủ Demo cho mục đích sản xuất, kinh doanh thật là một ý tưởng tồi.

## Quản lý tài khoản người dùng

<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>

### Quản lý tài khoản trên BTCPay Server

Sau khi chủ cửa hàng đã tạo tài khoản của họ, họ có thể quản lý nó ở góc dưới bên trái của giao diện người dùng BTCPay Server. Dưới nút Tài khoản - Account, có nhiều cài đặt cấp cao hơn.

- Chế độ sáng / tối.
- Nut chuyển để ẩn thông tin nhạy cảm
- Quản lý tài khoản

![image](assets/en/3.webp)

### Chế độ sáng và tối

Người dùng của BTCPay Server có thể chọn giữa giao diện người dùng ở chế độ tối hoặc sáng. Nội dung và thành phần của các trang sẽ không thay đổi, chỉ là chế độ tối, sáng của nó.

### Nút chuyển để ẩn thông tin nhạy cảm

Nút ẩn thông tin nhạy cảm mang lại một lớp bảo mật nhanh chóng và đơn giản. Bất cứ khi nào bạn cần vận hành BTCPay Server của mình, cũng có thể có người lén nhìn qua vai bạn ở không gian công cộng, hãy bật nút `Hide Sensitive Info` để ẩn các thông tin nhạy vsmt, và tất cả các giá trị, cong số trong BTCPay Server sẽ được ẩn đi. Người ta có thể nhìn qua vai bạn nhưng không thể thấy các giá trị, con số mà bạn đang xử lý.

### Quản lý tài khoản

Một khi tài khoản người dùng đã được tạo, đây là nơi để quản lý mật khẩu, xác thực hai yếu tố (2fa), hoặc khóa API.

### Quản lý tài khoản - Tài khoản

Bạn có thể cập nhật tài khoản của mình bằng địa chỉ Email khác nếu muốn. Để đảm bảo rằng địa chỉ email của bạn chính xác, BTCPay Server cho phép bạn gửi một email xác nhận. Nhấn lưu nếu người dùng thiết lập một địa chỉ email mới và xác nhận việc xác minh thành công. Tên đăng nhập vẫn giữ nguyên như địa chỉ Email trước đó.

Người dùng có thể quyết định xóa toàn bộ tài khoản của mình. Điều này có thể được thực hiện bằng cách nhấn vào nút `Delete Account - Xoá tài khoản` trên tab Tài khoản.

![image](assets/en/4.webp)

**!Lưu ý!**

Sau khi thay đổi Email, tên đăng nhập cho tài khoản sẽ không thay đổi. Địa chỉ Email được cung cấp trước đó sẽ vẫn là tên đăng nhập.

### Quản lý tài khoản - Mật khẩu

Sinh viên có thể muốn thay đổi mật khẩu của mình. Anh ta có thể làm điều này bằng cách đi tới tab `Password - Mật khẩu`. Tại đây, anh ta cần phải nhập mật khẩu cũ và có thể thay đổi thành một mật khẩu mới.

![image](assets/en/5.webp)

### Xác thực hai yếu tố (2fa)

Để hạn chế hậu quả của việc mất cắp mật khẩu, bạn có thể sử dụng xác thực hai yếu tố (2fa), một phương pháp bảo mật tương đối mới. Bạn có thể kích hoạt xác thực hai yếu tố thông qua Quản lý tài khoản và tab xác thực hai yếu tố. Bạn phải hoàn thành một bước xác thực thứ hai sau khi đăng nhập bằng tên đăng nhập và mật khẩu của mình.

BTCPay Server cho phép hai cách kích hoạt 2FA, 2FA dựa trên ứng dụng (Authy, Google, Microsoft authenticators) hoặc thông qua Thiết bị bảo mật (FIDO2 hoặc LNURL Auth).

### Xác thực hai yếu tố (2fa) - Dựa trên ứng dụng

Tuỳ vào Hệ điều hành điện thoại di động của bạn (Android hoặc iOS), người dùng có thể chọn giữa các ứng dụng sau;

1. Tải xuống một ứng dụng xác thực hai yếu tố;
   - Authy cho [Android](https://play.google.com/store/apps/details?id=com.authy.authy) hoặc [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator cho [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) hoặc [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator cho [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) hoặc [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)
2. Sau khi tải xuống và cài đặt Ứng dụng xác thực hai yếu tố.
   - Quét mã QR được cung cấp bởi BTCPay Server
   - Hoặc nhập khóa được tạo bởi BTCPay Server vào ứng dụng Xác thực của bạn một cách thủ công.
3. Ứng dụng Xác thực sẽ cung cấp cho bạn một mã độc nhất. Nhập mã này vào BTCPay Server để xác minh cài đặt, và nhấn `Verify - Xác thực` để hoàn tất quá trình.

![image](assets/en/6.webp)

### Tóm tắt Kỹ năng

Trong phần này, bạn đã học được những điều sau:

- Các tùy chọn quản lý tài khoản và các cách khác nhau để quản lý một tài khoản trên phiên bản Demo của BTCPay Server.
- Cách thiết lập xác thực hai yếu tố (2fa) dựa trên ứng dụng.

### Đánh giá kiến thức

#### Đánh giá kiến thức lý thuyết

Mô tả cách xác thực hai yếu tố dựa trên ứng dụng giúp bảo vệ tài khoản của bạn

## Tạo một cửa hàng mới

<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>
Khi một người dùng mới đăng nhập vào BTCPay Server, môi trường của họ là trống trơn và cần có cửa hàng đầu tiên. BTCPay Server sẽ cung cấp cho người dùng tùy chọn ‘Create your store - Tạo cửa hàng của bạn’ (1). Một Cửa hàng có thể được xem như là một ngôi nhà cho nhu cầu Bitcoin của bạn. Một node BTCPay Server mới sẽ bắt đầu với việc đồng bộ hóa Blockchain Bitcoin (2). Tùy thuộc vào cơ sở hạ tầng bạn chạy BTCPay Server ở trên đố, việc đồng bộ này có thể mất từ vài giờ đến vài ngày. Phiên bản hiện tại của máy chủ được hiển thị ở góc dưới bên phải của giao diện người dùng của bạn. Điều này hữu ích cho việc tham khảo khi khắc phục sự cố.
![hình ảnh](assets/en/7.webp)

### Tạo cửa hàng

Từ đây, khoả học này sẽ bắt đầu với một màn hình hơi khác so với trang trước. Khi giáo viên của bạn đã chuẩn bị môi trường Demo, Blockchain Bitcoin đã được đồng bộ hóa trước, và do đó bạn sẽ không thấy trạng thái đồng bộ của các node.

Người dùng có thể quyết định xóa toàn bộ tài khoản của họ. Điều này có thể được thực hiện bằng cách nhấp vào nút xóa trên tab Tài khoản.

![hình ảnh](assets/en/8.webp)

**!Lưu ý!**

Tài khoản BTCPay Server có thể tạo được một số lượng không giới hạn các cửa hàng. Mỗi cửa hàng là một ví hoặc một “ngôi nhà”.

### Ví dụ

Bắt đầu bằng cách nhấp vào "Create your store - Tạo cửa hàng của bạn".

![hình ảnh](assets/en/9.webp)

Điều này sẽ tạo ra Ngôi nhà và bảng điều khiển đầu tiên của bạn để có thể sử dụng BTCPay server.

(1) Sau khi nhấp vào "Create your store - Tạo cửa hàng của bạn", BTCPay Server sẽ yêu cầu bạn đặt tên cho cửa hàng; điều này có thể là bất cứ thứ gì hữu ích cho bạn.

![hình ảnh](assets/en/10.webp)

(2) Tiếp theo, cần phải thiết lập một đơn vị tiền tệ mặc định cho cửa hàng, có thể là tiền pháp định hoặc được định giá theo tiêu chuẩn Bitcoin / Sats. Đối với môi trường demo, chúng tôi sẽ thiết lập nó thành USD.

![hình ảnh](assets/en/11.webp)

(3) Là tham số cuối cùng trong việc thiết lập cửa hàng, BTCPay Server yêu cầu bạn thiết lập một "Preferred Price Source - Nguồn giá ưa thích" nhằm xác định mức giá Bitcoin tính theo tiền pháp định hiện tại để cửa hàng của bạn hiển thị tỷ giá hối đoái chính xác giữa Bitcoin và tiền tệ pháp định được thiết lập cho cửa hàng. Chúng tôi sẽ tuân theo mặc định trong ví dụ Demo và thiết lập điều này thành sàn giao dịch Kraken. BTCPay Server sử dụng API của Kraken để kiểm tra tỷ giá hối đoái.

![hình ảnh](assets/en/12.webp)

(4) Bây giờ, sau khi các tham số cửa hàng đã được thiết lập, nhấp vào nút `Create - Tạo`, và BTCPay Server sẽ tạo bảng điều khiển cửa hàng đầu tiên của bạn, để bạn có thể quản lý nó.

![hình ảnh](assets/en/13.webp)

Xin chúc mừng, bạn đã tạo cửa hàng đầu tiên của mình, và bài tập này đã được hoàn thành.

![hình ảnh](assets/en/14.webp)

### Tóm tắt kỹ năng

Trong phần này, bạn đã học:

- Tạo cửa hàng và cấu hình đơn vị tiền tệ mặc định kết hợp với nguồn lấy giá ưa thích
- Mỗi "Cửa hàng" là một ngôi nhà mới tách biệt khỏi các cửa hàng khác theo cài đặt này của BTCPay Server.

# Giới thiệu về Bảo mật Khóa Bitcoin

<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>

## Hiểu biết về việc tạo khóa Bitcoin

<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>

### Việc tạo khóa Bitcoin bao gồm những gì?

Khi tạo ví Bitcoin, ví sẽ tạo ra một cái gọi là "hạt giống", chuỗi các từ được tạo ra trước đó còn được biết đến như là cụm từ ghi nhớ. Hạt giống được sử dụng để tạo ra các Khóa Bitcoin riêng lẻ từ đó và được sử dụng để gửi hoặc nhận Bitcoin. Cụm từ hạt giống không bao giờ nên được chia sẻ với bên thứ ba hoặc các đối tác không đáng tin cậy.
Việc tạo seed được thực hiện theo tiêu chuẩn công nghiệp được biết đến với tên gọi là cấu trúc ví "Tất định phân tầng - Hierarchical Deterministic" (HD).
![image](assets/en/15.webp)

### Địa chỉ

BTCPay Server được xây dựng để tạo ra một địa chỉ mới. Điều này giảm bớt vấn đề tái sử dụng khoá công khai hoặc địa chỉ. Sử dụng cùng một khóa công khai làm cho việc theo dõi toàn bộ lịch sử thanh toán của bạn trở nên rất dễ dàng. Xem khóa công khai như là phiếu sử dụng một lần sẽ cải thiện đáng kể quyền riêng tư của bạn. Chúng tôi cũng sử dụng địa chỉ Bitcoin, đừng nhầm lẫn chúng với khóa công khai.

Một địa chỉ được tạo ra từ khóa công khai thông qua một “thuật toán băm.” Tuy nhiên, hầu hết ví và giao dịch sẽ hiển thị địa chỉ thay vì những khóa công khai đó. Địa chỉ, nói chung, ngắn hơn khóa công khai và thường bắt đầu bằng `1`, `3`, hoặc `bc1`, trong khi khóa công khai bắt đầu bằng `02`, `03`, hoặc `04`.

- Địa chỉ bắt đầu bằng `1.....` vẫn là các địa chỉ rất phổ biến. Như đã đề cập trong chương Tạo một cửa hàng mới, đây là các địa chỉ theo chuẩn cũ (legacy). Loại địa chỉ này dành cho giao dịch P2PKH. P2PKH sử dụng mã hóa Base58, làm cho địa chỉ nhạy cảm với chữ hoa và chữ thường. Cấu trúc của nó dựa trên khóa công khai với chữ số 1 được thêm vào như một định danh.

- Địa chỉ bắt đầu bằng `bc1...` đang dần trở thành các địa chỉ rất phổ biến. Đây được biết đến là địa chỉ SegWit (native - bản địa). Chúng mang đến một cơ cấu phí tốt hơn so với các loại địa chỉ khác đã đề cập. Địa chỉ SegWit (native - bản địa) sử dụng mã hóa Bech32 và chỉ cho phép sử dụng chữ thường.

- Địa chỉ bắt đầu bằng `3...` thường được sử dụng bởi các sàn giao dịch cho địa chỉ nạp tiền. Địa chỉ này được đề cập trong chương Tạo một cửa hàng mới, là địa chỉ SegWit (wrapped - bọc). Tuy nhiên, chúng cũng có thể hoạt động như một "Địa chỉ đa chữ ký - Multisig". Khi được sử dụng như một địa chỉ SegWit, loại địa chỉ này cũng giúp tiết kiệm phí giao dịch, tuy nhiên sẽ ít hơn so với SegWit (native). Địa chỉ P2SH sử dụng mã hóa Base58. Điều này làm cho nó nhạy cảm với chữ hoa và chữ thường, giống như địa chỉ legacy.

- Địa Chỉ bắt đầu bằng `2...` là địa chỉ Testnet - thử nghiệm. Chúng được dùng để nhận bitcoin testnet (tBTC). Bạn không bao giờ nên nhầm lẫn và gửi Bitcoin đến những địa chỉ này. Với mục đích thử nghiệm và phát triển, bạn có thể tạo một ví testnet. Có nhiều nguồn cung cấp bitcoin testnet trực tuyến. Không bao giờ mua Bitcoin testnet. Bitcoin testnet có thể đào đyiwch. Điều này có thể là lý do mà một nhà phát triển sử dụng Regtest thay thế. Đây là một môi trường thử nghiệm cho các nhà phát triển, thiếu một số thành phần mạng. Tuy nhiên, Bitcoin, cho mục đích thử nghiệm và phát triển, rất hữu ích.

### Khóa công khai - Public Key

Khóa công khai ngày nay ít được sử dụng trong thực tế. Theo thời gian, người dùng bitcoin đã thay thế chúng bằng địa chỉ. Chúng vẫn tồn tại và đôi khi vẫn được sử dụng. Khóa công khai, nói chung, là chuỗi ký tự dài hơn nhiều so với địa chỉ. Giống như với địa chỉ, chúng bắt đầu với một định danh cụ thể.

- Đầu tiên, `02...` và `03...` là các định danh khóa công khai rất tiêu chuẩn được mã hóa trong định dạng SEC. Chúng có thể được xử lý và chuyển đổi thành địa chỉ để nhận, được sử dụng để tạo địa chỉ multi-sig, hoặc để xác minh chữ ký. Các giao dịch Bitcoin những ngày đầu sử dụng khóa công khai là một phần của giao dịch P2PK.

- Tuy nhiên, ví HD sử dụng một cấu trúc khác. `xpub...`, `ypub...` hoặc `zpub...` được gọi là khóa công khai mở rộng hay còn gọi là xpubs. Những khóa này được sử dụng để tạo ra nhiều khóa công khai vì chúng là một phần của ví HD. Vì xpub của bạn giữ các bản ghi của toàn bộ lịch sử của bạn, nghĩa là các giao dịch trong quá khứ và tương lai, không bao giờ chia sẻ chúng với các bên không đáng tin cậy.

### Tóm tắt kỹ năng

Trong phần này, bạn đã học được những điều sau:

- Sự khác biệt giữa địa chỉ và khóa công khai và lợi ích của việc sử dụng địa chỉ so với khóa công khai.

### Đánh giá kiến thức

Mô tả lợi ích của việc sử dụng địa chỉ mới cho mỗi giao dịch so với việc tái sử dụng địa chỉ hoặc sử dụng khoá công khai.

## Bảo mật các khóa với ví cứng

<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>

### Lưu trữ các khoá Bitcoin

Sau khi tạo ra cụm từ hạt giống, danh sách 12 hoặc 24 từ này đòi hỏi phải được sao lưu và bảo mật đúng cách, vì những từ này là cách duy nhất để khôi phục quyền truy cập vào ví. Cấu trúc của ví HD và cách nó tạo ra địa chỉ một cách tất định sử dụng hạt giống đó, tất cả địa chỉ bạn tạo ra sẽ được sao lưu sử dụng danh sách cụm từ hạt giống hay cụm từ khôi phục này.

Hãy lưu giữ an toàn và bảo mật cụm từ khôi phục của bạn. Nếu ai đó, đặc biệt là với ý đồ xấu, truy cập được, họ có thể lấy chuyển tiền của bạn. Có một số phương pháp để lưu trữ khóa riêng tư Bitcoin, mỗi phương pháp đều có lợi ích và nhược điểm, dù là về bảo mật, riêng tư, tiện lợi, hay phương tiện vật lý. Do tầm quan trọng của khóa riêng tư, người dùng bitcoin thường lưu trữ và giữ an toàn những khóa này theo phương pháp "tự quản - self custody" thay vì sử dụng dịch vụ "giữ hộ - custodial" như ngân hàng. Tùy thuộc vào người dùng, anh ta phải sử dụng giải pháp lưu trữ lạnh hoặc là dùng ví nóng.

### Lưu trữ khóa bitcoin nóng và lạnh (Hot and Cold storage)

Thông thường, ví bitcoin được phân loại thành ví nóng (Hot Wallet) và ví lạnh (Cold Wallet). Hầu hết sự đánh đổi nằm ở sự tiện lợi, dễ sử dụng và rủi ro bảo mật. Chúng ta cung có thể bắt gặp các phương pháp lưu trữ này được cung cấp bởi dịch vụ giữ hộ. Tuy nhiên, sự đánh đổi ở đây chủ yếu là trên khía cạnh bảo mật và riêng tư và điều này vượt ra ngoài phạm vi của khóa học này.

### Ví nóng - Hot Wallet

Ví Nóng là cách tiện lợi nhất để tương tác với Bitcoin qua điện thoại di động, web, hoặc phần mềm máy tính. Ví luôn kết nối với internet, cho phép người dùng gửi hoặc nhận bitcoin. Tuy nhiên, đây cũng là điểm yếu của nó, vì luôn trực tuyến, ví sẽ dễ bị tấn công bởi hacker hoặc mã độc trên thiết bị của bạn. Trong BTCPay Server, ví nóng lưu trữ khóa riêng trên instance. Bất kỳ ai truy cập vào cửa hàng BTCPay Server của bạn có thể ăn cắp tiền từ địa chỉ này nếu họ có ý đồ xấu. Khi BTCPay Server chạy trong môi trường sử dụng dịch vụ hosting (hosted environment), bạn nên luôn xem xét đến điều này trong phương án bảo mật của mình và ưu tiên không sử dụng ví nóng trong trường hợp như vậy. Khi BTCPay Server được cài đặt trên phần cứng do bạn sở hữu, được bảo mật và có độ tin cậy, mức độ rủi ro giảm đáng kể, nhưng nó không bao giờ biến mất hoàn toàn!

### Ví lạnh - Cold Wallet

Cá nhân chuyển bitcoin của họ vào ví lạnh vì nó có thể biệt lập khóa riêng tư ra khỏi internet. Loại bỏ kết nối internet giúp giảm thiểu rủi ro của mã độc, phần mềm gián điệp, và tấn công đổi SIM. Lưu trữ lạnh được tin là vượt trội hơn lưu trữ nóng về mặt an toàn và tự chủ, miễn là các biện pháp phòng ngừa thích hợp được thực hiện để tránh mất khóa riêng tư. Do sự phức tạp trong cài đặt và sử dụng, lưu trữ lạnh phù hợp nhất cho số lượng bitcoin có giá trị cao.

Có nhiều phương pháp để lưu trữ khóa riêng tư với ví lạnh, từ ví giấy đến ví não, ví cứng, hoặc như những ngày đầu của Bitcoin là một file. Hầu hết ví sử dụng BIP 39 để tạo cụm từ hạt giống. Tuy nhiên, trong phần mềm Bitcoin Core, vẫn chưa đạt được sự đồng thuận về việc sử dụng nó. Phần mềm Bitcoin Core vẫn sẽ tạo ra một file dữ liệu là Wallet.dat và bạn cần lưu trữ nó ở một vị trí ngoại tuyến an toàn.

### Tóm tắt kỹ năng

Trong phần này, bạn đã học được:

- Sự khác biệt giữa ví nóng và ví lạnh về chức năng cũng như những sự đánh đổi của chúng.

### Đánh giá kiến thức lý thuyết

- Ví tiền là gì?
- Sự khác biệt giữa ví nóng và ví lạnh là gì?
- Mô tả ý nghĩa của hoạt động "khởi tạo ví - generating a wallet"?

## Sử dụng khóa Bitcoin của bạn

<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>

### Ví BTCPay Server

BTCPay Server bao gồm các tính năng ví tiêu chuẩn sau:

- Giao dịch - Transactions
- Gửi - Send
- Nhận - Receive
- Quét lại - Rescan
- Yêu cầu thanh toán - Pull Payments
- Xuất chi - Payouts
- Giao dịch Bitcoin ký một phần - Partially Signed Bitcoin Transactions - PSBT
- Cài đặt chung - General Settings

### Giao dịch

Quản trị viên có thể xem các giao dịch đến và đi cho ví on-chain được kết nối với cửa hàng cụ thể trong giao diện giao dịch. Mỗi giao dịch sẽ được phân biệt giữa nhận và gửi. Giao dịch nhận sẽ có màu xanh và giao dịch gửi đi sẽ có màu đỏ. Trong giao diện giao dịch của BTCPay Server, quản trị viên cũng sẽ thấy một bộ nhãn tiêu chuẩn.

| Loại Giao Dịch  | Mô Tả                                                  |
| --------------- | ------------------------------------------------------ |
| App             | Thanh toán được nhận qua hóa đơn tạo bởi ứng dụng      |
| invoice         | Thanh toán được nhận qua hóa đơn                       |
| payjoin         | Chưa thanh toán, bộ đếm thời gian hóa đơn vẫn chưa hết |
| payjoin-exposed | UTXO được tiết lộ qua đề xuất payjoin của hóa đơn      |
| payment-request | Thanh toán được nhận qua yêu cầu thanh toán            |
| payout          | Thanh toán được gửi qua một đợt xuất chi hoặc hoàn tiền      |

### Cách gửi

Chức năng gửi của BTCPay Server gửi giao dịch từ ví on-chain của BTCPay Server. BTCPay Server cho phép nhiều cách ký giao dịch để chi tiêu tiền. Một giao dịch có thể được ký với;

- Ví cứng - Hardware Wallet
- Ví hỗ trợ PSBT
- Khóa riêng tư hoặc hạt giống khôi phục của ví HD
- Ví nóng

#### Ví cứng

BTCPay Server có tích hợp hỗ trợ ví cứng cho phép bạn sử dụng ví cứng của mình với BTCPay Vault mà không tiết lộ thông tin cho máy chủ hoặc ứng dụng bên thứ ba. Tích hợp ví cứng trong BTCPay Server cho phép bạn nhập (import) ví cứng của mình và chi tiêu dòng tiền chuyển đến chỉ với một xác nhận đơn giản trên thiết bị của bạn. Khóa riêng tư của bạn không bao giờ rời khỏi thiết bị, và tất cả tiền đều được xác thực bởi đầy đủ của bạn, vì vậy không có rò rỉ dữ liệu.

#### Ký với ví hỗ trợ PSBT

PSBT (Partially Signed Bitcoin Transactions - Giao dịch Bitcoin được ký một phần) là một định dạng trao đổi cho các giao dịch Bitcoin cần được ký đầy đủ. PSBT được hỗ trợ trong BTCPay Server và có thể được ký bởi ví cứng và phần mềm tương thích.

Quy trình xây dựng một giao dịch Bitcoin được ký đầy đủ diễn ra qua các bước sau:

- Một PSBT được thiết lập với các đầu vào và đầu ra cụ thể nhưng không có chữ ký
- PSBT được xuất có thể được nhập vào bởi ví hỗ trợ định dạng này
- Dữ liệu giao dịch có thể được kiểm tra và ký bằng ví
- Tệp PSBT đã ký được xuất từ ví và nhập vào nhờ BTCPay Server
- BTCPay Server tạo ra giao dịch Bitcoin cuối cùng
- Bạn xác minh kết quả và phát sóng nó lên mạng lưới

#### Ký với khoá riêng tư hoặc hạt giống khôi phục ví HD

Nếu bạn đã tạo một ví trước khi sử dụng BTCPay Server, bạn có thể chi tiêu tiền bằng cách nhập (import) khóa riêng tư của mình vào một trường thích hợp. Đặt một "AccountKeyPath" phù hợp trong cài đặt ví; nếu không, bạn không thể chi tiêu tiền của mình.

#### Ký với ví nóng

Nếu bạn đã tạo một ví mới khi thiết lập cửa hàng của mình và kích hoạt nó như một ví nóng, nó sẽ tự động sử dụng hạt giống được lưu trữ trên máy chủ để ký.

### RBF (Replace-By-Fee) - Thay thế bằng phí
Replace-By-Fee (RBF) là một tính năng của giao thức Bitcoin cho phép bạn thay thế một giao dịch đã được phát sóng trước đó (trong khi vẫn chưa được xác nhận). Điều này cho phép ngẫu nhiên hóa dấu vân tay giao dịch của ví hoặc thay thế nó bằng một giao dịch cơ mức phí cao hơn để đưa nó lên vị trí ưu tiên cao hơn trong khi đợi được xác nhận (đào). Điều này sẽ thay thế hiệu quả giao dịch gốc vì mức phí cao hơn sẽ được ưu tiên, và một khi được xác nhận, sẽ làm vô hiệu giao dịch gốc (không lặp chi).
Nhấn vào nút `Advanced Settings - Cài đặt nâng cao` để xem các tùy chọn RBF:

![image](assets/en/16.webp)

- Randomize for higher privacy - Ngẫu nhiên hóa để tăng tính riêng tư, cho phép giao dịch được thay thế tự động để ngẫu nhiên hóa dấu vân tay giao dịch.
- Yes - Có, Đánh dấu giao dịch cho RBF và được thay thế một cách rõ ràng (Không được thay thế theo mặc định, chỉ qua đầu vào)
- No - Không, Không cho phép giao dịch được thay thế.

### Lựa chọn coin

Lựa chọn coin là một tính năng nâng cao tăng cường quyền riêng tư, nó cho phép bạn chọn các coin bạn muốn chi tiêu khi tạo một giao dịch. Ví dụ, thanh toán bằng các coin mới từ một lần trộn coin (coinjoin).

Lựa chọn coin hoạt động tự nhiên với tính năng nhãn ví. Điều này cho phép bạn gắn nhãn cho các khoản tiền đến để quản lý UTXO và chi tiêu một cách mượt mà hơn.

BTCpay Server cũng hỗ trợ BIP-329 cho quản lý nhãn. BIP-329 cho phép gắn nhãn lên; nếu bạn chuyển từ một ví hỗ trợ BIP39này và thiết lập nhãn, BTCPay Server sẽ nhận biết và nhập chúng. Khi chuyển đổi máy ch, thông tin này cũng có thể được xuất và nhập vào môi trường mới.

### Cách Nhận

Khi nhấn vào nút nhận trong BTCPay Server, nó tạo ra một địa chỉ mới để nhận thanh toán. Quản trị viên cũng có thể tạo ra một địa chỉ mới bằng cách tạo một “Invoice - Hóa đơn” mới.

BTCPay Server luôn yêu cầu tạo địa chỉ có sẵn tiếp theo để tránh tái sử dụng địa chỉ. Sau khi nhấn “Generate next available BTC Address - Tạo địa chỉ có sẵn tiếp theo”, BTCPay Server sẽ tạo ra một địa chỉ mới và mã QR. Nó cũng cho phép bạn trực tiếp thiết lập một nhãn cho địa chỉ đó để quản lý địa chỉ của bạn tốt hơn.

![image](assets/en/17.webp)

![image](assets/en/18.webp)

#### Quét Lại - Rescan

Tính năng quét lại dựa vào “Scantxoutset” của Bitcoin Core 0.17.0 để quét trạng thái hiện tại của blockchain (gọi là UTXO Set) để tìm các coin thuộc về lược đồ phái sinh được địn dạng. Quét lại ví giải quyết hai vấn đề mà người dùng BTCPay Server gặp phải.

1. Vấn đề giới hạn khoảng trống - Hầu hết các ví bên thứ ba là ví nhẹ (light wallet) chia sẻ một node giữa nhiều người dùng. Ví dựa vào node đầy đủ và node rút gọn giới hạn số lượng (thường là 20) địa chỉ rỗng mà chúng theo dõi trên blockchain để tránh vấn đề ảnh hưởng tới hiệu suất. BTCPay Server tạo ra một địa chỉ mới cho mỗi hóa đơn. Do đó, sau khi BTCPay Server tạo ra 20 hóa đơn chưa thanh toán liên tiếp, ví bên ngoài ngừng tìm kiếm các giao dịch, giả định rằng không có giao dịch mới nào xảy ra. Ví bên ngoài của bạn sẽ không hiển thị chúng một khi các hóa đơn được thanh toán trên lần thứ 21, 22, v.v. Ngược lại, ví của BTCPay Server theo dõi bất kỳ địa chỉ nào nó tạo ra cùng với một giới hạn khoảng trống lớn hơn nhiều. Nó không phụ thuộc vào bên thứ ba và luôn có thể hiển thị số dư chính xác.
2. Giải pháp giới hạn khoảng trống - Nếu [ví bên ngoài/ví hiện tại](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-wallet) của bạn cho phép cấu hình giới hạn khoảng trống, cách đơn giản là tăng nó lên. Tuy nhiên, đa số ví không cho phép làm điều này. Chỉ có một số ít ví cho phép cấu hình giới hạn khoảng trống mà chúng tôi biết đến là Electrum, Wasabi và Sparrow Wallet. Thật không may, bạn có thể gặp vấn đề với nhiều ví khác. Để có trải nghiệm người dùng tốt nhất và bảo mật, hãy cân nhắc từ bỏ ví ngoài và sử dụng ví nội bộ của BTCPay Server.

#### BTCPay Server sử dụng “mempoolfullrbf=1”

BTCPay Server sử dụng “mempoolfullrbf=1”; chúng tôi đã thêm mặc định này vào cài đặt BTCPay Server của bạn. Tuy nhiên, chúng tôi cũng đã tạo ra một phân đoạn mà bạn có thể tự tắt. Không có “mempoolfullrbf=1”, nếu một khách hàng thực hiện giao dịch lặp chi mà không báo hiệu RBF, người bán chỉ biết sau khi xác nhận.

Quản trị viên có thể không muốn sử dụng cài đặt này. Bằng chuỗi sau, bạn có thể thay đổi cài đặt mặc định.

```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCLUDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i**
```

### Cài đặt ví BTCPay Server

Cài đặt ví trong BTCPay Server cung cấp cái nhìn tổng quan rõ ràng và nhanh chóng về cài đặt chung cho ví của bạn. Tất cả các cài đặt này được điền trước nếu ví được tạo với BTCPay Server.

![image](assets/en/19.webp)

Bắt đầu việc cài đặt ví của BTCPay Server với trạng thái ví. Là ví chỉ dùng để xem (Watch-Only) hay ví nóng? Tùy thuộc vào loại ví, các hành động có thể khác nhau từ quét lại ví để tìm kiếm giao dịch bị thiếu, cắt bớt giao dịch cũ khỏi lịch sử, đăng ký ví cho liên kết thanh toán, hoặc thay thế và xóa ví hiện tại được gắn với cửa hàng. Trong cài đặt ví của BTCPay Server, quản trị viên có thể gắn nhãn cho ví để quản lý ví tốt hơn. Tại đây, quản trị viên cũng có thể thấy Sơ đồ phát sinh (Derivation Scheme), khóa tài khoản (xpub), dấu vân tay (fingerprint), và đường dẫn khóa (keypath). Cài đặt thanh toán trong cài đặt ví chỉ có 2 cài đặt chính. Thanh toán không hợp lệ nếu giao dịch không xác nhận trong (số phút đã đặt) sau khi hóa đơn hết hạn. Xem xét hóa đơn được xác nhận khi giao dịch thanh toán có X số lần xác nhận. Quản trị viên cũng có thể đặt một công tắc để hiển thị phí được đề xuất tại thời điểm thực hiện thanh toán hoặc đặt thủ công mục tiêu xác nhận theo số khối.

![image](assets/en/20.webp)

**!Lưu ý!**

Nếu bạn theo dõi khóa học này một mình, việc tạo tài khoản này có thể là điều bạn sẽ làm trên một máy chủ của bên thứ ba, do đó, một lần nữa chúng tôi nhắc bạn không sử dụng những môi trường này cho mục đích sản xuất kinh doanh thực, mà chỉ dùng cho mục đích đào tạo.

### Ví dụ

#### Thiết lập ví Bitcoin trong BTCPay Server

BTCPay Server cho phép hai cách thiết lập ví. Một cách là nhập một ví Bitcoin đã tồn tại. Việc nhập có thể được thực hiện bằng cách kết nối ví cứng, nhập tệp ví, nhập khóa công khai mở rộng, quét mã QR của ví, hoặc ít được ưa chuộng nhất, nhập bằng tay hạt giống khôi phục ví đã tạo trước đó. Trong BTCPay Server, cũng có thể tạo ví mới. Có hai cách có thể cấu hình BTCPay Server khi tạo ví mới.
Tùy chọn ví nóng trong BTCPay Server cho phép sử dụng các tính năng như 'Payjoin' hoặc 'Liquid'. Tuy nhiên, có một nhược điểm, cụm từ hạt giống khôi phục được tạo cho ví này sẽ được lưu trữ trên máy ch, nơi bất kỳ ai có quyền Admin cũng có thể truy cập cụm từ hạt giống khôi phục. Vì khóa riêng tư của bạn được tạo ra từ cụm từ hạt giống khôi phục, một người có ý định xấu có thể truy cập vào số tiền hiện tại và tương lai của bạn!

Để giảm thiểu rủi ro này trong BTCPay Server, một Admin có thể thiết lập trong Cài đặt máy chủ (Server Settings)> Chính sách (Policies) > "Cho phép người không phải là admin tạo ví nóng cho cửa hàng của họ - Allow non-admins to create hot wallet for their stores" thành KHÔNG, như mặc định. Để tăng cường bảo mật cho những ví nóng này, quản trị viên máy chủ nên kích hoạt xác thực 2FA cho các tài khoản được phép có ví nóng. Lưu trữ khóa riêng tư trên máy chủ công khai là nguy hiểm và đi kèm với rủi ro. Một số rủi ro tương tự như rủi ro của Lightning Network (xem chương tiếp theo về rủi ro của Lightning Network).

Tùy chọn thứ hai mà BTCPay Server cung cấp trong việc tạo ví mới là tạo một ví chỉ dùng để xem (Watch-Only Wallet). BTCPay Server sẽ tạo ra khóa riêng tư của bạn một lần. Sau khi người dùng xác nhận đã ghi lại cụm từ hạt giống của họ, BTCPay Server sẽ xóa khóa riêng tư khỏi máy chủ. Kết quả là, cửa hàng của bạn giờ đây có một ví chỉ dùng để xem được kết nối với nó. Để chi tiêu số tiền nhận được trên ví chỉ dùng để xem của bạn, xem chương cách gửi, hoặc là sử dụng BTCPay Server Vault, hoặc PSBT (giao dịch bitcoin được ký một phần), hoặc ít được khuyến khích nhất, nhập thủ công cụm từ hạt giống của bạn.

Bạn đã tạo một 'Cửa hàng' mới trong phần trước đây. Trình cài đặt sẽ tiếp tục bằng cách yêu cầu thiết lập ví - `Set up a wallet` hoặc thiết lập một Lightning Node - `Set up a Linghtning node`. Trong ví dụ này, bạn sẽ theo quy trình hướng dẫn thiết lập ví (1).

![image](assets/en/21.webp)

Sau khi nhấp vào "Thiết lập ví - Set up a wallet", trình hướng dẫn sẽ tiếp tục bằng cách yêu cầu bạn muốn tiếp tục như thế nào; BTCPay Server hiện tại cung cấp tùy chọn kết nối ví Bitcoin hiện có với cửa hàng mới của bạn. Nếu bạn không có ví, BTCPay Server đề xuất tạo một ví mới. Ví dụ này sẽ theo các bước để “Tạo một ví mới - Create a new wallet” (2). Theo dõi các bước để tìm hiểu cách "Kết nối ví hiện có - Connect an existing wallet" (1).

![image](assets/en/22.webp)

**!Lưu ý!**

Nếu bạn tham gia khóa học này trong một lớp học, ví dụ hiện tại và cụm từ hạt giống chúng tôi tạo ra chỉ dành cho mục đích giáo dục. Không bao giờ nên có số tiền lớn nào khác ngoài số tiền yêu cầu qua các bài tập trên các địa chỉ này.

(1) Tiếp tục quy trình hướng dẫn "Ví mới - New wallet" bằng cách nhấp vào nút "Tạo ví mới - Create a new wallet".

![image](assets/en/23.webp)

(2) Sau khi nhấp vào “Tạo ví mới - Create a new wallet”, cửa sổ tiếp theo trong quy trình hướng dẫn sẽ đưa ra các tùy chọn “Ví nóng - Hot wallet” và “Ví chỉ dùng để xem - Watch-only wallet”. Nếu bạn theo dõi cùng một giảng viên, môi trường của bạn là một môi trường Demo chung, và bạn chỉ có thể tạo một ví chỉ dùng để xem. Chú ý sự khác biệt giữa hai hình dưới đây. Khi bạn đang trong môi trường Demo và theo dõi cùng giảng viên, hãy tạo một "Ví chỉ dùng xem" và tiếp tục với quy trình hướng dẫn "Ví mới".

![image](assets/en/24.webp)

![image](assets/en/25.webp)

(3) Tiếp tục quy trình hướng dẫn ví mới, bạn bây giờ đang ở phần "Tạo ví BTC chỉ dùng để xem - Create BTC watch-only wallet". Tại đây chúng ta có thể thiết lập "Loại địa chỉ ví - Address type" mà BTCPay Server cho phép bạn chọn loại địa chỉ ưa thích của mình; tính đến thời điểm viết khóa học này, người dùng vẫn được khuyến nghị sử dụng địa chỉ bech32. Tìm hiểu chi tiết hơn về các loại địa chỉ trong chương đầu tiên của phần này.

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

(4) Khi thiết lập tham số cho Ví, BTCPay Server cho phép người dùng tuỳ chọn thiết lập một cụm từ mật khẩu (passphrase) thông qua BIP39, hãy chắc chắn xác nhận mật khẩu của bạn.

![image](assets/en/27.webp)

(5) Sau khi thiết lập loại địa chỉ ví và có thể thiết lập một số tùy chọn nâng cao, nhấp vào "Tạo - Create", và BTCPay Server sẽ tạo ví mới cho bạn. Lưu ý rằng đây là bước cuối cùng trước khi tạo cụm từ hạt giống của bạn. Hãy chắc chắn chỉ thực hiện điều này trong một môi trường mà người khác không thể đánh cắp cụm từ hạt giống bằng cách nhìn vào màn hình của bạn.

![image](assets/en/28.webp)

(6) Trong màn hình tiếp theo của trình hướng dẫn, BTCPay Server hiển thị cho bạn cụm từ hạt giống phục hồi cho ví mới tạo của bạn; đây là chìa khóa để khôi phục ví và ký giao dịch. BTCPay Server tạo ra một cụm từ hạt giống gồm 12 từ. Những từ này sẽ được xóa khỏi server sau màn hình thiết lập này. Ví này cụ thể là một ví chỉ dùng để xem (watch-only). Khuyến nghị không lưu trữ cụm từ hạt giống này dưới dạng số hoặc hình ảnh. Người dùng chỉ có thể tiếp tục trình hướng dẫn nếu họ xác nhận rằng họ đã ghi chép cụm từ hạt giống của mình.

![image](assets/en/29.webp)

(7) Sau khi nhấp vào "Hoàn tất - Done" và bảo mật cụm từ hạt giống của ví Bitcoin mới tạo, BTCPay Server sẽ cập nhật cửa hàng của bạn với ví mới đính kèm và sẵn sàng nhận thanh toán. Trong giao diện người dùng, trong menu điều hướng bên trái, chú ý cách dòng chữ Bitcoin hiện được làm nổi bật và kích hoạt dưới mục ví (WALLETS).

![image](assets/en/30.webp)

### Ví dụ: Ghi chép cụm từ hạt giống

Đây là một khoảnh khắc rất đặc biệt và an toàn để sử dụng Bitcoin. Như đã đề cập trước đó, chỉ bạn mới nên có quyền truy cập hoặc biết về cụm từ hạt giống của mình. Khi bạn theo dõi cùng một giáo viên và lớp học, cụm từ hạt giống tạo ra chỉ nên được sử dụng trong khóa học này. Quá nhiều yếu tố, ánh mắt tò mò từ bạn cùng lớp, hệ thống không an toàn, và nhiều yếu tố khác làm cho những chìa khóa này chỉ mang tính giáo dục và không đáng tin cậy. Tuy nhiên, các chìa khóa được tạo ra vẫn nên được lưu trữ cho các ví dụ trong khóa học.

Phương pháp đầu tiên chúng ta sẽ sử dụng trong tình huống hiện tại, cũng là phương pháp ít an toàn nhất, là ghi chép cụm từ hạt giống theo đúng thứ tự. Một thẻ cụm từ hạt giống có trong tài liệu khóa học được cung cấp cho sinh viên hoặc tìm thấy trên GitHub của BTCPay Server. Chúng ta sẽ sử dụng thẻ này để ghi chép các từ được tạo ra ở bước trước. Hãy chắc chắn ghi chúng theo đúng thứ tự. Sau khi bạn đã ghi chép, kiểm tra lại với phần mềm để đảm bảo bạn đã ghi chép đúng thứ tự. Sau khi bạn đã ghi chép, nhấp vào hộp xác nhận bạn đã ghi chép cụm từ hạt giống của mình một cách chính xác.

### Ví dụ: Lưu trữ cụm từ hạt giống trên một ví phần cứng

Trong khóa học này, chúng tôi đề cập đến việc lưu trữ cụm từ hạt giống trên một ví phần cứng. Theo dõi khóa học này cùng một giáo viên có thể sẽ không có thiết bị như vậy. Trong tài liệu hướng dẫn của khóa học, có một danh sách các ví cứng được cung cấp phù hợp với bài tập này.
Chúng ta sẽ sử dụng kho lưu trữ BTCPay Server và ví cứng Blockstream Jade trong ví dụ này.
Bạn cũng có thể theo dõi qua video để tham khảo cách kết nối ví cứng.
![BTCPay Server - Cách kết nối ví cứng của bạn với BTCPay Vault.](https://youtu.be/s4qbGxef43A)

Tải về kho lưu trữ BTCPay Server: https://github.com/btcpayserver/BTCPayServer.Vault/releases

Hãy chắc chắn bạn đã tải về các tệp đúng cho hệ thống của mình. Người dùng Windows nên tải gói [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe), người dùng Mac tải [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg), và người dùng Linux nên tải [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)

Sau khi cài đặt BTCPay Server Vault, khởi động phần mềm bằng cách nhấp vào biểu tượng trên màn hình của bạn. Khi BTCPay Server Vault được cài đặt đúng cách và khởi động lần đầu tiên, nó sẽ yêu cầu quyền được sử dụng với ứng dụng Web. Nó sẽ yêu cầu cấp quyền truy cập cho BTCPay Server cụ thể mà bạn làm việc. Chấp nhận các điều kiện này. BTCPay Server Vault giờ đây sẽ tìm kiếm ví cứng. Một khi thiết bị được tìm thấy, BTCPay Server sẽ nhận ra rằng Vault đang chạy và đã tìm thấy thiết bị của bạn.

**!Lưu Ý!**

Không cung cấp khóa SSH hoặc tài khoản quản trị máy chủ cho bất kỳ ai khác ngoài các quản trị viên khi sử dụng ví nóng. Bất kỳ ai có quyền truy cập vào các tài khoản này sẽ có quyền truy cập vào các quỹ trong ví nóng

### Tóm tắt kỹ năng

Trong phần này, bạn đã học được những điều sau:

- Cách xem giao dịch của ví Bitcoin và các phân loại khác nhau của nó.
- Các lựa chọn khác nhau khi gửi từ ví Bitcoin, từ ví cứng cho đến ví nóng.
- Vấn đề giới hạn khoảng trống khi sử dụng hầu hết các ví và cách khắc phục.
- Cách tạo một ví Bitcoin mới trong BTCPay Server, bao gồm lưu trữ khóa trong ví cứng và sao lưu cụm từ khôi phục.

Trong phần này, bạn đã học cách tạo một ví Bitcoin mới trong BTCPay Server. Chúng ta chưa đi vào cách bảo mật hoặc sử dụng những khóa đó. Tổng quát về phần này, bạn đã học cách thiết lập cửa hàng đầu tiên trên BTCPay Server. Bạn đã học cách tạo cụm từ hạt giống khôi phục Bitcoin.

### Đánh giá kiến thức thực hành

Mô tả một phương pháp để tạo khóa và một kế hoạch bảo mật chúng, cùng với các sự đánh đổi/ rủi ro của phương pháp bảo mật.

## Ví Lightning trên BTCPay Server

<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>

Khi một quản trị viên server thiết lập một BTCPay Server Instance mới, anh ta có thể thiết lập một bản triển khai mạng lưới Lightning, LND, Core Lightning, hoặc Eclair; xem Phần Cấu hình BTCPay Server để biết hướng dẫn cài đặt chi tiết hơn.
Nếu được áp dụng trong một lớp học, việc kết nối một Lightning Node với BTCPay Server của bạn được thực hiện thông qua một node tùy chỉnh. Người dùng không phải là quản trị viên trên BTCPay Server sẽ không thể sử dụng Lightning Node nội bộ mặc định. Điều này nhằm bảo vệ chủ sở hữu khỏi việc mất tiền. Các quản trị viên máy chủ có thể cài đặt một plugin để cung cấp quyền truy cập vào Lightning Node của họ thông qua LNBank; điều này nằm ngoài phạm vi của khoá này; đọc thêm về LNBank trên trang plugin chính thức.

### Kết nối node nội bộ (quản trị viên máy chủ)

Quản trị viên máy chủ có thể sử dụng Lightning Node nội bộ của BTCPay Server. Bất kể triển khai Lightning nào, việc kết nối với Lightning Node nội bộ đều giống nhau.

Đi tới cửa hàng đã thiết lập trước đó và nhấp vào ví "Lightning" trong menu bên trái. BTCPay Server cung cấp hai khả năng thiết lập, sử dụng node nội bộ (chỉ dành cho quản trị viên máy chủ theo mặc định) hoặc một node tùy chỉnh (kết nối bên ngoài). Các quản trị viên có thể nhấp vào tùy chọn "Sử dụng node nội bộ - Use internal node". Không cần cấu hình thêm. Nhấp vào nút "lưu - save" và chú ý thông báo nói rằng, "Lightning Node đã được cập nhật - BTC Lightning node updated". Cửa hàng giờ đây đã thành công hỗ trợ mạng Lightning.

### Kết nối node bên ngoài (người dùng /chủ cửa hàng)

Do chủ cửa hàng theo mặc định không được phép sử dụng Lightning Node của quản trị viên, nên kết nối cần được thực hiện với một node bên ngoài, hoặc là node thuộc sở hữu của chủ cửa hàng trước khi thiết lập BTCPay Server, một plugin LNBank nếu được quản trị viên cung cấp, hoặc một giải pháp giữ hộ (custodial) như Alby.

Đi tới cửa hàng đã thiết lập trước đó và nhấp vào "Lightning" dưới Wallet trong menu bên trái. Vì chủ cửa hàng không được phép sử dụng node nội bộ theo mặc định, tùy chọn này bị vô hiệu hóa. Sử dụng một node tùy chỉnh là tùy chọn duy nhất mặc định có sẵn cho chủ cửa hàng.

BTCPay Server cần thông tin kết nối; thông tin cụ thể cho một bản triển khai Lightning sẽ được cung cấp bởi giải pháp đã thiết lập trước đó (hoặc giải pháp giữ hộ). Trong BTCPay Server, chủ cửa hàng có thể sử dụng các kết nối sau;

- C-lightning qua TCP hoặc Unix domain socket connection.
- Lightning Charge qua HTTPS
- Eclair qua HTTPS
- LND qua proxy REST
- LNDhub qua REST API

![image](assets/en/31.webp)

Nhấp vào "Kiểm tra kết nối - Test connection" để đảm bảo bạn đã nhập đúng chi tiết kết nối. Sau khi kết nối được xác nhận là tốt, nhấp lưu, và BTCPay Server hiển thị cửa hàng được cập nhật với Lightning Node.

### Quản lý Lightning Node nội bộ LND (Quản trị viên máy chủ)

Sau khi kết nối Lightning Node nội bộ, các quản trị viên sẽ nhận thấy các ô mới trên bảng điều khiển dành cho thông tin Lightning.

- Số dư Lightning
- BTC trong các kênh
  - BTC trong các kênh mở
  - BTC số dư nội bộ
  - BTC số dư từ xa
  - BTC trong các kênh đang đóng
- BTC On-chain
  - BTC đã xác nhận
  - BTC chưa xác nhận
  - BTC dự trữ
- Dịch vụ Lightning
  - Ride the Lightning (RTL).

Bằng cách nhấp vào biểu tượng Ride the Lightning trong ô "Dịch vụ Lightning - Lightning Services" hoặc "Lightning" dưới ví trong menu bên trái, các quản trị viên có thể truy cập RTL để quản lý Lightning Node.

**Lưu ý!**

Kết nối Lightning Node nội bộ sẽ thất bại nếu kết nối nội bộ thất bại, xác nhận:

1. Node Bitcoin on-chain đã được đồng bộ hóa đầy đủ
2. Lightning Node nội bộ được "Kích hoạt - Enabled" dưới "Lightning" > "Cài đặt - Settings" > "Cài đặt Lightning BTC - BTC Lightning Settings"
   Nếu bạn không thể kết nối với Lightning Node của mình, hãy thử khởi động lại máy chủ của bạn, hoặc đọc thêm chi tiết trong tài liệu chính thức của BTCPay Server tại đây; https://docs.btcpayserver.org/Troubleshooting/. Bạn không thể chấp nhận thanh toán Lightning trong cửa hàng của mình cho đến khi Lightning Node của bạn hiển thị trạng thái "Online". Hãy thử kiểm tra kết nối Lightning của bạn bằng cách nhấp vào liên kết "Public Node Info"

### Ví Lightning

Trong tùy chọn ví Lightning ở thanh menu bên trái, các quản trị viên máy chủ sẽ tìm thấy quyền truy cập dễ dàng đến RTL, thông tin node công khai của họ, và các cài đặt Lightning đặc biệt cho cửa hàng BTCPay Server của họ.

#### Thông tin node nội bộ

Các quản trị viên có thể nhấp vào thông tin node nội bộ và xem qua trạng thái máy chủ (Online/ Offline) và chuỗi kết nối cho Clearnet hoặc Tor.

![image](assets/en/32.webp)

#### Thay đổi kết nối

Nếu chủ cửa hàng quyết định thay đổi trong Cài đặt Lightning - Thay đổi kết nối (Change connection).
Bên cạnh thông tin node công khai, chủ cửa hàng có thể tìm thấy tùy chọn này. Nó sẽ quay trở lại cài đặt ban đầu cho kết nối Lightning Node bên ngoài, điền thông tin Lightning Node mới, nhấp lưu và cập nhật cửa hàng với thông tin node mới.

![image](assets/en/33.webp)

#### Dịch vụ

Nếu quản trị viên quyết định cài đặt nhiều dịch vụ cho việc triển khai Lightning, chúng sẽ được liệt kê ở đây. Với việc triển khai LND tiêu chuẩn, quản trị viên sẽ có Ride The Lightning (RTL) là công cụ quản lý node tiêu chuẩn.

#### Cài đặt ví BTC Lightning

Sau khi thêm Lightning Node vào cửa hàng ở bước trước, trong cài đặt của ví Lightning, chủ cửa hàng vẫn có thể chọn vô hiệu hóa nó cho cửa hàng của họ bằng cách sử dụng nút toggle ở đầu cài đặt Lightning.

![image](assets/en/34.webp)

#### Tùy chọn thanh toán Lightning

Chủ cửa hàng có thể thiết lập các tham số sau để nâng cao trải nghiệm Lightning cho khách hàng của họ.

- Hiển thị số lượng thanh toán Lightning bằng Satoshis.
- Thêm gợi ý các kênh riêng tư vào hóa đơn Lightning.
- Thống nhất URL/QR code thanh toán on-chain và Lightning tại điểm thanh toán.
- Thiết lập mẫu mô tả cho hóa đơn lightning.

#### LNURL

Chủ cửa hàng có thể chọn sử dụng hoặc không sử dụng LNURL. Một URL của Lightning Network, hay LNURL, là một tiêu chuẩn đề xuất cho các tương tác giữa người thanh toán Lightning và người nhận thanh toán. Nói ngắn gọn, một LNURL là một url được mã hóa bech32 có tiền tố là lnurl. Ví Lightning sẽ giải mã URL, liên hệ với URL, và chờ đợi một đối tượng JSON với hướng dẫn tiếp theo, đặc biệt là một thẻ xác định hành vi của LNURL.

- Kích hoạt LNURL
- Chế độ LNURL Cổ điển
  - Đối với sự tương thích ví, mã hóa Bech32 (cổ điển) so với URL văn bản rõ ràng (sắp tới)
- Cho phép người nhận thanh toán gửi bình luận.

### Ví dụ 1

#### Kết nối với Lightning bằng node nội bộ (Quản trị viên)

Tùy chọn này chỉ có sẵn nếu bạn là quản trị viên của phiên bản này hoặc nếu quản trị viên đã thay đổi cài đặt mặc định nơi người dùng có thể sử dụng Lightning Node nội bộ.

Là một quản trị viên, nhấp vào ví Lightning trong thanh menu bên trái. BTCPay Server sẽ yêu cầu sử dụng một trong hai tùy chọn để kết nối một Lightning Node, một node nội bộ hoặc một node bên ngoài tùy chỉnh. Nhấp vào `Sử dụng node nội bộ - Use internal node` và nhấp lưu.

#### Quản lý Lightning Node của bạn (RTL)

Sau khi kết nối với Lightning Node nội bộ, BTCPay Server sẽ cập nhật và hiển thị thông báo "Lightning Node đã được cập nhật - BTC Lightning node updated", xác nhận bạn đã kết nối Lightning với cửa hàng của mình.

Quản lý Lightning Node là nhiệm vụ của quản trị viên máy chủ. Điều này bao gồm:

- Quản lý giao dịch
- Quản lý thanh khoản
  - Thanh khoản đầu vào
  - Thanh khoản đầu ra
- Quản lý đối tác và kênh
  - Đối tác đã kết nối
  - Phí của kênh
  - Trạng thái kênh
- Thực hiện sao lưu thường xuyên các trạng thái kênh.
- Kiểm tra báo cáo định tuyến.
- Hoặc sử dụng các dịch vụ như Loop.

Tất cả các công việc quản lý Lightning Node đều được thực hiện thông qua RTL (giả sử bạn đang chạy trên bản triển khai LND). Quản trị viên có thể nhấp vào Lightning Wallet trong BTCPay Server và tìm nút để mở RTL. Bảng điều khiển chính của BTCPay Server giờ đây được cập nhật với các ô Lightning Network, bao gồm quyền truy cập nhanh đến RTL.

### Ví dụ 2

#### Kết nối với Lightning qua Alby

Khi kết nối với một đơn vị giữ hộ (custodial) như Alby, chủ cửa hàng trước tiên nên tạo một tài khoản, truy cập: https://getalby.com/

![hình ảnh](assets/en/35.webp)

Sau khi tạo tài khoản Alby, đi đến cửa hàng BTCPay Server của bạn.

Bước 1: Nhấp vào 'Cài đặt một Lightning Node - Set up a Lightning node' trên Bảng điều khiển hoặc 'Lightning' dưới mục ví.

![hình ảnh](assets/en/36.webp)

Bước 2: Nhập thông tin xác thực kết nối ví được cung cấp bởi Alby. Trên bảng điều khiển (Dashboard) của Alby, nhấp vào ví. Tại đây bạn sẽ tìm thấy "Wallet Connection Credentials". Sao chép các thông tin này. Dán thông tin xác thực từ Alby vào trường cấu hình kết nối trong BTCPay Server.

![hình ảnh](assets/en/37.webp)

Bước 3: Sau khi cung cấp cho BTCPay Server các chi tiết kết nối, nhấp vào nút "Test Connection" để đảm bảo kết nối hoạt động đúng cách. Chú ý đến thông báo "Kết nối tới Lightning Node thành công - Connection to lightning node successful" ở đầu màn hình của bạn. Điều này xác nhận mọi thứ hoạt động ổn định.

![hình ảnh](assets/en/38.webp)

Bước 4: Nhấp lưu, và cửa hàng của bạn giờ đây đã được kết nối với một Lightning Node thông qua Alby.

![hình ảnh](assets/en/39.webp)

**!Lưu ý!**

Không bao giờ tin tưởng một giải pháp Lightning giữ hộ với giá trị nhiều hơn só tiền bạn sẵn lòng mất.

### Tóm tắt kỹ năng

Trong phần này bạn đã học:

- Cách kết nối một Lightning Node nội bộ hoặc bên ngoài
- Nội dung và chức năng của các ô liên quan đến Lightning trên Bảng điều khiển
- Cách cấu hình ví Lightning sử dụng Voltage Surge hoặc Alby

### Đánh giá kiến thức thực hành

Mô tả một số lựa chọn khác nhau để kết nối ví Lightning với cửa hàng của bạn.

# Giao diện BTCPay Server

<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>

## Tổng quan về bảng điều khiển (Dashboard)

<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>

BTCPay Server là một gói phần mềm được đóng gói thành các mô-đun. Tuy nhiên, có những tiêu chuẩn mà mọi BTCPay Server đều có và quản trị viên/người dùng sẽ tương tác với. Bắt đầu với bảng điều khiển. Điểm vào chính của mọi BTCPay Server sau khi đăng nhập. Bảng điều khiển cung cấp giao diện tổng quan về hiệu suất của cửa hàng, số dư ví hiện tại, và các giao dịch cuối cùng trong 7 ngày qua. Vì đây là một cái nhìn có tính chất mô-đun, các Plugin có thể tận dụng cái nhìn này cho lợi ích của mình và tạo các ô của riêng họ trên bảng điều khiển. Trong hướng dẫn này, chúng tôi chỉ nói về các plugin/ứng dụng tiêu chuẩn và giao diện tương ứng của chúng qua BTCPay Server.

### Các ô trên bảng điều khiển

Trong giao diện chính của bảng điều khiển BTCPay Server có một số ô tiêu chuẩn có sẵn. Các ô này dành cho chủ cửa hàng hoặc quản trị viên để họ có thể nhanh chóng quản lý cửa hàng của mình trong giao diện tổng quan.

- Số dư ví
- Hoạt động giao dịch
- Số dư Lightning (nếu Lightning được kích hoạt trên cửa hàng)
- Dịch vụ Lightning (nếu Lightning được kích hoạt trên cửa hàng)
- Giao dịch gần đây.
- Hóa đơn gần đây
- Các chiến dịch gây quỹ cộng đồng đang hoạt động
- Hiệu suất cửa hàng / các mặt hàng bán chạy nhất.

### Số dư ví - Wallet Balance
  Ô số dư ví cung cấp cái nhìn tổng quan nhanh về tiền trong ví và hiệu suất ví của bạn. Chúng ta có thể xem bằng BTC hoặc tiền pháp định trong biểu đồ hàng tuần, hàng tháng, hoặc hàng năm.
  ![image](assets/en/40.webp)

### Hoạt động giao dịch - Transaction Activity

Cạnh ô số dư ví, BTCPay Server hiển thị tổng quan nhanh về các khoản thanh toán đang chờ, số lượng giao dịch trong 7 ngày qua, và nếu cửa hàng của bạn đã phát hành bất kỳ khoản hoàn tiền nào. Nhấn vào nút quản lý sẽ đưa bạn vào khu vực quản lý các khoản thanh toán đang chờ (tìm hiểu thêm về thanh toán trong BTCPay Server - chương về Thanh toán).

![image](assets/en/41.webp)

### Số dư Lightning - Lightning Balance

Chỉ hiển thị khi Lightning được kích hoạt.

Khi quản trị viên đã cấp phép cho Lightning Network, bảng điều khiển BTCPay Server giờ đây có một ô mới với thông tin về Lightning Node của bạn. Bao nhiêu BTC trong các kênh, các kênh này được cân bằng cục bộ hay từ xa (dung lượng vào hoặc ra) nếu các kênh đang đóng hoặc mở, và bao nhiêu bitcoin được giữ on-chain trên Lightning Node.

![image](assets/en/42.webp)

### Dịch vụ Lightning - Lightning Services

Chỉ hiển thị khi lightning được kích hoạt.

Bên cạnh việc xem số dư Lightning trên bảng điều khiển BTCPay Server, các quản trị viên cũng sẽ thấy ô cho Dịch vụ Lightning. Tại đây, các quản trị viên có thể tìm thấy các nút thao tác nhanh cho các công cụ họ sử dụng để quản lý Lightning Node của mình; ví dụ, Ride the Lightning (RTL) là một trong những công cụ tiêu chuẩn với BTCPay Server cho quản lý Lightning Node.

![image](assets/en/43.webp)

### Giao dịch gần đây - Recent Transactions

Ô giao dịch gần đây sẽ hiển thị các giao dịch gần đây nhất từ cửa hàng của bạn. Chỉ với một cú nhấp, quản trị viên của BTCPay Server Instance có thể xem giao dịch mới nhất và xem liệu có cần chú ý đến nó không.

![image](assets/en/44.webp)

### Hóa đơn gần đây - Recent invoices

Ô hóa đơn gần đây hiển thị 6 hóa đơn mới nhất được tạo bởi BTCPay Server của bạn, bao gồm trạng thái và số tiền hóa đơn. Ô cũng bao gồm một nút "Xem tất cả - View all" để dễ dàng truy cập dữ liệu hóa đơn đầy đủ.

![image](assets/en/45.webp)

### Điểm bán hàng và huy động vốn cộng đồng - Point of Sale and Crowdfunds

Vì BTCPay Server cung cấp một bộ plugin hoặc ứng dụng tiêu chuẩn, điểm bán hàng và huy động vốn cộng đồng là hai plugin chính của BTCPay Server. Với mỗi cửa hàng và ví, người dùng BTCPay Server có thể tạo bất kỳ điểm bán hàng hoặc đợt huy động vốn cộng đồng nào mà họ thấy phù hợp. Mỗi cái sẽ tạo một ô bảng điều khiển mới hiển thị hiệu suất của plugin.

![image](assets/en/46.webp)

Chú ý sự khác biệt nhỏ giữa ô điểm bán hàng và ô huy động vốn cộng đồng. Quản trị viên thấy các mặt hàng bán chạy nhất trong ô điểm bán hàng. Trong ô huy động vốn cộng đồng, điều này trở thành Top Perks. Cả hai ô đều có các nút thao tác nhanh để quản lý ứng dụng tương ứng và xem các hóa đơn gần đây được tạo bởi các mặt hàng hàng đầu hoặc top perks.

![image](assets/en/47.webp)

**!?Lưu Ý!?**

Biểu đồ số dư và giao dịch gần đây chỉ có sẵn cho phương thức thanh toán trên chuỗi. Thông tin về số dư và giao dịch Lightning Network đang trong danh sách công việc cần làm. Tính đến Phiên bản BTCPay Server 1.6.0, số dư Lightning cơ bản đã có sẵn.

### Tóm tắt kỹ năng

Trong phần này, bạn đã học được những điều sau:

- Cấu trúc cơ bản của các ô trên bảng điều khiển
- Hiểu biết cơ bản về nội dung của mỗi ô.

### Đánh giá kiến thức

Liệt kê càng nhiều ô của bảng điều khiển từ trí nhớ của bạn càng tốt

## BTCPay Server - Cài đặt cửa hàng

<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>
Trong phần mềm BTCPay Server, chúng ta biết đến 2 loại cài đặt. Cài đặt cụ thể cho Cửa hàng BTCPay Server, nút cài đặt được tìm thấy ở thanh menu bên trái dưới bảng điều khiển - dashboard, và cài đặt BTCPay Server, được tìm thấy ở cuối thanh menu ngay trên Account. Cài đặt cụ thể cho Server BTCPay Server chỉ có thể xem được bởi các quản trị viên máy chủ.
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

### Cài đặt chung - General

Trong tab cài đặt Chung, chủ cửa hàng thiết lập thương hiệu và mặc định thanh toán của họ. Tại thiết lập ban đầu của cửa hàng, một tên cửa hàng đã được đặt; điều này sẽ được phản ánh trong Cài đặt chung dưới Store Name - Tên cửa hàng. Tại đây, chủ cửa hàng cũng có thể thiết lập trang web của họ để phù hợp với thương hiệu và một Store ID để quản trị viên nhận biết trong cơ sở dữ liệu.

#### Thương hiệu - Branding

Vì BTCPay Server là FOSS, chủ cửa hàng có thể làm thương hiệu tùy chỉnh để phù hợp với cửa hàng của mình. Thiết lập màu sắc thương hiệu, lưu trữ logo của thương hiệu và thêm CSS tùy chỉnh cho các trang đối diện với khách hàng/công chúng (Hóa đơn, Yêu cầu thanh toán, Rút tiền)

#### Thanh toán - Payment

Trong cài đặt thanh toán, chủ cửa hàng thiết lập tiền tệ mặc định cho cửa hàng của họ (bằng Bitcoin hoặc bất kỳ đồng tiền pháp định nào).

#### Cho phép bất kỳ ai tạo hóa đơn

Cài đặt này dành cho các nhà phát triển hoặc người xây dựng trên BTCPay Server. Với cài đặt này được bật cho cửa hàng của bạn, nó cho phép thế giới bên ngoài tạo hóa đơn trên BTCPay Server Instance của bạn.

#### Thêm phí bổ sung (phí mạng lưới) vào hóa đơn

Một tính năng trong BTCPay để bảo vệ các nhà bán hàng khỏi các cuộc tấn công bụi hoặc khách hàng gây ra chi phí cao về phí sau này khi nhà bán hàng cần di chuyển một lượng lớn bitcoin cùng một lúc. Ví dụ, khách hàng tạo một hóa đơn 20$ và thanh toán một phần, trả 1$ 20 lần cho đến khi hóa đơn được thanh toán đầy đủ. Bây giờ nhà bán hàng có một giao dịch lớn hơn, làm tăng chi phí khai thác trong trường hợp nhà bán hàng quyết định di chuyển số tiền đó sau này. Mặc định, BTCPay áp dụng một khoản phí mạng lưới bổ sung vào tổng số tiền của hóa đơn để bao gồm chi phí đó cho nhà bán hàng khi hóa đơn được thanh toán bằng nhiều giao dịch. BTCPay cung cấp một số tùy chọn để tùy chỉnh tính năng bảo vệ này. Bạn có thể áp dụng phí mạng:

- Chỉ khi khách hàng thực hiện nhiều hơn một lần thanh toán cho hóa đơn (Trong ví dụ trên, nếu khách hàng tạo một hóa đơn 20\$ và trả 1\$, tổng số tiền hóa đơn còn nợ bây giờ là 19\$ + phí mạng lưới. Phí mạng lưới được áp dụng sau lần thanh toán đầu tiên)
- Trên mỗi lần thanh toán (bao gồm cả lần thanh toán đầu tiên, trong ví dụ của chúng ta, tổng số sẽ là 20\$ + phí mạng lưới ngay lập tức, ngay cả trong lần thanh toán đầu tiên)
- Không bao giờ thêm phí mạng lưới (vô hiệu hóa hoàn toàn phí mạng lưới)

Mặc dù nó bảo vệ khỏi các giao dịch bụi, nhưng nó cũng có thể ảnh hưởng tiêu cực đối với doanh nghiệp nếu không được thông báo đúng cách. Khách hàng có thể có thắc mắc và nghĩ rằng bạn đang tính phí quá cao.

#### Hóa đơn hết hạn nếu số tiền đầy đủ không được thanh toán sau?

Bộ đếm thời gian của hóa đơn được thiết lập mặc định là 15 phút. Bộ đếm thời gian là một cơ chế bảo vệ chống lại sự biến động vì nó khóa số lượng bitcoin theo tỷ giá bitcoin / tiền pháp định. Nếu khách hàng không thanh toán hóa đơn trong khoảng thời gian đã định, hóa đơn được coi là hết hạn. Hóa đơn được coi là "đã thanh toán" ngay khi giao dịch hiển thị trên blockchain (0-xác nhận) nhưng được coi là "hoàn thành" khi đạt được số lần xác nhận mà nhà bán hàng đã định (thường là 1-6). Bộ đếm thời gian có thể tùy chỉnh theo phút.

#### Xem xét hóa đơn đã thanh toán ngay cả khi số tiền thanh toán ít hơn X% so với dự kiến?

Khi khách hàng sử dụng ví sàn giao dịch để trực tiếp thanh toán cho một hóa đơn, sàn giao dịch sẽ thu một khoản phí nhỏ. Điều này có nghĩa là hóa đơn đó không được coi là đã thanh toán hoàn toàn. Hóa đơn sẽ nhận được trạng thái "đã thanh toán một phần". Bạn có thể thiết lập tỷ lệ phần trăm ở đây nếu một người bán hàng muốn chấp nhận hóa đơn thanh toán thiếu.

### Tỷ giá - Rates

Trong BTCPay Server, khi một hóa đơn được tạo ra, nó luôn cần có thông tin chính xác và cập nhật nhất về mức giá của bitcoin theo tiền pháp định. Khi tạo một cửa hàng mới trong BTCPay Server, quản trị viên được yêu cầu thiết lập nguồn giá ưa thích của họ; sau khi cửa hàng được thiết lập, chủ sở hữu cửa hàng luôn có thể thay đổi nguồn giá của mình trong tab này.

#### Quy tắc tỷ giá nâng cao

Chủ yếu được sử dụng bởi người dùng có kinh nghiệm. Nếu được bật, chủ sở hữu cửa hàng có thể tạo các kịch bản xung quanh hành vi giá và cách tính phí khách hàng của họ.

#### Kiểm tra

Một nơi kiểm tra nhanh cho các cặp tiền tệ ưa thích của bạn. Điều này cũng bao gồm tính năng kiểm tra các cặp tiền tệ mặc định qua truy vấn REST.

### Giao diện thanh toán - Checkout Appearance

Tab giao diện thanh toán bắt đầu với các cài đặt cụ thể cho hóa đơn và phương thức thanh toán mặc định, và kích hoạt các phương thức thanh toán cụ thể khi đáp ứng được các yêu cầu đã thiết lập.

#### Cài đặt hóa đơn

Phương thức thanh toán mặc định. BTCPay Server trong cấu hình tiêu chuẩn có ba lựa chọn.

- BTC (On-chain)
- BTC (LNURL-pay)
- BTC (Off-chain & Lightning)

Chúng ta có thể thiết lập các tham số cho cửa hàng của mình, nơi khách hàng chỉ tương tác với Lightning khi giá nhỏ hơn X và ngược lại cho giao dịch trên chuỗi khi X lớn hơn Y.

![image](assets/en/48.webp)

#### Thanh toán

Tính đến phiên bản phát hành 1.7 của BTCPay Server, một giao diện thanh toán mới đã được giới thiệu, được gọi là Checkout V2. Kể từ phiên bản 1.9 được chuẩn hóa, quản trị viên và chủ sở hữu cửa hàng vẫn có thể thiết lập giao diện thanh toán về phiên bản trước. Bằng cách sử dụng chuyển đổi "Sử dụng giao diện thanh toán cổ điển - Use the classic checkout", chủ sở hữu cửa hàng có thể đặt cửa hàng trở lại trải nghiệm thanh toán trước đó. BTCPay Server cũng có một bộ các cài đặt sẵn cho thương mại điện tử hoặc trải nghiệm tại cửa hàng.

![image](assets/en/49.webp)

Khi khách hàng tương tác với cửa hàng và tạo ra một hóa đơn, có một thời gian hết hạn cho hóa đơn. Theo mặc định, BTCPay Server thiết lập giới hạn này là 5 phút, và quản trị viên có thể thiết lập giới hạn này theo mức họ thấy phù hợp. Trang thanh toán có thể được tùy chỉnh thêm bằng cách kiểm tra các tham số sau:

- Chào mừng việc thanh toán bằng cách hiển thị hiệu ứng tung hoa
- Hiển thị thông tin thương hiệu cửa hàng (Tên và logo)
- Hiển thị nút "Thanh toán trong ví"
- Thống nhất URL/QR của thanh toán on-chain và off-chain
- Hiển thị khoản thanh toán Lightning bằng Satoshis
- Tự động phát hiện ngôn ngữ khi thanh toán

![image](assets/en/50.webp)

Khi chức năng tự động phát hiện ngôn ngữ không được thiết lập, BTCPay Server, theo mặc định, sẽ hiển thị tiếng Anh. Chủ sở hữu cửa hàng có thể thay đổi mặc định này sang ngôn ngữ ưa thích của họ.

![image](assets/en/51.webp)

Nhấp vào nút sổ xuống và chủ cửa hàng có thể thiết lập một Tiêu đề HTML tùy chỉnh để hiển thị trên trang thanh toán.

![image](assets/en/52.webp)

Để đảm bảo khách hàng biết phương thức thanh toán của mình, chủ cửa hàng có thể thiết lập rõ ràng rằng thanh toán của mình luôn yêu cầu người dùng chọn phương thức thanh toán ưa thích của họ. Khi hóa đơn được thanh toán, BTCPay Server cho phép khách hàng quay trở lại cửa hàng trực tuyến. Chủ cửa hàng có thể thiết lập điều hướng này sau khi khách hàng đã thanh toán tự động.

![image](assets/en/53.webp)

#### Biên lai công khai

Trong cài đặt biên lai công khai, chủ cửa hàng có thể thiết lập các trang biên lai thành công khai và hiển thị danh sách thanh toán trên trang biên lai cũng như mã QR của biên lai để khách hàng dễ dàng truy cập điện tử.
![image](assets/vi/54.webp)

### Token truy cập

Token truy cập được sử dụng để ghép nối với một số tích hợp thương mại điện tử hoặc tích hợp xây dựng tùy chỉnh.

![image](assets/vi/55.webp)

### Người Dùng

Người dùng cửa hàng là nơi chủ cửa hàng có thể quản lý nhân viên của mình, tài khoản của họ và quyền truy cập vào cửa hàng. Sau khi nhân viên tạo tài khoản của họ, chủ cửa hàng có thể thêm người dùng cụ thể vào cửa hàng dưới dạng khách hoặc chủ sở hữu. Để xác định thêm vai trò của nhân viên, tham khảo phần tiếp theo về “Cài đặt cửa hàng BTCPay Server - Vai trò.”

![image](assets/vi/56.webp)

### Vai Trò

Chủ cửa hàng có thể thấy vai trò tiêu chuẩn của người dùng không đủ quan trọng. Trong cài đặt vai trò tùy chỉnh, chủ cửa hàng có thể xác định nhu cầu cụ thể cho mỗi vai trò trong doanh nghiệp của mình.

(1) Để tạo một vai trò mới, nhấn vào nút "+ Thêm vai trò - Add role".

![image](assets/vi/57.webp)

(2) Nhập tên Vai trò, ví dụ, "Thu Ngân - Cashier".

![image](assets/vi/58.webp)

(3) Thiết lập các quyền riêng cho từng vai trò.

- Chỉnh sửa cửa hàng của bạn.
- Quản lý tài khoản sàn giao dịch liên kết với cửa hàng của bạn.
  - Xem tài khoản sàn giao dịch liên kết với cửa hàng của bạn.
- Quản lý các yêu cầu thanh toán của bạn.
- Tạo các khoản thanh toán kéo - Pull Payment.
  - Tạo các khoản thanh toán kéo không được phê duyệt.
- Chỉnh sửa hóa đơn.
  - Xem hóa đơn.
  - Tạo hóa đơn.
  - Tạo hóa đơn từ các Lightning Node liên kết với cửa hàng của bạn.
- Xem cửa hàng của bạn.
  - Xem hóa đơn.
  - Xem các yêu cầu thanh toán của bạn.
  - Chỉnh sửa webhook của cửa hàng.
- Chỉnh sửa các yêu cầu thanh toán của bạn.
  - Xem các yêu cầu thanh toán của bạn.
- Sử dụng các Lightning Node liên kết với cửa hàng của bạn.
  - Xem các hóa đơn Lightning liên kết với cửa hàng của bạn.
  - Tạo hóa đơn từ các Lightning Node liên kết với cửa hàng của bạn.
- Gửi tiền vào tài khoản sàn giao dịch liên kết với cửa hàng của bạn.
- Rút tiền từ tài khoản sàn giao dịch về cửa hàng của bạn.
- Giao dịch tiền trên tài khoản sàn giao dịch của cửa hàng.

Khi vai trò được tạo, tên sẽ được cố định và không thể thay đổi sau đó ở chế độ chỉnh sửa.

![image](assets/vi/59.webp)

### Webhooks

Trong BTCPay Server, việc tạo một "Webhook" mới khá dễ dàng. Trong tab Cài đặt cửa hàng BTCPay Server - Webhooks, chủ cửa hàng có thể dễ dàng tạo một webhook mới bằng cách nhấn vào "+ Tạo Webhook - + Add Webhook". Webhooks cho phép BTCPay Server gửi các sự kiện HTTP liên quan đến cửa hàng của bạn đến các máy chủ khác hoặc tích hợp thương mại điện tử.

![image](assets/vi/60.webp)

Bạn đang ở trong giao diện tạo Webhook. Đảm bảo bạn biết URL Payload của mình và dán nó vào BTCPay Server của bạn. Trong khi bạn đã dán URL Payload, phía dưới nó hiển thị bí mật webhook. Sao chép bí mật webhook và cung cấp nó cho đầu cuối. Khi mọi thứ đã được thiết lập, bạn có thể chuyển đổi trong BTCPay Server để Giao lại tự động. Chúng ta sẽ cố gắng giao lại bất kỳ giao hàng nào thất bại sau 10 giây, 1 phút, và lên đến 6 lần sau 10 phút. Bạn có thể chuyển đổi giữa mọi sự kiện hoặc chỉ định các sự kiện theo nhu cầu của bạn. Hãy chắc chắn kích hoạt webhook (Enabled) và nhấn Thêm webhook để lưu nó.

![image](assets/vi/61.webp)

Webhooks không được thiết kế để tương thích với API Bitpay. Có hai IPN riêng biệt (trong thuật ngữ BitPay: "Thông báo thanh toán tức thì") trong BTCPay Server.

- Webhook
- Thông báo

Chỉ sử dụng URL thông báo khi bạn tạo hóa đơn qua API Bitpay.

### Các bộ xử lý xuất chi - Payout Processors

Các bộ xử lý xuất chi hoạt động cùng với khái niệm xuất chi (Payout) trong BTCPay Server. Một trình tổng hợp xuất chi để gộp nhiều giao dịch và gửi chúng cùng một lúc. Với các bộ xử lý xuất chi, chủ cửa hàng có thể tự động hóa việc xuất chi cho nhiều khoản cùng một lúc. BTCPay Server cung cấp hai phương thức xuất chi tự động, On-chain và Off-chain (LN).
Chủ cửa hàng có thể nhấp vào và cấu hình cho cả hai bộ xử lý xuất chi riêng biệt. Chủ cửa hàng có thể chỉ muốn chạy bộ xử lý On-chain mỗi X giờ một lần, trong khi Off-chain có thể diễn ra mỗi vài phút. Đối với On-chain, bạn cũng có thể thiết lập mục tiêu về khối mà giao dịch nên được gắn vào. Theo mặc định, điều này được thiết lập là 1 (có nghĩa là khối tiếp theo có sẵn). Lưu ý rằng việc thiết lập bộ xử lý thanh toán Off-chain chỉ có bộ hẹn giờ và không có mục tiêu khối. Các khoản thanh toán qua mạng Lightning là tức thì.

![hình ảnh](assets/en/62.webp)
![hình ảnh](assets/en/63.webp)

Chủ cửa hàng chỉ có thể cấu hình bộ xử lý Nn-chain nếu họ có một ví nóng kết nối với cửa hàng của họ.

![hình ảnh](assets/en/64.webp)

Sau khi thiết lập một bộ xử lý xuất chi, bạn có thể nhanh chóng loại bỏ hoặc chỉnh sửa nó bằng cách quay trở lại tab bọ xử lý xuất chi - Payout Processors trong cài đặt cửa hàng trên BTCPay Server.

**!?Lưu ý!?**

Bộ xử lý xuất chi On-chain chỉ có thể hoạt động trên một cửa hàng được cấu hình với một ví nóng đã kết nối. Nếu không có ví nóng được kết nối, BTCPay Server không giữ chìa khóa của ví và sẽ không thể tự động xử lý các khoản xuất chi.

### Các email

BTCPay Server có thể sử dụng các email để gửi thông báo hoặc, khi được thiết lập đúng cách, để khôi phục các tài khoản đã được tạo trên hệ thống, vì theo tiêu chuẩn BTCPay Server không gửi email khi mật khẩu bị mất.

![hình ảnh](assets/en/65.webp)

Trước khi chủ cửa hàng có thể thiết lập các quy tắc email để kích hoạt chúng dựa trên các sự kiện cụ thể, chúng ta phải thiết lập một số cài đặt email cơ bản. BTCPay Server cần những cài đặt này để gửi email dựa trên các sự kiện cụ thể của cửa hàng hoặc để đặt lại mật khẩu.

BTCPay Server đã làm cho việc điền thông tin này dễ dàng hơn bằng cách sử dụng tùy chọn "Điền nhanh - Quick Fill":

- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid

Bằng cách sử dụng tùy chọn điền nhanh, BTCPay Server sẽ tự động điền các trường cho máy chủ SMTP và cổng; bây giờ, chủ cửa hàng chỉ cần điền thông tin đăng nhập của mình vào địa chỉ Email, Đăng nhập (thường giống với địa chỉ email của bạn), và mật khẩu của bạn. Tùy chọn nâng cao mà BTCPay Server cung cấp trong cài đặt email là Vô hiệu hóa kiểm tra bảo mật của Chứng chỉ TLS; theo mặc định, điều này được Bật.

![hình ảnh](assets/en/66.webp)

Với các quy tắc Email, chủ cửa hàng có thể thiết lập các sự kiện cụ thể để kích hoạt email đến các địa chỉ email cụ thể.

- Hóa đơn được tạo
- Hóa đơn thanh toán đã nhận
- Hóa đơn đang xử lý
- Hóa đơn hết hạn
- Hóa đơn đã quyết toán
- Hóa đơn không hợp lệ
- Hoá đơn thanh toán đã được quyết toán

Nếu khách hàng đã cung cấp địa chỉ Email, những kích hoạt này cũng có thể gửi thông tin cho khách hàng. Chủ cửa hàng có thể tự điền dòng `Chủ đề - Subject` để làm rõ lý do tại sao Email này được gửi và điều gì đã kích hoạt nó.

![hình ảnh](assets/en/67.webp)

### Forms - Các biểu mẫu

Vì BTCPay Server không thu thập bất kỳ dữ liệu nào, chủ cửa hàng có thể muốn thêm một biểu mẫu tùy chỉnh vào trải nghiệm thanh toán của họ; theo cách này, chủ cửa hàng có thể thu thập thêm thông tin từ khách hàng của mình. Bộ xây dựng biểu mẫu của BTCPay Server bao gồm hai phần, một giao diện trực quan và một giao diện nâng cao.
Khi tạo một biểu mẫu mới, BTCPay Server mở một cửa sổ mới yêu cầu thông tin cơ bản về những yêu cầu mà biểu mẫu mới của bạn đưa ra. Đầu tiên, chủ cửa hàng cần đặt một tên rõ ràng cho biểu mẫu mới của mình, tên này KHÔNG thể thay đổi sau khi đã được thiết lập.
![image](assets/en/68.webp)

Sau khi chủ cửa hàng đặt tên cho biểu mẫu, bạn cũng có thể chuyển công tắc "Cho phép biểu mẫu sử dụng công cộng - Allow form for public use" sang ON, và nó sẽ chuyển sang màu xanh. Điều này giúp cho biểu mẫu được sử dụng ở mọi nơi có tiếp xúc với khách hàng. Ví dụ, nếu một chủ cửa hàng tạo 1 hóa đơn riêng biệt không qua điểm bán hàng của mình, anh ta vẫn muốn thu thập thông tin từ khách hàng; việc chuyển sang ON cho phép thu thập thông tin đó.

![image](assets/en/69.webp)

Mỗi biểu mẫu bắt đầu với ít nhất 1 trường biểu mẫu mới. Chủ cửa hàng có thể chọn loại trường nào theo ý mình:

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

BTCPay Server cũng cho phép bạn xây dựng biểu mẫu trong bằng việc lập trình mã code. Cụ thể là JSON. Thay vì nhìn vào trình soạn thảo, chủ cửa hàng có thể nhấp vào nút CODE ngay cạnh trình soạn thảo và vào phần mã code của Biểu mẫu của họ. Trong định nghĩa trường, chỉ có các trường sau có thể được thiết lập; giá trị của các trường được lưu trong metadata của hóa đơn:

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
| .fields.required      | Nếu đúng, trường sẽ được yêu cầu                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| .fields.label         | Nhãn của trường                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| .fields.helpText      | Văn bản bổ sung để cung cấp giải thích cho trường.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| .fields.fields        | Bạn có thể tổ chức các trường của mình theo một cấu trúc phân cấp, cho phép các trường con được lồng vào metadata của hóa đơn. Cấu trúc này có thể giúp bạn tổ chức và quản lý thông tin thu thập được một cách tốt hơn, làm cho việc truy cập và giải thích thông tin trở nên dễ dàng hơn. Ví dụ, nếu bạn có một biểu mẫu thu thập thông tin khách hàng, bạn có thể nhóm các trường dưới một trường cha có tên là khách hàng. Trong trường cha này, bạn có thể có các trường con như tên, Email, và địa chỉ. |

Tên trường đại diện cho tên thuộc tính JSON lưu trữ giá trị do người dùng cung cấp trong metadata của hóa đơn. Một số tên quen thuộc có thể được diễn giải và thay đổi cài đặt của hóa đơn.

| Tên trường       | Mô tả               |
| ---------------- | ------------------- |
| invoice_amount   | Số tiền của hóa đơn |
| invoice_currency | Loại tiền tệ của hóa đơn |

Bạn có thể tự động điền trước các trường của hóa đơn bằng cách thêm chuỗi truy vấn vào URL của biểu mẫu, như "?your_field=value".

Dưới đây là một số trường hợp sử dụng cho tính năng này:

- Hỗ trợ nhập liệu của người dùng: Điền trước các trường với thông tin khách hàng đã biết để giúp họ hoàn thành biểu mẫu dễ dàng hơn. Ví dụ, nếu bạn đã biết địa chỉ email của một khách hàng, bạn có thể điền trước trường email để tiết kiệm thời gian cho họ.
- Cá nhân hóa: Tùy chỉnh biểu mẫu dựa trên sở thích hoặc phân loại khách hàng. Ví dụ, nếu bạn có các cấp độ khách hàng khác nhau, bạn có thể điền trước biểu mẫu với dữ liệu liên quan, như cấp độ thành viên của họ hoặc các ưu đãi cụ thể.
- Theo dõi: Theo dõi nguồn gốc của lượt truy cập từ khách hàng bằng cách sử dụng các trường ẩn và giá trị điền trước. Ví dụ, bạn có thể tạo liên kết với các giá trị utm_media được điền trước cho mỗi kênh tiếp thị (ví dụ, Twitter, Facebook, Email). Điều này giúp bạn phân tích hiệu quả của các nỗ lực tiếp thị của mình.
- Thử nghiệm A/B: Điền trước các trường với các giá trị khác nhau để thử nghiệm các phiên bản biểu mẫu khác nhau, cho phép bạn tối ưu hóa trải nghiệm người dùng và tỷ lệ chuyển đổi.

### Tóm tắt kỹ năng

Trong phần này, bạn đã học được những điều sau:

- Bố cục và chức năng của các tab trong phần Cài đặt cửa hàng
- Nhiều lựa chọn để điều chỉnh việc xử lý tỷ giá hối đoái cơ bản, thanh toán một phần, thanh toán thiếu một chút, và hơn nữa.
- Tùy chỉnh giao diện thanh toán, bao gồm cả sử dụng On-chain hoặc Lightning tùy thuộc vào mức giá trên hóa đơn.
- Quản lý cấp độ truy cập và quyền hạn của cửa hàng qua các vai trò.
- Cấu hình tự động việc gửi email và các kích hoạt của chúng
- Tạo biểu mẫu tùy chỉnh để thu thập thông tin khách hàng khi thanh toán.

### Đánh giá kiến thức

#### Đánh kiến thức

Sự khác biệt giữa Cài đặt cửa hàng (Store Settings) và Cài đặt máy chủ (Server Settings) là gì?

#### Giả Định KA

Mô tả một số lựa chọn bạn có thể chọn trong Giao diện thanh toán > Cài đặt hoá đơn, và lý do tại sao.

## BTCPay Server - Cài đặt máy chủ

<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>

BTCPay Server bao gồm hai giao diện cài đặt khác nhau. Một dành cho Cài đặt cưa hàng và một dành cho Cài đặt máy chủ. Cài đặt máy chủ chỉ có sẵn nếu bạn là quản trị viên máy chủ và không dành cho chủ cửa hàng. Quản trị viên máy chủ có thể thêm người dùng, tạo vai trò tùy chỉnh, cấu hình email, thiết lập chính sách, thực hiện các nhiệm vụ bảo trì, kiểm tra tất cả các dịch vụ gắn với BTCPay Server, tải tệp tin lên máy chủ, hoặc kiểm tra nhật ký.

### Người dùng

Như đã đề cập trong phần trước, quản trị viên máy chủ có thể mời người dùng tham gia vào máy chủ của họ bằng cách thêm họ vào tab `Người dùng - User`.

### Vai trò tùy chỉnh trên máy chủ

BTCPay Server biết hai loại vai trò tùy chỉnh, vai trò tùy chỉnh cụ thể của cửa hàng và vai trò tùy chỉnh trên toàn máy chủ trong cài đặt BTCPay Server. Cả hai đều có một bộ quyền tương tự; tuy nhiên, nếu được thiết lập thông qua tab `Cài đặt BTCPay Server - Vai trò - BTCPay Server Settings - Roles', vai trò này sẽ có phạm vi trên toàn bộ máy chủ và áp dụng cho nhiều cửa hàng. Lưu ý nhãn "Server-wide" đối với các vai trò tùy chỉnh trong Cài đặt máy chủ.

### Các vai trò tuỳ chỉnh trên toàn máy chủ

Bộ quyền của các vai trò tùy chỉnh trên toàn máy chủ:

- Chỉnh sửa cửa hàng của bạn.
- Quản lý các tài khoản giao dịch liên kết với cửa hàng của bạn.
  - Xem các tài khoản giao dịch liên kết với cửa hàng của bạn.
- Quản lý các khoản yêu cầu thanh toán của bạn.
- Tạo các khoản thanh toán kéo - Pull Payment.
  - Tạo các khoản thanh toán kéo không được phê duyệt.
- Chỉnh sửa hóa đơn.
  - Xem hóa đơn.
  - Tạo hóa đơn.
  - Tạo hóa đơn từ các Lightning Node liên kết với cửa hàng của bạn.
- Xem cửa hàng của bạn.
  - Xem các hóa đơn.
  - Xem các yêu cầu thanh toán của bạn.
  - Chỉnh sửa webhook của cửa hàng.
- Chỉnh sửa các yêu cầu thanh toán của bạn.
  - Xem các yêu cầu thanh toán của bạn.
- Sử dụng các Lightning Node liên kết với cửa hàng của bạn.
  - Xem các hóa đơn Lightning liên kết với cửa hàng của bạn.
  - Tạo hóa đơn từ các Lightning Node liên kết với cửa hàng của bạn.
- Nạp tiền vào các tài khoản sàn giao dịch liên kết với cửa hàng của bạn.
- Rút tiền từ các tài khoản sàn giao dịch về cửa hàng của bạn.
- Giao dịch tiền trên các tài khoản sản giao dịch của cửa hàng.

**!?Lưu ý!?**

Khi vai trò được tạo, tên sẽ được cố định và sau đó không thể thay đổi trong chế độ chỉnh sửa.

### Email

Cài đặt Email trên toàn máy chủ cũng tương tự như cài đặt Email cụ thể của cửa hàng. Tuy nhiên, thiết lập này không chỉ xử lý các kích hoạt cho cửa hàng hoặc nhật ký quản trị viên. Thiết lập Email này cũng làm cho khả năng khôi phục mật khẩu trên BTCPay Server tại trang đăng nhập trở nên khả dụng. Nó hoạt động tương tự như cài đặt cụ thể của cửa hàng; quản trị viên có thể nhanh chóng điền vào các thông số Email của họ và nhập thông tin đăng nhập email, và máy chủ giờ đây có thể gửi email.

### Chính sách

Các quản trị viên chính sách của BTCPay Server có thể thiết lập một số cài đặt về các chủ đề như Cài đặt người dùng hiện hành, Cài đặt người dùng mới, Cài đặt thông báo, và Cài đặt bảo trì. Những cài đặt này dành cho việc đăng ký người dùng mới làm quản trị viên hoặc người dùng bình thường hoặc thậm chí ẩn BTCPay Server khỏi các công cụ tìm kiếm bằng cách thêm server header.

#### Cài đặt người dùng hiện tại - Existing Users

Các tùy chọn có sẵn ở đây tách biệt với các vai trò tùy chỉnh. Những quyền hạn bổ sung này có thể làm cho cửa hàng hoặc chủ cửa hàng dễ bị tấn công. Các chính sách có thể được thêm vào cho người dùng hiện tại:

- Cho phép người dùng không phải admin sử dụng Lightning Node nội bộ trong cửa hàng của họ.
  - Điều này sẽ cho phép chủ cửa hàng sử dụng Lightning Node của quản trị viên máy chủ và do đó, sử dụng tiền của anh ta! Hãy cẩn thận, đây không phải là giải pháp để cung cấp quyền truy cập vào Lightning.
- Cho phép người dùng không phải admin tạo ví nóng cho cửa hàng của họ.
  - Điều này sẽ cho phép bất kỳ ai có tài khoản trên phiên bản BTCPay Server của bạn tạo Ví nóng và lưu trữ hạt giống khôi phục trên máy chủ của quản trị viên. Điều này có thể khiến quản trị viên chịu trách nhiệm của bên thứ ba giữ tiền cho họ (người dùng).
- Cho phép người dùng không phải admin nhập ví nóng cho cửa hàng của họ.
  - Tương tự như chủ đề tạo ví nóng phía trên, chính sách này cho phép nhập một ví nóng, với những nguy hiểm đã được đề cập trong phần tạo ví nóng.

#### Cài đặt người dùng mới - New Users

Chúng ta có thể thiết lập một số cài đặt quan trọng để quản lý người dùng mới đến với máy chủ. Chúng ta có thể thiết lập một email xác nhận cho đăng ký mới, vô hiệu hóa việc tạo người dùng mới qua màn hình đăng nhập, và hạn chế quyền truy cập của người dùng không phải là quản trị viên đến việc tạo người dùng qua API.

- Yêu cầu email xác nhận để đăng ký.
  - Quản trị viên máy chủ phải đã thiết lập một máy chủ email!
- Vô hiệu hóa đăng ký người dùng mới trên máy chủ
- Vô hiệu hóa quyền truy cập của người dùng không phải quản trị viên đến điểm cuối API tạo người dùng

Mặc định, BTCPay Server đã bật vô hiệu hóa đăng ký người dùng mới và tắt quyền truy cập của người dùng không phải quản trị viên đến điểm cuối API tạo người dùng. Điều này xuất phát từ khía cạnh bảo mật, nơi không có người lạ nào có thể tìm thấy trang đăng nhập vào BTCPay trên máy chủ bạn và bắt đầu tạo tài khoản.

#### Cài đặt thông báo

![image](assets/en/76.webp)

#### Cài đặt bảo trì

BTCPay Server là một dự án mã nguồn mở tồn tại trên GitHub. Mỗi khi BTCPay Server phát hành một phiên bản mới của phần mềm, các quản trị viên có thể được thông báo rằng một phiên bản mới đã sẵn sàng. Các quản trị viên cũng có thể muốn ngăn chặn các công cụ tìm kiếm (google, yahoo, duckduckgo) lập chỉ mục tên miền BTCPay Server. Vì BTCPay Server là FOSS, các nhà phát triển trên toàn thế giới có thể muốn tạo ra các tính năng mới; BTCPay Server có một tính năng thử nghiệm khi được bật, và một quản trị viên có thể sử dụng các tính năng không dành cho hoạt động kinh doanh sản xuất thật mà chỉ dùng để thử nghiệm.

- Kiểm tra các bản phát hành trên GitHub và thông báo khi có phiên bản mới của BTCPay Server.
- Ngăn chặn các công cụ tìm kiếm lập chỉ mục trang web này
- Kích hoạt các tính năng thử nghiệm.

![image](assets/en/77.webp)

#### Plugins

BTCPay Server có thể thêm các Plugin và mở rộng bộ tính năng của mình. Các plugin, theo mặc định, được tải từ kho lưu trữ plugin-builder của BTCPay Server. Tuy nhiên, một quản trị viên có thể chọn xem các plugin ở trạng thái Pre-release, và nếu nhà phát triển plugin cho phép, quản trị viên máy chủ có thể cài đặt các phiên bản beta của plugin.

![image](assets/en/78.webp)

##### Cài đặt tuỳ chỉnh

Một bản triển khai BTCPay Server tiêu chuẩn sẽ có thể truy cập thông qua tên miền được thiết lập cho nó khi cài đặt. Tuy nhiên, một quản trị viên máy chủ có thể ánh xạ lại tên miền gốc và hiển thị một trong các ứng dụng đã tạo từ một cửa hàng cụ thể. Quản trị viên máy chủ cũng có thể ánh xạ các tên miền cụ thể cho các ứng dụng cụ thể.

- Hiển thị ứng dụng trên gốc của trang web
  - Hiển thị danh sách các ứng dụng có thể hiển thị trên tên miền gốc.

![image](assets/en/79.webp)

- Ánh xạ các tên miền cụ thể cho các ứng dụng cụ thể.
  - Khi bạn nhấp vào để thiết lập một tên miền cụ thể cho các ứng dụng cụ thể, quản trị viên có thể thiết lập nhiều tên miền chỉ đến các ứng dụng cần thiết.

![image](assets/en/80.webp)

#### Công cụ trình quyệt blockchain

BTCPay Server, theo mặc định, sử dụng mempool.space làm công cụ trình duyệt blockchain cho các giao dịch. Khi BTCPay Server tạo một hóa đơn mới và có một giao dịch liên quan đến nó, chủ cửa hàng có thể nhấp vào để mở giao dịch; BTCPay Server sẽ điều hướng đến mempool.space làm công cụ trình duyệt blockchain; một quản trị viên máy chủ có thể thay đổi điều này theo sở thích của mình.

![image](assets/en/81.webp)

### Các dịch vụ

Tab `Cài đặt BTCPay Server: Dịch vụ - PTCPay Server Settings: Services` là một giao diện tổng quan về các thành phần mà BTCPay Server của bạn sử dụng. Các dịch vụ mà BTCPay Server của bạn cung cấp có thể thay đổi tùy thuộc vào phương pháp triển khai.

Một quản trị viên BTCPay Server có thể nhấp vào “Xem thông tin” sau mỗi dịch vụ để mở nó và thiết lập các cài đặt cụ thể.

![image](assets/en/82.webp)

#### LND (gRPC)

BTCPay sử dụng dịch vụ gRPC của LND cho việc sử dụng bên ngoài; bạn sẽ tìm thấy thông tin kết nối trong menu cài đặt cụ thể này; ví tương thích được liệt kê ở đây. BTCPay Server cũng cung cấp mã QR để kết nối, quét và áp dụng trong ví di động.

Quản trị viên máy chủ có thể mở thêm chi tiết để xem:

- Chi tiết máy chủ
- Sử dụng SSL
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon
- Bộ mã hóa SSL GRPC (GRPC_SSL_CIPHER_SUITES)

#### LND (REST)

BTCPay sử dụng dịch vụ REST của LND cho việc sử dụng bên ngoài; bạn sẽ tìm thấy thông tin kết nối ở đây; ví tương thích được liệt kê ở đây. Trong số các ví tương thích có Joule, Alby, và ZeusLN. BTCPay Server cung cấp mã QR để kết nối, quét và áp dụng trong ví tương thích.

- Uri REST
- Macaroon
- AdminMacaroon - InvoiceMacaroon
- ReadonlyMacaroon

#### Sao lưu hạt giống LND

Việc sao lưu hạt giống LND hữu ích để khôi phục tiền từ ví LND của bạn trong trường hợp máy chủ của bạn bị hỏng. Vì Lightning Node là một ví nóng, bạn có thể tìm thấy thông tin hạt giống bảo mật trên trang này.

LND đã có tài liệu về quy trình khôi phục. Xem https://github.com/lightningnetwork/lnd/blob/master/docs/recovery.md để biết tài liệu.

#### Ride The Lightning - RTL

Ride the Lightning là một công cụ quản lý Lightning Node được xây dựng dưới dạng phần mềm mã nguồn mở. BTCPay Server sử dụng RTL làm đơn vị quản lý Lightning Node. Quản trị viên BTCPay Server có thể truy cập RTL thông qua cài đặt máy chủ - tab Dịch vụ hoặc bằng cách nhấp vào ví Lightning.

#### Full node P2P

Quản trị viên máy chủ có thể muốn kết nối node Bitcoin của họ với ví di động. Trang này cung cấp thông tin để kết nối từ xa với full node của bạn qua giao thức P2P. Tính đến thời điểm viết cuốn sách này, BTCPay Server liệt kê Blockstream Green và Wasabi wallet là ví tương thích. BTCPay Server cung cấp mã QR để kết nối, quét và áp dụng trong ví tương thích.

#### Full node RPC

Trang này cung cấp thông tin để kết nối từ xa với full node của bạn qua giao thức RPC.

#### SSH

SSH được sử dụng cho mục đích bảo trì. BTCPay Server hiển thị lệnh kết nối ban đầu để truy cập sercer của bạn và khóa công khai SSH được ủy quyền để kết nối với máy chủ của bạn. Quản trị viên có thể muốn tắt thay đổi SSH qua giao diện người dùng của BTCPay Server.

#### DNS động - Dynamic DNS

DNS động cho phép bạn có một tên DNS ổn định trỏ đến máy chủ của bạn, ngay cả khi địa chỉ IP của bạn thay đổi thường xuyên. Điều này được khuyến khích nếu bạn lưu trữ BTCPay Server tại nhà và muốn có một tên miền clearnet để truy cập máy chủ của bạn.

Lưu ý rằng bạn cần cấu hình đúng NAT và cài đặt BTCPay Server của mình để nhận chứng chỉ HTTPS.

### Theme

BTCPay Server, theo mặc định, đi kèm với hai theme: Chế độ sáng và tối. Bạn có thể chuyển đổi bằng cách nhấp vào `Tài khoản - Account` ở góc dưới bên trái và chuyển đổi giữa chủ đề tối hoặc sáng. Quản trị viên BTCPay Server có thể thêm theme của riêng mình bằng cách cung cấp một theme CSS tùy chỉnh.

Quản trị viên có thể mở rộng chủ đề Sáng/Tối bằng cách thêm CSS tùy chỉnh của riêng họ hoặc thiết lập theme tùy chỉnh của họ làm một theme tùy chỉnh hoàn toàn.

![image](assets/en/83.webp)

#### Thương hiệu máy chủ

Quản trị viên máy chủ có thể thay đổi thương hiệu của BTCPay Server bằng cách thiết lập thương hiệu toàn máy chủ của công ty bạn. Vì BTCPay Server là FOSS, quản trị viên máy chủ có thể nhãn trắng (white lable) phần mềm và thay đổi giao diện để phù hợp với doanh nghiệp của họ.

![image](assets/en/84.webp)

### Bảo trì - Maintenance

Là một quản trị viên máy chủ, người dùng mong đợi bạn chăm sóc tốt máy chủ. Trong tab Bảo trì của BTCPay Server, quản trị viên có thể thực hiện một số công việc bảo trì cơ bản. Thiết lập tên miền cho BTCPay Server Instance, khởi động lại hoặc dọn dẹp máy chủ. Có lẽ quan trọng nhất là chạy các bản cập nhật.

BTCPay Server là một dự án mã nguồn mở và thường xuyên cập nhật. Mỗi bản phát hành mới được thông báo qua Thông báo BTCPay Server của bạn hoặc trên các kênh giao tiếp chính thức của BTCPay Server.

![image](assets/en/85.webp)

#### Tên miền

Sau khi BTCPay Server được thiết lập, một quản trị viên có thể muốn thay đổi và không dùng tên miền gốc của mình nữa. Trong tab Bảo trì, quản trị viên có thể thay đổi tên miền. Sau khi nhấp xác nhận và thiết lập các bản ghi DNS đúng trên tên miền, BTCPay Server cập nhật và khởi động lại để hoạt động tên miền mới.

![image](assets/en/86.webp)

#### Khởi động lại

Khởi động lại BTCPay Server và các dịch vụ liên quan.

![image](assets/en/87.webp)

#### Dọn dẹp

BTCPay Server hoạt động với các thành phần Docker; với các bản cập nhật, có thể có những tệp ảnh Docker, tệp tạm, v.v. còn sót lại. Quản trị viên máy chủ có thể dọn dẹp những thứ này và thu hồi không gian trên môi trường làm việc của họ bằng cách chạy script Clean.
![image](assets/en/88.webp)

#### Cập nhật

Có lẽ là tùy chọn quan trọng nhất trong tab Bảo trì. BTCPay Server được xây dựng bởi cộng đồng, và do đó, chu kỳ cập nhật của nó thường xuyên hơn so với hầu hết các sản phẩm phần mềm khác. Khi BTCPay Server có một bản phát hành mới, quản trị viên sẽ được thông báo trong trung tâm thông báo của họ. Bằng cách nhấp vào nút cập nhật, BTCPay Server sẽ kiểm tra GitHub để tìm bản phát hành mới nhất, cập nhật máy chủ và khởi động lại. Trước khi cập nhật, quản trị viên máy chủ luôn được khuyến khích đọc các ghi chú phát hành được phân phối qua các kênh giao tiếp chính thức của BTCPay Server.

![image](assets/en/89.webp)

### Nhật ký - Logs

Đối mặt với một vấn đề không bao giờ là điều vui vẻ cả. Tài liệu này giải thích quy trình và các bước phổ biến nhất để xác định vấn đề của bạn một cách hiệu quả và tự giải quyết nó hoặc nhờ sự giúp đỡ của cộng đồng.

Việc xác định vấn đề là rất quan trọng.

#### Tái tạo vấn đề

Đầu tiên và quan trọng nhất, hãy cố gắng xác định khi nào thì vấn đề xảy ra. Hãy cố gắng tái tạo lại vấn đề. Cố gắng cập nhật và khởi động lại máy chủ của bạn để xác nhận rằng bạn có thể tái tạo lại vấn đề của mình. Nếu nó mô tả vấn đề của bạn tốt hơn, hãy chụp một ảnh màn hình.

##### Cập nhật máy chủ

Kiểm tra phiên bản BTCPay Server của bạn nếu nó cũ hơn nhiều so với [phiên bản mới nhất](https://github.com/btcpayserver/btcpayserver/releases) của BTCPay Server. Cập nhật máy chủ của bạn có thể giải quyết vấn đề.

##### Khởi động lại máy chủ

Khởi động lại máy chủ của bạn là một cách dễ dàng để giải quyết nhiều vấn đề phổ biến nhất của BTCPay Server. Bạn có thể cần SSH vào máy chủ của bạn để khởi động lại nó.

##### Khởi động lại một dịch vụ

Đối với một số vấn đề, bạn chỉ cần khởi động lại một dịch vụ cụ thể trong bản triển khai BTCPay Server của mình. Chẳng hạn như khởi động lại `container lets encrypt` để gia hạn chứng chỉ SSL.

```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```

Sử dụng docker ps để tìm tên của một dịch vụ khác mà bạn muốn khởi động lại.

#### Xem qua nhật ký

Nhật ký có thể cung cấp một phần thông tin quan trọng. Trong các đoạn văn sau, chúng tôi sẽ mô tả cách lấy thông tin log cho các phần khác nhau của BTCPay.

##### Nhật ký BTCPay

Từ phiên bản v1.0.3.8, bạn có thể dễ dàng truy cập nhật ký của BTCPay Server từ giao diện người dùng. Nếu bạn là quản trị viên máy chủ, hãy vào Server Settings > Logs và mở tệp nhật ký. Nếu bạn không biết lỗi cụ thể trong nhật ký có nghĩa là gì, hãy đề cập đến nó khi khắc phục sự cố.

Nếu bạn muốn xem nhật ký chi tiết hơn và đang sử dụng triển khai Docker, bạn có thể xem nhật ký của các container Docker cụ thể bằng dòng lệnh. Xem [hướng dẫn này để ssh](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) vào một instance của BTCPay đang chạy trên VPS.

Trang tiếp theo, một danh sách tổng quát các tên container được sử dụng cho BTCPay Server.

Chạy các lệnh dưới đây để in nhật ký theo tên container. Thay thế tên container để xem nhật ký của các container khác.

```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```

| Nhật ký cho     | Tên Container                     |
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
Navigate to the correct directory:
cd btcpayserver-docker
# Find container name:
docker ps
Print logs by container name:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```

Ngoài ra, bạn có thể nhanh chóng in nhật ký bằng cách sử dụng ID container (chỉ cần các ký tự ID duy nhất đầu tiên, như hai ký tự bên trái nhất):

```bash
docker logs 'add your container ID'
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

Để truy cập nhật ký nén trong `.gzip`, sử dụng `gzip -d lnd.log.16.gz` (trong trường hợp này chúng ta đang truy cập `lnd.log.16.gz`). Điều này sẽ tạo ra một tệp mới, bạn có thể làm `cat lnd.log.16`. Trong trường hợp những thao tác ở trên không hoạt động, bạn có thể cần cài đặt gzip trước với `sudo apt-get install gzip`.

###### Lightning Network c-lightning - Docker

```bash
sudo su -
docker ps
# Find the c-lightning container ID.
docker logs 'add your container ID here'
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

[(mở cửa sổ mới)](https://developer.bitcoin.org/reference/rpc/index.html) để lấy thông tin từ node bitcoin của bạn. BTCPay có chưa một script để cho phép bạn giao tiếp với node Bitcoin của mình một cách dễ dàng.

Trong thư mục btcpayserver-docker, lấy thông tin blockchain sử dụng node của bạn:

```bash
bitcoin-cli.sh getblockchaininfo
```
### Các tập tin - Files
BTCPay Server có một hệ thống tệp tin cục bộ và tải các tài sản của Cửa hàng (sản phẩm), Logo, và thương hiệu trực tiếp lên máy chủ. Hệ thống tệp tin của máy chủ chỉ có thể truy cập bởi quản trị viên máy chủ; chủ sở hữu cửa hàng có thể tải lên logo/thương hiệu của họ ở cấp độ cửa hàng.
Khi Quản trị viên máy chủ đang ở trong tab `Lưu trữ tệp - File Storage`, có thể trực tiếp tải lên Máy chủ của bạn hoặc thay đổi nhà cung cấp dịch vụ lưu trữ tệp tin sang Hệ thống tệp tin cục bộ hoặc Azure Blob Storage.

![hình ảnh](assets/en/90.webp)

![hình ảnh](assets/en/91.webp)

### Tóm tắt kỹ năng

Trong phần này, bạn đã học được những điều sau:

- Sự khác biệt giữa Cài đặt cửa hàng và Cài đặt máy chủ, đặc biệt là liên quan đến người dùng, vai trò, và email
- Thiết lập các chính sách chung cho máy chủ về việc sử dụng và tạo ví nóng Lightning hoặc Bitcoin, đăng ký người dùng mới, và thông báo email.
- Cách thêm các theme tùy chỉnh (thay vì chỉ có tùy chọn sáng/tối đơn giản được cung cấp sẵn) cũng như tạo logo tùy chỉnh
- Thực hiện các nhiệm vụ bảo trì máy chủ đơn giản qua GUI được cung cấp sẵn
- Khắc phục sự cố, bao gồm lấy thông tin chi tiết của bất kỳ container Docker nào hoặc node của bạn
- Quản lý lưu trữ tệp

### Đánh giá kiến thức

#### Đánh giá kiến thức lý thuyết

Sự khác biệt trong vai trò được gán qua Cài đặt máy chủ so với Cài đặt cửa hàng là gì, và điều gì cho thấy một trường hợp sử dụng mà quyền của vai trò này vượt vai trò kia.

#### Đánh giá kiến thức thực hành

Mô tả một số trường hợp sử dụng có thể được kích hoạt trong tab Chính sách.

#### Đánh kiến thức thực hành

Mô tả một số hành động mà một quản trị viên có thể thường xuyên thực hiện trong tab Bảo trì.

## BTCPay Server - Thanh toán

<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>

Hóa đơn là một tài liệu mà người bán phát hành cho người mua để thu tiền.

Trong BTCPay Server, một hóa đơn đại diện cho một tài liệu phải được thanh toán trong một khoảng thời gian xác định với tỷ giá cố định. Hóa đơn có thời hạn vì chúng khóa tỷ giá trong một khung thời gian xác định để bảo vệ người nhận khỏi sự biến động giá.

Cốt lõi của BTCPay Server là khả năng hoạt động như một hệ thống quản lý hóa đơn Bitcoin. Hóa đơn là một công cụ thiết yếu để theo dõi và quản lý các khoản thanh toán đã nhận.

Trừ khi bạn sử dụng [ví](https://docs.btcpayserver.org/Wallet/) tích hợp để nhận thanh toán một cách thủ công, tất cả các khoản thanh toán trong một cửa hàng sẽ được hiển thị trên trang `Hóa đơn - Invoice`. Trang này sắp xếp tổng hợp các khoản thanh toán theo ngày và là trung tâm cho việc quản lý hóa đơn và khắc phục sự cố thanh toán.

![hình ảnh](assets/en/92.webp)

### Tổng quan

#### Trạng thái hóa đơn

Bảng dưới đây liệt kê và mô tả các trạng thái hóa đơn tiêu chuẩn trong BTCPay và đề xuất các hành động phổ biến. Các hành động chỉ là khuyến nghị. Quyết định hành động tốt nhất cho các trường hợp sử dụng và kinh doanh của họ là do người dùng quyết định.

| Trạng thái hóa đơn                    | Mô tả                                                                                                                     | Hành động                                                                                                                                             |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| New - Mới                                   | Chưa thanh toán, bộ đếm thời gian hóa đơn vẫn chưa hết hạn                                                                | Không có                                                                                                                                              |
| New (paidPartial) - Mới (đã thanh toán một phần)          | Đã thanh toán, không đủ, bộ đếm thời gian hóa đơn vẫn chưa hết hạn                                                        | Không có                                                                                                                                              |
| Expired - Hết hạn                               | Chưa thanh toán, bộ đếm thời gian hóa đơn đã hết hạn                                                                      | Không có                                                                                                                                              |
| Expired (paidPartial) - Hết hạn (đã thanh toán một phần) \*\* | Đã thanh toán, không đủ số tiền, và đã hết hạn                                                                            | Liên hệ với người mua để sắp xếp hoàn tiền hoặc yêu cầu họ thanh toán số tiền còn thiếu. Có thể tuỳ chọn đánh dấu hóa đơn là quyết toán hoặc không hợp lệ |
| Expired (paidLate) - Hết hạn (đã thanh toán muộn)          | Đã thanh toán, đủ số tiền, sau khi bộ đếm thời gian hóa đơn đã hết hạn                                                    | Liên hệ với người mua để sắp xếp hoàn tiền hoặc xử lý đơn hàng nếu việc xác nhận muộn được chấp nhận.                                                 |
| Settled (paidOver) - Đã tất toán (trả quá số tiền)       | Trả nhiều hơn số tiền trên hóa đơn, đã thanh toán, nhận đủ số xác nhận cần thiết                                    | Liên hệ với người mua để sắp xếp hoàn trả số tiền thừa, hoặc tùy chọn chờ người mua liên hệ với bạn                                                   |
| Processing - Đang xử lý                            | Đã trả đủ tiền, nhưng chưa nhận đủ số xác nhận cần thiết theo cài đặt của cửa hàng                                  | Liên hệ với người mua để sắp xếp hoàn trả số tiền thừa, hoặc tùy chọn chờ người mua liên hệ với bạn                                                   |
| Processing (paidOver) - Đang xử lý (trả quá số tiền)          | Trả nhiều hơn số tiền trên hóa đơn, chưa nhận đủ số xác nhận cần thiết                                              | Chờ được thanh toán sau đó liên hệ với người mua để sắp xếp hoàn trả số tiền thừa, hoặc tùy chọn chờ người mua liên hệ với bạn                        |
| Settled - Đã tất toán                        | Đã trả đủ tiền, nhận đủ số xác nhận cần thiết trong cửa hàng                                                        | Hoàn tất đơn hàng                                                                                                                                   |
| Settled (marked) - Đã tất toán (được đánh dấu)         | Trạng thái đã được thay đổi thủ công thành đã thanh toán từ trạng thái đang xử lý hoặc không hợp lệ                       | Quản trị viên cửa hàng đã đánh dấu thanh toán là đã được hoàn tất                                                                                  |
| Invalid - Không hợp lệ\*                        | Đã trả tiền, nhưng không nhận đủ số xác nhận cần thiết trong thời gian quy định của cài đặt cửa hàng                | Kiểm tra giao dịch trên trình duyệt blockchain, nếu nó nhận đủ xác nhận, đánh dấu là đã hoàn tất                                                   |
| Invalid (marked) - Không hợp lệ (được đánh dấu)          | Trạng thái đã được thay đổi thủ công thành không hợp lệ từ trạng thái đã hoàn tất hoặc hết hạn                          | Quản trị viên cửa hàng đã đánh dấu thanh toán là không hợp lệ                                                                                         |
| Invalid (paidOver) - Không hợp lệ (trả quá số tiền)        | Trả nhiều hơn số tiền trên hóa đơn, nhưng không nhận đủ số xác nhận cần thiết trong thời gian quy định của cửa hàng | Kiểm tra giao dịch trên trình duyệt blockchain, nếu nó nhận đủ số xác nhận, đánh dấu là đã hoàn tất                                                    |

#### Chi tiết hóa đơn

Trang chi tiết hóa đơn chứa tất cả thông tin liên quan đến một hóa đơn.

Thông tin hóa đơn được tạo tự động dựa trên trạng thái hóa đơn, tỷ giá hối đoái, v.v. Thông tin sản phẩm được tạo tự động nếu hóa đơn được tạo với thông tin sản phẩm, như trong ứng dụng điểm bán cuối - PoS.

#### Lọc hóa đơn

Hóa đơn có thể được lọc qua các bộ lọc nhanh nằm cạnh nút tìm kiếm hoặc các bộ lọc nâng cao, có thể được chuyển đổi bằng cách nhấp vào liên kết (Trợ giúp - Help) ở trên cùng. Người dùng có thể lọc hóa đơn theo cửa hàng, mã đơn hàng, mã mặt hàng, trạng thái, hoặc ngày.

#### Xuất hóa đơn

Hóa đơn BTCPay Server có thể được xuất dưới dạng CSV hoặc JSON để biết thêm thông tin về xuất hóa đơn và kế toán.

#### Hoàn trả hóa đơn

Nếu, vì bất kỳ lý do gì, bạn muốn thực hiện hoàn trả, bạn có thể dễ dàng tạo một lệnh hoàn trả từ giao diện xem hóa đơn.

#### Lưu trữ hóa đơn

Do tính năng không sử dụng lại địa chỉ của BTCPay Server, thường thấy nhiều hóa đơn hết hạn trên trang hóa đơn của cửa hàng. Để ẩn chúng khỏi giao diện của bạn, chọn chúng trong danh sách và đánh dấu là đã lưu trữ. Hóa đơn đã được đánh dấu là đã lưu trữ không bị xóa. Thanh toán cho một hóa đơn đã lưu trữ vẫn sẽ được BTCPay Server phát hiện (trạng thái trả muộn). Bạn có thể xem các hóa đơn đã lưu trữ của cửa hàng bất cứ lúc nào bằng cách chọn hóa đơn đã lưu trữ từ bộ lọc tìm kiếm.

#### Tiền tệ mặc định

Tiền tệ mặc định của cửa hàng, được thiết lập tại trình hướng dẫn tạo cửa hàng

#### Cho phép bất kỳ ai tạo hóa đơn

Bạn nên kích hoạt tùy chọn này nếu bạn muốn cho phép người bên ngoài tạo hóa đơn trong cửa hàng của bạn. Tùy chọn này chỉ hữu ích nếu bạn đang sử dụng nút thanh toán hoặc nếu bạn đang phát hành hóa đơn qua API hoặc website HTML của bên thứ ba. Ứng dụng PoS được ủy quyền trước và không cần kích hoạt này cho một khách truy cập ngẫu nhiên mở cửa hàng PoS của bạn và tạo hóa đơn.

#### Thêm phí bổ sung (phí mạng lưới) vào hóa đơn

- Chỉ khi khách hàng thực hiện nhiều hơn một lần thanh toán cho hóa đơn
- Trên mỗi lần thanh toán
- Không bao giờ thêm phí mạng lưới

#### Hóa đơn sẽ hết hạn nếu số tiền đầy đủ không được thanh toán sau ... Phút.

Bộ đếm thời gian của hóa đơn được thiết lập mặc định là 15 phút. Bộ đếm thời gian là một cơ chế bảo vệ nhằm chống lại sự biến động giá cả vì nó khóa số lượng tiền điện tử theo tỷ giá hối đoái Bitcoin / tiền pháp định. Nếu khách hàng không thanh toán hóa đơn trong khoảng thời gian đã định, hóa đơn được coi là đã hết hạn. Hóa đơn được coi là "đã thanh toán" ngay khi giao dịch hiển thị trên blockchain (0-xác nhận) nhưng được coi là "hoàn thành" khi có được xác nhận mà người bán hàng đã định (thường là 1-6). Bộ đếm thời gian có thể tùy chỉnh.

#### Xem xét hóa đơn đã thanh toán ngay cả khi số tiền thanh toán ít hơn ... % so với dự kiến.

Trong trường hợp khách hàng sử dụng ví trên sàn giao dịch để trực tiếp thanh toán cho một hóa đơn, giao dịch sẽ mất một lượng phí nhỏ. Điều này có nghĩa là hóa đơn đó không được coi là hoàn tất đầy đủ. Hóa đơn nhận được trạng thái "đã thanh toán một phần". Nếu một người bán hàng muốn chấp nhận hóa đơn thanh toán thiếu, bạn có thể thiết lập tỷ lệ phần trăm ở đây.

### Yêu cầu

Yêu cầu thanh toán là một tính năng cho phép chủ sở hữu cửa hàng BTCPay tạo hóa đơn lâu dài. Tiền được thanh toán cho một yêu cầu thanh toán sử dụng tỷ giá hối đoái tại thời điểm thanh toán. Điều này cho phép người dùng thực hiện thanh toán theo sự tiện lợi của họ mà không cần thương lượng hoặc xác minh tỷ giá hối đoái với chủ cửa hàng tại thời điểm thanh toán.

Người dùng có thể thanh toán các yêu cầu này bằng cách thanh toán một phần. Yêu cầu thanh toán sẽ còn hiệu lực cho đến khi nó được thanh toán đầy đủ hoặc nếu chủ cửa hàng đặt ra một thời gian hết hạn. Địa chỉ không bao giờ được tái sử dụng. Một địa chỉ mới được tạo ra mỗi lần người dùng nhấp vào nút thanh toán để tạo hóa đơn cho yêu cầu thanh toán.

Chủ cửa hàng có thể in yêu cầu thanh toán (hoặc xuất dữ liệu hóa đơn) để lưu trữ và làm kế toán. BTCPay tự động gắn nhãn hóa đơn là Yêu cầu thanh toán trong danh sách hóa đơn của cửa hàng.

#### Tùy chỉnh yêu cầu thanh toán của bạn

- Số tiền - Thiết lập số tiền yêu cầu thanh toán
- Đơn vị tiền tệ - Hiển thị số tiền được yêu cầu theo đồng tiền pháp định hoặc đồng tiền mã hoá
- Số lượng thanh toán - Chỉ cho phép thanh toán một lần hoặc cho phép thanh toán một phần
- Thời gian hết hạn - Cho phép thanh toán cho đến một thời điểm nào đó hoặc không bao giờ hết hạn
- Mô tả - Trình soạn thảo văn bản, bảng dữ liệu, nhúng hình ảnh và video
- Hình thức - Màu sắc và kiểu dáng với theme CSS

![image](assets/en/93.webp)

#### Tạo một yêu cầu thanh toán
Trong menu bên trái, đi đến `Yêu cầu thanh toán - Payment Request` và nhấp vào "Tạo yêu cầu thanh toán - Create Payment Request".

![image](assets/en/94.webp)

Cung cấp tên của yêu cầu, số tiền, đơn vị tiền tệ được hiển thị, cửa hàng liên két, thời gian hết hạn và mô tả (tuỳ chọn).

Chọn tùy chọn cho phép người thanh toán tạo hóa đơn theo đơn vị tiền tệ của họ nếu bạn muốn cho phép thanh toán một phần.

Nhấp vào Lưu & Xem để xem lại yêu cầu thanh toán của bạn.

BTCPay tạo một URL cho yêu cầu thanh toán. Chia sẻ URL này để xem yêu cầu thanh toán của bạn. Cần nhiều yêu cầu giống nhau? Bạn có thể nhân bản yêu cầu thanh toán sử dụng tùy chọn Clone trong menu chính.

![image](assets/en/95.webp)

**CẢNH BÁO**

Yêu cầu thanh toán phụ thuộc vào cửa hàng, nghĩa là mỗi yêu cầu thanh toán được liên kết với một cửa hàng khi được tạo. Hãy chắc chắn rằng bạn có một ví được kết nối với cửa hàng mà yêu cầu thanh toán đó thuộc về.

#### Yêu cầu đã được thanh toán

Người thanh toán và người yêu cầu có thể xem trạng thái của yêu cầu thanh toán sau khi gửi thanh toán. Trạng thái sẽ hiển thị là `Đã hoàn tất - Settled` nếu thanh toán đã được nhận đầy đủ. Nếu chỉ có thanh toán một phần, `Số tiền còn nợ - Amount Due` sẽ hiển thị số dư còn lại.

![image](assets/en/96.webp)

#### Tùy chỉnh yêu cầu thanh toán

Nội dung mô tả có thể được chỉnh sửa sử dụng trình soạn thảo văn bản của yêu cầu thanh toán. Cả hai tùy chọn đều có sẵn nếu bạn muốn sử dụng thêm màu sắc hoặc tùy chỉnh CSS.
Người dùng không chuyên kỹ thuật có thể sử dụng [bootstrap theme](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes). Việc tùy chỉnh sâu hơn có thể được thực hiện bằng cách cung cấp thêm mã CSS, như được hiển thị dưới đây.

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

Truyền thống, người nhận tiền chia sẻ địa chỉ Bitcoin của họ, sau đó người gửi chuyển tiền vào địa chỉ này. Hệ thống như vậy được gọi là Thanh toán đẩy, vì người gửi khởi xướng thanh toán trong khi người nhận có thể không có mặt, đẩy thanh toán đến người nhận.

Tuy nhiên, nếu đảo ngược vai trò thì sao?

Nếu thay vì người gửi đẩy thanh toán, người gửi cho phép người nhận kéo thanh toán vào thời điểm người nhận thấy phù hợp? Đây là khái niệm của Thanh toán kéo. Điều này cho phép nhiều ứng dụng mới, như:

- Dịch vụ đăng ký (nơi người đăng ký cho phép nhà cung cấp thực hiện một khoản thanh toán kéo x khoảng thời gian)
- Hoàn tiền (nơi người bán cho phép khách hàng kéo tiền hoàn lại vào ví khi họ thấy phù hợp)
- Thanh toán hoá đơn dựa trên thời gian cho freelancer (nơi người thuê cho phép freelancer kéo tiền vào ví của họ khi thời gian làm việc được báo cáo)
- Tài trợ (nơi người tài trợ cho phép người nhận kéo tiền hàng tháng để tiếp tục hỗ trợ công việc của họ)
- Bán hàng tự động (nơi khách hàng của một sàn giao dịch cho phép sàn giao dịch kéo tiền từ ví của họ để bán hàng tự động hàng tháng)
- Hệ thống rút tiền dựa trên số dư (nơi một dịch vụ có lượng giao dịch cao cho phép người dùng yêu cầu rút tiền từ số dư của họ, dịch vụ sau đó có thể dễ dàng gộp tất cả các khoản thanh toán cho nhiều người dùng vào các khoảng thời gian cố định)

### Xuất chi - Payouts

Chức năng xuất chi được tích hợp vào [Thanh toán kéo](https://docs.btcpayserver.org/PullPayments/). Tính năng này cho phép bạn xuất chi trong BTCPay của mình. Tính năng này cho phép bạn xử lý thanh toán kéo (hoàn tiền, thanh toán lương, hoặc rút tiền).

#### Ví dụ 1: Hoàn tiền

Hãy bắt đầu với ví dụ về hoàn tiền. Khách hàng đã mua một mặt hàng trong cửa hàng của bạn nhưng không may phải trả lại mặt hàng. Họ muốn được hoàn tiền. Trong BTCPay, bạn có thể tạo một giao dịch [hoàn tiền](https://docs.btcpayserver.org/Refund/) và cung cấp cho khách hàng liên kết để họ có thể nhận lại tiền. Khi khách hàng đã cung cấp địa chỉ của họ và yêu cầu rút khoản tiền, nó sẽ được hiển thị trong Xuất chi - Payouts.

Trạng thái đầu tiên là Đang chờ phê duyệt. Nhân viên cửa hàng có thể kiểm tra nếu có nhiều khoản đang chờ, và sau khi lựa chọn, bạn sử dụng nút Hành động

Tùy chọn trên nút Hành động - Actions

- Phê duyệt các khoản xuất chi đã chọn
- Phê duyệt & gửi các khoản xuất chi đã chọn
- Hủy các khoản xuất chi đã chọn

Bước tiếp theo là phê duyệt & gửi các khoản xuất chi đã chọn vì chúng ta muốn hoàn tiền cho khách hàng. Kiểm tra địa chỉ của khách hàng, hiển thị số tiền và xem thử chúng ta có muốn phí được trừ từ số tiền hoàn lại hay không. Sau khi bạn đã kiểm tra, việc còn lại là ký giao dịch
Khách hàng giờ đây được cập nhật trên trang `Yêu cầu thanh toán - Claiming`. Anh ta có thể theo dõi giao dịch vì được cung cấp một liên kết đến trình duyệt blockchain và giao dịch của mình. Một khi giao dịch được xác nhận và trạng thái thay đổi thành Hoàn thành.

#### Ví dụ 2: Lương

Bây giờ, chúng ta hãy nói về việc thanh toán lương, vì điều này được thực hiện từ bên trong cửa hàng và không theo yêu cầu của khách hàng. Cơ bản là giống nhau; nó sử dụng các khoản thanh toán kéo. Nhưng thay vì tạo một khoản hoàn tiền, chúng ta sẽ tạo một [khoản thanh toán kéo](https://docs.btcpayserver.org/PullPayments/).

Đi đến tab Khoản thanh toán kéo - Pull Payments trong BTCPay Servercủa bạn. Ở góc trên bên phải, nhấp vào nút `Tạo khoản thanh toán kéo - Create Pull Payment`.

Bây giờ chúng ta đang trong quá trình tạo khoản xuất chi, đặt tên cho nó và số tiền cần chi theo đơn vị tiền tệ mong muốn, điền vào mô tả, để nhân viên biết nó là cái gì. Phần tiếp theo tương tự như hoàn tiền. Nhân viên điền địa chỉ nhận và số tiền anh ta muốn yêu cầu từ khoản xuất chi này. Anh ta có thể quyết định làm 2 yêu cầu riêng biệt, đến các địa chỉ khác nhau, hoặc thậm chí yêu cầu một phần qua lightning.

Nếu có nhiều khoản xuất chi đang chờ, bạn có thể gộp chúng lại để được ký và gửi đi. Một khi đã ký, các khoản xuất chi chuyển sang tab `Đang tiến hành - In progress` và hiển thị Giao dịch. Khi được mạng lưới chấp nhận, khoản thanh toán chuyển sang tab `Hoàn thành - Completed`. Tab Hoàn thành chỉ mang mục đích lịch sử. Nó giữ các khoản xuất chi đã xử lý và giao dịch thuộc về nó.

### Khoản thanh toán kéo

#### Khái niệm

Khi người gửi thiết lập một khoản thanh toán kéo, họ có thể cấu hình một số thuộc tính:

- Tên của yêu cầu khoản thanh toán kéo
- Một số tiền giới hạn
- Đơn vị (như BTC, SAT, USD)
- Phương thức Thanh toán
  - BTC On-chain
  - BTC Off-chain
- Mô tả
- CSS tùy chỉnh
- Ngày kết thúc (tùy chọn cho Lightning Network BOLT11)

Sau đó, người gửi có thể chia sẻ khoản thanh toán kéo bằng một liên kết với người nhận, cho phép người nhận tạo một khoản xuất chi. Người nhận sẽ chọn khoản xuất chi của mình:

- Phương thức thanh toán nào để sử dụng
- Gửi tiền đến đâu

Một khi một khoản xuất chi được tạo, nó sẽ được tính vào giới hạn của khoản thanh toán kéo cho kỳ hiện tại. Người gửi sau đó sẽ phê duyệt khoản thanh toán bằng cách thiết lập tỷ giá mà khoản xuất chi sẽ được gửi và xử lý thanh toán.

Đối với người gửi, chúng tôi cung cấp một phương thức để họ dễ dàng gộp thanh toán của nhiều khoản xuất chi từ [ví nội bộ BTCPay](https://docs.btcpayserver.org/Wallet/).

#### Greenfield API

BTCPay Server cung cấp một API đầy đủ cho cả người gửi và người nhận được tài liệu hóa trong trang `/docs` của Instance mà bạn đang dùng. (hoặc trên trang web tài liệu https://docs.btcpayserver.org)

Vì API của chúng ta được tiếp cận với toàn bộ chức năng của khoản thanh toán kéo, người gửi có thể tự động hóa các khoản thanh toán theo nhu cầu của mình.

### Tóm tắt kỹ năng

Trong phần này, bạn đã học được những điều sau:

- Hiểu sâu về các trạng thái hóa đơn của BTCPay Server cũng như các hành động có thể thực hiện trên chúng
- Tùy chỉnh và quản lý các cơ chế hóa đơn dài hạn được biết đến như các Yêu cầu
- Các cách thức thanh toán linh hoạt với tính năng khoản thanh toán kéo độc đáo của BTCPay Server, đặc biệt là cách xử lý hoàn tiền và thanh toán lương.

### Đánh giá kiến thức

#### Đánh giá kiến thức lý thuyết

Những điểm khác biệt nào giữa hóa đơn và yêu cầu thanh toán, và đâu là lý do để sử dụng yêu cầu thanh toán?

#### Đánh giá kiến thức lý thuyết

Khoản thanh toán kéo mở rộng như thế nào so với những gì thường có thể được thực hiện on-chain? Mô tả một số trường hợp sử dụng mà chúng kích hoạt.

## Plugin mặc định của BTCPay Server

<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>

### Plugin và Ứng dụng mặc định

BTCPay Server đi kèm với một bộ Plugin tiêu chuẩn có thể biến BTCPay Server thành một cổng thanh toán thương mại điện tử. Với sự bổ sung của Điểm bán hàng, Nền tảng gây quỹ, và nút Thanh toán dễ dàng, BTCPay Server trở thành giải pháp dễ dàng triển khai.

### Điểm bán hàng - Point of Sale

Một trong những Plugin tiêu chuẩn của BTCPay Server là Điểm bán hàng (PoS). Với plugin PoS, chủ cửa hàng có thể tạo một Webshop trực tiếp từ BTCPay Server, chủ cửa hàng không cần giải pháp thương mại điện tử của bên thứ ba để vận hành Webshop. Ứng dụng PoS dựa trên web cho phép người dùng với cửa hàng truyền thống dễ dàng chấp nhận Bitcoin, không tốn chi phí hoặc phải thông qua bên thứ ba, trực tiếp vào ví của họ. PoS có thể được hiển thị dễ dàng trên máy tính bảng hoặc các thiết bị khác hỗ trợ duyệt web. Người dùng có thể dễ dàng tạo một lối tắt màn hình chính để truy cập ứng dụng web nhanh chóng.

#### Cách tạo điểm bán hàng mới

BTCPay Server cho phép chủ cửa hàng tạo một điểm bán hàng một cách nhanh chóng. BTCPay Server nhận ra rằng không phải mọi cửa hàng đều là thương mại điện tử, và không phải mọi cửa hàng là quán bar hay nhà hàng, và nó đi kèm với nhiều thiết lập tiêu chuẩn cho PoS của bạn.

Khi chủ cửa hàng nhấp vào "Điểm bán hàng" trong thanh menu bên trái của mình, BTCPay Server sẽ yêu cầu một tên; tên này sẽ được hiển thị trong thanh menu bên trái. Nhấp `Tạo - Create` để tạo PoS.

![image](assets/en/97.webp)

#### Cập nhật điểm bán hàng mới tạo

Sau khi tạo một PoS mới, màn hình tiếp theo sẽ là để cập nhật điểm bán hàng và thêm các mặt hàng cho cửa hàng của bạn.

##### Tên ứng dụng

Tên được đặt ở đây cho điểm bán hàng của bạn sẽ được hiển thị trong menu chính của BTCPay Server.

##### Tiêu đề hiển thị

Công chúng sẽ thấy tiêu đề công khai hoặc tên khi ghé thăm cửa hàng của bạn. Theo tiêu chuẩn BTCPay Server theo tiêu chuẩn đặt tên cửa hàng của bạn là “Tiệm trà - Tea Shop”, hãy thay thế tên mặc định này bằng tên cửa hàng của bạn.

![image](assets/en/98.webp)

#### Chọn kiểu điểm bán hàng

BTCPay Server có khả năng hiển thị điểm bán hàng của mình theo nhiều cách.

- Danh sách sản phẩm
  - Một giao diện cửa hàng nơi khách hàng chỉ có thể mua 1 sản phẩm mỗi lần.
- Danh sách sản phẩm với giỏ hàng.
  - Một giao diện cửa hàng nơi khách hàng có thể mua nhiều mặt hàng cùng một lúc và có được thông tin giỏ hàng ở bên phải màn hình của họ.
- Chỉ bàn phím
  - Không có danh sách sản phẩm, chỉ có bàn phím cho việc lập hóa đơn trực tiếp.
- Hiển thị in (Danh sách sản phẩm có thể in với QR)
  - Nếu bạn không thể luôn hiển thị danh sách sản phẩm của mình một cách kỹ thuật số, bạn cần một giải pháp "ngoại tuyến" cho sản phẩm; BTCPay Server có chức năng hiển thị in để hoạt động như một cửa hàng ngoại tuyến.

![image](assets/en/99.webp)

#### Kiểu điểm bán hàng - Danh sách sản phẩm

![image](assets/en/100.webp)

#### Kiểu Điểm Bán Hàng - Danh sách sản phẩm + Giỏ hàng

![image](assets/en/101.webp)

#### Kiểu điểm bán hàng - Chỉ bàn phím

![image](assets/en/102.webp)

#### Kiểu điểm bán hàng - Hiển thị in

![image](assets/en/103.webp)

#### Tiền tệ

Chủ cửa hàng có thể đặt một loại tiền tệ khác cho điểm bán hàng của mình so với loại tiền tệ mặc định đã được thiết lập. Loại tiền tệ mặc định của cửa hàng sẽ tự động điền vào trường này.

#### Mô tả

Hãy kể cho thế giới biết về cửa hàng của bạn; bạn đang bán gì và với giá bao nhiêu? Mọi thứ giải thích về cửa hàng của bạn đều được viết ở đây.

#### Sản phẩm

Khi một điểm bán hàng được tạo ra, một BTCPay Server chuẩn sẽ thêm một vài mặt hàng vào cửa hàng để tham khảo. Nhấn vào nút Chỉnh sửa trên bất kỳ mặt hàng tiêu chuẩn nào để hiểu rõ hơn về từng tùy chọn có thể có cho một mặt hàng.

Việc tạo một sản phẩm mới trong cửa hàng bao gồm các trường sau;

- Tiêu đề
- Giá (cố định, tối thiểu, hoặc tùy chỉnh)
- URL Hình ảnh
- Mô tả
- Tồn kho
- ID
- Tên nút mua
- Bật/Tắt

Sau khi chủ cửa hàng đã điền tất cả các trường sản phẩm mới, nhấn vào lưu, và bạn sẽ nhận thấy rằng mục sản phẩm trong điểm bán hàng bây giờ đang được điền vào. Luôn đảm bảo lưu ở góc trên bên phải của màn hình để tránh việc chủ cửa hàng có thể mất tiến độ khi thêm sản phẩm.

Chủ cửa hàng cũng có thể sử dụng "Trình Cchỉnh sửa thô - Raw Editor" để cấu hình sản phẩm của họ. Trình chỉnh sửa thô yêu cầu có hiểu biết cơ bản về cấu trúc JSON.

#### Thanh toán - Checkout

BTCPay Server cho phép tùy chỉnh thanh toán cụ thể cho PoS nhỏ. Chủ cửa hàng có thể thiết lập văn bản "Mua với x" hoặc yêu cầu dữ liệu khách hàng cụ thể bằng cách thêm vào biểu mẫu.

#### Tiền bo - Tips

Không phải tất cả các cửa hàng đều cần tùy chọn cho Tiền bo trên trang bán hàng của họ. Chủ cửa hàng có thể bật hoặc tắt tùy chọn này tùy theo nhu cầu của mình. Nếu cửa hàng sử dụng tiền bo được bật, chủ cửa hàng có thể thiết lập văn bản trong trường cho tiền bo mà họ thích. Tiền bo trên BTCPay Server hoạt động dựa trên một số tiền phần trăm. Chủ cửa hàng có thể thêm nhiều phần trăm với sự phân cách bằng dấu phẩy.

#### Giảm giá - Discount

Là một chủ cửa hàng, bạn có thể muốn cung cấp cho khách hàng một chính sách giảm giá tùy chỉnh khi thanh toán; nút bật/tắt cho `Giảm giá - Discount` sẽ có sẵn tại phần thanh toán của cửa hàng. Tuy nhiên, điều này được khuyến khích không sử dụng cho hệ thống tự thanh toán.

#### Thanh toán tuỳ chỉnh

Khi tùy chọn Thanh toán tuỳ chỉnh được bật, khách hàng có thể nhập giá của họ tương đương hoặc cao hơn hóa đơn gốc được tạo bởi cửa hàng.

#### Tùy chọn bổ sung

Sau khi thiết lập mọi thứ cho Điểm bán hàng của bạn, còn một số tùy chọn bổ sung. Chủ cửa hàng có thể dễ dàng nhúng PoS của họ thông qua một khuôn khổ hoặc nhúng một nút thanh toán liên kết đến một mặt hàng cụ thể của cửa hàng. Để tạo phong cách cho cửa hàng PoS vừa được tạo, chủ cửa hàng có thể thêm CSS tùy chỉnh ở cuối các tùy chọn bổ sung.

#### Xóa ứng dụng này

Nếu chủ cửa hàng muốn xoá hoàn toàn Điểm bán hàng khỏi BTCPay Server của mình, ở cuối cập nhật PoS, chủ cửa hàng có thể nhấn vào nút `Xóa ứng dụng này - Delete this app` để làm việc đó. Khi nhấn "Xóa ứng dụng này", BTCPay Server sẽ yêu cầu xác nhận bằng cách gõ `DELETE` và xác nhận bằng cách nhấn vào nút Xóa. Sau khi xóa, chủ cửa hàng trở lại bảng điều khiển BTCPay Server.

### BTCPay Server - Gây quỹ cộng đồng - Crowdfund

Bên cạnh plugin Điểm bán hàng, BTCPay Server cũng có tùy chọn để tạo một chiến dịch gây quỹ. Giống như bất kỳ nền tảng gây quỹ nào khác, chủ cửa hàng có thể thiết lập mục tiêu, tạo các quyền lợi cho các khoản đóng góp, và tùy chỉnh theo nhu cầu của họ.

#### Cách thiết lập một chiến dịch gây quỹ mới

Nhấn vào plugin `Gây quỹ - Crowdfund` thông qua menu chính ở bên trái BTCPay Server của bạn, dưới mục Plugin. BTCPay Server bây giờ sẽ yêu cầu bạn đặt tên cho chiến dịch gây quỹ, tên này cũng sẽ được hiển thị trong thanh menu bên trái.

#### Hiển thị tên chiến dịch

Tên của chiến dịch gây quỹ được hiển thị công khai để cộng đồng biết.

#### Dòng Tagline

Đưa ra một câu slogan ngắn gọn để mọi người nhận biết đợt gây quỹ này về liên quan tới điều gì.

![hình ảnh](assets/en/107.webp)

#### URL hình ảnh đại diện

Mỗi đợt gây quỹ đều có hình ảnh chính của mình, đó là banner mà bạn có thể nhận ra ngay lập tức. Hình ảnh này có thể được lưu trữ trên máy chủ của bạn nếu bạn có quyền quản trị, Quản trị viên có thể tải lên trong phần cài đặt BTCPay Server - Files. Khi bạn là chủ sở hữu cửa hàng, hình ảnh phải được tải lên web thông qua một bên thứ ba (ví dụ như imgur)

#### Công khai chiến dịch gây quỹ

Nút chuyển này giúp bạn công khai đợt gây quỹ, do đó người khác sẽ nhìn thấy. Đối với mục đích kiểm tra hoặc để xem giao diện của bạn được áp dụng đúng cách, bạn có thể muốn giữ nó ở chế độ TẮT trong thời gian thiết lập đợt gây quỹ.

#### Mô tả

Hãy kể cho thế giới biết về đợt gây quỹ của bạn, bạn đang gây quỹ cho điều gì? Mọi thứ giải thích về đợt gây quỹ của bạn đều được viết ở đây.

![hình ảnh](assets/en/108.webp)

#### Mục tiêu của đợt gây quỹ

Đặt một số tiền mục tiêu mà đợt gây quỹ nên kiếm được cho dự án và đơn vị tiền tệ của mục tiêu. Đảm bảo rằng nếu mục tiêu của bạn được đặt theo các khoảng thời gian, bao gồm những ngày mục tiêu và kết thúc.

![hình ảnh](assets/en/109.webp)

#### Quyền lợi

Quyền lợi giúp ích rất nhiều cho việc gây quỹ của bạn. Điều này là bởi vì quyền lợi cung cấp cho mọi người một cách tham gia vào chiến dịch của bạn. Chúng tác động đến động cơ ích kỷ cũng như động cơ nhân ái. Và chúng cho phép bạn tiếp cận với việc xuống tiền của những người ủng hộ, không chỉ là hoàn toàn theo mục đích từ thiện của họ - bạn có thể đoán xem cái nào quan trọng hơn.

Tạo một quyền lợi mới bao gồm các trường sau:

- Tiêu đề
- Giá (cố định, tối thiểu, hoặc tùy chỉnh)
- URL Hình ảnh
- Mô tả
- Tồn kho
- ID
- Văn bản hiển thị Nút Mua.
- Bật/Tắt

Một khi chủ cửa hàng đã điền đầy đủ tất cả các trường của quyền lợi mới để tạo, nhấn vào lưu, và bạn sẽ thấy rằng phần Quyền lợi trong chiến dịch gây quỹ bây giờ đã được thêm vào và hiện lên.

![hình ảnh](assets/en/110.webp)

#### Đóng Góp

Chủ cửa hàng có thể lựa chọn cách thức hiển thị Quyền lợi, chúng được sắp xếp như thế nào, hoặc thậm chí được xếp hạng so với các quyền lợi khác. Tuy nhiên, một khi mục tiêu gây quỹ được đạt, chủ cửa hàng có thể muốn ngừng việc đóng góp vào đợt gây quỹ này. Do đó, anh ta có thể bật "Không cho phép đóng góp thêm sau khi đạt mục tiêu". Điều này sẽ ngừng nhận đóng góp cho chiến dịch.

##### Hành vi gây quỹ

Chỉ có hóa đơn được tạo với chiến dịch gây quỹ mới được tính vào mục tiêu. Tuy nhiên, có thể có trường hợp chủ cửa hàng muốn tất cả hóa đơn được tạo trong cửa hàng này đều được tính vào mục tiêu của đợt gây quỹ.

#### Tùy chọn bổ sung cho việc tuỳ chỉnh

BTCPay Server cung cấp một số tùy chỉnh bổ sung. Thêm âm thanh, hoạt ảnh, hoặc thậm chí là luồng thảo luận vào chiến dịch gây quỹ. Chủ cửa hàng cũng có thể thay đổi giao diện của đợt gây quỹ bằng cách nhập CSS tùy chỉnh của riêng mình.

#### Xóa ứng dụng này

Nếu chủ cửa hàng muốn xóa hoàn toàn đợt gây quỹ khỏi BTCPay Server của mình, ở cuối cập nhật Gây quỹ, chủ cửa hàng có thể Nhấn vào nút “Xóa ứng dụng này - Delete this app” để hủy bỏ hoàn toàn ứng dụng Gây quỹ của mình. Khi nhấn "Xóa ứng dụng này", BTCPay Server sẽ yêu cầu xác nhận bằng cách gõ `DELETE` và xác nhận bằng cách nhấn vào nút Xóa. Sau khi xóa, chủ cửa hàng trở lại bảng điều khiển BTCPay Server.

### BTCPay Server - Pay Button - Nút Thanh Toán

Các nút thanh toán HTML dễ tích hợp và có thể dễ dàng tùy chỉnh cho phép chủ cửa hàng nhận được tiền tip và quyên góp. Trong thanh menu bên trái của BTCPay Server, dưới mục Plugins, chủ cửa hàng có thể nhấp vào “Pay Button” và nhấp "Enable" để tạo một Nút thanh toán.

#### Cài đặt chung

Trong phần Cài đặt chung cho Nút thanh toán, chủ cửa hàng có thể thiết lập

- Giá tiêu chuẩn
- Tiền tệ mặc định
- Phương thức thanh toán mặc định
  - Sử dụng mặc định của cửa hàng
  - BTC on-chain
  - BTC off-chain (Lightning)
  - BTC of-chain (LNURL-pay)
- Mô tả thanh toán
- ID đơn hàng

#### Tùy chọn hiển thị

Nút thanh toán của BTCPay Server có thể được cấu hình để phù hợp với các phong cách khác nhau. Các nút có thể có một số tiền cố định hoặc tùy chỉnh, hiển thị bằng cách sử dụng thanh trượt hoặc các nút cộng và trừ.

#### Sử dụng Modal

Khi tạo nút thanh toán, chủ cửa hàng có thể chọn hành vi của nó khi khách hàng nhấp vào và hiển thị trong một modal hoặc trên một trang mới.

**!?Lưu ý!?**

Cảnh báo: Nút thanh toán chỉ nên được sử dụng cho tiền tip và quyên góp

Sử dụng nút thanh toán cho tích hợp thương mại điện tử không được khuyến khích vì thông tin liên quan đến đơn hàng có thể được người dùng chỉnh sửa. Đối với thương mại điện tử, bạn nên sử dụng Greenfield API của chúng tôi. Nếu cửa hàng này xử lý các giao dịch thương mại, chúng tôi khuyên bạn nên tạo một cửa hàng riêng biệt trước khi sử dụng nút thanh toán.

#### Tùy chỉnh văn bản hiển thị nút thanh toán

Mặc định, nút thanh toán của BTCPay Server hiển thị "Pay With BTCPay". Chủ cửa hàng có thể thiết lập văn bản này theo ý muốn và thay đổi logo BTCPay Server bằng logo của riêng họ. Thiết lập văn bản bằng cách sử dụng "Pay Button Text" và dán URL hình ảnh dưới "Pay Button Image URL".

##### Kích thước Hình ảnh

Kích thước của hình ảnh trong nút chỉ có thể được thiết lập thành ba kích cỡ mặc định.

- 146x40px
- 168x46px
- 209x57px

#### Loại nút

BTCPay Server nhận biết ba trạng thái cho Nút thanh toán.

- Số tiền cố định
  - Giá đã được thiết lập trước trong cài đặt chung của nút.
- Số tiền tùy chỉnh
  - Nút thanh toán của BTCPay Server có các nút + và - để thiết lập một giá tùy chỉnh.
  - Khi sử dụng số tiền tùy chỉnh, BTCPay Server sẽ yêu cầu một mức nhỏ nhất (Min), mức tối đa (Max) và mức độ tăng dần.
  - Các nút có thể được thiết lập để “Sử dụng kiểu nhập đơn giản”. Điều này loại bỏ các nút +/-.
  - Phù hợp nút inline nơi nút và các nút điều chỉnh hiển thị cùng một dòng.
- Thanh trượt
  - Tương tự như số tiền tùy chỉnh, tuy nhiên, khác biệt về mặt hình ảnh vì nó có thanh trượt thay vì các nút +/-.
  - Khi sử dụng thanh trượt, BTCPay Server sẽ yêu cầu một mức nhỏ nhất - Min, mức tối đa - Max và mức độ tăng dần.

**!?Lưu ý!?**

Xóa Nút thanh toán có thể được thực hiện ở phía trên trong mô tả cảnh báo.

#### Thông báo thanh toán

Server IPN (Instant Payment Notification) dành cho webhooks và có thể được điền bằng URL để đăng dữ liệu sau mua hàng.

#### Thông báo qua Email

Bất cứ khi nào có thanh toán, BTCPay Server có thể thông báo cho chủ cửa hàng.

#### Chuyển hướng trình duyệt

Khi khách hàng hoàn thành việc mua hàng, anh ta sẽ được chuyển hướng đến liên kết này nếu được chủ cửa hàng thiết lập.

#### Tùy chọn Nút thanh toán nâng cao

Chỉ định các tham số chuỗi truy vấn bổ sung nên được thêm vào trang thanh toán một khi hóa đơn được tạo. Ví dụ, `lang=da-DK` sẽ tải trang thanh toán bằng tiếng Đan Mạch theo mặc định.

#### Sử dụng ứng dụng làm Điểm cuối

Liên kết trực tiếp nút thanh toán với một mặt hàng trong một trong các ứng dụng Điểm bán hàng - PoS hoặc Chiến dịch gây quỹ - Crowdfund trước đó.
Các chủ cửa hàng có thể nhấp vào menu thả xuống và chọn Ứng dụng mong muốn; sau khi Ứng dụng được chọn, chủ cửa hàng có thể thêm mục cần được liên kết.

#### Mã được tạo

Vì nút thanh toán của BTCPay Server là HTML dễ nhúng, BTCPay Server hiển thị mã được tạo để sao chép vào một trang web ở phía dưới sau khi thiết lập xong cấu hình cho nút thanh toán.

Các chủ cửa hàng có thể sao chép mã được tạo để dán vào trang web của họ, và nút thanh toán từ BTCPay Server sẽ trực tiếp hoạt động trên trang web của họ.

### Tóm tắt kỹ năng

Trong phần này bạn đã học:

- Cách sử dụng plugin Điểm bán hàng - PoS tích hợp vào BTCPay Server để dễ dàng tạo một cửa hàng tùy chỉnh
- Cách sử dụng plugin Gây quỹ - Crowdfund tích hợp vào BTCPay Server để dễ dàng tạo một ứng dụng gây quỹ tùy chỉnh
- Tạo mã cho nút thanh toán tùy chỉnh sử dụng plugin Nút thanh toán

### Đánh giá kiến thức

Ba plugin tích hợp có sẵn với BTCPay Server là gì? Mô tả ngắn gọn cách mỗi plugin có thể được sử dụng.

# Cấu hình BTCPay Server

<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>

## Hiểu biết cơ bản về việc cài đặt BTCPay Server trên môi trường LunaNode

<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>

### Cài đặt BTCPay Server trên môi trường sử dụng dịch vụ hosting của bên thứ ba - Hosted Env. (LunaNode)

Những bước này sẽ cung cấp tất cả thông tin cần thiết để bắt đầu sử dụng BTCPay Server trên LunaNode. Có nhiều lựa chọn về cách triển khai phần mềm.
Bạn có thể tìm tất cả chi tiết của BTCPay Server tại https://docs.btcpayserver.org.

#### Bắt đầu từ đâu?

Trong phần này, bạn sẽ làm quen với LunaNode là nhà cung cấp dịch vụ hosting, tìm hiểu về những bước đầu tiên để sử dụng BTCPay Server của bạn, và tìm hiểu cách làm việc với Lightning Network. Sau khi chúng ta đã đi qua tất cả các bước, bạn có thể vận hành một cửa hàng trực tuyến hoặc nền tảng gây quỹ chấp nhận Bitcoin!

Đây là một trong nhiều cách để triển khai BTCPay Server. Đọc tài liệu của chúng tôi để biết thêm chi tiết,

https://docs.btcpayserver.org.

### Triển khai BTCPay Server - LunaNode

Đầu tiên, hãy truy cập vào trang web của LunaNode.com, nơi chúng ta sẽ tạo một tài khoản mới. Nhấp vào "Sign Up" ở góc trên bên phải hoặc sử dụng trình hướng dẫn "Get Started" trên trang chủ của họ.
![image](assets/en/111.webp)

Sau khi bạn đã tạo tài khoản mới, LunaNode sẽ gửi một email xác nhận. Một khi bạn xác nhận tài khoản, khác với Voltage, bạn ngay lập tức được yêu cầu nạp tiền vào số dư tài khoản của mình. Số dư này được dùng để thanh toán chi phí bộ nhớ máy chủ và dịch vụ hosting.

![image](assets/en/112.webp)

#### Nạp tiền vào tài khoản LunaNode của bạn

Khi bạn nhấp vào "Deposit credit", bạn sẽ được thiết lập số tiền muốn nạp vào tài khoản và phương thức thanh toán. LunaNode và BTCPay Server sẽ có phí từ 10$USD đến 20$USD hàng tháng.
Khác với Voltage.cloud, bạn sẽ có quyền truy cập đầy đủ vào Máy chủ ảo riêng của mình (VPS từ đây trở đi) và do đó có thêm một số quyền kiểm soát đối với máy chủ của mình. Sau khi bạn đã tạo tài khoản mới, LunaNode sẽ gửi một email xác nhận.
Một khi bạn xác nhận tài khoản, khác với Voltage, bạn ngay lập tức được yêu cầu nạp tiền vào số dư tài khoản của mình. Số dư này cần thiết để thanh toán chi phí bộ nhớ máy chủ và dịch vụ hosting.

#### Cách triển khai một máy chủ mới?

Trong hướng dẫn này, chúng ta sẽ đi qua quá trình thiết lập bằng cách tạo một bộ khóa API và sử dụng trình khởi chạy BTCPay Server do LunaNode tạo ra.

Trong bảng điều khiển LunaNode của bạn, nhấp vào API ở góc trên bên phải. Điều này mở ra một trang mới. Chúng ta chỉ cần đặt Tên cho khóa API. Phần còn lại sẽ được LunaNode xử lý và sẽ không được đề cập trong hướng dẫn này. Nhấp vào nút "Create API Credential".
Sau khi tạo xong thông tin xác thực API, bạn sẽ nhận được một chuỗi dài các chữ cái và ký tự. Đây là khóa API của bạn.

![image](assets/en/113.webp)

Có 2 phần cho thông tin xác thực này, khóa API và ID API; chúng ta sẽ cần cả hai. Trước khi chúng ta tiếp tục bước tiếp theo, hãy mở một tab mới trong trình duyệt và truy cập vào https://launchbtcpay.lunanode.com/

Tại đây, bạn sẽ được yêu cầu cung cấp khóa API và ID API của mình. Điều này để xác minh rằng chính bạn là người thiết lập máy chủ mới này. Khóa API vẫn nên được mở trong tab trước đó của bạn; nếu bạn cuộn xuống bảng bên dưới, bạn sẽ tìm thấy ID API.

Quay lại trang với Launcher, điền các trường với khóa API và ID của bạn, và nhấp vào tiếp tục.

![image](assets/en/114.webp)

Trong bước tiếp theo, bạn có thể cung cấp tên miền. Nếu bạn đã sở hữu một tên miền và muốn sử dụng nó cho BTCPay Server, hãy đảm bảo bạn cũng thêm bản ghi DNS (Gọi là bản ghi `A`) vào tên miền của mình. Nếu bạn không sở hữu một tên miền, hãy sử dụng tên miền do LunaNode cung cấp thay thế (bạn có thể thay đổi điều này sau trong cài đặt BTCPay Server) và nhấp vào `Tiếp tục - Continue`.

Đọc thêm về cách thiết lập hoặc thay đổi bản ghi DNS cho BTCPay Server; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name

#### Khởi chạy BTCPay Server trên LunaNode

Sau khi thực hiện các bước trước, chúng ta có thể thiết lập tất cả các tùy chọn cho máy chủ mới của mình. Tại đây chúng ta sẽ chọn Bitcoin (BTC) là đồng tiền được hỗ trợ; chúng ta có thể thiết lập email để nhận thông báo về việc gia hạn chứng chỉ mã hóa; điều này không bắt buộc.
Hướng dẫn này nhằm mục đích thiết lập một môi trường Mainnet (Bitcoin thực tế); tuy nhiên, LunaNode cũng cho phép bạn thiết lập này cho Testnet hoặc Regtest cho mục đích thử nghiệm và phát triển. Chúng tôi sẽ giữ tùy chọn Mainnet cho hướng dẫn này.
Chọn bản triển khai Lightning của bạn. LunaNode cung cấp hai triển khai khác nhau, LND và Core Lightning. Đối với hướng dẫn này, chúng tôi sẽ chọn LND. Có những khác biệt nhỏ nhưng thực sự giữa cả hai triển khai; để biết thêm về điều này, chúng tôi khuyên bạn đọc kỹ tài liệu mở rộng; https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln

![hình ảnh](assets/en/115.webp)

LunaNode cung cấp nhiều kế hoạch Máy ảo (VM) khác nhau. Những kế hoạch này khác nhau về phạm vi giá và thông số kỹ thuật của máy chủ. Đối với hướng dẫn này, một kế hoạch m2 là đủ; tuy nhiên, nếu bạn đã chọn nhiều đồng tiền hơn chỉ là Bitcoin làm tiền tệ, hãy xem xét sử dụng ít nhất m4.

Tăng tốc độ đồng bộ hóa blockchain ban đầu; điều này là tùy chọn và phụ thuộc vào nhu cầu của bạn. Có các tùy chọn nâng cao như thiết lập một Lightning Alias, chỉ định một phiên bản GitHub cụ thể, hoặc thiết lập khóa SSH; không có tùy chọn nào trong số này được đề cập trong hướng dẫn này.

Sau khi điền vào mẫu, bạn phải nhấp vào `Launch VM`, và Lunanode sẽ bắt đầu tạo VM mới của bạn, bao gồm cả việc cài đặt BTCPay Server trên đó. Quá trình này mất vài phút; một khi máy chủ của bạn sẵn sàng, LunaNode sẽ cung cấp cho bạn liên kết đến BTCPay Server mới của bạn.

Sau quá trình tạo, nhấp vào liên kết đến BTCPay Server của bạn; tại đây, bạn sẽ được yêu cầu tạo một tài khoản quản trị viên.

![hình ảnh](assets/en/116.webp)

### Tóm tắt kỹ năng

Trong phần này bạn đã học:

- Tạo và nạp tiền vào tài khoản trên LunaNode
- Sử dụng BTCPay Server Launcher để tạo máy chủ của riêng bạn

### Đánh giá kiến thức

#### Đánh giá kiến thức lý thuyết

Mô tả một số sự khác biệt giữa việc chạy một phiên bản của BTCPay Server trên một Máy chủ riêng ảo so với việc tạo một tài khoản trên một phiên bản được tự host.

## Cài Đặt BTCPay Server trên môi trường Voltage

<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>

Bạn sẽ làm quen với Voltage.cloud là nhà cung cấp dịch vụ hosting, tìm hiểu về các bước đầu tiên khi sử dụng BTCPay Server của mình, và học cách làm việc với Lightning Network. Sau khi chúng ta đã đi qua tất cả các bước, bạn có thể chạy một cửa hàng trực tuyến hoặc nền tảng gây quỹ chấp nhận Bitcoin!

Đây là một trong nhiều cách để triển khai BTCPay Server. Đọc tài liệu của chúng tôi để biết thêm chi tiết,
https://docs.btcpayserver.org.

### BTCPay Server - Triển khai Voltage.cloud

Đầu tiên, truy cập website Voltage.cloud và đăng ký một tài khoản mới. Khi tạo tài khoản, bạn có thể đăng ký trải nghiệm miễn phí 7 ngày. Hoặc nhấp vào Sign Up ở góc phải trên cùng hoặc sử dụng "Try a free 7 day trial" trên trang chủ của họ.

![hình ảnh](assets/en/117.webp)

Sau khi bạn đã tạo một tài khoản, nhấp vào nút `NODES` trên bảng điều khiển của bạn. Một khi chúng ta đã chọn Nodes và tạo một node mới, chúng ta được giới thiệu tới các node mà Voltage cung cấp. Vì hướng dẫn này cũng sẽ đi vào LightningNetwork, tại Voltage, chúng ta đầu tiên phải chọn triển khai Lightning của mình trước khi tạo một BTCPay Server. Nhấp vào Lightning Node.

![hình ảnh](assets/en/118.webp)
Tại đây, bạn sẽ phải chọn loại Lightning Node mà bạn muốn. Voltage cung cấp nhiều lựa chọn cho cấu hình lighting của bạn. Điều này khác biệt khi triển khai với, ví dụ như, LunaNode. Đối với mục đích của hướng dẫn này, một Lite Node là đủ. Đọc thêm về sự khác biệt tại Voltage.cloud.
![image](assets/en/119.webp)

Đặt tên cho node của bạn, thiết lập một mật khẩu và bảo mật nó. Nếu mất mật khẩu này, bạn sẽ mất quyền truy cập vào các bản sao lưu, và Voltage không thể khôi phục nó. Tạo node, và Voltage sẽ hiển thị tiến trình. Voltage đã tạo Lightning Node của bạn. Bây giờ chúng ta có thể tạo BTCPay Server Instance và truy cập trực tiếp vào Lightning Network.

Nhấp vào Nodes ở góc trên bên trái của bảng điều khiển của bạn. Tại đây bạn có thể thiết lập phần tiếp theo của BTCPay Server Instance của mình. Nhấp vào `Tạo mới - Create new` một khi bạn ở trang tổng quan các node. Bạn sẽ nhận được một màn hình tương tự như trước. Bây giờ thay vì Lightning Node, chúng ta chọn BTCPay Server.

Voltage hiển thị vị trí địa lý của BTCPay Server của bạn, voltage lưu trữ ở khu vực Tây nước Mỹ. Tại đây bạn cũng sẽ thấy chi phí hosting cho máy chủ. Nhấp vào `Tạo Create` và đặt tên cho BTCPay Server của bạn. Kích hoạt Lightning và Voltage sẽ hiển thị Lightning Node được tạo trong bước trước. Nhấp vào `Tạo - Create`, và Voltage sẽ tạo một BTCPay Server Instance.

![image](assets/en/120.webp)

Sau khi bạn nhấp vào `Tạo - Create`, Voltage sẽ cung cấp cho bạn tên người dùng và mật khẩu mặc định. Chúng tương tự như mật khẩu bạn đã thiết lập trước đó trong Voltage. Nhấp vào nút `Đăng nhập vào tài khoản - Login to Account` để được chuyển hướng đến BTCPay Server của bạn.

Chào mừng đến với BTCPay Server Instance mới của bạn. Vì chúng tôi đã thiết lập Lightning trong quá trình tạo, nó sẽ hiển thị Lightning đã được kích hoạt!

### Tóm tắt kỹ năng

Trong chương này bạn đã học:

- Tạo một tài khoản trên Voltage.cloud
- Các bước để vận hành BTCPay Server cùng với một Lightning Node trên tài khoản

### Đánh giá kiến thức

#### Đánh giá kiến thức lý thuyết

Những điểm khác biệt chính giữa cài đặt Voltage và LunaNode là gì?

## Cài đặt BTCPay Server trên một node Umbrel

<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>

Sau những bước này, bạn có thể chấp nhận thanh toán Lightning cho cửa hàng BTCPay của mình trên mạng nội bộ. Quy trình này cũng áp dụng nếu bạn vận hành một node umbrel trong một nhà hàng hoặc doanh nghiệp. Nếu bạn muốn kết nối cửa hàng này với một website công cộng, theo dõi bài tập Nâng cao để đưa node umbrel của bạn ra công chúng.

https://umbrel.com/

![image](assets/en/121.webp)

### BTCPay Server - Triển khai Umbrel

Sau khi node Umbrel của bạn đã đồng bộ hoàn toàn với blockchain Bitcoin, đi đến Umbrel App Store, và tìm kiếm BTCPay Server dưới mục Apps.

![image](assets/en/122.webp)

Nhấp vào BTCPay Server để xem chi tiết App. Khi chi tiết của BTCPay Server được mở, phía dưới bên phải hiển thị các yêu cầu để App hoạt động đúng cách. Chúng ta sẽ thấy nó yêu cầu Bitcoin Node và Lightning Node. Nếu bạn chưa cài đặt Lightning Node trên Umbrel của mình, nhấp vào Install. Quá trình này có thể mất vài phút.

![image](assets/en/123.webp)

Sau khi cài đặt Lightning Node của bạn:

1. Nhấp mở trong chi tiết app hoặc trên App trong bảng điều khiển Umbrels.
2. Nhấp vào thiết lập một node mới; bạn sẽ được hiển thị 24 từ cho việc khôi phục Lightning node của mình.
3. Ghi chúng lại.

![image](assets/en/124.webp)
Umbrel sẽ yêu cầu xác minh các từ vừa được ghi lại. Sau khi cài đặt Lightning Node, quay lại Umbrel App Store và tìm BTCPay Server. Nhấn vào nút cài đặt, và Umbrel sẽ hiển thị nếu các thành phần cần thiết đã được cài đặt và BTCPay Server yêu cầu quyền truy cập vào các thành phần này. Sau khi cài đặt, nhấn `Mở - Open` ở góc trên bên phải của chi tiết Ứng dụng hoặc mở BTCPay Server qua bảng điều khiển của Umbrel.

Umbrel sẽ yêu cầu xác minh các từ khôi phục vừa được ghi lại.

![hình ảnh](assets/en/125.webp)

**!?Lưu ý!?**

Hãy chắc chắn lưu trữ chúng ở một vị trí thích hợp như bạn đã được học khi lưu trữ khóa riêng tư.

Sau khi cài đặt Lightning Node, quay lại Umbrel App Store và tìm BTCPay Server. Nhấn vào nút cài đặt, và Umbrel sẽ hiển thị nếu các thành phần cần thiết đã được cài đặt và BTCPay Server yêu cầu quyền truy cập vào các thành phần này.

![hình ảnh](assets/en/126.webp)

Sau khi cài đặt, nhấn `Mở - Open` ở góc trên bên phải của chi tiết ứng dụng hoặc mở BTCPay Server qua bảng điều khiển của Umbrel.

![hình ảnh](assets/en/127.webp)

### Tóm tắt kỹ năng

Trong phần này bạn đã học:

- Các bước để cài đặt BTCPay Server với chức năng Lightning trên một nút Umbrel

### Đánh giá kiến thức

#### Đánh giá kiến thức lý thuyết

Cài đặt trên Umbrel khác với hai lựa chọn sử dụng dịch vụ hosting trước đó như thế nào?

# Kết Luận

<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>



## Đánh giá khóa học
<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>
<isCourseReview>true</isCourseReview>

## Kết luận khoá học

<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

![hình ảnh](assets/en/128.webp)

Bạn cũng nên có một hiểu biết tổng quan về Bitcoin là gì, nó hoạt động như thế nào, và nó có thể mở rộng như thế nào với các lớp thứ hai như Lightning Network. Trong khóa học này, chúng tôi đã đề cập đến việc sử dụng BTCPay Server một cách toàn diện, từ việc cài đặt ban đầu đến việc tạo cửa hàng và quản lý hóa đơn phức tạp, để trở thành một cá nhân hoặc doanh nghiệp tự chủ về tài chính.

Xin chúc mừng bạn đã hoàn thành khóa học này. Chúng tôi hy vọng bạn thích nội dung khoá học và tiếp tục sử dụng và khám phá BTCPay Server, và như chúng tối, sẽ cảm thấy phấn khích về tương lai hứa hẹn mà Bitcoin và cộng đồng ngày càng phát triển của các nhà xây dựng và người tham gia sẽ mang lại.

> **FOSS là điều chắc chắn sẽ xảy ra - FOSS is inevitable.**

### Từ vựng liên quan

| Thuật Ngữ                               | Định Nghĩa                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 51% Attack - Tấn công 51%               | Hành động xây dựng một blockchain mới dài nhất để thay thế các khối trong blockchain. Điều này cho phép bạn thay thế các giao dịch đã được đào trong blockchain. Loại tấn công này dễ thực hiện nhất khi bạn có phần lớn sức mạnh đào, đó là lý do tại sao nó được gọi là “Tấn công Đa Số” hoặc “Tấn công 51%”.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| AccountKey - Khoá tài khoản             | Khóa tài khoản để rebase                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| AccountKeyPath                          | Đường dẫn từ gốc đến khóa tài khoản được tiền tố bởi dấu vân tay khóa công khai chính.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Địa chỉ                                 | Địa chỉ Bitcoin mã hóa thông tin cần thiết để thanh toán cho người nhận. Một địa chỉ hiện đại bao gồm một chuỗi các chữ cái và số bắt đầu với bc1 và có dạng tương tư như bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4. Địa chỉ là cách viết tắt cho script khóa của người nhận, người gửi sử dụng địa chỉ này để chuyển tiền cho người nhận. Hầu hết các địa chỉ hoặc là đại diện cho khóa công khai của người nhận hoặc một số hình thức script định nghĩa các điều kiện chi tiêu phức tạp hơn. Ví dụ trước đây là một địa chỉ bech32 mã hóa một chương trình chứng nhận khóa tiền vào hash của một khóa công khai (Xem Pay-to-Witness-Public-Key-Hash). Cũng có các định dạng địa chỉ cũ hơn bắt đầu với 1 hoặc 3 sử dụng mã hóa địa chỉ Base58Check để đại diện cho hash của khóa công khai hoặc hash của script. |
| Loại dịa chỉ                            | Một địa chỉ có thể đại diện cho nhiều script khác nhau. Địa chỉ được mã hóa và có tiền tố để truyền đạt loại script của chúng. Địa chỉ Legacy sử dụng Base58, và khi một địa chỉ Legacy là mã băm của một khóa công khai, một địa chỉ P2PKH, nó bắt đầu với ‘1’. Ít thường xuyên hơn, một địa chỉ legacy là mã băm của một script, trong trường hợp đó nó sẽ bắt đầu với ‘3’. Hiện tại, tất cả địa chỉ SegWit được mã hóa trong Bech32 và bắt đầu với tiền tố ‘bc1’.                                                                                                                                                                                                                                                                                                                                              |
| Ứng dụng                                | BTCPay Server có các plugin có thể hoạt động như một ứng dụng độc lập.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| BIP 329                                 | Xuất/nhập nhãn ví                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| BIP49                                   | Định nghĩa sơ đồ phái sinh cho ví HD sử dụng định dạng serialization P2WPKH-nested-in-P2SH (BIP 141) cho các giao dịch SegWit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Địa chỉ Bitcoin - Bitcoin Address        | Chuỗi ký tự chữ và số nơi bạn gửi bitcoin của mình, vì vậy bitcoin nằm ở đó, nó bao gồm một chuỗi khoảng 33 chữ cái và số kết hợp. Trong phiên bản giao thức hiện tại, một địa chỉ bắt đầu với 1, 3, hoặc b. Có địa chỉ của người nhận là một phần cần thiết để khởi tạo giao dịch bitcoin. Địa chỉ Bitcoin được tạo từ khóa công khai và nhiều địa chỉ có thể được tạo từ một bộ khóa công khai để cải thiện sự riêng tư. Địa chỉ Bitcoin hoạt động giống như địa chỉ email, nếu bạn muốn gửi một tin nhắn bạn cần biết nó đang đi đâu, tương tự như với bitcoin. Trước khi gửi một giao dịch bitcoin, bạn cần đảm bảo rằng địa chỉ của người nhận chính xác vì giao dịch bitcoin không thể đảo ngược và bạn có thể đang gửi bitcoin đến địa chỉ không thuộc về người nhận.                   |
| bitcoin so với Bitcoin                  | Bitcoin là mạng lưới tiền tệ, và bitcoin (viết thường) là đơn vị tiền tệ trên mạng lưới Bitcoin. Bạn sử dụng tiền tệ bitcoin hoặc token để giao dịch trên mạng Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Khối - Block                            | Một khối - block là cấu trúc dữ liệu trong blockchain Bitcoin bao gồm một tiêu đề và một phần thân gồm các giao dịch Bitcoin. Khối được gán nhãn thời gian và gắn với một khối phía trước (khối cha) cụ thể. Khi được băm, tiêu đề khối cung cấp bằng chứng công việc làm cho blockchain trở nên gần như không thể thay đổi theo một xác suất nào đó. Các khối phải tuân thủ các quy tắc được thực thi bởi sự đồng thuận của mạng lưới để mở rộng blockchain. Khi một khối được thêm vào blockchain, các giao dịch nằm trong đó được coi là đã có xác nhận đầu tiên.                                                                                                                                                                                                                                                                 |
| Trình duyệt blockchain - Block Explorer     | Một công cụ trực tuyến cho phép bạn tìm kiếm thông tin thời gian thực và lịch sử về một blockchain, bao gồm dữ liệu liên quan đến khối, giao dịch, địa chỉ, và nhiều hơn nữa.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Mã băm của khối - Block Hash                 | Mã băm của một khối là mã của hàm băm SHA-256 của dữ liệu khối, thường được biểu diễn dưới dạng hệ thập lục phân. Mã hash khối có thể được hiểu như một số rất lớn. Để đáp ứng yêu cầu Bằng chứng công việc (Proof-of-Work), mã băm của một khối phải nhỏ hơn một ngưỡng nhất định. Do đó, tất cả mã băm của khối bắt đầu bằng một chuỗi các chữ số 0 rồi tiếp đến là một chuỗi ký tự chữ và số. Một số khối có tới hai mươi chữ số 0 đứng đầu, trong khi các khối trước đây có ít hơn như chỉ tám chứ số không. Số lượng chữ số 0 yêu cầu phản ánh sơ bộ về độ khó của việc đào vào thời điểm khối được công bố.                                                                                                                                                                                                                        |
| Chiều cao khối - Block Height                 | Mỗi khối được đánh số theo thứ tự tăng dần, bắt đầu từ số không.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Phần thưởng khối - Block Reward           | Bao gồm trợ cấp khối (bitcoin mới được in tạo) và tổng số phí giao dịch từ các giao dịch được đính kèm trong khối.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Kích thước khối - Block Size               | Mỗi khối có một lượng giới hạn có thể chứa dữ liệu. Dữ liệu không vừa vào một khối nhất định sẽ được ghi lại trong một trong số các khối tiếp theo. Đối với các khối bitcoin, trước đây có kích thước giới hạn là 1mb, tuy nhiên sau một soft fork (SegWit) kích thước khối tối đa có thể lên đến 4mb dữ liệu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Trợ cấp khối - Block Subsidy               | Lượng bitcoin mới được tạo ra trong mỗi khối. Mỗi khối được đào và thêm vào blockchain cho phép người tạo khối in ra một lượng bitcoin mới nhất định. Trợ cấp khối bắt đầu từ 50 BTC mỗi khối, và được cắt giảm một nửa sau mỗi 210,000 khối hoặc khoảng 4 năm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Blockchain                              | Một cuốn sổ cái phân tán, hoặc cơ sở dữ liệu, của tất cả giao dịch Bitcoin. Giao dịch được nhóm trong các đợt cập nhật rời rạc gọi là khối, giới hạn lên đến 4 triệu đơn vị weight. Các khối được tạo ra (đào) khoảng mỗi 10 phút thông qua một quá trình ngẫu nhiên gọi là đào coin. Mỗi khối bao gồm một "bằng chứng công việc" đòi hỏi tính toán phức tạp. Yêu cầu về bằng chứng công việc được sử dụng để điều chỉnh khoảng thời gian giữa các khối và bảo vệ blockchain khỏi các cuộc tấn công nhằm viết lại lịch sử: kẻ tấn công cần phải vượt qua bằng chứng công việc hiện có để thay thế các khối đã được công bố, làm cho mỗi khối có tính gần như bất biến theo xác suất khi nó được chôn dưới các khối tiếp theo.                                                                                                            |
| BTCPay Server Vault                     | Để cân bằng tối ưu giữa sự tiện lợi, an toàn và riêng tư, nên sử dụng Ví BTCPay Server với một ví cứng. BTCPay Vault được xây dựng để kết nối ví cứng với BTCPay Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Bài toán các vị tướng Byzantine - Byzantine General's Problem             | Một vấn đề trong lý thuyết trò chơi mô tả khó khăn mà các bên phi tập trung gặp phải khi cần đạt được sự đồng thuận mà không dựa vào một bên trung tâm đáng tin cậy. Tên gọi xuất phát từ tình huống của một số tướng đang bao vây Byzantium. Họ đã bao vây thành phố, nhưng phải quyết định cùng nhau về thời điểm tấn công. Nếu tất cả các tướng tấn công cùng một lúc, họ sẽ chiến thắng, nhưng nếu họ tấn công vào các thời điểm khác nhau, họ sẽ thua. Các tướng không có kênh liên lạc an toàn với nhau vì bất kỳ thông điệp nào họ gửi hoặc nhận có thể đã bị chặn hoặc thay đổi bởi những người bảo vệ Byzantium. Làm thế nào các tướng có thể tổ chức tấn công cùng một lúc?                                                                                                                            |
| Kiểm duyệt - Censorship                  | Kiểm soát thông tin nào có thể được truyền đến quần chúng. Khi nói đến bitcoin, kiểm duyệt là khả năng ngăn chặn một giao dịch nào đó bởi bên thứ ba.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Tiền thối - Change                      | Phần của các UTXO được trả lại vào ví của người gửi, thường qua một địa chỉ khác. Bằng cách tính tổng số đầu vào trừ đi số tiền đã tiêu và phí giao dịch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Child Pays For Parent (CPFP)            | Kỹ thuật tăng phí giao dịch, trong đó người dùng chi tiêu một đầu ra từ một giao dịch chưa xác nhận có mức phí thấp trong một giao dịch con với mức phí cao nhằm khuyến khích các thợ đào đưa cả hai giao dịch vào trong một khối.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Giao dịch Coinbase - Coinbase Transaction        | Giao dịch đầu tiên trong mỗi khối, phân phối phần thưởng khối (gồm trợ cấp khối + tổng phí các giao dịch trong khối) cho người đã đào được khối đó.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Vấn đề trùng khớp kép về nhu cầu - Coincidence of Wants                    | Hiện tượng kinh tế khi hai bên mỗi bên sở hữu một mặt hàng mà bên kia mong muốn, vì vậy họ trao đổi những mặt hàng này trực tiếp mà không cần thông qua trung gian tiền tệ.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Lưu trữ lạnh - Cold Storage              | Cách quản lý dữ liệu mà không cần kết nối internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Ví lạnh - Cold Wallet                             | Loại ví bitcoin lưu trữ khóa riêng tư của bạn ngoại tuyến, thường trên một thiết bị vật lý. Còn được biết đến như một ví cứng, và nó bảo vệ bitcoin của bạn khỏi hacker trực tuyến bằng cách sử dụng thiết bị giống như ổ đĩa flash không kết nối internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Giao diện dòng lệnh - Command Line Interface (CLI)            | Tương tác với thiết bị hoặc chương trình máy tính bằng các lệnh từ người dùng hoặc khách hàng, và phản hồi từ thiết bị hoặc chương trình, dưới dạng các dòng văn bản.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Giao dịch cam kết - Commitment Transaction                  | Giao dịch cam kết là một giao dịch Bitcoin, được ký bởi cả hai đối tác kênh, mã hóa số dư mới nhất của một kênh. Mỗi khi một khoản thanh toán mới được thực hiện hoặc chuyển tiếp sử dụng kênh, số dư kênh sẽ được cập nhật, và một giao dịch cam kết mới sẽ được ký bởi cả hai bên. Quan trọng, trong một kênh giữa Alice và Bob, cả Alice và Bob giữ phiên bản của riêng mình về giao dịch cam kết, cũng được ký bởi bên kia. Bất kỳ lúc nào, kênh có thể được đóng bởi Alice hoặc Bob nếu họ nộp giao dịch cam kết của mình lên blockchain Bitcoin. Nộp một giao dịch cam kết cũ (lỗi thời) được coi là gian lận (tức là, vi phạm giao thức) trong Lightning Network và có thể bị phạt bởi bên kia, bên đó sẽ lấy tất cả các tiền trong kênh cho mình, thông qua một giao dịch phạt.                                       |
| Xác nhận - Confirmation                | Một khi giao dịch được đưa vào trong một khối, nó có một xác nhận. Ngay khi một khối khác được đào trên blockchain, giao dịch có hai xác nhận, và cứ thế tiếp tục. Sáu xác nhận trở lên được coi là đủ để giao dịch không thể được đảo ngược.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Gây quỹ cộng đồng - Crowdfund (CF)                          | Một plugin mặc định của BTCPay Server cho phép chủ cửa hàng dễ dàng tạo một trang web gây quỹ điển hình. Họ có thể dễ dàng đặt mục tiêu, tạo các quyền lợi cho các khoản đóng góp, và tùy chỉnh theo nhu cầu của mình.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Mật mã - Cryptography                     | Một hệ thống đặc biệt, nơi thông điệp gốc được thay đổi sao cho chỉ những người nhận được xác định trước mới có thể nhận được.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Bảng điều khiển - Dashboard               | Trang điều khiển chính của BTCPay Server. Nó cung cấp một cái nhìn tổng quan về tất cả hoạt động cho một cửa hàng, hiển thị qua nhiều ô.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Demo                                    | Đề cập đến môi trường ảo mà các bản demo phần mềm diễn ra.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Triển khai - Deployment                     | Triển khai phần mềm là tất cả các hoạt động làm cho một hệ thống phần mềm sẵn sàng để sử dụng. Quá trình triển khai chung bao gồm nhiều hoạt động liên quan với các chuyển tiếp có thể xảy ra giữa chúng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Đường dẫn phái sinh - Diviation Path        | Một dữ liệu chỉ ra cho ví phân cấp tất định (HD) cách phái sinh một khóa cụ thể trong một cây khóa. Đường dẫn phái sinh được sử dụng như một tiêu chuẩn Bitcoin và được giới thiệu cùng với ví HD như một phần của BIP 32.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Điều chỉnh độ khó - Difficulty Adjustment      | Điều chỉnh mục tiêu độ khó, cứ sau 2016 khối (khoảng hai tuần) để đảm bảo rằng các khối được khai thác trung bình mỗi 10 phút một lần. Từ đó tạo ra một khoảng thời gian nhất quán giữa các khối và một lượng phát hành bitcoin mới nhất quán (thông qua trợ cấp khối).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Mục tiêu độ khó - Difficulty Target            | Trong hoạt động đào coin, đây là một số mà mã băm của khối phải thấp hơn để khối đó được thêm vào blockchain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Chữ ký số - Digital Signature                   | Chữ ký số là một phương pháp toán học để xác minh tính xác thực và toàn vẹn của các thông điệp hoặc tài liệu số. Nó có thể được coi là một cam kết mật mã trong đó thông điệp không bị ẩn giấu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Dễ chia nhỏ - Divisible                         | Tính chất của một hàng hóa có thể được chia nhỏ thành các lượng nhỏ hơn mà không mất giá trị. Bởi vì các giao dịch kinh tế thường xảy ra với các giá trị khác nhau, một loại tiền tệ phải dễ dàng chia nhỏ được để có thể sử dụng rộng rãi trong nền kinh tế.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Docker                                  | Phần mềm dùng để đóng gói phần mềm vào các đơn vị tiêu chuẩn gọi là container chứa mọi thứ phần mềm cần để chạy bao gồm thư viện, công cụ hệ thống, mã nguồn và thời gian chạy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Lặp chi - Double-Spend                        | Kết quả của việc chi tiêu thành công một số tiền hơn một lần. Bitcoin bảo vệ chống lại việc lặp chi bằng cách xác minh rằng mỗi giao dịch được thêm vào blockchain tuân thủ các quy tắc đồng thuận; điều này có nghĩa là kiểm tra để đảm bảo rằng các đầu vào cho giao dịch chưa được chi tiêu trước đó.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Bền vững - Durable                               | Tính chất của tiền, trong đó tiền tệ có thể duy trì trạng thái ban đầu theo thời gian và chịu được việc dùng đi dùng lại nhiều lần. Một đồng tiền bền vững phải có khả năng sống sót trước các rủi ro tiềm ẩn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Electrum                                | Electrum là một trong những ví Bitcoin phổ biến nhất, được tạo ra vào năm 2011.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Khóa công khai mở rộng - Extended Public Key (Xpub)           | Khóa công khai mở rộng còn được biết đến là Xpub, một khóa công khai hoạt động như một khóa cha cho các khóa được phái sinh từ Xpub như một tính năng của ví HD. Xpub là một tiêu chuẩn được giới thiệu trong BIP 32. Ví sử dụng nó một cách ẩn danh để phái sinh các khóa công khai con. Người ta không ngăn cản việc chia sẻ công khai Xpub, tài sản của bạn sẽ không có nguy cơ bị đánh cắp trực tiếp, Xpub không thể phái sinh các khóa riêng tư. Lợi ích của việc chia sẻ một Xpub có thể là cho mục đích gây quỹ trong BTCPay Server. Xpub được chia sẻ thông qua phương tiện trực tuyến, trong khi các khóa riêng tư vẫn ở ngoại tuyến trên một HWW.                                                                                                                                                                          |
| F.U.D.                                  | Viết tắt của Fear, uncertainty and doubt (Sợ hãi, không chắc chắn và nghi ngờ); Thường được gợi lên một cách có chủ ý nhằm đặt một đối thủ vào tình thế bất lợi.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Phí - Fee                              | Trong bối cảnh của Lightning Network, các nút sẽ thu phí định tuyến cho việc chuyển tiếp các khoản thanh toán cho người dùng khác. Các node cá nhân có thể thiết lập chính sách phí của riêng mình, được tính toán dựa trên tổng số của một phí cơ bản cố định và một tỷ lệ phí phụ thuộc vào số tiền thanh toán. Trong bối cảnh của Bitcoin, người gửi của một giao dịch trả một phí giao dịch cho các thợ đào để giao dịch được đưa vào trong một khối. Phí giao dịch Bitcoin không bao gồm phí cơ bản và phụ thuộc tuyến tính vào dung lượng dữ liệu (weight) của giao dịch, nhưng không phụ thuộc vào số tiền.                                                                                                                                                                                                                             |
| Tiền pháp định - Fiat                  | Đồng tiền do chính phủ phát hành không được bảo chứng bởi một hàng hóa như vàng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Không vô hạn - Finite                   | Ám chỉ nguồn cung Bitcoin được giới hạn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Chia tách - Fork                         | Sự thay đổi đối với một giao thức hoặc một đoạn mã. Fork thường được giới thiệu để nâng cấp một dự án. Trong cộng đồng mã nguồn mở, fork tồn tại bởi vì nhiều cá nhân chọn tải xuống và chạy cùng một phần mềm vào các thời điểm khác nhau và không phải lúc nào cũng cập nhật. Nếu hai người dùng tải xuống và chạy phiên bản 1 của một phần mềm, và chỉ một người dùng nâng cấp khi phiên bản 2 được phát hành, người dùng đã cập nhật đang chạy một fork của phiên bản 1.                                                                                                                                                                                                                                                                                                                                            |
| Giao dịch cấp vốn - Funding Transaction        | Giao dịch cấp vốn được sử dụng để mở một kênh thanh toán. Giá trị (bằng bitcoin) của giao dịch này chính xác là khả năng của kênh thanh toán. Đầu ra của giao dịch này là một kịch bản đa chữ ký dạng 2-trong-2 (multisig) nơi mỗi đối tác kênh kiểm soát một khóa. Do bản chất đa chứ ký của nó, nó chỉ có thể được chi tiêu bằng sự đồng thuận giữa các đối tác kênh. Nó cuối cùng sẽ được chi tiêu bởi một trong các giao dịch cam kết hoặc bởi giao dịch đóng.                                                                                                                                                                                                                                                                                                                                                       |
| Tính đổi lẫn - Fungible                                | Là cái gì đó (như tiền tệ hoặc hàng hóa) có tính chất mà một phần hoặc lượng nhất định có thể được thay thế bằng một phần hoặc lượng bằng nhau khác trong việc thanh toán nợ hoặc tất toán một khoản tiền (Các đồng tiền có giá trị như nhau có thể đổi lẫn, thay thế cho nhau).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Gap Limit                               | Ám chỉ số lượng địa chỉ công khai tiêu chuẩn được kiểm tra để tìm giao dịch trong blockchain nhằm tính toán số dư của một tài khoản. Giao dịch nhận được trên một địa chỉ vượt quá Gap Limit không được phát hiện.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Khối khởi nguyên - Genesis Block                           | Khối đầu tiên trong blockchain Bitcoin. Satoshi Nakamoto, người tạo ra Bitcoin, đã khai thác khối Genesis vào ngày 3 tháng 1 năm 2009 và đã bao gồm dòng tít của tờ Financial Times ngày hôm đó, “Chancellor on brink of second bailout for banks.”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Github                                  | Một nền tảng và dịch vụ dựa trên đám mây cho phát triển phần mềm và kiểm soát phiên bản sử dụng Git, cho phép các nhà phát triển lưu trữ và quản lý mã nguồn của họ.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Giao thức Gossip - Gossip Protocol        | Các node LN gửi và nhận thông tin về cấu trúc của Lightning Network thông qua các tin nhắn gossip được trao đổi với các đối tác. Giao thức gossip chủ yếu được định nghĩa trong BOLT #7 và định nghĩa định dạng của các tin nhắn node_announcement, channel_announcement, và channel_update. Để ngăn chặn spam, tin nhắn thông báo node chỉ được chuyển tiếp nếu node đã có một kênh, và tin nhắn thông báo kênh chỉ được chuyển tiếp nếu giao dịch cấp vốn của kênh đã được xác nhận bởi mạng Bitcoin. Thông thường, các Lightning Node kết nối với các đối tác kênh của họ, nhưng cũng có thể kết nối với bất kỳ Lightning Node nào khác để xử lý tin nhắn gossip.                                                                                                                                                         |
| Định luật Gresham - Gresham's Law         | Luật nói rằng “tiền xấu đẩy tiền tốt ra khỏi lưu thông”. Nói cách khác, trong một nền kinh tế nơi hai loại tiền tệ được sử dụng, cá nhân sẽ chi tiêu tiền có phẩm chất kém trước, loại tiền này liên tục mất giá, và giữ tiền có phẩm chất tốt lại, loại tiền giữ được giá trị của mình. Do đó, "tiền xấu" sẽ chiếm ưu thế về mặt lưu thông và sử dụng trong các giao dịch hàng ngày, trong khi "tiền tốt" sẽ chiếm ưu thế về mặt tiết kiệm và đầu tư dài hạn.                                                                                                                                                                                                                                                                                                                                                                                                  |
| Halving                                 | Sự kiện giảm tỷ lệ phát hành bitcoin đi một nửa sau mỗi 210,000 khối (khoảng bốn năm).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Chia tách cứng - Hard Fork               | Sự thay đổi đồng thuận không tương thích ngược. Tính không tương thích ngược xảy ra khi một hành vi trước đây không hợp lệ được chấp nhận là hợp lệ. Để duy trì đồng thuận qua một hard fork, tất cả các node đều phải nâng cấp. Nếu không, các nút cũ sẽ từ chối giao dịch hoặc khối mới do họ đang theo các quy tắc cũ, trong khi các nút đã nâng cấp sẽ chấp nhận chúng là hợp lệ. Vì lý do này, trong Bitcoin, hard fork được tránh bằng mọi giá.                                                                                                                                                                                                                                                                                                                                                                     |
| Ví cứng - Hardware Wallet (HWW)                   | Một loại ví Bitcoin đặc biệt lưu trữ khóa riêng tư của người dùng trong một thiết bị phần cứng an toàn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Hàm băm - Hash Function                           | Một hàm băm mật mã là một thuật toán toán học ánh xạ dữ liệu kích thước tùy ý thành một chuỗi bit có kích thước cố định (một mã băm) và được thiết kế thành hàm một chiều, tức là, một hàm không thể đảo ngược. Cách duy nhất để tái tạo dữ liệu đầu vào từ đầu ra của một hàm băm mật mã lý tưởng là thử nghiệm tìm kiếm vét cạn (brute-force) các đầu vào có thể để thử xem chúng có tạo ra kết quả khớp không.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Tốc độ băm - Hash Rate                               | Một đại lượng để đo lường số lượng mã băm mà các thợ đào tạo ra mỗi giây trên mạng lưới Bitcoin. Một mã băm đơn lẻ là một nỗ lực tạo ra Bằng chứng Công việc cho một khối.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Ví nóng - Hot Wallet                              | Một thiết bị có kết nối bên ngoài, đặc biệt là kết nối internet. Ví nóng một ví Bitcoin kết nối với internet. Những ví này tiện lợi hơn cho việc chi tiêu hàng ngày, nhưng không an toàn bằng các lựa chọn lưu trữ lạnh vì chúng tương tác với internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Tải về lần đầu - Initial Block Download (IBD)            | Quá trình xây dựng toàn bộ blockchain Bitcoin từ đầu. Khi một node mới được thiết lập và tham gia vào mạng, nó kết nối với các node khác và yêu cầu họ gửi các khối. Node mới xử lý các khối này và xây dựng blockchain cho đến khi nó bắt kịp và đồng bộ với mạng lưới.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Hoá đơn - Invoice                                 | Một tài liệu thương mại do người bán phát hành cho người mua liên quan đến một giao dịch bán hàng và chỉ ra các sản phẩm, số lượng, và giá đã thỏa thuận cho các sản phẩm hoặc dịch vụ mà người bán đã cung cấp cho người mua.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Know Your Customer (KYC)                | Các luật nhằm ngăn chặn việc sử dụng các tổ chức tài chính cho việc chuyển tiền bất hợp pháp bằng cách yêu cầu tất cả các tài khoản phải được xác minh danh tính                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Lớp hai - Layer 2                                 | Một mạng lưới được xây dựng trên cơ sở một blockchain, ví dụ, Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Địa chỉ Legacy - Legacy Address                          | Địa chỉ legacy sử dụng Base58, và khi một địa chỉ legacy là mã băm của một khóa công khai, một địa chỉ P2PKH, nó bắt đầu bằng ‘1’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Lightning Network                       | Một giao thức được xây dựng bên trên mạng lưới Bitcoin. Nó tạo ra một mạng lưới các kênh thanh toán cho phép chuyển tiền không cần tin cậy qua mạng lưới đó với sự giúp đỡ của HTLCs và `Định tuyến onion - Onion Routing. Các thành phần khác của Lightning Network bao gồm giao thức gossip, tầng vận chuyển, và yêu cầu thanh toán.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Thanh khoản - Liquidity                               | Đo lường một số đặc điểm của sổ lệnh của một tài sản cụ thể trong một thị trường nhất định. Tính thanh khoản là một chỉ số cho biết ảnh hưởng của một lệnh lớn đến giá của một tài sản sẽ như thế nào. Một tài sản có tính thanh khoản cao sẽ có độ sâu sổ lệnh lớn hơn. Điều này có nghĩa là nó có thể hấp thụ nhiều lệnh hơn với sự biến động giá nhỏ hơn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Chuỗi dài nhất - Longest Chain                          | Lag blockchain (chuỗi) mất nhiều công sức nhất để xây dựng. Được đặt tên như vậy vì theo trực giác, một blockchain có nhiều khối hơn sẽ mất nhiều năng lượng hơn để xây dựng so với một chuỗi có ít khối hơn, nhưng chính xác hơn, đó là chuỗi đòi hỏi nhiều bằng chứng công việc hơn để tạo ra, vì vậy tốt hơn nên gọi là "chuỗi nặng nhất."                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Chuỗi chính - Main Chain                             | Trong bối cảnh của Lightning Network, đây là mạng lưới Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Phương tiện trung gian thanh toán - Medium of Exchange                    | Một loại hàng hóa giúp tạo điều kiện cho việc trao đổi các hàng hóa và dịch vụ khác trong một nền kinh tế. Trong lịch sử, các vật phẩm như vỏ sò, hạt, và vàng đã được sử dụng như một phương tiện trung gian thanh toán.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Mempool                                 | Viết tắt của "memory pool," là nơi lưu trữ tạm thời cho các giao dịch đã được một node nhận ra.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Thợ đào - Miner                                  | Một node tham gia vào quá trình xây dựng blockchain bằng cách thêm các khối mới thông qua quá trình băm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Đào coin                                 | Quá trình xây dựng một khối từ các giao dịch Bitcoin gần đây và sau đó giải quyết một bài toán được yêu cầu như bằng chứng công việc. Đây là quá trình mà qua đó sổ cái Bitcoin chung (tức là, blockchain Bitcoin) được cập nhật và qua đó các giao dịch mới được đưa vào trong sổ cái. Đây cũng là quá trình mà qua đó bitcoin mới được phát hành. Mỗi khi một khối mới được tạo ra, node thợ đào sẽ nhận được bitcoin mới được tạo trong giao dịch coinbase của khối đó.                                                                                                                                                                                                                                                                                                                                        |
| Đa chữ ký (multisig)                    | Một script yêu cầu nhiều hơn một chữ ký để ủy quyền chi tiêu. Các kênh thanh toán luôn được mã hóa dưới dạng địa chỉ đa chữ ký yêu cầu một chữ ký từ mỗi đối tác của kênh thanh toán. Trong trường hợp tiêu chuẩn của một kênh thanh toán hai bên, một địa chỉ đa chữ ký dạng 2-trong-2 được sử dụng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Node                                    | Một máy tính tham gia vào một mạng lưới. Cụ thể là mạng lưới Bitcoin hoặc Lightning.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Đầu ra - Output                                  | Các bitcoin (hoặc mảnh bitcoin) được tạo trong một giao dịch bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Khóa đầu ra - Output Lock                      | Một tập hợp các yêu cầu đặt ra cho một đầu ra. Các yêu cầu này phải được đáp ứng để có thể sử dụng đầu ra đó làm đầu vào cho một giao dịch mới. Ví dụ phổ biến nhất là yêu cầu có khóa riêng tư.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Địa chỉ P2SH                            | Địa chỉ P2SH là mã hóa Base58Check của hash 20-byte của một script. Địa chỉ P2SH bắt đầu bằng "3." Địa chỉ P2SH ẩn tất cả sự phức tạp, sao cho người gửi một khoản thanh toán không thấy script.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Địa chỉ P2WPKH                          | Định dạng địa chỉ "native SegWit v0", địa chỉ P2WPKH được mã hóa bech32 và bắt đầu bằng "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Địa chỉ P2WSH                           | Định dạng địa chỉ script "native Segwit v0", địa chỉ P2WSH được mã hóa bech32 và bắt đầu bằng "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Giao Dịch Bitcoin Đã Ký Một Phần - Partially Signed Bitcoin TransactionPartially Signed Bitcoin Transaction (PSBT) | Một tiêu chuẩn Bitcoin giúp tạo điều kiện cho việc di chuyển giao dịch chưa ký, cho phép nhiều bên dễ dàng ký cùng một giao dịch. Điều này rất hữu ích khi nhiều bên muốn thêm đầu vào cho cùng một giao dịch. PSBT được giới thiệu bởi BIP 174, và cho phép người dùng dễ dàng hơn trong việc ký giao dịch trên một thiết bị lưu trữ lạnh và sau đó phát sóng giao dịch đã ký từ một thiết bị kết nối với internet.                                                                                                                                                                                                                                                                                                                                                                                                      |
| Tìm dường dẫn - Pathfinding              | Quá trình tìm kiếm một lộ trình cho việc thanh toán từ điểm nguồn cho đến điểm đến trong Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Pay-to-Public-Key-Hash (P2PKH)          | P2PKH là một loại đầu ra khóa bitcoin vào hash của một khóa công khai. Một đầu ra được khóa bởi một script P2PKH có thể được mở khóa (chi tiêu) bằng cách trình bày khóa công khai phù hợp với hash và chữ ký số được tạo bởi khóa riêng tư tương ứng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Pay-to-Script-Hash (P2SH)               | P2SH là một loại đầu ra linh hoạt cho phép sử dụng các Bitcoin Scripts phức tạp. Với P2SH, script phức tạp chi tiết hoá các điều kiện để chi tiêu đầu ra (redeem script) không được trình bày trong script khóa. Thay vào đó, giá trị được khóa vào hash của một script, script này phải được trình bày và thỏa mãn để chi tiêu đầu ra.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Pay-to-Taproot (P2TR)                   | Được kích hoạt vào tháng 11 năm 2021, Taproot là một loại đầu ra mới khóa bitcoin vào một cây của các điều kiện chi tiêu, hoặc một điều kiện gốc duy nhất.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Pay-to-Witness-Public-Key-Hash (P2WPKH) | P2WPKH là phiên bản SegWit của P2PKH. Chữ ký để chi tiêu một đầu ra P2WPKH được đặt trong cây witness thay vì trường ScriptSig.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Pay-to-Witness-Script-Hash (P2WSH)      | P2WSH là phiên bản SegWit của P2SH. Chữ ký và script để chi tiêu một đầu ra P2WSH được đặt trong cây witness thay vì trường ScriptSig.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Payjoin                                 | Một loại giao dịch Bitcoin đặc biệt nơi cả người gửi và người nhận đều đóng góp đầu vào để phá vỡ giả định sở hữu đầu vào chung, một giả định được sử dụng để loại bỏ quyền riêng tư của người dùng bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Kênh thanh toán - Paymen Channel                        | Một mối quan hệ tài chính giữa hai nút trên Lightning Network, được tạo ra bằng cách sử dụng một giao dịch bitcoin thanh toán cho một địa chỉ đa chữ ký. Các đối tác kênh có thể sử dụng kênh để gửi bitcoin qua lại cho nhau mà không cần phải ghi lại tất cả các giao dịch lên blockchain Bitcoin. Trong một kênh thanh toán điển hình chỉ có hai giao dịch, giao dịch cấp vốn và giao dịch cam kết, được thêm vào blockchain. Các khoản thanh toán được gửi qua kênh không được ghi lại trong blockchain và được cho là xảy ra "ngoài chuỗi - off-chain."                                                                                                                                                                                                                                                                      |
| Yêu cầu thanh toán - Payment Request                     | Một tính năng cho phép chủ cửa hàng BTCPay tạo hóa đơn lâu dài. Các khoản tiền thanh toán cho một yêu cầu thanh toán sử dụng tỷ giá hối đoái tại thời điểm thanh toán. Điều này cho phép người dùng thực hiện các khoản thanh toán theo sự tiện lợi của họ mà không cần phải thương lượng hoặc xác minh tỷ giá hối đoái với chủ cửa hàng tại thời điểm thanh toán.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Xuất chi - Payout                              | Chức năng thanh toán được liên kết với Pull Payments. Tính năng này cho phép bạn xử lý thanh toán kéo (hoàn tiền, thanh toán lương, hoặc rút tiền).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Plugin                                  | Một phần mềm bổ sung được cài đặt trên một chương trình, tăng cường khả năng của nó.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Điểm bán hàng - Point of Sale (PoS)                     | Một plugin mặc định của BTCPay Server cho phép chủ cửa hàng tạo một cửa hàng trực tuyến trực tiếp từ BTCPay Server. Chủ cửa hàng không cần bất kỳ giải pháp thương mại điện tử bên thứ ba nào để vận hành một cửa hàng trực tuyến.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Di động - Portable                                 | Khả năng của một loại hàng hóa được vận chuyển dễ dàng theo không gian. Tính di động là một đặc điểm quan trọng của một đồng tiền tốt; để một đồng tiền được chấp nhận và sử dụng rộng rãi, nó phải có thể được di chuyển qua biên giới, giữa các cá nhân, và qua những khoảng cách dài một cách tương đối dễ dàng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Bằng chứng công việc - Proof Of Work (PoW)                     | Dữ liệu yêu cầu tính toán đáng kể để tìm ra, và có thể được dễ dàng xác minh bởi bất kỳ ai để chứng minh lượng công việc đã được yêu cầu để tạo nó. Trong Bitcoin, các thợ đào phải tìm ra một giải pháp số cho thuật toán SHA-256 phù hợp với một mục tiêu chung của mạng, gọi là mục tiêu độ khó.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Pseudonym                               | Một tên giả được cá nhân sử dụng để bảo vệ danh tính của họ hoặc xây dựng danh tiếng riêng biệt từ danh tính thực của họ. Khóa công khai được sử dụng để cho phép người dùng Bitcoin nhận bitcoin trong khi vẫn giữ ẩn danh với blockchain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Mã hó khoá công khai - Public-Key Cryptography                 | Bao gồm một cặp khóa được biết đến là khóa công khai và khóa riêng tư, liên quan đến một thực thể cần xác thực danh tính của mình trên môi trường điện tử hoặc để ký hoặc mã hóa dữ liệu. Khóa công khai được công bố và khóa riêng tư tương ứng được giữ bí mật. Dữ liệu được mã hóa bằng khóa công khai chỉ có thể được giải mã bằng khóa riêng tư tương ứng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Khoá công khai / Riêng tư - Public/Private Key                      | Cặp khóa được sử dụng trong mã hóa khóa công khai. Khóa công khai được chia sẻ với người khác một cách công khai, và có thể được coi là một số tài khoản, trong khi khóa riêng tư được giữ bí mật và có thể được coi là một mật khẩu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Thanh toán kéo - Pull Payment                            | Truyền thống, để thực hiện một khoản thanh toán Bitcoin, người nhận chia sẻ địa chỉ bitcoin của họ và sau đó người gửi gửi tiền đến địa chỉ này. Hệ thống như vậy được gọi là thanh toán đẩy vì người gửi khởi xướng việc thanh toán trong khi người nhận có thể không có mặt, đẩy khoản thanh toán cho người nhận. Thay vì kịch bản điển hình của người gửi "đẩy" khoản thanh toán, người gửi cho phép người nhận kéo khoản thanh toán vào thời điểm mà người nhận thấy phù hợp.                                                                                                                                                                                                                                                                                                                                  |
| Hang thỏ không đáy - Rabbit Hole                             | Khái niệm bắt nguồn từ tác phẩm Alice In Wonderland nơi người hùng bắt đầu một cuộc phiêu lưu bằng cách đi vào một hang thỏ. Trong Bitcoin, nó ám chỉ những chủ đề dường như không bao giờ kết thúc mà một người khám phá và thấy khi họ đã bắt đầu hiểu về Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Nhận - Receive                                 | Quá trình nhận bitcoin được gửi đến địa chỉ được cung cấp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Đăng ký - Register                                | Quá trình tạo một tài khoản hoặc đăng ký dịch vụ thường được thực hiện bằng cách chọn một tên người dùng và mật khẩu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Thay thế bằng phí - Replace By Fee (RBF)                    | Một giao dịch Bitcoin có thể được chỉ định là RBF để cho phép người gửi thay thế giao dịch này bằng một giao dịch tương tự khác trả phí cao hơn. Cơ chế này tồn tại để cho phép người dùng phản ứng nếu mạng lưới trở nên tắc nghẽn và phí tăng đột ngột.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Repository                              | Trong các hệ thống kiểm soát phiên bản, một repository là một cấu trúc dữ liệu lưu trữ metadata cho một tập hợp các tệp hoặc cấu trúc thư mục. Tùy thuộc vào việc hệ thống kiểm soát phiên bản đang sử dụng là phân tán, như Git hoặc Mercurial, hay tập trung, như Subversion, CVS, hoặc Perforce, toàn bộ thông tin trong repository có thể được sao chép trên hệ thống của mỗi người dùng hoặc được duy trì trên một máy chủ duy nhất. Một số metadata mà một repository chứa bao gồm, trong số các thứ khác, một bản ghi lịch sử của các thay đổi trong repository, một tập hợp các đối tượng commit, và một tập hợp các tham chiếu đến các đối tượng commit, gọi là heads.                                                                                                                                         |
| Quét lại - Rescan                                  | Quá trình quét lại trạng thái hiện tại của bộ UTXO để tìm kiếm các đồng tiền thuộc về một lược đồ phái sinh đã được cấu hình trước.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Khoá thu hồi - Revokation Key                          | Mỗi Revocalbe Sequence Maturity Contract (RSMC) chứa hai khóa thu hồi. Mỗi đối tác kênh biết một khóa thu hồi. Biết cả hai khóa thu hồi, đầu ra của RSMC có thể được chi tiêu trong khoảng thời gian đã định trước. Trong quá trình thương lượng trạng thái kênh mới, các khóa thu hồi cũ được chia sẻ, từ đó "thu hồi" trạng thái cũ. Khóa thu hồi được sử dụng để ngăn chặn các đối tác kênh phát sóng trạng thái kênh cũ.                                                                                                                                                                                                                                                                                                                                                                               |
| Định tuyến - Routing                                 | Quá trình sử dụng đường dẫn của Lightning Network để thực hiện thanh toán.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Phí định tuyến - Routing Fees                            | Trong Lightning Network, phí được tính cho việc chuyển tiếp thanh toán của người dùng khác. Các node cá nhân có thể thiết lập chính sách phí của riêng mình, được tính là tổng của một mức phí cơ sở (báe-fee)cố định và một mức phí tỷ lên (fee_rate) tùy thuộc vào số tiền thanh toán.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Mức độ dễ bán - Salability                              | Khả năng dễ dàng bán một hàng hóa trên thị trường bất cứ khi nào người nắm giữ mong muốn, với tổn thất ít nhất về giá của nó.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Satoshi (sat)                           | Satoshi là đơn vị nhỏ nhất (đơn vị tiền tệ) của bitcoin có thể được ghi lại trên blockchain. Một satoshi bằng 1/100 triệu (0.00000001) bitcoin và được đặt theo tên của người tạo ra Bitcoin, Satoshi Nakamoto.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Satoshi Nakamoto                        | Tên được sử dụng bởi cá nhân hoặc nhóm người đã thiết kế Bitcoin và tạo ra bản triển khai ban đầu của nó. Là một phần của việc triển khai, họ cũng đã phát minh ra cơ sở dữ liệu blockchain đầu tiên. Trong quá trình đó, họ là người đầu tiên giải quyết vấn đề lặp chi cho tiền tệ số. Danh tính thực sự của họ vẫn còn là một bí ẩn.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Satoshi Per Byte (Sat/B)                      | Đơn vị đo độ ưu tiên của giao dịch, được xác định bởi phí giao dịch bằng satoshi chia cho kích thước của giao dịch bằng byte.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Satoshi Per Virtual Byte (Sat/vB)                   | Khái niệm tương tự như Satoshi Per Byte, nhưng dành cho địa chỉ mới sử dụng Segwit. Bằng với kích thước giao dịch tính bằng đơn vị weight chia cho 4. Đơn vị weight được tính bằng cách lấy kích thước giao dịch (không bao gồm phần witness) nhân với 3, cộng với kích thước giao dịch bao gồm witness.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Độ khan hiểm Scarcity                                | Tính chất của một hàng hóa không thể dễ dàng bị sao chép, nhân bản mà không tốn kém. Sự khan hiếm không phụ thuộc vào số lượng đơn vị hiện có của một hàng hóa, mà phụ thuộc vào chi phí để sản xuất thêm đơn vị mới.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Script                                  | Bitcoin sử dụng một hệ thống kịch bản cho giao dịch gọi là Bitcoin Script. Giống như ngôn ngữ lập trình Forth, nó đơn giản, dựa trên stack và được xử lý từ trái sang phải. Nó cố ý không phải là Turing complete, không có vòng lặp hay đệ quy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Cụm từ hạt giống - Seed Phrase                             | Một danh sách các từ lưu trữ tất cả thông tin cần thiết để khôi phục quỹ Bitcoin trên trên blockchain. Phần mềm ví thường tạo ra một cụm từ hạt giống và hướng dẫn người dùng viết nó ra giấy. Nếu máy tính của người dùng hỏng hoặc ổ cứng bị hỏng, họ có thể tải lại phần mềm ví tương tự và sử dụng bản sao lưu này để lấy lại bitcoin của mình.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Segregated Witness (SegWit)             | Segregated Witness (SegWit) là một nâng cấp của giao thức Bitcoin được giới thiệu vào năm 2017, bổ sung một trường chứng nhận mới cho chữ ký và các bằng chứng ủy quyền giao dịch khác. Trường chứng nhận mới này được miễn không đưa vào để tính toán ID giao dịch, giải quyết hầu hết các loại biến đổi giao dịch bởi bên thứ ba. Segregated Witness được triển khai dưới dạng một soft fork và là một thay đổi kỹ thuật làm cho quy tắc giao thức của Bitcoin trở nên hạn chế hơn.                                                                                                                                                                                                                                                                                                                                            |
| Chủ quyền tự thân - Self-Sovereignty                        | Một mô hình quản lý danh tính số mà trong đó cá nhân hoặc doanh nghiệp có quyền sở hữu độc lập đối với khả năng kiểm soát tài khoản và dữ liệu cá nhân của họ.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Gửi - Send                                    | Quá trình chuyển bitcoin đến một địa chỉ.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Trạng thái nhạy cảm - Sensitivity Mode                        | Được kích hoạt qua một nút chuyển đổi trong cài đặt cửa hàng, kích hoạt làm cho các giá trị số (ví dụ, số lượng bitcoin) bị ẩn đi trong tất cả các giao diện.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Cài đặt máy chủ - Server Settings                         | Cài đặt trong BTCPay Server áp dụng cho toàn bộ máy chủ (khác với Store Settings chỉ áp dụng cho một cửa hàng duy nhất).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SHA-256                                 | Một hàm băm mật mã. Là một thành viên của gia đình hàm băm Secure Hashing Algorithm (SHA).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Shopify                                 | Một công ty đa quốc gia về thương mại điện tử có trụ sở tại Ottawa, Ontario, Canada. Shopify là tên của nền tảng thương mại điện tử độc quyền của họ cho các cửa hàng trực tuyến và hệ thống bán lẻ tại điểm bán hàng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| SMTP                                    | Simple Mail Transfer Protocol là một giao thức truyền thông tiêu chuẩn của Internet dành cho việc truyền tải thư điện tử.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Phan tách mềm - Soft Fork                               | Một nâng cấp giao thức tương thích với phiên bản cũ, cho phép cả node cũ và node mới tiếp tục sử dụng cùng một blockchain chung.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Software Stack                          | Trong lĩnh vực máy tính, một solution stack hoặc software stack là một tập hợp các hệ thống phụ trợ hoặc thành phần phần mềm cần thiết để tạo ra một nền tảng hoàn chỉnh sao cho không cần thêm phần mềm nào khác để hỗ trợ các ứng dụng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Cửa hàng - Store                                   | Một cửa hàng trong BTCPay Server có thể được coi là "Nhà" của một ví bitcoin cụ thể, mở rộng với tất cả các tính năng của BTCPay Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Cài đặt cửa hàng - Store Settings                          | Cài đặt trong BTCPay Server dành riêng cho một cửa hàng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Taproot                                 | Nâng cấp cho Bitcoin sẽ giới thiệu một số tính năng mới. Nâng cấp được mô tả trong các BIPs 340, 341, và 342, và giới thiệu lược đồ chữ ký Schnorr, Taproot, và Tapscript. Cùng nhau, những nâng cấp này giới thiệu các cách mới, hiệu quả hơn, linh hoạt hơn, và riêng tư hơn trong việc chuyển giao bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Định luật Thier - Thier's Law                             | Luật nói rằng tiền tốt sẽ đẩy tiền xấu đến chỗ biến mất                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Dịch vụ host của bên thứ ba - Third-Party Host                        | Khi một trang web của cá nhân hoặc công ty được vận hành trên máy chủ thuộc sở hữu và quản lý của một doanh nghiệp khác. Lựa chọn khác là tự bạn lưu trữ trang web trên máy chủ của mình trong trung tâm dữ liệu của mình.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Khoá thời gian - Timelock                                | Một loại ràng buộc ngăn cản việc chi tiêu một số bitcoin cho đến một thời điểm hoặc độ cao khối cụ thể trong tương lai. Timelock đóng vai trò quan trọng trong nhiều hợp đồng Bitcoin, bao gồm các kênh thanh toán và HTLCs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Topology                                | Topology của Lightning Network mô tả hình dạng của Lightning Network như một đồ thị toán học. Các nút của đồ thị là các Lightning Node (người tham gia/máy chủ ngang hàng trong mạng). Các cạnh của đồ thị là các kênh thanh toán. Topology của Lightning Network được công bố công khai nhờ vào giao thức gossip, ngoại trừ các kênh không được công bố. Điều này có nghĩa là Lightning Network có thể lớn hơn nhiều so với số lượng kênh và nút được công bố. Việc biết topology đặc biệt quan trọng trong quá trình định tuyến dựa trên nguồn của các giao dịch thanh toán, trong đó người gửi tìm ra một lộ trình.                                                                                                                                                                                                   |
| Giao dịch - Transaction                             | Giao dịch là các cấu trúc dữ liệu được Bitcoin sử dụng để chuyển bitcoin từ một địa chỉ này sang địa chỉ khác. Hàng ngàn giao dịch được tổng hợp vào trong một khối, sau đó được ghi (đào) lên blockchain. Giao dịch đầu tiên trong mỗi khối, gọi là giao dịch coinbase, tạo ra bitcoin mới.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ID của giao dịch - Transaction ID                          | Một chuỗi các chữ cái và số xác định một giao dịch cụ thể trên blockchain. Chuỗi này đơn giản là một mã băm SHA-256 kép của một giao dịch. Băm này có thể được sử dụng để tra cứu một giao dịch trên một node hoặc trình duyệt blockchain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Xác thực hai yếu tố - Two Factor Authentication (2FA)         | Phương pháp bảo mật quản lý danh tính và truy cập yêu cầu hai hình thức xác thực để truy cập vào tài nguyên và dữ liệu, thường kèm theo một thiết bị phụ bên cạnh mật khẩu đăng nhập tiêu chuẩn.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Không thể kiểm duyệt - Uncensorable                            | Tính chất mà không có thực thể nào có khả năng đảo ngược một giao dịch Bitcoin hoặc đưa một ví hoặc địa chỉ vào danh sách đen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Không thể tịch thu - Unconfiscatable                         | Tính chất mà không có thực thể nào có thể lấy bitcoin từ một thực thể khác mà không có sự đồng ý của họ.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Đầu ra chưa chi tiêu - Unspent Transaction Outputs (UTXO)      | Các đầu ra chưa được tiêu, do đó có sẵn để được sử dụng làm đầu vào trong các giao dịch mới.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Trải nghiệm người dùng - User Experience (UX)                    | Cách một người dùng tương tác và trải nghiệm một sản phẩm, hệ thống hoặc dịch vụ. Nó bao gồm nhận thức của một người về tính hữu ích, dễ sử dụng và hiệu quả.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Giao diện người dùng - User Interface (UI)                     | Điểm của tương tác và giao tiếp giữa con người và máy tính trong một thiết bị.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Dễ xác thực - Vefiable                              | Tính chất của một hàng hóa có thể dễ dàng phân biệt với hàng giả mạo và hàng nhái.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Ảo - Virtual                                 | Tồn tại trên hoặc được mô phỏng trên máy tính hoặc mạng máy tính.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Máy ảo - Virtual Machine (VM)                    | Trong lĩnh vực máy tính, máy ảo là sự ảo hóa hoặc mô phỏng của một hệ thống máy tính. Máy ảo dựa trên kiến trúc máy tính và cung cấp chức năng của một máy tính vật lý. Các triển khai của chúng có thể liên quan đến phần cứng chuyên dụng, phần mềm, hoặc sự kết hợp của cả hai.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Máy chủ ảo riêng - Virtual Private Server                  | Một máy chủ ảo riêng là một máy ảo được bán dưới dạng dịch vụ bởi một dịch vụ lưu trữ Internet. Thuật ngữ "máy chủ ảo dành riêng" cũng có ý nghĩa tương tự. Một máy chủ ảo riêng chạy bản sao của hệ điều hành riêng, và khách hàng có thể có quyền truy cập cấp độ superuser đối với hệ điều hành đó, vì vậy họ có thể cài đặt gần như bất kỳ phần mềm nào chạy trên hệ điều hành đó.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Biến động - Volatility                              | Đo lường mức độ biến động của giá tài sản theo thời gian. Các tài sản trải qua những thay đổi lớn về giá một cách thường xuyên có tính biến động cao, trong khi các tài sản có giá ổn định hơn có tính biến động thấp.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Ví - Wallet                                     | Ví Bitcoin giữ chìa khóa của người dùng, cho phép người dùng nhận bitcoin, ký giao dịch và kiểm tra số dư tài khoản của họ. Chìa khóa riêng tư và chìa khóa công khai được giữ trong ví Bitcoin đảm nhận hai chức năng riêng biệt nhưng được liên kết với nhau khi tạo ra. Ví Bitcoin chứa chìa khóa của người dùng, không phải bitcoin thực sự của họ. Về mặt khái niệm, ví giống như một móc khóa trong ý nghĩa nó giữ nhiều cặp chìa khóa riêng tư và công khai. Những chìa khóa này được sử dụng để ký giao dịch, cho phép người dùng chứng minh họ sở hữu các đầu ra giao dịch trên blockchain, tức là bitcoin của họ. Tất cả bitcoin được ghi lại trên blockchain dưới dạng đầu ra giao dịch.                                                                                                                           |
| Wasabi Wallet                           | Một ví Bitcoin tập trung vào quyền riêng tư, mã nguồn mở, không giữ hộ trên Desktop thực hiện trộn coin không cần tin cậy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Ví chỉ dùng để xem - Watch-only Wallet                              | Ví Bitcoin cho phép bạn theo dõi bitcoin của mình trong lưu trữ lạnh mà vẫn vô hiệu hóa khả năng chi tiêu quỹ. Điều này là bởi vì ví chỉ xem không lưu trữ hoặc sử dụng chìa khóa riêng tư và do đó không thể ủy quyền bất kỳ khoản chi tiêu nào thay mặt cho người dùng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Whale (Cá Voi)                          | Trong bối cảnh của Bitcoin, một cá voi là người nắm giữ một lượng lớn bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Nhãn trắng - White-Label                             | Một sản phẩm hoặc dịch vụ nhãn trắng là sản phẩm hoặc dịch vụ được sản xuất bởi một công ty mà các công ty khác tái thương hiệu để làm cho nó trông như thể họ đã tạo ra nó.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Bản cáo bạch - Whitepaper                              | Giới thiệu một ý tưởng mới hoặc chủ đề để thảo luận. Bản cáo bạch Bitcoin giới thiệu Bitcoin như một “Hệ thống tiền mặt điện tử ngang hàng” mà “không cần bên thứ ba đáng tin cậy”. Satoshi Nakamoto phát hành bản cáo bạch vào ngày 31 tháng 10 năm 2008 cho một danh sách email của các nhà mật mã học và cypherpunks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Wrapped Segwit                          | Một triển khai thiết kế được bao gồm trong nâng cấp SegWit nhằm mục đích giúp ví và phần mềm Bitcoin khác dễ dàng hỗ trợ SegWit hơn. Để đạt được điều này, hai kịch bản SegWit gốc, P2WPKH và P2WSH, được sử dụng như là “redeemScript” của một giao dịch P2SH, tạo ra các loại kịch bản SegWit được bọc là P2SH-P2WPKH và P2SH-P2WSH tương ứng.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

![image](assets/en/129.webp)
