# 🍁 Canada Student Cost Estimator

A comprehensive cost-of-living calculator for international students planning to study in Canada.  
Provides detailed expense breakdowns, multi-city comparisons, and budget visualization tools using cloud-hosted data.

---

## 🎯 Purpose

This tool helps international students:

- **Estimate** total annual costs (tuition + living expenses)
- **Compare** tuition across 20+ programs and 30+ universities
- **Plan** budgets for different lifestyle choices
- **Understand** how program choice affects total cost
- **Visualize** spending patterns through interactive charts
- **Export** personalized budget reports

---

## ✨ Features

### ☁️ Dynamic Cloud Data (Amazon S3)

- University, program, and city cost data fetched dynamically from Amazon S3
- No hardcoded datasets
- Updates can be made without redeploying the application
- Centralized, scalable, production-style data storage

---

### 🎓 Program-Specific Tuition

Supports **20 major programs** with realistic international tuition multipliers:

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

Supports **30+ institutions** across Canada with international tuition data loaded dynamically.

**Toronto**
- University of Toronto ($58k)
- York University ($35k)
- Toronto Metropolitan University ($33k)
- OCAD University ($27k)

**Vancouver**
- UBC ($51k)
- Simon Fraser University ($32k)
- Emily Carr University ($24k)

**Montreal**
- McGill University ($48k)
- Concordia University ($29k)
- Université de Montréal ($27k)

**Ottawa**
- University of Ottawa ($45k)
- Carleton University ($33k)
- Algonquin College ($16k)

**Calgary**
- University of Calgary ($32k)
- Mount Royal University ($21k)
- SAIT Polytechnic ($18k)

**Edmonton**
- University of Alberta ($31k)
- MacEwan University ($20k)
- NAIT ($17k)

**Waterloo**
- University of Waterloo ($53k)
- Wilfrid Laurier University ($28k)
- Conestoga College ($16k)

Other supported cities include **Guelph, Quebec City, Winnipeg, Halifax**, and more.

*Custom university option available.*

---

### 📈 Visual Analytics

- Monthly expense breakdown (pie charts)
- Annual cost distribution (bar charts)
- Multi-period expense visualization

---

### 💾 Export Options

- CSV budget reports
- Timestamped exports
- Easy sharing with family and advisors

---

## 🚀 How to Run

### Web App (Streamlit)

```bash
pip install streamlit matplotlib pandas requests
streamlit run app.py
