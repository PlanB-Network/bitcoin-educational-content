---
name: Đóng góp - Obsidian
description: Làm thế nào để đóng góp cho Mạng lưới PlanB với GitHub và Obsidian?
---
![cover](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn tài nguyên giáo dục hàng đầu về Bitcoin, bằng càng nhiều ngôn ngữ khả dụng nhất. Tất cả nội dung được công bố trên trang web là mã nguồn mở và được lưu trữ trên GitHub, do đó, mở ra cơ hội cho bất kỳ ai muốn tham gia vào việc làm phong phú thêm nền tảng. Đóng góp có thể có nhiều hình thức: sửa chữa và hiệu đính các văn bản hiện có, dịch sang ngôn ngữ khác, cập nhật thông tin, hoặc tạo mới các hướng dẫn chưa có trên trang web của chúng tôi.

Nếu bạn muốn đóng góp cho Mạng lưới PlanB, nhưng bạn không thoải mái khi sử dụng GitHub, hướng dẫn này được thiết kế đặc biệt cho bạn. Chúng tôi sẽ chi tiết cách đóng góp cho Mạng lưới PlanB qua GitHub, trong khi sử dụng Obsidian, một công cụ được thiết kế để hỗ trợ việc viết lách.

Bạn sẽ thấy rằng việc thiết lập toàn bộ quy trình làm việc khá dài, đặc biệt nếu bạn chưa bao giờ sử dụng GitHub trước đây. Tuy nhiên, việc sử dụng Git làm cho việc hợp tác viết nội dung trở nên dễ dàng hơn, vì nó cho phép theo dõi chính xác các thay đổi, quản lý phiên bản hiệu quả, và cũng cho phép xem xét và cải thiện nội dung bởi các đóng góp viên khác. Hơn nữa, một khi quy trình làm việc được thiết lập trên PC của bạn, bạn sẽ thấy rằng Git rất hỗ trợ công việc của bạn. Bạn thậm chí có thể muốn sử dụng Git cho các dự án cá nhân khác của mình vì phần mềm này hiệu quả đến vậy.

## Từ vựng Git
- **Fetch origin:** Lệnh lấy thông tin và thay đổi gần đây từ một kho lưu trữ từ xa mà không hợp nhất chúng với công việc cục bộ của bạn.
- **Pull origin:** Lệnh lấy cập nhật từ một kho lưu trữ từ xa và ngay lập tức tích hợp chúng vào nhánh cục bộ của bạn để đồng bộ hóa nó.
- **Sync Fork:** Lệnh trên GitHub cập nhật fork của bạn của một dự án với những thay đổi mới nhất từ kho lưu trữ nguồn.
- **Push origin:** Lệnh được sử dụng để gửi các sửa đổi cục bộ của bạn đến một kho lưu trữ từ xa.
- **Pull Request:** Một yêu cầu được gửi bởi một người đóng góp để chỉ ra rằng họ đã đẩy các sửa đổi trên một nhánh trong một kho lưu trữ từ xa và mong muốn những sửa đổi này được xem xét và có thể được tích hợp (hợp nhất) vào nhánh chính của kho lưu trữ.
- **Commit:** Lưu các sửa đổi của bạn. Một commit giống như một bức ảnh tức thì của công việc của bạn tại một thời điểm nhất định, giúp giữ lại lịch sử của các thay đổi.
- **Branch:** Một phiên bản song song của kho lưu trữ, cho phép bạn làm việc trên các sửa đổi mà không ảnh hưởng đến nhánh chính (gọi là "`dev`" trên kho lưu trữ PlanB).
- **Merge:** Việc hợp nhất bao gồm tích hợp các sửa đổi từ một nhánh này sang nhánh khác. Nó được sử dụng, ví dụ, để thêm các sửa đổi từ một nhánh làm việc vào nhánh chính.
- **Fork:** Fork một kho lưu trữ có nghĩa là tạo một bản sao của kho lưu trữ đó trên tài khoản GitHub của bạn, cho phép bạn làm việc trên dự án mà không ảnh hưởng đến kho lưu trữ gốc.
- **Clone:** Cloning một kho lưu trữ có nghĩa là tạo một bản sao cục bộ trên máy tính của bạn, cho phép bạn truy cập vào tất cả các tệp và lịch sử sửa đổi.

- **Repository:** Một không gian lưu trữ cho một dự án trên GitHub. Nó chứa tất cả các tệp dự án cũng như lịch sử của tất cả các sửa đổi đã được thực hiện.

## Nội dung nào để viết trên Mạng lưới PlanB?
Chúng tôi chủ yếu tìm kiếm các hướng dẫn về các công cụ liên quan đến Bitcoin hoặc hệ sinh thái của nó. Những nội dung này có thể được cấu trúc xung quanh sáu danh mục chính:
- Ví;
- Node;
- Đào mỏ;
- Thương nhân;
- Sàn giao dịch;
- Riêng tư.

Ngoài những chủ đề cụ thể liên quan đến Bitcoin, PlanB cũng tìm kiếm các đóng góp về các chủ đề nổi bật về chủ quyền cá nhân, như:
- Công cụ mã nguồn mở;
- Tin học;
- Mật mã học;
- Năng lượng;
- Toán học;
- Kinh tế;
- DIY;
- LifeHacking...
Ví dụ, hiện tại chúng tôi có các hướng dẫn về Tails, Nostr, hoặc GrapheneOS. Những công cụ này không trực tiếp liên quan đến Bitcoin, nhưng chúng là những hệ thống có thể thu hút chúng ta trong việc tiếp cận chủ quyền trong thế giới số, hoặc trong việc học cách đạt được điều đó. Những nội dung này có thể được tích hợp vào một tiểu mục của mục "Khác".

Bạn có thể chọn thiết kế một hướng dẫn từ đầu hoặc tái bản một hướng dẫn đã được xuất bản trước đó trên trang web của bạn (miễn là bạn sở hữu bản quyền) để cũng chia sẻ nó trên Mạng PlanB, kèm theo một liên kết đến bài viết gốc.

Dù bạn chọn phương án nào, hãy nhớ rằng tất cả nội dung được xuất bản trên Mạng PlanB đều dưới giấy phép tự do [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/). Giấy phép này cho phép bất kỳ ai cũng có thể sao chép và, có khả năng, chỉnh sửa nội dung của bạn, miễn là nguồn gốc ban đầu được ghi công đúng cách.

## Quy Trình Đóng Góp
Để thêm một hướng dẫn vào trang web Mạng PlanB, bạn cần thực hiện một Pull Request trên kho lưu trữ GitHub hiện được gọi là [sovereign-university-data](https://github.com/DecouvreBitcoin/sovereign-university-data). Đóng góp của bạn phải tuân thủ cấu trúc tiêu chuẩn và bao gồm tất cả các tệp cần thiết. Đây chính xác là những gì chúng tôi sẽ chi tiết trong các phần sau.

Sau đó, một quản trị viên sẽ xem xét hướng dẫn của bạn. Nếu cần điều chỉnh, họ sẽ thông báo cho bạn để các sửa đổi có thể được thực hiện. Một khi được chấp thuận, hướng dẫn sẽ được tích hợp vào kho lưu trữ.

## Bước 1: Tạo một Tài Khoản GitHub
Nếu bạn chưa đăng ký GitHub, bạn sẽ cần tạo một tài khoản. Để làm điều này, truy cập [https://github.com/signup](https://github.com/signup). Nhập địa chỉ email của bạn, sau đó chọn một mật khẩu mạnh. ![github](assets/1.webp)
Tiếp theo, chọn tên người dùng của bạn. Bạn có lựa chọn tiết lộ danh tính thực của mình hoặc ưu tiên sử dụng một bí danh. Nhấn vào `Continue` và hoàn thành Captcha. Một email chứa mã xác nhận sẽ được gửi cho bạn; bạn sẽ cần nhập nó để hoàn tất việc tạo tài khoản.
![github](assets/2.webp)
Điền vào các câu hỏi nếu bạn muốn GitHub hướng dẫn bạn đến một số công cụ nhất định, hoặc nhấn vào `skip personalization` để bỏ qua.
![github](assets/3.webp)
Chọn gói miễn phí bằng cách nhấn vào nút `Continue for free`.
![github](assets/4.webp)
Sau đó, bạn sẽ được chuyển hướng đến bảng điều khiển của mình. Nếu bạn muốn, bạn có thể tùy chỉnh tài khoản của mình bằng cách nhấn vào ảnh đại diện của bạn ở góc trên bên phải của màn hình, sau đó truy cập menu `Settings`.
![github](assets/5.webp)
Trong phần này, bạn có tùy chọn thêm một ảnh đại diện mới, chọn một tên, tùy chỉnh tiểu sử của bạn, hoặc thêm một liên kết đến trang web cá nhân của bạn.
![github](assets/6.webp)
Tôi cũng khuyên bạn nên xem xét menu `Password and authentication`, để thiết lập xác thực hai yếu tố.
![github](assets/7.webp)

## Bước 2: Cài Đặt GitHub Desktop
Truy cập https://desktop.github.com/ để tải xuống phần mềm GitHub Desktop. Phần mềm này cho phép bạn tương tác dễ dàng với GitHub, mà không cần sử dụng terminal.
![github](assets/8.webp)
Khi phần mềm được khởi chạy lần đầu, bạn sẽ được yêu cầu kết nối tài khoản GitHub của mình. Để làm điều này, nhấn vào `Sign in to GitHub.com`.

![github](assets/9.webp)

Một trang xác thực sẽ mở trong trình duyệt của bạn. Nhập địa chỉ email và mật khẩu đã chọn ở bước trước, sau đó nhấn vào nút `Sign in`.
![github](assets/10.webp)
Nhấp vào `Authorize desktop` để xác nhận kết nối giữa tài khoản của bạn và phần mềm. ![github](assets/11.webp)
Bạn sẽ tự động được chuyển hướng đến phần mềm GitHub Desktop. Nhấp vào `Finish`.

![github](assets/12.webp)

Nếu bạn mới tạo tài khoản GitHub, bạn sẽ được chuyển hướng đến trang thông báo rằng bạn chưa tạo bất kỳ kho lưu trữ nào. Tại thời điểm này, hãy tạm gác phần mềm GitHub Desktop sang một bên; chúng ta sẽ quay lại với nó sau.

![github](assets/13.webp)

## Bước 3: Cài đặt Obsidian
Chúng ta tiếp tục với việc cài đặt phần mềm viết. Ở đây, bạn có một số lựa chọn. Có rất nhiều phần mềm chuyên biệt trong việc chỉnh sửa tệp Markdown, như Typora, được thiết kế đặc biệt cho việc viết. Mặc dù không lý tưởng, nhưng cũng có thể chọn một trình biên tập mã, như Visual Studio Code (VSC) hoặc Sublime Text. Tuy nhiên, với tư cách là một người viết, tôi thích sử dụng phần mềm Obsidian. Hãy cùng xem cách cài đặt và bắt đầu sử dụng nó. ![github](assets/14.webp)
Truy cập https://obsidian.md/download và tải phần mềm về. Cài đặt nó, chọn ngôn ngữ của bạn, sau đó nhấp vào `Quick Start`.

![github](assets/15.webp)

Bạn sẽ đến với phần mềm Obsidian. Hiện tại, bạn chưa mở tệp nào.

![github](assets/16.webp)

## Bước 4: Fork kho lưu trữ PlanB Network
Truy cập kho dữ liệu PlanB Network tại địa chỉ sau: [https://github.com/DecouvreBitcoin/sovereign-university-data](https://github.com/DecouvreBitcoin/sovereign-university-data). Nếu bạn chưa đăng nhập vào tài khoản GitHub của mình, vui lòng đăng nhập lại.
![github](assets/17.webp)
Từ trang này, nhấp vào nút `Fork` ở góc trên bên phải của cửa sổ.
![github](assets/18.webp)
Trong menu tạo mới, bạn có thể để nguyên các cài đặt mặc định. Đảm bảo rằng ô `Copy the dev branch only` đã được chọn, sau đó nhấp vào nút `Create fork`.
![github](assets/19.webp)
Sau đó, bạn sẽ đến với fork của riêng bạn của kho lưu trữ PlanB Network. 
![github](assets/20.webp)
Fork này do đó tạo thành một kho lưu trữ riêng biệt từ bản gốc, mặc dù hiện tại nó vẫn chứa cùng một dữ liệu. Bây giờ bạn sẽ làm việc trên kho lưu trữ mới này.

## Bước 5: Clone kho lưu trữ của bạn
Quay trở lại phần mềm GitHub Desktop. Bây giờ, fork của bạn nên xuất hiện trong mục `Your repositories`. Nếu bạn không thấy nó ngay lập tức, sử dụng nút mũi tên kép để làm mới danh sách. Khi fork của bạn xuất hiện, nhấp vào nó để chọn.

![github](assets/21.webp)

Sau đó nhấp vào nút màu xanh: `Clone [username]/sovereign-university-data`.

![github](assets/22.webp)

Sau đó, bạn có tùy chọn thay đổi đường dẫn truy cập cục bộ trên máy tính của bạn nơi clone của kho lưu trữ của bạn sẽ được lưu trữ. Bạn có thể giữ nguyên đường dẫn mặc định. Để xác nhận, nhấp vào nút màu xanh `Clone`.

![github](assets/23.webp)

Chờ trong khi GitHub Desktop clone fork của bạn về máy cục bộ.

![github](assets/24.webp)
Sau khi clone kho lưu trữ, phần mềm sẽ cung cấp cho bạn hai lựa chọn. Bạn phải chọn lựa chọn đầu tiên: `Đóng góp cho dự án mẹ`. Lựa chọn này sẽ cho phép bạn trình bày công việc tương lai của mình như là một đóng góp cho dự án mẹ (`DecouvreBitcoin/sovereign-university-data`), chứ không chỉ là sửa đổi của fork cá nhân của bạn (`[username]/sovereign-university-data`). Sau khi lựa chọn được chọn, nhấn vào `Tiếp tục`.![github](assets/25.webp)

GitHub Desktop của bạn giờ đây đã được cấu hình đúng cách. Bây giờ, bạn có thể để phần mềm mở ở chế độ nền để theo dõi các thay đổi mà chúng tôi sẽ thực hiện.

![github](assets/26.webp)

## Bước 6: Tạo một kho lưu trữ mới trên Obsidian
Mở phần mềm Obsidian và nhấn vào biểu tượng kho lưu trữ nhỏ ở góc dưới bên trái của cửa sổ.

![github](assets/27.webp)

Nhấn vào nút `Mở` để mở một thư mục hiện có như một kho lưu trữ.

![github](assets/28.webp)

Trình duyệt tệp của bạn sẽ mở ra. Bạn cần tìm và chọn thư mục có tiêu đề `GitHub`, nó nên nằm trong thư mục `Tài liệu` của bạn giữa các tệp của bạn. Đường dẫn này tương ứng với đường dẫn bạn đã thiết lập trong bước 5. Sau khi chọn thư mục, xác nhận lựa chọn của mình. Việc tạo kho lưu trữ của bạn trên Obsidian sẽ sau đó được khởi chạy trên một trang mới của phần mềm.

![github](assets/29.webp)

-> **Chú ý**, điều quan trọng là không chọn thư mục `sovereign-university-data` khi tạo một kho lưu trữ mới trên Obsidian. Thay vào đó, chọn thư mục mẹ, `GitHub`. Nếu bạn chọn thư mục `sovereign-university-data`, thư mục cấu hình `.obsidian`, chứa cài đặt Obsidian cục bộ của bạn, sẽ tự động được tích hợp vào kho lưu trữ. Chúng tôi muốn tránh điều này, vì không cần thiết phải chuyển cài đặt Obsidian của bạn sang kho lưu trữ của PlanB Network. Một phương án khác là thêm thư mục `.obsidian` vào tệp `.gitignore`, nhưng phương pháp này cũng sẽ dẫn đến việc sửa đổi tệp `.gitignore` của kho lưu trữ gốc, điều này không mong muốn.

Ở phía bên trái của cửa sổ, bạn có thể thấy cây tệp với các kho lưu trữ GitHub khác nhau của bạn đã được clone cục bộ. Bằng cách nhấn vào các mũi tên cạnh tên thư mục, bạn có thể mở rộng chúng để truy cập vào các thư mục con của các kho lưu trữ và tài liệu của chúng.

![github](assets/30.webp)

Đừng quên thiết lập Obsidian sang chế độ tối: "*Ánh sáng thu hút côn trùng*" ;)

## Bước 7: Cài đặt một trình soạn thảo mã
Hầu hết các sửa đổi của bạn sẽ được thực hiện trên các tệp định dạng Markdown (`.md`). Để chỉnh sửa các tài liệu này, bạn có thể sử dụng Obsidian, phần mềm mà chúng tôi đã thảo luận trước đó. Tuy nhiên, PlanB Network sử dụng các định dạng tệp khác, và bạn sẽ cần chỉnh sửa một số trong số đó.
Ví dụ, khi tạo một hướng dẫn mới, bạn sẽ cần tạo một tệp YAML (`.yml`) để bao gồm các thẻ của hướng dẫn, tiêu đề của nó, cũng như định danh giáo viên của bạn. Obsidian không cung cấp khả năng chỉnh sửa loại tệp này, vì vậy bạn sẽ cần một trình soạn thảo mã.
Đối với điều này, có một số lựa chọn có sẵn cho bạn. Mặc dù notepad tiêu chuẩn trên máy tính của bạn có thể được sử dụng để thực hiện các sửa đổi này, giải pháp này không lý tưởng cho công việc gọn gàng. Tôi khuyên bạn nên chọn phần mềm được thiết kế đặc biệt cho mục đích này, như [VS Code](https://code.visualstudio.com/download) hoặc [Sublime Text](https://www.sublimetext.com/download). Sublime Text, vì là khá nhẹ, sẽ hơn là đủ cho nhu cầu của chúng ta.
![github](assets/31.webp)
Cài đặt một trong những chương trình này, và giữ nó sang một bên cho sau này.
## Bước 8: Thêm giáo viên mới (tùy chọn)
Nếu bạn đã từng đóng góp cho Mạng lưới PlanB, bạn đã có một mã định danh người đóng góp. Bạn có thể tìm thấy nó trong thư mục giáo viên của mình, có thể truy cập qua [trang này](https://github.com/DecouvreBitcoin/sovereign-university-data/tree/dev/professors). Nếu đúng là như vậy, bạn có thể bỏ qua bước này và chuyển thẳng đến bước 9.
![github](assets/32.webp)
Nếu bạn chưa từng đóng góp cho Mạng lưới PlanB, bạn sẽ cần tạo hồ sơ của mình để tên bạn xuất hiện trên các hướng dẫn trong tương lai. Để làm điều này, chúng ta sẽ bắt đầu bằng cách tạo một nhánh mới dành riêng cho việc thêm hồ sơ giáo viên của bạn. Một nhánh trong Git là một phiên bản song song của dự án, cho phép bạn thực hiện các thay đổi mà không ảnh hưởng đến nhánh chính, cho đến khi công việc sẵn sàng để được hợp nhất.

Trước khi tiến hành tạo một nhánh mới, điều quan trọng là đảm bảo bạn đang làm việc trên phiên bản mới nhất của dự án để giảm thiểu rủi ro xung đột khi hợp nhất các thay đổi của bạn. Để làm điều này, mở trình duyệt của bạn và truy cập vào trang của bản fork PlanB của bạn. Đây là bản fork bạn đã thiết lập trên GitHub ở bước 4. URL của bản fork của bạn sẽ trông giống như:

`https://github.com/[username]/sovereign-university-data`
![github](assets/34.webp)
Đảm bảo bạn đang ở trên nhánh chính `dev` sau đó nhấp vào nút `Sync fork`. Nếu bản fork của bạn không cập nhật, GitHub sẽ đề nghị cập nhật nhánh của bạn. Tiến hành đồng bộ hóa này. Nếu ngược lại, nhánh của bạn đã cập nhật, GitHub sẽ thông báo cho bạn.
![github](assets/35.webp)
Bây giờ bản fork của bạn trên GitHub đã được đồng bộ hóa với kho lưu trữ nguồn của Mạng lưới PlanB, đã đến lúc cũng làm mới kho lưu trữ cục bộ trên máy tính của bạn. Mở phần mềm GitHub Desktop và đảm bảo rằng bản fork của bạn được chọn đúng cách ở góc trên bên trái của cửa sổ.
Nhấp vào nút `Fetch origin`. Nếu kho lưu trữ cục bộ của bạn đã cập nhật, GitHub Desktop sẽ không đề xuất thêm hành động nào. Nếu không, tùy chọn `Pull origin` sẽ xuất hiện. Nhấp vào nút này để cập nhật kho lưu trữ cục bộ của bạn.

Sau khi đồng bộ hóa kho lưu trữ của bạn với những đóng góp mới nhất, bạn đã sẵn sàng để tạo một nhánh làm việc mới. Vẫn sử dụng GitHub Desktop, đảm bảo rằng bạn đang ở trên nhánh chính `dev`.

Nhấp vào nhánh này, sau đó nhấp vào nút `New Branch`.

Đảm bảo nhánh mới được dựa trên kho lưu trữ nguồn, cụ thể là `DecouvreBitcoin/sovereign-university-data`. Đặt tên cho nhánh của bạn một cách rõ ràng về mục đích của nó, sử dụng dấu gạch ngang để phân cách từng từ. Vì nhánh này dành cho việc thêm hồ sơ giáo viên, một ví dụ tên có thể là: `add-professor-[tên-của-bạn]`. Sau khi nhập tên, nhấp vào `Create branch` để xác nhận việc tạo nhánh.

Bây giờ nhấp vào nút `Publish branch` để lưu nhánh làm việc mới của bạn trên fork trực tuyến của bạn trên GitHub.

Tại thời điểm này, trên GitHub Desktop, bạn sẽ thấy mình đang ở trên nhánh mới của mình. Điều này có nghĩa là tất cả các thay đổi được thực hiện cục bộ trên máy tính của bạn sẽ được ghi lại độc quyền trên nhánh cụ thể này. Ngoài ra, miễn là nhánh này vẫn được chọn trên GitHub Desktop, các tệp hiển thị cục bộ trên máy của bạn tương ứng với những tệp của nhánh này (`add-professor-tên-của-bạn`), và không phải là những tệp của nhánh chính (`dev`).

Để thêm hồ sơ giáo viên của bạn, mở trình duyệt tệp và đi đến kho lưu trữ cục bộ của bạn, trong thư mục `professors`. Bạn sẽ tìm thấy nó dưới đường dẫn: `\GitHub\sovereign-university-data\professors`.
Trong thư mục này, hãy tạo một thư mục mới với tên hoặc bí danh của bạn. Đảm bảo rằng tên thư mục không có khoảng trắng. Vì vậy, nếu tên bạn là "Loic Pandul" và không có giáo sư nào khác có tên này, thư mục cần tạo sẽ được đặt tên là `loic-pandul`.
Để việc này trở nên dễ dàng hơn, bạn có thể sao chép và dán tất cả các tài liệu từ một giáo sư khác vào thư mục của mình. Chúng tôi sẽ tiếp tục chỉnh sửa những tài liệu này để tùy chỉnh chúng theo hồ sơ của bạn.
Bắt đầu bằng cách điều hướng đến thư mục `assets`. Xóa bức ảnh đại diện của giáo sư mà bạn đã sao chép trước đó, và thay thế bằng ảnh đại diện của bạn. Điều quan trọng là hình ảnh này phải ở định dạng `.webp` và được đặt tên là `profile`, từ đó tạo ra tên file hoàn chỉnh là `profile.webp`. Lưu ý, hình ảnh này sẽ được công bố trên Internet và mọi người đều có thể truy cập.
![github](assets/45.webp)

Tiếp theo, mở file `professor.yml` bằng trình soạn thảo mã của bạn (VSC hoặc Sublime Text). Bạn sẽ đến với file đã được sao chép từ một giáo sư hiện có.

![github](assets/46.webp)

Sau đó, bạn cần cập nhật thông tin hiện có bằng thông tin của mình:
- **name:** nhập tên hoặc bí danh của bạn;
- **links:** chỉ ra các tài khoản trên mạng xã hội như Twitter và Nostr, cũng như URL của trang web cá nhân của bạn (tùy chọn);
- **affiliation:** nêu tên công ty mà bạn làm việc (tùy chọn);
- **tags:** chỉ định các lĩnh vực chuyên môn của bạn từ danh sách sau, biết rằng bạn có thể thêm các chủ đề của riêng mình. Tuy nhiên, hãy chắc chắn giới hạn số lượng tags không quá 4 để đảm bảo giao diện người dùng tốt:
	- privacy,
	- cryptography,
	- bitcoin,
	- mining,
	- lightning-network,
	- economy,
	- history,
	- merchants,
	- security,
	- ...
- **tips:** cung cấp địa chỉ Lightning của bạn để nhận quyên góp, cho phép độc giả của các hướng dẫn tương lai của bạn gửi cho bạn một số sats (tùy chọn);
- **company:** nếu bạn sở hữu một công ty, hãy chỉ ra tên công ty của bạn (tùy chọn).

![github](assets/47.webp)

Bạn cũng cần chỉnh sửa `contributor-id`. Định danh này được sử dụng để nhận diện bạn trên website, nhưng không được công bố ra ngoài GitHub. Bạn tự do chọn bất kỳ sự kết hợp nào của hai từ, tham khảo danh sách tiếng Anh của 2048 từ từ BIP39, có thể truy cập tại đây: [https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt](https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt). Đừng quên chèn một dấu gạch ngang giữa hai từ đã chọn. Ví dụ, ở đây, tôi chọn `crazy-cactus`.

![github](assets/48.webp)

Khi bạn đã hoàn thành việc chỉnh sửa tài liệu `professor.yml`, nhấp vào `File > Save` để lưu file của bạn. Bạn có thể sau đó thoát khỏi trình soạn thảo mã.

![github](assets/49.webp)
Đã đến lúc tiến hành viết tiểu sử của bạn. Trong file giáo viên của bạn, bạn có thể xóa các tài liệu được viết bằng ngôn ngữ không liên quan đến bạn, ban đầu được sao chép từ một giáo viên khác. Chỉ giữ lại file tương ứng với ngôn ngữ mẹ đẻ của bạn. Ví dụ, trong trường hợp của tôi, tôi chỉ giữ lại file `fr.yml`, vì ngôn ngữ của tôi là tiếng Pháp.
![github](assets/50.webp)

Nhấp đúp vào file này để mở nó bằng trình soạn thảo mã của bạn. Trong file này, bạn có cơ hội viết tiểu sử đầy đủ của mình dưới mục `bio` và một tóm tắt hoặc một tiêu đề súc tích dưới `short_bio`.

![github](assets/51.webp)
Sau khi lưu tài liệu `fr.yml` của bạn, cần thiết phải tạo một bản sao của tệp này cho mỗi ngôn ngữ sau đây:
- Đức (DE);
- Anh (EN);
- Pháp (FR);
- Tây Ban Nha (ES);
- Ý (IT);
- Bồ Đào Nha (PT).

Tiến hành sao chép dán tệp gốc của bạn, sau đó dịch mỗi tài liệu sang ngôn ngữ tương ứng. Nếu bạn thông thạo ngôn ngữ, bạn có thể thực hiện việc dịch một cách thủ công. Nếu không, bạn có thể sử dụng công cụ dịch tự động hoặc chatbot. Nếu bạn muốn, cũng có thể chỉ giữ lại phần tiểu sử bằng ngôn ngữ mẹ đẻ của bạn; chúng tôi sẽ tiến hành dịch sau khi bạn gửi Pull Request của mình.

![github](assets/52.webp)

Thư mục giáo viên của bạn do đó sẽ trông như thế này:

![github](assets/53.webp)

Bây giờ quay trở lại GitHub Desktop. Ở phía bên trái cửa sổ của bạn, bạn sẽ quan sát thấy tất cả các sửa đổi đã được thực hiện đối với các tài liệu, cụ thể là cho nhánh của bạn. Đảm bảo rằng những sửa đổi này là chính xác.

![github](assets/54.webp)

Nếu các sửa đổi dường như chính xác với bạn, thêm một tiêu đề cho lần commit của bạn. Một commit là một lưu của các sửa đổi đã được thực hiện đối với nhánh, đi kèm với một thông điệp mô tả, cho phép theo dõi sự phát triển của một dự án theo thời gian. Sau khi nhập tiêu đề, nhấn vào nút màu xanh `Commit to [your branch]` để xác nhận những sửa đổi này.

![github](assets/55.webp)

Sau đó nhấp vào nút `Push origin`. Điều này sẽ gửi commit của bạn đến fork của bạn.

![github](assets/56.webp)

Nếu bạn đã hoàn thành các sửa đổi cho nhánh này, bây giờ nhấp vào nút `Preview Pull Request`.

![github](assets/57.webp)

Bạn có thể kiểm tra một lần nữa xem các sửa đổi của bạn có thực sự chính xác không, sau đó nhấp vào nút `Create pull request`.

![github](assets/58.webp)

Bạn sẽ được tự động chuyển hướng đến trình duyệt của mình trên GitHub đến trang để chuẩn bị Pull Request của bạn. Một Pull Request là một yêu cầu được thực hiện để tích hợp các sửa đổi của nhánh bạn vào nhánh chính của kho lưu trữ PlanB Network, cho phép xem xét và thảo luận về các thay đổi trước khi hợp nhất.
![github](assets/59.webp)
Trên trang chuẩn bị này, chỉ ra một tiêu đề tóm tắt ngắn gọn các thay đổi bạn muốn hợp nhất với kho lưu trữ nguồn. Thêm một bình luận ngắn gọn mô tả những thay đổi này. Sau khi hoàn thành các bước này, nhấp vào nút màu xanh lá `Create pull request` để xác nhận yêu cầu hợp nhất. ![github](assets/60.webp)
PR của bạn sau đó sẽ được hiển thị trong tab `Pull Request` của kho lưu trữ chính của PlanB Network. Bạn chỉ cần chờ đợi cho đến khi một quản trị viên liên hệ với bạn để xác nhận việc hợp nhất đóng góp của bạn hoặc yêu cầu bất kỳ sửa đổi bổ sung nào.
![github](assets/61.webp)
Sau khi hợp nhất PR của bạn với nhánh chính, được khuyến nghị xóa nhánh làm việc của bạn (`add-professor-your-name`) để duy trì lịch sử sạch sẽ trên fork của bạn. GitHub sẽ tự động cung cấp cho bạn tùy chọn này trên trang PR của bạn:
![github](assets/62.webp)
Trên phần mềm GitHub Desktop, bạn có thể chuyển trở lại nhánh chính của fork của bạn (`dev`).

![github](assets/63.webp)

Nếu bạn muốn thực hiện thay đổi đối với đóng góp của mình sau khi bạn đã gửi PR của mình, quy trình cần tuân theo phụ thuộc vào trạng thái hiện tại của PR của bạn:
- Nếu PR của bạn vẫn đang mở và chưa được hợp nhất, hãy thực hiện các thay đổi một cách cục bộ trong khi vẫn ở trên cùng một nhánh. Sau khi các sửa đổi được hoàn thiện, sử dụng nút `Push origin` để thêm một commit mới vào PR vẫn đang mở của bạn;
- Trong trường hợp PR của bạn đã được hợp nhất với nhánh chính, bạn sẽ cần bắt đầu quy trình từ đầu bằng cách tạo một nhánh mới, sau đó gửi một PR mới. Đảm bảo rằng kho lưu trữ cục bộ của bạn được đồng bộ hóa với kho lưu trữ nguồn của Mạng PlanB trước khi tiến hành.
## Bước 9: Thêm Một Hướng Dẫn Mới
Xin chúc mừng, bạn đã hoàn thành tất cả các bước chuẩn bị! Bây giờ bạn đã sẵn sàng để đóng góp cho Mạng PlanB. Từ bây giờ, cho mỗi bài viết mới bạn muốn xuất bản, bạn sẽ cần tạo một nhánh mới từ `dev`. Một nhánh trong Git là một phiên bản song song của dự án, cho phép bạn thực hiện các thay đổi mà không ảnh hưởng đến nhánh chính, cho đến khi công việc sẵn sàng để được hợp nhất.

Trước khi tiến hành tạo một nhánh mới, điều quan trọng là đảm bảo bạn đang làm việc trên phiên bản mới nhất của dự án để giảm thiểu rủi ro xung đột khi hợp nhất các thay đổi của bạn. Để làm điều này, mở trình duyệt của bạn và truy cập vào trang fork của bạn từ kho lưu trữ PlanB. Đây là fork bạn đã thiết lập trên GitHub ở bước 4. URL của fork của bạn sẽ trông giống như: `https://github.com/[tên-người-dùng-của-bạn]/sovereign-university-data`.
![github](assets/34.webp)
Đảm bảo bạn đang ở trên nhánh chính `dev` sau đó nhấp vào nút `Sync fork`. Nếu fork của bạn không cập nhật, GitHub sẽ đề nghị cập nhật nhánh của bạn. Tiến hành cập nhật này. Ngược lại, nếu nhánh của bạn đã cập nhật, GitHub sẽ thông báo cho bạn. ![github](assets/35.webp)
Bây giờ fork của bạn trên GitHub đã được đồng bộ hóa với kho lưu trữ nguồn của Mạng PlanB, đã đến lúc làm mới kho lưu trữ cục bộ trên máy tính của bạn. Mở phần mềm GitHub Desktop và đảm bảo fork của bạn được chọn đúng cách ở góc trên bên trái của cửa sổ.

![github](assets/36.webp)

Nhấp vào nút `Fetch origin`. Nếu kho lưu trữ cục bộ của bạn đã cập nhật, GitHub Desktop sẽ không đề xuất thêm hành động nào. Ngược lại, tùy chọn `Pull origin` sẽ xuất hiện. Nhấp vào nút này để cập nhật kho lưu trữ cục bộ của bạn.

![github](assets/37.webp)

Sau khi đồng bộ hóa kho lưu trữ của bạn với những đóng góp mới nhất, bạn đã sẵn sàng để tạo một nhánh làm việc mới. Vẫn từ GitHub Desktop, xác minh rằng bạn thực sự đang ở trên nhánh chính `dev`.

![github](assets/38.webp)

Nhấp vào nhánh này, sau đó nhấp vào nút `New Branch`.

![github](assets/64.webp)

Đảm bảo nhánh mới được dựa trên kho lưu trữ nguồn, cụ thể là `DecouvreBitcoin/sovereign-university-data`. Đặt tên cho nhánh của bạn một cách rõ ràng về mục đích của nó, sử dụng dấu gạch ngang để phân cách từng từ. Ví dụ, giả sử mục tiêu của chúng ta là viết một hướng dẫn về việc sử dụng phần mềm Sparrow Wallet. Trong trường hợp này, nhánh làm việc dành riêng cho việc viết hướng dẫn này có thể được đặt tên: `tuto-sparrow-wallet-loic`. Sau khi nhập tên phù hợp, bạn chỉ cần nhấp vào `Create branch` để xác nhận việc tạo nhánh.

![github](assets/65.webp)

Bây giờ nhấp vào nút `Publish branch` để lưu nhánh làm việc mới của bạn trên fork trực tuyến trên GitHub.

![github](assets/66.webp)
Tại thời điểm này, trên GitHub Desktop, bạn sẽ thấy mình đang ở trên nhánh mới của mình. Điều này có nghĩa là tất cả các thay đổi được thực hiện trên máy tính của bạn sẽ chỉ được ghi lại trên nhánh cụ thể này. Ngoài ra, miễn là nhánh này vẫn được chọn trên GitHub Desktop, các tệp tin hiển thị trên máy của bạn sẽ tương ứng với những tệp tin của nhánh này (`tuto-sparrow-wallet-loic`), và không phải là những tệp tin của nhánh chính (`dev`).
![github](assets/68.webp)
Bây giờ, khi nhánh làm việc đã được tạo, đã đến lúc tích hợp hướng dẫn mới của bạn. Để làm điều này, mở trình quản lý tệp tin của bạn và điều hướng đến thư mục `sovereign-university-data`, đại diện cho bản sao cục bộ của kho lưu trữ của bạn. Bạn nên tìm thấy nó dưới `Documents\GitHub\sovereign-university-data`. Trong thư mục này, sẽ cần phải xác định thư mục phụ thích hợp để đặt hướng dẫn của bạn. Cách tổ chức các thư mục phản ánh các phần khác nhau của trang web Mạng PlanB. Trong ví dụ của chúng tôi, vì chúng tôi muốn thêm một hướng dẫn về Sparrow Wallet, nên đi đến đường dẫn sau: `sovereign-university-data\tutorials\wallet` tương ứng với phần `WALLET` trên trang web.
![github](assets/69.webp)

Trong thư mục `wallet`, bạn cần tạo một thư mục mới cụ thể dành riêng cho hướng dẫn của bạn. Tên của thư mục này nên gợi lên phần mềm được đề cập trong hướng dẫn, đảm bảo kết nối các từ bằng dấu gạch ngang. Đối với ví dụ của tôi, thư mục sẽ được đặt tên là `sparrow-wallet`.

![github](assets/70.webp)

Trong thư mục mới này dành riêng cho hướng dẫn của bạn, cần chuẩn bị các yếu tố khác nhau:
- Tạo một thư mục `assets`, dành để nhận tất cả các hình minh họa cần thiết cho hướng dẫn của bạn;
	- Trong thư mục `assets` này, bạn cần tạo 6 thư mục phụ có tên là `fr`, `de`, `en`, `it`, `es`, và `pt`, để phân loại hình ảnh theo ngôn ngữ tương ứng.
- Một tệp tin `tutorial.yml` phải được tạo để ghi lại các chi tiết liên quan đến hướng dẫn của bạn;
- Một tệp tin định dạng markdown cần được tạo để viết nội dung thực sự của hướng dẫn. Tệp tin này phải được đặt tên theo mã ngôn ngữ của bài viết. Ví dụ, cho một hướng dẫn viết bằng tiếng Pháp, tệp tin phải được gọi là `fr.md`.

Cách tổ chức thư mục của bạn nên trông như thế này:

![github](assets/71.webp)

Để bắt đầu, mở tệp tin `tutorial.yml` của bạn bằng trình soạn thảo mã của bạn. Điền vào nó với thông tin được chỉ định dưới đây:
- **builder**: Nhập tiêu đề của hướng dẫn của bạn, phải vừa chính xác vừa gợi lên nội dung bạn sẽ trình bày;
- **tags**: Xác định một loạt từ khóa chặt chẽ liên quan đến chủ đề của bài viết của bạn, để tạo điều kiện cho việc tìm kiếm và lập chỉ mục của nó;
- **category**: Chọn một phân loại phụ thích hợp trong số những phân loại có sẵn trên trang PlanB, dựa trên nội dung của hướng dẫn của bạn. Ví dụ, cho một hướng dẫn liên quan đến phần `WALLET`, các tùy chọn có sẵn là `Desktop`, `Hardware`, và `Mobile`;
- **level**: Chỉ ra mức độ khó của hướng dẫn của bạn bằng cách chọn một trong bốn phân loại sau:
	- Người mới bắt đầu (`beginner`),
	- Trung cấp (`intermediary`),
	- Nâng cao (`advanced`),
- Chuyên gia (`expert`).- **professor**: Nhập ID người đóng góp của bạn như nó xuất hiện trên hồ sơ giáo sư của bạn. Để biết thêm chi tiết, tham khảo bước 8 của bài viết này;
- **link** (tùy chọn): Nếu bạn muốn ghi công một trang web nguồn cho hướng dẫn bạn đang phát triển, như trang cá nhân của bạn, đây là nơi bạn có thể thêm liên kết liên quan.
![github](assets/72.webp)
Sau khi bạn đã hoàn thành việc chỉnh sửa tệp `tutorial.yml` của mình, hãy lưu tài liệu bằng cách nhấp vào `File > Save`. Bây giờ bạn có thể đóng trình soạn thảo mã của mình.

![github](assets/73.webp)

Trong thư mục `assets`, bạn cần thêm một tệp có tên là `logo.webp`, sẽ được sử dụng như một hình thu nhỏ cho bài viết của bạn. Hình ảnh này, phải ở định dạng `.webp`, nên có kích thước vuông để phù hợp với giao diện người dùng. Bạn có thể tự do chọn logo của phần mềm được đề cập trong hướng dẫn hoặc bất kỳ hình ảnh liên quan nào khác, miễn là nó không vi phạm bản quyền.

Ngoài ra, cũng thêm một hình ảnh với tiêu đề `cover.webp` tại cùng một vị trí. Hình ảnh này sẽ được hiển thị ở đầu hướng dẫn của bạn. Đảm bảo rằng hình ảnh này, giống như logo, tuân thủ quyền sử dụng và phù hợp với bối cảnh của hướng dẫn của bạn.

![github](assets/74.webp)

Các thư mục ngôn ngữ nằm trong thư mục `assets` được sử dụng để tổ chức các sơ đồ và hình ảnh minh họa sẽ đi kèm với hướng dẫn của bạn. Nếu hình ảnh của bạn chứa văn bản, hãy xem xét việc dịch chúng cho mỗi ngôn ngữ liên quan, để làm cho nội dung của bạn dễ tiếp cận với khán giả quốc tế.

**-> Mẹo:** Khi chia sẻ các tệp công khai, như hình ảnh, điều quan trọng là loại bỏ metadata không cần thiết. Chúng có thể chứa thông tin nhạy cảm, như dữ liệu vị trí, ngày tạo, hoặc chi tiết về tác giả. Để bảo vệ sự riêng tư, bạn nên xóa metadata này. Để đơn giản hóa thao tác này, bạn có thể sử dụng các công cụ chuyên biệt như [Exif Cleaner](https://exifcleaner.com/), cho phép làm sạch metadata của một tài liệu thông qua thao tác kéo và thả đơn giản.

Bây giờ, bạn có thể mở tệp sẽ chứa hướng dẫn của mình, được đặt tên theo mã ngôn ngữ của bạn, như `en.md`. Đi đến Obsidian, ở phía bên trái của cửa sổ, cuộn qua cây thư mục cho đến khi bạn tìm thấy thư mục của hướng dẫn và tệp bạn đang tìm kiếm.

![github](assets/75.webp)

Nhấp vào tệp để mở nó.

![github](assets/76.webp)

Chúng ta sẽ bắt đầu bằng cách điền vào phần `Properties` ở đầu tài liệu. Trong trường hợp phần này không có trong tệp của bạn (nếu tài liệu hoàn toàn trống), bạn có thể tái tạo nó bằng cách sao chép từ một hướng dẫn khác đã tồn tại.

![github](assets/77.webp)
Bạn cũng có thể thêm nó một cách thủ công theo cách này bằng trình soạn thảo mã của mình:
![github](assets/78.webp)

Điền tên của hướng dẫn cũng như một mô tả ngắn gọn về nó.

![github](assets/79.webp)

Sau đó thêm hình ảnh bìa của bạn vào đầu hướng dẫn. Để làm điều này, gõ:

`![cover-sparrow](assets/cover.webp)`

Cú pháp này sẽ hữu ích mỗi khi cần thêm một hình ảnh vào hướng dẫn của bạn. Dấu chấm than biểu thị đó là một hình ảnh, với văn bản thay thế (alt) được chỉ định giữa các dấu ngoặc vuông. Đường dẫn đến hình ảnh được chỉ định giữa các dấu ngoặc đơn.

![github](assets/80.webp)

Tiếp tục viết hướng dẫn của bạn bằng cách viết nội dung của bạn. Khi bạn muốn tích hợp một tiêu đề phụ, áp dụng định dạng markdown phù hợp bằng cách thêm tiền tố cho văn bản với `##`.

![github](assets/81.webp)

Khi thêm các yếu tố hình ảnh vào hướng dẫn của bạn, hãy chắc chắn chọn đường dẫn tương ứng với ngôn ngữ nội dung của bạn. Ví dụ:

`![sparrow](assets/1.webp)`

![github](assets/82.webp)
Nếu hình ảnh của bạn chứa văn bản, chẳng hạn như một sơ đồ, bạn nên dịch nó sang sáu ngôn ngữ đề xuất (Tiếng Đức, Tiếng Anh, Tiếng Pháp, Tiếng Ý, Tiếng Tây Ban Nha, và Tiếng Bồ Đào Nha) và đặt mỗi phiên bản dịch trong thư mục con ngôn ngữ tương ứng của nó trong thư mục `assets`.
Các hình ảnh phải được đánh số tuần tự theo thứ tự xuất hiện của chúng trong hướng dẫn. Do đó, hình ảnh đầu tiên sẽ được đặt tên là `1.webp`, hình ảnh thứ hai là `2.webp`, và cứ thế tiếp tục. Bạn có thể sử dụng các định dạng hình ảnh khác nhau như `jpeg`, `png`, hoặc `webp`.
![github](assets/83.webp)
Sau khi bạn hoàn thành việc viết hướng dẫn của mình bằng ngôn ngữ bạn chọn, bước tiếp theo là gửi một Pull Request. Người quản trị sau đó sẽ thêm năm bản dịch còn thiếu của hướng dẫn của bạn, nhờ vào phương pháp dịch tự động của chúng tôi. Để tiến hành với Pull Request, mở phần mềm GitHub Desktop. Nó sẽ tự động phát hiện những thay đổi bạn đã thực hiện so với kho lưu trữ gốc. Trước khi tiếp tục, hãy kiểm tra cẩn thận ở phía bên trái của giao diện rằng những thay đổi này chính xác là những gì bạn mong đợi.

![github](assets/84.webp)

Nếu những thay đổi đó đúng với bạn, hãy thêm một tiêu đề cho lần commit của bạn. Một commit là một lưu của những thay đổi đã thực hiện đối với nhánh, đi kèm với một thông điệp mô tả, cho phép theo dõi sự phát triển của một dự án theo thời gian. Sau khi tiêu đề được nhập, nhấn vào nút màu xanh `Commit to [nhánh của bạn]` để xác nhận những thay đổi này.

![github](assets/85.webp)

Sau đó nhấn vào nút `Push origin`. Điều này sẽ gửi commit của bạn đến fork của bạn.

![github](assets/86.webp)
Nếu bạn đã hoàn thành chỉnh sửa cho nhánh này, bây giờ hãy nhấn vào nút `Preview Pull Request`.
![github](assets/87.webp)

Bạn có thể kiểm tra một lần cuối cùng rằng các chỉnh sửa của bạn là chính xác, sau đó nhấn vào nút `Create pull request`.

![github](assets/88.webp)

Bạn sẽ được tự động chuyển hướng đến trình duyệt trên GitHub đến trang chuẩn bị của Pull Request của bạn. Một Pull Request là một yêu cầu được thực hiện để tích hợp các thay đổi từ nhánh của bạn vào nhánh chính của kho lưu trữ PlanB Network, cho phép xem xét và thảo luận về các thay đổi trước khi chúng được hợp nhất.
![github](assets/89.webp)
Trên trang chuẩn bị này, chỉ ra một tiêu đề tóm tắt ngắn gọn các chỉnh sửa bạn muốn hợp nhất với kho lưu trữ nguồn. Thêm một bình luận ngắn mô tả những thay đổi này. Sau khi hoàn thành những bước này, nhấn vào nút màu xanh lá `Create pull request` để xác nhận yêu cầu hợp nhất.
![github](assets/90.webp)
PR của bạn sau đó sẽ hiển thị trong tab `Pull Request` của kho lưu trữ chính của PlanB Network. Bây giờ, tất cả những gì bạn phải làm là chờ đợi cho đến khi một người quản trị liên hệ với bạn để xác nhận việc hợp nhất đóng góp của bạn hoặc để yêu cầu bất kỳ chỉnh sửa bổ sung nào.
![github](assets/91.webp)
Sau khi hợp nhất PR của bạn với nhánh chính, bạn được khuyến khích xóa nhánh làm việc của mình (`tuto-sparrow-wallet`) để duy trì lịch sử sạch sẽ trên fork của bạn. GitHub sẽ tự động cung cấp cho bạn tùy chọn này trên trang của PR của bạn:
![github](assets/92.webp)
Trên phần mềm GitHub Desktop, bạn có thể chuyển lại sang nhánh chính của fork của bạn (`dev`).

![github](assets/63.webp)

Nếu bạn muốn thực hiện chỉnh sửa đối với đóng góp của mình sau khi đã gửi PR của mình, quy trình cần tuân theo phụ thuộc vào trạng thái hiện tại của PR của bạn:
- Nếu PR của bạn vẫn đang mở và chưa được hợp nhất, thực hiện các chỉnh sửa một cách địa phương trong khi vẫn ở trên cùng một nhánh. Một khi các chỉnh sửa được hoàn thiện, sử dụng nút `Push origin` để thêm một commit mới vào PR vẫn đang mở của bạn;
Trong trường hợp PR của bạn đã được hợp nhất với nhánh chính, bạn sẽ cần phải bắt đầu lại quy trình từ đầu bằng cách tạo một nhánh mới, sau đó gửi một PR mới. Đảm bảo rằng kho lưu trữ cục bộ của bạn đã được đồng bộ hóa với kho lưu trữ nguồn của Mạng PlanB trước khi tiến hành.