---
name: Bitcoin Knots
description: Làm thế nào để khởi chạy một nút bằng ứng dụng khách thay thế Bitcoin Knots?
---
![cover](assets/cover.webp)

Bitcoin Knots là một triển khai thay thế của giao thức Bitcoin, bắt nguồn từ Bitcoin Core. Được thiết kế và bảo trì bởi Luke Dashjr, nó cung cấp một số tính năng bổ sung và điều chỉnh quy tắc từ Mempool, trong khi vẫn tương thích với các nút khác trên mạng. Bitcoin Knots tích hợp Bitcoin Wallet, nhưng cũng có thể được sử dụng như một nút Bitcoin đơn giản cùng với phần mềm Wallet khác.

## Tại sao nên sử dụng Knots thay vì Core?

Hiện tại, Core là triển khai phần lớn giao thức Bitcoin trên mạng. Giao thức Bitcoin chỉ là một tập hợp các quy tắc. Nó yêu cầu phần mềm để áp dụng chúng. Một máy chạy phần mềm triển khai giao thức Bitcoin được gọi là một nút và tất cả các nút này cùng nhau tạo nên mạng Bitcoin.

Trong suốt lịch sử của Bitcoin, nhiều máy khách bắt nguồn từ phần mềm ban đầu do Satoshi Nakamoto phát triển đã xuất hiện. Ngày nay (tháng 3 năm 2025), Bitcoin Core là phần lớn áp đảo, với gần 98% các nút trên mạng Bitcoin sử dụng máy khách này.

Tuy nhiên, phần mềm thay thế cũng khả dụng. Đây không phải là các nút liên kết Altcoin như Bitcoin Cash, mà là các máy khách thay thế tương thích với mạng Bitcoin thực. Trong số này, Bitcoin Knots là máy khách được biết đến nhiều nhất. Hiện tại, nó chiếm khoảng 1,4% mạng. Các máy khách thay thế khác vẫn còn rất ít.

![Image](assets/fr/01.webp)

Có hai lý do chính để sử dụng ứng dụng thay thế như Knots thay vì Core:


- Kỹ thuật**: Các máy khách này thường cung cấp các tùy chọn khác nhau cho Core, đặc biệt là về mặt quản lý Mempool, bằng cách xác định giao dịch nào được nút của bạn chấp nhận và phát đi.
- Chính sách**: Một số người thích sử dụng các máy khách thay thế như Knots vì những lý do không liên quan đến kỹ thuật, đặc biệt là để hỗ trợ một giải pháp thay thế cho Core và do đó làm giảm sự độc quyền của nó. Nếu Core bị xâm phạm, sẽ hữu ích không chỉ khi có các máy khách thay thế vững chắc, được bảo trì tốt mà còn phải biết cách sử dụng chúng. Những người khác sử dụng Knots cho mục đích phản đối, vì họ đã mất lòng tin vào các nhà phát triển Core hoặc không chấp thuận cách quản lý của phần lớn máy khách.

## Làm thế nào để cài đặt Bitcoin Knots?

Truy cập [trang web chính thức của Bitcoin Knots](https://bitcoinknots.org/#download) để tải xuống phiên bản cho hệ điều hành của bạn. Đừng quên tải xuống dấu vân tay và chữ ký để xác minh phần mềm. Các tệp này cũng có sẵn [trên kho lưu trữ GitHub của Bitcoin Knots](https://github.com/bitcoinknots/Bitcoin).

![Image](assets/fr/02.webp)

Trước khi cài đặt phần mềm trên máy của bạn, chúng tôi đặc biệt khuyên bạn nên kiểm tra tính xác thực và toàn vẹn của nó. Nếu bạn không biết cách, hãy xem hướng dẫn khác này:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc
Sau khi phần mềm đã được xác minh, hãy cài đặt phần mềm bằng cách làm theo các bước được chỉ dẫn trong bảng cài đặt.

![Image](assets/fr/03.webp)

## Ra mắt IBD

Lần đầu tiên bạn khởi chạy Bitcoin Knots, bạn sẽ có thể chọn thư mục cục bộ nơi dữ liệu nút của bạn (bao gồm Blockchain, UTXO và các tham số) sẽ được lưu trữ.

![Image](assets/fr/04.webp)

Bạn cũng có thể chọn cắt tỉa dữ liệu Blockchain để chỉ giữ lại các khối gần đây nhất. Tùy chọn này cho phép nút của bạn kiểm tra toàn bộ từng khối trong giới hạn lưu trữ đã đặt, do đó dần dần loại bỏ các khối cũ nhất. Nếu bạn có đủ dung lượng đĩa (hiện tại khoảng 650 GB, nhưng con số này đang tăng lên), hãy bỏ chọn tùy chọn này. Nếu dung lượng đĩa của bạn bị giới hạn, hãy kích hoạt cắt tỉa và chỉ định dung lượng tối đa được phép.

Xin lưu ý: Nếu nút của bạn bị cắt bớt và bạn sử dụng nó để đồng bộ hóa Wallet đã phục hồi, bạn sẽ không thể truy xuất các giao dịch trước khối được lưu trữ cục bộ cũ nhất.

![Image](assets/fr/05.webp)

Một tùy chọn khả dụng khác là "*Giả định hợp lệ*". Tùy chọn này tăng tốc quá trình đồng bộ hóa ban đầu bằng cách bỏ qua xác minh chữ ký cho các giao dịch được bao gồm trong các khối trước một khối cụ thể.

Mục đích của "*Giả định hợp lệ*" là tăng tốc quá trình đồng bộ hóa đầu tiên của nút mà không làm giảm đáng kể tính bảo mật, bằng cách giả định rằng các giao dịch này đã được mạng lưới xác thực hàng loạt trước đó. Sự thỏa hiệp quan trọng duy nhất là nút của bạn sẽ không phát hiện bất kỳ vụ trộm Bitcoin nào trước đó, nhưng nó vẫn đảm bảo tính chính xác của tổng số bitcoin được phát hành. Nút của bạn sẽ xác minh tất cả các chữ ký giao dịch sau khối được chỉ định. Cách tiếp cận này dựa trên giả định rằng một giao dịch đã được mạng lưới chấp nhận từ lâu mà không có thách thức thì rất có thể là hợp lệ.

Ví dụ, tại đây, "*Giả sử hợp lệ*" được đặt thành khối số 855 000 `00000000000000000000000233ea80aa10d38aa4486cd7033fffc2c4df556d0b9138`, được xuất bản vào ngày 1 tháng 8 năm 2024. Do đó, trong quá trình IBD, nút của tôi sẽ chỉ bắt đầu xác minh chữ ký đầy đủ từ khối này.

![Image](assets/fr/06.webp)

Sau đó nhấp vào nút "*OK*" để khởi chạy *Tải xuống khối ban đầu*. Bạn sẽ cần phải kiên nhẫn trong quá trình đồng bộ hóa nút ban đầu. Nếu bạn muốn tiếp tục đồng bộ hóa sau đó, chỉ cần đóng phần mềm và tắt máy tính. Đồng bộ hóa sẽ tiếp tục mà không gặp trục trặc nào vào lần tiếp theo bạn mở chương trình.

![Image](assets/fr/07.webp)

## Thiết lập nút Bitcoin của bạn

Nhấp vào tab "*Cài đặt*", sau đó chọn "*Tùy chọn*".

![Image](assets/fr/08.webp)

Trong tab "*Chính*", bạn truy cập vào các tham số chính của nút:


- "*Bắt đầu...*" tự động khởi chạy nút khi máy tính của bạn khởi động để bắt đầu đồng bộ hóa ngay lập tức;
- "*Cắt bớt...*" điều chỉnh giới hạn lưu trữ nếu bạn đã chọn cắt bớt Blockchain;
- "*Bộ nhớ đệm cơ sở dữ liệu...*" thiết lập dung lượng RAM tối đa được phép cho nút của bạn;
- Cuối cùng, kích hoạt "*Bật máy chủ RPC*" nếu bạn muốn kết nối nút Bitcoin Knots của mình với phần mềm danh mục đầu tư khác, chẳng hạn như Sparrow Wallet hoặc Liana.

![Image](assets/fr/09.webp)

Trong tab "*Wallet*", bạn sẽ tìm thấy các thiết lập cho danh mục đầu tư tích hợp mà bạn có thể tạo sau này trên Knots. Tôi khuyên bạn nên kích hoạt RBF và kiểm soát tiền xu. Bạn cũng có thể xác định loại tập lệnh sẽ sử dụng.

![Image](assets/fr/10.webp)

Tab "*Mạng*" chứa các thông số mạng mà bạn có thể điều chỉnh theo nhu cầu cụ thể của mình.

![Image](assets/fr/11.webp)

Tab "*Mempool*" cho phép bạn cấu hình *Nhóm bộ nhớ*, tức là quản lý các giao dịch chưa xác nhận được lưu trữ trong bộ nhớ và kích thước tối đa được phân bổ cho chức năng này (mặc định là 300 MB).

![Image](assets/fr/12.webp)

Tab "Lọc thư rác" là một tính năng của Bitcoin Knots. Tại đây, bạn sẽ tìm thấy một số cài đặt cho phép bạn chọn giao dịch nào bạn sẽ chấp nhận hoặc từ chối phát sóng. Mục tiêu chính là hạn chế một số cách sử dụng Bitcoin ở mức độ biên, đặc biệt là các siêu giao thức, để chống lại các hoạt động này trong khi tránh làm quá tải nút của bạn. Đây là một lựa chọn chính trị, tùy thuộc vào tầm nhìn cá nhân của bạn về Bitcoin.

Bạn cũng sẽ tìm thấy các tham số cổ điển như định nghĩa ngưỡng "*Dust*".

Tuy nhiên, các tham số này chỉ ảnh hưởng đến các quy tắc chuẩn hóa. Nút của bạn sẽ tiếp tục chấp nhận các giao dịch chưa được xác nhận chỉ khi chúng được đưa vào một khối, để duy trì khả năng tương thích với phần còn lại của mạng Bitcoin. Các thiết lập này chỉ sửa đổi cách nút của bạn xử lý và phân phối các giao dịch chưa được xác nhận cho các nút ngang hàng của nó. Trên thực tế, vì Knots là thiểu số, nên các quy tắc được thiết lập theo mặc định trên Bitcoin Core sẽ xác định chuẩn hóa trên mạng.

![Image](assets/fr/13.webp)

Tab "*Mining*" cho phép bạn cấu hình khả năng tham gia của nút bạn vào Mining, nếu bạn muốn kích hoạt chức năng này.

![Image](assets/fr/14.webp)

Cuối cùng, tab "*Hiển thị*" liên quan đến các thông số liên quan đến đồ họa Interface, bao gồm ngôn ngữ phần mềm.

![Image](assets/fr/15.webp)

## Tạo danh mục đầu tư Bitcoin

Sau khi quá trình đồng bộ hóa ban đầu hoàn tất, nút Bitcoin Knots của bạn sẽ hoạt động đầy đủ. Bây giờ bạn có tùy chọn kết nối nút này với phần mềm Wallet khác hoặc sử dụng trực tiếp Hot Wallet tích hợp. Để thực hiện, hãy nhấp vào nút "*Tạo Wallet mới*".

![Image](assets/fr/16.webp)

Đặt tên cho Wallet của bạn. Bạn cũng có thể bảo vệ nó bằng passphrase BIP39 bằng cách nhấp vào "*Mã hóa Wallet*". Khi đã sẵn sàng, hãy nhấp vào nút "*Tạo*".

![Image](assets/fr/17.webp)

passphrase BIP39 là mật khẩu tùy chọn mà bạn có thể tự do lựa chọn, ngoài cụm từ Mnemonic của bạn, để tăng tính bảo mật cho Wallet của bạn. Trước khi cấu hình tính năng này, chúng tôi khuyên bạn nên đọc bài viết sau, giải thích chi tiết về cách passphrase hoạt động trên lý thuyết và cách tránh những sai lầm có thể dẫn đến mất vĩnh viễn bitcoin của bạn:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7
Nếu bạn đã kích hoạt tùy chọn passphrase, hãy chọn tùy chọn mạnh mẽ và lưu cẩn thận trên một hoặc nhiều phương tiện vật lý an toàn.

![Image](assets/fr/18.webp)

Danh mục đầu tư Bitcoin của bạn hiện đã được tạo.

![Image](assets/fr/19.webp)

## Sao lưu danh mục đầu tư Bitcoin của bạn

Ngay cả trước khi bạn nhận được bitcoin đầu tiên, điều cần thiết là phải sao lưu Bitcoin Wallet của bạn để bạn có thể khôi phục tiền của mình trong trường hợp mất hoặc hỏng máy tính. Để thực hiện việc này, hãy nhấp vào tab "*File*" rồi nhấp vào "*Backup Wallet*".

![Image](assets/fr/20.webp)

Hoạt động này tạo ra một tệp duy nhất có thể được sử dụng để khôi phục tất cả bitcoin của bạn. Vì vậy, hãy rất cẩn thận và lưu nó trên một phương tiện bên ngoài an toàn.

## Nhận bitcoin

Để nhận bitcoin trực tiếp vào Knots Wallet của bạn, hãy nhấp vào nút "*Nhận*".

![Image](assets/fr/21.webp)

Gán "*Nhãn*" cho Address của bạn để dễ dàng xác định mục đích của nó và tạo điều kiện thuận lợi cho việc sử dụng *Coin Control* trong tương lai. Bạn cũng có thể xác định trước số tiền chính xác sẽ nhận được tại Address này hoặc thêm tin nhắn cho người trả tiền. Sau khi bạn đã thiết lập các thông số, hãy nhấp vào "*Yêu cầu thanh toán*".

![Image](assets/fr/22.webp)

Sau đó, Bitcoin Knots sẽ hiển thị Address nhận, bạn có thể sao chép hoặc quét và gửi cho người trả tiền.

![Image](assets/fr/23.webp)

Sau khi giao dịch được phát sóng, bạn có thể theo dõi trạng thái của giao dịch đó trực tiếp trong menu "*Giao dịch*".

![Image](assets/fr/24.webp)

## Gửi bitcoin

Bây giờ bạn đã có bitcoin trong Knots Wallet, bạn có thể gửi chúng. Để thực hiện, hãy nhấp vào nút "*Gửi*".

![Image](assets/fr/25.webp)

Nhấp vào nút "*Đầu vào...*" để chọn chính xác số UTXO mà bạn muốn chi cho giao dịch này.

![Image](assets/fr/26.webp)

Nhập Bitcoin Address của người nhận.

![Image](assets/fr/27.webp)

Thêm nhãn để ghi nhớ mục đích của giao dịch này.

![Image](assets/fr/28.webp)

Nhập số tiền bạn muốn gửi tới Address này.

![Image](assets/fr/29.webp)

Nhấp vào nút "*Chọn...*" để chọn mức phí phù hợp cho giao dịch của bạn, dựa trên trạng thái mạng hiện tại.

![Image](assets/fr/30.webp)

Nếu mọi thứ đều làm bạn hài lòng, hãy nhấp vào nút "*Gửi*". Nếu bạn đang sử dụng passphrase, bạn sẽ được yêu cầu điền thông tin ở giai đoạn này.

![Image](assets/fr/31.webp)

Kiểm tra lại các thông số giao dịch lần cuối, sau đó, nếu mọi thứ đều chính xác, hãy nhấp vào nút "*Gửi*" một lần nữa để ký và phân phối giao dịch của bạn.

![Image](assets/fr/32.webp)

Giao dịch đang chờ xác nhận của bạn hiện sẽ xuất hiện trong tab "*Giao dịch*".

![Image](assets/fr/33.webp)

## Kết nối nút của bạn với chương trình khác

Interface tích hợp của Bitcoin Knots để quản lý danh mục đầu tư Bitcoin của bạn không nhất thiết phải là trực quan nhất và chức năng của nó vẫn còn tương đối hạn chế. Tuy nhiên, bạn có thể kết nối nút Bitcoin Knots của mình với phần mềm quản lý danh mục đầu tư chuyên dụng để dễ dàng truy cập dữ liệu Blockchain Bitcoin và phát các giao dịch của bạn.

Quy trình này sẽ tùy thuộc vào phần mềm được sử dụng, nhưng có hai trường hợp chính: Bitcoin Knots được cài đặt trên cùng máy tính với phần mềm danh mục đầu tư của bạn hoặc chạy trên một máy riêng biệt.

### Với Bitcoin Knots cục bộ:

Nếu Bitcoin Knots được cài đặt trên máy tính của bạn, hãy tìm tệp `Bitcoin.conf` trong số các tệp phần mềm. Nếu tệp này không tồn tại, bạn có thể tạo tệp đó. Mở tệp đó bằng trình soạn thảo văn bản và chèn dòng sau:

```ini
server=1
```

Sau đó lưu lại thay đổi.

Bạn cũng có thể thực hiện việc này thông qua đồ họa Interface của Bitcoin-QT bằng cách điều hướng đến "*Cài đặt*" > "*Tùy chọn...*" và bật tùy chọn "*Bật máy chủ RPC*".

Đừng quên khởi động lại phần mềm sau khi thực hiện những thay đổi này.

![Image](assets/fr/34.webp)

Sau đó, hãy vào phần mềm quản lý danh mục đầu tư của bạn (ví dụ: Sparrow Wallet hoặc Liana) và nhập đường dẫn đến tệp cookie, thường nằm trong cùng thư mục với `Bitcoin.conf`, tùy thuộc vào hệ điều hành của bạn:

|**macOS**|~/Thư viện/Hỗ trợ ứng dụng/Bitcoin|

|---|---|

|**Windows**|%APPDATA%\Bitcoin|

|**Linux**|~/.Bitcoin|

![Image](assets/fr/35.webp)

Giữ nguyên các thông số khác theo mặc định, URL `127.0.0.1` và cổng `8332`, sau đó nhấp vào "*Kiểm tra kết nối*".

![Image](assets/fr/36.webp)

### Với nút điều khiển từ xa Bitcoin:

Nếu Bitcoin Knots được cài đặt trên một máy khác được kết nối với cùng một mạng, trước tiên hãy định vị tệp `Bitcoin.conf` trong số các tệp phần mềm. Nếu tệp này chưa tồn tại, bạn có thể tạo tệp đó. Mở tệp này bằng trình soạn thảo văn bản và thêm dòng sau:

```ini
server=1
```

Sau khi chỉnh sửa tệp, hãy đảm bảo bạn lưu tệp vào thư mục phù hợp với hệ điều hành của bạn:

|**macOS**|~/Thư viện/Hỗ trợ ứng dụng/Bitcoin|

|---|---|

|**Windows**|%APPDATA%\Bitcoin|

|**Linux**|~/.Bitcoin|

Hoạt động này cũng có thể được thực hiện thông qua đồ họa Interface của Bitcoin-QT. Vào menu "*Settings*", sau đó "*Options...*", và kích hoạt tùy chọn "*Enable RPC server*" bằng cách đánh dấu vào ô tương ứng. Nếu tệp `Bitcoin.conf` không tồn tại, bạn có thể tạo tệp trực tiếp từ Interface này bằng cách nhấp vào "*Open Configuration File*".

![Image](assets/fr/37.webp)

Tìm IP Address của máy lưu trữ Bitcoin Knots trên mạng cục bộ của bạn. Để thực hiện việc này, bạn có thể sử dụng một công cụ như [Angry IP Scanner](https://angryip.org/). Giả sử, để lập luận, IP Address của nút của bạn là `192.168.1.18`.

Trong tệp `Bitcoin.conf`, thêm các dòng sau, thiết lập `rpcbind=192.168.1.18` để khớp với IP Address của nút của bạn.

```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```

![Image](assets/fr/38.webp)

Ngoài ra, hãy thêm tên người dùng và mật khẩu cho các kết nối từ xa vào tệp `Bitcoin.conf`. Hãy đảm bảo thay thế `loic` bằng tên người dùng của bạn và `my_password` bằng mật khẩu mạnh:

```ini
rpcuser=loic
rpcpassword=my_password
```

![Image](assets/fr/39.webp)

Sau khi sửa đổi và lưu tệp, hãy khởi động lại Bitcoin Knots.

Bây giờ bạn có thể vào phần mềm quản lý danh mục đầu tư của mình (ví dụ: Sparrow Wallet hoặc Liana). Trên Sparrow, hãy vào tab "*User / Pass*". Nhập tên người dùng và mật khẩu bạn đã cấu hình trong tệp `Bitcoin.conf`. Để các tham số khác theo mặc định, tức là URL `127.0.0.1` và cổng `8332`. Sau đó nhấp vào "*Test Connection*".

![Image](assets/fr/40.webp)

Kết nối đã được thiết lập.

Bây giờ bạn đã biết tất cả về việc triển khai nút Bitcoin thay thế.

Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn để lại một ngón tay cái Green bên dưới. Hãy thoải mái chia sẻ nó trên mạng xã hội của bạn. Cảm ơn bạn rất nhiều!

Tôi cũng giới thiệu hướng dẫn khác này trong đó tôi giải thích cách thiết lập nút Lightning của riêng bạn:

https://planb.network/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a