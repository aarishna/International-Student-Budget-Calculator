# 🍁 Canada Student Cost Estimator

A comprehensive cost-of-living calculator for international students planning to study in Canada. Provides detailed expense breakdowns, multi-city comparisons, and budget visualization tools using cloud-hosted data.

---

## 🎯 Purpose

Helps international students:
- Estimate total annual costs (tuition + living expenses)
- Compare tuition across 20+ programs and 30+ universities
- Plan budgets for different lifestyle choices
- Understand how program choice affects total cost
- Visualize spending patterns through interactive charts
- Export personalized budget reports

---

## ✨ Features

### ☁️ Dynamic Cloud Data (Amazon S3)
- University, program, and city cost data is fetched dynamically from Amazon S3
- Eliminates hardcoded datasets
- Enables updates without redeploying the application
- Centralized, scalable, production-style data storage

### 🎓 Program-Specific Tuition
20 major programs with realistic tuition adjustments:
- STEM: Engineering (1.4x), Computer Science (1.35x), Sciences (1.1x)
- Health: Medicine (2.0x), Dentistry (1.8x), Nursing (1.2x)
- Professional: Law (1.5x), Business (1.25x), Architecture (1.3x)
- Liberal Arts: Arts/Humanities (0.95x), Social Sciences (0.95x), Education (0.9x)
- Creative: Fine Arts (1.0x), Communications (1.0x)
- Trades: Culinary Arts (0.85x), Hospitality (0.85x)

Multipliers based on typical international student tuition variations.

### 📊 Comprehensive Expense Tracking
- Housing: Rent, utilities, internet
- Transportation: Public transit or free university passes
- Food: Groceries and dining out
- Lifestyle: Entertainment, social activities, shopping
- Summer Planning: Stay, relocate, or return home

### 🎓 University Database
30+ institutions across Canada with international tuition data loaded dynamically.

Toronto:
- University of Toronto ($58k)
- York University ($35k)
- Toronto Metropolitan University ($33k)
- OCAD University ($27k)

Vancouver:
- UBC ($51k)
- Simon Fraser University ($32k)
- Emily Carr University ($24k)

Montreal:
- McGill University ($48k)
- Concordia University ($29k)
- Université de Montréal ($27k)

Ottawa:
- University of Ottawa ($45k)
- Carleton University ($33k)
- Algonquin College ($16k)

Calgary:
- University of Calgary ($32k)
- Mount Royal University ($21k)
- SAIT Polytechnic ($18k)

Edmonton:
- University of Alberta ($31k)
- MacEwan University ($20k)
- NAIT ($17k)

Waterloo:
- University of Waterloo ($53k)
- Wilfrid Laurier University ($28k)
- Conestoga College ($16k)

Other cities include Guelph, Quebec City, Winnipeg, Halifax, and more.

Custom university option available.

### 📈 Visual Analytics
- Monthly expense breakdown (pie charts)
- Annual cost distribution (bar charts)
- Multi-period expense visualization

### 💾 Export Options
- CSV budget reports
- Timestamped exports
- Shareable with family and advisors

---

## 🚀 How to Run

Web App (Streamlit):
1. Install dependencies: pip install streamlit matplotlib pandas requests
2. Run the app: streamlit run app.py
3. Open http://localhost:8501

CLI Version:
1. Install dependencies: pip install matplotlib pandas requests
2. Run the script: python cost_estimator.py

---

## 📦 Installation

1. Clone the repository:
   git clone https://github.com/aarishna/International-Student-Budget-Calculator.git
2. Navigate to the project directory:
   cd canada-student-cost-estimator
3. Install requirements:
   pip install -r requirements.txt
4. Run the application:
   streamlit run app.py

Requirements:
- streamlit >= 1.28.0
- matplotlib >= 3.7.0
- pandas >= 2.0.0
- requests >= 2.30.0

---

## 🏙️ Supported Cities & Universities

Toronto: $2,500–$3,000  
Vancouver: $2,400–$2,900  
Montreal: $2,100–$2,600  
Ottawa: $2,200–$2,700  
Calgary: $2,300–$2,800  
Edmonton: $2,200–$2,700  
Waterloo: $2,200–$2,700  
Guelph: $2,100–$2,600  
Quebec City: $1,900–$2,400  
Winnipeg: $2,000–$2,500  
Halifax: $2,100–$2,600  

Estimates include rent, groceries, utilities, and transportation.

---

## 🛠️ Technical Details

Built with:
- Python 3.8+
- Streamlit
- Pandas
- Matplotlib
- Amazon S3 (cloud data source)

Design highlights:
- No hardcoded datasets
- Cloud-driven configuration
- Modular and DRY architecture
- Graceful error handling
- Resume-grade project structure

---

## 🎓 For Students

This tool helps you:
- Budget realistically before arriving in Canada
- Avoid financial surprises
- Compare cities and programs confidently
- Prepare financial documentation for visa applications

All values are estimates and may vary.

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 👤 Author

Aarish Naiyer  
GitHub: https://github.com/aarishna  
LinkedIn: https://linkedin.com/in/aarishna  

---

## ⚠️ Disclaimer

This tool provides estimates only. Actual costs vary based on lifestyle, inflation, and university-specific fees. Always verify with official sources.

---

Made with ❤️ for international students coming to Canada
