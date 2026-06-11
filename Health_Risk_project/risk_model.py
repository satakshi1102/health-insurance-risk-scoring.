import csv

def load_portfolio(filename):
    records = []
    with open(filename, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append({
                "MemberID": row["MemberID"],
                "Age": int(row["Age"]),
                "BMI": int(row["BMI"]),
                "IsSmoker": int(row["IsSmoker"]),
                "Condition": row["Condition"],
                "PastClaims": float(row["PastClaims"])
            })
    return records

class HealthRiskScorer:
    def calculate_score(self, member):
        # Start everyone at a base score of 0 points
        score = 0
        
        # Add simple, flat points for higher risk traits
        if member["Age"] > 50:
            score += 30
            
        if member["BMI"] > 30:
            score += 20
            
        if member["IsSmoker"] == 1:
            score += 30
            
        if member["Condition"] != "None":
            score += 20
            
        return score

    def evaluate_portfolio(self, portfolio):
        # Create empty groups to categorize our members
        low_risk = []
        med_risk = []
        high_risk = []
        
        total_predicted_cost = 0.0
        
        for member in portfolio:
            score = self.calculate_score(member)
            member["RiskScore"] = score
            
            # Simple Prediction: Future claims = past claims + a percentage based on their risk score
            member["FutureClaimEstimate"] = member["PastClaims"] * (1 + (score / 100))
            total_predicted_cost += member["FutureClaimEstimate"]
            
            # Assign to folders based on their total point scores
            if score <= 20:
                low_risk.append(member)
            elif score <= 50:
                med_risk.append(member)
            else:
                high_risk.append(member)
                
        return low_risk, med_risk, high_risk, total_predicted_cost