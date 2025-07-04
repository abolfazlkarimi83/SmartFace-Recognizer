# 😎 Real-Time Face Recognition using Face\_Recognition and OpenCV

(تشخیص چهره به‌صورت زنده با استفاده از کتابخانه Face\_Recognition و OpenCV)

---

## 📚 About the Project | درباره پروژه

This project performs real-time face recognition using a webcam and the powerful `face_recognition` library in Python.
The program detects faces from a live video feed and matches them with previously known faces by comparing facial encodings.

این پروژه به تشخیص چهره افراد از طریق وب‌کم به صورت زنده می‌پردازد. با استفاده از کتابخانه `face_recognition` چهره‌ها تشخیص داده شده و با چهره‌های از پیش شناخته‌شده مقایسه می‌شوند تا در صورت تطابق، نام فرد نمایش داده شود.

---

## 🧵 Features | ویژگی‌ها

* Real-time face detection from webcam
  (تشخیص چهره به صورت زنده از طریق دوربین)
* Facial recognition using encoding comparison
  (شناسایی چهره‌ها با مقایسه بردارهای ویژگی)
* Display name label on recognized faces
  (نمایش نام افراد شناخته‌شده روی تصویر)
* Easily extensible for adding more known faces
  (قابلیت افزودن چهره‌های جدید با عکس دلخواه)

---

## 📊 How it Works | نحوه عملکرد

1. Load known face images and extract their encodings.
   (بارگذاری عکس‌های چهره و استخراج ویژگی‌های آن‌ها)
2. Capture real-time video from the webcam.
   (دریافت ویدیو زنده از دوربین)
3. Detect all faces in the current frame.
   (تشخیص چهره در تصویر فعلی)
4. Compare detected faces with known encodings.
   (مقایسه چهره‌های تشخیص داده شده با چهره‌های شناخته شده)
5. Display the name of the matched person on the screen.
   (نمایش نام فرد تطبیق داده شده روی تصویر)

---

## 🛠️ Technologies Used | تکنولوژی‌های استفاده شده

* Python 3.x
* OpenCV
* face\_recognition (based on dlib)
* NumPy

---

## 🚀 How to Run | نحوه اجرای پروژه

1. Make sure Python 3 is installed.

2. Install required packages:

   ```bash
   pip install opencv-python face_recognition numpy
   ```

3. Prepare images of known faces and name them (e.g., `person1.jpg`, `person2.jpg`).

4. Update the Python script with the correct file names and names.

5. Run the script:

   ```bash
   python face_recognition_script.py
   ```

6. Press `q` to exit the video stream.

---

## 👤 About Me | درباره من

**Abolfazl Karimi** — AI and Machine Learning Developer
**ابوالفضل کریمی** — توسعه‌دهنده هوش مصنوعی و یادگیری ماشین

📧 Email: [karimiabolfazl466@gmail.com](mailto:karimiabolfazl466@gmail.com)
📱 Telegram: [@Abolfazlk83](https://t.me/Abolfazlk83)
👍 GitHub: [github.com/abolfazlkarimi83](https://github.com/abolfazlkarimi83)

---

> This project provides a strong foundation for building real-time surveillance systems, secure access applications, or smart home automation tools.
>
> این پروژه می‌تواند پایه‌ای برای سیستم‌های نظارتی زنده، اپلیکیشن‌های امنیتی یا ابزارهای خانه هوشمند باشد.
