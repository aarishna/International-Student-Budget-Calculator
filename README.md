# 🍁 Canada Student Cost Estimator

A comprehensive cost-of-living calculator for international students planning to study in Canada. Provides detailed expense breakdowns, multi-city comparisons, and budget visualization tools.

---

## 🎯 Purpose

Helps international students:
- **Estimate** total annual costs (tuition + living expenses)
- **Compare** tuition across 20+ programs and 30+ universities
- **Plan** budgets for different lifestyle choices
- **Understand** how program choice affects total cost
- **Visualize** spending patterns through interactive charts
- **Export** personalized budget reports

---

## ✨ Features

### 🎓 Program-Specific Tuition
**20 major programs** with realistic tuition adjustments:
- **STEM:** Engineering (1.4x), Computer Science (1.35x), Sciences (1.1x)
- **Health:** Medicine (2.0x), Dentistry (1.8x), Nursing (1.2x)
- **Professional:** Law (1.5x), Business (1.25x), Architecture (1.3x)
- **Liberal Arts:** Arts/Humanities (0.95x), Social Sciences (0.95x), Education (0.9x)
- **Creative:** Fine Arts (1.0x), Communications (1.0x)
- **Trades:** Culinary Arts (0.85x), Hospitality (0.85x)

*Multipliers based on typical international student tuition variations*

### 📊 Comprehensive Expense Tracking
- **Housing:** Rent, utilities, internet
- **Transportation:** Public transit costs (or free university passes)
- **Food:** Groceries + dining out
- **Lifestyle:** Entertainment, social activities, shopping
- **Summer Planning:** Options to stay, relocate, or go home

### 🎓 University Database
**30+ institutions** across Canada with pre-loaded international student tuition:

**Toronto (4):**
- University of Toronto ($58k)
- York University ($35k)
- Toronto Metropolitan University ($33k)
- OCAD University ($27k)

**Vancouver (3):**
- UBC ($51k)
- Simon Fraser University ($32k)
- Emily Carr University ($24k)

**Montreal (3):**
- McGill University ($48k)
- Concordia University ($29k)
- Université de Montréal ($27k)

**Ottawa (3):**
- University of Ottawa ($45k)
- Carleton University ($33k)
- Algonquin College ($16k)

**Calgary (3):**
- University of Calgary ($32k)
- Mount Royal University ($21k)
- SAIT Polytechnic ($18k)

**Edmonton (3):**
- University of Alberta ($31k)
- MacEwan University ($20k)
- NAIT ($17k)

**Waterloo (3):**
- University of Waterloo ($53k)
- Wilfrid Laurier University ($28k)
- Conestoga College ($16k)

**Other Cities:**
- University of Guelph ($31k)
- Université Laval - Quebec City ($26k)
- University of Manitoba ($19k)
- Dalhousie University ($28k)
- Plus 5 more institutions

*Custom university option available for any institution*

### 📈 Visual Analytics
- Monthly expense breakdown (pie charts)
- Annual cost distribution (bar charts)
- Multi-city comparison charts

### 💾 Export Options
- CSV reports with detailed breakdowns
- Timestamped for record-keeping
- Easy to share with family/advisors

---

## 🚀 How to Run

### Option 1: Web App (Streamlit) - **Recommended**
```bash
# Install dependencies
pip install streamlit matplotlib pandas

# Run the app
streamlit run app.py
```
Then open your browser to `http://localhost:8501`

### Option 2: Command-Line Interface (CLI)
```bash
# Install dependencies
pip install matplotlib pandas

# Run the script
python cost_estimator.py
```

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/canada-student-cost-estimator.git
cd canada-student-cost-estimator

# Install requirements
pip install -r requirements.txt

# Run your preferred version
streamlit run app.py          # Web version
python cost_estimator.py      # CLI version
```

**requirements.txt:**
```
streamlit>=1.28.0
matplotlib>=3.7.0
pandas>=2.0.0
```

---

## 🏙️ Supported Cities & Universities

| City | Universities | Avg Monthly Cost* |
|------|-------------|-------------------|
| **Toronto** | U of T, York, TMU, OCAD | $2,500 - $3,000 |
| **Vancouver** | UBC, SFU, Emily Carr | $2,400 - $2,900 |
| **Montreal** | McGill, Concordia, UdeM | $2,100 - $2,600 |
| **Ottawa** | U Ottawa, Carleton, Algonquin | $2,200 - $2,700 |
| **Calgary** | U Calgary, MRU, SAIT | $2,300 - $2,800 |
| **Edmonton** | U Alberta, MacEwan, NAIT | $2,200 - $2,700 |
| **Waterloo** | UWaterloo, Laurier, Conestoga | $2,200 - $2,700 |
| **Guelph** | U Guelph | $2,100 - $2,600 |
| **Quebec City** | Laval, Mérici | $1,900 - $2,400 |
| **Winnipeg** | U Manitoba, U Winnipeg, RRC | $2,000 - $2,500 |
| **Halifax** | Dalhousie, SMU, NSCAD | $2,100 - $2,600 |

*\*Estimates include rent, groceries, utilities, transport (varies by lifestyle)*

Each city includes localized data for groceries, utilities, transportation, and internet costs.

---

## 📸 Screenshots

### Web Interface (Streamlit)
![Dashboard Overview](screenshots/dashboard.png)  
*Interactive budget calculator with real-time updates*

![Expense Charts](screenshots/charts.png)  
*Visual breakdown of monthly and annual costs*

### CLI Interface
![CLI Demo](screenshots/cli.png)  
*Terminal-based calculator with guided input*

---

## 🛠️ Technical Details

**Built with:**
- Python 3.8+
- Streamlit (web framework)
- Matplotlib (visualizations)
- Pandas (data handling)

**Code Quality:**
- DRY principles (no repeated logic)
- Type hints for better readability
- Comprehensive input validation
- Error handling & graceful exits

---

## 📝 Usage Example

### Streamlit App
1. **Select your university** (auto-fills city and base tuition)
2. **Choose your program/major** (adjusts tuition automatically)
3. Enter monthly rent and select included utilities
4. Add lifestyle expenses (dining, entertainment, etc.)
5. Choose summer plans (stay, relocate, or go home)
6. View instant calculations and charts
7. Download CSV report

### CLI Version
```
$ python cost_estimator.py

🍁 CANADA STUDENT COST ESTIMATOR
═══════════════════════════════════════════════

SELECT YOUR UNIVERSITY
═══════════════════════════════════════════════

📍 TORONTO
1. University of Toronto ($58k)
2. York University ($35k)
...

Select university number: 17

SELECT YOUR PROGRAM/MAJOR
═══════════════════════════════════════════════
1. ⚙️  Engineering                              ~$74k
2. 💻 Computer Science                          ~$72k
3. 💼 Business/Commerce                         ~$66k
4. 🩺 Medicine                                  ~$106k
5. 🦷 Dentistry                                 ~$95k
...

Select program number: 2

✓ University of Waterloo - Waterloo
✓ Program: 💻 Computer Science
✓ Estimated Int'l Tuition: $71,550

Use this tuition amount? (y/n): y

🏠 HOUSING EXPENSES - WATERLOO
═══════════════════════════════════════════════
Monthly rent (CAD): $1200
...

📊 COST ESTIMATE
═══════════════════════════════════════════════
🎓 University: University of Waterloo
📍 City: Waterloo
📚 Program: Computer Science

💰 MONTHLY (Fall/Winter): $2,547
   Rent                          $1,200.00
   Groceries                       $370.00
   ...

📅 ANNUAL BREAKDOWN:
   Fall & Winter (8 months)     $20,376.00
   Summer (4 months)            $10,188.00
   Tuition                      $71,550.00
   ─────────────────────────────────────────
   TOTAL                        $102,114.00
```

---

## 🎓 For Students

This tool is designed to help you:
1. **Budget realistically** before arriving in Canada
2. **Avoid financial surprises** during your first year
3. **Make informed decisions** about city and lifestyle choices
4. **Present financial proof** for visa applications

> **Note:** All costs are estimates based on 2024 data. Actual expenses may vary based on personal choices and inflation.

---

## 🤝 Contributing

Contributions welcome! To improve the tool:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/university-data`)
3. Commit changes (`git commit -m 'Add X university tuition data'`)
4. Push to branch (`git push origin feature/university-data`)
5. Open a Pull Request

**Ideas for contributions:**
- Add more universities
- Update cost data for 2025
- Add new cities
- Improve visualizations
- Add PDF export functionality

---


## 👤 Author 

Aarish Naiyer
[GitHub]([https://github.com/aarish_na](https://github.com/aarishna/aarishna.git)) | [LinkedIn](https://linkedin.com/in/aarishna)

*Built to help international students navigate the financial planning process for studying in Canada* 🍁

---

## 🙏 Acknowledgments

- Cost data sourced from the Government of Canada and university websites
- Inspired by the challenges faced by international students
- Built with feedback from current students across Canada
- This is an open-source project
---

## ⚠️ Disclaimer

This tool provides estimates only. Actual costs vary based on:
- Individual lifestyle choices
- Inflation and market changes  
- Specific program fees
- Personal circumstances

Always verify current costs with official university sources and the [Government of Canada](https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit/prepare/get-documents.html).

---

**Made with ❤️ for international students coming to Canada**
