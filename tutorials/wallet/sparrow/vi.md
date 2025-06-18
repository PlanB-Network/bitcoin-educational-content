---
name: Chim sẻ Wallet
description: Cài đặt, cấu hình và sử dụng Sparrow Wallet
---
![cover](assets/cover.webp)

Sparrow Wallet là phần mềm quản lý danh mục đầu tư Bitcoin tự quản do Craig Raw phát triển. Phần mềm nguồn mở này được những người chơi bitcoin đánh giá cao vì nhiều tính năng và Interface trực quan.

Có hai cách để sử dụng Sparrow:


- Giống như Hot Wallet, khóa riêng của bạn được lưu trữ trên PC.
- Với tư cách là người quản lý Cold Wallet, nơi các khóa riêng được lưu giữ trên Hardware Wallet. Ở chế độ này, Sparrow chỉ thao túng thông tin công khai của Wallet, theo dõi tiền, tạo địa chỉ và xây dựng giao dịch, nhưng chữ ký Hardware Wallet là bắt buộc để làm cho các giao dịch này hợp lệ. Do đó, nó có thể thay thế các ứng dụng như Ledger Live hoặc Trezor Suite.

Sparrow hỗ trợ ví đơn chữ ký và đa chữ ký, và cho phép quản lý linh hoạt nhiều ví. Ví dụ, bạn có thể đồng thời điều khiển một Wallet được kết nối với Ledger, một Wallet khác được kết nối với Trezor và cũng có Hot Wallet.

Phần mềm này cũng cung cấp các tính năng kiểm soát tiền tiên tiến, cho phép bạn chọn chính xác UTXO nào để sử dụng trong giao dịch của mình nhằm tối ưu hóa tính bảo mật.

Về mặt kết nối, Sparrow cho phép bạn kết nối với nút Bitcoin của riêng bạn, từ xa thông qua Electrum Server hoặc với Bitcoin Core. Bạn cũng có thể sử dụng nút công khai nếu bạn chưa có nút riêng. Kết nối từ xa được thực hiện thông qua Tor.

## Cài đặt Sparrow Wallet

Truy cập [trang tải xuống Sparrow Wallet chính thức](https://sparrowwallet.com/download/) và chọn phiên bản phần mềm tương ứng với hệ điều hành của bạn.

![Image](assets/fr/01.webp)

Điều quan trọng là phải kiểm tra tính toàn vẹn và tính xác thực của phần mềm trước khi cài đặt. Nếu bạn không biết cách thực hiện, bạn sẽ tìm thấy hướng dẫn đầy đủ tại đây:

https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Sau khi Sparrow được cài đặt, bạn có thể bỏ qua màn hình giải thích ban đầu và đi thẳng đến màn hình quản lý kết nối.

![Image](assets/fr/02.webp)

## Kết nối với mạng Bitcoin

Để tương tác với mạng Bitcoin và phát các giao dịch của bạn, Sparrow phải được kết nối với một nút Bitcoin. Có ba cách chính để thiết lập kết nối này:


- 🟡 Sử dụng một nút công khai, tức là kết nối với một nút của bên thứ ba cho phép các kết nối như vậy. Nếu bạn không có nút Bitcoin của riêng mình, tùy chọn này cho phép bạn bắt đầu sử dụng Sparrow một cách nhanh chóng. Tuy nhiên, nút mà bạn kết nối sẽ thấy tất cả các giao dịch của bạn, điều này có thể làm mất tính bảo mật của bạn. Kiểm soát được khóa của bạn là điều cần thiết, nhưng có nút riêng của bạn thậm chí còn tốt hơn. Vì vậy, chỉ sử dụng tùy chọn này nếu bạn mới bắt đầu, đồng thời nhận thức được những rủi ro đối với quyền riêng tư của bạn.
- 🟢 Kết nối với nút Bitcoin Core. Nếu bạn có nút Bitcoin Core của riêng mình, bạn có thể kết nối nó với Sparrow Wallet, cục bộ nếu Bitcoin Core được cài đặt trên cùng một máy hoặc từ xa.
- 🔵 Kết nối qua máy chủ Electrum. Nếu nút Bitcoin của bạn được trang bị Electrs, như trường hợp của các giải pháp node-in-a-box như Umbrel hoặc Start9, bạn có thể kết nối từ xa với nó từ Sparrow.

**Tốt hơn hết là sử dụng kết nối qua Electrs hoặc Bitcoin Core trên nút của riêng bạn để giảm nhu cầu tin tưởng bên thứ ba và tối ưu hóa tính bảo mật của bạn**

### Kết nối với một nút công khai 🟡

Kết nối với một nút công khai rất đơn giản. Nhấp vào tab "*Máy chủ công khai*".

![Image](assets/fr/03.webp)

Chọn một nút từ danh sách thả xuống.

![Image](assets/fr/04.webp)

Sau đó nhấp vào "*Kiểm tra kết nối*".

![Image](assets/fr/05.webp)

Sau khi kết nối, Sparrow Wallet sẽ hiển thị dấu tích màu vàng ở góc dưới bên phải của Interface để cho biết bạn đã kết nối với một nút công cộng.

![Image](assets/fr/06.webp)

### Kết nối với lõi Bitcoin 🟢

Phương pháp thứ hai để kết nối với một nút Bitcoin là liên kết Sparrow với một Bitcoin Core. Nếu Bitcoin Core được cài đặt trên cùng một máy, xác thực sẽ thông qua tệp cookie. Nếu Bitcoin Core nằm trên một máy từ xa, bạn sẽ cần sử dụng mật khẩu được xác định trong tệp `Bitcoin.conf`.

Xin lưu ý rằng nếu bạn sử dụng nút Bitcoin Core đã cắt tỉa, bạn sẽ không thể khôi phục Wallet chứa các giao dịch trước các khối được lưu trữ cục bộ. Tuy nhiên, đối với Wallet mới được tạo trên Sparrow, điều này sẽ không thành vấn đề: các giao dịch mới của bạn sẽ hiển thị, ngay cả với nút đã cắt tỉa.

Để cấu hình nút Bitcoin Core, bạn có thể tham khảo một trong các hướng dẫn sau, tùy thuộc vào hệ điều hành của bạn:

https://planb.network/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3

https://planb.network/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

Trên Sparrow, hãy chuyển đến tab "*Bitcoin Core*".

![Image](assets/fr/07.webp)

**Với Bitcoin Core cục bộ:**

Nếu Bitcoin Core được cài đặt trên máy tính của bạn, hãy tìm tệp `Bitcoin.conf` trong số các tệp phần mềm. Nếu tệp này không tồn tại, bạn có thể tạo tệp đó. Mở tệp đó bằng trình soạn thảo văn bản và chèn dòng sau:

```ini
server=1
```

Sau đó lưu lại thay đổi.

Bạn cũng có thể thực hiện việc này thông qua đồ họa Interface của Bitcoin-QT bằng cách điều hướng đến "*Cài đặt*" > "*Tùy chọn...*" và kích hoạt tùy chọn "*Bật máy chủ RPC*".

Đừng quên khởi động lại phần mềm sau khi thực hiện những thay đổi này.

![Image](assets/fr/08.webp)

Sau đó quay lại Sparrow Wallet và nhập đường dẫn đến tệp cookie của bạn, thường nằm trong cùng thư mục với `Bitcoin.conf`, tùy thuộc vào hệ điều hành của bạn:

| **macOS** | ~/Thư viện/Hỗ trợ ứng dụng/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

![Image](assets/fr/09.webp)

Giữ nguyên các thông số khác theo mặc định, URL `127.0.0.1` và cổng `8332`, sau đó nhấp vào "*Kiểm tra kết nối*".

![Image](assets/fr/10.webp)

Kết nối đã được thiết lập. Một dấu tích Green sẽ xuất hiện ở góc dưới bên phải để cho biết bạn đã kết nối với nút Bitcoin Core.

![Image](assets/fr/11.webp)

**Với điều khiển từ xa Bitcoin Core:**

Nếu Bitcoin Core được cài đặt trên một máy khác được kết nối với cùng một mạng, trước tiên hãy định vị tệp `Bitcoin.conf` trong số các tệp phần mềm. Nếu tệp này chưa tồn tại, bạn có thể tạo tệp đó. Mở tệp này bằng trình soạn thảo văn bản và thêm dòng sau:

```ini
server=1
```

Sau khi chỉnh sửa tệp, hãy đảm bảo bạn lưu tệp vào thư mục phù hợp với hệ điều hành của bạn:

| **macOS** | ~/Thư viện/Hỗ trợ ứng dụng/Bitcoin |

| ----------- | ------------------------------------- |

| **Windows** | %APPDATA%\Bitcoin |

| **Linux** | ~/.Bitcoin |

Hoạt động này cũng có thể được thực hiện thông qua Bitcoin-QT Interface đồ họa Interface. Vào menu "*Settings*", sau đó "*Options...*", và kích hoạt tùy chọn "*Enable RPC server*" bằng cách đánh dấu vào ô tương ứng. Nếu tệp `Bitcoin.conf` không tồn tại, bạn có thể tạo tệp trực tiếp từ Interface này bằng cách nhấp vào "*Open Configuration File*".

![Image](assets/fr/12.webp)

Tìm IP Address của máy lưu trữ Bitcoin Core trên mạng cục bộ của bạn. Để thực hiện việc này, bạn có thể sử dụng một công cụ như [Angry IP Scanner](https://angryip.org/). Giả sử, để lập luận, IP Address của nút của bạn là `192.168.1.18`.

Trong tệp `Bitcoin.conf`, thêm các dòng sau, thiết lập `rpcbind=192.168.1.18` để khớp với IP Address của nút của bạn.

```ini
[main]
rpcbind=127.0.0.1
rpcbind=192.168.1.18
rpcallowip=127.0.0.1
rpcallowip=192.168.1.0/24
```

![Image](assets/fr/13.webp)

Trong tệp `Bitcoin.conf`, hãy thêm tên người dùng và mật khẩu cho các kết nối từ xa. Hãy đảm bảo thay thế `loic` bằng tên người dùng của bạn và `my_password` bằng mật khẩu mạnh:

```ini
rpcuser=loic
rpcpassword=my_password
```

![Image](assets/fr/14.webp)

Sau khi sửa đổi và lưu tệp, hãy khởi động lại phần mềm Bitcoin-QT.

Bây giờ bạn có thể quay lại Sparrow Wallet. Đi đến tab "*User / Pass*". Nhập tên người dùng và mật khẩu bạn đã cấu hình trong tệp `Bitcoin.conf`. Để các tham số khác theo mặc định, tức là URL `127.0.0.1` và cổng `8332`. Sau đó nhấp vào "*Test Connection*".

![Image](assets/fr/15.webp)

Kết nối đã được thiết lập. Một dấu tích Green sẽ xuất hiện ở góc dưới bên phải để cho biết bạn đã kết nối với nút Bitcoin Core.

![Image](assets/fr/16.webp)

### Kết nối với máy chủ Electrum 🔵

Tùy chọn cuối cùng để kết nối là sử dụng máy chủ Electrum từ xa. Phương pháp này cho phép bạn kết nối với nút của mình qua Tor từ một thiết bị khác và tận dụng trình lập chỉ mục để duyệt danh mục đầu tư của bạn trên Sparrow nhanh hơn. Nó đặc biệt phù hợp nếu bạn có giải pháp nút trong hộp như Umbrel hoặc Start9, cho phép bạn cài đặt Electrs chỉ bằng một cú nhấp chuột.

Để thực hiện việc này, hãy lấy Tor `.onion' Address của máy chủ Electrum của bạn. Ví dụ, với Umbrel, bạn sẽ tìm thấy nó trong ứng dụng Electrs.

![Image](assets/fr/17.webp)

Trên Sparrow Wallet, truy cập vào tab "*Private Electrum*".

![Image](assets/fr/18.webp)

Nhập Tor Address của bạn vào ô trống được cung cấp. Các thiết lập khác có thể giữ nguyên mặc định. Sau đó nhấp vào "*Kiểm tra kết nối*".

![Image](assets/fr/19.webp)

Kết nối đã được xác nhận. Nếu bạn đóng cửa sổ này, một dấu tích màu xanh sẽ xuất hiện ở góc dưới bên phải, cho biết bạn đã kết nối với máy chủ Electrum.

![Image](assets/fr/20.webp)

## Tạo một danh mục đầu tư ấm áp

Bây giờ Sparrow Wallet đã được cấu hình để giao tiếp với mạng Bitcoin, bạn đã sẵn sàng để tạo Wallet đầu tiên của mình. Phần này hướng dẫn bạn cách tạo Hot Wallet, tức là Wallet có khóa riêng được lưu trữ trên máy tính của bạn. Vì máy tính của bạn là một máy phức tạp được kết nối với Internet, nên nó tạo ra một bề mặt tấn công rất lớn. Do đó, Hot Wallet chỉ nên được sử dụng cho số lượng bitcoin hạn chế. Để lưu trữ số lượng lớn hơn, hãy chọn Wallet an toàn với Hardware Wallet. Nếu đây là những gì bạn đang tìm kiếm, bạn có thể bỏ qua phần tiếp theo.

Để tạo Hot Wallet, từ màn hình chính Sparrow Wallet, nhấp vào tab "*File*" rồi nhấp vào "*New Wallet*".

![Image](assets/fr/21.webp)

Nhập tên cho danh mục đầu tư của bạn và nhấp vào "*Tạo Wallet*".

![Image](assets/fr/22.webp)

Ở đầu Interface, bạn có thể chọn tạo danh mục đầu tư "*Chữ ký đơn*" hoặc "*Chữ ký đa*". Ngay bên dưới, hãy chọn loại tập lệnh để khóa UTXO của bạn. Tôi khuyên bạn nên sử dụng tiêu chuẩn mới nhất: "*Taproot (P2TR)*".

![Image](assets/fr/23.webp)

Sau đó nhấp vào "*Software Wallet mới hoặc nhập khẩu*".

![Image](assets/fr/24.webp)

Chọn chuẩn BIP39 vì nó được hỗ trợ bởi hầu như tất cả các phần mềm danh mục đầu tư Bitcoin. Tiếp theo, chọn độ dài của cụm từ khôi phục. Hiện tại, cụm từ 12 từ là đủ vì cả hai đều cung cấp tính bảo mật tương tự, nhưng cụm từ 12 từ dễ lưu hơn.

![Image](assets/fr/25.webp)

Nhấp vào nút "*generate New*" để generate cụm từ Mnemonic của Wallet. Cụm từ này cung cấp quyền truy cập đầy đủ, không hạn chế vào tất cả bitcoin của bạn. Bất kỳ ai sở hữu cụm từ này đều có thể đánh cắp tiền của bạn, ngay cả khi không có quyền truy cập vật lý vào máy tính của bạn.

Cụm từ 12 từ này khôi phục quyền truy cập vào bitcoin của bạn trong trường hợp máy tính của bạn bị mất, bị trộm hoặc bị hỏng. Do đó, điều rất quan trọng là phải lưu trữ cẩn thận và cất giữ ở nơi an toàn.

Bạn có thể khắc nó trên giấy hoặc, để tăng thêm tính bảo mật, hãy khắc nó trên thép không gỉ để bảo vệ nó khỏi hỏa hoạn, lũ lụt hoặc sụp đổ. Lựa chọn phương tiện cho Mnemonic của bạn sẽ phụ thuộc vào chiến lược bảo mật của bạn, nhưng nếu bạn sử dụng Sparrow như một Wallet chi tiêu ấm áp chứa một lượng vừa phải, thì giấy sẽ đủ.

Để biết thêm thông tin về cách lưu và quản lý cụm từ Mnemonic của bạn, tôi thực sự khuyên bạn nên làm theo hướng dẫn khác này, đặc biệt nếu bạn là người mới bắt đầu:

https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

![Image](assets/fr/26.webp)

**Rõ ràng là bạn không bao giờ được chia sẻ những từ này trên Internet, như tôi đã làm trong hướng dẫn này. Ví dụ Wallet này sẽ chỉ được sử dụng trên Testnet và sẽ bị xóa vào cuối hướng dẫn.**

Bạn cũng có thể chọn thêm passphrase BIP39 bằng cách nhấp vào hộp "*Sử dụng passphrase*". Cảnh báo: sử dụng passphrase có thể rất hữu ích, nhưng nếu bạn không hiểu cách thức hoạt động của nó, nó có thể rất nguy hiểm. Đó là lý do tại sao tôi thực sự khuyên bạn nên đọc bài viết lý thuyết ngắn này về chủ đề này:

https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Sau khi lưu Mnemonic và bất kỳ passphrase nào vào phương tiện vật lý, hãy nhấp vào "*Xác nhận sao lưu*".

![Image](assets/fr/27.webp)

Nhập lại 12 từ của bạn để xác nhận rằng chúng đã được lưu chính xác, sau đó nhấp vào "*Tạo kho khóa*".

![Image](assets/fr/28.webp)

Sau đó nhấp vào "*Nhập kho khóa*" để generate nhập khóa danh mục đầu tư của bạn từ cụm từ Mnemonic.

![Image](assets/fr/29.webp)

Nhấp vào "*Áp dụng*" để hoàn tất việc tạo danh mục đầu tư.

![Image](assets/fr/30.webp)

Đặt mật khẩu mạnh để bảo mật quyền truy cập vào danh mục đầu tư Sparrow của bạn. Tốt nhất là bạn nên lưu mật khẩu này trong trình quản lý mật khẩu để không quên. Lưu ý rằng mật khẩu này không đóng vai trò gì trong việc tạo ra khóa của bạn. Nó chỉ được sử dụng để truy cập Wallet của bạn thông qua Sparrow Wallet. Vì vậy, ngay cả khi không có mật khẩu này, cụm từ Mnemonic của bạn vẫn đủ để truy cập bitcoin của bạn từ bất kỳ ứng dụng nào tương thích với BIP39.

![Image](assets/fr/31.webp)

Hot Wallet của bạn hiện đã được tạo. Bạn có thể bỏ qua phần *Nhận Bitcoin* của hướng dẫn này nếu bạn không có ý định sử dụng Hardware Wallet với Sparrow.

## Quản lý danh mục đầu tư Cold

Cách thứ hai để sử dụng Sparrow Wallet là thiết lập nó như một trình quản lý danh mục đầu tư với Hardware Wallet. Trong cấu hình này, khóa riêng của Bitcoin Wallet của bạn vẫn nằm độc quyền trên Hardware Wallet, trong khi Sparrow chỉ truy cập thông tin công khai. Cách tiếp cận này cung cấp mức độ bảo mật cao hơn so với ví Hot được thảo luận ở trên, vì khóa riêng được lưu giữ trên một thiết bị chuyên dụng, thường có chip an toàn, không được kết nối với Internet và do đó tạo ra bề mặt tấn công nhỏ hơn nhiều so với máy tính thông thường.

Có hai cách chính để kết nối Hardware Wallet với Sparrow:


- Bằng cáp, thường được sử dụng với các mẫu cơ bản như Trezor Safe 3 hoặc Ledger Nano S Plus;
- Ở chế độ Air-Gap, tức là không có kết nối có dây trực tiếp, thông qua thẻ MicroSD hoặc mã QR Exchange.

Sparrow hỗ trợ tất cả các phương thức giao tiếp này và tương thích với hầu hết các ví phần cứng trên thị trường.

Đối với hướng dẫn này, tôi sẽ sử dụng Ledger Nano S có cáp, nhưng quy trình tương tự ở chế độ Air-Gap. Bạn sẽ tìm thấy thông tin chi tiết cụ thể về Hardware Wallet của mình trong hướng dẫn chuyên sâu về Plan ₿ Network.

Trước khi bắt đầu, hãy đảm bảo rằng Wallet đã được cấu hình trên Hardware Wallet của bạn. Nếu bạn đang sử dụng kết nối có dây, hãy kết nối nó với máy tính qua cáp.

Để nhập cái gọi là "*Keystore*" (thông tin công khai cần thiết để quản lý danh mục đầu tư) vào Sparrow Wallet, hãy nhấp vào tab "*File*", sau đó nhấp vào "*New Wallet*".

![Image](assets/fr/32.webp)

Đặt tên cho danh mục đầu tư của bạn và nhấp vào "*Tạo Wallet*". Tôi khuyên bạn nên nhập tên Hardware Wallet của bạn để dễ dàng nhận dạng sau này.

![Image](assets/fr/33.webp)

Ở đầu Interface, hãy chọn giữa danh mục "*Chữ ký đơn*" hoặc "*Chữ ký đa*". Đối với ví dụ của chúng tôi, chúng tôi sẽ cấu hình danh mục chữ ký đơn.

Ngay bên dưới, hãy chọn loại tập lệnh để khóa UTXO của bạn. Nếu Hardware Wallet của bạn hỗ trợ, tôi khuyên bạn nên chọn "*Taproot (P2TR)*".

![Image](assets/fr/34.webp)

Tiếp theo, quy trình sẽ khác nhau tùy theo phương pháp kết nối của bạn. Nếu bạn đang sử dụng phương pháp Air-Gap, hãy chọn "*Airgapped Hardware Wallet*". Sau đó làm theo hướng dẫn dành riêng cho thiết bị của bạn.

![Image](assets/fr/35.webp)

Nếu bạn đang sử dụng kết nối cáp, như trong trường hợp của tôi, hãy chọn "*Đã kết nối Hardware Wallet*".

![Image](assets/fr/36.webp)

Nhấp vào "*Quét*" để Sparrow phát hiện thiết bị của bạn. Đảm bảo rằng thiết bị được cắm vào và mở khóa. Đối với một số kiểu máy, chẳng hạn như Ledger, bạn sẽ cần mở ứng dụng "*Bitcoin*" để bật chức năng phát hiện.

![Image](assets/fr/37.webp)

Chọn "*Nhập kho khóa*".

![Image](assets/fr/38.webp)

Nhấp vào "*Áp dụng*" để hoàn tất việc tạo danh mục đầu tư.

![Image](assets/fr/39.webp)

Đặt mật khẩu mạnh để bảo mật quyền truy cập vào Sparrow Wallet của bạn. Mật khẩu này sẽ bảo vệ khóa công khai, địa chỉ và lịch sử giao dịch của bạn. Chúng tôi khuyên bạn nên lưu nó trong trình quản lý mật khẩu. Lưu ý rằng mật khẩu này không đóng vai trò gì trong việc tạo ra khóa của bạn. Ngay cả khi không có nó, bạn vẫn có thể khôi phục quyền truy cập vào bitcoin của mình bằng Mnemonic thông qua bất kỳ phần mềm nào tương thích với BIP39.

![Image](assets/fr/40.webp)

Danh mục quản lý của bạn hiện đã được cấu hình trên Sparrow.

![Image](assets/fr/41.webp)

## Nhận bitcoin

Bây giờ Wallet của bạn đã được thiết lập trên Sparrow, bạn có thể nhận bitcoin. Chỉ cần truy cập menu "*Nhận*".

![Image](assets/fr/42.webp)

Sparrow sẽ hiển thị Address chưa sử dụng đầu tiên trong Wallet của bạn. Bạn có thể thêm "*Nhãn*" vào Address này để nhắc nhở bạn về nguồn gốc của những satoshi này trong tương lai.

![Image](assets/fr/43.webp)

Nếu bạn đang sử dụng Hot Wallet, bạn có thể sử dụng Address được hiển thị ngay lập tức bằng cách sao chép hoặc quét mã QR liên quan.

Nếu bạn đang sử dụng Hardware Wallet, điều rất quan trọng là phải kiểm tra Address trên màn hình thiết bị trước khi sử dụng. Đối với các thiết bị có dây, hãy kết nối và mở khóa Hardware Wallet của bạn, sau đó trong Sparrow, nhấp vào "*Hiển thị Address*". Đảm bảo rằng Address hiển thị trên Hardware Wallet của bạn khớp với Address hiển thị trên Sparrow.

![Image](assets/fr/44.webp)

Đối với người dùng Hardware Wallet Air-Gap, xác minh Address thay đổi tùy theo kiểu máy. Xem hướng dẫn Plan ₿ Network chuyên dụng để biết hướng dẫn chính xác.

Sau khi giao dịch được người trả tiền phát sóng, bạn sẽ thấy giao dịch đó xuất hiện trong tab "*Giao dịch*". Bạn có thể nhấp vào đó để biết thêm chi tiết, chẳng hạn như txid.

![Image](assets/fr/45.webp)

Trong tab "*Địa chỉ*", bạn sẽ thấy danh sách tất cả các địa chỉ hộp thư đến của mình. Bạn có thể xem liệu chúng đã được sử dụng hay chưa và liệu có nhãn nào được thêm vào hay không. Địa chỉ *Nhận*" là những địa chỉ mà Sparrow hiển thị khi bạn nhấp vào "*Nhận*" và dành cho các khoản thanh toán đến. Địa chỉ "*Thay đổi*" được sử dụng cho Exchange trong các giao dịch của bạn, tức là để khôi phục phần UTXO chưa sử dụng của bạn trong các mục nhập.

![Image](assets/fr/46.webp)

Tab "*UTXOs*" hiển thị tất cả UTXO của bạn, tức là các mảnh Bitcoin mà bạn giữ. Bạn có thể thấy số lượng của mỗi UTXO và nhãn liên quan.

![Image](assets/fr/47.webp)

## Gửi bitcoin

Bây giờ bạn đã có một vài satoshi trong Wallet, bạn cũng có tùy chọn gửi một số. Mặc dù có một số cách để thực hiện việc này, tôi khuyên bạn nên sử dụng menu "*UTXOs*" để kiểm soát chính xác hơn số tiền bạn chi tiêu (*coin control*), thay vì trực tiếp vào menu "*Send*" (mặc dù cách sau có thể đủ nếu bạn là người mới bắt đầu).

![Image](assets/fr/48.webp)

Chọn UTXO bạn muốn sử dụng làm đầu vào cho giao dịch này, sau đó nhấp vào "*Gửi mục đã chọn*". Cách tiếp cận này cho phép bạn chọn các nguồn phù hợp nhất trong số các UTXO của mình, theo chi phí của bạn và các nhãn được áp dụng khi chúng được nhận, để tối ưu hóa tính bảo mật của các khoản thanh toán của bạn. Đảm bảo rằng tổng số UTXO đã chọn lớn hơn số tiền bạn muốn gửi.

![Image](assets/fr/49.webp)

Nhập Address của người nhận vào trường "*Pay to*". Bạn cũng có thể quét Address bằng webcam của mình bằng cách nhấp vào biểu tượng camera. Nút "*+Add*" cho phép bạn thanh toán nhiều địa chỉ trong một giao dịch.

![Image](assets/fr/50.webp)

Thêm nhãn vào giao dịch của bạn để nhắc nhở bạn về mục đích của giao dịch. Nhãn này cũng sẽ được liên kết với Exchange cuối cùng của bạn.

![Image](assets/fr/51.webp)

Nhập số tiền cần gửi tới Address này.

![Image](assets/fr/52.webp)

Điều chỉnh mức phí theo điều kiện thị trường hiện tại. Bạn có thể thực hiện bằng cách nhập giá trị phí tuyệt đối hoặc điều chỉnh mức phí bằng thanh trượt.

![Image](assets/fr/53.webp)

Ở cuối Interface, bạn có thể chọn giữa "*Hiệu quả*" và "*Quyền riêng tư*". Trong trường hợp của tôi, tùy chọn "*Quyền riêng tư*" không khả dụng vì tôi chỉ có một UTXO trong danh mục đầu tư này. "*Hiệu quả*" tương ứng với một giao dịch cổ điển, trong khi "*Quyền riêng tư*" là một giao dịch kiểu Stonewall, một cấu trúc giao dịch củng cố tính bảo mật của bạn bằng cách mô phỏng một mini-CoinJoin, giúp phân tích chuỗi phức tạp hơn.

![Image](assets/fr/54.webp)

Sparrow hiển thị sơ đồ tóm tắt cho thấy đầu vào, đầu ra và phí giao dịch của bạn (lưu ý rằng phí thực tế không phải là đầu ra, trái ngược với những gì sơ đồ này gợi ý). Nếu bạn hài lòng với mọi thứ, hãy nhấp vào "*Tạo giao dịch*".

![Image](assets/fr/55.webp)

Thao tác này sẽ đưa bạn đến trang nêu chi tiết Elements của giao dịch của bạn. Kiểm tra xem tất cả thông tin đã chính xác chưa, sau đó nhấp vào "*Hoàn tất giao dịch để ký*".

![Image](assets/fr/56.webp)

Điều quan trọng là phải giữ nguyên Sighash mặc định. Để hiểu lý do, hãy xem khóa đào tạo này, trong đó tôi giải thích mọi thứ bạn cần biết về Sighash:

https://planb.network/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f

Trên màn hình tiếp theo, các tùy chọn sẽ khác nhau tùy theo loại Wallet bạn đang sử dụng:


- Đối với Hardware Wallet Air-Gap, hãy nhấp vào "*Show QR*" để hiển thị PSBT mà bạn có thể ký bằng thiết bị của mình, sau đó tải PSBT đã ký vào Sparrow bằng cách sử dụng "*Scan QR*". Tùy chọn "*Save Transaction*" hoạt động theo cách tương tự, nhưng với các giao dịch trên thẻ nhớ microSD;
- Đối với Hot Wallet, chỉ cần nhấp vào "*Ký*" và nhập mật khẩu Wallet để ký;
- Đối với Hardware Wallet có dây, hãy nhấp vào "*Ký*" để gửi giao dịch chưa ký đến thiết bị của bạn.

![Image](assets/fr/57.webp)

Trên Hardware Wallet của bạn, hãy kiểm tra Address của người nhận, số tiền đã gửi và các khoản phí. Nếu mọi thứ đều chính xác, hãy tiến hành ký tên.

Sau khi giao dịch được ký, nó sẽ xuất hiện lại trong Sparrow, sẵn sàng để phát trên mạng Bitcoin để đưa vào khối tiếp theo. Nếu mọi thứ đều chính xác, hãy nhấp vào "*Phát giao dịch*".

![Image](assets/fr/58.webp)

Giao dịch của bạn hiện đã được phát và đang chờ xác nhận.

![Image](assets/fr/59.webp)

## Quản lý và cấu hình danh mục đầu tư trên Sparrow

Trong tab "*Cài đặt*", bạn sẽ tìm thấy thông tin chi tiết về danh mục đầu tư của mình, chẳng hạn như:


- Loại danh mục đầu tư (chữ ký đơn hoặc multi-sig);
- Loại tập lệnh được sử dụng;
- Tên bạn đã gán cho danh mục đầu tư;
- Dấu ấn chìa khóa chính;
- Đường vòng;
- Khóa công khai mở rộng của tài khoản.

![Image](assets/fr/60.webp)

Nút "*Xuất*" cho phép bạn xuất thông tin danh mục đầu tư của mình để có thể sử dụng trong phần mềm khác trong khi vẫn giữ nguyên thông tin được thiết lập trong Sparrow.

Nút "*Thêm tài khoản*" cho phép bạn thêm một tài khoản bổ sung vào danh mục đầu tư của mình. Một tài khoản tương ứng với một tập hợp các địa chỉ hộp thư đến riêng biệt. Tính năng này có thể hữu ích, ví dụ, nếu bạn muốn tách một tài khoản cá nhân và một tài khoản doanh nghiệp, bằng một cụm từ Mnemonic duy nhất.

Nút "*Nâng cao*" cho phép truy cập vào các cài đặt nâng cao, chẳng hạn như tùy chỉnh tìm kiếm Address của Sparrow và thay đổi mật khẩu danh mục đầu tư.

![Image](assets/fr/61.webp)

Khi bạn đóng Sparrow Wallet, Wallet của bạn sẽ tự động khóa. Lần sau khi bạn mở phần mềm, một cửa sổ sẽ nhắc bạn mở khóa Wallet bằng mật khẩu của nó.

![Image](assets/fr/62.webp)

Nếu cửa sổ này không mở hoặc nếu bạn muốn mở một danh mục đầu tư khác trên Sparrow, hãy nhấp vào tab "*File*" và chọn "*Open Wallet*".

![Image](assets/fr/63.webp)

Thao tác này sẽ mở File Manager của bạn đến thư mục nơi Sparrow lưu trữ ví của bạn. Chỉ cần chọn Wallet mà bạn muốn mở và nhập mật khẩu để mở khóa.

![Image](assets/fr/64.webp)

Trong menu "*File*" bên dưới "*Settings*", bạn sẽ tìm thấy các thông số kết nối mạng Bitcoin đã được khám phá trong các phần trước. Bạn cũng có thể điều chỉnh nhiều thông số khác nhau như đơn vị được sử dụng, tiền tệ fiat để chuyển đổi và nguồn thông tin.

![Image](assets/fr/65.webp)

Tab "*Xem*" cung cấp các tùy chọn tùy chỉnh và quyền truy cập vào một số lệnh hữu ích, chẳng hạn như "*Làm mới Wallet*", giúp làm mới tìm kiếm giao dịch cho danh mục đầu tư của bạn.

![Image](assets/fr/66.webp)

Tab "*Công cụ*" nhóm lại một số công cụ nâng cao, bao gồm:


- "*Ký/Xác minh tin nhắn*" cho phép bạn chứng minh quyền sở hữu của người nhận Address hoặc xác minh chữ ký.
- "*Gửi đến nhiều*" cung cấp Interface được đơn giản hóa để thực hiện giao dịch đến nhiều địa chỉ nhận cùng lúc, rất thuận tiện cho việc chi tiêu theo đợt.
- "*Sweep Private Key*" cho phép bạn lấy bitcoin được bảo mật bằng khóa riêng đơn giản và chuyển chúng vào Sparrow Wallet của bạn. Điều này có thể đặc biệt hữu ích đối với những người có bitcoin từ đầu những năm 2010, trước thời đại của ví HD.
- "Xác minh tải xuống" xác minh tính toàn vẹn và xác thực của phần mềm đã tải xuống trước khi cài đặt vào thiết bị của bạn.
- "*Khởi động lại*" cho phép bạn chuyển sang ví của mình trên mạng Testnet hoặc Signet. Điều này có thể hữu ích nếu bạn muốn truy cập vào mạng thử nghiệm với các đồng tiền không có giá trị thực.

![Image](assets/fr/67.webp)

Bây giờ bạn đã biết tất cả về phần mềm Sparrow Wallet, một công cụ tuyệt vời để quản lý danh mục đầu tư Bitcoin của bạn hàng ngày.

Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn để lại một ngón tay cái Green bên dưới. Hãy thoải mái chia sẻ nó trên mạng xã hội của bạn. Cảm ơn bạn rất nhiều!

Tôi cũng giới thiệu hướng dẫn khác này trong đó tôi giải thích cách cấu hình Hardware Wallet COLDCARD Q với Sparrow Wallet:

https://planb.network/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3