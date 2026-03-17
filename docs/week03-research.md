# 1. Tìm hiểu về Django Signals
Django Signals là một cơ chế cho phép các ứng dụng (apps) được thông báo khi có một sự kiện nhất định xảy ra trong hệ thống.

Cơ chế hoạt động: Gồm có Sender (người gửi tín hiệu) và Receiver (người nhận tín hiệu).

Ứng dụng trong dự án: Sử dụng tín hiệu post_save từ Model User.

Mục đích: Tự động tạo một bản ghi Profile tương ứng ngay khi một User mới được đăng ký thành công.

Lợi ích: Đảm bảo tính nhất quán của dữ liệu. Người dùng luôn có hồ sơ cá nhân (Profile) mà không cần phải viết thêm logic tạo profile trong hàm xử lý đăng ký (Signup View).

## 2. Tìm hiểu về File Uploads trong Django
Cơ chế giúp hệ thống tiếp nhận và lưu trữ các tệp tin (hình ảnh, tài liệu) từ phía người dùng.

request.FILES: Trong Django, các tệp tin được upload sẽ không nằm trong request.POST mà được lưu trữ trong request.FILES.

enctype="multipart/form-data": Đây là thuộc tính bắt buộc phải có trong thẻ <form> của HTML để trình duyệt có thể mã hóa và gửi dữ liệu tệp tin lên server.

Cấu hình Media:

MEDIA_ROOT: Đường dẫn vật lý trên ổ đĩa để lưu trữ tệp tin.

MEDIA_URL: Đường dẫn URL để truy cập vào tệp tin qua trình duyệt.

Xử lý trong Model: Sử dụng ImageField để lưu trữ đường dẫn ảnh và định nghĩa thư mục lưu trữ thông qua thuộc tính upload_to.

## 3. Kết quả thực hiện trong Tuần 3
Xây dựng thành công trang Settings cho phép người dùng cập nhật: Ảnh đại diện, Tiểu sử (Bio), và Vị trí (Location).

Kết nối thành công logic xử lý ảnh từ giao diện vào Database thông qua request.FILES.

Đăng ký Model Profile vào trang Django Admin để quản lý và kiểm tra dữ liệu đã cập nhật.