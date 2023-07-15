name = 'Eric'
print(f"Hello {name}, would you like to learn some python today?")
print(f"{name.title()},{name.upper()},{name.lower()}")

famous_person = "Albert Einstein"
message = "A person who never made a mistake never tried anything new."
print(f"{famous_person} once said, “{message}”")

name = " Somebody \t\n"
print(f"{name.lstrip()},{name.rstrip()},{name.strip()}")