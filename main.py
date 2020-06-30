# -*- coding: utf-8 -*-
"""
Created on Wed June 26 07:10:08 2020
Project : Rackspace
@author: Akash Gupta

This code is responsible for
creating the bill for the user cart
after applying the discount
"""

SPACES = 19
PRE_PROMO_SPACES = 6
POST_PROMO_SPACES = 11
HEADER_SPACES = 18


class ClsCheckOut:
    """
    This is a checkout class
    """
    PRODUCT_DICT = {
        'CH1': 3.11,
        'AP1': 6.00,
        'CF1': 11.23,
        'MK1': 4.75,
        'OM1': 3.69
    }

    APPL_DISCOUNT = -1.50
    APOM_DISCOUNT = -0.5 * PRODUCT_DICT['AP1']
    CHMK_DISCOUNT = -1 * PRODUCT_DICT['MK1']

    def __init__(self):
        self.total = 0.00

        self.promo_status = dict({
            'BOGO': False,
            'APPL': False,
            'CHMK': False,
            'APOM': False
        })

        self.product_mapping = {
            'CH1': self.product_chai,
            'AP1': self.product_apple,
            'CF1': self.product_coffee,
            'MK1': self.product_milk,
            'OM1': self.product_oatmeal
        }
        print("Item" + " " * HEADER_SPACES + 'Price')
        print("----" + " " * HEADER_SPACES + '-----')

    def check_promo(self, cart: dict):
        """
        This function updated the kind of promo applicable to the cart
        :param cart: (dict) of items with frequency
        :return: None (updated the class variable promo_status)
        """

        if cart.get('AP1', 0) >= 3:
            self.promo_status['APPL'] = True

        if cart.get('CH1', None) and cart.get('MK1', None):
            self.promo_status['CHMK'] = True

        if cart.get('OM1', None) and cart.get('AP1', None):
            self.promo_status['APOM'] = True

    def product_chai(self):
        """
        Calculates the price of the chai product and
        any promo applicable to it
        :return: None (updates the total of the cart)
        """
        price = ClsCheckOut.PRODUCT_DICT['CH1']

        print("CH1"
              + " " * SPACES
              + str(price))

        self.total += price

    def product_apple(self):
        """
        Calculates the price of the apple product and
        any promo applicable to it
        :return: None (updates the total of the cart)
        """
        price = ClsCheckOut.PRODUCT_DICT['AP1']

        print("AP1"
              + " " * SPACES
              + str(price))
        self.total += price

        if self.promo_status['APPL']:
            print(" " * PRE_PROMO_SPACES
                  + "APPL"
                  + " " * POST_PROMO_SPACES
                  + str(ClsCheckOut.APPL_DISCOUNT))

            self.total += ClsCheckOut.APPL_DISCOUNT

        if self.promo_status['APOM']:
            print(" " * PRE_PROMO_SPACES
                  + "APOM"
                  + " " * POST_PROMO_SPACES
                  + str(ClsCheckOut.APOM_DISCOUNT))

            self.total += ClsCheckOut.APOM_DISCOUNT

    def product_coffee(self):
        """
        Calculates the price of the coffee product and
        any promo applicable to it
        :return: None (updates the total of the cart)
        """
        price = ClsCheckOut.PRODUCT_DICT['CF1']

        print("CF1"
              + " " * SPACES
              + str(price))

        self.total += price

        if self.promo_status['BOGO']:
            print(" " * PRE_PROMO_SPACES
                  + "BOGO"
                  + " " * POST_PROMO_SPACES
                  + str(-1 * price))

            self.promo_status['BOGO'] = False
            self.total += price * -1
        else:
            self.promo_status['BOGO'] = True

    def product_milk(self):
        """
        Calculates the price of the milk product and
        any promo applicable to it
        :return: None (updates the total of the cart)
        """
        price = ClsCheckOut.PRODUCT_DICT['MK1']

        print("MK1"
              + " " * SPACES
              + str(price))

        self.total += price

        if self.promo_status['CHMK']:
            print(" " * PRE_PROMO_SPACES
                  + "CHMK"
                  + " " * POST_PROMO_SPACES
                  + str(ClsCheckOut.CHMK_DISCOUNT))

            self.promo_status['CHMK'] = False
            self.total += ClsCheckOut.CHMK_DISCOUNT

    def product_oatmeal(self):
        """
        Calculates the price of the oatmeal product and
        any promo applicable to it
        :return: None (updates the total of the cart)
        """
        price = ClsCheckOut.PRODUCT_DICT['OM1']

        print("OM1"
              + " " * SPACES
              + str(price))

        self.total += price

    def product_unknown(self):
        """
        This function basically reject all the
        unknown cart values and does not raise exception
        :return: None
        """

    def calculate(self, items: list) -> float:
        """
        This function call all the product calculation function
        and dislays the final total to the user
        :param items: (list) represents the cart items in the order of addition
        :return:  total value of the cart after applying all the promos
        """
        cart = self.count_frequency(items)

        self.check_promo(cart)

        for item in items:
            self.product_mapping.get(item, self.product_unknown)()
        print("--------------------------")
        print("                      " + str(round(self.total, 2)))

        return self.total

    @staticmethod
    def count_frequency(items: list) -> dict:
        """
        This method creates a dict for the frequency of the items
        :param items: (list) represents the cart items in the order of addition
        :return:  (dict) frequency of each type of item purchased
        """
        # Creating an empty dictionary
        freq = {}

        for item in items:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1

        return freq


def main():
    """
    Reading inputs via file from the user
    and running the code.
    Each line consists of a test case.
    :return: None
    """
    file1 = open('input.txt', 'r')
    lines = file1.readlines()
    for index, line in enumerate(lines):
        cart = [str(piece).strip() for piece in line.split(',')]
        print("\n")
        print("Test Case: " + str(index+1))
        print("Input: {0}".format(cart))
        print("--------------------------")
        print("\n")
        ClsCheckOut().calculate(cart)
        print("\n")


if __name__ == '__main__':
    # ClsCheckOut().calculate(['CH1', 'CF1', 'AP1', 'AP1', 'MK1', 'MK1', 'OM1', 'CF1', 'CF1'])
    main()
