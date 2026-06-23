from order import Order


class Waiter:
    def take_order(self, order: Order):
        print(f"Waiter takes the order: {order}")
        order.execute()

        