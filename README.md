# 🍁 Canada Student Cost Estimator

<<<<<<< HEAD
A comprehensive cost-of-living calculator for international students planning to study in Canada. Provides detailed expense breakdowns, multi-city comparisons, and budget visualization tools using cloud-hosted data.
=======
A comprehensive cost-of-living calculator for international students planning to study in Canada.  
Provides detailed expense breakdowns, multi-city comparisons, and budget visualization tools using cloud-hosted data.
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485

---

## 🎯 Purpose

Helps international students:
<<<<<<< HEAD
- Estimate total annual costs (tuition + living expenses)
- Compare tuition across 20+ programs and 30+ universities
- Plan budgets for different lifestyle choices
- Understand how program choice affects total cost
- Visualize spending patterns through interactive charts
- Export personalized budget reports
=======

- **Estimate** total annual costs (tuition + living expenses)
- **Compare** tuition across 20+ programs and 30+ universities
- **Plan** budgets for different lifestyle choices
- **Understand** how program choice affects total cost
- **Visualize** spending patterns through interactive charts
- **Export** personalized budget reports
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485

---

## ✨ Features

### ☁️ Dynamic Cloud Data (Amazon S3)
<<<<<<< HEAD
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
=======

- University, program, and city cost data fetched dynamically from Amazon S3
- Eliminates hardcoded datasets
- Enables updates without redeploying the application
- Centralized, scalable, production-style data storage

---

### 🎓 Program-Specific Tuition

**20 major programs** with realistic tuition adjustments:

- **STEM:** Engineering (1.4x), Computer Science (1.35x), Sciences (1.1x)
- **Health:** Medicine (2.0x), Dentistry (1.8x), Nursing (1.2x)
- **Professional:** Law (1.5x), Business (1.25x), Architecture (1.3x)
- **Liberal Arts:** Arts/Humanities (0.95x), Social Sciences (0.95x), Education (0.9x)
- **Creative:** Fine Arts (1.0x), Communications (1.0x)
- **Trades:** Culinary Arts (0.85x), Hospitality (0.85x)

*Multipliers based on typical international student tuition variations.*

---

### 📊 Comprehensive Expense Tracking

- **Housing:** Rent, utilities, internet
- **Transportation:** Public transit or free university passes
- **Food:** Groceries and dining out
- **Lifestyle:** Entertainment, social activities, shopping
- **Summer Planning:** Stay, relocate, or return home

---

### 🎓 University Database

**30+ institutions** across Canada with international tuition data loaded dynamically.

**Toronto**
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485
- University of Toronto ($58k)
- York University ($35k)
- Toronto Metropolitan University ($33k)
- OCAD University ($27k)

<<<<<<< HEAD
Vancouver:
=======
**Vancouver**
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485
- UBC ($51k)
- Simon Fraser University ($32k)
- Emily Carr University ($24k)

<<<<<<< HEAD
Montreal:
=======
**Montreal**
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485
- McGill University ($48k)
- Concordia University ($29k)
- Université de Montréal ($27k)

<<<<<<< HEAD
Ottawa:
=======
**Ottawa**
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485
- University of Ottawa ($45k)
- Carleton University ($33k)
- Algonquin College ($16k)

<<<<<<< HEAD
Calgary:
=======
**Calgary**
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485
- University of Calgary ($32k)
- Mount Royal University ($21k)
- SAIT Polytechnic ($18k)

<<<<<<< HEAD
Edmonton:
=======
**Edmonton**
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485
- University of Alberta ($31k)
- MacEwan University ($20k)
- NAIT ($17k)

<<<<<<< HEAD
Waterloo:
=======
**Waterloo**
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485
- University of Waterloo ($53k)
- Wilfrid Laurier University ($28k)
- Conestoga College ($16k)

<<<<<<< HEAD
Other cities include Guelph, Quebec City, Winnipeg, Halifax, and more.

Custom university option available.
=======
Other supported cities include **Guelph, Quebec City, Winnipeg, Halifax**, and more.

*Custom university option available.*

---
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485

### 📈 Visual Analytics

- Monthly expense breakdown (pie charts)
- Annual cost distribution (bar charts)
- Multi-period expense visualization
<<<<<<< HEAD

### 💾 Export Options
- CSV budget reports
- Timestamped exports
- Shareable with family and advisors
=======

---

### 💾 Export Options

- CSV budget reports
- Timestamped exports
- Easy sharing with family and advisors
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485

---

## 🚀 How to Run

<<<<<<< HEAD
Web App (Streamlit):
1. Install dependencies: pip install streamlit matplotlib pandas requests
2. Run the app: streamlit run app.py
3. Open http://localhost:8501

CLI Version:
1. Install dependencies: pip install matplotlib pandas requests
2. Run the script: python cost_estimator.py
=======
### Web App (Streamlit)

1. Install dependencies  
   `pip install streamlit matplotlib pandas requests`
2. Run the app  
   `streamlit run app.py`
3. Open  
   `http://localhost:8501`

### CLI Version

1. Install dependencies  
   `pip install matplotlib pandas requests`
2. Run the script  
   `python cost_estimator.py`
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485

---

## 📦 Installation

<<<<<<< HEAD
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
=======
1. Clone the repository  
   `git clone https://github.com/aarishna/International-Student-Budget-Calculator.git`
2. Navigate to the directory  
   `cd canada-student-cost-estimator`
3. Install requirements  
   `pip install -r requirements.txt`
4. Run the app  
   `streamlit run app.py`

**Requirements**
- streamlit ≥ 1.28.0
- matplotlib ≥ 3.7.0
- pandas ≥ 2.0.0
- requests ≥ 2.30.0
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485

---

## 🏙️ Supported Cities & Universities

<<<<<<< HEAD
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
=======
- **Toronto:** $2,500–$3,000
- **Vancouver:** $2,400–$2,900
- **Montreal:** $2,100–$2,600
- **Ottawa:** $2,200–$2,700
- **Calgary:** $2,300–$2,800
- **Edmonton:** $2,200–$2,700
- **Waterloo:** $2,200–$2,700
- **Guelph:** $2,100–$2,600
- **Quebec City:** $1,900–$2,400
- **Winnipeg:** $2,000–$2,500
- **Halifax:** $2,100–$2,600

*Estimates include rent, groceries, utilities, and transportation.*
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485

---

## 🛠️ Technical Details

<<<<<<< HEAD
Built with:
=======
**Built with**
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485
- Python 3.8+
- Streamlit
- Pandas
- Matplotlib
- Amazon S3 (cloud data source)

<<<<<<< HEAD
Design highlights:
- No hardcoded datasets
- Cloud-driven configuration
- Modular and DRY architecture
=======
**Design Highlights**
- No hardcoded datasets
- Cloud-driven configuration
- Modular, DRY architecture
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485
- Graceful error handling
- Resume-grade project structure

---

## 🎓 For Students

This tool helps you:
<<<<<<< HEAD
- Budget realistically before arriving in Canada
- Avoid financial surprises
- Compare cities and programs confidently
- Prepare financial documentation for visa applications

All values are estimates and may vary.
=======

- Budget realistically before arriving in Canada
- Avoid financial surprises
- Compare cities and programs confidently
- Prepare financial documentation for visa applications

*All values are estimates and may vary.*
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 👤 Author

<<<<<<< HEAD
Aarish Naiyer  
=======
**Aarish Naiyer**  
>>>>>>> bd36959fd6072e8a60cfcfc48dfc8e8cfb6f0485
GitHub: https://github.com/aarishna  
LinkedIn: https://linkedin.com/in/aarishna  

---

## ⚠️ Disclaimer

This tool provides estimates only. Actual costs vary based on lifestyle, inflation, and university-specific fees. Always verify with official sources.

---

Made with ❤️ for international students coming to Canada
