---
name: GitHub Desktop
description: Cách thiết lập môi trường làm việc cục bộ của bạn?
---
![github](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn tài nguyên giáo dục hàng đầu về Bitcoin bằng càng nhiều ngôn ngữ khác nhau càng tốt. Tất cả nội dung được công bố trên trang web đều là mã nguồn mở và được lưu trữ trên GitHub, điều này cho phép bất kỳ ai cũng có thể tham gia vào việc làm giàu cho nền tảng. Sự đóng góp có thể có nhiều hình thức: sửa chữa và hiệu đính các văn bản hiện có, dịch sang ngôn ngữ khác, cập nhật thông tin, hoặc tạo mới các hướng dẫn chưa có trên trang web của chúng tôi.

Nếu bạn muốn đóng góp cho Mạng lưới PlanB, bạn sẽ cần sử dụng GitHub để đề xuất thay đổi. Để làm điều này, bạn có hai lựa chọn:
- **Đóng góp trực tiếp qua giao diện web của GitHub**: Đây là phương pháp đơn giản nhất. Nếu bạn là người mới hoặc nếu bạn chỉ dự định đóng góp một vài sửa đổi nhỏ, lựa chọn này có lẽ là tốt nhất cho bạn;
- **Đóng góp cục bộ sử dụng Git**: Phương pháp này phù hợp hơn nếu bạn dự định đóng góp thường xuyên hoặc đáng kể cho Mạng lưới PlanB. Mặc dù việc thiết lập môi trường Git cục bộ trên máy tính của bạn có thể có vẻ phức tạp ban đầu, nhưng cách tiếp cận này hiệu quả hơn trong dài hạn. Nó cho phép quản lý thay đổi linh hoạt hơn. Nếu bạn mới làm quen với điều này, đừng lo, **chúng tôi giải thích toàn bộ quy trình thiết lập môi trường của bạn trong hướng dẫn này** (hứa, bạn sẽ không cần phải gõ bất kỳ dòng lệnh nào ^^).

Nếu bạn không biết GitHub là gì, hoặc nếu bạn muốn tìm hiểu thêm về các thuật ngữ kỹ thuật liên quan đến Git và GitHub, tôi khuyên bạn đọc bài viết giới thiệu của chúng tôi để làm quen với những khái niệm này.

https://planb.network/tutorials/others/contribution/basics-of-github-471f7f00-8b5a-4b63-abb1-f1528b032bbb



- Để bắt đầu, rõ ràng bạn sẽ cần một tài khoản GitHub. Nếu bạn đã có một, bạn có thể đăng nhập, nếu không, bạn có thể sử dụng hướng dẫn của chúng tôi để tạo một tài khoản mới.

https://planb.network/tutorials/others/contribution/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



## Bước 1: Cài đặt GitHub Desktop

- Truy cập https://desktop.github.com/ để tải phần mềm GitHub Desktop. Phần mềm này cho phép bạn tương tác dễ dàng với GitHub, mà không cần phải sử dụng terminal:
![github-desktop](assets/1.webp)
- Khi bạn khởi chạy phần mềm lần đầu tiên, bạn sẽ được yêu cầu kết nối tài khoản GitHub của mình. Để làm điều này, nhấp vào `Sign in to GitHub.com`:
![github-desktop](assets/2.webp)
- Một trang xác thực sẽ mở trong trình duyệt của bạn. Nhập địa chỉ email và mật khẩu bạn đã chọn khi tạo tài khoản, sau đó nhấp vào nút `Sign in`:
![github-desktop](assets/3.webp)
- Nhấp vào `Authorize desktop` để xác nhận kết nối giữa tài khoản của bạn và phần mềm:
![github-desktop](assets/4.webp)
- Bạn sẽ được tự động chuyển hướng đến phần mềm GitHub Desktop. Nhấp vào `Finish`: ![github-desktop](assets/5.webp)
- Nếu bạn vừa mới tạo tài khoản GitHub của mình, bạn sẽ được chuyển hướng đến một trang thông báo rằng bạn chưa tạo bất kỳ kho lưu trữ nào. Tại thời điểm này, hãy để GitHub Desktop sang một bên; chúng tôi sẽ quay lại với nó sau: ![github-desktop](assets/6.webp)

## Bước 2: Cài đặt Obsidian

Chúng ta tiếp tục với việc cài đặt phần mềm viết. Ở đây, bạn có một số lựa chọn. Bạn sẽ cần phần mềm hỗ trợ chỉnh sửa các tệp Markdown, vì Mạng lưới PlanB sử dụng định dạng này cho các tệp văn bản trong kho lưu trữ của mình.
Có rất nhiều phần mềm chuyên dụng để chỉnh sửa các tệp Markdown, như Typora, được thiết kế đặc biệt cho việc viết lách. Mặc dù không lý tưởng, nhưng cũng có thể chọn một trình biên tập mã, như Visual Studio Code (VSC) hoặc Sublime Text. Tuy nhiên, với tư cách là một nhà văn, tôi thích sử dụng phần mềm Obsidian. Hãy cùng nhau xem cách cài đặt và bắt đầu sử dụng nó.
- Truy cập https://obsidian.md/download và tải xuống phần mềm: ![github-desktop](assets/7.webp)
- Cài đặt Obsidian, khởi chạy phần mềm, chọn ngôn ngữ của bạn, sau đó nhấp vào `Quick Start`: ![github-desktop](assets/8.webp)
- Bạn sẽ đến với phần mềm Obsidian. Hiện tại, bạn chưa mở tệp nào: ![github-desktop](assets/9.webp)

## Bước 3: Fork kho lưu trữ PlanB Network

- Truy cập vào kho dữ liệu PlanB Network tại địa chỉ sau: [https://github.com/PlanB-Network/bitcoin-educational-content](https://github.com/PlanB-Network/bitcoin-educational-content): ![github-desktop](assets/10.webp)
- Từ trang này, nhấp vào nút `Fork` ở góc trên bên phải của cửa sổ: ![github-desktop](assets/11.webp)
- Trong menu tạo mới, bạn có thể để nguyên cài đặt mặc định. Đảm bảo rằng ô `Copy the dev branch only` đã được chọn, sau đó nhấp vào nút `Create fork`: ![github-desktop](assets/12.webp)
- Bạn sẽ đến với fork của riêng mình của kho lưu trữ PlanB Network: ![github-desktop](assets/13.webp)
Fork này tạo thành một kho lưu trữ riêng biệt từ bản gốc, mặc dù hiện tại nó vẫn chứa cùng một dữ liệu. Bây giờ bạn sẽ làm việc trên kho lưu trữ mới này.

Chúng ta đã, theo một cách nào đó, tạo một bản sao của kho lưu trữ nguồn PlanB Network. Fork của bạn (bản sao) và kho lưu trữ gốc giờ đây sẽ phát triển độc lập với nhau. Trên kho lưu trữ gốc, các đóng góp viên khác có thể thêm dữ liệu mới, trong khi bạn, trên fork của mình, sẽ tiến hành các chỉnh sửa của riêng mình.
Để duy trì sự nhất quán giữa hai kho lưu trữ này, sẽ cần thiết phải đồng bộ chúng định kỳ để chúng lấy cùng một thông tin. Để gửi các thay đổi của bạn đến kho lưu trữ nguồn, bạn sẽ sử dụng cái gọi là **Pull Request**. Và để tích hợp các thay đổi từ kho lưu trữ nguồn vào fork của bạn, bạn sẽ sử dụng lệnh **Sync fork** có sẵn trên giao diện web của GitHub.
![github-desktop](assets/14.webp)

## Bước 4: Clone fork

- Quay trở lại phần mềm GitHub Desktop. Bây giờ, fork của bạn nên xuất hiện trong mục `Your repositories`. Nếu bạn không thấy ngay lập tức, sử dụng nút mũi tên kép để làm mới danh sách. Khi fork của bạn xuất hiện, nhấp vào nó để chọn:
![github-desktop](assets/15.webp)
- Sau đó nhấp vào nút màu xanh: `Clone [username]/bitcoin-educational-content`:
![github-desktop](assets/16.webp)
- Giữ nguyên đường dẫn mặc định. Để xác nhận, nhấp vào nút màu xanh `Clone`:
![github-desktop](assets/17.webp)
- Chờ trong khi GitHub Desktop clone fork của bạn về máy cục bộ:
![github-desktop](assets/18.webp)
- Sau khi sao chép kho lưu trữ, phần mềm sẽ cung cấp cho bạn hai lựa chọn. Bạn phải chọn lựa chọn đầu tiên: `Đóng góp cho dự án mẹ`. Lựa chọn này sẽ cho phép bạn trình bày công việc tương lai của mình như là một đóng góp cho dự án mẹ (`PlanB-Network/bitcoin-educational-content`), và không chỉ là sửa đổi riêng lẻ của bản sao cá nhân của bạn (`[username]/bitcoin-educational-content`). Sau khi lựa chọn được chọn, nhấp vào `Tiếp tục`: ![github-desktop](assets/19.webp)
- GitHub Desktop của bạn giờ đây đã được cấu hình đúng cách. Bây giờ, bạn có thể để phần mềm mở ở chế độ nền để theo dõi các thay đổi mà chúng tôi sẽ thực hiện.
![github-desktop](assets/20.webp)
Những gì chúng ta đã đạt được ở giai đoạn này là việc tạo ra một bản sao cục bộ của kho lưu trữ của bạn, được lưu trữ trên GitHub. Như một lời nhắc nhở, kho lưu trữ này là một bản sao của kho lưu trữ nguồn của PlanB Network. Bạn sẽ có thể thực hiện các thay đổi đối với bản sao cục bộ này, chẳng hạn như thêm hướng dẫn, bản dịch, hoặc sửa đổi. Một khi những thay đổi này được thực hiện, bạn sẽ sử dụng lệnh **Push origin** để gửi các thay đổi cục bộ của mình lên bản sao của bạn được lưu trữ trên GitHub.

Bạn cũng có thể lấy các thay đổi từ bản sao, ví dụ, trong quá trình đồng bộ hóa với kho lưu trữ của PlanB Network. Để làm điều này, bạn sẽ sử dụng lệnh **Fetch origin** để tải các thay đổi về bản sao cục bộ của mình (bản sao của bạn), và sau đó sử dụng lệnh **Pull origin** để hợp nhất chúng với công việc của mình. Điều này cho phép bạn cập nhật với những phát triển mới nhất của dự án trong khi đóng góp hiệu quả.

![github-desktop](assets/21.webp)
## Bước 5: Tạo một kho lưu trữ mới trên Obsidian

- Mở phần mềm Obsidian và nhấp vào biểu tượng kho lưu trữ nhỏ ở góc dưới bên trái của cửa sổ:
![github-desktop](assets/22.webp)
- Nhấp vào nút `Mở` để mở một thư mục hiện có như một kho lưu trữ: ![github-desktop](assets/23.webp)
- Trình duyệt tệp của bạn sẽ mở ra. Bạn cần tìm và chọn thư mục có tiêu đề `GitHub`, nó nên nằm trong thư mục `Documents` giữa các tệp của bạn. Đường dẫn này tương ứng với đường dẫn bạn thiết lập trong bước 4. Sau khi chọn thư mục, xác nhận lựa chọn của mình. Việc tạo kho lưu trữ của bạn trên Obsidian sau đó sẽ được khởi động trên một trang mới của phần mềm:

![github-desktop](assets/24.webp)
-> **Chú ý**, điều quan trọng là không chọn thư mục `bitcoin-educational-content` khi tạo một kho lưu trữ mới trên Obsidian. Thay vào đó, hãy chọn thư mục cha, `GitHub`. Nếu bạn chọn thư mục `bitcoin-educational-content`, thư mục cấu hình `.obsidian`, chứa cài đặt Obsidian cục bộ của bạn, sẽ tự động được tích hợp vào kho lưu trữ. Chúng ta muốn tránh điều này, vì không cần thiết phải chuyển cài đặt Obsidian của bạn sang kho lưu trữ của PlanB Network. Một phương án khác là thêm thư mục `.obsidian` vào tệp `.gitignore`, nhưng phương pháp này cũng sẽ thay đổi tệp `.gitignore` của kho lưu trữ nguồn, điều này không mong muốn.

- Ở phía bên trái của cửa sổ, bạn có thể thấy cây tệp với các kho lưu trữ GitHub khác nhau của bạn đã được sao chép cục bộ.
- Bằng cách nhấp vào các mũi tên cạnh tên thư mục, bạn có thể mở rộng chúng để truy cập vào các thư mục con của các kho lưu trữ và tài liệu của chúng:
![github-desktop](assets/25.webp)
- Đừng quên thiết lập Obsidian sang chế độ tối: "Ánh sáng thu hút côn trùng" ;)

## Bước 6: Cài đặt một Trình Biên Tập Mã
Hầu hết các sửa đổi của bạn sẽ được thực hiện trên các tệp định dạng Markdown (`.md`). Để chỉnh sửa những tài liệu này, bạn có thể sử dụng Obsidian, phần mềm mà chúng ta đã thảo luận trước đó. Tuy nhiên, PlanB Network sử dụng các định dạng tệp khác, và bạn sẽ cần phải chỉnh sửa một số trong số chúng.

Ví dụ, khi tạo một hướng dẫn mới, bạn sẽ cần tạo một tệp YAML (`.yml`) để nhập các thẻ cho hướng dẫn của bạn, tiêu đề và ID giáo viên của bạn. Obsidian không cung cấp khả năng chỉnh sửa loại tệp này, vì vậy bạn sẽ cần một trình soạn thảo mã.

Đối với việc này, có một số lựa chọn có sẵn cho bạn. Mặc dù notepad chuẩn của máy tính bạn có thể được sử dụng cho những sửa đổi này, giải pháp này không lý tưởng cho công việc gọn gàng. Tôi khuyên bạn nên chọn phần mềm được thiết kế đặc biệt cho mục đích này, như [VS Code](https://code.visualstudio.com/download) hoặc [Sublime Text](https://www.sublimetext.com/download). Sublime Text, với tính năng nhẹ nhàng đặc biệt, sẽ hơn là đủ cho nhu cầu của chúng ta.
- Cài đặt một trong những phần mềm này, và giữ nó sang một bên cho những sửa đổi tương lai của bạn. ![github-desktop](assets/26.webp)
Xin chúc mừng! Môi trường làm việc của bạn giờ đây đã được thiết lập để đóng góp cho PlanB Network. Bạn giờ đây có thể khám phá các hướng dẫn cụ thể khác của chúng tôi cho từng loại đóng góp (dịch thuật, hiệu đính, viết.

https://planb.network/tutorials/others

..).
