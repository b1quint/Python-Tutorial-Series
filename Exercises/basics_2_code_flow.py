#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Python Tutorial Series 2019 - Basics 2: Code Flow

This file holds a simple example of the basic Python code flow syntax. It
includes:

    - A method
    - A class
    - A if/elif/else case
    - A for loop

Excercise:

1) Find all the Syntax Errors before running
2) Debug why the cat is not eating the Meat
3) Create a new class called Dog and write how it behaves depending on the food
   it eats.

"""

class Pet:
    """
    Pets usually have a name and eat a lot. So let us represent our pet by
    its name and its "is_hungry" state.

    Parameters
    ----------
    name : str
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
        print('{} eats anything and is happy to eat {}'.format(
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
            print('{} seems happy!'.format(self.name))
            self.is_hungry = False

        elif food_name in ['milk']:
            print('{} is happy but still hungry.')

        else:
            print('{} does not like {}'.format(self.name, food_name))


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

    list_of_pets = [Cat('Charlie'), Cat('Mila'), Pet('Tao')]
    list_of_food = ['Chocolate', 'milk', 'Meat', 'apple', 'fish']

    for i in range(list_of_food):
        give_food_to_pet(list_of_pets[0], list_of_food[i])
