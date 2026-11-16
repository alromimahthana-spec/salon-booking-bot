# بوت صالون تجميل - ثناء | thanaa.codes
# يحجز مواعيد، يعرض الأسعار، ويذكر الزبونة بموعدها

services = {
    "1": {"name": "قص شعر", "price": "5000 ريال يمني / 30 ريال سعودي", "time": "45 دقيقة"},
    "2": {"name": "صبغة شعر", "price": "15000 ريال يمني / 80 ريال سعودي", "time": "ساعتين"},
    "3": {"name": "مكياج سهرة", "price": "20000 ريال يمني / 120 ريال سعودي", "time": "ساعة ونص"},
    "4": {"name": "مناكير وبديكير", "price": "8000 ريال يمني / 40 ريال سعودي", "time": "ساعة"},
    "5": {"name": "استشوار + تسريحة", "price": "10000 ريال يمني / 50 ريال سعودي", "time": "ساعة"},
}

orders = []

def show_menu():
    print("💅 أهلاً فيك في صالون الجمال!")
    print("اختاري الخدمة:")
    for key, s in services.items():
        print(f"{key}. {s['name']} - {s['price']} - {s['time']}")
    print("0. الخروج")

def book_appointment():
    show_menu()
    choice = input("اكتبي رقم الخدمة: ")
    if choice == "0":
        print("شكراً لزيارتك 🌸")
        return
    if choice in services:
        s = services[choice]
        name = input("اسمك: ")
        phone = input("رقمك: ")
        date = input("تاريخ الحجز (مثال: 2026-11-20): ")
        time = input("وقت الحجز (مثال: 4 عصراً): ")
        
        booking = {
            "name": name,
            "phone": phone,
            "service": s['name'],
            "price": s['price'],
            "date": date,
            "time": time
        }
        orders.append(booking)
        print("\n✅ تم الحجز بنجاح!")
        print(f"الاسم: {name}")
        print(f"الخدمة: {s['name']}")
        print(f"السعر: {s['price']}")
        print(f"التاريخ: {date} - الساعة: {time}")
        print(f"📩 بنرسل لك تذكير قبل موعدك بيوم!")
    else:
        print("اختيار غلط، حاولي مرة ثانية")

while True:
    book_appointment()
    again = input("\nتبغي تحجزي خدمة ثانية؟ (نعم/لا): ")
    if again.lower() != "نعم":
        print("مع السلامة، نورتينا 💗")
        break
