import os
import time
import urllib.parse
import streamlit as st
from google import genai
from google.genai import types

# إعداد واجهة الصفحة
st.set_page_config(page_title="المتسوق الذكي - الصفقة المباشرة", layout="centered", page_icon="🎯")

st.markdown("<h2 style='text-align: center;'>🎯 رادار الصفقات المباشرة</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>أفضل جهاز مطابق لمواصفات السعودية (220V) مع رابط الشراء المباشر فوراً</p>", unsafe_allow_html=True)

# جلب مفتاح API بأمان
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

query = st.text_input("اكتب اسم الجهاز أو المنتج الذي تبحث عنه:", placeholder="...مثال: قلاية هوائية، شواية ذكية، مفرمة لحم")

if st.button("اعثر على أفضل صفقة ورابط الشراء المباشر 🚀", use_container_width=True):
    if not query.strip():
        st.warning("يرجى كتابة اسم المنتج أولاً.")
    elif not api_key:
        st.error("مفتاح API غير متوفر في الإعدادات.")
    else:
        with st.spinner("جاري استخراج السلعة الفائزة ومواصفاتها..."):
            client = genai.Client(api_key=api_key)
            prompt = f"""أنت مستشار مشتريات محترف في الرياض.
المستخدم يبحث عن: {query}

المطلوب إجابة مختصرة ومركزة جداً بدون حشو:
1. اختر منتجاً واحداً فقط يعتبر 'الصفقة الرابحة والأفضل عالمياً' المطابق لكهرباء السعودية 220V-240V وتردد 50/60Hz.
2. اذكر اسمه التجاري الكامل ورقم الموديل الدقيق بالإنجليزية (Model Number).
3. متوسط سعره بالريال السعودي اليوم في متاجر الرياض وأين يتوفر بأقل سعر.
4. جملتين فقط عن أهم ميزاته ولماذا هو الخيار الأفضل.
5. توضيح الموديل البديل في حال عدم توفره."""

            response = None
            last_err = None

            # محاولة الإرسال مع إعادة المحاولة التلقائية لتفادي ضغط السيرفرات (503)
            for attempt in range(3):
                try:
                    response = client.models.generate_content(
                        model='gemini-3.8-flash',
                        contents=prompt
                    )
                    if response:
                        break
                except Exception as e:
                    last_err = e
                    time.sleep(2)  # انتظار ثانيتين ثم إعادة المحاولة تلقائياً

            if response:
                st.success("تم تحديد أفضل صفقة مطابقة لمواصفات السعودية بنجاح!")
                st.markdown(response.text)

                # روابط بحث دقيقة ومباشرة بمواصفات 220V
                st.markdown("---")
                st.markdown("#### 🛒 فتح صفحة المنتج للشراء فوراً:")
                search_term = urllib.parse.quote(f"{query} 220V")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.link_button("🟢 شراء من أمازون السعودية", f"https://www.amazon.sa/s?k={search_term}", use_container_width=True)
                with col2:
                    st.link_button("🟡 شراء من نون السعودية", f"https://www.noon.com/saudi-ar/search/?q={search_term}", use_container_width=True)
            else:
                st.error(f"خوادم جوجل تشهد ضغطاً مؤقتاً، يرجى المحاولة بعد لحظات: {last_err}")
