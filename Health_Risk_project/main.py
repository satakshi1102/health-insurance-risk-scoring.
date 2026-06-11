from health_data_generator import generate_health_data
from risk_model import load_portfolio, HealthRiskScorer

def main():
    print("🚀 Running simplified Health Risk Scoring pipeline...")
    
    # 1. Create the fake database
    generate_health_data("health_portfolio.csv", num_records=2000)
    
    # 2. Load the spreadsheet rows into memory
    portfolio = load_portfolio("health_portfolio.csv")
    
    # 3. Calculate risks and group the results
    scorer = HealthRiskScorer()
    low, med, high, total_cost = scorer.evaluate_portfolio(portfolio)
    
    # 4. Display a straightforward summary printout
    print("\n📊 --- Risk Segment Breakdown ---")
    print(f"🟢 Low Risk Group  : {len(low)} members")
    print(f"🟡 Medium Risk Group: {len(med)} members")
    print(f"🔴 High Risk Group : {len(high)} members")
    
    print(f"\n💰 Total Estimated Future Claims Portfolio Liability: ${total_cost:,.2f}")
    print("\n🎯 Pipeline completed successfully!")

if __name__ == "__main__":
    main()