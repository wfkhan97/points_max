import pandas as pd

# Define card-specific earning rates and statement credits
card_benefits = {
    'Platinum': {
        'earning_rates': {
            'flights': 5,
            'prepaid_hotels': 5,
            'default': 1
        },
        'statement_credits': {
            'Airline Fee Credit': 200,
            'Hotel Credit': 200,
            'Digital Entertainment Credit': 240,
            'Walmart+ Credit': 155,
            'Uber Cash': 200
        }
    },
    'Gold': {
        'earning_rates': {
            'restaurants': 4,
            'supermarkets': 4,
            'flights': 3,
            'default': 1
        },
        'statement_credits': {
            'Dining Credit': 120,
            'Uber Cash': 120
        }
    },
    'Delta Reserve': {
        'earning_rates': {
            'delta': 3,
            'default': 1
        },
        'statement_credits': {
            'Companion Certificate': 'Value varies',
            'Global Entry/TSA PreCheck Credit': 100
        }
    }
}

# Function to determine the earning rate based on description
def get_earning_rate(card, description):
    description = description.lower()
    rates = card_benefits[card]['earning_rates']
    if 'flight' in description or 'airline' in description:
        return rates.get('flights', rates['default'])
    elif 'hotel' in description:
        return rates.get('prepaid_hotels', rates['default'])
    elif 'restaurant' in description or 'dining' in description:
        return rates.get('restaurants', rates['default'])
    elif 'supermarket' in description or 'grocery' in description:
        return rates.get('supermarkets', rates['default'])
    elif 'delta' in description:
        return rates.get('delta', rates['default'])
    else:
        return rates['default']

# Read the CSV file
df = pd.read_csv('transactions.csv')

# Initialize totals
total_rewards = 0
total_credits = 0

# Process each transaction
for index, row in df.iterrows():
    card = row['Card']
    description = row['Description']
    amount = row['Amount']
    
    # Determine earning rate
    earning_rate = get_earning_rate(card, description)
    
    # Calculate rewards earned
    rewards_earned = amount * earning_rate
    total_rewards += rewards_earned
    
    # Check for applicable statement credits
    credits = card_benefits[card]['statement_credits']
    for credit, value in credits.items():
        if credit.lower() in description.lower():
            if isinstance(value, (int, float)):
                total_credits += min(amount, value)
            else:
                print(f"Statement credit '{credit}' has a variable value.")

# Output the results
print(f"Total Rewards Earned: {total_rewards} points/miles")
print(f"Total Statement Credits Applied: ${total_credits}")
