def calculate_refund():
    print("\n=== Noom Partial Refund Calculator ===")
    
    original_price = float(input("Enter original price: $"))
    total_days = int(input("Total days in period: "))
    days_used = int(input("Days used: "))
    
    daily_rate = original_price / total_days
    refund = max(round(original_price - (daily_rate * days_used), 2), 0.00)  # Fixed closing parenthesis
    
    print(f"\nRefund Amount: ${refund:.2f}")
    input("\nPress Enter to return to main menu...")