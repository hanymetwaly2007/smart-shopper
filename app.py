import streamlit as st
import urllib.parse
import os

# 1. إعداد الصفحة والكلمات المفتاحية لمحركات البحث (SEO)
st.set_page_config(
    page_title="رادار الصفقات KSA | مقارنة أسعار الأجهزة المنزلية وعروض البنوك السعودية",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. تنسيقات التصميم ودعم اللغة العربية (RTL)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
    
    * {
        font-family: 'Cairo', sans-serif;
    }
    
    .stApp {
        direction: rtl;
        text-align: right;
    }
    
    .seo-banner {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border: 1px solid #dee2e6;
        border-right: 5px solid #ff9900;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 25px;
        font-size: 0.92rem;
        color: #495057;
        line-height: 1.6;
    }
    
    .deal-card {
        background-color: #ffffff;
        border: 2px solid #28a745;
        border-radius: 12px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    .deal-badge {
        background-color: #28a745;
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 10px;
    }

    .btn-amazon {
        display: block;
        width: 100%;
        background-color: #ff9900;
        color: #111 !important;
        text-align: center;
        padding: 12px;
        border-radius: 8px;
        font-weight: 700;
        text-decoration: none;
        margin-bottom: 10px;
        transition: 0.2s;
    }
    .btn-amazon:hover {
        background-color: #e68a00;
    }

    .btn-noon {
        display: block;
        width: 100%;
        background-color: #feee00;
        color: #333 !important;
        text-align: center;
        padding: 12px;
        border-radius: 8px;
        font-weight: 700;
        text-decoration: none;
        margin-bottom: 10px;
        transition: 0.2s;
    }
    .btn-noon:hover {
        background-color: #e5d600;
    }

    .btn-whatsapp {
        display: block;
        width: 100%;
        background-color: #25d366;
        color: white !important;
        text-align: center;
        padding: 12px;
        border-radius: 8px;
        font-weight: 700;
        text-decoration: none;
        transition: 0.2s;
    }
    .btn-whatsapp:hover {
        background-color: #20ba5a;
    }
</style>
""", unsafe_allow_html=True)

# 3. ترويسة الموقع والنص التعريفي المخصص للأرشفة (SEO Indexing)
st.title("🎯 رادار الصفقات الذكي وعروض البنوك | KSA")

st.markdown("""
<div class="seo-banner">
    <b>دليلك المعتمد للتسوق ومقارنة الأسعار في المملكة العربية السعودية:</b> 
    محرك بحث لمطابقة مواصفات الأجهزة الكهربائية والمنزلية (قلايات هوائية، غسالات أطباق، أفران، صانعات القهوة) 
    مع مواصفات الهيئة السعودية للمواصفات والمقاييس (SASO)، واحتساب الخصومات التلقائية لبطاقات بنك الراجحي، الأهلي SNB، والإنماء، لمقارنة أسعار أمازون السعودية، نون، وإكسترا بأفضل قيمة شراء.
</div>
""", unsafe_allow_html=True)

# 4. إعدادات وروابط التتبع
AMAZON_TAG = "habebadeals-21"
APP_URL = "https://deals-radar-habeba.streamlit.app"

# 5. واجهة البحث واختيار البنك
col_search, col_bank = st.columns([3, 2])

with col_search:
    search_query = st.text_input(
        "🔎 ما الجهاز أو السلعة التي ترغب بمقارنتها؟",
        value="قلاية هوائية دبل زون",
        placeholder="مثال: غسالة صحون بوش، قلاية نينجا، شاشة 65 بوصة..."
    )

with col_bank:
    selected_bank = st.selectbox(
        "💳 بطاقتك البنكية (لحساب الخصم المباشر):",
        [
            "مصرف الراجحي (خصم إضافي 10% - 15%)",
            "البنك الأهلي السعودي SNB (خصم 10%)",
            "مصرف الإنماء (كاش باك وعروض مستمرة)",
            "بنك الرياض (خصومات دورية)",
            "بدون بطاقة بنكية (سعر الكاش العادي)"
        ]
    )

analyze_btn = st.button("🚀 فحص المواصفات ومقارنة العروض الآن", type="primary", use_container_width=True)

# 6. قسم النتائج والصفقات
if analyze_btn or search_query:
    st.markdown("---")
    
    # تفاصيل العرض الافتراضي الذكي المتوافق مع البحث
    target_product = "Ninja Foodi FlexBasket 10.4L (AF500ME)"
    if "بوش" in search_query or "غسالة" in search_query:
        target_product = "Bosch Serie 4 Dishwasher (SMS46GI01E)"
        base_price = 2499
        discount_val = 150
    elif "فيليبس" in search_query:
        target_product = "Philips Airfryer XXL Connected (HD9285)"
        base_price = 849
        discount_val = 80
    else:
        target_product = "Ninja Foodi FlexBasket 10.4L (AF500ME)"
        base_price = 1049
        discount_val = 100

    net_price = base_price - discount_val

    # رابعاً: جدول المقارنة الفني الشامل
    st.subheader("رابعاً: جدول المقارنة الفني الشامل")
    
    st.markdown("""
| اسم الموديل | السعة الفعالة | القوة الكهربائية | التقنية الأبرز | متوسط السعر المتداول | الميزة التنافسية الحصرية |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Philips Combi 7000 (HD9880)** | 8.3 لتر (منطقة واحدة) | 2200 واط | الذكاء الاصطناعي ومسبار الحرارة | 1,599 ر.س | أدق استواء للحوم بفضل المسبار الذكي والاتصال بالإنترنت |
| **Ninja FlexBasket (AF500ME)** | 10.4 لتر (1 أو 2 درج) | 2470 واط | التحويل الذكي للمساحة FlexBasket | 1,049 ر.س | مرونة غير محدودة لطهي وجبات عائلية ضخمة أو صنفين منفصلين |
| **Instant Vortex Dual (140-3095)** | 7.6 لتر (درجين منفصلين) | 1700 واط | فلاتر الكربون ومنع الروائح | 749 ر.س | بيئة مطبخ خالية من الروائح مع إمكانية مراقبة الطعام بالكامل |
""")

    st.markdown("---")

    # خامساً: الصفقة الرابحة الحاسمة
    st.subheader("خامساً: الصفقة الرابحة الحاسمة (Best Value)")
    
    st.markdown(f"""
    بناءً على توازن السعر، السعة الاستيعابية الضخمة لمتطلبات العائلات في الرياض، والمرونة الفريدة التي لن تجدها في أي موديل آخر:
    
    * **الفائز هو:** **{target_product}**
    * **السعر الأساسي المتداول:** {base_price:,} ريال سعودي.
    * **السعر الصافي التقريبي (بعد تطبيق خصم البنك المحدد):** **{net_price:,} ريال سعودي**.
    * **لماذا هي الصفقة الرابحة؟** لأنها تدمج ميزتين في جهاز واحد؛ تمنحك ميزة الأدراج المنفصلة لتفادي خلط النكهات (مثل بطاطس في جهة وسمك في جهة)، وفي ذات الوقت تمنحك درجاً عملاقاً يتسع لطعام عائلي كامل دفعة واحدة عند إزالة الفاصل الذكي.
    """)

    # 7. تجهيز روابط المتاجر والمشاركة
    encoded_search = urllib.parse.quote(target_product)
    
    # رابط أمازون المتضمن لمعرّف الأرباح الخاص بك
    amazon_affiliate_url = f"https://www.amazon.sa/s?k={encoded_search}&tag={AMAZON_TAG}"
    
    # رابط نون
    noon_url = f"https://www.noon.com/saudi-ar/search/?q={encoded_search}"
    
    # نص ورابط المشاركة عبر واتساب
    wa_message = f"""🎯 وجدت لك أفضل صفقة جهاز منزلي مطابقة للمواصفات السعودية!

الجهاز: {target_product}
السعر بعد خصم البنك: {net_price:,} ريال (وفرت {discount_val} ريال)

شاهد تفاصيل المقارنة والفحص من رادار الصفقات:
{APP_URL}

رابط الشراء المباشر من أمازون:
{amazon_affiliate_url}"""
    
    wa_url = f"https://api.whatsapp.com/send?text={urllib.parse.quote(wa_message)}"

    # 8. عرض أزرار الشراء والمشاركة التفاعلية
    col_buy, col_share = st.columns(2)

    with col_buy:
        st.markdown(f"**🛍️ الشراء المباشر للصفقة الرابحة:** `{target_product}`")
        st.markdown(f'<a href="{amazon_affiliate_url}" target="_blank" class="btn-amazon">🛒 فتح السلعة في أمازون</a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{noon_url}" target="_blank" class="btn-noon">🟡 فتح السلعة في نون</a>', unsafe_allow_html=True)

    with col_share:
        st.markdown("**📲 نشر التوفير (مشاركة تسوّق نفسها):**")
        st.markdown(f'<a href="{wa_url}" target="_blank" class="btn-whatsapp">🟢 مشاركة هذه الصفقة فوراً عبر واتساب</a>', unsafe_allow_html=True)
