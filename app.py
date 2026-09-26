import os
import streamlit as st
from google import genai
from google.genai import types

# إعداد واجهة وتصميم الصفحة
st.set_page_config(page_title="رادار المشتريات والصفقات", layout="centered", page_icon="🛒")

st.markdown("<h2 style='text-align: center;'>🛒 رادار الصفقات وأحدث الإصدارات</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>اكتشف أحدث إصدار عالمي وأقل سعر متوفر اليوم في متاجر الرياض</p>", unsafe_allow_html=True)

# جلب المفتاح بأمان من الإعدادات السحابية
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

query = st.text_input("ما هو المنتج أو الجهاز الذي تبحث عنه؟", placeholder="...مثال: قلاية هوائية، شواية ذكية، مكواة بخار")

if st.button("فحص العروض وأحدث موديل", use_container_width=True):
    if not query.strip():
        st.warning("يرجى كتابة اسم المنتج أولاً.")
    elif not api_key:
        st.error("مفتاح API غير متوفر. يرجى إضافته في إعدادات الأسرار Secrets.")
    else:
        with st.spinner("جاري فحص المتاجر وجلب روابط الشراء المباشرة للمنتج..."):
            try:
                client = genai.Client(api_key=api_key)
                prompt = f"""المستخدم يريد شراء هذا المنتج: {query}
قدم تقريراً استشارياً دقيقاً ومباشراً:
1. حدد أفضل وأحدث جهازين في السوق متوافقين مع مواصفات السعودية (220-240V بتردد 50/60Hz).
2. لكل جهاز ترشحه، اذكر:
   - الاسم التجاري الكامل ورقم الموديل الدقيق بالإنجليزية (Model Number / SKU).
   - أهم الميزات ولماذا هو الأفضل.
   - روابط شراء مباشرة للسلعة المحددة بعينها (Direct Product Page) على المتاجر المتاحة (أمازون السعودية Amazon.sa، إكسترا eXtra، نون Noon).
   - في حال استخدام رابط بحث المتجر، يجب أن يكون الرابط دقيقاً ومباشراً يحتوي على اسم الماركة ورقم الموديل بالإنجليزية فقط (مثال: https://www.amazon.sa/s?k=Ninja+AG551EU أو https://www.noon.com/saudi-ar/search/?q=Ninja+AG551) حتى يفتح صفحة هذا الجهاز بعينه مباشرة للمستخدم دون تشتت بين منتجات أخرى.
3. جدول مقارنة بالأسعار التقريبية في متاجر الرياض اليوم.
4. إعلان 'الصفقة الرابحة' مع رابط الشراء المباشر لها بشكل بارز."""

                try:
                    response = client.models.generate_content(
                        model='gemini-3.8-flash',
                        contents=prompt,
                        config=types.GenerateContentConfig(
                            tools=[types.Tool(google_search=types.GoogleSearch())]
                        )
                    )
                except Exception:
                    response = client.models.generate_content(
                        model='gemini-3.8-flash',
                        contents=prompt
                    )

                st.success("تم حصر البيانات وتجهيز روابط الشراء المباشرة بنجاح!")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"حدث خطأ أثناء الفحص: {e}")
