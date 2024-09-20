# **Sales Analysis and Optimization Project**

### **Overview**
This project focuses on the analysis and optimization of sales across multiple retail stores. Using data-driven techniques, we identified key factors that impact sales performance, developed actionable insights, and provided solutions to enhance sales and improve store performance. The project includes data cleaning, exploratory data analysis (EDA), machine learning model building, and actionable insights based on data analysis.

### **Data-Driven Insights and Solutions**
You can find the detailed insights and data-driven solutions [here](documents/Data_driven_solution/Insights.md).

---

### **Project Structure**

The repository is organized into the following directories:

sales-optimization-project/
│
├── data/                           # Data storage
│   ├── raw/                        # Raw, unprocessed data
│   └── processed/                  # Cleaned and processed data
│
├── documents/                      # Documentation and reports
│   ├── Dashboard/                  # Dashboard files for insights visualization
│   └── Data_driven_solution/       # Insights and recommendations
│       └── Insights.md             # Markdown file containing insights and solutions
│
├── notebooks/                      # Jupyter notebooks for analysis
│   └── EDA.ipynb                   # Exploratory Data Analysis and statistical analysis
│
├── scripts/                        # Python scripts for data processing and modeling
│   ├── data_cleaning.py            # Data cleaning and preprocessing functions
│   ├── model_building.py           # Model training and evaluation functions
│   └── explainability.py           # LIME-based model explainability
│
├── README.md                       # Project description and instructions
├── requirements.txt                # Required Python libraries
└── LICENSE                         # License for the project

### **Usage Instructions**

To use or reproduce this project, follow these steps:

1. **Clone the repository**:

   git clone https://github.com/HadeelAls618/Sales-Analysis-and-Optimization-Project.git
   cd Sales-Analysis-and-Optimization-Project

2. **Install Dependencies**:

To install the required Python packages using the `requirements.txt` file, run the following command:

pip install -r requirements.txt


3. **Explore the EDA and Statistical Analysis**:
   - Run the `notebooks/EDA.ipynb` notebook to explore the data and perform statistical analysis.

4. **Execute the Data Cleaning and Model Training Scripts**:
   - You can run the data cleaning and model building scripts located in the `scripts/` folder. Example:
   
   python scripts/data_cleaning.py
   python scripts/model_building.py

### **View the Dashboard**

The dashboard below visualizes key insights derived from the analysis.

![Dashboard Preview](documents/Dashboard/dashboard.png)



