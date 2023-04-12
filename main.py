import lupa

# Define Python functions
def multiply_numbers(a, b):
    print('stuff')
    return a * b

def create_333():
    print('creating 333')

def create_444():
    print('creating 444')

# Create a Lua runtime
lua = lupa.LuaRuntime()

# Expose Python functions to the Lua runtime
lua.globals().create_333 = create_333
lua.globals().create_444 = create_444
lua.globals().multiply_numbers = multiply_numbers

# Define a variable to determine which function to call
was_approved = True
lua.globals().was_approved = was_approved

# Define Lua code that calls the Python functions based on the value of was_approved
lua_code = """
result = multiply_numbers(6, 7)

if was_approved then
    create_333()
else
    create_444()
end
"""

# Execute the Lua code
lua.execute(lua_code)

# Get the result from the Lua side
result = lua.globals().result

print("The result of the Python function called from Lua is:", result)

