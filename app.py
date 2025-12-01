"""
Streamlit Web Application for International Student Cost Estimator
Run with: streamlit run app.py
"""

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# ============================================================================
# DATA
# ============================================================================

PROGRAMS = {
    "Engineering": {"multiplier": 1.4, "emoji": "⚙️"},
    "Computer Science": {"multiplier": 1.35, "emoji": "💻"},
    "Business/Commerce": {"multiplier": 1.25, "emoji": "💼"},
    "Medicine": {"multiplier": 2.0, "emoji": "🩺"},
    "Dentistry": {"multiplier": 1.8, "emoji": "🦷"},
    "Law": {"multiplier": 1.5, "emoji": "⚖️"},
    "Architecture": {"multiplier": 1.3, "emoji": "🏛️"},
    "Sciences": {"multiplier": 1.1, "emoji": "🔬"},
    "Mathematics": {"multiplier": 1.0, "emoji": "📊"},
    "Arts/Humanities": {"multiplier": 0.95, "emoji": "📚"},
    "Social Sciences": {"multiplier": 0.95, "emoji": "🌍"},
    "Fine Arts/Design": {"multiplier": 1.0, "emoji": "🎨"},
    "Nursing": {"multiplier": 1.2, "emoji": "🏥"},
    "Education": {"multiplier": 0.9, "emoji": "👨‍🏫"},
    "Psychology": {"multiplier": 1.0, "emoji": "🧠"},
    "Economics": {"multiplier": 1.15, "emoji": "📈"},
    "Environmental Studies": {"multiplier": 1.0, "emoji": "🌱"},
    "Communications": {"multiplier": 1.0, "emoji": "📡"},
    "Culinary Arts": {"multiplier": 0.85, "emoji": "👨‍🍳"},
    "Hospitality": {"multiplier": 0.85, "emoji": "🏨"},
}

CITY_DATA = {
    "Toronto": {"groceries": 400, "utilities": 150, "transportation": 156, "internet_phone": 80},
    "Vancouver": {"groceries": 420, "utilities": 130, "transportation": 136, "internet_phone": 75},
    "Montreal": {"groceries": 350, "utilities": 120, "transportation": 94, "internet_phone": 70},
    "Ottawa": {"groceries": 380, "utilities": 140, "transportation": 122, "internet_phone": 75},
    "Calgary": {"groceries": 390, "utilities": 160, "transportation": 112, "internet_phone": 80},
    "Edmonton": {"groceries": 370, "utilities": 155, "transportation": 103, "internet_phone": 75},
    "Waterloo": {"groceries": 370, "utilities": 145, "transportation": 100, "internet_phone": 75},
    "Guelph": {"groceries": 365, "utilities": 140, "transportation": 95, "internet_phone": 75},
    "Quebec City": {"groceries": 340, "utilities": 115, "transportation": 90, "internet_phone": 70},
    "Winnipeg": {"groceries": 360, "utilities": 145, "transportation": 105, "internet_phone": 70},
    "Halifax": {"groceries": 385, "utilities": 135, "transportation": 82, "internet_phone": 75}
}

UNIVERSITIES = {
    # Toronto (4)
    "University of Toronto": {"city": "Toronto", "tuition": 58160},
    "York University": {"city": "Toronto", "tuition": 35000},
    "Toronto Metropolitan University": {"city": "Toronto", "tuition": 33000},
    "OCAD University": {"city": "Toronto", "tuition": 27000},
    
    # Vancouver (3)
    "UBC": {"city": "Vancouver", "tuition": 51000},
    "Simon Fraser University": {"city": "Vancouver", "tuition": 32000},
    "Emily Carr University": {"city": "Vancouver", "tuition": 24000},
    
    # Montreal (3)
    "McGill University": {"city": "Montreal", "tuition": 48000},
    "Concordia University": {"city": "Montreal", "tuition": 29000},
    "Université de Montréal": {"city": "Montreal", "tuition": 27000},
    
    # Ottawa (3)
    "University of Ottawa": {"city": "Ottawa", "tuition": 45000},
    "Carleton University": {"city": "Ottawa", "tuition": 33000},
    "Algonquin College": {"city": "Ottawa", "tuition": 16000},
    
    # Calgary (3)
    "University of Calgary": {"city": "Calgary", "tuition": 32000},
    "Mount Royal University": {"city": "Calgary", "tuition": 21000},
    "SAIT Polytechnic": {"city": "Calgary", "tuition": 18000},
    
    # Edmonton (3)
    "University of Alberta": {"city": "Edmonton", "tuition": 31000},
    "MacEwan University": {"city": "Edmonton", "tuition": 20000},
    "NAIT": {"city": "Edmonton", "tuition": 17000},
    
    # Waterloo (3)
    "University of Waterloo": {"city": "Waterloo", "tuition": 53000},
    "Wilfrid Laurier University": {"city": "Waterloo", "tuition": 28000},
    "Conestoga College": {"city": "Waterloo", "tuition": 16000},
    
    # Guelph (1)
    "University of Guelph": {"city": "Guelph", "tuition": 31000},
    
    # Quebec City (2)
    "Université Laval": {"city": "Quebec City", "tuition": 26000},
    "Collège Mérici": {"city": "Quebec City", "tuition": 14000},
    
    # Winnipeg (3)
    "University of Manitoba": {"city": "Winnipeg", "tuition": 19000},
    "University of Winnipeg": {"city": "Winnipeg", "tuition": 17000},
    "Red River College": {"city": "Winnipeg", "tuition": 15000},
    
    # Halifax (3)
    "Dalhousie University": {"city": "Halifax", "tuition": 28000},
    "Saint Mary's University": {"city": "Halifax", "tuition": 21000},
    "NSCAD University": {"city": "Halifax", "tuition": 19000},
    
    "Custom/Other": {"city": None, "tuition": 0}
}

# ============================================================================
# CONFIG
# ============================================================================

st.set_page_config(page_title="Canada Student Budget", page_icon="🍁", layout="wide")

st.markdown("""
<style>
    .main-header {font-size: 2.5rem; color: #FF0000; text-align: center; margin-bottom: 0.5rem;}
    .sub-header {font-size: 1.1rem; color: #666; text-align: center; margin-bottom: 1.5rem;}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>🍁 Canada Student Budget Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Plan Your International Student Expenses</p>", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR INPUTS
# ============================================================================

with st.sidebar:
    st.header("🎓 University & Program")
    
    # Group universities by city for better UX
    uni_options = []
    for uni, data in UNIVERSITIES.items():
        if uni == "Custom/Other":
            uni_options.append(uni)
        else:
            city_short = data['city'].split()[0]
            tuition_k = data['tuition'] // 1000
            uni_options.append(f"{uni} ({city_short}, ${tuition_k}k)")
    
    uni_display = st.selectbox("Select university:", uni_options)
    
    # Extract actual university name
    if "Custom/Other" in uni_display:
        uni = "Custom/Other"
    else:
        uni = uni_display.split(" (")[0]
    
    # Always show program selection
    program_options = [f"{PROGRAMS[p]['emoji']} {p}" for p in PROGRAMS.keys()]
    program_display = st.selectbox("Select your program/major:", program_options, 
                                     help="Different programs have different tuition rates")
    program = program_display.split(" ", 1)[1]  # Remove emoji
    
    if uni == "Custom/Other":
        city = st.selectbox("Select city:", list(CITY_DATA.keys()))
        tuition = st.number_input("Annual Tuition (CAD)", min_value=0, value=25000, step=1000)
    else:
        city = UNIVERSITIES[uni]["city"]
        base_tuition = UNIVERSITIES[uni]["tuition"]
        
        # Show info about tuition calculation
        multiplier = PROGRAMS[program]["multiplier"]
        if multiplier != 1.0:
            st.info(f"ℹ️ {program} tuition is typically {multiplier}x the base rate")
        
        # Calculate adjusted tuition based on program
        adjusted_tuition = int(base_tuition * multiplier)
        
        tuition = st.number_input(
            f"Annual Tuition (CAD)", 
            min_value=0, 
            value=adjusted_tuition, 
            step=1000,
            help=f"Estimated for {program}: ${base_tuition:,} × {multiplier} = ${adjusted_tuition:,}"
        )
        st.caption(f"📍 {city} | Base rate: ${base_tuition:,}/year")
    
    st.header("🏠 Housing")
    rent = st.number_input("Monthly Rent (CAD)", min_value=0, value=1200, step=50)
    
    rent_incl_util = st.checkbox("Rent includes utilities")
    utilities = 0 if rent_incl_util else st.number_input(
        "Utilities (CAD/month)", min_value=0, value=CITY_DATA[city]["utilities"], step=10)
    
    rent_incl_internet = st.checkbox("Rent includes internet")
    internet = 0 if rent_incl_internet else st.number_input(
        "Internet & Phone (CAD/month)", min_value=0, value=CITY_DATA[city]["internet_phone"], step=5)
    
    transport_covered = st.checkbox("Free transit pass from university")
    
    st.header("🎉 Lifestyle")
    dining = st.number_input("Dining Out (monthly)", min_value=0, value=200, step=20)
    entertainment = st.number_input("Entertainment (monthly)", min_value=0, value=100, step=10)
    social = st.number_input("Social Activities (monthly)", min_value=0, value=150, step=10)
    shopping = st.number_input("Shopping (monthly)", min_value=0, value=100, step=10)
    misc = st.number_input("Miscellaneous (monthly)", min_value=0, value=100, step=10)
    
    st.header("☀️ Summer (4 months)")
    summer_type = st.radio("Where will you be?",
        ["Staying in same city", "Moving to another city", "Going home"])
    
    summer_city = city
    summer_rent = rent
    if summer_type == "Moving to another city":
        summer_city = st.selectbox("Summer city:", [c for c in CITY_DATA.keys() if c != city])
        summer_rent = st.number_input("Summer rent", min_value=0, value=1000, step=50)

# ============================================================================
# CALCULATIONS
# ============================================================================

city_costs = CITY_DATA[city]

monthly_expenses = {
    "Rent": rent,
    "Groceries": city_costs["groceries"],
    "Utilities": utilities,
    "Internet & Phone": internet,
    "Transportation": 0 if transport_covered else city_costs["transportation"],
    "Dining Out": dining,
    "Entertainment": entertainment,
    "Social": social,
    "Shopping": shopping,
    "Miscellaneous": misc
}

monthly_total = sum(monthly_expenses.values())
fall_winter_total = monthly_total * 8

if summer_type == "Going home":
    summer_total = 0
elif summer_type == "Staying in same city":
    summer_total = monthly_total * 4
else:
    sc = CITY_DATA[summer_city]
    summer_monthly = summer_rent + sc["groceries"] + sc["utilities"] + sc["internet_phone"] + sc["transportation"]
    summer_total = summer_monthly * 4

annual_total = fall_winter_total + summer_total + tuition

# ============================================================================
# DISPLAY
# ============================================================================

# Header with university and program info
st.info(f"🎓 **{uni}** | 📍 {city} | 📚 {program} | 💰 Tuition: ${tuition:,}")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Monthly", f"${monthly_total:,.0f}", "Fall/Winter")
col2.metric("8 Months", f"${fall_winter_total:,.0f}", "Fall + Winter")
col3.metric("4 Months", f"${summer_total:,.0f}", "Summer")
col4.metric("Annual Total", f"${annual_total:,.0f}", "All-in")

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["📊 Breakdown", "📈 Charts", "💾 Export"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Monthly Expenses")
        df = pd.DataFrame({
            'Category': monthly_expenses.keys(),
            'Amount': monthly_expenses.values()
        })
        df = df[df['Amount'] > 0]
        st.dataframe(df.style.format({'Amount': '${:,.2f}'}), hide_index=True, use_container_width=True)
        st.metric("Total", f"${monthly_total:,.0f}")
    
    with col2:
        st.subheader("Annual Summary")
        summary = pd.DataFrame({
            'Period': ['Fall & Winter (8mo)', 'Summer (4mo)', 'Tuition', 'TOTAL'],
            'Amount': [fall_winter_total, summer_total, tuition, annual_total]
        })
        st.dataframe(summary.style.format({'Amount': '${:,.2f}'}), hide_index=True, use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Monthly Distribution")
        data = {k: v for k, v in monthly_expenses.items() if v > 0}
        fig, ax = plt.subplots(figsize=(8, 8))
        colors = plt.cm.Set3(range(len(data)))
        ax.pie(data.values(), labels=data.keys(), autopct='%1.1f%%', colors=colors, startangle=90)
        ax.set_title(f"${monthly_total:,.0f}/month", fontsize=14, fontweight='bold')
        st.pyplot(fig)
    
    with col2:
        st.subheader("Annual Breakdown")
        fig, ax = plt.subplots(figsize=(8, 6))
        periods = ['Fall/Winter', 'Summer', 'Tuition']
        amounts = [fall_winter_total, summer_total, tuition]
        bars = ax.bar(periods, amounts, color=['#2E86AB', '#F18F01', '#A23B72'])
        ax.set_ylabel("Amount (CAD)", fontweight='bold')
        ax.set_title(f"Total: ${annual_total:,.0f}", fontsize=14, fontweight='bold')
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, h, f'${h:,.0f}', 
                   ha='center', va='bottom', fontweight='bold')
        st.pyplot(fig)

with tab3:
    st.subheader("Download Your Budget")
    
    export_data = pd.DataFrame({
        'Category': ['University', 'City', 'Program', '', 'MONTHLY EXPENSES'] + 
                    list(monthly_expenses.keys()) + 
                    ['', 'ANNUAL SUMMARY', 'Fall & Winter Total', 'Summer Total', 
                     'Tuition', 'ANNUAL TOTAL'],
        'Amount': [uni, city, program, '', ''] + 
                  list(monthly_expenses.values()) + 
                  ['', '', fall_winter_total, summer_total, tuition, annual_total]
    })
    
    csv = export_data.to_csv(index=False)
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name=f"budget_{uni.replace(' ', '_')}_{program.replace('/', '_')}_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )
    
    st.info("💡 **Tip:** You can screenshot the charts above for your records!")

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; font-size: 0.9rem;'>
    Made for international students 🍁 | Data based on 2024 estimates
</div>
""", unsafe_allow_html=True)