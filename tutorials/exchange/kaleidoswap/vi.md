---
name: KaleidoSwap
description: Hướng dẫn nâng cao về giao dịch tài sản RGB trên Lightning Network với KaleidoSwap
---

![cover](assets/cover.webp)


KaleidoSwap là một ứng dụng máy tính để bàn mã nguồn mở tiên tiến, đóng vai trò cầu nối giữa Giao thức RGB và Lightning Network. Nó hoạt động như một giao diện toàn diện để quản lý các Nút Lightning RGB, tương tác với các Nhà cung cấp Dịch vụ Lightning RGB (LSP) thông qua đặc tả LSPS1 và thực hiện các giao dịch hoán đổi nguyên tử tài sản RGB.


Là một giải pháp không lưu giữ khóa riêng, KaleidoSwap cho phép người dùng duy trì toàn quyền kiểm soát khóa và dữ liệu của họ. Bằng cách tận dụng mô hình xác thực phía máy khách của RGB, nó cho phép các hợp đồng thông minh riêng tư và có khả năng mở rộng trên nền tảng Bitcoin. Hướng dẫn này sẽ đi sâu vào các tính năng nâng cao của KaleidoSwap, hướng dẫn bạn qua những điểm phức tạp của việc quản lý UTXO "có màu", thanh khoản kênh cho các tài sản cụ thể và mô hình giao dịch taker-maker, đảm bảo bạn có thể tận dụng tối đa giao thức trao đổi phi tập trung mạnh mẽ này.


## Lắp đặt


KaleidoSwap cung cấp các tệp nhị phân được biên dịch sẵn cho các hệ điều hành chính, nhưng đối với người dùng nâng cao, việc biên dịch từ mã nguồn đảm bảo bạn đang chạy phiên bản mã mới nhất với cấu hình cụ thể của mình.


### Tải xuống các tệp nhị phân


Bạn có thể tải xuống phiên bản mới nhất cho hệ điều hành của mình từ [trang web chính thức](https://kaleidoswap.com/) hoặc [trang phát hành trên GitHub](https://github.com/kaleidoswap/desktop-app/releases).


### Phương pháp lắp đặt


1. **Windows**: Tải xuống tệp cài đặt `.exe` và chạy nó.

2. **macOS**: Tải xuống tệp `.dmg`, mở nó và kéo KaleidoSwap vào thư mục Ứng dụng của bạn.

3. **Linux**: Tải xuống tệp `.AppImage` hoặc `.deb` và cài đặt/chạy ứng dụng.



## Tùy chọn thiết lập nút


Khi bạn khởi chạy KaleidoSwap lần đầu tiên, bạn sẽ thấy **Màn hình Kết nối**. Đây là bước đầu tiên trong quá trình cấu hình môi trường của bạn.


![Node Selection Screen](assets/en/01.webp)


Bạn phải chọn cách kết nối với RGB hoặc Lightning Network. Lựa chọn này sẽ ảnh hưởng đến mức độ kiểm soát và quyền riêng tư của bạn.


### Phương án 1: Nút cục bộ (Khuyến nghị cho trường hợp tự quản lý)


**Để có quyền kiểm soát và bảo mật hoàn toàn**, hãy chạy một node trực tiếp trên máy tính của bạn, xem các ưu điểm bên dưới:


- Tự quản lý**: Bạn nắm giữ chìa khóa. Không bên thứ ba nào có thể đóng băng tiền của bạn hoặc kiểm duyệt các giao dịch của bạn.
- **Bảo mật**: Dữ liệu của bạn chỉ được lưu trữ trên thiết bị của bạn.
- Độc lập**: Không phụ thuộc vào các nhà cung cấp dịch vụ bên ngoài.


Nếu bạn chọn **Nút cục bộ**, bạn sẽ được chuyển đến màn hình thiết lập, nơi bạn có thể tạo wallet mới hoặc khôi phục wallet hiện có.


![Local Node Setup Screen](assets/en/02.webp)


### Phương án 2: Nút từ xa


Kết nối với RGB Lightning Node từ xa (tự lưu trữ trên VPS hoặc nhà cung cấp dịch vụ lưu trữ).


- Ưu điểm**: Không tiêu tốn tài nguyên cục bộ, hoạt động 24/7.
- **Sự đánh đổi**: Yêu cầu phải tin tưởng nhà cung cấp dịch vụ lưu trữ hoặc quản lý máy chủ từ xa.


![Remote Node Setup Screen](assets/en/03.webp)


**KaleidoSwap được thiết kế để thúc đẩy quyền tự quản lý.** Chúng tôi đặc biệt khuyến nghị bạn tự vận hành node của riêng mình—hoặc cục bộ (Tùy chọn 1) hoặc bằng cách tự lưu trữ node từ xa—để tận dụng tối đa các đặc tính chống kiểm duyệt của Bitcoin và RGB.


## Tạo Wallet


KaleidoSwap quản lý cả tài sản Bitcoin và RGB. Quá trình tạo wallet khởi tạo một kho khóa bảo mật số tiền on-chain và trạng thái kênh Lightning của bạn.


Dưới đây là quy trình chi tiết:

1. Mở KaleidoSwap và chọn **Local Node**.

2. Nhấp vào **Tạo Wallet mới**.

3. **Thiết lập tài khoản**: Nhập **Tên tài khoản** và chọn **Mạng** (ví dụ: Bitcoin, Mainnet, Testnet, Signet).

4. **Cấu hình nâng cao** (Tùy chọn): Nếu bạn là người dùng thành thạo, bạn có thể cấu hình các điểm cuối RPC tùy chỉnh, URL trình lập chỉ mục hoặc cài đặt Proxy trong mục "Cài đặt nâng cao".

5. Nhấp vào **Tiếp tục**.

6. **Mật khẩu**: Hãy đặt một mật khẩu mạnh để mã hóa tệp wallet của bạn trên máy tính cục bộ.

7. **Cụm từ khôi phục**: Hãy viết cụm từ seed của bạn ra và cất giữ ở nơi an toàn.


    - Quan trọng**: Cụm từ này cần thiết để khôi phục số tiền và danh tính nút on-chain của bạn.
    - Cảnh báo**: **Trạng thái kênh Lightning không thể được khôi phục hoàn toàn chỉ bằng seed**. Bạn cũng phải duy trì các bản sao lưu kênh tĩnh (SCB) để khôi phục số tiền bị khóa trong các kênh.


![Wallet Creation Screen](assets/en/04.webp)



## Tổng quan bảng điều khiển


Sau khi tài khoản wallet của bạn được tạo, bạn sẽ được chuyển đến **Bảng điều khiển** chính.


![KaleidoSwap Dashboard](assets/en/05.webp)


_Lưu ý: Ảnh chụp màn hình ở trên hiển thị một wallet đã được nạp tiền và có các kênh hoạt động. Một wallet mới sẽ hiển thị số dư bằng không và không có kênh hoạt động nào cho đến khi bạn nạp tiền vào._


## Tìm nguồn tài trợ cho Wallet của bạn


Để giao dịch với tài sản RGB, bạn cần nạp tiền vào wallet. KaleidoSwap hỗ trợ nạp cả tài sản Bitcoin và RGB thông qua giao dịch on-chain hoặc Lightning Network.


### Đang gửi Bitcoin


1. Nhấp vào **Nạp tiền** trong menu Thao tác nhanh.

2. Chọn **BTC** từ danh sách tài sản.


![Select BTC Asset](assets/en/06.webp)


3. Chọn phương thức nạp tiền: **Trên chuỗi** hoặc **Lightning**.


![BTC Deposit Options](assets/en/07.webp)



- Trên chuỗi**: Quét mã QR hoặc sao chép địa chỉ để gửi Bitcoin từ một wallet khác.
- Lightning**: Tạo hóa đơn với số tiền mong muốn.


![BTC On-chain Deposit](assets/en/08.webp)


### Gửi tài sản RGB và UTXO được tô màu.


Để nhận được tài sản RGB (như USDT), bạn cần có các UTXO cụ thể để được "đánh dấu" (gán tài sản).


1. Nhấp vào **Nạp tiền** và chọn tài sản RGB (ví dụ: USDT). **Quan trọng**: Nếu đây là **lần đầu tiên** node của bạn nhận được tài sản cụ thể này, **hãy để trống trường ID tài sản**. Việc nhập ID cho một tài sản không xác định sẽ khiến node trả về lỗi vì nó chưa nhận dạng được tài sản đó.

2. Chọn **On-chain** hoặc **Lightning**.


![USDT Deposit Options](assets/en/09.webp)


#### Các chế độ nhận trên chuỗi: Witness so với Blinded


Khi nhận tài sản RGB hoặc on-chain, bạn có hai chế độ bảo mật:



- Nhận ẩn danh (Khuyến nghị để bảo mật)**: Bạn cung cấp cho người gửi một UTXO "blinded". Bạn yêu cầu người gửi gửi tài sản đến một UTXO hiện có mà bạn sở hữu, nhưng bạn che giấu mã định danh UTXO thực tế. Điều này mang lại sự bảo mật tốt hơn.
- **Xác nhận chứng thực**: Bạn cung cấp địa chỉ Bitcoin tiêu chuẩn. Bạn yêu cầu người gửi tạo một UTXO *mới* cho bạn bằng cách gửi tài sản đến địa chỉ đó. Điều này cho phép tài sản RGB được đính kèm trực tiếp vào UTXO mới được tạo bởi giao dịch.


#### Tiền gửi sét


Đối với các khoản tiền gửi Lightning, chỉ cần sử dụng hóa đơn generate. Tài sản RGB sẽ được chuyển đến bạn thông qua các kênh mở của bạn.


![USDT Lightning Invoice](assets/en/10.webp)



## Mở rộng kênh liên lạc với các thiết bị RGB


Để định tuyến tài sản RGB qua Lightning Network, bạn cần một kênh có đủ thanh khoản và phân bổ tài sản. Cách dễ nhất để bắt đầu là **Mua một kênh** từ một LSP (Nhà cung cấp dịch vụ Lightning).


### Mua kênh từ Kaleido LSP


1. Vào tab **Kênh**. Bạn sẽ thấy các tùy chọn "Mở kênh" (thủ công) hoặc "Mua kênh" (LSP).

2. Nhấp vào **Mua kênh**.


![Channels Dashboard](assets/en/11.webp)


3. **Kết nối với LSP**: Ứng dụng sẽ kết nối với LSP mặc định của Kaleido. Nhà cung cấp này cung cấp thanh khoản đầu vào và hỗ trợ định tuyến tài sản RGB.


![Connect to LSP](assets/en/12.webp)


4. **Cấu hình kênh**:


    - Dung lượng**: Chọn tổng dung lượng Bitcoin cho kênh.
    - Phân bổ RGB**: Chọn loại tài sản RGB (ví dụ: USDT) mà bạn muốn có thể nhận hoặc gửi. LSP sẽ đảm bảo kênh được cấu hình để hỗ trợ loại tài sản này.


![Configure Channel](assets/en/13.webp)



    - Phân bổ RGB**: Chọn loại tài sản RGB (ví dụ: USDT) mà bạn muốn có thể nhận hoặc gửi. LSP sẽ đảm bảo kênh được cấu hình để hỗ trợ loại tài sản này.


![RGB Allocation](assets/en/14.webp)


5. **Thanh toán**: Bạn phải trả phí cho LSP để mở kênh và cung cấp thanh khoản. Bạn có thể thanh toán bằng **Lightning** hoặc **trên chuỗi** Bitcoin. Việc thanh toán có thể được thực hiện từ wallet nội bộ của KaleidoSwap hoặc wallet bên ngoài.


![Complete Payment](assets/en/15.webp)


6. Sau khi thanh toán được xác nhận, LSP sẽ tiến hành giao dịch mở kênh. Bạn sẽ thấy màn hình **Đơn hàng hoàn tất**.


![Order Completed](assets/en/16.webp)


7. Sau khi được xác nhận trên blockchain, kênh của bạn sẽ hoạt động và sẵn sàng cho các giao dịch chuyển khoản RGB.



## Giao dịch: Mô hình người mua-người bán


Hệ thống giao dịch của KaleidoSwap hoạt động theo mô hình **Người mua - Người bán**. Bạn có thể tự mình trao đổi tài sản với người dùng khác hoặc sử dụng Nhà tạo lập thị trường (LSP).


### Giao dịch hoán đổi với nhà tạo lập thị trường (LSP)


Đây là cách giao dịch phổ biến nhất. Bạn đóng vai trò là **Người nhận lệnh**, thực hiện các lệnh dựa trên lượng thanh khoản có sẵn do LSP cung cấp (**Người tạo lệnh**).


1. Điều hướng đến tab **Giao dịch** và chọn **Nhà tạo lập thị trường**.

2. **Nhập số lượng**: Nhập số lượng Bitcoin bạn muốn gửi (hoặc tài sản bạn muốn nhận). Giao diện sẽ hiển thị tỷ giá hối đoái ước tính và phí.


![Market Maker Swap](assets/en/17.webp)


3. **Xác nhận giao dịch**: Xem lại chi tiết, bao gồm tỷ giá hối đoái và số tiền chính xác bạn sẽ nhận được. Nhấp vào **Xác nhận giao dịch**.


![Confirm Swap](assets/en/18.webp)


4. **Quá trình xử lý**: Thao tác hoán đổi được thực hiện một cách nguyên tử trên Lightning Network. Bạn sẽ thấy màn hình trạng thái cho biết thao tác hoán đổi đang chờ xử lý.


![Swap Pending](assets/en/19.webp)


5. **Thành công**: Sau khi các HTLC được xác nhận, giao dịch hoán đổi hoàn tất và tài sản đã có trong kênh của bạn.


![Swap Success](assets/en/20.webp)



## Nhà phát triển API


Đối với các nhà phát triển xây dựng dựa trên KaleidoSwap, ứng dụng này cung cấp một API hỗ trợ:



- RGB LSPS1**: Dành cho các dịch vụ thanh khoản tự động.
- Swap API**: Dành cho giao dịch lập trình và tạo lập thị trường.
- WebSocket**: Dành cho việc đăng ký nhận dữ liệu thị trường theo thời gian thực.


Vui lòng tham khảo [Tài liệu API](https://docs.kaleidoswap.com/api/introduction) để biết đầy đủ các điểm cuối và thông số kỹ thuật.


## Phần kết luận


KaleidoSwap cho phép bạn tận dụng tính bảo mật và khả năng mở rộng của tài sản RGB trên Lightning Network. Bằng cách hiểu về Colored UTXO và phân bổ tài sản kênh, bạn có thể khai thác tối đa giao thức trao đổi phi tập trung mạnh mẽ này.