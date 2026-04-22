---
name: Liana
description: Thiết lập và sử dụng wallet trên Liana
---
![cover](assets/cover.webp)


![video](https://youtu.be/rTId6hfiRm0)


Trong hướng dẫn này, chúng tôi sẽ giải thích từng bước cách sử dụng ứng dụng Liana trên máy tính. Trong số những nội dung khác, bạn sẽ học cách thiết lập kế hoạch kế nhiệm tự động, nhận và gửi bitcoin trong các tình huống thông thường, và rút tiền từ wallet hiện có sau một khoảng thời gian nhất định.


Vào tháng 1 năm 2025, wallet phần cứng tương thích với Liana là: BitBox02, Blockstream Jade, Blockstream Jade Plus, COLDCARD MK4, COLDCARD Q, Ledger Nano S, Ledger Nano S Plus, Ledger Nano X, Ledger Flex, Specter DIY.


Nếu bạn muốn thu hồi tiền từ Liana hoặc wallet hiện có, hãy đọc bài thuyết trình bên dưới và chuyển thẳng đến phần "Thu hồi bitcoin".


## Giới thiệu phần mềm Liana


Liana là một gói phần mềm mã nguồn mở được thiết kế để tạo và quản lý các wallet nâng cao, đặc biệt là như một phần của hệ thống kế thừa tự động hoặc cơ chế sao lưu mạnh mẽ. Dự án này đã được phát triển từ năm 2022 bởi Wizardsardine, một công ty do Kévin Loaec và Antoine Poinsot đồng sáng lập. Trên trang web chính thức, Liana được giới thiệu là "một wallet đơn giản để quản lý cá nhân, với các chức năng phục hồi và kế thừa". Phần mềm này chạy trên các máy tính -- Linux, MacOS, Windows -- và mã nguồn (mở) của nó có sẵn [trên GitHub](https://github.com/wizardsardine/liana).


Liana được xây dựng dựa trên khả năng lập trình của Bitcoin để tạo ra một wallet tiên tiến hơn. Cụ thể, nó tận dụng các khóa thời gian (*timelocks*), cho phép chỉ chi tiêu tiền sau khi một khoảng thời gian nhất định đã trôi qua, và các khóa này cũng được sử dụng trong quá trình khôi phục Bitcoin. Do đó, một Liana wallet được tạo thành từ nhiều lộ trình chi tiêu khác nhau:




- Một kênh chi tiêu chính, luôn luôn khả dụng;
- Ít nhất một lộ trình phục hồi, lộ trình này sẽ khả dụng sau một khoảng thời gian nhất định.


Sơ đồ dưới đây minh họa hoạt động của một wallet với hai đường dẫn chi tiêu:


![Schéma explicatif](assets/fr/01.webp)


Thao tác này cho phép bạn thiết lập nhiều cấu hình khác nhau, bao gồm:




- Kế hoạch thừa kế (hoặc kế hoạch kế vị), cho phép người thừa kế thu hồi tiền trong trường hợp người dùng qua đời. Để biết thêm thông tin về chủ đề này, chúng tôi khuyên bạn nên đọc [phần 4](https://planb.academy/courses/f3e3843d-1a1d-450c-96d6-d7232158b81f/233c88d3-2e8e-5eba-ac06-efe67a209038) của khóa học BTC102.
- Một bản sao lưu được tăng cường với thời gian phục hồi, cho phép người dùng sử dụng wallet mà không cần phải lưu giữ cụm từ bí mật tương ứng và tránh nguy cơ bị đánh cắp, ví dụ như trong một vụ trộm.
- Một mạng lưới an toàn cho những người mới bắt đầu với Bitcoin: họ sẽ tự quản lý wallet của mình, và "người giám hộ" của họ (ví dụ: một người thân) sẽ có quyền thu hồi tiền của họ sau một khoảng thời gian nhất định.
- Một chương trình chữ ký đa bên (*multisig*) với các yêu cầu giảm dần theo thời gian, nhằm đối phó với sự biến mất của một hoặc nhiều bên tham gia, chẳng hạn như các đối tác của công ty.


Điểm mạnh lớn nhất của Liana là nó đưa ra một phương pháp tiêu chuẩn hóa để đảm bảo việc khôi phục tiền trong trường hợp mất khóa chính, được sử dụng cho các khoản chi tiêu hiện tại. Điều này thể hiện một sự đổi mới lớn đối với việc bảo quản tiền một cách an toàn, vốn tiềm ẩn nhiều rủi ro, đặc biệt nếu bạn không am hiểu về vấn đề này. Do đó, Liana có thể khuyến khích ngay cả những người dùng ngại rủi ro nhất ngừng sử dụng dịch vụ lưu ký (như sàn giao dịch) để giữ tiền của họ và lấy lại quyền sở hữu tiền của mình, phù hợp với tinh thần cypherpunk của Bitcoin.


Tất nhiên, Liana cũng có những nhược điểm. Đầu tiên là bạn phải cập nhật wallet thường xuyên bằng cách thực hiện giao dịch trên Bitcoin và blockchain. Điều này có thể gây phiền phức (tùy thuộc vào tần suất sử dụng phần mềm) và tốn kém (tùy thuộc vào mức phí tại thời điểm đó), nhưng đó là cái giá bạn phải trả cho sự bảo mật cao hơn.


Một điểm tiêu cực thứ hai có thể là vấn đề bảo mật. Khi bạn để người khác tham gia vào quá trình cấu hình, người đó sẽ biết tất cả địa chỉ của bạn và do đó có thể theo dõi hoạt động của bạn. Tuy nhiên, điều này sẽ không thành vấn đề nếu bạn chọn phương án sao lưu dự phòng nâng cao, hoặc kế hoạch kế nhiệm mà người thừa kế của bạn không biết ngay lập tức các chi tiết của wallet.


## Sự chuẩn bị


Trong hướng dẫn này, chúng ta sẽ thiết lập một kế hoạch kế nhiệm. Chúng ta sẽ sử dụng:




- Ledger Nano S Plus, dùng cho chi tiêu hàng ngày;


https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4


- Một thiết bị Blockstream Jade, được sử dụng để thu hồi tiền;


https://planb.academy/tutorials/wallet/hardware/jade-7d62bf0c-f460-4e68-9635-af9b731dabc3


- Hai thiết bị lưu trữ (USB) để lưu trữ mô tả wallet;
- Thư thừa kế, trong đó có hướng dẫn về việc thu hồi số tiền;
- Một túi niêm phong có đánh số, để đảm bảo rằng thiết bị thu hồi (Jade) chưa được sử dụng.


## Cài đặt và cấu hình


Hãy truy cập trang web chính thức của Wizardsardine và tải xuống Liana tại https://wizardsardine.com/liana/. Bạn cũng có thể tải xuống phiên bản mới nhất [từ kho lưu trữ GitHub](https://github.com/wizardsardine/liana/releases), nơi bạn có thể kiểm tra tính xác thực của phần mềm. Phiên bản được sử dụng trong hướng dẫn này là 0.9.


![Télécharger Liana](assets/fr/02.webp)


Để tìm hiểu cách xác minh thủ công tính xác thực và tính toàn vẹn của phần mềm trước khi cài đặt, chúng tôi khuyên bạn nên tham khảo hướng dẫn này:


https://planb.academy/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

Cài đặt phần mềm vào máy tính của bạn và khởi chạy nó. Chọn tùy chọn "*Tạo Liana wallet mới*" để cấu hình wallet của bạn.


![Accueil Liana](assets/fr/03.webp)


Hãy chọn loại wallet của bạn. Nếu bạn muốn thiết lập bản sao lưu nâng cao với thời gian phục hồi, bạn có thể chọn tùy chọn "*Tự xây dựng*" và chọn phương án mặc định. Cách này sẽ hoạt động tương tự, ngoại trừ việc bạn sẽ không cần giữ lại cụm từ phục hồi phần cứng wallet.


Ở đây chúng ta bỏ qua trường hợp của *Expanding multisig*, vốn thiết lập một cấu hình phức tạp hơn.


Trong hướng dẫn này, chúng ta sẽ sử dụng kế thừa đơn giản.


![Choisir type de portefeuille](assets/fr/04.webp)


Dưới đây là lời giải thích ngắn gọn.


![Rapide explication](assets/fr/05.webp)


Sau khi đọc xong phần giải thích, bạn sẽ có thể thiết lập các khóa cho Liana wallet của mình. Đây là một bước quan trọng, vì nó quyết định đặc điểm chi tiêu của tài khoản của bạn.


![Configurer clés](assets/fr/06.webp)


Trước hết, trong menu "Cài đặt nâng cao", bạn có thể quyết định "loại mô tả", tức là cách thức hợp đồng sẽ được viết trên chuỗi. Bạn có thể chọn giữa hai loại: P2WSH (SegWit) hoặc Taproot. Trong cả hai trường hợp, ngữ nghĩa của các điều kiện chi tiêu sẽ giống nhau. Mặc dù P2WSH giúp hợp đồng dễ hiểu hơn, Taproot lại vượt trội hơn vì nó ẩn các điều kiện không sử dụng và tiết kiệm chi phí trong quá trình truy xuất.


Lựa chọn này là tùy chọn: nếu không chắc chắn, hãy để nguyên tùy chọn mặc định (P2WSH trong trường hợp phiên bản 0.9, nhưng điều này có thể thay đổi).


![Choisir le type de descripteur](assets/fr/07.webp)


Tiếp theo, hãy cấu hình khóa chính của bạn. Khóa này (hay đúng hơn là tập hợp các khóa này) sẽ được sử dụng cho việc chi tiêu tiền hiện tại, không bị ràng buộc bởi bất kỳ điều kiện thời gian nào. Bằng cách nhấp vào "*Thiết lập*", bạn có thể chọn thiết bị ký tương ứng. Trong trường hợp này, chúng tôi đã chọn phần cứng Ledger Nano S Plus wallet.


Cho phép chia sẻ khóa công khai mở rộng từ thiết bị. Đặt cho khóa này một cái tên có ý nghĩa (trong trường hợp này là "Nano S+"). Lưu ý rằng tất cả các ứng dụng được cài đặt trên thiết bị sẽ tiếp tục hoạt động bình thường.


![Configurer clé principale](assets/fr/08.webp)


Tiếp theo, thiết lập độ trễ hoàn trả, tức là thời gian sau đó số tiền có thể được sử dụng bởi *khóa thừa kế*. Độ trễ này được xác định theo khối, với mỗi khối cách nhau trung bình 10 phút. Nó có thể dao động từ 10 phút (1 khối) đến khoảng 15 tháng (65.535 khối). Giới hạn trên này là một hạn chế của giao thức Bitcoin, vì thời gian khóa được mã hóa trên 16 bit.


Trừ những trường hợp đặc biệt, hãy chọn thời gian chờ dài nhất: 15 tháng hoặc 65.535 khối. Điều này sẽ giúp bạn tiết kiệm chi phí. Tuy nhiên, chúng tôi khuyến nghị bạn nên thực hiện quy trình cập nhật (được mô tả trong phần "Cập nhật wallet") mỗi năm một lần, luôn vào cùng một thời điểm trong năm, để "tạo thói quen" cho việc này và tránh quên.


Ở đây, chúng tôi đã thiết lập thời gian nghỉ ngơi là một giờ (6 khối) để tiến hành các bài kiểm tra.


![Configurer temps de verrouillage](assets/fr/09.webp)


Cuối cùng, hãy thiết lập khóa tài sản của bạn. Khóa này (hay đúng hơn là một tập hợp các khóa) sẽ được sử dụng để thu hồi tiền trong trường hợp bạn biến mất. Nhấp vào "*Thiết lập*", chọn thiết bị ký và xác thực việc chia sẻ khóa công khai mở rộng trên đó.


Trong hướng dẫn này, chúng ta đã chọn Jade. Hãy đặt cho khóa một cái tên gợi nhớ (ở đây là "Jade"). Giống như thiết bị đầu tiên, các tài khoản thông thường vẫn sẽ hoạt động bình thường.


![Configurer clé de succession](assets/fr/10.webp)


Sau khi hoàn tất tất cả các bước này, hãy kiểm tra xem mọi thứ đã ổn chưa và nhấp vào "*Tiếp tục*" để xác nhận lựa chọn của bạn.


![Confirmer clés](assets/fr/11.webp)


Bước tiếp theo là lưu lại mã mô tả wallet của bạn. Đây là thông tin bạn cần để tìm số tiền trong tài khoản. Trái ngược với cụm từ ghi nhớ, mã mô tả này không cho phép bạn chi tiêu tiền, vì vậy việc tiết lộ nó chỉ gây ra vấn đề về bảo mật (người đó sẽ biết tất cả các giao dịch của bạn).


Hãy lưu hai bản sao của mô tả này vào phương tiện lưu trữ điện tử, chẳng hạn như USB. Đảm bảo bạn cũng in ra hai bản sao trên giấy để có thể truy cập chúng trong trường hợp phương tiện lưu trữ điện tử bị hỏng. Mỗi bản sao lưu phải được liên kết với một thiết bị nhận dạng.


![Sauvegarder descripteur](assets/fr/12.webp)


Bộ mô tả của chúng tôi (được phân tích ở cuối bài hướng dẫn) như sau:


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


Bước cuối cùng trong quá trình cấu hình wallet ban đầu là xác minh mô tả trong mỗi thiết bị wallet phần cứng đóng vai trò là thiết bị ký số.


![Enregistrer descripteur](assets/fr/13.webp)


Thực hiện tương tự cho từng thiết bị ký. Bạn cần kiểm tra và xác nhận rằng mô tả đã được thêm vào từng thiết bị phần cứng wallet.


![Enregistrer descripteur Nano S Plus](assets/fr/14.webp)


Thông tin wallet của bạn hiện đã được đăng ký, và tất cả những gì còn lại là cấu hình cách bạn muốn kết nối với mạng Bitcoin. Bạn có thể chọn sử dụng nút mạng của riêng mình (cục bộ hoặc từ xa) hoặc sử dụng cơ sở hạ tầng của WizardSardine. Trong trường hợp thứ hai, bạn cần liên kết một địa chỉ email với wallet của mình, điều này sẽ cho phép bạn truy xuất mô tả. WizardSardine sẽ có quyền truy cập vào tất cả các giao dịch của bạn. Do đó, tùy chọn đầu tiên được khuyến nghị.


![Sélectionner connexion réseau](assets/fr/15.webp)


Chúng tôi đã chọn sử dụng node riêng của mình. Bạn có thể sử dụng một node hiện có, hoặc cài đặt một node *pruned* trên máy tính của mình. Nếu bạn không có quyền truy cập vào bất kỳ node nào khác, hãy tự cài đặt node riêng trên máy tính của bạn, việc này sẽ mất một khoảng thời gian (khoảng vài ngày).


![Choisir type de nœud](assets/fr/16.webp)


Trong hướng dẫn này, chúng tôi đã sử dụng một máy chủ Electrum hiện có (công khai). Nhưng hãy cẩn thận! Nó có quyền truy cập vào tất cả hoạt động của chúng tôi với Liana và wallet. Vì vậy, hãy sử dụng máy chủ riêng của bạn nếu bạn muốn bảo vệ quyền riêng tư của mình.


![Connexion serveur Electrum public](assets/fr/17.webp)


Sau khi cấu hình nút hoàn tất, màn hình chính sẽ hiện ra, hiển thị Liana và wallet vừa được tạo.


Hãy tận dụng cơ hội để cất giữ thiết bị phục hồi ở một nơi an toàn. Nó nên được cất giữ ở một vị trí chiến lược, để người thừa kế của bạn có thể tìm thấy trong trường hợp bạn qua đời.


Để tăng cường bảo mật, bạn có thể đặt các linh kiện dùng để khôi phục vào một túi kín (*túi chống giả mạo*) và ghi lại số sê-ri của túi ở đâu đó. Điều này đảm bảo rằng không ai có thể truy cập vào túi và thiết bị của bạn vẫn hợp lệ.


Trong ví dụ này, chúng ta đã tập hợp các thành phần sau:




- Blockstream Jade được sử dụng làm thiết bị nhận dạng cho toàn bộ hệ thống;
- Cáp USB để kết nối và sạc thiết bị;
- Bản sao lưu bằng giấy của câu lệnh trong trường hợp thiết bị bị trục trặc hoặc hư hỏng (lưu ý rằng phương tiện lưu trữ cũng có thể là kim loại, và do đó được bảo vệ khỏi các yếu tố môi trường, như trường hợp của các viên nang Cryptosteel chẳng hạn);
- USB chứa mô tả wallet;
- Bản sao lưu trên giấy của mô tả, phòng trường hợp USB bị trục trặc hoặc hư hỏng (bản sao lưu này không được chụp ảnh ở đây);
- Thư ủy quyền thừa kế mô tả các bước cần thực hiện để thu hồi số tiền.


![Éléments de récupération](assets/fr/18.webp)


Và chúng tôi đã niêm phong những mặt hàng này!


![Sachet scellé récupération](assets/fr/19.webp)


## Nhận tiền


Màn hình chính của Liana hiển thị số dư và các giao dịch (quá khứ và hiện tại) được liên kết với wallet của bạn. Trong trường hợp này, số dư là 0, điều này là bình thường.


![Écran principal](assets/fr/20.webp)


Để nhận tiền, hãy vào tab "*Nhận*" và nhấp vào "*Tạo địa chỉ*". Một địa chỉ mới sẽ xuất hiện trên màn hình của bạn. Địa chỉ này dài hơn so với các wallet thông thường: đó là địa chỉ được liên kết với một hợp đồng độc lập (P2WSH hoặc Taproot).


![Générer nouvelle adresse](assets/fr/21.webp)


Bạn cần xác minh địa chỉ này trên thiết bị phần cứng wallet bằng cách nhấp vào "*Xác minh trên thiết bị phần cứng*".


![Vérifier adresse portefeuille matériel](assets/fr/22.webp)


Sau khi tiền được gửi đi, giao dịch sẽ hiển thị trên màn hình chính (ban đầu là chưa xác nhận, sau đó là đã xác nhận). Ở đây, chúng tôi đã gửi 50.000 satoshi (tương đương hơn 50 đô la Mỹ tại thời điểm chuyển khoản) cho thử nghiệm này. Tất nhiên, số tiền được chuyển trong trường hợp của bạn sẽ phải cao hơn nhiều so với giá trị này do phí giao dịch.


![Vérifier solde](assets/fr/23.webp)


Bạn có thể kiểm tra trạng thái hết hạn của tiền bằng cách vào tab "*Coins*". Tab này hiển thị các loại tiền điện tử khác nhau (UTXO) trong wallet của bạn. Ở đây, chúng ta có thể thấy rằng 50.000 đồng satoshi được tạo ra từ giao dịch của chúng ta sẽ hết hạn vào cùng ngày (sau một giờ).


![Obtenir informations pièce](assets/fr/24.webp)


Để hiểu rõ hơn về mô hình đại diện UTXO được sử dụng trong Bitcoin, bạn có thể tham khảo phần đầu tiên của khóa học về tính bảo mật trong Bitcoin do Loïc Morel biên soạn:


https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Chi tiêu hiện tại


Việc chi tiêu hiện tại là tình trạng bình thường khi sử dụng Liana. Việc gửi bitcoin bằng khóa chính hoạt động như trên tất cả các Bitcoin và wallet cổ điển như Electrum hoặc Sparrow.


Để thực hiện giao dịch, hãy vào tab "*Gửi*" và nhập các thông tin cần thiết: địa chỉ BTC của người nhận, số tiền cần gửi và tỷ lệ phí mong muốn. Bạn cũng có thể thêm mô tả (được lưu cục bộ) để thuận tiện hơn. Trong ví dụ này, chúng tôi đã gửi 10.000 satoshi đến một Bob cụ thể, với tỷ lệ phí là 4 sat/ov, hoặc 0,67 đô la tại thời điểm giao dịch.


Liana cũng cung cấp chức năng "kiểm soát tiền xu": bạn chỉ định loại tiền xu (UTXO) mà bạn muốn sử dụng. Ở đây, chúng tôi đã chọn loại tiền xu 50.000 satoshi được tạo ra trước đó.


![Envoyer fonds clé principale](assets/fr/25.webp)


Sau đó, ký giao dịch bằng thiết bị ký điện tử được liên kết với khóa chính bằng cách nhấp vào "*Ký*". Bạn cần xác minh và xác nhận giao dịch trên thiết bị phần cứng wallet của mình. Ở đây, chúng tôi đã sử dụng Nano S Plus để ký giao dịch.


![Signer transaction clé principale](assets/fr/26.webp)


Cuối cùng, hãy phát sóng giao dịch trên mạng bằng cách nhấp vào "*Phát sóng*". Lưu ý rằng việc gửi tiền sẽ đặt lại thời gian phục hồi cho số tiền đã sử dụng.


![Diffuser transaction clé principale](assets/fr/27.webp)


Giao dịch sẽ hiển thị trên màn hình chính và số dư của bạn sẽ được cập nhật.


![Solde après dépense](assets/fr/28.webp)


## Cập nhật danh mục đầu tư


Như đã giải thích ở trên, Liana và wallet yêu cầu bạn cập nhật số dư tài khoản thường xuyên bằng cách thực hiện giao dịch trên blockchain. Nếu bạn không làm vậy, số tiền của bạn có thể bị người thừa kế (hoặc thiết bị thứ hai của bạn trong trường hợp sao lưu nâng cao) thu hồi. Tình huống này không quá nguy hiểm, nhưng nó làm mất đi mục đích của việc thiết lập cơ chế này: duy trì quyền kiểm soát bitcoin của bạn mà không cần đến bên thứ ba đáng tin cậy, đồng thời được hưởng lợi từ một mạng lưới an toàn.


Một cảnh báo sẽ được hiển thị trước khi số tiền của bạn (hoặc một phần trong số đó) hết hạn và có thể được sử dụng bằng khóa khôi phục. Cảnh báo sẽ cho biết "lộ trình khôi phục" (*recovery path*) của bạn sẽ sớm khả dụng. Do thời gian khôi phục ngắn (một giờ), thông báo này được hiển thị trực tiếp trong trường hợp của chúng tôi.


![Avertissement chemin récupération](assets/fr/29.webp)


Khi thời hạn đến gần, một nút sẽ xuất hiện nhắc bạn cập nhật số tiền liên quan.


![Actualiser pièces depuis l'écran principal](assets/fr/30.webp)


Để cập nhật số tiền của bạn, hãy vào tab "*Coins*" và nhấp vào "*Làm mới tiền*" trong ô tiền tương ứng. Nếu bạn có nhiều tiền, bạn nên làm mới từng cái một, và với khoảng thời gian tương đối ngắn, vì lý do bảo mật. Để giảm chi phí, bạn có thể hợp nhất tiền của mình bằng cách gửi toàn bộ wallet đến một địa chỉ nhận mới, nhưng điều này sẽ ảnh hưởng đến tính bảo mật của bạn.


![Actualiser pièce](assets/fr/31.webp)


Hãy chỉ định mức phí mong muốn cho giao dịch. Vì đây là chuyển khoản cho chính bạn, bạn có thể đặt mức phí khá thấp, đặc biệt nếu bạn thực hiện giao dịch vài ngày trước khi hết hạn.


![Transfert à soi-même](assets/fr/32.webp)


Giao dịch (được gắn nhãn "*tự chuyển khoản*") sẽ chỉ hiển thị trong tab "*Giao dịch*".


![Transactions après auto-transfert](assets/fr/33.webp)


Sau khi được xác nhận, đồng xu của bạn đã được an toàn! Bạn có thể yên tâm cho đến ngày hết hạn tiếp theo.


## Phục hồi Bitcoin


Khi khôi phục dữ liệu từ Liana hoặc wallet, bạn có thể gặp phải một trong hai trường hợp. Bạn có thể truy cập được vào máy tính đã cài đặt phần mềm, trong trường hợp đó tất cả những gì bạn cần làm là mở nó (điều này sẽ xảy ra với mô hình sao lưu nâng cao). Tuy nhiên, bạn có thể không truy cập được vào máy tính này, vì vậy chúng ta sẽ bắt đầu lại từ đầu. Lưu ý rằng quy trình khôi phục là giống nhau trong cả hai trường hợp.


Để bắt đầu, hãy tải xuống Liana từ [trang web chính thức của Wizardsardine](https://wizardsardine.com/liana/), hoặc từ [kho lưu trữ GitHub](https://github.com/wizardsardine/liana/releases), nơi bạn có thể kiểm tra tính xác thực của phần mềm. Cài đặt phần mềm và chạy nó. Phiên bản được sử dụng trong trường hợp của chúng tôi là 0.9, vì vậy giao diện có thể đã thay đổi. Trên màn hình chào mừng, chọn tùy chọn "Thêm Liana wallet hiện có".


![Ajouter portefeuille existant](assets/fr/34.webp)


Hãy cấu hình cách bạn muốn kết nối với mạng. Bạn có thể chọn sử dụng nút mạng riêng của mình (cục bộ hoặc từ xa) hoặc sử dụng cơ sở hạ tầng của WizardSardine. Trong trường hợp thứ hai, bạn sẽ cần địa chỉ email được người tạo wallet sử dụng để hệ thống có thể tự động định vị nguồn vốn. Nếu bạn không có thông tin này, hãy chọn tùy chọn đầu tiên.


![Sélectionner connexion réseau](assets/fr/35.webp)


Nếu bạn đang sử dụng node riêng, hãy nhập mô tả wallet. Đây là mô tả kỹ thuật của tài khoản, cho phép bạn truy xuất số tiền được giữ trong đó. Trong trường hợp của chúng tôi, đó là các thông tin sau:


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


![Importer descripteur](assets/fr/36.webp)


Liana sẽ yêu cầu bạn nhập một cụm từ ghi nhớ. Nếu bạn có thiết bị ký điện tử hoạt động tốt (wallet phần cứng), hãy bỏ qua bước này. Nếu thiết bị của bạn bị mất hoặc bị hỏng, nhưng bạn có 12 hoặc 24 từ tương ứng, bạn vẫn có thể sử dụng tùy chọn này. Để an toàn hơn (nếu số tiền cần khôi phục lớn), chúng tôi vẫn khuyên bạn nên mua một thiết bị wallet phần cứng mới và sử dụng cụm từ ghi nhớ để khôi phục khóa trên thiết bị đó.


Trong trường hợp của chúng tôi, chúng tôi sử dụng phần cứng Blockstream Jade wallet làm thiết bị khôi phục và chọn bỏ qua ("*Bỏ qua*") bước này.


![Passer phrase mnémotechnique](assets/fr/37.webp)


Kiểm tra và lưu mô tả vào thiết bị chữ ký của bạn bằng cách chọn nó trên màn hình. Nếu thiết bị phần cứng wallet của bạn không xuất hiện, hãy kiểm tra xem nó đã được kết nối và mở khóa chưa. Kiểm tra và xác nhận rằng thông tin này đã được thêm vào thiết bị của bạn.


![Enregistrer descripteur sur l'appareil de récupération](assets/fr/38.webp)


Cấu hình node của bạn. Bạn có thể sử dụng một node hiện có hoặc cài đặt một node *pruned* trên máy tính của mình. Trong trường hợp này, chúng tôi đã sử dụng một node hiện có.


![Choisir type de nœud](assets/fr/39.webp)


Trong hướng dẫn này, chúng tôi đã sử dụng máy chủ Electrum công cộng. Tuy nhiên, nó có quyền truy cập vào tất cả hoạt động của chúng tôi với Liana và wallet. Nếu bạn muốn bảo vệ quyền riêng tư của mình, tốt hơn hết bạn nên sử dụng node riêng.


![Connexion serveur Electrum public](assets/fr/17.webp)


Sau khi thiết lập node, bạn sẽ được chuyển đến màn hình chính của wallet, nơi bạn có thể xem số dư và các giao dịch trước đó liên kết với tài khoản. Bạn cũng có thể kiểm tra xem có thể rút tiền hay không. Ở đây, chúng ta thấy rằng một đồng tiền có thể được rút ra.


![Accueil Liana récupération](assets/fr/40.webp)


Để khôi phục số tiền trong wallet, hãy vào Cài đặt ("*Cài đặt*") ở góc dưới bên trái và nhấp vào "*Khôi phục*".


![Récupération dans paramètres](assets/fr/41.webp)


Sử dụng đồng xu trong wallet bằng cách đánh dấu vào ô thích hợp. Chỉ định địa chỉ BTC mà bạn muốn gửi tiền đến, cũng như mức phí giao dịch. Sau đó nhấp vào "*Tiếp theo*".


![Récupération des pièces](assets/fr/42.webp)


Hãy ký xác nhận giao dịch bằng cách nhấp vào "*Ký*" và xác thực giao dịch trên thiết bị phần cứng wallet của bạn.


![Signer transaction clé de récupération](assets/fr/43.webp)


Sau đó, hãy phát sóng nó qua mạng bằng cách nhấp vào "*Phát sóng*".


![Diffuser transaction clé de récupération](assets/fr/44.webp)


Giao dịch sẽ hiển thị trên màn hình chính. Sau khi xác nhận, quá trình khôi phục hoàn tất!


![Écran principal après récupération](assets/fr/45.webp)


## Phần thưởng: phân tích mô tả


Bộ mô tả là một chuỗi ký tự dễ đọc đối với con người, mô tả đầy đủ một tập hợp các địa chỉ. Nó kết hợp một số thông tin thiết yếu để truy xuất các phần (UTXO) của wallet nâng cao. Cách viết bộ mô tả dựa trên [cú pháp Miniscript](https://bitbox.swiss/blog/understanding-bitcoin-miniscript-part-2/), ngôn ngữ scripting được phát triển bởi Andrew Poelstra, Pieter Wuille và Sanket Kanjalkar vào năm 2019.


Để hiểu rõ hơn tại sao chuỗi ký tự này lại quan trọng, chúng ta hãy phân tích mô tả trong ví dụ của mình, đó là:


```plaintext
wsh(or_d(pk([3689a8e7/48'/0'/0'/2']xpub6FKYNH4XbbdADV98yTVxgZZrtB4eE2tiUPreEv5iJAS3U1CvXGAtQGFXSHyFYdYNn9wNa9KU1pwfYoxQhwq4sPXGihD725VncdSy66v9WQa/<0;1>/*),and_v(v:pkh([42e629dd/48'/0'/0'/2']xpub6DpQGv9LkwAQXvghWASvsfA7t1BVj7bGDQ939v32iB6aUJsMRB6inckim26gRp74NBdS2zuyfHNXDZ9dTuNXkFFiz6QvwEeVvBuC2cnRWQd/<0;1>/*),older(6))))#8alrve5h
```


Các thông tin sau đây có thể được trích xuất từ ​​mô tả này:




- `wsh` (viết tắt của *witness script hash*): Đây là loại đầu ra giao dịch được tạo ra. Nếu chúng ta chọn sử dụng Taproot, mã định danh sẽ là `tr`.
- `or_d`: Đây là một toán tử logic cho biết rằng *một trong hai* điều kiện sau phải được đáp ứng thì khoản chi phí mới được chấp nhận (ký tự `_d` chỉ định một cú pháp cụ thể).
- `pk` (viết tắt của *khóa công khai*): Toán tử này kiểm tra chữ ký được cung cấp so với khóa công khai sau và trả về kết quả dưới dạng Boolean (ĐÚNG hoặc SAI).
- `[3689a8e7/48'/0'/0'/2']`: Phần tử này bao gồm *dấu vân tay* của khóa chính cho phần cứng chính wallet (trong trường hợp này là Nano S Plus) và đường dẫn dẫn đến khóa riêng mở rộng được liên kết (từ đó tất cả các khóa riêng khác được dẫn xuất).
- `xpub6FKY ... WQa`: Đây là khóa công khai mở rộng được liên kết với phần cứng chính wallet (ở đây là Nano S Plus)
- `/<0;1>/*`: Đây là các đường dẫn tạo ra các khóa và địa chỉ đơn giản: `0` để nhận, `1` để thực hiện các thao tác nội bộ (*thay đổi*), với ký tự đại diện ("wildcard") ("*") cho phép tạo ra nhiều địa chỉ theo trình tự có thể cấu hình, tương tự như cách quản lý "giới hạn khoảng cách" của phần mềm wallet cổ điển.
- `and_v`: Đây là một toán tử logic cho biết *hai* điều kiện sau phải được đáp ứng thì khoản chi phí mới được chấp nhận (ký hiệu `_v` chỉ một cú pháp cụ thể).
- `v:pkh` (viết tắt của *verify: public key hash*): Toán tử này xác thực chữ ký và khóa công khai đã cho so với khóa công khai hash (*hash*) theo sau. Về cơ bản, đây là cùng một thao tác kiểm tra như đối với P2PKH và P2WPKH script.
- `[42e629dd/48'/0'/0'/2']`: Đây là cùng một phần tử như trên (bao gồm dấu vết và đường dẫn dẫn xuất), ngoại trừ việc dấu vết của khóa chính của thiết bị khôi phục phần cứng wallet (trong trường hợp này là Jade) được chỉ ra.
- `xpub6DpQ ... WQd`: Đây là khóa công khai mở rộng được liên kết với thiết bị khôi phục phần cứng wallet (ở đây là Jade).
- `older(6)` : Toán tử này kiểm tra xem đầu ra giao dịch được tạo ra phải có tuổi lớn hơn 6 khối để có thể được sử dụng.


Mục dữ liệu cuối cùng (`8alrve5h`) là tổng kiểm tra mô tả và tương ứng với mã định danh wallet.


Các script được tạo ra từ wallet này sẽ có hình dạng như sau:


```plaintext
<primary_key> CHECKSIG IFDUP NOTIF DUP HASH160 <recovery_key_hash> EQUALVERIFY CHECKSIGVERIFY <locktime> CHECKSEQUENCEVERIFY ENDIF
```


Vì tính bảo mật của Bitcoin và wallet của bạn cũng phụ thuộc vào sự hiểu biết của bạn về cách thức hoạt động của chúng, tôi khuyên bạn nên nghiên cứu sâu về cơ chế hoạt động của wallet mang tính xác định và phân cấp bằng cách tham gia khóa đào tạo miễn phí về Plan ₿ Academy này:


https://planb.academy/courses/46b0ced2-9028-4a61-8fbc-3b005ee8d70f