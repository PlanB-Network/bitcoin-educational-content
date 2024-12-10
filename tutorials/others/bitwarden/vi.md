---
name: Bitwarden
description: Cách thiết lập một trình quản lý mật khẩu?
---
![cover](assets/cover.webp)

Trong kỷ nguyên số, chúng ta cần quản lý nhiều tài khoản trực tuyến khác nhau bao gồm nhiều khía cạnh trong cuộc sống hàng ngày, bao gồm ngân hàng, nền tảng tài chính, email, lưu trữ tệp, sức khỏe, quản trị, mạng xã hội, trò chơi video, v.v.

Để xác thực bản thân trên mỗi tài khoản này, chúng ta sử dụng một định danh, thường là địa chỉ email, kèm theo một mật khẩu. Đối mặt với việc không thể ghi nhớ một số lượng lớn mật khẩu duy nhất, người ta có thể bị cám dỗ sử dụng lại cùng một mật khẩu hoặc chỉnh sửa nhẹ một cơ sở chung để dễ nhớ. Tuy nhiên, những thực hành này nghiêm trọng làm giảm an toàn của các tài khoản của bạn.

Nguyên tắc đầu tiên cần tuân theo cho mật khẩu là không tái sử dụng chúng. Mỗi tài khoản trực tuyến nên được bảo vệ bởi một mật khẩu duy nhất hoàn toàn khác biệt với những cái khác. Điều này quan trọng vì, nếu một kẻ tấn công quản lý để xâm phạm một trong những mật khẩu của bạn, bạn không muốn họ có quyền truy cập vào tất cả các tài khoản của bạn. Có một mật khẩu duy nhất cho mỗi tài khoản cô lập các cuộc tấn công tiềm năng và giới hạn phạm vi của chúng. Ví dụ, nếu bạn sử dụng cùng một mật khẩu cho một nền tảng trò chơi video và cho email của bạn, và mật khẩu đó bị xâm phạm qua một trang web lừa đảo liên quan đến nền tảng trò chơi, kẻ tấn công có thể dễ dàng truy cập vào email của bạn và kiểm soát tất cả các tài khoản trực tuyến khác của bạn.

Nguyên tắc thiết yếu thứ hai là độ mạnh của mật khẩu. Một mật khẩu được coi là mạnh nếu nó khó bị bẻ khóa, tức là, khó đoán thông qua thử và sai. Điều này có nghĩa là mật khẩu của bạn phải càng ngẫu nhiên càng tốt, dài và bao gồm nhiều loại ký tự (chữ thường, chữ hoa, số và ký hiệu).

Áp dụng hai nguyên tắc bảo mật mật khẩu này (độc nhất và mạnh mẽ) có thể chứng minh là khó khăn trong cuộc sống hàng ngày, vì gần như không thể ghi nhớ một mật khẩu duy nhất, ngẫu nhiên và mạnh mẽ cho tất cả các tài khoản của chúng ta. Đây là nơi trình quản lý mật khẩu đóng vai trò.

Một trình quản lý mật khẩu tạo và lưu trữ an toàn các mật khẩu mạnh, cho phép bạn truy cập vào tất cả các tài khoản trực tuyến mà không cần phải ghi nhớ chúng một cách riêng lẻ. Bạn chỉ cần nhớ một mật khẩu, mật khẩu chính, cho phép bạn truy cập vào tất cả mật khẩu đã lưu trong trình quản lý. Sử dụng trình quản lý mật khẩu tăng cường an ninh trực tuyến của bạn vì nó ngăn chặn việc tái sử dụng mật khẩu và hệ thống tạo mật khẩu ngẫu nhiên. Nhưng nó cũng đơn giản hóa việc sử dụng hàng ngày các tài khoản của bạn bằng cách tập trung truy cập vào thông tin nhạy cảm của bạn.
Trong hướng dẫn này, chúng ta sẽ khám phá cách thiết lập và sử dụng trình quản lý mật khẩu để tăng cường an ninh trực tuyến của bạn. Tôi sẽ giới thiệu bạn với Bitwarden, và trong một hướng dẫn khác, chúng ta sẽ tìm hiểu về một giải pháp khác gọi là KeePass.
https://planb.network/tutorials/others/general/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Cảnh báo: Trình quản lý mật khẩu rất tốt để lưu trữ mật khẩu, nhưng **bạn không bao giờ nên lưu cụm từ ghi nhớ của ví Bitcoin trong đó!** Nhớ rằng, cụm từ ghi nhớ nên được lưu trữ độc quyền trong định dạng vật lý, như một tờ giấy hoặc kim loại.

## Giới thiệu về Bitwarden

Bitwarden là một trình quản lý mật khẩu phù hợp cho cả người mới bắt đầu và người dùng nâng cao. Nó mang lại nhiều lợi ích. Trước hết và quan trọng nhất, Bitwarden là một giải pháp đa nền tảng, có nghĩa là bạn có thể sử dụng nó như một ứng dụng di động, ứng dụng web, tiện ích mở rộng trình duyệt và phần mềm máy tính.
![BITWARDEN](assets/notext/01.webp)
Bitwarden cho phép bạn lưu trữ mật khẩu trực tuyến và đồng bộ hóa chúng trên tất cả các thiết bị của bạn, đồng thời đảm bảo mã hóa đầu cuối với mật khẩu chính của bạn. Điều này cho phép bạn, ví dụ, truy cập mật khẩu của mình trên cả máy tính và điện thoại thông minh, với sự đồng bộ hóa giữa hai thiết bị. Vì mật khẩu của bạn được mã hóa, chúng vẫn không thể truy cập được bởi bất kỳ ai, bao gồm cả Bitwarden, nếu không có khóa giải mã là mật khẩu chính của bạn.
Hơn nữa, Bitwarden là mã nguồn mở, điều này có nghĩa là phần mềm có thể được kiểm định bởi các chuyên gia độc lập. Về giá cả, Bitwarden cung cấp ba gói:
- Một phiên bản miễn phí mà chúng ta sẽ khám phá trong hướng dẫn này. Mặc dù là miễn phí, nó cung cấp một mức độ bảo mật tương đương với các phiên bản trả phí. Bạn có thể lưu trữ số lượng mật khẩu không giới hạn và đồng bộ hóa nhiều thiết bị tùy ý;
- Một phiên bản cao cấp với giá 10 đô la mỗi năm bao gồm các tính năng bổ sung như lưu trữ tệp, sao lưu thẻ ngân hàng, khả năng thiết lập 2FA với một khóa bảo mật vật lý, và truy cập xác thực 2FA TOTP trực tiếp với Bitwarden;
- Và một gói gia đình với giá 40 đô la mỗi năm mở rộng lợi ích của phiên bản cao cấp cho sáu người dùng khác nhau.
![BITWARDEN](assets/notext/02.webp)
Theo ý kiến của tôi, những mức giá này là hợp lý. Phiên bản miễn phí là một lựa chọn xuất sắc cho người mới bắt đầu, và phiên bản cao cấp cung cấp giá trị rất tốt so với các trình quản lý mật khẩu khác trên thị trường, đồng thời cung cấp nhiều tính năng hơn. Ngoài ra, việc Bitwarden là mã nguồn mở là một lợi thế lớn. Do đó, đây là một sự thỏa hiệp thú vị, đặc biệt là cho người mới bắt đầu.
Một tính năng khác của Bitwarden là khả năng tự lưu trữ trình quản lý mật khẩu của bạn nếu bạn sở hữu, ví dụ, một NAS tại nhà. Bằng cách thiết lập cấu hình này, mật khẩu của bạn không được lưu trữ trên máy chủ của Bitwarden, mà là trên máy chủ của riêng bạn. Điều này cho bạn quyền kiểm soát hoàn toàn về việc có sẵn mật khẩu của mình. Tuy nhiên, lựa chọn này đòi hỏi quản lý sao lưu chặt chẽ để tránh mất quyền truy cập. Do đó, việc tự lưu trữ của Bitwarden phù hợp hơn với người dùng nâng cao, và chúng ta sẽ thảo luận về nó trong một hướng dẫn khác.
## Làm thế nào để tạo một tài khoản Bitwarden?

Truy cập [trang web Bitwarden](https://bitwarden.com/) và nhấp vào "*Bắt đầu*".
![BITWARDEN](assets/notext/03.webp)
Bắt đầu bằng cách nhập địa chỉ email của bạn cũng như tên hoặc biệt danh của bạn.
![BITWARDEN](assets/notext/04.webp)
Tiếp theo, bạn sẽ cần thiết lập mật khẩu chính của mình. Như chúng ta đã thấy trong phần giới thiệu, mật khẩu này rất quan trọng vì nó cho phép bạn truy cập vào tất cả các mật khẩu khác đã lưu trong trình quản lý. Nó sau đó đặt ra hai rủi ro chính: mất và bị xâm phạm. Nếu bạn mất quyền truy cập vào mật khẩu này, bạn sẽ không thể truy cập vào tất cả các thông tin đăng nhập của mình. Nếu mật khẩu của bạn bị đánh cắp, kẻ tấn công sẽ có thể truy cập vào tất cả các tài khoản của bạn.

Để giảm thiểu rủi ro mất mát, tôi khuyên bạn nên sao lưu mật khẩu chính của mình trên giấy và lưu trữ nó ở một nơi an toàn. Nếu có thể, đóng gói sao lưu này trong một phong bì an toàn để thường xuyên đảm bảo rằng không ai khác có quyền truy cập vào nó.

Để ngăn chặn việc mật khẩu chính bị xâm phạm, nó phải cực kỳ mạnh mẽ. Nó nên dài nhất có thể, sử dụng đa dạng các ký tự, và được chọn một cách ngẫu nhiên. Trong năm 2024, các khuyến nghị tối thiểu cho một mật khẩu an toàn là 13 ký tự bao gồm số, chữ thường và chữ hoa, cũng như biểu tượng, miễn là mật khẩu thực sự ngẫu nhiên. Tuy nhiên, tôi khuyên bạn nên chọn một mật khẩu ít nhất 20 ký tự, bao gồm tất cả các loại ký tự có thể, để đảm bảo an toàn cho nó lâu hơn.

Nhập mật khẩu chính của bạn vào ô dành riêng và xác nhận nó trong ô tiếp theo.
![BITWARDEN](assets/notext/05.webp)
Nếu bạn muốn, bạn có thể thêm một gợi ý cho mật khẩu chính của mình. Tuy nhiên, tôi khuyên bạn không nên làm như vậy, vì gợi ý không cung cấp một phương pháp đáng tin cậy để khôi phục nếu bạn mất mật khẩu và thậm chí có thể hữu ích cho những kẻ tấn công cố gắng đoán hoặc dùng lực brute force mật khẩu của bạn. Như một quy tắc chung, tránh tạo ra những gợi ý công khai có thể làm lộ lỗ hổng bảo mật của mật khẩu chính của bạn.
![BITWARDEN](assets/notext/06.webp)
Sau đó, nhấp vào nút "*Tạo một tài khoản*".
![BITWARDEN](assets/notext/07.webp)
Bây giờ bạn có thể đăng nhập vào tài khoản Bitwarden mới của mình. Nhập địa chỉ email của bạn.
![BITWARDEN](assets/notext/08.webp)
Sau đó nhập mật khẩu chính của bạn.
![BITWARDEN](assets/notext/09.webp)
Bây giờ bạn đang ở trên giao diện web của trình quản lý mật khẩu của mình.
![BITWARDEN](assets/notext/10.webp)
## Làm thế nào để thiết lập Bitwarden?

Đầu tiên, chúng ta sẽ xác nhận địa chỉ email của mình. Nhấp vào "*Gửi Email*".
![BITWARDEN](assets/notext/11.webp)
Sau đó nhấp vào nút nhận được qua email.
![BITWARDEN](assets/notext/12.webp)
Cuối cùng, đăng nhập lại.
![BITWARDEN](assets/notext/13.webp)
Trước hết và quan trọng nhất, tôi rất khuyên bạn nên thiết lập xác thực hai yếu tố (2FA) để bảo vệ trình quản lý mật khẩu của mình. Bạn có sự lựa chọn giữa việc sử dụng ứng dụng TOTP hoặc một khóa bảo mật vật lý. Bằng cách kích hoạt 2FA, mỗi lần bạn đăng nhập vào tài khoản Bitwarden của mình, bạn sẽ được yêu cầu không chỉ mật khẩu chính mà còn cả bằng chứng của yếu tố xác thực thứ hai. Đây là một lớp bảo mật bổ sung, đặc biệt hữu ích trong trường hợp bản sao lưu giấy của mật khẩu chính bị lộ.

Nếu bạn không chắc cách thiết lập và sử dụng các thiết bị 2FA này, tôi khuyên bạn nên theo dõi 2 hướng dẫn khác này:

https://planb.network/tutorials/others/general/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

https://planb.network/tutorials/others/general/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Để làm điều này, đi đến tab "*Bảo mật*" trong menu "*Cài đặt*".
![BITWARDEN](assets/notext/14.webp)
Sau đó nhấp vào tab "*Đăng nhập hai bước*".
![BITWARDEN](assets/notext/15.webp)
Ở đây, bạn có thể chọn phương thức 2FA bạn ưa thích. Ví dụ, tôi sẽ chọn 2FA với ứng dụng TOTP bằng cách nhấp vào nút "*Quản lý*".
![BITWARDEN](assets/notext/16.webp)
Xác nhận mật khẩu chính của bạn.
![BITWARDEN](assets/notext/17.webp)
Sau đó quét mã QR với ứng dụng 2FA của bạn.
![BITWARDEN](assets/notext/18.webp)
Nhập mã 6 chữ số ghi trên ứng dụng 2FA của bạn, sau đó nhấp vào nút "*Bật*". ![BITWARDEN](assets/notext/19.webp)
Xác thực hai yếu tố đã được thiết lập thành công trên tài khoản của bạn.
![BITWARDEN](assets/notext/20.webp)
Bây giờ, nếu bạn cố gắng đăng nhập lại vào trình quản lý của mình, bạn sẽ cần phải nhập mật khẩu chính trước, sau đó là mã 6 chữ số động được tạo bởi ứng dụng 2FA của bạn. Hãy chắc chắn bạn luôn có quyền truy cập vào mã động này; nếu không, bạn sẽ không thể khôi phục mật khẩu của mình.
![BITWARDEN](assets/notext/21.webp)
Trong cài đặt, bạn cũng có tùy chọn để tùy chỉnh trình quản lý của mình trong tab "*Tùy chọn*". Ở đây, bạn có thể thay đổi thời gian trước khi trình quản lý của bạn tự động khóa, cũng như ngôn ngữ và chủ đề của giao diện.
Tôi rất khuyến khích bạn điều chỉnh độ dài của các mật khẩu được tạo bởi Bitwarden. Theo mặc định, độ dài được thiết lập là 14 ký tự, có thể không đủ để đảm bảo an ninh tối ưu. Bây giờ bạn đã có một trình quản lý để nhớ tất cả mật khẩu của mình, bạn cũng nên tận dụng nó để sử dụng những mật khẩu rất mạnh.

Để làm điều này, hãy vào menu "*Generator*".
Tại đây, bạn có thể tăng độ dài của mật khẩu lên đến 40 và đánh dấu vào ô để bao gồm các ký tự đặc biệt.

## Làm thế nào để bảo vệ các tài khoản của bạn với Bitwarden?

Bây giờ trình quản lý mật khẩu của bạn đã được cấu hình, bạn có thể bắt đầu lưu trữ thông tin đăng nhập cho các tài khoản trực tuyến của mình. Để thêm một mục mới, hãy nhấp trực tiếp vào nút "*New item*" hoặc vào nút "*New*" nằm ở góc trên bên phải của màn hình, sau đó chọn "*item*".

Trong biểu mẫu mở ra, bắt đầu bằng cách xác định bản chất của mục cần lưu. Để lưu thông tin đăng nhập, chọn tùy chọn "*Login*" từ menu thả xuống.

Trong trường "*Name*", nhập tên mô tả cho thông tin đăng nhập của bạn. Điều này sẽ giúp dễ dàng tìm kiếm và tổ chức mật khẩu của bạn, đặc biệt nếu bạn có số lượng lớn. Ví dụ, nếu bạn muốn lưu thông tin đăng nhập của mình cho trang web PlanB Network, bạn có thể đặt tên cho mục này một cách dễ nhận biết trong các tìm kiếm tương lai của bạn.

Tùy chọn "*Folder*" cho phép bạn phân loại thông tin đăng nhập của mình vào các thư mục. Hiện tại, chúng tôi chưa tạo bất kỳ thư mục nào, nhưng tôi sẽ chỉ bạn cách làm sau.

Trong trường "*Username*", nhập tên người dùng của bạn, thường là địa chỉ email của bạn.

Tiếp theo, trong trường "*Password*", bạn có thể nhập mật khẩu của mình. Tuy nhiên, tôi rất khuyến khích bạn để Bitwarden tạo ra một mật khẩu dài, ngẫu nhiên và duy nhất cho bạn. Điều này đảm bảo bạn có một mật khẩu mạnh. Để sử dụng tính năng này, nhấp vào biểu tượng mũi tên kép phía trên trường cần điền.

Bạn có thể thấy rằng mật khẩu của bạn đã được tạo.

Trong trường "*URI 1*", bạn có thể nhập tên miền của trang web.

Và cuối cùng, trong trường "*Notes*", bạn có thể thêm chi tiết bổ sung nếu cần thiết.

Khi bạn đã hoàn thành việc điền tất cả các trường này, nhấp vào nút "*Save*".

Bây giờ, thông tin đăng nhập của bạn xuất hiện trong trình quản lý Bitwarden của bạn.

Bằng cách nhấp vào nó, bạn có thể truy cập chi tiết của nó và chỉnh sửa chúng.

Bằng cách nhấp vào ba chấm nhỏ ở bên phải, bạn có quyền truy cập nhanh để sao chép mật khẩu hoặc thông tin đăng nhập.
Chúc mừng, bạn đã thành công trong việc lưu mật khẩu đầu tiên vào trình quản lý của mình! Nếu bạn muốn tổ chức các định danh của mình một cách tốt hơn, bạn có thể tạo các thư mục cụ thể. Để làm điều này, hãy nhấp vào nút "*New*" ở góc trên bên phải của màn hình, sau đó chọn "*Folder*".![BITWARDEN](assets/notext/38.webp)
Nhập tên cho thư mục của bạn.
![BITWARDEN](assets/notext/39.webp)
Sau đó nhấp vào "*Save*".
![BITWARDEN](assets/notext/40.webp)
Thư mục của bạn giờ đây xuất hiện trong trình quản lý của bạn.
![BITWARDEN](assets/notext/41.webp)
Bạn có thể gán một thư mục cho một định danh khi tạo nó, như chúng tôi đã làm trước đó, hoặc bằng cách chỉnh sửa một định danh hiện có. Ví dụ, bằng cách nhấp vào định danh của tôi cho Mạng PlanB, tôi có thể chọn phân loại nó vào thư mục "*Bitcoin*".
![BITWARDEN](assets/notext/42.webp)
Như vậy, bạn có thể cấu trúc trình quản lý mật khẩu của mình để dễ dàng tìm kiếm các định danh của bạn. Bạn có thể tổ chức chúng với các thư mục như cá nhân, chuyên nghiệp, ngân hàng, email, mạng xã hội, đăng ký, mua sắm, quản trị, phát trực tuyến, lưu trữ, du lịch, sức khỏe, v.v.
Nếu bạn muốn chỉ sử dụng phiên bản web của Bitwarden, hoàn toàn có thể làm như vậy. Sau đó, tôi khuyên bạn nên thêm trình quản lý mật khẩu của mình vào mục yêu thích của trình duyệt để dễ dàng truy cập và tránh rủi ro phishing. Tuy nhiên, Bitwarden cũng cung cấp một loạt các ứng dụng khách cho phép bạn sử dụng trình quản lý của mình trên các thiết bị khác nhau và đơn giản hóa việc sử dụng hàng ngày. Họ đặc biệt cung cấp một ứng dụng di động, một tiện ích mở rộng trình duyệt và phần mềm máy tính. Hãy xem cách thiết lập chúng cùng nhau.

![BITWARDEN](assets/notext/43.webp)

## Làm thế nào để sử dụng tiện ích mở rộng trình duyệt Bitwarden?

Đầu tiên, bạn có thể thiết lập tiện ích mở rộng trình duyệt nếu bạn muốn. Tiện ích mở rộng này hoạt động như một phiên bản rút gọn của trình quản lý của bạn và cung cấp cho bạn khả năng tự động lưu mật khẩu mới, tạo gợi ý cho mật khẩu an toàn và tự động điền thông tin đăng nhập của bạn trên các trang đăng nhập website.

Việc sử dụng hàng ngày tiện ích mở rộng này rất tiện lợi, nhưng cũng có thể mở ra các vector tấn công mới. Một số chuyên gia an ninh mạng do đó khuyên không sử dụng tiện ích mở rộng trình duyệt cho trình quản lý mật khẩu. Tuy nhiên, nếu bạn chọn sử dụng tiện ích mở rộng Bitwarden, đây là cách tiến hành:

Bắt đầu bằng cách truy cập [trang tải xuống chính thức của Bitwarden](https://bitwarden.com/download/#downloads-web-browser).

![BITWARDEN](assets/notext/44.webp)

Chọn trình duyệt của bạn từ danh sách được cung cấp. Trong ví dụ này, tôi sử dụng Firefox, vì vậy tôi được chuyển hướng đến tiện ích mở rộng Bitwarden chính thức trên Firefox Add-ons Store. Quy trình tương tự khá giống nhau cho các trình duyệt khác.

![BITWARDEN](assets/notext/45.webp)

Nhấp vào nút "*Add to Firefox*".

![BITWARDEN](assets/notext/46.webp)

Bạn có thể sau đó gắn Bitwarden vào thanh tiện ích mở rộng để dễ dàng truy cập. Nhấp vào tiện ích mở rộng để đăng nhập.

![BITWARDEN](assets/notext/47.webp)

Nhập địa chỉ email của bạn.

![BITWARDEN](assets/notext/48.webp)

Sau đó nhập mật khẩu chính của bạn.

![BITWARDEN](assets/notext/49.webp)

Và cuối cùng, nhập mã 6 chữ số từ ứng dụng xác thực của bạn.

![BITWARDEN](assets/notext/50.webp)

Bây giờ bạn đã kết nối với trình quản lý Bitwarden của mình thông qua tiện ích mở rộng trình duyệt.

![BITWARDEN](assets/notext/51.webp)
Ví dụ, nếu tôi quay trở lại trang web PlanB Network và thử đăng nhập vào tài khoản của mình, bạn có thể thấy rằng tiện ích mở rộng Bitwarden tích hợp vào trình duyệt nhận biết các trường đăng nhập và tự động đề xuất cho tôi chọn định danh mà tôi đã lưu trước đó.
![BITWARDEN](assets/notext/52.webp)
Nếu tôi chọn định danh này, Bitwarden sẽ tự động điền các trường đăng nhập cho tôi. Tính năng này của tiện ích mở rộng cho phép kết nối nhanh chóng đến các trang web, mà không cần phải sao chép-dán thông tin xác thực từ ứng dụng web hoặc phần mềm Bitwarden.
![BITWARDEN](assets/notext/53.webp)
Tiện ích mở rộng cũng được thiết kế để phát hiện việc tạo tài khoản mới. Ví dụ, khi tạo một tài khoản mới trên PlanB Network, Bitwarden tự động đề xuất lưu định danh mới.
![BITWARDEN](assets/notext/54.webp)
Bằng cách nhấp vào đề xuất này khi nó xuất hiện, tiện ích mở rộng sẽ mở ra. Nó cho phép tôi nhập chi tiết của định danh mới và tạo một mật khẩu mạnh, độc đáo.
![BITWARDEN](assets/notext/55.webp)
Sau khi hoàn tất thông tin và nhấp vào "*Lưu*", tiện ích mở rộng sẽ lưu thông tin xác thực.
![BITWARDEN](assets/notext/56.webp)
Sau đó, tiện ích mở rộng tự động điền thông tin xác thực của chúng tôi vào các trường thích hợp trên trang web.
![BITWARDEN](assets/notext/57.webp)
## Làm thế nào để sử dụng phần mềm Bitwarden?

Để cài đặt phần mềm Bitwarden cho máy tính, bắt đầu bằng cách truy cập [trang tải xuống](https://bitwarden.com/download/#downloads-desktop). Chọn và tải xuống phiên bản phù hợp với hệ điều hành của bạn.
![BITWARDEN](assets/notext/58.webp)
Sau khi tải xuống hoàn tất, tiến hành cài đặt phần mềm trên máy tính của bạn. Khi khởi chạy phần mềm Bitwarden lần đầu tiên, bạn sẽ cần nhập thông tin xác thực của mình để mở khóa trình quản lý mật khẩu.
![BITWARDEN](assets/notext/59.webp)
Sau đó, bạn sẽ đến trang chủ của trình quản lý. Giao diện gần như giống hệt với ứng dụng web.
![BITWARDEN](assets/notext/60.webp)
## Làm thế nào để sử dụng ứng dụng Bitwarden?

Để truy cập mật khẩu từ điện thoại của bạn, bạn có thể cài đặt ứng dụng di động Bitwarden. Bắt đầu bằng cách truy cập [trang tải xuống](https://bitwarden.com/download/#downloads-mobile) và sử dụng điện thoại thông minh của bạn để quét mã QR tương ứng với hệ điều hành của bạn.
![BITWARDEN](assets/notext/61.webp)
Tải xuống và cài đặt ứng dụng di động chính thức của Bitwarden. Khi mở ứng dụng lần đầu tiên, nhập thông tin xác thực của bạn để mở khóa quyền truy cập vào trình quản lý mật khẩu của bạn.
![BITWARDEN](assets/notext/62.webp)
Một khi đã kết nối, bạn sẽ có thể xem và quản lý tất cả mật khẩu của mình trực tiếp từ ứng dụng.
![BITWARDEN](assets/notext/63.webp)
Để tăng cường bảo mật cho ứng dụng của bạn, tôi khuyên bạn nên vào cài đặt và kích hoạt bảo vệ bằng mã PIN. Điều này sẽ thêm một lớp bảo mật bổ sung trong trường hợp mất hoặc bị đánh cắp điện thoại của bạn.
![BITWARDEN](assets/notext/64.webp)
## Làm thế nào để sao lưu Bitwarden?
Để đảm bảo bạn không bao giờ mất quyền truy cập vào mật khẩu của mình, ngay cả trong trường hợp mất mật khẩu chính hoặc một sự cố ảnh hưởng đến máy chủ của Bitwarden, tôi khuyên bạn nên thường xuyên thực hiện sao lưu mã hóa của trình quản lý trên một phương tiện bên ngoài.
Ý tưởng là mã hóa tất cả các thông tin đăng nhập Bitwarden của bạn bằng một mật khẩu khác với mật khẩu chính của bạn và lưu bản sao lưu đã mã hóa này vào một ổ USB hoặc ổ cứng mà bạn giữ tại nhà, chẳng hạn. Sau đó, bạn có thể giữ một bản sao vật lý của mật khẩu giải mã ở một vị trí khác với nơi lưu trữ phương tiện sao lưu. Ví dụ, bạn có thể giữ ổ USB tại nhà và giao bản sao vật lý của mật khẩu mã hóa cho một người bạn đáng tin cậy.

Phương pháp này đảm bảo rằng ngay cả khi phương tiện sao lưu của bạn bị đánh cắp, dữ liệu của bạn vẫn sẽ không thể truy cập được mà không có mật khẩu giải mã. Tương tự, người bạn của bạn sẽ không thể truy cập vào dữ liệu của bạn nếu không có phương tiện vật lý.

Tuy nhiên, trong trường hợp có vấn đề, bạn có thể sử dụng mật khẩu và phương tiện bên ngoài để lấy lại quyền truy cập vào thông tin đăng nhập của mình, độc lập với Bitwarden. Như vậy, ngay cả khi máy chủ của Bitwarden bị hủy, bạn vẫn có khả năng lấy lại mật khẩu của mình.

Do đó, tôi khuyên bạn nên thực hiện các bản sao lưu này một cách định kỳ để chúng luôn bao gồm thông tin đăng nhập mới nhất của bạn. Để tránh làm phiền người bạn giữ bản sao của mật khẩu mã hóa với mỗi bản sao lưu mới, bạn có thể lưu mật khẩu này trong trình quản lý mật khẩu của mình. Điều này không được coi là một bản sao lưu, vì người bạn của bạn đã có một bản sao vật lý, mà là để đơn giản hóa các thủ tục xuất khẩu trong tương lai của bạn.

Để tiến hành xuất khẩu, rất đơn giản: vào mục "*Công cụ*" của trình quản lý Bitwarden của bạn, sau đó chọn "*Xuất kho lưu trữ*".
![BITWARDEN](assets/notext/65.webp)
Đối với định dạng, chọn "*.json (Đã mã hóa)*".
![BITWARDEN](assets/notext/66.webp)
Sau đó chọn tùy chọn "*Được bảo vệ bằng mật khẩu*".
![BITWARDEN](assets/notext/67.webp)
Ở đây, điều quan trọng là chọn một mật khẩu mạnh, độc đáo và được tạo ngẫu nhiên để mã hóa bản sao lưu. Điều này đảm bảo rằng, ngay cả trong trường hợp bản sao lưu đã mã hóa của bạn bị đánh cắp, sẽ không thể cho kẻ tấn công giải mã bằng cách sử dụng lực lượng brút-fôs.
![BITWARDEN](assets/notext/68.webp)
Nhấp vào "*Xác nhận định dạng*" và nhập mật khẩu chính của bạn để tiến hành việc xuất khẩu.
![BITWARDEN](assets/notext/69.webp)
Khi quá trình xuất khẩu hoàn tất, bạn sẽ tìm thấy tệp sao lưu đã mã hóa của mình trong thư mục tải xuống. Chuyển nó sang một thiết bị lưu trữ bên ngoài an toàn, như một ổ USB hoặc ổ cứng. Lặp lại thao tác này định kỳ tùy thuộc vào việc sử dụng của bạn. Ví dụ, bạn có thể làm mới bản sao lưu mỗi tuần hoặc mỗi tháng, tùy theo nhu cầu của bạn.