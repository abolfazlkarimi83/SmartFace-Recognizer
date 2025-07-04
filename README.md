🔐 Real-time Face Recognition with Webcam
(تشخیص چهره به‌صورت زنده با استفاده از وب‌کم)

📚 About the Project | درباره پروژه
This project demonstrates how to build a simple real-time face recognition system using a webcam and the face_recognition library.
It allows users to compare faces captured by the webcam with reference images and identify known individuals by displaying their names on screen.

این پروژه نشان می‌دهد چگونه می‌توان یک سیستم ساده‌ی تشخیص چهره به صورت زنده با استفاده از وب‌کم و کتابخانه‌ی face_recognition ایجاد کرد.
این برنامه چهره‌های شناسایی‌شده از طریق وب‌کم را با تصاویر مرجع مقایسه کرده و در صورت تشخیص، نام آن‌ها را روی تصویر نمایش می‌دهد.

🧩 How It Works | این پروژه چطور کار می‌کند؟
Load face images (reference images) with names you choose (e.g., person1.jpg, person2.jpg).

Encode each face using face_recognition.face_encodings.

Start the webcam and capture live video frames.

Detect and encode faces in each frame.

Compare live faces with known encodings.

Display the person's name if matched, or mark as unknown.

۱. تصاویر مرجع (مثلاً person1.jpg، person2.jpg) را با نام دلخواه خود وارد کنید.
۲. چهره‌ها توسط تابع face_encodings کدگذاری می‌شوند.
۳. ویدیو به‌صورت زنده از وب‌کم دریافت می‌شود.
۴. چهره‌ها در هر فریم تشخیص و کدگذاری می‌شوند.
۵. چهره زنده با چهره‌های مرجع مقایسه می‌شود.
۶. اگر چهره تطبیق پیدا کرد، نام فرد نمایش داده می‌شود، در غیر این صورت برچسب «ناشناس» (Unknown) قرار می‌گیرد.

🧠 Technologies Used | تکنولوژی‌های استفاده شده
Python 3.x

OpenCV (cv2) for webcam access and drawing

face_recognition library for encoding and comparing faces

NumPy

🚀 How to Run | نحوه اجرای پروژه
Install required packages:

bash
Copy
Edit
pip install face_recognition opencv-python numpy
Put your reference face images (e.g., ali.jpg, reza.jpg) in the same directory.

Update the code with the filenames and labels you want (e.g., "Ali", "Reza").

Run the script:

bash
Copy
Edit
python face_recognizer.py
Press q to quit the webcam window.

📁 Example Folder Structure | ساختار فایل پروژه
Copy
Edit
face_recognition_project/
│
├── face_recognizer.py
├── ali.jpg
├── reza.jpg
└── README.md
📷 Output Example | نمونه خروجی
وقتی وب‌کم یک چهره را شناسایی می‌کند، نام آن شخص روی تصویر ظاهر می‌شود. اگر تطبیقی یافت نشود، برچسب "is not a defined" نمایش داده می‌شود.

When the webcam recognizes a face, it shows the person’s name on screen. If no match is found, it displays “is not a defined”.

🔐 Use Cases | موارد استفاده
Entry access systems

Attendance systems

Personalized AI interfaces

Educational and demo projects

سیستم‌های کنترل ورود

سیستم حضور و غیاب

رابط‌های کاربری هوشمند شخصی‌سازی‌شده

پروژه‌های آموزشی و دمو

About Me | درباره من
👋 My name is Abolfazl Karimi, and I'm an AI programmer focused on real-world deep learning and computer vision applications.
📫 Email: karimiabolfazl466@gmail.com
📱 Telegram: @Abolfazlk83
🐙 GitHub: github.com/abolfazlkarimi83

👋 من ابوالفضل کریمی هستم، برنامه‌نویس هوش مصنوعی با تمرکز بر پروژه‌های عملی در حوزه یادگیری عمیق و بینایی ماشین.
📫 ایمیل: karimiabolfazl466@gmail.com
📱 تلگرام: @Abolfazlk83
🐙 گیت‌هاب: github.com/abolfazlkarimi83

