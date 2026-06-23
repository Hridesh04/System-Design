from chef import Chef
from pizza_order import PizzaOrder
from burger_order import BurgerOrder
from waiter import Waiter

chef = Chef()
burger_order = BurgerOrder(chef)
pizza_order = PizzaOrder(chef)

waiter = Waiter()
waiter.take_order(burger_order)
waiter.take_order(pizza_order)