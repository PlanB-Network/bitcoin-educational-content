---
name: Trung tâm Alby
description: Làm thế nào để dễ dàng khởi chạy nút Lightning của riêng bạn?
---
![cover](assets/cover.webp)

Alby Hub là phần mềm mã nguồn mở mới nhất của Alby, công ty đứng sau tiện ích mở rộng web Lightning phổ biến. Alby Hub là Wallet tự quản lý với nút Lightning dễ sử dụng nhất, có thể truy cập từ mọi nơi để tích hợp với hàng chục ứng dụng. Alby Hub là Interface dễ sử dụng để quản lý các nút Lightning.

Trong hướng dẫn này, chúng ta sẽ xem xét các cách khác nhau để sử dụng Alby Hub, cách kết nối nó với Alby Go, ứng dụng di động của Alby hoặc Tiện ích mở rộng trình duyệt Alby. Điều này sẽ cho phép bạn sử dụng Sats khi di chuyển trong khi vẫn tự chủ trong việc quản lý nút của mình.

![ALBY HUB](assets/fr/01.webp)

## Alby Hub là gì?

Alby Hub được thiết lập để trở thành công cụ chủ lực mới trong hệ sinh thái Alby. Phần mềm này cho phép người dùng dễ dàng quản lý Wallet tự lưu giữ của riêng họ bằng một nút Lightning tích hợp, trong khi vẫn giữ lại Ownership của khóa của họ (tự lưu giữ).

Alby Hub là một công cụ có khả năng thích ứng cao. Nó có thể đáp ứng nhu cầu của cả người mới bắt đầu và người dùng nâng cao. Người mới sẽ sử dụng nó để dễ dàng vận hành một nút Lightning thực sự của riêng họ, mà không phải giải quyết sự phức tạp cơ bản. Đối với những người dùng có kinh nghiệm hơn, Alby Hub có thể được sử dụng như một Interface hoàn chỉnh để quản lý nâng cao một nút Lightning hiện có.

Tùy thuộc vào nhu cầu của bạn, Alby Hub có 4 cấu hình:


- Alby Hub Đám mây :**

Lý tưởng cho người mới bắt đầu, tùy chọn đầu tiên này là tùy chọn đám mây Alby. Nó cho phép bạn triển khai Hub trực tiếp trên máy chủ do Alby quản lý, có thể truy cập thông qua Alby Hub Interface của bạn. Mặc dù Alby quản lý máy chủ, nhưng bạn vẫn giữ được quyền tối cao đối với tiền của mình vì khóa của bạn được mã hóa bằng mật khẩu chỉ bạn biết. Tuy nhiên, khóa của bạn phải được giải mã trong RAM để nút hoạt động, về mặt lý thuyết, điều này sẽ khiến chúng gặp rủi ro nếu ai đó truy cập vật lý vào máy chủ. Đây là một sự thỏa hiệp thú vị cho người mới bắt đầu, nhưng điều quan trọng là phải nhận thức được những rủi ro.

Ưu điểm chính của tùy chọn này là bạn có thể thiết lập và chạy một nút Lightning 24/7 mà không cần phải tự quản lý lưu trữ. Hơn nữa, việc sao lưu nút Lightning của bạn được đơn giản hóa và tự động hóa, so với các tùy chọn tự lưu trữ mà bạn phải tự quản lý sao lưu kênh.

Alby Cloud là dịch vụ trả phí [Kiểm tra giá của họ](https://albyhub.com/#pricing) để biết thêm chi tiết. Phí được tự động khấu trừ từ Wallet của bạn thông qua Lightning Invoice do Alby phát hành. Điều này được thực hiện thông qua kết nối NWC cấu hình nút của bạn để tự động thanh toán hóa đơn Alby liên quan đến đăng ký của bạn.


- Alby Hub có một nút hiện có :**

Nếu bạn đã có một nút được lưu trữ, ví dụ trên Umbrel hoặc Start9, Alby Hub có thể được sử dụng làm Interface quản lý nâng cao, tương tự như ThunderHub hoặc RTL.


- Alby Hub địa phương :**

Bạn cũng có thể cài đặt Alby Hub trực tiếp trên PC của mình, mặc dù tùy chọn này ít thực tế hơn vì PC của bạn phải luôn hoạt động để truy cập từ xa vào nút Lightning. Tuy nhiên, giải pháp thay thế này có thể phù hợp với nhu cầu cụ thể của bạn.


- Alby Hub trên máy chủ cá nhân :**

Đối với người dùng nâng cao, Alby Hub có thể được triển khai trên máy chủ cá nhân chỉ bằng một lệnh đơn giản. Tùy chọn này không được đề cập trong hướng dẫn này, nhưng bạn có thể tìm thấy hướng dẫn chuyên dụng [trên GitHub của Alby](https://github.com/getAlby/hub?tab=readme-ov-file#docker).

Hướng dẫn này tập trung chủ yếu vào Interface, sẽ giống nhau bất kể tùy chọn nào được chọn. Chúng tôi cũng sẽ xem cách triển khai Alby Hub với tùy chọn đám mây trả phí, sau đó với tùy chọn node-in-box (Umbrel hoặc Start9).

![ALBY HUB](assets/fr/02.webp)

Để cài đặt cục bộ trên PC của bạn, hãy [tải xuống và cài đặt phần mềm theo hệ điều hành của bạn](https://github.com/getAlby/hub/releases), sau đó làm theo các hướng dẫn tương tự trên Interface.

![ALBY HUB](assets/fr/03.webp)

## Tạo tài khoản Alby

Bước đầu tiên là tạo một tài khoản Alby. Mặc dù điều này không cần thiết để sử dụng Alby Hub, nhưng nó cho phép bạn tận dụng tối đa các tùy chọn có sẵn, bao gồm khả năng có được Lightning Address.

Truy cập [trang web chính thức của Alby](https://getalby.com/) và nhấp vào nút "*Tạo tài khoản*".

![ALBY HUB](assets/fr/04.webp)

Nhập biệt danh và email Address, sau đó nhấp vào "*Đăng ký*". Email Address này sẽ được sử dụng để đăng nhập vào tài khoản của bạn sau này.

![ALBY HUB](assets/fr/05.webp)

Nhập mã xác minh bạn nhận được qua email.

![ALBY HUB](assets/fr/06.webp)

Sau khi đăng nhập vào tài khoản trực tuyến của bạn, hãy nhấp vào nút "*Tiếp tục*".

![ALBY HUB](assets/fr/07.webp)

Nhấp vào "*Tiếp tục*" một lần nữa.

![ALBY HUB](assets/fr/08.webp)

## Tùy chọn lưu trữ đám mây

Sau đó, bạn sẽ phải chọn giữa tùy chọn tự lưu trữ, nơi bạn cài đặt Alby Hub trên thiết bị của mình hoặc tùy chọn cao cấp. Tôi sẽ bắt đầu bằng cách giải thích cách tiến hành với tùy chọn Pro Cloud (lưu ý rằng đây là tùy chọn trả phí, hãy xem chi tiết ở phần trước).

Nhấp vào "*Nâng cấp*".

![ALBY HUB](assets/fr/09.webp)

Xác nhận bằng cách nhấp vào "*Đăng ký ngay*".

![ALBY HUB](assets/fr/10.webp)

Nhấp vào "*Khởi chạy Alby Hub*".

![ALBY HUB](assets/fr/11.webp)

Chờ một vài phút để nút của bạn được tạo.

![ALBY HUB](assets/fr/12.webp)

Và thế là xong, Alby Hub của bạn đã được cấu hình. Trong phần tiếp theo, tôi sẽ chỉ cho bạn cách cài đặt Alby Hub trên một node hiện có. Nếu bạn chưa có node lightning, bạn có thể bỏ qua phần tiếp theo để cấu hình Alby Hub trên Alby Cloud.

![ALBY HUB](assets/fr/13.webp)

## Tùy chọn tự lưu trữ

Nếu bạn muốn sử dụng Alby Hub như một Interface cho nút Lightning hiện tại của mình, bạn có một số tùy chọn: cài đặt trên máy chủ, cục bộ trên máy tính của bạn hoặc thông qua một nút trong hộp (Umbrel hoặc Start9). Sử dụng Alby Hub trong các cấu hình này là miễn phí. Chúng ta sẽ tập trung vào tùy chọn nút trong hộp, vì tôi thấy rằng tùy chọn máy chủ, không có quyền truy cập vật lý, có những rủi ro tương tự như phiên bản đám mây và cài đặt cục bộ trên PC thường không phù hợp.

Để thiết lập trên Umbrel (các bước thực hiện trên Start9 giống hệt), trước tiên bạn phải cấu hình sẵn một nút LND.

Đăng nhập vào Umbrel Interface của bạn và vào cửa hàng ứng dụng.

![ALBY HUB](assets/fr/14.webp)

Tìm ứng dụng "*Alby Hub*".

![ALBY HUB](assets/fr/15.webp)

Cài đặt nó trên nút của bạn.

![ALBY HUB](assets/fr/16.webp)

Alby Hub Interface của bạn hiện đã sẵn sàng. Bạn có thể làm theo phần còn lại của hướng dẫn như thể bạn đang sử dụng đám mây Interface, nhưng không có các tùy chọn của phiên bản trả phí. Hơn nữa, không giống như phiên bản đám mây, khóa của bạn được lưu trữ cục bộ trên nút của bạn, không phải trên máy chủ của Alby.

![ALBY HUB](assets/fr/17.webp)

## Ra mắt Alby Hub

Nhấp vào nút "*Bắt đầu*".

![ALBY HUB](assets/fr/18.webp)

Alby Hub sau đó sẽ nhắc bạn chọn mật khẩu. Mật khẩu này rất quan trọng vì nó sẽ được sử dụng để mã hóa Wallet của bạn. Trong phiên bản đám mây trả phí, khóa của bạn được lưu trữ trên máy chủ Alby, được mã hóa bằng mật khẩu này mà chỉ bạn biết, sau đó được giải mã và chỉ lưu trữ trong RAM để ký giao dịch khi cần thiết.

Do đó, điều cần thiết là phải chọn một mật khẩu mạnh. Bất kỳ ai có mật khẩu này đều có khả năng truy cập vào nút của bạn. Đảm bảo bạn cũng tạo một hoặc nhiều bản sao lưu vật lý của mật khẩu này trên một tờ giấy hoặc tốt hơn nữa là trên một miếng kim loại để tăng thêm tính bảo mật.

Sau khi bạn đã chọn và lưu mật khẩu cẩn thận, hãy nhấp vào "*Tạo mật khẩu*".

![ALBY HUB](assets/fr/19.webp)

Bây giờ bạn có thể truy cập vào nút Lightning của mình.

![ALBY HUB](assets/fr/20.webp)

Hành động đầu tiên cần thực hiện là lưu cụm từ khôi phục của bạn, từ đó các khóa của bạn được lấy ra. Để thực hiện việc này, hãy nhấp vào "Cài đặt". Cụm từ này cho phép bạn khôi phục quyền truy cập vào Wallet của mình nếu bạn đã bật sao lưu tự động.

![ALBY HUB](assets/fr/21.webp)

Sau đó, hãy chuyển đến tab "*Sao lưu*". Nhập mật khẩu của bạn để truy cập.

![ALBY HUB](assets/fr/22.webp)

Sau đó, bạn sẽ có quyền truy cập vào cụm từ khôi phục gồm 12 từ của mình. Tạo một hoặc nhiều bản sao lưu vật lý của cụm từ này trên giấy hoặc kim loại và lưu trữ ở nơi an toàn.

![ALBY HUB](assets/fr/23.webp)

Sau khi lưu cụm từ, hãy đánh dấu vào ô để xác nhận rằng bạn đã lưu cụm từ đó và nhấp vào "*Tiếp tục*".

![ALBY HUB](assets/fr/24.webp)

## Làm thế nào tôi có thể khôi phục quyền truy cập vào bitcoin của mình?

Trước khi gửi tiền đến Alby Hub của bạn, điều quan trọng là phải hiểu cách khôi phục tiền trong trường hợp có sự cố, cũng như thông tin nào là cần thiết cho quá trình khôi phục này. Quy trình thay đổi tùy theo bản chất của số tiền cần khôi phục và chế độ lưu trữ của nút của bạn.

Đối với người dùng đám mây trả phí, việc khôi phục hoàn toàn số bitcoin của bạn cần có ba Elements thiết yếu:


- Cụm từ phục hồi của bạn;
- Truy cập vào tài khoản Alby của bạn để lấy bản sao lưu tự động.

Việc thiếu bất kỳ thông tin nào trong 2 thông tin này sẽ khiến bạn không thể khôi phục toàn bộ số bitcoin của mình.

Đối với những người chạy Alby Hub trên thiết bị của riêng họ, quy trình khôi phục được ghi lại [tại đây](https://guides.getalby.com/user-guide/alby-account-and-browser-extension/alby-hub/backups-and-recover#alby-hub-self-hosted-with-an-alby-account).

Nếu bạn đã cài đặt Alby Hub trên một nút hiện có, bạn sẽ cần phải làm theo quy trình khôi phục của hệ điều hành nút cụ thể đó. Ví dụ: Umbrel cung cấp [một tùy chọn](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) để mã hóa trạng thái mới nhất của các kênh Lightning của bạn và lưu nó một cách động và ẩn danh qua Tor. Hãy lưu ý rằng chỉ các bản sao lưu tự động từ Alby mới cho phép bạn khôi phục hoàn toàn Hub của mình mà không cần đóng bất kỳ kênh nào.

## Mua kênh Lightning đầu tiên của bạn

Bây giờ bạn có thể làm theo hướng dẫn do Alby Hub cung cấp. Nhấp vào nút để mở kênh đầu tiên của bạn để nhận tiền mặt.

![ALBY HUB](assets/fr/25.webp)

Chọn "*Mở kênh*". Nếu bạn không có ý định trở thành nút định tuyến và không thực sự cần nút này, tôi khuyên bạn nên chọn kênh riêng.

![ALBY HUB](assets/fr/26.webp)

Alby Hub sẽ generate và Invoice để bạn thanh toán. Khoản thanh toán này bao gồm phí giao dịch cần thiết để mở kênh của bạn, cũng như phí dịch vụ của LSP (*Nhà cung cấp dịch vụ Lightning*) sẽ mở kênh đến nút của bạn, cho phép bạn nhận thanh toán ngay lập tức.

![ALBY HUB](assets/fr/27.webp)

Sau khi Invoice được thanh toán và giao dịch được xác nhận, kênh Lightning đầu tiên của bạn sẽ được thiết lập.

![ALBY HUB](assets/fr/28.webp)

Trong tab "*Node*", bạn có thể thấy rằng hiện tại bạn đã có tiền mặt đến, cho phép bạn nhận thanh toán qua Lightning.

![ALBY HUB](assets/fr/29.webp)

Để nhận thanh toán, hãy nhấp vào tab "*Wallet*" rồi nhấp vào "*Nhận*".

![ALBY HUB](assets/fr/30.webp)

Nhập số tiền và thêm mô tả nếu cần, sau đó nhấp vào "*Tạo Invoice*".

![ALBY HUB](assets/fr/31.webp)

Tôi đã nhận được khoản thanh toán đầu tiên là 120.000 Sats.

![ALBY HUB](assets/fr/32.webp)

Bằng cách quay lại tab "*Wallet*", bạn có thể kiểm tra số dư Wallet của mình. Lưu ý rằng Alby Hub tự động dành riêng 354 Sats khi bạn thực hiện khoản thanh toán đầu tiên. Đối với mỗi kênh Lightning bạn mở sau đó, Alby Hub sẽ tự động dành riêng một khoản dự trữ tương đương với 1% dung lượng của kênh. Khoản dự trữ này là biện pháp bảo mật cho phép nút của bạn khôi phục tiền của kênh trong trường hợp có hành vi gian lận của đối tác. Đó là lý do tại sao, mặc dù tôi đã gửi 120.000 Sats, nhưng chỉ có 119.646 Sats được hiển thị trên số dư của tôi.

![ALBY HUB](assets/fr/33.webp)

## Gửi bitcoin trên chuỗi

Nếu bạn muốn có tiền mặt để thanh toán, bạn cũng có thể tự mở kênh. Để làm như vậy, bạn sẽ cần bitcoin onchain trong Wallet của mình.

Từ tab "*Node*", nhấp vào "*Deposit*".

![ALBY HUB](assets/fr/34.webp)

Gửi bitcoin đến Address được hiển thị. Address này được lấy từ cụm từ khôi phục đã lưu trước đó của bạn.

![ALBY HUB](assets/fr/35.webp)

Tôi đã gửi 72.000 Sats. Bây giờ chúng có thể nhìn thấy trong "*Số dư tiết kiệm*", bao gồm tất cả các khoản tiền tôi sở hữu trên blockchain, chứ không phải trên Lightning.

![ALBY HUB](assets/fr/36.webp)

## Mở kênh Lightning

Bây giờ bạn đã có tiền trên chuỗi, bạn có thể mở một kênh Lightning mới. Nên mở nhiều kênh, với số tiền đủ để đảm bảo bạn luôn có thể thanh toán mà không bị ràng buộc. Hầu hết các LSP (*Nhà cung cấp dịch vụ Lightning*) yêu cầu tối thiểu 150.000 Sats để mở một kênh với bạn.

Trong tab "*Node*", nhấp vào "*Open Channel*".

![ALBY HUB](assets/fr/37.webp)

Chọn kích thước kênh của bạn. Tôi khuyên bạn không nên mở các kênh quá nhỏ, lưu ý rằng đây là nút Lightning và máy lưu trữ khóa của bạn không cung cấp cùng mức độ bảo mật như Hardware Wallet. Vì vậy, hãy cẩn thận với số lượng bạn chọn chặn.

![ALBY HUB](assets/fr/38.webp)

Trong menu "*Tùy chọn nâng cao*", bạn có thể chọn LSP để mở kênh của mình hoặc nhập thủ công một nút Lightning khác.

![ALBY HUB](assets/fr/39.webp)

Sau đó nhấp vào "*Mở kênh*".

![ALBY HUB](assets/fr/40.webp)

Chờ cho kênh của bạn được xác nhận trên chuỗi.

![ALBY HUB](assets/fr/41.webp)

Kênh mới của bạn bây giờ sẽ xuất hiện trong tab "*Node*".

![ALBY HUB](assets/fr/42.webp)

## Quản lý nút

Quản lý các kênh Lightning của bạn dễ hơn bạn nghĩ. Alby Hub cho phép bạn chuyển Sats giữa số dư chi tiêu và số dư On-Chain của bạn. Đó là cách bạn có thể tăng khả năng chi tiêu hoặc nhận.

![ALBY HUB](assets/fr/66.webp)

## Kết nối một ứng dụng chi phí

Bây giờ bạn đã có một nút Lightning đang hoạt động, bạn có thể sử dụng nó để nhận và chi tiêu Sats hàng ngày. Mặc dù web Interface của Alby Hub rất tiện lợi để quản lý nút của bạn, nhưng nó không lý tưởng để thực hiện các giao dịch nhanh khi đang di chuyển. Đối với điều này, chúng ta sẽ sử dụng ứng dụng Lightning Wallet được cài đặt trên điện thoại thông minh của mình.

Trong hướng dẫn này, tôi khuyên bạn nên chọn Alby Go, một ứng dụng rất dễ sử dụng, nhưng bạn cũng có thể sử dụng các ứng dụng tương thích khác như Zeus.

![ALBY HUB](assets/fr/43.webp)

Để cài đặt Alby Go, hãy vào cửa hàng ứng dụng trên thiết bị của bạn:


- [Dành cho Android](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Dành cho Apple](https://apps.apple.com/us/app/alby-go/id6471335774).

![ALBY HUB](assets/fr/44.webp)

Người dùng Android cũng có thể cài đặt ứng dụng thông qua tệp `.apk` [có trên GitHub của Alby](https://github.com/getAlby/go/releases).

![ALBY HUB](assets/fr/45.webp)

Khi ứng dụng được khởi chạy, hãy nhấp vào "*Kết nối Wallet*".

![ALBY HUB](assets/fr/46.webp)

Trong Alby Hub của bạn, bên dưới App Store, tìm “Alby Go” và nhấp vào “Kết nối”

![ALBY HUB](assets/fr/47.webp)

Nhấp vào “Kết nối với One-Tab Connections”. Thao tác này sẽ cho phép bạn liên kết Alby Hub của mình chỉ bằng một cú nhấp chuột với các ứng dụng khác bằng Alby Go.

![ALBY HUB](assets/fr/48.webp)

Alby Hub sau đó sẽ sử dụng generate để thiết lập kết nối tới Alby Go.

![ALBY HUB](assets/fr/49.webp)

Quay lại ứng dụng Alby Go, quét mã QR hoặc dán bí mật.

![ALBY HUB](assets/fr/50.webp)

Nhấp vào "Hoàn tất*".

![ALBY HUB](assets/fr/51.webp)

Bây giờ bạn có thể truy cập từ xa vào Alby Hub chạy bằng nút Lightning từ điện thoại thông minh của mình, giúp bạn dễ dàng chi tiêu và nhận Sats khi di chuyển mỗi ngày.

![ALBY HUB](assets/fr/52.webp)

Nếu cần, bạn có thể quản lý quyền cho kết nối này trực tiếp trên Alby Hub bằng cách nhấp vào kết nối đó.

![ALBY HUB](assets/fr/53.webp)

Để nhận Sats, chỉ cần nhấp vào "*Nhận*".

![ALBY HUB](assets/fr/54.webp)

Sửa đổi số lượng và mô tả Invoice bằng cách nhấp vào "*Invoice*".

![ALBY HUB](assets/fr/55.webp)

Sạc Invoice để nhận Sats.

![ALBY HUB](assets/fr/56.webp)

Để gửi Sats, hãy nhấp vào "*Gửi*".

![ALBY HUB](assets/fr/57.webp)

Quét mã Invoice mà bạn muốn thanh toán.

![ALBY HUB](assets/fr/58.webp)

Sau đó nhấp vào "*Thanh toán*".

![ALBY HUB](assets/fr/59.webp)

Giao dịch của bạn đã được xác nhận.

![ALBY HUB](assets/fr/60.webp)

Bằng cách nhấp vào mũi tên nhỏ, bạn có thể truy cập lịch sử giao dịch của mình.

![ALBY HUB](assets/fr/61.webp)

Các giao dịch này cũng có thể được nhìn thấy trên Alby Hub của bạn.

![ALBY HUB](assets/fr/62.webp)

## Tùy chỉnh Lightning Address của bạn

Alby cung cấp cho bạn tùy chọn Lightning Address. Điều này cho phép bạn nhận thanh toán trên nút của mình mà không cần phải generate thủ công một Invoice mỗi lần. Theo mặc định, Alby chỉ định cho bạn một Lightning Address, nhưng bạn có thể tùy chỉnh nó. Đăng nhập vào tài khoản trực tuyến Alby của bạn, nhấp vào tên của bạn ở góc trên bên phải, sau đó chọn "*Cài đặt*".

![ALBY HUB](assets/fr/63.webp)

Điều hướng đến menu "*Lightning Address*".

![ALBY HUB](assets/fr/64.webp)

Sửa đổi Address của bạn, sau đó xác nhận bằng cách nhấp vào "*Cập nhật Lightning Address*".

![ALBY HUB](assets/fr/65.webp)

Xin lưu ý rằng sau khi Address của bạn đã được thay đổi, nó không còn thuộc về bạn nữa. Vì vậy, hãy đảm bảo rằng bạn không bao giờ gửi Sats cho nó nữa.

Và thế là xong, giờ bạn đã biết cách sử dụng Lightning với node của riêng mình bằng công cụ Alby Hub. Nếu bạn thấy hướng dẫn này hữu ích, tôi sẽ rất biết ơn nếu bạn để lại một ngón tay cái Green bên dưới. Vui lòng chia sẻ bài viết này trên mạng xã hội của bạn. Cảm ơn bạn rất nhiều!

Để hiểu chi tiết tất cả các cơ chế Lightning mà chúng tôi đã xử lý trong hướng dẫn này, tôi thực sự khuyên bạn nên khám phá khóa đào tạo miễn phí của chúng tôi về chủ đề này:

https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb