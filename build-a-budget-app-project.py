class Category:
    def __init__(self, name):
        """
        Initialize the category with a name and an empty ledger.
        """
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """
        Add a deposit to the ledger.
        """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """
        Add a withdrawal to the ledger if there are enough funds.
        The amount should be stored as a negative number.
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """
        Return the current balance based on the deposits and withdrawals.
        """
        total_balance = sum(item["amount"] for item in self.ledger)
        return total_balance

    def transfer(self, amount, category):
        """
        Transfer an amount from this category to another category.
        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """
        Check if the current balance is enough to cover the given amount.
        """
        return self.get_balance() >= amount

    def __str__(self):
        """
        Return the string representation of the category, including the ledger entries.
        """
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:23}" + f"{item['amount']:>7.2f}" + "\n"
            total += item['amount']
        output = title + items + "Total: " + f"{total:.2f}"
        return output


def create_spend_chart(categories):
    """
    Create a bar chart showing the percentage spent in each category.
    """
    title = "Percentage spent by category\n"
    
    # Calculate the total withdrawals per category
    total_spent = 0
    category_spent = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += -item["amount"]
        category_spent.append(spent)
        total_spent += spent
    
    # Calculate the percentage spent in each category
    percentages = [(spent / total_spent) * 100 for spent in category_spent]
    
    # Construct the chart
    chart = ""
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    
    # Bottom line of the chart
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"
    
    # Category names written vertically
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        chart += "\n"
    
    return title + chart.rstrip("\n")


# Usage Example

if __name__ == "__main__":
    # Create budget categories
    food = Category("Food")
    clothing = Category("Clothing")
    entertainment = Category("Entertainment")

    # Deposit and withdraw in food category
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food")

    # Transfer from food to clothing
    food.transfer(50, clothing)

    # Deposit and withdraw in clothing category
    clothing.deposit(100, "clothing deposit")
    clothing.withdraw(25.55, "shoes")

    # Print category details
    print(food)
    print(clothing)

    # Create and print the spend chart
    print(create_spend_chart([food, clothing, entertainment]))
