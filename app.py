import os
import urllib.parse
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
        with st.spinner("جاري مسح المتاجر وتحديث أحدث الأسعار في الرياض..."):
            try:
                client = genai.Client(api_key=api_key)
                prompt = f"""المستخدم يريد شراء أو الاستفسار عن: {query}
قم بتقديم تقرير استشاري دقيق وشامل:
1. تحديد أحدث وأفضل إصدار عالمي متاح حالياً ومطابق لكهرباء 220V بتردد 50/60Hz.
2. مسح ومقارنة الأسعار التقريبية في متاجر الرياض (أمازون السعودية، إكسترا، نون، ساكو).
3. تضمين روابط شراء واضحة ومباشرة وقابلة للنقر (Markdown links) للموديلات المقترحة، مثل:
   - [شراء من أمازون السعودية](https://www.amazon.sa/s?k=اسم_الموديل)
   - [شراء من نون](https://www.noon.com/saudi-ar/search/?q=اسم_الموديل)
   - [شراء من إكسترا](https://www.extra.com/ar-sa/search/?q=اسم_الموديل)
   - [شراء من ساكو](https://www.saco.sa/ar/search?text=اسم_الموديل)
4. توضيح أي عروض شائعة أو نصائح للشراء.
5. تقديم جدول مقارنة واضح وختم التقرير بنصيحة 'الصفقة الرابحة' مع رابط الشراء المباشر لها."""

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

                st.success("تم حصر البيانات بنجاح!")
                st.markdown(response.text)

                # أزرار الشراء المباشر السريعة
                st.markdown("---")
                st.markdown("### 🛍️ روابط سريعة للشراء المباشر من المتاجر:")
                encoded_q = urllib.parse.quote(query)
                col1, col2 = st.columns(2)
                col3, col4 = st.columns(2)

                with col1:
                    st.link_button("🛒 أمازون السعودية (Amazon.sa)", f"https://www.amazon.sa/s?k={encoded_q}", use_container_width=True)
                with col2:
                    st.link_button("🟡 نون السعودية (Noon)", f"https://www.noon.com/saudi-ar/search/?q={encoded_q}", use_container_width=True)
                with col3:
                    st.link_button("🔵 إكسترا (eXtra)", f"https://www.extra.com/ar-sa/search/?q={encoded_q}", use_container_width=True)
                with col4:
                    st.link_button("🔴 ساكو (SACO)", f"https://www.saco.sa/ar/search?text={encoded_q}", use_container_width=True)

            except Exception as e:
                st.error(f"حدث خطأ أثناء الفحص: {e}")
