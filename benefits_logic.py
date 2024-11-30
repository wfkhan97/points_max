import pandas as pd
import re

# Define card-specific benefits and earning rates
card_benefits = {
    'Platinum': {
        'earning_rates': {
            'flights': 5,
            'prepaid_hotels': 5,
            'default': 1
        },
        'monthly_statement_credits': {
            'Uber Cash': 15,
            'Walmart+ Credit': 12.95,
            'Digital Entertainment Credit': 20
        },
        'annual_statement_credits': {
            'Airline Fee Credit': 200,
            'Hotel Credit': 200,
            'Global Entry/TSA PreCheck Credit': 100
        },
        'all_benefits': [
            'Car Rental Privileges',
            'Fine Hotels + Resorts Program',
            'No Foreign Transaction Fees'
        ]
    },
    'Gold': {
        'earning_rates': {
            'restaurants': 4,
            'supermarkets': 4,
            'flights': 3,
            'default': 1
        },
        'monthly_statement_credits': {
            'Dining Credit': 10,
            'Uber Cash': 10
        },
        'annual_statement_credits': {},
        'all_benefits': [
            'Purchase Protection',
            'Extended Warranty',
            'Global Assist Hotline'
        ]
    },
    'Delta Reserve': {
        'earning_rates': {
            'delta': 3,
            'default': 1
        },
        'monthly_statement_credits': {},
        'annual_statement_credits': {
            'Companion Certificate': 'Value varies',
            'Global Entry/TSA PreCheck Credit': 100
        },
        'all_benefits': [
            'Priority Boarding',
            'First Checked Bag Free',
            '20% In-Flight Savings'
        ]
    }
}

# Map card numeric identifiers to card names
card_mapping = {
    '-41002': 'Platinum',
    '-91006': 'Gold',
    # Add additional mappings as necessary
    'default': 'Generic Card'
}

# Load the CSV file
df = pd.read_csv('/Users/WK/Documents/GitHub/points_max/transactions.csv')

# Map card numeric identifiers to card names
card_mapping = {
    '-41002': 'Platinum',
    '-91006': 'Gold',
    # Add additional mappings as necessary
}

# Check all unique card identifiers in the dataset
unique_cards = df['Card'].unique()
print("Unique card identifiers in the dataset:", unique_cards)

# Map and handle undefined cards
df['Card'] = df['Card'].map(card_mapping)

# Identify transactions with undefined cards
undefined_transactions = df[df['Card'].isna()]
if not undefined_transactions.empty:
    print(f"Warning: Transactions with undefined cards found: {undefined_transactions.shape[0]}")
    undefined_transactions.to_csv('undefined_transactions.csv', index=False)
    print("Saved undefined transactions to 'undefined_transactions.csv' for review.")

# Clean up and preprocess the data
df['Card'] = df['Card'].map(card_mapping)
df['Amount'] = df['Amount'].replace('[\$,]', '', regex=True).astype(float)
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')
df['Year'] = df['Date'].dt.year

# Identify undefined card identifiers
undefined_cards = df[df['Card'].isna()]['Card'].unique()
if len(undefined_cards) > 0:
    print("Undefined card identifiers:", undefined_cards)
    # Save undefined transactions for review
    undefined_transactions = df[df['Card'].isna()]
    undefined_transactions.to_csv('undefined_transactions.csv', index=False)
    print("Saved undefined transactions to 'undefined_transactions.csv' for review.")

# Initialize tracking dictionaries
monthly_credits_used = {}
annual_credits_used = {}
all_benefits_used = {}

# Process transactions
for index, row in df.iterrows():
    card = row['Card']
    description = row['Description']
    amount = row['Amount']
    month = row['Month']
    year = row['Year']

    if pd.isna(card):
        print(f"Warning: Undefined card in transaction on {row['Date']}. Skipping.")
        # Optional: Log skipped transactions for review
        with open('skipped_transactions.log', 'a') as log_file:
            log_file.write(f"Undefined card transaction: {row.to_dict()}\n")
        continue

    # Initialize tracking for this card and period
    monthly_credits_used.setdefault(card, {})
    annual_credits_used.setdefault(card, set())
    all_benefits_used.setdefault(card, set())

    # Monthly statement credits
    for benefit, credit in card_benefits[card]['monthly_statement_credits'].items():
        if benefit.lower() in description.lower():
            monthly_credits_used[card].setdefault(month, set()).add(benefit)

    # Annual statement credits
    for benefit, credit in card_benefits[card]['annual_statement_credits'].items():
        if benefit.lower() in description.lower():
            annual_credits_used[card].add(benefit)

    # "All Benefits" tracking
    for benefit in card_benefits[card]['all_benefits']:
        if benefit.lower() in description.lower():
            all_benefits_used[card].add(benefit)

# Identify unused credits and benefits
def identify_unused_credits(card, monthly_credits_used, annual_credits_used):
    unused_monthly = [
        benefit
        for benefit in card_benefits[card]['monthly_statement_credits']
        if benefit not in monthly_credits_used
    ]
    unused_annual = [
        benefit
        for benefit in card_benefits[card]['annual_statement_credits']
        if benefit not in annual_credits_used
    ]
    return unused_monthly, unused_annual

# Summarize results
for card in card_benefits:
    unused_monthly, unused_annual = identify_unused_credits(
        card, monthly_credits_used.get(card, {}), annual_credits_used.get(card, set())
    )
    print(f"Unused Monthly Credits for {card}: {unused_monthly}")
    print(f"Unused Annual Credits for {card}: {unused_annual}")
    print(f"All Benefits Used for {card}: {all_benefits_used.get(card, set())}")
