import random
import csv
from datetime import datetime, timedelta

def generate_claims_data(filename="raw_claims.csv", num_claims=1000):
    start_date = datetime(2021, 1, 1)
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Header row
        writer.writerow(["ClaimID", "AccidentYear", "DevelopmentYear", "ClaimAmount"])
        
        for claim_id in range(1, num_claims + 1):
            # Randomly assign an accident year between 2021 and 2024
            acc_year = random.randint(2021, 2024)
            
            # Development year cannot be before the accident year
            dev_year = random.randint(acc_year, 2025)
            
            # Simulate claim amounts (log-normal distribution lookalike)
            base_amount = random.randint(500, 5000)
            inflation_factor = 1.05 ** (acc_year - 2021)
            claim_amount = round(base_amount * inflation_factor, 2)
            
            writer.writerow([f"CLM{claim_id:04d}", acc_year, dev_year, claim_amount])
            
    print(f"✅ Successfully generated {num_claims} mock insurance claims in '{filename}'")

if __name__ == "__main__":
    generate_claims_data()