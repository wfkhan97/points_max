# points_max

Purpose of this repo is to delineate the requirements for a maximization tool for credit card rewards points
-----
for the txns in the transactions.csv - please note, 002 is the platinum card and 006 is the gold card
-----
benefits_logic.py:

### Summary for the Credit Card Rewards & Benefits Tracker Module

This Python module is designed to process and analyze credit card transactions to help users maximize the value of their credit card benefits. It provides insights into the rewards earned, money saved through statement credits, and unused benefits. The module is tailored to work with American Express credit cards but can be extended to accommodate other card issuers.

---

### **Key Features**
1. **Rewards Calculation:**
   - Automatically determines the reward points or miles earned for each transaction based on the card type and transaction description.
   - Uses pre-defined earning rates for categories like flights, hotels, restaurants, and general purchases.

2. **Monthly Statement Credit Tracking:**
   - Tracks monthly statement credits (e.g., Uber Cash, Dining Credit) for each card.
   - Identifies whether the user has utilized these credits during the corresponding month.
   - Flags unused monthly credits for easy tracking.

3. **Annual Statement Credit Tracking:**
   - Monitors annual statement credits (e.g., Global Entry/TSA PreCheck Credit, Airline Fee Credit).
   - Ensures these credits are redeemed within the calendar year.
   - Highlights unused annual credits to prevent missing out on valuable benefits.

4. **"All Benefits" Section Usage Tracking:**
   - Captures and tracks the use of additional benefits listed in the "All Benefits" section of each card, such as:
     - Priority boarding for Delta cards.
     - Complimentary access to airport lounges for Platinum cards.
   - Summarizes which benefits have been utilized and which remain unused.

5. **Comprehensive Reporting:**
   - Outputs a summary of rewards earned, total credits applied, and benefits usage.
   - Flags opportunities to maximize the card’s value by identifying unused credits and benefits.

---

### **How It Works**
1. **Input:** 
   - Reads a CSV file of credit card transactions with columns for date, card type, status, description, multiplier, amount, and points/miles earned.

2. **Processing:** 
   - Categorizes transactions based on keywords in the description to identify the appropriate earning rate and applicable benefits.
   - Maintains separate tracking for monthly and annual credits, ensuring they are not double-counted across periods.

3. **Output:** 
   - Provides a detailed summary of:
     - Rewards earned.
     - Total value of statement credits utilized.
     - Unused monthly and annual credits.
     - Benefits from the "All Benefits" section that have been utilized.

4. **Customization:**
   - Includes a modular structure for adding new cards or benefits.
   - Users can define additional earning categories or benefits by modifying the `card_benefits` dictionary.

---

### **Ideal Use Cases**
- **Personal Finance Management:** Helps users monitor and optimize their credit card usage.
- **Maximizing Benefits:** Ensures that valuable credits and benefits are not overlooked.
- **Card Comparison:** Assists in evaluating the overall value of a credit card by analyzing rewards and benefits utilization.

---

### **Future Enhancements**
- Add support for additional card issuers or customizable card configurations.
- Integrate visual reporting using libraries like Matplotlib or Seaborn for trend analysis.
- Support multi-currency transactions with automatic currency conversion for international purchases.

This module is an essential tool for anyone looking to extract the maximum value from their credit card benefits.