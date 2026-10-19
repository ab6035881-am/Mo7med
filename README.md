# Twist Hub — نسخة جاهزة للنشر على Render

## خطوات الرفع
1. فك ضغط الملف.
2. ارفع محتوياته إلى مستودع GitHub جديد.
3. افتح https://render.com وسجّل الدخول.
4. اختر New + ثم Web Service، واربط مستودع GitHub.
5. أوامر البناء والتشغيل: `pip install -r requirements.txt` و `gunicorn app:app`.
6. بعد النشر سيعطيك Render رابط الموقع.

## تشغيل محلي
`pip install -r requirements.txt` ثم `python app.py` وافتح `http://127.0.0.1:5000`.

## تنبيه
هذه نسخة تجريبية ببيانات وهمية. تسجيل دخول OTP الحقيقي ورصيد Twist والمهام والاستبدال الحقيقي غير مفعّلين؛ يلزم تكامل رسمي ومصرّح به مع الخدمة.
