prices = [29.99, 45.50, 12.75, 38.20]
discount_factors = [0.10, 0.20, 0.15, 0.05]
for idx in range(len(prices)):
    prices[idx] -= prices[idx] * discount_factors[idx]
    print(f"Updated price for item {idx}: ${prices[idx] * 1:.2f}")