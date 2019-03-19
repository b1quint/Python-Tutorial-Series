#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python Tutorial Series 2019 - Basics 2: Code Flow

This file holds a simple example of the basic Python code flow syntax. It
includes:

    - A method
    - A class
    - A sub-class
    - A if/elif/else case
    - A for loop

Exercise:

1) Find all the Syntax Errors before running

2) Debug why the cat is not eating the Meat

3) Create a new class called Dog and write how it behaves depending on the food
   it eats.

   3.1) Create an empty class
   3.2) Add the docstring explaining how it will behave
   3.3) Implement the actual code in a way it behaves as you explained

4) (Challenge) Add a "while" loop that will stop when all the pets are not
   hungry anymore.
"""


class Pet:
    """
    Pets usually have a name and eat a lot. So let us represent our pet by
    its name and its "is_hungry" state.

    Parameters
    ----------
    new_name : str
        A new name for our new pet.

    Attributes
    ----------
    name : str
        The pet's name
    is_hungry : bool
        Is our pet hungry?
    """
    def __init__(self, new_name):
        self.name = new_name
        self.is_hungry = True

    def eat(self, food_name):
        """
        Give some food to our pet. After this, it is not hungry anymore.

        Parameters
        ----------
        food_name : str
            The name of the food you will give to our pet.
        """
        print(' {} eats anything and is happy to eat {}!!'.format(
            self.name, food_name))
        self.is_hungry = False


class Cat(Pet):
    """
    New class that inherits the Pet attributes. The only difference is
    its behaviour when it eats.
    """
    def eat(self, food_name):
        """
        Overrides Pet.eat() method. You know, cats **love** fish and meat. They
        also like milk but will still hungry after drinking it.

        Parameters
        ----------
        food_name : str
            The name of the food you will give to our pet.
        """

        if food_name in ['fish', 'meat']:
            print(' {} just loved the {}'.format(self.name, food_name))
            self.is_hungry = False

        elif food_name in ['milk']:
            print(' {} liked the {} but still hungry...'.format(
                self.name, food_name)

        else:
            print(' {} does not like {}...'.format(self.name, food_name))


def give_food_to_pet(my_pet, food):
    """
    Give some food to my pet.

    Parameters
    ----------
    my_pet : Pet or any of its subclass
        My pet
    """
    my_pet.eat(food)


if __name__ == '__main__':

    list_of_pets = [Cat('Charlie'), Cat('Mila'), Pet('Haru')]
    list_of_food = ['Biscuit', 'milk', 'Meat', 'Apple', 'fish']

    print()

    while len(list_of_food) > 0:
        food = list_of_food.pop()

        for pet in range(list_of_pets):
            give_food_to_pet(pet, food)

    print()
