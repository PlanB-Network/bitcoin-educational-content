---
name: GitHub Desktop
description: Cách thiết lập môi trường làm việc cục bộ của bạn?
---
![github](assets/cover.webp)

Sứ mệnh của PlanB là cung cấp nguồn học liệu hàng đầu về Bitcoin bằng nhiều ngôn ngữ nhất có thể. Toàn bộ nội dung được đăng tải trên trang web đều là mã nguồn mở và được lưu trữ trên GitHub, tạo điều kiện cho bất kỳ ai cũng có thể tham gia đóng góp và làm phong phú thêm kho kiến thức chung này. Đóng góp có thể dưới nhiều hình thức: sửa lỗi và soát lỗi các văn bản hiện có, dịch sang các ngôn ngữ khác, cập nhật thông tin hoặc tạo các hướng dẫn mới chưa có trên trang web của chúng tôi.

Nếu bạn muốn đóng góp cho Plan ₿ Academy, bạn cần sử dụng GitHub để đề xuất thay đổi. Để làm điều này, bạn có hai lựa chọn:
- **Đóng góp trực tiếp qua giao diện web của GitHub**: Đây là phương pháp đơn giản nhất. Nếu bạn là người mới hoặc nếu bạn chỉ dự định đóng góp một vài sửa đổi nhỏ, lựa chọn này có lẽ là tốt nhất cho bạn;
- **Đóng góp cục bộ sử dụng Git**: Phương pháp này phù hợp hơn nếu bạn dự định đóng góp thường xuyên hoặc đáng kể cho Plan ₿ Academy. Mặc dù việc thiết lập môi trường Git cục bộ trên máy tính thoạt nhìn có vẻ phức tạp, nhưng cách tiếp cận này hiệu quả hơn về lâu dài. Nó cho phép quản lý các thay đổi linh hoạt hơn. Nếu bạn mới bắt đầu với việc này, đừng lo, **chúng tôi sẽ giải thích toàn bộ quy trình thiết lập môi trường làm việc trong hướng dẫn này** (chúng tôi hứa là bạn sẽ không cần phải gõ bất kỳ dòng lệnh nào ^^).

Nếu bạn không biết GitHub là gì, hoặc nếu bạn muốn tìm hiểu thêm về các thuật ngữ kỹ thuật liên quan đến Git và GitHub, tôi khuyên bạn đọc bài viết giới thiệu của chúng tôi để làm quen với những khái niệm này.

- Để bắt đầu, tất nhiên bạn sẽ cần một tài khoản GitHub. Nếu bạn đã có sẵn, bạn có thể đăng nhập. Nếu chưa có, bạn có thể xem hướng dẫn của chúng tôi để tạo tài khoản mới.

https://planb.academy/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c



## Bước 1: Cài đặt GitHub Desktop

- Truy cập https://desktop.github.com/ để tải phần mềm GitHub Desktop. Phần mềm này cho phép bạn tương tác dễ dàng với GitHub mà không cần phải gõ dòng lệnh (terminal):

![github-desktop](assets/1.webp)

- Khi khởi chạy lần đầu, phần mềm sẽ yêu cầu kết nối với tài khoản GitHub. Hãy nhấn vào `Sign in to GitHub.com`:

![github-desktop](assets/2.webp)

- Trình duyệt sẽ mở trang xác thực. Nhập email và mật khẩu tài khoản của bạn, sau đó nhấn nút `Sign in`:

![github-desktop](assets/3.webp)

- Nhấn `Authorize desktop` để xác nhận kết nối giữa tài khoản và phần mềm:

![github-desktop](assets/4.webp)

- Bạn sẽ được tự động chuyển hướng quay lại phần mềm GitHub Desktop. Nhấn `Finish`:

![github-desktop](assets/5.webp)

- Nếu bạn vừa mới tạo tài khoản GitHub của mình, bạn sẽ thấy thông báo chưa có kho lưu trữ (repository) nào. Tạm thời hãy để GitHub Desktop đó, chúng ta sẽ quay lại sau:

![github-desktop](assets/6.webp)

## Bước 2: Cài đặt Obsidian

Tiếp theo, chúng ta sẽ cài đặt phần mềm soạn thảo. Bạn sẽ cần một phần mềm hỗ trợ chỉnh sửa các tệp Markdown, vì Plan ₿ Academy sử dụng định dạng này cho các tệp văn bản trong kho lưu trữ của mình.

Có rất nhiều phần mềm chuyên dụng để chỉnh sửa các tệp Markdown, chẳng hạn như Typora - được thiết kế đặc biệt cho việc viết lách. Mặc dù không phải là lý tưởng nhất, nhưng  bạn cũng có thể chọn một trình biên tập mã, như Visual Studio Code (VSC) hoặc Sublime Text. Tuy nhiên, với tư cách là một người viết lách, tôi ưu tiên sử dụng Obsidian. Hãy cùng xem cách cài đặt và bắt đầu sử dụng nó.

- Truy cập https://obsidian.md/download và tải xuống phần mềm:

![github-desktop](assets/7.webp)

- Cài đặt Obsidian, khởi chạy phần mềm, chọn ngôn ngữ của bạn, sau đó nhấp vào `Quick Start`:

![github-desktop](assets/8.webp)

- Bạn sẽ đến với phần mềm Obsidian. Hiện tại, bạn chưa có tệp nào được mở:

![github-desktop](assets/9.webp)

## Bước 3: Fork kho lưu trữ Plan ₿ Academy

- Truy cập vào kho lưu trữ dữ liệu Plan ₿ Academy tại địa chỉ: [https://github.com/PlanB-Network/bitcoin-educational-content](https://github.com/PlanB-Network/bitcoin-educational-content):

![github-desktop](assets/10.webp)

- Từ trang này, nhấp vào nút `Fork` ở góc trên bên phải của cửa sổ:

![github-desktop](assets/11.webp)

- Trong menu tạo mới, bạn có thể để nguyên các thiết lập mặc định. Đảm bảo rằng ô `Copy the dev branch only` đã được chọn, sau đó nhấn vào nút `Create fork`:

![github-desktop](assets/12.webp)

- Bạn sẽ chuyển tới bản fork của riêng mình từ kho lưu trữ Plan ₿ Academy:

![github-desktop](assets/13.webp)

Bản fork này tạo thành một kho lưu trữ riêng biệt so với kho lưu trữ gốc, mặc dù nó có cùng dữ liệu. Bạn sẽ làm việc trên kho lưu trữ mới này.

Nói một cách dễ hiểu, chúng ta đã tạo ra một bản sao của kho lưu trữ gốc Plan ₿ Academy. Bản fork của bạn (bản sao) và kho lưu trữ gốc bây giờ sẽ phát triển độc lập với nhau. Trên kho lưu trữ gốc, các cộng tác viên khác có thể thêm dữ liệu mới, trong khi bạn, trên bản fork của mình, sẽ tiến hành các chỉnh sửa của riêng mình.
Để duy trì tính nhất quán giữa hai kho lưu trữ này, việc đồng bộ hóa định kỳ là cần thiết để cả hai cùng nhận được những thông tin giống nhau. Để gửi các thay đổi của bạn đến kho lưu trữ gốc, bạn sẽ sử dụng cái được gọi là **`Pull Request`**. Và để tích hợp các thay đổi từ kho lưu trữ gốc vào bản fork của bạn, bạn sẽ sử dụng lệnh **`Sync fork`** có sẵn trên giao diện web của GitHub.

![github-desktop](assets/14.webp)

## Bước 4: Clone bản fork

- Quay trở lại phần mềm GitHub Desktop. Bây giờ, bản fork của bạn sẽ xuất hiện trong mục `Your repositories`. Nếu bản fork không hiển thị, sử dụng nút mũi tên kép để làm mới danh sách. Khi bản fork xuất hiện, nhấn vào nó để chọn:

![github-desktop](assets/15.webp)

- Sau đó nhấp vào nút màu xanh: `Clone [username]/bitcoin-educational-content`:

![github-desktop](assets/16.webp)

- Giữ nguyên đường dẫn mặc định. Để xác nhận, nhấn vào nút màu xanh `Clone`:

![github-desktop](assets/17.webp)

- Đợi trong giây lát khi GitHub Desktop thực hiện clone bản fork về máy tính:\

![github-desktop](assets/18.webp)

- Sau khi clone xong, phần mềm sẽ cung cấp cho bạn hai lựa chọn. Bạn hãy chọn cái đầu tiên: `To contribute to the parent project`. Lựa chọn này sẽ cho phép bạn gửi các thay đổi trong tương lai dưới dạng đóng góp cho dự án gốc (`Plan ₿ Academy/bitcoin-educational-content`), thay vì chỉ coi đó là các chỉnh sửa trên bản fork cá nhân của bạn (`[username]/bitcoin-educational-content`). Sau khi chọn xong, nhấn vào nút `Continue`:
![github-desktop](assets/19.webp)

- GitHub Desktop của bạn giờ đây đã được cấu hình đúng cách. Bây giờ, bạn có thể để phần mềm mở ở chế độ nền để theo dõi các thay đổi mà chúng ta sẽ thực hiện.

![github-desktop](assets/20.webp)

Ở bước này, bạn đã tạo được một bản sao cục bộ (local copy) của kho lưu trữ trên GitHub. Nhắc lại một chút: kho lưu trữ này là một bản fork từ kho mã nguồn gốc của Plan ₿ Academy. Bạn có thể thực hiện các chỉnh sửa trực tiếp trên bản sao cục bộ này, chẳng hạn như thêm hướng dẫn, bản dịch hoặc các chỉnh sửa nội dung. Sau khi hoàn tất các thay đổi, bạn sẽ sử dụng lệnh **`Push origin`** để gửi các chỉnh sửa từ máy của mình lên bản fork được lưu trữ trên GitHub.

Ngoài ra, bạn cũng có thể lấy về các thay đổi từ bản fork, ví dụ khi đồng bộ với kho lưu trữ của Plan ₿ Academy. Để làm điều này, bạn sẽ dùng lệnh **`Fetch origin`** để tải các thay đổi về bản sao cục bộ (bản clone), sau đó sử dụng lệnh **`Pull origin`** để hợp nhất chúng với phần công việc hiện tại của bạn. Cách làm này giúp bạn luôn cập nhật những thay đổi mới nhất của dự án trong khi vẫn đóng góp một cách hiệu quả.

![github-desktop](assets/21.webp)

## Bước 5: Tạo một Obsidian vault mới

- Mở phần mềm Obsidian và nhấp vào biểu tượng vault (kho lưu trữ) nhỏ ở góc dưới bên trái của cửa sổ:

![github-desktop](assets/22.webp)

- Nhấn vào nút `Open` để mở một thư mục có sẵn dưới dạng vault:

![github-desktop](assets/23.webp)

- Trình quản lý tệp (file explorer) của bạn sẽ mở ra. Bạn cần tìm và chọn thư mục có tên `GitHub`, thư mục này thường nằm trong thư mục `Documents` của bạn. Đường dẫn này tương ứng với đường dẫn bạn đã thiết lập ở bước 4. Sau khi chọn thư mục, hãy xác nhận lựa chọn. Quá trình tạo vault trong Obsidian sẽ bắt đầu và mở ra trong một trang mới của phần mềm:

![github-desktop](assets/24.webp)

-> **Lưu ý**, khi tạo một vault mới trong Obsidian, không được chọn thư mục `bitcoin-educational-content`. Thay vào đó, hãy chọn thư mục cha là `GitHub`. Nếu bạn chọn thư mục `bitcoin-educational-content`, thư mục cấu hình `.obsidian` (chứa cài đặt Obsidian cục bộ của bạn) sẽ tự động được thêm vào kho lưu trữ. Điều này là không cần thiết, vì chúng ta không muốn đưa các cấu hình Obsidian cá nhân lên repository của Plan ₿ Academy. Một phương án khác là thêm thư mục `.obsidian` vào tệp `.gitignore`, nhưng phương pháp này cũng sẽ thay đổi tệp `.gitignore` của kho lưu trữ gốc, đây cũng là điều mà chúng ta nên tránh.

- Ở phía bên trái cửa sổ, bạn có thể thấy cây thư mục hiển thị các repository GitHub đã được clone về máy.
- Bằng cách nhấp vào các mũi tên bên cạnh tên thư mục, bạn có thể mở rộng chúng để truy cập các thư mục con và tài liệu bên trong:

![github-desktop](assets/25.webp)

- Đừng quên chuyển Obsidian sang chế độ tối (dark mode): « _Light attracts bugs_ » ;)

## Bước 6: Cài đặt trình biên tập mã (Code editor)

Phần lớn các chỉnh sửa của bạn sẽ được thực hiện trên các tệp có định dạng Markdown (`.md`). Để chỉnh sửa các tài liệu này, bạn có thể sử dụng Obsidian – phần mềm mà chúng ta đã đề cập trước đó. Tuy nhiên, Plan ₿ Academy còn sử dụng các định dạng tệp khác, và bạn sẽ cần chỉnh sửa một số trong số đó.

Ví dụ, khi tạo một hướng dẫn mới, bạn sẽ cần tạo một tệp YAML (`.yml`) để nhập các thẻ (tags), tiêu đề của hướng dẫn và ID của giảng viên. Obsidian không hỗ trợ chỉnh sửa loại tệp này, vì vậy bạn sẽ cần một trình biên tập mã.

Có nhiều lựa chọn khác nhau cho mục đích này. Mặc dù trình soạn thảo văn bản mặc định trên máy tính của bạn có thể dùng để chỉnh sửa các tệp này, nhưng đây không phải là giải pháp lý tưởng cho công việc cần sự gọn gàng và chính xác. Chúng tôi khuyên bạn nên sử dụng các phần mềm được thiết kế chuyên biệt cho mục đích này, chẳng hạn như [VS Code](https://code.visualstudio.com/download) hoặc [Sublime Text](https://www.sublimetext.com/download). Sublime Text khá nhẹ và hoàn toàn đáp ứng đủ nhu cầu của chúng ta.

- Cài đặt một trong những phần mềm này, và để nó sang một bên, chúng ta sẽ cần đến chúng trong tương lai.

![github-desktop](assets/26.webp)

Xin chúc mừng! Môi trường làm việc của bạn đã sẵn sàng để đóng góp cho Plan ₿ Academy. Bây giờ, bạn có thể khám phá các hướng dẫn chuyên biệt khác dành cho từng loại đóng góp (dịch thuật, hiệu đính, viết nội dung...)

https://planb.academy/tutorials/contribution
