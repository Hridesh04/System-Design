class Chef():
    def cook_pasta(self):
        print("The chef makes pasta")

    def cook_pizza(self):
        print("The chef makes pizza")


class Waiter:
    def __init__(self, chef):
        self.chef = chef

    def place_order(self, item: str):
        if item == "pasta":
            self.chef.cook_pasta()
        elif item == "pizza":
            self.chef.cook_pizza()
        else:
            print("Sorry, we don't have that item.")

# Example usage
chef = Chef()
waiter = Waiter(chef)
waiter.place_order("pasta")
waiter.place_order("pizza")
waiter.place_order("salad")
