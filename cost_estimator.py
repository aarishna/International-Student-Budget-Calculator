"""
International Student Cost of Living Estimator for Canada
A comprehensive tool to estimate living expenses for international students.
"""

import matplotlib.pyplot as plt
import csv
import sys
from datetime import datetime
from typing import Dict, List

# ============================================================================
# CONFIGURATION
# ============================================================================

PROGRAMS = {
    "Engineering": {"multiplier": 1.4, "emoji": "⚙️"},
    "Computer Science": {"multiplier": 1.35, "emoji": "💻"},
    "Business/Commerce": {"multiplier": 1.25, "emoji": "💼"},
    "Medicine": {"multiplier": 2.0, "emoji": "🩺"},
    "Dentistry": {"multiplier": 1.8, "emoji": "🦷"},
    "Law": {"multiplier": 1.5, "emoji": "⚖️"},
    "Architecture": {"multiplier": 1.3, "emoji": "🏛️"},
    "Sciences (Biology, Chemistry, Physics)": {"multiplier": 1.1, "emoji": "🔬"},
    "Mathematics/Statistics": {"multiplier": 1.0, "emoji": "📊"},
    "Arts/Humanities": {"multiplier": 0.95, "emoji": "📚"},
    "Social Sciences": {"multiplier": 0.95, "emoji": "🌍"},
    "Fine Arts/Design": {"multiplier": 1.0, "emoji": "🎨"},
    "Nursing": {"multiplier": 1.2, "emoji": "🏥"},
    "Education": {"multiplier": 0.9, "emoji": "👨‍🏫"},
    "Psychology": {"multiplier": 1.0, "emoji": "🧠"},
    "Economics": {"multiplier": 1.15, "emoji": "📈"},
    "Environmental Studies": {"multiplier": 1.0, "emoji": "🌱"},
    "Communications/Media": {"multiplier": 1.0, "emoji": "📡"},
    "Culinary Arts": {"multiplier": 0.85, "emoji": "👨‍🍳"},
    "Hospitality/Tourism": {"multiplier": 0.85, "emoji": "🏨"},
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
    # Toronto
    "University of Toronto": {"city": "Toronto", "tuition_intl": 58160},
    "York University": {"city": "Toronto", "tuition_intl": 35000},
    "Toronto Metropolitan University (TMU)": {"city": "Toronto", "tuition_intl": 33000},
    "OCAD University": {"city": "Toronto", "tuition_intl": 27000},
    
    # Vancouver
    "University of British Columbia (UBC)": {"city": "Vancouver", "tuition_intl": 51000},
    "Simon Fraser University (SFU)": {"city": "Vancouver", "tuition_intl": 32000},
    "Emily Carr University": {"city": "Vancouver", "tuition_intl": 24000},
    
    # Montreal
    "McGill University": {"city": "Montreal", "tuition_intl": 48000},
    "Concordia University": {"city": "Montreal", "tuition_intl": 29000},
    "Université de Montréal": {"city": "Montreal", "tuition_intl": 27000},
    
    # Ottawa
    "University of Ottawa": {"city": "Ottawa", "tuition_intl": 45000},
    "Carleton University": {"city": "Ottawa", "tuition_intl": 33000},
    "Algonquin College": {"city": "Ottawa", "tuition_intl": 16000},
    
    # Calgary
    "University of Calgary": {"city": "Calgary", "tuition_intl": 32000},
    "Mount Royal University": {"city": "Calgary", "tuition_intl": 21000},
    "SAIT Polytechnic": {"city": "Calgary", "tuition_intl": 18000},
    
    # Edmonton
    "University of Alberta": {"city": "Edmonton", "tuition_intl": 31000},
    "MacEwan University": {"city": "Edmonton", "tuition_intl": 20000},
    "NAIT": {"city": "Edmonton", "tuition_intl": 17000},
    
    # Waterloo
    "University of Waterloo": {"city": "Waterloo", "tuition_intl": 53000},
    "Wilfrid Laurier University": {"city": "Waterloo", "tuition_intl": 28000},
    "Conestoga College": {"city": "Waterloo", "tuition_intl": 16000},
    
    # Guelph
    "University of Guelph": {"city": "Guelph", "tuition_intl": 31000},
    
    # Quebec City
    "Université Laval": {"city": "Quebec City", "tuition_intl": 26000},
    "Collège Mérici": {"city": "Quebec City", "tuition_intl": 14000},
    
    # Winnipeg
    "University of Manitoba": {"city": "Winnipeg", "tuition_intl": 19000},
    "University of Winnipeg": {"city": "Winnipeg", "tuition_intl": 17000},
    "Red River College": {"city": "Winnipeg", "tuition_intl": 15000},
    
    # Halifax
    "Dalhousie University": {"city": "Halifax", "tuition_intl": 28000},
    "Saint Mary's University": {"city": "Halifax", "tuition_intl": 21000},
    "NSCAD University": {"city": "Halifax", "tuition_intl": 19000},
    
    "Custom/Other": {"city": None, "tuition_intl": 0}
}

FALL_WINTER_MONTHS = 8
SUMMER_MONTHS = 4

# ============================================================================
# INPUT UTILITIES (Unified & DRY)
# ============================================================================

def get_input(prompt: str, type_='float', min_val=0, allow_zero=False) -> float:
    """Unified input validation."""
    while True:
        try:
            value = float(input(prompt)) if type_ == 'float' else int(input(prompt))
            if value < min_val or (value == 0 and not allow_zero):
                print(f"Please enter a value {'> 0' if not allow_zero else f'>= {min_val}'}")
            else:
                return value
        except (ValueError, KeyboardInterrupt):
            if isinstance(sys.exc_info()[1], KeyboardInterrupt):
                print("\n\nExiting..."); sys.exit(0)
            print("Invalid input. Try again.")

def get_yes_no(prompt: str) -> bool:
    """Get yes/no response."""
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes']: return True
        if response in ['n', 'no']: return False
        print("Enter 'y' or 'n'")

def select_from_menu(title: str, options: List[str]) -> int:
    """Display menu and get selection."""
    print(f"\n{'='*60}\n{title}\n{'='*60}")
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")
    print("="*60)
    while True:
        try:
            choice = int(input("\nSelect: "))
            if 1 <= choice <= len(options): return choice
            print(f"Enter 1-{len(options)}")
        except ValueError:
            print("Enter a number")

# ============================================================================
# DATA COLLECTION (Refactored)
# ============================================================================

def select_university() -> tuple:
    """Select university and get city/tuition."""
    options = list(UNIVERSITIES.keys())
    
    # Group by city for better display
    print("\n" + "="*60)
    print("SELECT YOUR UNIVERSITY")
    print("="*60)
    
    current_city = None
    idx = 1
    uni_map = {}
    
    for uni, data in UNIVERSITIES.items():
        if data['city'] != current_city and data['city'] is not None:
            current_city = data['city']
            print(f"\n📍 {current_city.upper()}")
        
        if uni == "Custom/Other":
            print(f"\n🔧 OTHER")
            print(f"{idx}. {uni}")
        else:
            tuition_k = data['tuition_intl'] // 1000
            print(f"{idx}. {uni} (${tuition_k}k)")
        
        uni_map[idx] = uni
        idx += 1
    
    print("="*60)
    
    while True:
        try:
            choice = int(input("\nSelect university number: "))
            if 1 <= choice < idx:
                break
            print(f"Enter 1-{idx-1}")
        except ValueError:
            print("Enter a number")
    
    uni = uni_map[choice]
    
    if uni == "Custom/Other":
        cities = list(CITY_DATA.keys())
        city_choice = select_from_menu("SELECT YOUR CITY", cities)
        city = cities[city_choice - 1]
        print(f"\n📚 Custom University in {city}")
        tuition = get_input("Enter annual tuition (CAD): $")
        return city, tuition, uni
    
    city = UNIVERSITIES[uni]["city"]
    tuition = UNIVERSITIES[uni]["tuition_intl"]
    print(f"\n✓ {uni} - {city} (Int'l Tuition: ${tuition:,})")
    if get_yes_no("Use this tuition amount? (y/n): "):
        return city, tuition, uni
    tuition = get_input("Enter your tuition (CAD): $")
    return city, tuition, uni

def collect_housing(city: str) -> Dict:
    """Collect housing expenses."""
    print(f"\n{'='*60}\n🏠 HOUSING EXPENSES - {city.upper()}\n{'='*60}")
    rent = get_input("Monthly rent (CAD): $")
    
    util_incl = get_yes_no("Rent includes utilities? (y/n): ")
    utilities = 0 if util_incl else get_input(
        f"Monthly utilities (CAD, default ${CITY_DATA[city]['utilities']}): $", allow_zero=True
    ) or CITY_DATA[city]['utilities']
    
    net_incl = get_yes_no("Rent includes internet? (y/n): ")
    internet = 0 if net_incl else get_input(
        f"Internet & phone (CAD, default ${CITY_DATA[city]['internet_phone']}): $", allow_zero=True
    ) or CITY_DATA[city]['internet_phone']
    
    transport_covered = get_yes_no("Transportation covered by university? (y/n): ")
    
    return {
        'rent': rent, 'utilities': utilities, 'internet': internet,
        'transport_covered': transport_covered, 'util_incl': util_incl, 'net_incl': net_incl
    }

def collect_lifestyle() -> Dict[str, float]:
    """Collect lifestyle expenses."""
    print(f"\n{'='*60}\n🎉 LIFESTYLE EXPENSES\n{'='*60}")
    
    categories = [
        ("Dining Out", "🍽️  restaurants/delivery"),
        ("Entertainment", "🎬 movies/concerts/streaming"),
        ("Social Activities", "☕ cafes/bars/friends")
    ]
    
    lifestyle = {}
    for name, desc in categories:
        print(f"\n{desc}")
        times = get_input(f"Times per month: ", type_='int', allow_zero=True)
        if times > 0:
            avg = get_input(f"Avg cost per time: $", allow_zero=True)
            lifestyle[name] = times * avg
        else:
            lifestyle[name] = 0
    
    lifestyle["Shopping"] = get_input("\n🛍️  Shopping budget (monthly): $", allow_zero=True)
    lifestyle["Miscellaneous"] = get_input("🔧 Misc (gym/haircuts/etc): $", allow_zero=True)
    
    print(f"\nTotal Lifestyle: ${sum(lifestyle.values()):,.2f}")
    return lifestyle

def collect_summer(city: str, housing: Dict, lifestyle: Dict) -> Dict:
    """Collect summer plans."""
    options = [f"Staying in {city}", "Moving to another city", "Going home"]
    choice = select_from_menu("☀️ SUMMER PLANS", options)
    
    if choice == 1:
        return {'type': 'staying'}
    elif choice == 3:
        return {'type': 'home'}
    else:
        cities = [c for c in CITY_DATA.keys() if c != city]
        city_choice = select_from_menu("Summer city:", cities)
        summer_city = cities[city_choice - 1]
        summer_housing = collect_housing(summer_city)
        summer_lifestyle = collect_lifestyle()
        return {'type': 'moving', 'city': summer_city, **summer_housing, 'lifestyle': summer_lifestyle}

# ============================================================================
# CALCULATIONS
# ============================================================================

def calculate_costs(city: str, tuition: float, housing: Dict, lifestyle: Dict, summer: Dict) -> Dict:
    """Calculate all costs."""
    city_costs = CITY_DATA[city]
    
    monthly = {
        "Rent": housing['rent'],
        "Groceries": city_costs["groceries"],
        "Utilities": housing['utilities'],
        "Internet & Phone": housing['internet'],
        "Transportation": 0 if housing['transport_covered'] else city_costs["transportation"],
        **lifestyle
    }
    
    fall_winter_total = sum(monthly.values()) * FALL_WINTER_MONTHS
    
    if summer['type'] == 'home':
        summer_total = 0
    elif summer['type'] == 'staying':
        summer_total = sum(monthly.values()) * SUMMER_MONTHS
    else:
        sc = CITY_DATA[summer['city']]
        summer_monthly = sum([
            summer['rent'], sc['groceries'], summer['utilities'], summer['internet'],
            0 if summer['transport_covered'] else sc['transportation'],
            *summer['lifestyle'].values()
        ])
        summer_total = summer_monthly * SUMMER_MONTHS
    
    return {
        'monthly': monthly,
        'fall_winter': fall_winter_total,
        'summer': summer_total,
        'tuition': tuition,
        'total': fall_winter_total + summer_total + tuition
    }

# ============================================================================
# OUTPUT & VISUALIZATION
# ============================================================================

def display_summary(city: str, uni: str, costs: Dict, summer: Dict):
    """Display complete summary."""
    print(f"\n{'='*60}\n📊 COST ESTIMATE - {uni}\n{'='*60}")
    print(f"\n💰 MONTHLY (Fall/Winter): ${sum(costs['monthly'].values()):,.2f}")
    for cat, val in costs['monthly'].items():
        if val > 0: print(f"   {cat:<30} ${val:>10,.2f}")
    
    print(f"\n📅 ANNUAL BREAKDOWN:")
    print(f"   Fall & Winter (8 months)     ${costs['fall_winter']:>12,.2f}")
    print(f"   Summer (4 months)            ${costs['summer']:>12,.2f}")
    print(f"   Tuition                      ${costs['tuition']:>12,.2f}")
    print(f"   {'─'*45}")
    print(f"   TOTAL                        ${costs['total']:>12,.2f}")
    print("="*60)

def create_visualizations(city: str, costs: Dict):
    """Create all charts."""
    data = {k: v for k, v in costs['monthly'].items() if v > 0}
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Pie chart
    colors = plt.cm.Set3(range(len(data)))
    ax1.pie(data.values(), labels=data.keys(), autopct='%1.1f%%', colors=colors)
    ax1.set_title(f'Monthly Breakdown - ${sum(data.values()):,.0f}')
    
    # Bar chart
    annual_data = {'Fall/Winter': costs['fall_winter'], 'Summer': costs['summer'], 
                   'Tuition': costs['tuition']}
    bars = ax2.bar(annual_data.keys(), annual_data.values(), 
                   color=['#2E86AB', '#F18F01', '#A23B72'])
    ax2.set_ylabel('Amount (CAD)')
    ax2.set_title(f'Annual Breakdown - ${costs["total"]:,.0f}')
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, height,
                f'${height:,.0f}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()

def export_csv(city: str, uni: str, costs: Dict):
    """Export to CSV."""
    filename = f"estimate_{city.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['International Student Cost Estimate'])
        writer.writerow(['University', uni])
        writer.writerow(['City', city])
        writer.writerow(['Date', datetime.now().strftime("%Y-%m-%d")])
        writer.writerow([])
        writer.writerow(['MONTHLY EXPENSES'])
        for cat, val in costs['monthly'].items():
            if val > 0: writer.writerow([cat, f"{val:.2f}"])
        writer.writerow([])
        writer.writerow(['ANNUAL SUMMARY'])
        writer.writerow(['Fall & Winter', f"{costs['fall_winter']:.2f}"])
        writer.writerow(['Summer', f"{costs['summer']:.2f}"])
        writer.writerow(['Tuition', f"{costs['tuition']:.2f}"])
        writer.writerow(['TOTAL', f"{costs['total']:.2f}"])
    print(f"\n✓ Exported to: {filename}")

# ============================================================================
# MAIN
# ============================================================================

def main():
    print("\n" + "="*60)
    print("🍁 CANADA STUDENT COST ESTIMATOR")
    print("="*60)
    
    city, tuition, uni = select_university()
    housing = collect_housing(city)
    lifestyle = collect_lifestyle()
    summer = collect_summer(city, housing, lifestyle)
    
    costs = calculate_costs(city, tuition, housing, lifestyle, summer)
    
    display_summary(city, uni, costs, summer)
    create_visualizations(city, costs)
    
    if get_yes_no("\nExport to CSV? (y/n): "):
        export_csv(city, uni, costs)
    
    if get_yes_no("\nCalculate for another university? (y/n): "):
        main()
    else:
        print("\n🍁 Good luck with your studies in Canada!\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)