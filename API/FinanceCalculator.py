# FIRE Calculator
def calculate_loan_amortization(principal, rate, loan_term, monthly_emi):
    # Convert annual interest rate to monthly rate
    r = rate / 100 / 12
    n = loan_term * 12  # Total number of payments

    # Initialize debt balance
    debt_balance = principal

    # Create a list to store yearly debt balances
    yearly_debt_balances = []

    for year in range(1, loan_term + 1):
        interest_paid = debt_balance * r
        principal_paid = monthly_emi - interest_paid
        debt_balance -= principal_paid
        yearly_debt_balances.append((year, debt_balance))

    return yearly_debt_balances

# Example usage:
loan_principal = 100000  # Example loan amount
annual_interest_rate = 5  # Example annual interest rate (in percentage)
loan_term_years = 20  # Example loan term in years
monthly_emi = 6000  # Example monthly EMI

result = calculate_loan_amortization(loan_principal, annual_interest_rate, loan_term_years, monthly_emi)
for year, balance in result:
    print(f"Year {year}: Debt balance = ${balance:.2f}")

def calculate_investment_growth(initial_amount, monthly_emi, investment_rate, investment_term):
    r = investment_rate / 100 / 12
    n = investment_term * 12

    # Calculate future value using compound interest formula
    future_value = initial_amount * (1 + r) ** n + monthly_emi * (((1 + r) ** n - 1) / r)

    return future_value

# Example usage:
initial_investment = 5000  # Example initial investment amount
monthly_contribution = 200  # Example monthly contribution
annual_investment_rate = 7  # Example annual investment rate (in percentage)
investment_term_years = 10  # Example investment term in years

investment_value = calculate_investment_growth(initial_investment, monthly_contribution,
                                               annual_investment_rate, investment_term_years)
print(f"Total investment value after {investment_term_years} years: ${investment_value:.2f}")


# Define a function to calculate time to retire
# def calculate_time_to_retire():
  #  current_age = int(input("Current Age: "))
   # retirement_age = int(input("Desired Retirement Age: "))
   # tax_bracket = float(input("Tax Bracket (%): "))

    # Your calculation logic goes here
    # ...

    # Display the result
    # print("Time to retire:", retirement_age - current_age, "years")

# Main function
def main():
    print("Welcome to the FIRE Calculator!")
   # calculate_time_to_retire()

if __name__ == "__main__":
    main()

# Debt table
loan_table = [
    {"Loan Type": input("Loan Type: "),
     "Monthly EMI": float(input("Monthly EMI: ")),
     "Loan Length (in years)": int(input("Loan Length (in years): ")),
     "Pending Loan Amount": float(input("Pending Loan Amount: "))},
]

# Investment table
investment_table = [
    {"Investment Type": input("Investment Type: "),
     "Monthly EMI": float(input("Monthly EMI: ")),
     "Period (in years)": int(input("Period (in years): ")),
     "Initial Amount": float(input("Initial Amount: "))},
]

# Add more rows to the tables as needed
# ...

# Note: Replace the input prompts with your actual logic for calculations.
