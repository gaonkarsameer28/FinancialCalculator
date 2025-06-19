def calculate_loan_amortization(principal, rate, loan_term, monthly_emi):
    # Convert annual interest rate to monthly rate
    r = rate / 100 / 12
    n = loan_term * 12  # Total number of payments

    # Initialize debt balance
    debt_balance = principal

    # Create lists to store yearly details
    yearly_debt_balances = []
    yearly_principal_paid = []
    yearly_interest_paid = []

    for year in range(1, loan_term + 1):
        interest_paid = debt_balance * r
        principal_paid = monthly_emi - interest_paid
        debt_balance -= principal_paid

        # Stop calculation when debt becomes zero
        if debt_balance <= 0:
            # Adjust last EMI
            monthly_emi = debt_balance + interest_paid
            debt_balance = 0

        yearly_debt_balances.append((year, debt_balance))
        yearly_principal_paid.append(principal_paid)
        yearly_interest_paid.append(interest_paid)

    return yearly_debt_balances, yearly_principal_paid, yearly_interest_paid

# Example usage:
loan_principal = 100000  # Example loan amount
annual_interest_rate = 5  # Example annual interest rate (in percentage)
loan_term_years = 20  # Example loan term in years
monthly_emi = 500  # Example monthly EMI

debt_balances, principal_paid, interest_paid = calculate_loan_amortization(
    loan_principal, annual_interest_rate, loan_term_years, monthly_emi
)
    
print("Year | Debt Balance | Principal Paid | Interest Paid")
print("-" * 45)
for year, balance, principal, interest in zip(range(1, loan_term_years + 1), debt_balances, principal_paid, interest_paid):
   print(f"{year:2f} | ${balance:.2f} | ${principal:.2f} | ${interest:.2f}")
