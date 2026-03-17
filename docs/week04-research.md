# 1. Tìm hiểu về Django QuerySets
QuerySet là một danh sách các đối tượng (objects) từ Database. Nó cho phép ta đọc, lọc và sắp xếp dữ liệu mà không cần viết câu lệnh SQL thuần túy.

1.1. Truy vấn tất cả dữ liệu (all())
Để lấy toàn bộ bài viết từ bảng Post hiển thị lên Timeline, ta sử dụng:

Cú pháp: Post.objects.all()

Giải thích: Câu lệnh này tương đương với SELECT * FROM core_post trong SQL.

1.2. Sắp xếp dữ liệu (order_by())
Một mạng xã hội cần bài viết mới nhất hiện lên đầu trang.

Cú pháp: Post.objects.all().order_by('-created_at')

Giải thích: * Dấu trừ (-) trước tên trường created_at biểu thị sắp xếp giảm dần (Descending).

Bài viết có thời gian tạo mới nhất sẽ có ID lớn hơn hoặc thời gian lớn hơn, do đó sẽ được đưa lên đầu danh sách.

# 2. Truyền dữ liệu sang Template (Context)
Để hiển thị được QuerySet ra file HTML, ta sử dụng một từ điển (Dictionary) gọi là Context.

Tại View: render(request, 'index.html', {'posts': posts})

'posts' (khóa): Là tên biến mà ta sẽ gọi ở file HTML.

posts (giá trị): Là biến chứa dữ liệu QuerySet vừa lấy từ Database.

# 3. Hiển thị dữ liệu bằng Tag {% for %}
Vì QuerySet là một danh sách, ta cần dùng vòng lặp của Django Template Language (DTL) để duyệt qua từng bài viết.

Cơ chế: Django sẽ lặp qua từng Object trong QuerySet, mỗi lần lặp ta có thể truy cập vào các thuộc tính của nó như {{ post.user }}, {{ post.image.url }}, {{ post.caption }}.