#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.items = []
    self.prices = []
    self.total = 0

  def add_item(self, title, price, quantity=1):
    self.title = title
    self.price = price
    self.quantity = quantity
    self.total += price * quantity
    self.items.extend([title]*quantity)
    self.prices.extend([price]*quantity)

  def apply_discount(self):
    if self.discount > 0:
      self.total = int(self.total - (self.total * (self.discount/100)))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    if self.items and self.quantity >= 1:
      last_price = self.prices.pop()
      self.total = self.total - (last_price * self.quantity)
      last_item = self.items.pop()
    else:
      self.total = 0.0