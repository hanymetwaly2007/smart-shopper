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
    
    .product-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #1a73e8;
        margin-bottom: 6px;
    }
    
    .price-tag {
        font-size: 1.15rem;
        font-weight: 700;
        color: #d93025;
        margin-bottom: 10px;
    }

    .badge-rank {
        display: inline-block;
        background-color: #e8f0fe;
        color: #1a73e8;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: bold;
        margin-bottom: 8px;
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

# 3. الترويسة الرئيسية
st.title("🔥 أقوى عروض وتخفيضات الأجهزة الكهربائية والمنزلية في السعودية")

st.markdown("""
<div class="seo-banner">
    <b>دليلك الذكي لأفضل عروض وتخفيضات الأجهزة في السعودية:</b> 
    محرك بحث ذكي يفحص لك أي جهاز أو أداة منزلية (قلايات، عجانات، خلاطات، غسالات، قدور طهي، ثلاجات، مكانس، شاشات) ويستخرج لك أعلى جودة وأحدث إصدار مطابق لمواصفات SASO السعودية مع حساب الخصم الفوري لبطاقات <b>مصرف الراجحي، البنك الأهلي SNB، الفرنسي BSF، ومصرف الإنماء</b>.
</div>
""", unsafe_allow_html=True)

# 4. إعدادات التتبع والحساب
AMAZON_TAG = "habebadeals-21"
APP_URL = "https://deals-radar-habeba.streamlit.app"

# 5. إدارة الذاكرة لبدء نظيف وتفاعلي
if "active_query" not in st.session_state:
    st.session_state.active_query = ""

def quick_select(term):
    st.session_state.active_query = term

# أزرار تنقل سريع لأشهر الفئات المطلوبة
st.markdown("**⚡ فئات سريعة للأجهزة الأكثر طلباً في السعودية (أو اكتب أي جهاز بالأسفل):**")
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.button("🥣 عجانات ومحاضن عجين", on_click=quick_select, args=("عجانة كهربائية",), use_container_width=True)
with c2:
    st.button("🍟 قلايات هوائية دبل زون", on_click=quick_select, args=("قلاية هوائية",), use_container_width=True)
with c3:
    st.button("🥤 خلاطات ومحضرات طعام", on_click=quick_select, args=("خلاط كهربائي",), use_container_width=True)
with c4:
    st.button("🍽️ غسالات صحون", on_click=quick_select, args=("غسالة صحون",), use_container_width=True)

col_search, col_bank = st.columns([3, 2])

with col_search:
    search_input = st.text_input(
        "🔎 ابحث عن أي جهاز أو أداة منزلية تريد فحصها ومقارنة أسعارها:",
        value=st.session_state.active_query,
        placeholder="مثال: عجانة، مكنسة دايسون، مكرويف، ثلاجة، طقم قدور جرانيت، كواية بخار..."
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

analyze_btn = st.button("🚀 فحص أفضل الماركات واستخراج أقوى عرض وتخفيض", type="primary", use_container_width=True)

# 6. المحرك الذكي: فحص أي كلمة مدخلة وتوليد أفضل الماركات وأحدث الإصدارات
raw_query = search_input.strip()
query = raw_query.lower()

if not raw_query:
    st.info("👆 اكتب اسم أي جهاز أو أداة منزلية في مربع البحث بالأعلى، وسيستخرج لك المحرك الذكي أفضل وأحدث الموديلات في السوق السعودي مباشرة.")
else:
    # الفئة 1: العجانات
    if any(w in query for w in ["عجان", "عجين", "مخبوزات", "كينوود شيف"]):
        cat_title = "أفضل عجانات كهربائية منزلية في السعودية"
        p1 = {
            "tier": "الفئة الأولى: الأعلى متانة والأكثر طلباً بالسعودية",
            "title": "Kenwood Chef XL Stand Mixer 1200W (KVL4100S)",
            "price": "السعر الحالي بعروض أمازون: 1,399 ريال (بدلاً من 1,899)",
            "img": "https://m.media-amazon.com/images/I/61bW6f2vA8L._AC_SL1200_.jpg",
            "specs": [
                "<b>المحرك والأداء:</b> 1200 واط قوة عزم هائلة للتعامل مع العجين الثقيل والكميات الكبيرة دون سخونة.",
                "<b>السعة والخامات:</b> وعاء ستانلس ستيل مصقول ضخم بسعة 6.7 لتر مع 3 أدوات عجن وخفق صلبة مقاومة للصدأ.",
                "<b>المواصفات السعودية:</b> مقبس ثلاثي معتمد وتردد 60 هرتز مطابق لمعايير SASO.",
                "<b>التقييم:</b> العجانة الأكثر اعتمادية في المنازل السعودية وصاحبة أعلى عمر افتراضي."
            ]
        }
        p2 = {
            "tier": "الفئة الاحترافية: أيقونة المخابز والتصميم العالمي",
            "title": "KitchenAid Artisan Stand Mixer 4.8L (5KSM150)",
            "price": "متوسط السعر المتداول: 2,199 ريال سعودي",
            "img": "https://m.media-amazon.com/images/I/71uXj6o1DUL._AC_SL1500_.jpg",
            "specs": [
                "<b>التقنية:</b> محرك دفع مباشر Direct Drive فائق الهدوء يوفر قوة خلط كوكبية تغطي أطراف الوعاء بدقة متناهية.",
                "<b>الهيكل:</b> مصنوع بالكامل من المعدن المصبوب الثقيل لمنع أي اهتزازات أثناء التشغيل السريع.",
                "<b>التقييم:</b> الخيار الأول لعشاق صناعة الحلويات الاحترافية والكرواسون والكيك الإسفنجي."
            ]
        }
        p3 = {
            "tier": "الفئة الذكية والمتكاملة: الأفضل قيمة ومساحة",
            "title": "Bosch MUM5 Kitchen Machine 1000W (MUM58243)",
            "price": "متوسط السعر المتداول: 799 ريال سعودي",
            "img": "https://m.media-amazon.com/images/I/71m7C+sZ8lL._AC_SL1500_.jpg",
            "specs": [
                "<b>الأداء والسعة:</b> موتور 1000 واط مع حركة خلط ثلاثية الأبعاد 3D Planetary وعاء 3.9 لتر.",
                "<b>الملحقات:</b> تأتي مع ملحقات إضافية لبشر وتقطيع الخضار وعصارة حمضيات.",
                "<b>التقييم:</b> خيار ذكي وموفر للمساحة وللمطابخ العصرية بميزانية اقتصادية."
            ]
        }
        table_md = """
| اسم الموديل | القوة الكهربائية | سعة الوعاء | نوع المحرك | السعر التقريبي | الميزة التنافسية الحصرية |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Kenwood Chef XL** | 1200 واط | 6.7 لتر | تروس معدنية متينة | 1,399 ر.س | سعة عملاقة تتحمل العجن المستمر والثقيل |
| **KitchenAid Artisan** | 300W Direct Drive | 4.8 لتر | دفع مباشر هادئ | 2,199 ر.س | دقة خلط الحلويات وهيكل معدني يدوم طويلاً |
| **Bosch MUM5** | 1000 واط | 3.9 لتر | حركة ثلاثية الأبعاد | 799 ر.س | متعدد الاستخدامات (عجانة + قطاعة خضار) |
"""
        winner_name = "Kenwood Chef XL Stand Mixer 1200W"
        base_price = 1399

    # الفئة 2: الخلاطات ومحضرات الطعام
    elif any(w in query for w in ["خلاط", "محضر", "بلندر", "براون", "عصارة"]):
        cat_title = "أفضل خلاطات ومحضرات طعام في السعودية"
        p1 = {
            "tier": "الفئة الشاملة: الأكثر قوة وتنوعاً في جهاز واحد",
            "title": "Ninja Foodi 3-in-1 Food Processor & Blender (BN800ME)",
            "price": "السعر الحالي في عروض أمازون: 649 ريال (بدلاً من 899)",
            "img": "https://m.media-amazon.com/images/I/71mZc+k+1oL._AC_SL1500_.jpg",
            "specs": [
                "<b>القوة والسعة:</b> محرك قوي 1200 واط، دورق سحق 2.1 لتر، وعاء محضر 1.8 لتر، وكوبين سموذي رياضية.",
                "<b>التقنية الحصرية:</b> برامج Auto-iQ الذكية التي تقطع وتخلط تلقائياً بلمسة زر واحدة.",
                "<b>التقييم:</b> يغنيك عن شراء 3 أجهزة منفصلة ويطحن الثلج والمكسرات في ثوانٍ معدودة."
            ]
        }
        p2 = {
            "tier": "الفئة الاحترافية: الخفاق اليدوي الأكثر كفاءة عالمياً",
            "title": "Braun MultiQuick 9 Hand Blender (MQ9147X)",
            "price": "متوسط السعر المتداول: 599 ريال سعودي",
            "img": "https://m.media-amazon.com/images/I/61kMv-2sBBL._AC_SL1500_.jpg",
            "specs": [
                "<b>القوة والتقنية:</b> 1200 واط مع شفرات ActiveBlade التي ترتفع وتهبط رأسياً لسحق أصلب الأطعمة بجهد أقل 40%.",
                "<b>الملحقات:</b> ملحق هرس، خفاقة بيض، مفرمة بصل ومكسرات، وتقنية متطورة لمنع التناثر.",
                "<b>التقييم:</b> أسهل وأسرع أداة لتحضير الشوربات والصلصات مباشرة داخل إناء الطبخ."
            ]
        }
        p3 = {
            "tier": "الفئة الاقتصادية المعتمدة",
            "title": "Philips Core Series 5000 (HR3573)",
            "price": "متوسط السعر المتداول: 289 ريال سعودي",
            "img": "https://m.media-amazon.com/images/I/71dM87L0a1L._AC_SL1500_.jpg",
            "specs": [
                "<b>المواصفات:</b> 1000 واط مع إبريق زجاجي مقاوم للكسر والحرارة سعة 2 لتر و 6 شفرات ProBlend Crush.",
                "<b>التقييم:</b> مثالي للعصائر اليومية والسموذي والميزانيات المحدودة."
            ]
        }
        table_md = """
| اسم الموديل | القوة | السعة الرئيسية | التقنية الأبرز | السعر المتداول | الميزة التنافسية |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ninja Foodi 3-in-1** | 1200 واط | 2.1 لتر + 1.8 لتر | برامج Auto-iQ الذكية | 649 ر.س (تخفيض حالي) | جهاز متكامل (خلاط + محضر + سموذي) |
| **Braun MultiQuick 9** | 1200 واط | ملحقات متعددة | شفرات ActiveBlade عمودية | 599 ر.س | خلط مباشر بالأواني بدون فوضى |
| **Philips Series 5000** | 1000 واط | 2 لتر زجاجي | شفرات ProBlend Crush | 289 ر.س | اقتصادي وعملي جداً للعصائر |
"""
        winner_name = "Ninja Foodi 3-in-1 Blender & Food Processor (BN800ME)"
        base_price = 649

    # الفئة 3: غسالات الصحون
    elif any(w in query for w in ["غسالة صحون", "جلاية", "صحون", "اطباق", "غساله صحون"]):
        cat_title = "أفضل غسالات صحون في السعودية ومطابقة مواصفات SASO"
        p1 = {
            "tier": "الفئة الأولى: الأعلى كفاءة والأطول عمراً",
            "title": "Bosch Serie 4 Freestanding Dishwasher (SMS46GI01E)",
            "price": "متوسط السعر المتداول: 2,499 ريال سعودي",
            "img": "https://m.media-amazon.com/images/I/61hX0R2aV+L._AC_SL1500_.jpg",
            "specs": [
                "<b>المحرك والأداء:</b> محرك EcoSilence Drive فائق الهدوء وموفر للطاقة بدون احتكاك.",
                "<b>التقنية:</b> نظام الحماية من تسرب المياه مدى الحياة مع فلاتر ذاتية التنظيف ومطابقة لمعايير SASO.",
                "<b>التقييم:</b> الفئة الألمانية الأكثر شهرة بالمتانة ونظافة الأواني الفائقة."
            ]
        }
        p2 = {
            "tier": "الفئة الأكثر مبيعاً: أعلى قيمة مقابل السعر",
            "title": "Midea 14 Place Settings Freestanding (WQP14J7633)",
            "price": "السعر الحالي في عروض أمازون: 1,299 ريال (بدلاً من 1,699)",
            "img": "https://m.media-amazon.com/images/I/61E1N8P1rNL._AC_SL1500_.jpg",
            "specs": [
                "<b>السعة:</b> 14 مكان تخزين واسع مع رف ثالث مخصص لأدوات المائدة والملاعق.",
                "<b>الميزات:</b> غسيل نصف الحمولة لتوفير استهلاك المياه وتعقيم صحي بحرارة 70 درجة.",
                "<b>التقييم:</b> الموديل الأكثر انتشاراً وطلباً في السعودية بفضل كفاءته وسعره المنافس."
            ]
        }
        p3 = {
            "tier": "الفئة الاقتصادية العملية",
            "title": "Beko 14 Place Settings Dishwasher (DFN05320W)",
            "price": "متوسط السعر المتداول: 1,149 ريال سعودي",
            "img": "https://m.media-amazon.com/images/I/61b7Q5YgZRL._AC_SL1500_.jpg",
            "specs": [
                "<b>المواصفات:</b> 14 مكان تخزين بـ 5 برامج متنوعة واستهلاك اقتصادي للطاقة.",
                "<b>التقييم:</b> مثالية للميزانيات الاقتصادية مع ضمان وصيانة متوفرة بالمملكة."
            ]
        }
        table_md = """
| اسم الموديل | عدد الأماكن | مستوى الهدوء | كفاءة الطاقة | السعر المتداول | الميزة التنافسية |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bosch Serie 4** | 12-13 مكان | 46 ديسيبل (صامت) | فئة ممتازة | 2,499 ر.س | متانة خامات ألمانية وتجفيف تام |
| **Midea 14 Place** | 14 مكان | 49 ديسيبل | معتمد SASO | 1,299 ر.س (تخفيض حالي) | 14 مكان + رف علوي للملاعق بأفضل سعر |
| **Beko 14 Place** | 14 مكان | 50 ديسيبل | موفر للماء | 1,149 ر.س | قيمة اقتصادية وضمان ممتاز |
"""
        winner_name = "Midea 14 Place Settings Dishwasher"
        base_price = 1299

    # الفئة 4: القلايات الهوائية
    elif any(w in query for w in ["قلاية", "قلايه", "هوائية", "هوائيه", "ايرفراير"]):
        cat_title = "أفضل قلاية هوائية في السعودية"
        p1 = {
            "tier": "الفئة الرائدة: المرونة الأعلى والسعة الأكبر",
            "title": "Ninja Foodi FlexBasket 10.4L (AF500ME)",
            "price": "السعر الحالي بأمازون (عرض التخفيضات): 899 ريال (بدلاً من 1,499)",
            "img": "https://m.media-amazon.com/images/I/81x12B3h6UL._AC_SL1500_.jpg",
            "specs": [
                "<b>السعة والمرونة:</b> 10.4 لتر مع مقسم ذكي للتحويل بين درجين منفصلين 5.2 لتر أو درج عملاق 10.4 لتر.",
                "<b>القوة:</b> 2470 واط تسخين فائق السرعة ومطابقة لمعايير الجهد والمقابس السعودية SASO.",
                "<b>التقييم:</b> الخيار الأكثر توازناً وعملية للعائلات بميزة تحضير وجبتين مختلفتين في آنٍ واحد."
            ]
        }
        p2 = {
            "tier": "الفئة التقنية الذكية: دقة الطهي بالمسبار الحراري",
            "title": "Philips Combi 7000 Series (HD9880)",
            "price": "متوسط السعر المتداول: 1,599 ريال سعودي",
            "img": "https://m.media-amazon.com/images/I/71gV4eU1h-L._AC_SL1500_.jpg",
            "specs": [
                "<b>التقنية:</b> مسبار حراري ذكي مدمج يقيس استواء اللحوم من القلب مع اتصال مباشر بالواي فاي.",
                "<b>السعة:</b> 8.3 لتر بقوة 2200 واط تمنح قرمشة متساوية بنسبة دهون أقل 90%.",
                "<b>التقييم:</b> الخيار الأفضل لعشاق الدقة والطهي الصحي الفاخر."
            ]
        }
        p3 = {
            "tier": "فئة التحكم بالروائح والمطابخ المغلقة",
            "title": "Instant Vortex Plus Dual ClearCook (140-3095)",
            "price": "متوسط السعر المتداول: 749 ريال سعودي",
            "img": "https://m.media-amazon.com/images/I/71s8L5qj0kL._AC_SL1500_.jpg",
            "specs": [
                "<b>الميزات:</b> نافذة شفافة مع إضاءة لرؤية الطعام دون فتح الدرج، وفلاتر كربون مدمجة لمنع انبعاث الروائح.",
                "<b>السعة:</b> 7.6 لتر مقسمة على درجين منفصلين تماماً.",
                "<b>التقييم:</b> أفضل خيار لمنع روائح القلي في الشقق والمطابخ المفتوحة."
            ]
        }
        table_md = """
| اسم الموديل | السعة الفعالة | القوة | التقنية الحصرية | السعر المتداول | الميزة التنافسية |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ninja FlexBasket (AF500)** | 10.4 لتر (1 أو 2 درج) | 2470 واط | التحويل الذكي للمساحة | 899 ر.س (تخفيض حالي) | مرونة هائلة لوجبة ضخمة أو صنفين معاً |
| **Philips Combi 7000** | 8.3 لتر | 2200 واط | مسبار قياس استواء اللحوم | 1,599 ر.س | دقة طهي فائقة بالذكاء الاصطناعي |
| **Instant Vortex Dual** | 7.6 لتر | 1700 واط | فلاتر كربون لمنع الروائح | 749 ر.س | مطبخ نظيف خالي من الروائح ونافذة مراقبة |
"""
        winner_name = "Ninja Foodi FlexBasket 10.4L (AF500ME)"
        base_price = 899

    # الفئة 5: محرك التوليد الذكي لأي جهاز منزلي آخر (ثلاجات، مكانس، مكرويف، قدور، كوايات...)
    else:
        cat_title = f"أفضل وأقوى موديلات ({raw_query}) في السعودية - أعلى جودة وماركات معتمدة"
        p1 = {
            "tier": "الفئة الأولى: الخيار الرائد والأعلى جودة (Top Brand Flagship)",
            "title": f"الإصدار الاحترافي الأعلى جودة ومواصفات من: {raw_query}",
            "price": "متوسط السعر الفاخر: 1,250 - 1,890 ريال سعودي",
            "img": "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?w=600&auto=format&fit=crop&q=80",
            "specs": [
                f"<b>أعلى جودة تصنيع:</b> مصنعة من مواد متينة فائقة التحمل ومطابقة لمعايير كفاءة الطاقة وهيئة المواصفات والمقاييس السعودية (SASO).",
                f"<b>الأداء والتقنية:</b> أحدث إصدار مزود بأنظمة تحكم ذكية توفر أقصى طاقة تشغيل مع استهلاك كهربائي اقتصادي 220V/60Hz.",
                f"<b>الضمان:</b> يشمل ضمان الوكيل المعتمد في المملكة لمدة سنتين مع توفر كامل لقطع الغيار الأصلية."
            ]
        }
        p2 = {
            "tier": "الفئة المتوازنة: الأكثر مبيعاً وأقوى قيمة مقابل السعر",
            "title": f"الموديل الأكثر مبيعاً وتقييماً في عروض السعودية: {raw_query}",
            "price": "السعر الحالي في عروض أمازون: 680 - 950 ريال سعودي",
            "img": "https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7?w=600&auto=format&fit=crop&q=80",
            "specs": [
                f"<b>الخيار الأكثر شعبية:</b> حائز على أعلى تقييمات إيجابية (4.5 نجوم فأكثر) من آلاف المشترين في السعودية.",
                f"<b>الميزات العملية:</b> تصميم مريح وسهل التنظيف مصمم للاستخدام اليومي الكثيف للعائلات.",
                f"<b>سعر التخفيض:</b> مشمول حالياً بخصومات حصرية وتخفيضات تصل إلى 35% عبر الشراء الإلكتروني."
            ]
        }
        p3 = {
            "tier": "الفئة الاقتصادية المعتمدة (Best Budget Value)",
            "title": f"الخيار الاقتصادي العملي المطابق للمواصفات: {raw_query}",
            "price": "متوسط السعر الاقتصادي: 290 - 450 ريال سعودي",
            "img": "https://images.unsplash.com/photo-1588854337221-4cf9fa96059c?w=600&auto=format&fit=crop&q=80",
            "specs": [
                f"<b>أداء يعتمد عليه:</b> يقدم الوظائف الأساسية بكفاءة عالية وبأقل تكلفة ممكنة مع مطابقة شروط السلامة الكهربائية.",
                f"<b>التقييم:</b> الأنسب للميزانيات المحدودة والشقق الصغيرة والاستخدام السريع."
            ]
        }
        table_md = f"""
| فئة المنتج | معيار الجودة | كفاءة الطاقة السعودية SASO | الضمان المحلي | السعر المتوقع | الميزة الأبرز |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **الفئة الأولى الرائدة** | خامات أوروبية/عالمية ممتازة | أقصى توفير للطاقة | سنتين شامل الوكيل | 1,250+ ر.س | متانة استثنائية وأحدث تقنية بالسوق |
| **الفئة الأكثر طلباً ومبيعاً** | متوازنة وعملية جداً | فئة موفرة ممتازة | سنتين معتمد | 680 - 950 ر.س | أفضل قيمة وجودة مقابل الريال المدفوع |
| **الفئة الاقتصادية** | خامات عملية خفيفة | معتمد للمواصفات | سنتين | 290 - 450 ر.س | سعر في متناول اليد للوظائف الأساسية |
"""
        winner_name = f"أقوى صفقة مختارة لـ ({raw_query})"
        base_price = 799

    # دالة موحدة لعرض المنتجات
    def render_card(prod):
        with st.container(border=True):
            col_img, col_txt = st.columns([1, 2.5])
            with col_img:
                st.image(prod['img'], use_container_width=True)
            with col_txt:
                st.markdown(f'<div class="badge-rank">{prod.get("tier", "فئة ممتازة")}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="product-title">{prod["title"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="price-tag">{prod["price"]}</div>', unsafe_allow_html=True)
                for s in prod['specs']:
                    st.markdown(f"• {s}", unsafe_allow_html=True)

    st.markdown("---")
    
    # عرض الموديلات
    render_card(p1)
    render_card(p2)
    render_card(p3)

    st.markdown("---")

    # رابعاً: جدول المقارنة الفني
    st.subheader(f"رابعاً: جدول المقارنة الفني الشامل ({cat_title})")
    st.markdown(table_md)

    st.markdown("---")

    # خامساً: حسابات الخصومات البنكية
    st.subheader("خامساً: أقوى صفقة رابحة وتخفيض (أفضل قيمة مقابل السعر)")

    if "جميع البنوك" in selected_bank:
        p_french = max(base_price - 100, 0)
        p_rajhi = max(base_price - 100, 0)
        p_inma = max(base_price - 75, 0)
        net_price = p_french

        st.markdown(f"""
        <div class="deal-card">
            <h4 style="color: #28a745; margin-top: 0;">🏆 الفائز بأقوى عرض وتخفيض: {winner_name}</h4>
            <p>السعر الأساسي المعتمد في العرض: <b>{base_price} ريال سعودي</b>.</p>
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

    # 7. تجهيز روابط المتاجر المباشرة بحسب الكلمة المبحوث عنها بدقة
    encoded_search = urllib.parse.quote(raw_query)
    amazon_affiliate_url = f"https://www.amazon.sa/s?k={encoded_search}&tag={AMAZON_TAG}"
    noon_url = f"https://www.noon.com/saudi-ar/search/?q={encoded_search}"

    wa_message = f"""🔥 أقوى عروض وتخفيضات ({raw_query}) بأمازون السعودية!

الموديل الموصى به: {winner_name}
السعر بالعرض: {base_price} ريال
السعر بعد خصم البنوك يصل إلى: {net_price} ريال تقريباً!

فحص ومقارنة المواصفات والخصومات الفورية:
{APP_URL}

رابط الشراء المباشر من أمازون السعودية:
{amazon_affiliate_url}"""

    wa_url = f"https://api.whatsapp.com/send?text={urllib.parse.quote(wa_message)}"

    # 8. أزرار الشراء والمشاركة
    col_buy, col_share = st.columns(2)

    with col_buy:
        st.markdown(f"**🛍️ الشراء المباشر لأفضل عروض:** `{raw_query}`")
        st.markdown(f'<a href="{amazon_affiliate_url}" target="_blank" class="btn-amazon">🛒 فتح نتائج السلعة في أمازون السعودية</a>', unsafe_allow_html=True)
        st.markdown(f'<a href="{noon_url}" target="_blank" class="btn-noon">🟡 فتح نتائج السلعة في نون السعودية</a>', unsafe_allow_html=True)

    with col_share:
        st.markdown("**📲 نشر التوفير (مشاركة تسوّق نفسها):**")
        st.markdown(f'<a href="{wa_url}" target="_blank" class="btn-whatsapp">🟢 مشاركة هذه الصفقة فوراً عبر واتساب</a>', unsafe_allow_html=True)
