# this is file to perform testing of our custom package imports

from package.maths import *
# importing subpackage module
from package.subpackages.mult import multiply


print(addition(10, 5))
print(subtraction(10, 5))

print(multiply(10, 5))

