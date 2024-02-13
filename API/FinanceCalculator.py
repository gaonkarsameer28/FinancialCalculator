# FIRE Calculator

# Define a function to calculate time to retire
def calculate_time_to_retire():
    current_age = int(input("Current Age: "))
    retirement_age = int(input("Desired Retirement Age: "))
    tax_bracket = float(input("Tax Bracket (%): "))

    # Your calculation logic goes here
    # ...

    # Display the result
    print("Time to retire:", retirement_age - current_age, "years")

# Main function
def main():
    print("Welcome to the FIRE Calculator!")
    calculate_time_to_retire()

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
