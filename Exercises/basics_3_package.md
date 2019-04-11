# Python Tutorial Series 2019 - Basics 3: Modules, Packages, Py2/3 and Conda

This file holds a simple example of a Python Project. It includes:

-  Three python files: 
    -  `my_module.py` that can be invoked from a terminal and return a random value between 1 and 6, 
    -  `dices.py` that contains classes with dices, 
    -  `setup.py` which contains the configuration for installation of the package.

## Excercise

1.  Rename the `basics_3_package/my_module.py` to `roll_dices.py`

2.  Turn `roll_dices.py` into a script.

    1. Create a new function called `main()` right after the `import` line. 
    
    2. Move the `print` statement in the end of the file to inside `main()`.
    
    3. Add `if __name__ == "__main__":` in the end of the file and call the `main()` function if it is True.
    
    4. Close the file and try to run it as a python script by typing `$ python roll_dices.py`.

3.  Create a new directory called `dice_roller`.
    
    1.  Add an empty file named `__init__.py`.
    
    2.  Move the `roll_dices.py` and the `dices.py` files to inside the `dice_roller`.
    
4.  Modify the `setup.py` file to install the new script you created.

    1. Open the `setup.py` file and add `"dice_roller/roll_dices.py",` inside the `script` list. Note the comma in the end of the string. 
    
    2. Install the package in editable mode (`-e`) using pip. 
    
    3. Go to another folder in your system and try to run the script again.

5.  Modify `roll()` to use the `dice_roller.dices.Dice` class instead of the `random.randint()` function.

   
