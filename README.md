🍁 Canada Student Cost Estimator

A comprehensive cost-of-living calculator for international students planning to study in Canada. Provides detailed expense breakdowns, multi-city comparisons, and budget visualization tools using cloud-hosted data.

🎯 Purpose

Helps international students:

Estimate total annual costs (tuition + living expenses)

Compare tuition across 20+ programs and 30+ universities

Plan budgets for different lifestyle choices

Understand how program choice affects total cost

Visualize spending patterns through interactive charts

Export personalized budget reports

✨ Features
☁️ Dynamic Cloud Data (Amazon S3)

University, program, and city cost data is fetched dynamically from Amazon S3

Replaces previously hardcoded datasets

Enables easy updates without modifying application code

Centralized and scalable data management

🎓 Program-Specific Tuition

20 major programs with realistic tuition adjustments:

STEM: Engineering (1.4x), Computer Science (1.35x), Sciences (1.1x)

Health: Medicine (2.0x), Dentistry (1.8x), Nursing (1.2x)

Professional: Law (1.5x), Business (1.25x), Architecture (1.3x)

Liberal Arts: Arts/Humanities (0.95x), Social Sciences (0.95x), Education (0.9x)

Creative: Fine Arts (1.0x), Communications (1.0x)

Trades: Culinary Arts (0.85x), Hospitality (0.85x)

Multipliers based on typical international student tuition variations

📊 Comprehensive Expense Tracking

Housing: Rent, utilities, internet

Transportation: Public transit costs (or free university passes)

Food: Groceries + dining out

Lifestyle: Entertainment, social activities, shopping

Summer Planning: Options to stay, relocate, or go home

🎓 University Database

30+ institutions across Canada with international student tuition data loaded dynamically from cloud storage:

Toronto (4):

University of Toronto ($58k)

York University ($35k)

Toronto Metropolitan University ($33k)

OCAD University ($27k)

Vancouver (3):

UBC ($51k)

Simon Fraser University ($32k)

Emily Carr University ($24k)

Montreal (3):

McGill University ($48k)

Concordia University ($29k)

Université de Montréal ($27k)

Ottawa (3):

University of Ottawa ($45k)

Carleton University ($33k)

Algonquin College ($16k)

Calgary (3):

University of Calgary ($32k)

Mount Royal University ($21k)

SAIT Polytechnic ($18k)

Edmonton (3):

University of Alberta ($31k)

MacEwan University ($20k)

NAIT ($17k)

Waterloo (3):

University of Waterloo ($53k)

Wilfrid Laurier University ($28k)

Conestoga College ($16k)

Other Cities:

University of Guelph ($31k)

Université Laval – Quebec City ($26k)

University of Manitoba ($19k)

Dalhousie University ($28k)

Plus additional institutions

Custom university option available for any institution

📈 Visual Analytics

Monthly expense breakdown (pie charts)

Annual cost distribution (bar charts)

Multi-city comparison charts

💾 Export Options

CSV reports with detailed breakdowns

Timestamped for record-keeping

Easy to share with family and advisors

🚀 How to Run
Option 1: Web App (Streamlit) – Recommended
pip install streamlit matplotlib pandas requests
streamlit run app.py


Then open http://localhost:8501

Option 2: Command-Line Interface (CLI)
pip install matplotlib pandas requests
python cost_estimator.py

📦 Installation
git clone https://github.com/aarishna/International-Student-Budget-Calculator.git
cd canada-student-cost-estimator
pip install -r requirements.txt
streamlit run app.py


requirements.txt:

streamlit>=1.28.0
matplotlib>=3.7.0
pandas>=2.0.0
requests>=2.30.0

🏙️ Supported Cities & Universities
City	Universities	Avg Monthly Cost*
Toronto	U of T, York, TMU, OCAD	$2,500 - $3,000
Vancouver	UBC, SFU, Emily Carr	$2,400 - $2,900
Montreal	McGill, Concordia, UdeM	$2,100 - $2,600
Ottawa	U Ottawa, Carleton, Algonquin	$2,200 - $2,700
Calgary	U Calgary, MRU, SAIT	$2,300 - $2,800
Edmonton	U Alberta, MacEwan, NAIT	$2,200 - $2,700
Waterloo	UWaterloo, Laurier, Conestoga	$2,200 - $2,700
Guelph	U Guelph	$2,100 - $2,600
Quebec City	Laval, Mérici	$1,900 - $2,400
Winnipeg	U Manitoba, U Winnipeg, RRC	$2,000 - $2,500
Halifax	Dalhousie, SMU, NSCAD	$2,100 - $2,600

*Estimates include rent, groceries, utilities, and transportation

Each city includes localized data for groceries, utilities, transportation, and internet costs.

🛠️ Technical Details

Built with:

Python 3.8+

Streamlit (web framework)

Matplotlib (visualizations)

Pandas (data handling)

Amazon S3 (cloud data storage)

Code Quality:

DRY principles (no repeated logic)

Type hints for readability

Comprehensive input validation

Graceful error handling

Cloud-driven, non-hardcoded architecture

📝 Usage Example
Streamlit App

Select your university (city and tuition auto-filled)

Choose your program/major (tuition adjusted dynamically)

Enter housing and lifestyle expenses

Select summer plans

View real-time calculations and charts

Download CSV report

CLI Version
$ python cost_estimator.py
...
TOTAL                        $102,114.00

🎓 For Students

This tool is designed to help you:

Budget realistically before arriving in Canada

Avoid financial surprises during your first year

Make informed decisions about city and lifestyle choices

Present financial proof for visa applications

Note: All costs are estimates based on recent public data.

🤝 Contributing

Contributions welcome!

Fork the repository

Create a feature branch

Commit your changes

Push to your branch

Open a Pull Request

👤 Author

Aarish Naiyer
GitHub
 | LinkedIn

Built to help international students navigate financial planning for studying in Canada 🍁

⚠️ Disclaimer

This tool provides estimates only. Actual costs vary based on lifestyle, inflation, and university-specific fees. Always verify costs with official sources.

Made with ❤️ for international students coming to Canada
