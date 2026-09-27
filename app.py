import streamlit as st
import urllib.parse

# 1. إعداد الصفحة والكلمات المفتاحية لمحركات البحث (SEO)
st.set_page_config(
    page_title="أقوى عروض وتخفيضات الأجهزة المنزلية في السعودية | مقارنة الأسعار وخصم البنوك",
    page_icon="🔥",
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
        background: linear-gradient(135deg, #fff8f0 0%, #fff0e0 100%);
        border: 1px solid #ffe0b2;
        border-right: 5px solid #ff9900;
        padding: 16px;
        border-radius: 10px;
        margin-bottom: 25px;
        font-size: 0.95rem;
        color: #333;
        line-height: 1.7;
    }

    .product-box {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 3px 8px rgba(0,0,0,0.04);
    }
    
    .product-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #1a73e8;
        margin-bottom: 8px;
    }
    
    .price-tag {
        font-size: 1.15rem;
        font-weight: 700;
        color: #d93025;
        margin-bottom: 12px;
    }

    .deal-card {
        background-color: #f6fff8;
        border: 2px solid #28a745;
        border-radius: 12px;
        padding: 22px;
        margin: 25px 0;
        box-shadow: 0 4px 8px rgba(40,167,69,0.1);
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

# 3. العنوان الرئيسي والنص التعريفي المخصص لمحركات البحث
st.title("🔥 أقوى عروض وتخفيضات الأجهزة الكهربائية والمنزلية في السعودية")

st.markdown("""
<div class="seo-banner">
    <b>دليلك الذكي لأفضل عروض وتخفيضات الأجهزة في السعودية:</b> 
    مقارنة دقيقة وشاملة لأفضل الأجهزة المنزلية (قلايات هوائية، خلاطات ومحضرات طعام، غسالات صحون) ومطابقة مواصفات الجودة السعودية SASO. 
    نبحث لك عن أقل سعر في <b>أمازون السعودية، نون، وإكسترا</b>، مع حساب الخصم المباشر لبطاقات <b>مصرف الراجحي، البنك الأهلي SNB، البنك السعودي الفرنسي BSF، ومصرف الإنماء</b> لنضمن لك أقوى صفقة توفير.
</div>
""", unsafe_allow_html=True)

# 4. إعدادات الحساب وروابط التتبع
AMAZON_TAG = "habebadeals-21"
APP_URL = "https://deals-radar-habeba.streamlit.app"

# 5. إدارة الذاكرة (تبدأ الصفحة فارغة تماماً دون بحث سابق)
if "search_term" not in st.session_state:
    st.session_state.search_term = ""

def set_category(cat_name):
    st.session_state.search_term = cat_name

# أزرار التنقل السريع
st.markdown("**⚡ اختر فئة سريعة أو اكتب في خانة البحث أدناه:**")
col_b1, col_b2, col_b3 = st.columns(3)
with col_b1:
    st.button("🍟 قلايات هوائية عائلية", on_click=set_category, args=("قلاية هوائية",), use_container_width=True)
with col_b2:
    st.button("🥤 خلاطات ومحضرات طعام", on_click=set_category, args=("خلاط كهربائي",), use_container_width=True)
with col_b3:
    st.button("🍽️ غسالات صحون أوتوماتيك", on_click=set_category, args=("غسالة صحون",), use_container_width=True)

col_search, col_bank = st.columns([3, 2])

with col_search:
    search_query = st.text_input(
        "🔎 ما الجهاز الذي تريد مقارنته واكتشاف خصوماته؟",
        value=st.session_state.search_term,
        placeholder="اكتب هنا مثلاً: قلاية هوائية، خلاط، غسالة صحون..."
    )

with col_bank:
    selected_bank = st.selectbox(
        "💳 بطاقتك البنكية (لحساب الخصم المباشر):",
        [
            "جميع البنوك (عرض مقارنة الخصومات لكافة البنوك)",
            "البنك السعودي الفرنسي BSF (كود BSF20 - خصم 100 ريال)",
            "مصرف الراجحي (خصم إضافي 100 ريال)",
            "البنك الأهلي السعودي SNB (خصم إضافي 100 ريال)",
            "مصرف الإنماء (خصم إضافي 75 ريال)",
            "بنك الرياض (خصم إضافي 50 ريال)",
            "بدون بطاقة بنكية (سعر الكاش العادي)"
        ]
    )

analyze_btn = st.button("🚀 فحص المواصفات واستخراج أقوى عرض وتخفيض", type="primary", use_container_width=True)

# 6. شرط الفحص (لا تظهر أي نتائج إلا إذا اختار المستخدم فئة أو كتب في البحث)
clean_query = search_query.strip().lower()

if not clean_query:
    st.info("👆 اضغط على إحدى الفئات السريعة بالأعلى أو اكتب اسم الجهاز في خانة البحث لتظهر لك المقارنة الفورية والأسعار وصور المنتجات.")
else:
    # تخصيص البيانات والصور حسب الكلمة المدخلة
    if any(w in clean_query for w in ["خلاط", "عجان", "محضر", "براون", "عصير", "سموذي"]):
        category_title = "أفضل خلاطات ومحضرات طعام في السعودية"
        p1 = {
            "title": "أولاً: Braun MultiQuick 9 Hand Blender (MQ9147X)",
            "price": "متوسط السعر المتداول: 599 ريال سعودي",
            "img": "https://m.media-amazon.com/images/I/61kMv-2sBBL._AC_SL1500_.jpg",
            "specs": [
                "<b>القوة والأداء:</b> 1200 واط تمنح أداءً فائقاً في هرس وسحق أقسى المكونات.",
                "<b>التقنية الحصرية:</b> شفرات ActiveBlade تتحرك عمودياً لطحن المكونات الأكثر صلابة بجهد أقل 40%.",
                "<b>الملحقات:</b> ملحق محضر طعام، خفاقة، ومفرمة صغيرة للمكسرات والبصل.",
                "<b>التقييم:</b> الخيار الأول للطبخ والصلصات والشوربات دون استهلاك مساحة."
            ]
        }
        p2 = {
            "title": "ثانياً: Ninja Foodi 3-in-1 Food Processor & Blender (BN800ME)",
            "price": "السعر الحالي في عروض أمازون: 649 ريال سعودي (بدلاً من 899)",
            "img": "https://m.media-amazon.com/images/I/71mZc+k+1oL._AC_SL1500_.jpg",
            "specs": [
                "<b>القوة والسعة:</b> موتور بقوة 1200 واط مع وعاء محضر 1.8 لتر، وإبريق 2.1 لتر، وكوبين سموذي.",
                "<b>التقنية الحصرية:</b> برامج Auto-iQ الآلية للخلط والعجن بلمسة واحدة.",
                "<b>الاستخدام المتعدد:</b> جهاز شامل يجمع الخلاط ومحضر الطعام ومحضرة السموذي.",
                "<b>التقييم:</b> الفائز المطلق في التنوع وسحق الثلج والوجبات العائلية الكبيرة."
            ]
        }
        p3 = {
            "title": "ثالثاً: Philips Core Series 5000 (HR3573)",
            "price": "متوسط السعر المتداول: 289 ريال سعودي",
            "img": "https://m.media-amazon.com/images/I/71dM87L0a1L._AC_SL1500_.jpg",
            "specs": [
                "<b>القوة والسعة:</b> 1000 واط مع دورق زجاجي مقاوم للكسر والحرارة بسعة 2 لتر.",
                "<b>التقنية الحصرية:</b> تقنية ProBlend Crush بـ 6 شفرات حادة لسحق الثلج مرتين أسرع.",
                "<b>التقييم:</b> الخيار الاقتصادي الأفضل للعصائر والسموذي اليومي."
            ]
        }
        table_md = """
| اسم الموديل | القوة الكهربائية | السعة الرئيسية | التقنية الأبرز | متوسط السعر المتداول | الميزة التنافسية |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Braun MultiQuick 9** | 1200 واط | ملحقات متعددة | شفرات ActiveBlade عمودية | 599 ر.س | خفيف، احترافي للشوربات وخلط الأطعمة بالوعاء مباشرة |
| **Ninja Foodi 3-in-1 (BN800)** | 1200 واط | 2.1 لتر + 1.8 لتر | برامج Auto-iQ الآلية | 649 ر.س (عرض حالي) | جهاز متكامل (خلاط + محضر طعام + سموذي) |
| **Philips Series 5000** | 1000 واط | 2 لتر زجاجي | شفرات ProBlend Crush | 289 ر.س | اقتصادي ومثالي لسحق الثلج والعصائر اليومية |
"""
        winner_name = "Ninja Foodi 3-in-1 Blender & Food Processor (BN800ME)"
        base_price = 649

    elif any(w in clean_query for w in ["غسالة", "صحون", "اطباق", "بوش", "بيكو"]):
        category_title = "أفضل غسالات صحون في السعودية ومطابقة مواصفات SASO"
        p1 = {
            "title": "أولاً: Bosch Serie 4 Free-Standing (SMS46GI01E)",
            "price": "متوسط السعر المتداول: 2,499 ريال سعودي",
            "img": "https://m.media-amazon.com/images/I/61hX0R2aV+L._AC_SL1500_.jpg",
            "specs": [
                "<b>السعة والأداء:</b> 12 مكان تخزين، صناعة ألمانية/تركية معتمدة وفق أعلى كفاءة طاقة.",
                "<b>التقنية الحصرية:</b> نظام حماية الزجاج الدقيق ومحرك EcoSilence Drive الهادئ للغاية.",
                "<b>التقييم:</b> الفئة الأولى في الاعتمادية وجودة التجفيف والتحمل طويل الأمد."
            ]
        }
        p2 = {
            "title": "ثانياً: Midea 14 Place Settings Freestanding (WQP14J7633)",
            "price": "السعر الحالي في عروض أمازون: 1,299 ريال سعودي (بدلاً من 1,699)",
            "img": "https://m.media-amazon.com/images/I/61E1N8P1rNL._AC_SL1500_.jpg",
            "specs": [
                "<b>السعة والأداء:</b> 14 مكان تخزين واسع مع رف ثالث مخصص لأدوات المائدة.",
                "<b>التقنية الحصرية:</b> غسيل نصف الحمولة لتوفير الماء والكهرباء مع تعقيم بدرجة حرارة 70° مئوية.",
                "<b>التقييم:</b> القيمة الأعلى مقابل السعر بالسوق السعودي وأكثر موديل طلباً."
            ]
        }
        p3 = {
            "title": "ثالثاً: Beko 14 Place Settings (DFN05320W)",
            "price": "متوسط السعر المتداول: 1,149 ريال سعودي",
            "img": "https://m.media-amazon.com/images/I/61b7Q5YgZRL._AC_SL1500_.jpg",
            "specs": [
                "<b>السعة والأداء:</b> 14 مكان تخزين بـ 5 برامج غسيل مختلفة.",
                "<b>التقنية الحصرية:</b> نظام الحماية من تسرب المياه ومرونة تعديل الرف العلوي للأواني الكبيرة.",
                "<b>التقييم:</b> الخيار الاقتصادي الأنسب للعائلات بميزانية في متناول اليد."
            ]
        }
        table_md = """
| اسم الموديل | عدد الأماكن | مستوى الضجيج | كفاءة الطاقة | متوسط السعر المتداول | الميزة التنافسية |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bosch Serie 4** | 12 مكان | 46 ديسيبل (فائق الهدوء) | فئة ممتازة | 2,499 ر.س | متانة خامات استثنائية ونظام تجفيف مثالي |
| **Midea 14 Place** | 14 مكان | 49 ديسيبل | فئة ممتازة SASO | 1,299 ر.س (تخفيض حالي) | 14 مكان + رف ثالث للملاعق بأفضل سعر |
| **Beko 14 Place** | 14 مكان | 50 ديسيبل | معتمد | 1,149 ر.س | سعر اقتصادي وبرامج غسيل سريعة |
"""
        winner_name = "Midea 14 Place Settings Dishwasher"
        base_price = 1299

    else:
        # الفئة الافتراضية: القلايات الهوائية
        category_title = "أفضل قلاية هوائية في السعودية"
        p1 = {
            "title": "أولاً: Philips Combi 7000 Series (HD9880)",
            "price": "متوسط السعر المتداول: 1,599 ريال سعودي",
            "img": "https://m.media-amazon.com/images/I/71gV4eU1h-L._AC_SL1500_.jpg",
            "specs": [
                "<b>السعة الفعالة:</b> 8.3 لتر (سلة فردية عملاقة تتسع لوجبة عائلية كاملة).",
                "<b>القوة الكهربائية:</b> 2200 واط متوافقة مع الجهد الكهربائي السعودي (230V / 60Hz).",
                "<b>التقنية الحصرية:</b> مسبار حراري ذكي مدمج (Food Thermometer) لقياس نضج اللحوم من الداخل بدقة بالغة.",
                "<b>التقييم:</b> الفئة الأعلى في دقة الطهي، لكن سعرها مرتفع وتعتمد على منطقة طهي واحدة."
            ]
        }
        p2 = {
            "title": "ثانياً: Ninja Foodi FlexBasket 10.4L (AF500ME)",
            "price": "السعر الحالي بأمازون (عرض اليوم الوطني): 899 ريال سعودي (بدلاً من 1,499)",
            "img": "https://m.media-amazon.com/images/I/81x12B3h6UL._AC_SL1500_.jpg",
            "specs": [
                "<b>السعة الفعالة:</b> 10.4 لتر مع نظام المقسم الذكي (درجين 5.2 لتر أو درج عملاق 10.4 لتر).",
                "<b>القوة الكهربائية:</b> 2470 واط تسخين فائق السرعة ومطابقة للمواصفات والمقابس السعودية SASO.",
                "<b>التقنية الحصرية:</b> FlexBasket لطهي صنفين مختلفين معاً أو وجبة ضخمة دفعة واحدة.",
                "<b>التقييم:</b> الخيار الأكثر توازناً وعملية للعائلات بفضل المرونة وسعر التخفيض الاستثنائي."
            ]
        }
        p3 = {
            "title": "ثالثاً: Instant Vortex Plus Dual ClearCook (140-3095)",
            "price": "متوسط السعر المتداول: 749 ريال سعودي",
            "img": "https://m.media-amazon.com/images/I/71s8L5qj0kL._AC_SL1500_.jpg",
            "specs": [
                "<b>السعة الفعالة:</b> 7.6 لتر مقسمة على درجين منفصلين تماماً (3.8 لتر لكل درج).",
                "<b>القوة الكهربائية:</b> 1700 واط اقتصادية في استهلاك الطاقة.",
                "<b>التقنية الحصرية:</b> نافذة رؤية شفافة ClearCook مع فلاتر كربون مدمجة لمنع الروائح.",
                "<b>التقييم:</b> ممتازة للمطابخ المغلقة ولمحبي التحكم بالروائح والميزانيات الاقتصادية."
            ]
        }
        table_md = """
| اسم الموديل | السعة الفعالة | القوة الكهربائية | التقنية الأبرز | متوسط السعر المتداول | الميزة التنافسية الحصرية |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Philips Combi 7000 (HD9880)** | 8.3 لتر (منطقة واحدة) | 2200 واط | الذكاء الاصطناعي ومسبار الحرارة | 1,599 ر.س | أدق استواء للحوم بفضل المسبار الذكي والاتصال بالإنترنت |
| **Ninja FlexBasket (AF500ME)** | 10.4 لتر (1 أو 2 درج) | 2470 واط | التحويل الذكي للمساحة FlexBasket | 899 ر.س (تخفيض حالي) | مرونة غير محدودة لطهي وجبات عائلية ضخمة أو صنفين منفصلين |
| **Instant Vortex Dual (140-3095)** | 7.6 لتر (درجين منفصلين) | 1700 واط | فلاتر الكربون ومنع الروائح | 749 ر.س | بيئة مطبخ خالية من الروائح مع إمكانية مراقبة الطعام بالكامل |
"""
        winner_name = "Ninja Foodi FlexBasket 10.4L (AF500ME)"
        base_price = 899

    # دالة مساعدة لعرض كارت المنتج مع الصورة بجواره
    def display_product_card(prod):
        st.markdown(f'<div class="product-box">', unsafe_allow_html=True)
        col_img, col_txt = st.columns([1, 2.5])
        with col_img:
            st.image(prod['img'], use_container_width=True)
        with col_txt:
            st.markdown(f'<div class="product-title">{prod["title"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="price-tag">{prod["price"]}</div>', unsafe_allow_html=True)
            for spec in prod['specs']:
                st.markdown(f"• {spec}", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    
    # أولاً وثانياً وثالثاً بالصور
    display_product_card(p1)
    display_product_card(p2)
    display_product_card(p3)

    st.markdown("---")

    # رابعاً: جدول المقارنة
    st.subheader(f"رابعاً: جدول المقارنة الفني الشامل ({category_title})")
    st.markdown(table_md)

    st.markdown("---")

    # خامساً: الصفقة الرابحة وحسابات البنوك
    st.subheader("خامساً: أقوى صفقة رابحة وتخفيض (أفضل قيمة مقابل السعر)")

    if "جميع البنوك" in selected_bank:
        p_french = max(base_price - 100, 0)
        p_rajhi = max(base_price - 100, 0)
        p_inma = max(base_price - 75, 0)
        net_price = p_french

        st.markdown(f"""
        <div class="deal-card">
            <h4 style="color: #28a745; margin-top: 0;">🏆 الفائز بأقوى عرض وتخفيض: {winner_name}</h4>
            <p>السعر الأساسي الحالي بالعرض: <b>{base_price} ريال</b>.</p>
            <p><b>جدول مقارنة الأسعار بحسب خصومات بطاقات البنوك السعودية:</b></p>
            <table style="width:100%; border-collapse: collapse; text-align: right; margin-bottom: 15px;">
                <tr style="background-color: #e8f5e9;">
                    <th style="padding: 8px; border: 1px solid #c8e6c9;">البنك / البطاقة</th>
                    <th style="padding: 8px; border: 1px solid #c8e6c9;">كود / تفاصيل الخصم</th>
                    <th style="padding: 8px; border: 1px solid #c8e6c9;">السعر النهائي بعد التخفيض</th>
                </tr>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd;"><b>البنك السعودي الفرنسي BSF</b></td>
                    <td style="padding: 8px; border: 1px solid #ddd;">كود <code>BSF20</code> (خصم 100 ر.س) / <code>BSF25</code> لبرايم</td>
                    <td style="padding: 8px; border: 1px solid #ddd; color: #d93025; font-weight: bold;">{p_french} ريال</td>
                </tr>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd;"><b>مصرف الراجحي</b></td>
                    <td style="padding: 8px; border: 1px solid #ddd;">خصم مباشر إضافي 100 ر.س</td>
                    <td style="padding: 8px; border: 1px solid #ddd; color: #d93025; font-weight: bold;">{p_rajhi} ريال</td>
                </tr>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd;"><b>البنك الأهلي SNB</b></td>
                    <td style="padding: 8px; border: 1px solid #ddd;">خصم مباشر إضافي 100 ر.س</td>
                    <td style="padding: 8px; border: 1px solid #ddd; color: #d93025; font-weight: bold;">{p_rajhi} ريال</td>
                </tr>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd;"><b>مصرف الإنماء</b></td>
                    <td style="padding: 8px; border: 1px solid #ddd;">خصم إضافي 75 ر.س</td>
                    <td style="padding: 8px; border: 1px solid #ddd; color: #d93025; font-weight: bold;">{p_inma} ريال</td>
                </tr>
                <tr>
                    <td style="padding: 8px; border: 1px solid #ddd;"><b>بدون بطاقة بنكية (كاش)</b></td>
                    <td style="padding: 8px; border: 1px solid #ddd;">سعر العرض المباشر بأمازون</td>
                    <td style="padding: 8px; border: 1px solid #ddd; font-weight: bold;">{base_price} ريال</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
    else:
        discount_val = 0
        if "BSF" in selected_bank or "الفرنسي" in selected_bank or "الراجحي" in selected_bank or "الأهلي" in selected_bank:
            discount_val = 100
        elif "الإنماء" in selected_bank:
            discount_val = 75
        elif "الرياض" in selected_bank:
            discount_val = 50

        net_price = max(base_price - discount_val, 0)

        st.markdown(f"""
        <div class="deal-card">
            <h4 style="color: #28a745; margin-top: 0;">🏆 الفائز بأقوى عرض وتخفيض: {winner_name}</h4>
            <ul>
                <li><b>السعر في التخفيضات الحالية:</b> {base_price} ريال سعودي.</li>
                <li><b>السعر الصافي التقريبي بعد خصم البنك:</b> <span style="font-size: 1.3rem; font-weight: 800; color: #d93025;">{net_price} ريال سعودي</span> (توفير {discount_val} ريال).</li>
                <li><b>ملاحظة:</b> إذا كنت تستخدم بطاقة الفرنسي BSF مع برايم استخدم كود <code>BSF25</code> لخصم أكبر.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # 7. روابط الشراء والمشاركة التفاعلية
    encoded_search = urllib.parse.quote(winner_name)
    amazon_affiliate_url = f"https://www.amazon.sa/s?k={encoded_search}&tag={AMAZON_TAG}"
    noon_url = f"https://www.noon.com/saudi-ar/search/?q={encoded_search}"

    wa_message = f"""🔥 أقوى عروض وتخفيضات الأجهزة المنزلية بأمازون السعودية!

الجهاز: {winner_name}
السعر بالعرض: {base_price} ريال
السعر بعد خصم البنك: يصل إلى {net_price} ريال تقريباً!

فحص ومقارنة العروض والخصومات:
{APP_URL}

رابط الشراء المباشر من أمازون:
{amazon_affiliate_url}"""

    wa_url = f"https://api.whatsapp.com/send?text={urllib.parse.quote(wa_message)}"

    # 8. أزرار الشراء والمشاركة
    col_buy, col_share = st.columns(2)

    with col_buy:
        st.markdown(f"**🛍️ الشراء المباشر للصفقة الرابحة:** `{winner_name}`")
        st.markdown(f'<a href="{amazon_affiliate_url}" target="_blank" class="btn-amazon">🛒 فتح السلعة في أمازون</a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{noon_url}" target="_blank" class="btn-noon">🟡 فتح السلعة في نون</a>', unsafe_allow_html=True)

    with col_share:
        st.markdown("**📲 نشر التوفير (مشاركة تسوّق نفسها):**")
        st.markdown(f'<a href="{wa_url}" target="_blank" class="btn-whatsapp">🟢 مشاركة هذه الصفقة فوراً عبر واتساب</a>', unsafe_allow_html=True)
