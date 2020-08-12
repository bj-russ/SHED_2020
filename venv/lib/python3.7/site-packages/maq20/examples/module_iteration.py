from maq20 import MAQ20

maq20 = MAQ20()

# Iterate through the system and print a module's name.
for a_module in maq20:
    print(a_module.get_name())

# Iterate through system and if module number is 1 then stop iteration.
print('')  # new line
for a_module in maq20:
    print('{}: {}'.format(a_module.get_registration_number(), a_module.get_name()))
    if a_module.get_registration_number() == 1:
        break

# How many modules are in a system?
print('\nlen(maq20) : {}'.format(len(maq20)))

# Access a module with array notation.
if len(maq20) > 1:
    some_module = maq20[2]
    print('\nmaq20[2] = {}'.format(some_module.get_name()))
