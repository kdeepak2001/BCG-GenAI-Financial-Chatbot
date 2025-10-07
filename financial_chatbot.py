import pandas as pd

# Load the financial data from Task 1
def load_data():
    """Load financial data from CSV file"""
    try:
        df = pd.read_csv('financial_data.csv')
        print("✅ Data loaded successfully!")
        print(f"📊 Total records: {len(df)}")
        return df
    except FileNotFoundError:
        print("❌ Error: financial_data.csv not found!")
        print("Make sure the CSV file is in the same folder as this Python file.")
        return None


def process_query(user_input, df):
    """Process user query and extract company, metric, and year"""
    user_input = user_input.lower()
    
    # Detect company
    company = None
    if 'microsoft' in user_input or 'msft' in user_input:
        company = 'Microsoft'
    elif 'tesla' in user_input or 'tsla' in user_input:
        company = 'Tesla'
    elif 'apple' in user_input or 'aapl' in user_input:
        company = 'Apple'
    
    # Detect year
    year = None
    if '2024' in user_input:
        year = 2024
    elif '2023' in user_input:
        year = 2023
    elif '2022' in user_input:
        year = 2022
    
    # Detect metric
    metric = None
    if 'revenue' in user_input or 'sales' in user_input:
        metric = 'Total Revenue'
    elif 'net income' in user_input or 'profit' in user_input:
        metric = 'Net Income'
    elif 'asset' in user_input:
        metric = 'Total Assets'
    
    return company, year, metric
def get_answer(company, year, metric, df):
    """Retrieve and format the answer from dataframe"""
    
    if company is None:
        return "❓ Please specify a company: Microsoft, Tesla, or Apple"
    
    if year is None:
        return "❓ Please specify a year: 2022, 2023, 2024, or 2025"
    
    if metric is None:
        return "❓ Please specify a metric: revenue, net income, or assets"
    
        # Map user-friendly names to actual column names
    metric_mapping = {
        'Total Revenue': 'Total_Revenue',
        'Net Income': 'NET_INCOME',
        'Total Assets': 'TOTAL_Assets '
    }
    
    column_name = metric_mapping.get(metric)
    
    # Filter data
    result = df[(df['Company'] == company) & (df['year'] == year)]
    
    if result.empty:
        return f"❌ No data found for {company} in {year}"
    
    value = result[column_name].values[0]
    
    return f"✅ {company}'s {metric} in {year}: ${value:,.0f} million"

# Main chatbot function
def chatbot():
    """Main chatbot interface"""
    print("="*60)
    print("💼 BCG FINANCIAL DATA CHATBOT")
    print("="*60)
    print("Ask me about Microsoft, Tesla, or Apple's financial data!")
    print("Example: 'What is Microsoft's revenue in 2024?'")
    print("Type 'exit' to quit\n")
    
    # Load data
    df = load_data()
    if df is None:
        return
    
    print("\n" + "="*60)
    
    # Chat loop
    while True:
        user_input = input("\n🤔 Your question: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("\n👋 Thanks for using BCG Financial Chatbot! Goodbye!")
            break
        
        # Process and answer
        company, year, metric = process_query(user_input, df)
        answer = get_answer(company, year, metric, df)
        print(f"\n🤖 Answer: {answer}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()

