def greet(name):
    """
    A simple function that takes a name as an input
    and returns a personalized greeting string.
    """
    return f"Hello, {name}! Welcome aboard."

# Example usage:
message = greet("Meet jaiswal")
print(message)
# Output: Hello, Meet! Welcome aboard.

def age_agent(age):
    if age < 18:
        return "You are a fresher."
    elif age >= 18 and age < 30:
        return "You are an experienced professional."
    else:
        return "You are a senior professional."
    
result = age_agent(25)
print(result)