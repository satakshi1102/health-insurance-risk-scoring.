import csv
import random

def generate_health_data(filename="health_portfolio.csv", num_records=2000):
    conditions = ["None", "Hypertension", "Diabetes", "Asthma", "Heart Condition"]
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write clean column headers
        writer.writerow(["MemberID", "Age", "BMI", "IsSmoker", "Condition", "PastClaims"])
        
        for i in range(1, num_records + 1):
            member_id = f"MEM-{i:04d}"
            age = random.randint(18, 75)
            bmi = random.randint(18, 40)
            is_smoker = random.choice([0, 1])  # 0 for No, 1 for Yes
            condition = random.choice(conditions)
            
            # Keep the past claims calculation simple and flat
            past_claims = 1000 + (age * 50) + (is_smoker * 2000)
            
            writer.writerow([member_id, age, bmi, is_smoker, condition, past_claims])
            
    print(f"✅ Created file '{filename}' with {num_records} members.")

if __name__ == "__main__":
    generate_health_data()