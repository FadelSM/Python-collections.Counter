from collections import Counter

def solve():
    # Read number of shoes (though not strictly needed for the logic)
    num_shoes = int(input())
    
    # Read shoe sizes and create the inventory counter
    shoe_sizes = list(map(int, input().split()))
    inventory = Counter(shoe_sizes)
    
    # Read number of customers
    num_customers = int(input())
    
    total_earned = 0
    
    for _ in range(num_customers):
        # Read desired size and offered price
        size, price = map(int, input().split())
        
        # Check if the size is in stock
        if inventory[size] > 0:
            total_earned += price
            # Reduce the count for that size by 1
            inventory[size] -= 1
            
    print(total_earned)

if __name__ == "__main__":
    solve()
