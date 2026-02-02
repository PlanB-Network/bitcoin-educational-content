---
name: Những điều cần thiết trong khóa huấn luyện Liquid
goal: Nắm vững kiến thức toàn diện về dự án Liquid Network và Elements, đồng thời học cách triển khai các giải pháp tiên tiến trong giao dịch bảo mật, mã hóa token và kiến trúc mạng phi tập trung.
objectives: 

  - Nắm vững các nguyên tắc cơ bản của kiến trúc Liquid và mối quan hệ của nó với Bitcoin.
  - Tìm hiểu cách cấu hình và vận hành các nút Liquid bằng phần mềm Elements.
  - Khám phá việc sử dụng các giao dịch bí mật và phát hành tài sản trên Liquid Network.
  - Nắm vững các khía cạnh kinh doanh và kỹ thuật của Liquid để ứng dụng trong thị trường vốn.

---

# Giới thiệu về mạng Liquid


Hãy bắt đầu hành trình học tập được thiết kế để cung cấp cho bạn sự hiểu biết sâu sắc về dự án Liquid Network và Elements. Khóa học chuyên sâu này kết hợp lý thuyết và thực hành để dạy bạn những kiến thức cơ bản về kỹ thuật, kiến trúc và kinh doanh cần thiết để triển khai và tận dụng các khả năng của Liquid. Từ các giao dịch bảo mật đến thiết kế hệ sinh thái, khóa học này lý tưởng cho những người muốn mở rộng kiến thức về các công cụ tiên tiến trong hệ sinh thái Bitcoin.


Với các bài thuyết trình của các chuyên gia trong ngành, khóa học bao gồm các chủ đề như kiến trúc Liquid, các ứng dụng mã hóa token, các khái niệm kỹ thuật của Elements và các trường hợp sử dụng sáng tạo như SDK Breez. Được thiết kế để phù hợp với người mới bắt đầu và người dùng trung cấp, khóa học cũng mang lại giá trị cho các nhà phát triển giàu kinh nghiệm muốn nắm vững Liquid như một nền tảng để tối ưu hóa các dự án của họ.

+++

# Giới thiệu


<partId>9f8a83d5-27e0-4e6d-af12-6cd6eb667291</partId>


## Tổng quan khóa học


<chapterId>3192ee7d-255b-4c4f-ba18-e08c5ab98577</chapterId>


Chào mừng đến với Khóa huấn luyện Liquid, một chương trình đào tạo toàn diện được thiết kế để trang bị cho bạn kiến thức và kỹ năng cần thiết để tận dụng hiệu quả dự án Liquid Network và Elements. Khóa học này cung cấp một cái nhìn toàn diện về các tính năng đặc biệt của Liquid, bao gồm Confidential Transactions, phát hành tài sản và kiến trúc mạng liên kết của nó, đồng thời giới thiệu các khái niệm nền tảng của Elements, phần mềm cung cấp năng lượng cho Liquid.


Trong suốt khóa huấn luyện, bạn sẽ khám phá các ứng dụng thực tiễn của Liquid Network, từ việc thiết lập và vận hành các node đến việc hiểu rõ cách sử dụng nó trong thị trường vốn và mã hóa token của Bitcoin. Với các bài thuyết trình từ các chuyên gia trong ngành, bạn cũng sẽ có được những hiểu biết sâu sắc về các chủ đề nâng cao như HTLC, SDK của Breez và dự án Blockstream AMP.


Khóa học này ban đầu được tổ chức trực tiếp, theo một lịch trình có cấu trúc (như trong hình) được thiết kế cho các buổi học trực tuyến. Tuy nhiên, đối với phiên bản điều chỉnh này, nội dung đã được sắp xếp lại để phù hợp hơn với hình thức trực tuyến và giúp học viên dễ hiểu hơn. Trình tự mới đảm bảo sự tiến triển logic từ các khái niệm cơ bản đến các chủ đề nâng cao và kỹ thuật hơn, từ đó tối đa hóa trải nghiệm học tập.


Chương trình này được thiết kế để phù hợp với người tham gia có trình độ chuyên môn khác nhau, kết hợp giữa kiến thức lý thuyết và kinh nghiệm thực hành. Sau khi hoàn thành khóa học, bạn sẽ nắm vững kiến trúc của Liquid, sự tích hợp với Bitcoin, và cách sử dụng các tính năng tiên tiến của nó để xây dựng và tối ưu hóa các giải pháp tài chính.


Khám phá thế giới của sidechain Liquid và khai phá toàn bộ tiềm năng của nó ngay bây giờ!

# Nguyên tắc cơ bản


<partId>6dd86449-c0f7-4e51-9252-5f135cf019df</partId>


## Kiến trúc Liquid


<chapterId>4bca9c70-d54d-4e9a-b2db-17c3a6fa655b</chapterId>


:::video id=ff6899d2-b47f-4c3d-983d-3bd66d2be59d:::

### Mô hình Kiến trúc và Đồng thuận Liquid Network


Liquid Network là một sidechain liên kết được xây dựng trên nền tảng mã nguồn của Elements, được thiết kế để mở rộng khả năng của Bitcoin trong khi vẫn dựa vào tính bảo mật cơ bản của nó. Không giống như Proof-of-Work của Bitcoin, Liquid hoạt động trên mô hình Đồng thuận Liên kết. Mạng lưới được duy trì bởi một nhóm thành viên phân tán toàn cầu, bao gồm các sàn giao dịch, bộ phận giao dịch và nhà cung cấp cơ sở hạ tầng. Từ các thành viên này, mười lăm "chức năng viên" được chọn để đóng vai trò là người ký khối.


Các chức năng viên này tạo ra các khối theo phương thức luân phiên xác định, với một khối mới được tạo ra mỗi phút. Thời gian chính xác này trái ngược với khoảng thời gian mười phút mang tính xác suất của Bitcoin. Để một khối hợp lệ, nó cần chữ ký của ít nhất 11 trong số 15 chức năng viên (ngưỡng hai phần ba cộng một). Cơ chế này cung cấp cho Liquid "tính xác thực hai khối", có nghĩa là một khi giao dịch đã có hai xác nhận (khoảng hai phút), về mặt toán học, không thể sắp xếp lại chuỗi. Tốc độ và sự chắc chắn này rất quan trọng đối với hoạt động chênh lệch giá, giao dịch tự động và thanh toán liên sàn nhanh chóng.


Liên đoàn này rất năng động. Thông qua giao thức Liên đoàn Năng động (Dynafed), mạng lưới có thể luân chuyển các chức năng viên hoặc cập nhật các tham số mà không cần đến thiết bị fork cố định. Điều này cho phép hệ thống phát triển và thay thế phần cứng hoặc thành viên một cách liền mạch trong khi vẫn duy trì hoạt động liên tục.


### Confidential Transactions và Quản lý Tài sản


Một đặc điểm nổi bật của Liquid là khả năng hỗ trợ gốc cho Confidential Transactions (CT) và nhiều loại tài sản. Trên chuỗi Bitcoin chính, tất cả chi tiết giao dịch—người gửi, người nhận và số tiền—đều được công khai. Trong Liquid, CT sử dụng các cam kết mật mã để che giấu loại tài sản và số tiền khỏi sổ cái công khai, đồng thời vẫn cho phép mạng lưới xác minh tính hợp lệ của giao dịch (tức là không xảy ra lạm phát). Chỉ những người tham gia nắm giữ khóa che giấu mới có thể xem được các giá trị cụ thể, mang lại mức độ bảo mật thương mại cần thiết cho các tổ chức giao dịch số lượng lớn.


Liquid coi tất cả các tài sản là "công dân bản địa" của blockchain. Điều này bao gồm Liquid, Bitcoin (LBTC), các stablecoin như USDT và các token bảo mật. Việc phát hành tài sản không yêu cầu các hợp đồng thông minh phức tạp; đó là một chức năng cơ bản của giao thức.


#### Tài sản được quản lý và AMP

Đối với các tài sản yêu cầu tuân thủ quy định, chẳng hạn như token bảo mật, Liquid sử dụng Nền tảng Quản lý Tài sản Blockstream (AMP). Nền tảng này giới thiệu một lớp được cấp phép, trong đó các giao dịch yêu cầu chữ ký thứ hai từ máy chủ ủy quyền. Điều này cho phép các nhà phát hành thực thi các quy tắc—chẳng hạn như Danh sách trắng hoặc các yêu cầu KYC—ở mức độ chi tiết, kết hợp hiệu quả của blockchain với các biện pháp kiểm soát quy định của tài chính truyền thống.


### Cơ sở hạ tầng chốt hai chiều và bảo mật


Mối liên hệ giữa Liquid và Bitcoin được duy trì thông qua cơ chế neo hai chiều. Để "neo vào", người dùng gửi Bitcoin đến một địa chỉ được tạo trên mainchain. Số tiền này sẽ bị khóa trong 102 lần xác nhận (khoảng 17 giờ) để loại bỏ rủi ro tái cấu trúc. Sau khi được xác nhận, một lượng LBTC tương đương sẽ được tạo trên chuỗi phụ Liquid.


Quá trình "đẩy giá" cho phép người dùng quy đổi LBTC lấy Bitcoin. Điều này yêu cầu việc đốt LBTC và sự ủy quyền mã hóa từ liên đoàn. Để ngăn chặn hành vi trộm cắp, việc đẩy giá được kiểm soát chặt chẽ bằng Khóa Ủy quyền Đẩy giá (PAK) do các thành viên liên đoàn nắm giữ. Ngoài ra, tiền có thể được hoán đổi ngay lập tức thông qua các nhà cung cấp bên thứ ba như SideSwap, bỏ qua độ trễ thanh toán để có tính thanh khoản nhanh hơn.


#### Mô-đun bảo mật phần cứng (HSM)

Bảo mật được thực thi nghiêm ngặt thông qua phần cứng. Các nhân viên không lưu trữ khóa riêng trên các máy chủ tiêu chuẩn; thay vào đó, họ vận hành các Mô-đun Bảo mật Phần cứng (HSM). Các thiết bị này được cách ly hoàn toàn khỏi logic của máy chủ chủ và được lập trình với các quy tắc nghiêm ngặt. Ví dụ, một HSM sẽ từ chối ký một khối nếu chiều cao của nó không lớn hơn khối trước đó, ngăn chặn việc ghi đè lịch sử. Mô hình bảo mật "đối kháng" này giả định rằng máy chủ chủ có thể bị xâm phạm, đảm bảo các khóa vẫn được bảo mật ngay cả khi vị trí vật lý bị xâm nhập.


## Những nguyên lý cơ bản của Elements


<chapterId>1e9cfbed-108e-4067-afb9-4cf950cb43d3</chapterId>


:::video id=5652dcb2-4303-484c-8be5-d98063b39c1c:::

### Elements: Nền tảng của Liquid


Elements là một nền tảng blockchain mã nguồn mở, được phát triển từ mã nguồn cốt lõi của Bitcoin. Nó mở rộng chức năng của Bitcoin bằng cách cho phép các sidechain – các blockchain độc lập có thể chuyển tài sản đến và từ Bitcoin. Trong khi Bitcoin Core cung cấp năng lượng cho mạng Bitcoin, Elements là công cụ phần mềm đằng sau Liquid Network và các sidechain tùy chỉnh khác.


Mối quan hệ rất đơn giản: Liquid là một "phiên bản" cụ thể của chuỗi phụ Elements, được cấu hình để sử dụng trong môi trường sản xuất với mô hình đồng thuận liên kết. Các nhà phát triển quen thuộc với Bitcoin sẽ thấy Elements trực quan, vì nó giữ nguyên giao diện RPC (Remote Procedure Call) và cấu trúc dòng lệnh (`elements-cli`, `elements-d`, `elements-qt`). Sự khác biệt chính nằm ở cấu hình: thiết lập `chain=liquidv1` kết nối một nút với mạng Liquid chính, trong khi `chain=elementsregtest` khởi tạo một môi trường kiểm thử hồi quy cục bộ, nơi các nhà phát triển có thể tạo khối generate ngay lập tức và kiểm thử mà không cần phụ thuộc vào các yếu tố bên ngoài.


#### Phát hành tài sản

Một tính năng nổi bật của Elements là khả năng phát hành tài sản trực tiếp. Không giống như Ethereum, nơi các token là các hợp đồng thông minh phức tạp, tài sản trong Elements là các đối tượng hạng nhất được tạo ra thông qua một lệnh RPC đơn giản (`issueasset`).


- Mã định danh duy nhất:** Mỗi tài sản sẽ có một mã định danh thập lục phân duy nhất gồm 64 ký tự.
- Token phát hành lại:** Các nhà phát hành có thể tùy chọn tạo token phát hành lại, cho phép người nắm giữ có quyền phát hành thêm tài sản này sau đó (hữu ích cho stablecoin hoặc token bảo mật).
- **Hệ thống đăng ký tài sản:** Vì mã định danh thập lục phân không thể đọc được bằng mắt thường, nên Hệ thống đăng ký tài sản của Blockstream ánh xạ các mã định danh này thành tên và mã giao dịch (ví dụ: "USDT"), tương tự như DNS dành cho tài sản.


### Bảo mật thông qua Confidential Transactions


Elements giải quyết một trong những hạn chế chính của các blockchain công khai: thiếu tính riêng tư thương mại. Trên Bitcoin, mọi số tiền giao dịch đều hiển thị công khai. Elements giới thiệu **Confidential Transactions (CT)**, công nghệ mã hóa làm mờ số tiền và loại tài sản trong khi vẫn cho phép mạng lưới xác minh tính hợp lệ của giao dịch.


Điều này được thực hiện bằng cách sử dụng **Cam kết Pedersen** và **Bằng chứng phạm vi**.


- Cam kết Pedersen** thay thế số tiền hiển thị bằng một cam kết mật mã. Nhờ mã hóa đồng hình, các trình xác thực có thể kiểm tra rằng *Cam kết đầu vào = Cam kết đầu ra + Phí* mà không cần nhìn thấy các giá trị thực tế.
- Bằng chứng phạm vi** ngăn người dùng tạo ra tiền từ hư không (ví dụ: bằng cách sử dụng số âm) bằng cách chứng minh về mặt toán học rằng giá trị ẩn là một số nguyên dương nằm trong một phạm vi hợp lệ.


Đối với người ngoài quan sát, một Giao dịch Bảo mật hiển thị các dữ liệu đầu vào và đầu ra hợp lệ nhưng che giấu *nội dung* được gửi đi và *số lượng*. Chỉ người gửi và người nhận (người sở hữu khóa che giấu) mới có thể xem dữ liệu dạng văn bản rõ ràng.


### Quy trình phát triển và RPC


Việc tương tác với một nút Elements chủ yếu được thực hiện thông qua giao diện JSON-RPC của nó. Điều này cho phép các ứng dụng được viết bằng Python, JavaScript hoặc Go giao tiếp với chuỗi khối.



- Thiết lập:** Thông thường, nhà phát triển bắt đầu ở chế độ `regtest`. Điều này cho phép tạo khối tức thì (`generateblock`) để xác nhận giao dịch ngay lập tức, bỏ qua thời gian tạo khối 1 phút của mạng thực tế.
- Các lệnh:** Các lệnh Bitcoin tiêu chuẩn như `getblockchaininfo` đều có sẵn, cùng với các lệnh dành riêng cho Elements như `dumpblindingkey` (để kiểm toán CT) hoặc `pegin` (để chuyển BTC vào sidechain).
- Bí danh:** Để quản lý nhiều nút (ví dụ: "người gửi" và "người nhận" để thử nghiệm), các nhà phát triển thường sử dụng các bí danh shell như `e1-cli` và `e2-cli` trỏ đến các thư mục dữ liệu khác nhau, mô phỏng mạng ngang hàng trên một máy duy nhất.


Kiến trúc này cho phép các nhà phát triển xây dựng các ứng dụng tài chính phức tạp—chẳng hạn như nền tảng chứng khoán hoặc cổng thanh toán riêng tư—sử dụng các công cụ mạnh mẽ và quen thuộc của hệ sinh thái Bitcoin.


## Kết nối các lớp Bitcoin


<chapterId>3ff2df4a-8995-4d5e-9b8a-cd114880e666</chapterId>


:::video id=31368c02-b979-44d7-b217-ceed96c7ca5c:::

### Cơ sở hạ tầng Cross-Layer và HTLCs


Hệ sinh thái Bitcoin đã phát triển thành một kiến trúc đa tầng, với Mainchain cung cấp chức năng thanh toán, Lightning cung cấp tốc độ và Liquid cho phép các khả năng quản lý tài sản tiên tiến. Việc chuyển giá trị giữa các tầng này mà không cần trung gian tập trung đòi hỏi một thuật toán mã hóa phi tập trung: Hash Time Locked Contract (HTLC).


Thiết bị HTLC tạo ra một kênh thanh toán có điều kiện liên kết các hệ thống độc lập một cách nguyên tử. Nó hoạt động thông qua hai ràng buộc chính: **khóa băm** và **khóa thời gian**.


- Khóa Hash:** Tiền có thể được chi tiêu ngay lập tức nếu người nhận tiết lộ một "ảnh gốc" bí mật khớp với một hàm băm mật mã cụ thể.
- Cơ chế khóa thời gian: Nếu người nhận không tiết lộ bí mật trong một khoảng thời gian nhất định (chiều cao khối), người gửi ban đầu có thể thu hồi lại tiền.


Cấu trúc đường dẫn kép này đảm bảo an toàn. Trong giao dịch hoán đổi đa lớp, cùng một khóa băm được sử dụng trên cả hai mạng. Khi người nhận tiết lộ bí mật để nhận tiền trên một lớp (ví dụ: Liquid), bí mật đó sẽ hiển thị cho người gửi, người này sau đó có thể sử dụng nó để nhận tiền tương ứng trên lớp khác (ví dụ: Lightning). Liên kết mật mã này đảm bảo rằng giao dịch hoán đổi hoặc hoàn tất thành công cho cả hai bên hoặc thất bại cho cả hai bên, loại bỏ rủi ro một bên mất tiền trong khi bên kia nhận được tiền.


### Nâng cấp Taproot và MuSig2


Các giao thức HTLC thế hệ cũ (SegWit v0) hoạt động tốt nhưng gặp phải những hạn chế về quyền riêng tư và hiệu quả. Chúng yêu cầu công bố toàn bộ logic kịch bản (on-chain), khiến các giao dịch hoán đổi dễ dàng bị các nhà phân tích blockchain nhận diện và tốn kém hơn do kích thước dữ liệu lớn. Sự ra đời của Taproot (SegWit v1) và giao thức MuSig2 đã cách mạng hóa kiến trúc này.


Taproot cho phép **Gộp khóa** thông qua MuSig2. Thay vì tiết lộ một kịch bản phức tạp với nhiều khóa công khai, MuSig2 cho phép những người tham gia trao đổi kết hợp các khóa của họ thành một khóa công khai tổng hợp duy nhất.


- **Phương thức hợp tác "Đường dẫn chính":** Nếu cả hai bên đồng ý với việc trao đổi (phương thức "thuận lợi"), họ sẽ cùng ký vào giao dịch. Đối với mạng lưới, điều này trông giống hệt như một khoản thanh toán tiêu chuẩn, chỉ cần một chữ ký. Nó tiêu tốn không gian khối tối thiểu và hoàn toàn không tiết lộ bất kỳ thông tin nào về các điều kiện trao đổi.
- **Đường dẫn kịch bản đối kháng":** Nếu một bên không phản hồi hoặc có hành vi xấu, kịch bản cơ bản (chứa khóa băm/thời gian) mới được tiết lộ. Kịch bản này được tổ chức theo dạng cây Merkle, cho phép bên trung thực chỉ tiết lộ nhánh cụ thể cần thiết để thu hồi tiền, giữ cho phần còn lại của logic hợp đồng được ẩn giấu.


### Ứng dụng thực tiễn: Liquid-Lightning Swaps


Trên thực tế, các giao thức này cho phép trao đổi liền mạch giữa các lớp của Bitcoin. Một giao dịch hoán đổi Liquid sang Lightning điển hình bắt đầu bằng việc khách hàng yêu cầu hoán đổi từ nhà cung cấp dịch vụ. Khách hàng cung cấp hóa đơn Lightning, và nhà cung cấp khóa số Liquid Bitcoin (L-BTC) tương đương vào một địa chỉ Taproot hỗ trợ Taproot.


Tính nguyên tử được đảm bảo khi giao dịch thanh toán hoàn tất. Để nhận được L-BTC, nhà cung cấp dịch vụ phải có ảnh gốc. Họ chỉ nhận được ảnh gốc này khi thanh toán thành công hóa đơn Lightning của khách hàng. Ngay khi giao dịch Lightning hoàn tất, ảnh gốc sẽ được tiết lộ, cho phép nhà cung cấp mở khóa số tiền Liquid.


#### Tóm tắt Wallet và Quản lý UTXO

Đối với người dùng cuối, sự phức tạp này hoàn toàn được trừu tượng hóa. Các ví hiện đại như Aqua xử lý việc tạo khóa, tạo hóa đơn và ký kết trong nền. Người dùng chỉ cần "thanh toán" hóa đơn Lightning bằng số dư Liquid của họ. Về phía sau, dịch vụ quản lý việc hợp nhất UTXO, định kỳ thu gom các khoản đầu ra nhỏ, chưa được nhận hoặc được hoàn lại để duy trì hiệu quả của wallet và giảm thiểu tác động đến phí trong thời gian lưu lượng truy cập cao điểm.


## Tổng quan về Liquid Network


<chapterId>1968db03-2364-46c0-9670-9e9844289ca1</chapterId>


:::video id=0bac0a62-90f2-41da-ac7c-330c0604bc61:::

### Kiến trúc và sự đồng thuận của Liquid Network


Liquid Network hoạt động như một chuỗi phụ liên kết được xây dựng trên nền tảng mã nguồn **Elements**. Trong khi Elements—một fork của Bitcoin Core—cung cấp nền tảng phần mềm, Liquid là triển khai mạng lưới sản xuất. Không giống như Proof-of-Work của Bitcoin, dựa trên mining cạnh tranh, Liquid sử dụng mô hình **Đồng thuận Liên kết**.


Mạng lưới này được duy trì bởi mười lăm "nhân viên" phân bố toàn cầu. Các thực thể này vận hành các máy chủ chuyên dụng thực hiện hai vai trò quan trọng:

1. **Sản xuất khối:** Các nhân viên thay phiên nhau tạo khối theo lịch trình luân phiên có định sẵn, tạo ra một khối mới chính xác mỗi phút.

2. **Ký tập thể:** Để một khối ký kết có hiệu lực, phải có ít nhất 11 trong số 15 thành viên ký tên.


Ngưỡng 11/15 này đảm bảo mạng có thể chịu được sự cố của tối đa bốn nút mà không bị dừng lại. Ưu điểm chính của sự đánh đổi này là **tính chắc chắn cuối cùng**. Trong khi Bitcoin xử lý dựa trên xác suất, Liquid đạt được sự chắc chắn về thanh toán sau hai khối (khoảng hai phút). Khi một khối đã có một xác nhận duy nhất ở trên cùng, chuỗi không thể được tổ chức lại, làm cho nó rất hiệu quả cho việc giao dịch chênh lệch giá và thanh toán nhanh chóng.


### Confidential Transactions và Tài sản Bản địa


Tính năng nổi bật của Liquid là việc sử dụng mặc định **Confidential Transactions (CT)**. Trên Bitcoin và mainchain, người gửi, người nhận và số tiền đều được công khai. Liquid cải thiện điều này bằng cách mã hóa số tiền và loại tài sản, trong khi vẫn giữ nguyên địa chỉ người gửi và người nhận để xác minh.


Để đảm bảo người dùng không thể in tiền (ví dụ: bằng cách gửi số tiền âm), Liquid sử dụng **Cam kết Pedersen** và **Bằng chứng phạm vi**. Các thuật toán mã hóa này cho phép mạng lưới xác minh rằng *Đầu vào = Đầu ra + Phí* và tất cả các giá trị đều là số nguyên dương, mà không bao giờ tiết lộ các con số cụ thể cho sổ cái công khai. Chỉ những người tham gia nắm giữ khóa che giấu mới có thể xem dữ liệu đã được giải mã.


#### Phát hành tài sản

Liquid coi tất cả các tài sản là "tài sản gốc". Cho dù đó là Liquid, Bitcoin (L-BTC), một stablecoin như USDT, hay một loại chứng khoán token, tất cả đều có chung kiến trúc. Việc phát hành một tài sản không yêu cầu hợp đồng thông minh—chỉ cần một lệnh gọi RPC đơn giản.


- Tài sản không được kiểm soát:** Bất kỳ ai cũng có thể phát hành mà không cần xin phép.
- Tài sản được quản lý:** Bằng cách sử dụng Nền tảng Quản lý Tài sản Blockstream (AMP), các nhà phát hành có thể thực thi các quy tắc tuân thủ (như KYC/AML) bằng cách yêu cầu chữ ký thứ hai từ máy chủ ủy quyền trước khi tài sản có thể được chuyển.


### Cơ chế neo hai chiều và liên bang năng động


Cầu nối giữa Bitcoin và Liquid là **Cơ chế neo hai chiều**. Nó cho phép người dùng chuyển BTC vào chuỗi phụ (Peg-in) và quay trở lại mainchain (Peg-out).


**Quy trình gắn chốt:**

Đây là giao dịch không cần cấp phép. Người dùng gửi BTC đến một địa chỉ do liên minh kiểm soát. Để bảo vệ chống lại các cuộc tái cấu trúc chuỗi khối Bitcoin, số tiền này phải chờ **102 xác nhận** (khoảng 17 giờ) trước khi L-BTC tương đương được tạo ra trên chuỗi phụ.


**Quy trình cắm chốt:**

Để quay trở lại Bitcoin, L-BTC được đốt. Tuy nhiên, để ngăn chặn hành vi trộm cắp dự trữ Bitcoin, việc rút tiền không được tự động hóa hoàn toàn. Chúng yêu cầu sự ủy quyền từ một thành viên nắm giữ **Khóa Ủy quyền Rút tiền (PAK)**. Bản thân quỹ Bitcoin được bảo mật trong wallet đa chữ ký 11/15, với các khóa được lưu giữ trong Mô-đun Bảo mật Phần cứng (HSM) được cách ly hoàn toàn khỏi máy chủ chính của các nhân viên vận hành.


**Liên đoàn năng động (Dynafed):**

Để đảm bảo tuổi thọ lâu dài, Liquid sử dụng Dynafed, một giao thức cho phép mạng xoay vòng các chức năng viên hoặc cập nhật các tham số mà không cần fork cứng nhắc. Nếu cần thay thế một chức năng viên, mạng sẽ phát đi một giao dịch chuyển đổi. Sau thời gian chuyển tiếp hai tuần, cấu hình mới sẽ tiếp quản, cho phép liên kết phát triển liền mạch trong khi vẫn duy trì thời gian hoạt động liên tục.


## Hệ sinh thái và thị trường vốn


<chapterId>5f4c0e50-b435-4b6c-b8b7-c55cc1a35431</chapterId>


:::video id=07e0b82f-2d60-4eb3-9b5d-2ccb7ad06e8a:::

### Liquid Network: Chiến lược kinh doanh và hệ sinh thái


Liquid không chỉ là một sidechain kỹ thuật; nó là một lớp cơ sở hạ tầng tập trung vào kinh doanh, được thiết kế để xử lý các yêu cầu phức tạp của thị trường vốn mà Bitcoin và mainchain không thể hỗ trợ hiệu quả. Trong khi Lightning Network tối ưu hóa cho các khoản thanh toán tần suất cao, giá trị thấp, Liquid lại nhắm đến các giao dịch chuyển tiền giá trị cao, phát hành tài sản và thanh toán liên sàn giao dịch.


Hệ sinh thái này được thúc đẩy bởi **Liên đoàn Liquid**, một tập đoàn gồm khoảng 73 công ty, bao gồm các sàn giao dịch, bộ phận giao dịch và nhà cung cấp cơ sở hạ tầng. Mô hình hợp tác này tương tự như các trung tâm thanh toán bù trừ tài chính truyền thống nhưng hoạt động minh bạch hơn và thời gian thanh toán được rút ngắn đáng kể (2 phút so với T+2 ngày).


### Mã hóa tài sản thế giới thực (RWA)


Cốt lõi của mô hình kinh doanh Liquid là "Mã hóa token" - thể hiện giá trị thực tế (cổ phiếu, trái phiếu, hợp đồng mining) dưới dạng token kỹ thuật số trên blockchain. Điều này mang lại ba lợi thế chính:

1. **Thị trường toàn cầu 24/7:** Loại bỏ giờ làm việc ngân hàng và các hạn chế về địa lý.

2. **Hiệu quả hoạt động:** Loại bỏ lỗi đối chiếu thông qua sổ cái chung, bất biến.

3. **Thanh toán nguyên tử:** Giảm rủi ro cho đối tác bằng cách đảm bảo việc giao hàng diễn ra đồng thời với việc thanh toán.


#### Tài sản được quản lý và AMP

Hầu hết các tài sản của các tổ chức không thể giao dịch mà không có sự cho phép do các yêu cầu pháp lý. **Nền tảng quản lý tài sản (AMP)** là tiêu chuẩn kỹ thuật thực thi các quy tắc này.


- Danh sách trắng:** Các tổ chức phát hành có thể hạn chế việc nắm giữ và giao dịch đối với các địa chỉ đã được xác minh KYC.
- Kiểm soát Multisig:** Các hành động tuân thủ (như đóng băng tiền bị đánh cắp hoặc cấp lại mã thông báo bị mất) được quản lý thông qua ủy quyền đa chữ ký, đảm bảo không một nhân viên nào có thể hành động đơn phương.


Cơ sở hạ tầng này hiện đang hoạt động. Các nền tảng như **Stalker** cung cấp dịch vụ mã hóa tài sản từ đầu đến cuối tại châu Âu, trong khi **Sideswap** hoạt động như một sàn giao dịch phi tập trung và wallet không lưu ký, cho phép giao dịch ngang hàng các tài sản như **Blockstream Mining Note (BMN)** và cổ phiếu MicroStrategy được mã hóa (CMSTR).


### Thành công thực tiễn: Nghiên cứu trường hợp Mayfell


Bằng chứng thuyết phục nhất về tính hữu ích của Liquid đến từ **Mayfell** ở Mexico. Trong một thị trường mà phương thức tài chính truyền thống dựa vào giấy nợ ghi nợ—vốn dễ bị mất mát, gian lận và xử lý chậm—Mayfell đã chuyển toàn bộ cơ sở hạ tầng sang Liquid.



- Quy mô:** Hơn 25.000 giấy nợ đã phát hành, với tổng giá trị hơn **1,5 tỷ đô la**.
- **Bảo mật:** Sử dụng Confidential Transactions của Liquid, số tiền cho vay chỉ hiển thị cho người cho vay và người đi vay, bảo vệ quyền riêng tư thương mại đồng thời cho phép kiểm toán viên xác minh tính toàn vẹn của sổ cái.
- Tác động:** Bằng cách kết nối các tổ chức cho vay phi ngân hàng với thị trường vốn toàn cầu thông qua công nghệ blockchain, Mayfell đã giảm chi phí và mở rộng khả năng tiếp cận tín dụng cho các doanh nghiệp vừa và nhỏ của Mexico, chứng minh rằng giá trị mà Liquid mang lại vượt xa hoạt động giao dịch đầu cơ.


### Định vị chiến lược so với các chuỗi cửa hàng khác


Liquid cạnh tranh trong một thị trường đầy rẫy các nền tảng mã hóa token (Ethereum, Solana, v.v.), nhưng nó sở hữu những lợi thế chiến lược riêng biệt:


- **Tính rõ ràng về quy định:** Liquid sử dụng Bitcoin (L-BTC) làm tài sản gốc. Nó không có token được khai thác trước hoặc ICO, tránh được rủi ro "chứng khoán chưa đăng ký" thường gặp ở các blockchain L1 khác.
- Tính ổn định:** Không giống như mô hình tài khoản của Ethereum, nơi các giao dịch thất bại vẫn tiêu tốn phí gas, mô hình UTXO của Liquid có tính xác định và đáng tin cậy đối với dữ liệu tài chính quan trọng.
- Bảo mật:** Bảo mật mặc định là yêu cầu bắt buộc đối với hầu hết các tổ chức tài chính, một tính năng mà Liquid cung cấp sẵn nhưng các chuỗi công khai lại khó thực hiện được nếu không có các tiện ích bổ sung phức tạp.


Đối với các nhà phát triển, hệ sinh thái này mang đến một cơ hội rõ ràng: xây dựng các công cụ (bảng điều khiển, ví điện tử, tích hợp tuân thủ) kết nối tài chính truyền thống với lớp thanh toán an toàn của Bitcoin.


## Blockstream AMP


<chapterId>4f21a0a7-0dc0-44cf-8a3a-d9e2f8a3f05f</chapterId>


:::video id=f00822b4-dc1a-46ff-adfc-ff7c97a0024d:::

### Blockstream AMP: Kiểm soát tài sản có quyền truy cập trên Liquid


Nền tảng quản lý tài sản Blockstream AMP đóng vai trò là lớp cơ sở hạ tầng quan trọng trên Liquid Network, được thiết kế đặc biệt cho các nhà phát hành chứng khoán kỹ thuật số và stablecoin được quản lý. Mặc dù Liquid cung cấp lớp nền tảng không cần cấp phép với khả năng phát hành tài sản gốc, nhưng các tổ chức được quản lý thường yêu cầu khả năng giám sát và tuân thủ nghiêm ngặt. AMP khắc phục khoảng trống này bằng cách giới thiệu lớp kiểm soát có cấp phép đối với các tài sản cụ thể mà không làm mất đi lợi ích về quyền riêng tư của Confidential Transactions trên Liquid.


Giá trị cốt lõi của nền tảng dựa trên hai khả năng chính: khả năng hiển thị toàn diện của nhà phát hành và ủy quyền giao dịch. Không giống như các tài sản Liquid tiêu chuẩn, nơi số lượng và loại tài sản được công khai cho tất cả mọi người trừ người tham gia, tài sản AMP cho phép nhà phát hành duy trì một nhật ký kiểm toán hoàn chỉnh. Tính minh bạch này rất cần thiết cho việc báo cáo theo quy định và kiểm toán nội bộ. Hơn nữa, AMP thực thi một mô hình ủy quyền nghiêm ngặt thông qua cơ chế đồng ký. Mỗi lần chuyển nhượng tài sản AMP đều yêu cầu chữ ký từ máy chủ AMP. Điều này cho phép các nhà phát hành thực thi các quy tắc phức tạp — chẳng hạn như đóng băng tài khoản, đưa nhà đầu tư đủ điều kiện vào danh sách trắng hoặc áp đặt giới hạn chuyển nhượng — hoạt động hiệu quả như một người gác cổng tập trung trong một mạng lưới phi tập trung.


#### Sự đánh đổi trong hoạt động

Kiến trúc này đưa ra những sự đánh đổi cụ thể. Hệ thống phụ thuộc vào tính khả dụng của máy chủ AMP; nếu máy chủ đóng vai trò là bên bảo lãnh và ngừng hoạt động, tính thanh khoản của tài sản sẽ bị tạm dừng. Ngoài ra, mặc dù quyền riêng tư giữa người dùng được duy trì, nhà đầu tư phải chấp nhận rằng nhà phát hành có toàn quyền truy cập vào số tài sản họ nắm giữ. Mô hình này lý tưởng cho các token bảo mật tuân thủ quy định nhưng không phù hợp với các loại tiền điện tử có khả năng chống kiểm duyệt.


### Sự tiến hóa kiến trúc và các con đường tích hợp


Hệ sinh thái AMP hiện đang chuyển đổi từ phiên bản đầu tiên sang kiến trúc "Phiên bản 2" linh hoạt và có khả năng tương tác cao hơn. Hệ thống cũ yêu cầu các nhà phát hành phải duy trì các nút Elements được đồng bộ hóa hoàn toàn và buộc các nhà phát triển phải phụ thuộc nhiều vào bộ SDK Green nguyên khối. Mặc dù vẫn hoạt động được, điều này đã tạo ra rào cản kỹ thuật cao và hạn chế các lựa chọn wallet.


Kiến trúc thế hệ tiếp theo về cơ bản đơn giản hóa các yêu cầu này bằng cách chuyển độ phức tạp sang máy chủ. Trong mô hình mới này, máy chủ AMP đảm nhiệm các công việc nặng nhọc như xây dựng giao dịch, lựa chọn UTXO và tính toán phí. Nó cung cấp cho bên phát hành một Giao dịch Elements được ký một phần (PSET) chỉ cần chữ ký. Cách tiếp cận "máy chủ thông minh, wallet đơn giản" này loại bỏ nhu cầu các bên phát hành phải vận hành các node đầy đủ và cho phép sử dụng ví phần cứng và các thiết lập đa chữ ký tiêu chuẩn để quản lý kho bạc.


Đối với các nhà phát triển, sự tiến hóa này có nghĩa là chuyển từ các SDK độc quyền sang các mô tả tiêu chuẩn và quy trình làm việc PSET. Ví điện tử giờ đây có thể đăng ký các mô tả đa chữ ký với máy chủ AMP để thiết lập quyền ủy quyền. Điều này giúp việc phát triển AMP phù hợp với các tiêu chuẩn Bitcoin và wallet rộng hơn, giúp việc tích hợp trở nên dễ dàng đối với bất kỳ ứng dụng nào có khả năng xử lý các định dạng PSBT/PSET. Các nhà phát triển hiện nay được khuyến khích sử dụng các công cụ như Liquid và Wallet Kit (LWK), hỗ trợ các kiến trúc dựa trên mô tả hiện đại này, đảm bảo ứng dụng của họ được trang bị đầy đủ cho các tiêu chuẩn AMP mới trong tương lai.


### Hệ sinh thái Liquid Wallet và tính bảo mật


Việc xây dựng ứng dụng trên Liquid đòi hỏi phải điều hướng qua một hệ thống phức tạp hơn so với phát triển Bitcoin tiêu chuẩn do các tính năng như tài nguyên gốc và Confidential Transactions. Hệ sinh thái được hỗ trợ bởi kiến trúc phân lớp: các thư viện cấp thấp như `secp256k1-zkp` xử lý các thuật toán mã hóa, trong khi các bộ công cụ cấp cao hơn quản lý logic wallet.


Trong quá khứ, bộ công cụ phát triển Green (GDK) cung cấp một giải pháp toàn diện nhưng cứng nhắc. Giải pháp thay thế hiện đại là bộ công cụ Liquid Wallet (LWK), cung cấp cách tiếp cận theo mô-đun. LWK tách biệt các vấn đề thành các crate riêng biệt—xử lý các mô tả, ký số và giao tiếp phần cứng một cách độc lập—mang lại cho các nhà phát triển sự linh hoạt để xây dựng các giải pháp tùy chỉnh mà không cần phải chịu gánh nặng của một thư viện nguyên khối.


#### Xử lý Confidential Transactions

Thách thức rõ rệt nhất trong hệ sinh thái này là quản lý vòng đời của quá trình che giấu thông tin. Trong Liquid, đầu ra giao dịch được mã hóa bằng cách sử dụng trao đổi khóa Elliptic Curve Diffie-Hellman (ECDH). Người gửi sử dụng khóa công khai che giấu của người nhận để mã hóa số lượng và loại tài sản, tạo ra bằng chứng phạm vi xác minh tính hợp lệ của giao dịch mà không tiết lộ giá trị.


Để một thiết bị wallet hoạt động, nó phải đảo ngược thành công quá trình này. Khi wallet phát hiện một giao dịch đến, nó cố gắng giải mã đầu ra bằng khóa mã hóa riêng của mình. Nếu khóa bí mật được chia sẻ khớp nhau, wallet có thể giải mã giá trị và cộng nó vào số dư của người dùng. Quá trình này đòi hỏi nhiều tài nguyên tính toán và quản lý chính xác các yếu tố mã hóa để đảm bảo các giao dịch được cân bằng về mặt toán học, một sự phức tạp mà các công cụ như LWK hướng đến việc đơn giản hóa cho nhà phát triển.


# Kỹ thuật


<partId>53629f58-b9e0-4a10-8ab2-d51b047414f8</partId>

<chapterId>f1fdf2b0-4b6a-4ba7-812c-7586dcb36713</chapterId>


## Bộ SDK Breez - Không cần nút


<chapterId>fb77442c-3d1e-427e-b2f5-16668ce4c643</chapterId>


:::video id=1a6289b5-fdae-4320-b5b1-41925150108c:::

### Giới thiệu về Breez Liquid SDK


Bộ công cụ Breez Liquid SDK là một bộ công cụ mã nguồn mở, tự quản lý được thiết kế để thu hẹp khoảng cách giữa hệ sinh thái Liquid Network và Bitcoin rộng lớn hơn. Nhiệm vụ chính của nó là đơn giản hóa sự phức tạp của việc quản lý nút Lightning Network và các giao dịch hoán đổi nguyên tử, cho phép các nhà phát triển xây dựng các ứng dụng tài chính liền mạch.


Được xây dựng theo triết lý "ưu tiên thiết bị di động", logic cốt lõi được viết bằng Rust để đảm bảo hiệu suất và an toàn, nhưng nó sử dụng UniFFI (Unified Foreign Function Interface) để cung cấp các liên kết gốc cho Kotlin, Swift, Python, C#, Dart và Flutter. Điều này đảm bảo rằng các nhà phát triển có thể tích hợp chức năng Bitcoin vào môi trường ưa thích của họ mà không cần quản lý các hoạt động mã hóa cấp thấp.


**Các loại giao dịch được hỗ trợ:**

Bộ SDK hoạt động với Liquid là "căn cứ chính". Nó xuất sắc trong ba hoạt động cụ thể:

1. **Liquid sang Liquid:** Chuyển khoản trực tiếp on-chain.

2. **Liquid-to-Lightning:** Thanh toán hóa đơn Lightning bằng tiền trong tài khoản Liquid.

3. **Từ Liquid sang Bitcoin:** Chuyển tiền trực tiếp sang Bitcoin và mainchain.


*Lưu ý: SDK này không hỗ trợ các giao dịch trực tiếp giữa Lightning và Lightning hoặc giữa Bitcoin và Bitcoin. Nó chỉ là công cụ tập trung vào Liquid.*


### Kiến trúc thanh toán: Hoán đổi ngầm dưới biển


Để đạt được khả năng tương tác giữa Liquid, Lightning và Bitcoin mà không cần người giám sát tập trung, Breez dựa vào **Submarine Swaps**. Đây là các hoạt động nguyên tử, trong đó giao dịch hoặc hoàn tất thành công trên cả hai mạng hoặc thất bại trên cả hai, đảm bảo tiền không bao giờ bị mất trong quá trình truyền tải.


#### Gửi nhanh như chớp (Trao đổi tàu ngầm)

Khi người dùng thanh toán hóa đơn Lightning, SDK sẽ phát đi một giao dịch "khóa" trên Liquid Network. Điều này giúp giữ số tiền trong tài khoản ký quỹ. Nhà cung cấp dịch vụ hoán đổi (Boltz) phát hiện điều này, thanh toán hóa đơn Lightning, và sau đó sử dụng ảnh trước của khoản thanh toán (biên lai mã hóa) để nhận số tiền bị khóa trên Liquid.


#### Nhận tín hiệu sét (Trao đổi tàu ngầm ngược)

Việc nhận Lightning là một quá trình ngược lại. Người dùng tạo hóa đơn, và nhà cung cấp dịch vụ hoán đổi khóa tiền trên Lightning Network. SDK giám sát quá trình này thông qua WebSockets. Sau khi khóa được xác nhận, SDK tự động thực hiện giao dịch yêu cầu để chuyển số tiền tương đương vào Liquid hoặc wallet của người dùng.


#### Chuỗi chéo Bitcoin

Đối với các giao dịch chuyển tiền từ Liquid sang Bitcoin, kiến trúc này sử dụng cơ chế "trao đổi kép". Các giao dịch khóa tiền diễn ra đồng thời trên cả hai chuỗi. Người gửi nhận tiền trên Bitcoin, trong khi người nhận nhận tiền trên Liquid. Điều này cho phép kết nối không cần tin cậy mà không cần dựa vào các cổng federated peg hoặc các sàn giao dịch tập trung.


### Nhà phát triển Interface và Quản lý tự động


Bộ SDK Breez đơn giản hóa trải nghiệm của nhà phát triển bằng cách cô đọng các quy trình tài chính phức tạp thành một quy trình ba bước tiêu chuẩn: **Kết nối, Chuẩn bị và Thực thi**.


1. **Kết nối:** Khởi tạo wallet, đồng bộ hóa với chuỗi khối bằng cách sử dụng Bộ công cụ Liquid Wallet (LWK) và thiết lập kết nối WebSocket để giám sát thời gian thực.

2. **Chuẩn bị:** Trước khi cam kết tiền, bước này tính toán và trả về tất cả các khoản phí mạng và phí hoán đổi liên quan, cho phép giao diện người dùng hiển thị tổng số tiền rõ ràng cho người dùng.

3. **Thực thi:** Bước này tạo ra giao dịch, phát tán nó và bắt đầu quá trình hoán đổi.


#### Cơ chế an toàn tự động

Một trong những tính năng quan trọng nhất của SDK là **Quản lý hoàn tiền tự động**. Trong trường hợp mạng gặp sự cố hoặc đối tác không hợp tác, về mặt lý thuyết, tiền có thể bị kẹt trong hợp đồng có thời hạn cố định. SDK hoàn toàn trừu tượng hóa logic phục hồi. Nó giám sát trạng thái của mọi giao dịch hoán đổi; nếu giao dịch hoán đổi thất bại hoặc hết thời gian, SDK sẽ tự động tạo và phát sóng giao dịch hoàn tiền để trả lại tiền cho wallet của người dùng.


Ngoài ra, SDK còn xử lý **Giải quyết siêu dữ liệu**. Nó hợp nhất dữ liệu hoán đổi off-chain (do bộ hoán đổi Boltz cung cấp) với lịch sử giao dịch on-chain. Điều này đảm bảo lịch sử giao dịch của người dùng dễ đọc, hiển thị chi tiết hóa đơn và ngữ cảnh thanh toán thay vì chỉ là các mã băm giao dịch thập lục phân thô.


# Phần cuối


<partId>7ec65e6b-6e63-41b6-92ea-6a13bc77c3ff</partId>


## Đánh giá & Xếp hạng


<chapterId>e5f6348c-e207-40ae-8fef-6a068a6bf741</chapterId>


<isCourseReview>true</isCourseReview>

## Bài kiểm tra cuối kỳ


<chapterId>b13c4aa8-ced6-11f0-8515-afd3f381a001</chapterId>

<isCourseExam>true</isCourseExam>

## Phần kết luận


<chapterId>e30a5587-d74b-4360-87fb-bbf3de1b0ba8</chapterId>

<isCourseConclusion>true</isCourseConclusion>