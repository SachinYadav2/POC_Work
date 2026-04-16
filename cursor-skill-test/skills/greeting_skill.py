import sys

country = sys.argv[1] if len(sys.argv) > 1 else "World"

message = f"Hello, greetings to the people of {country}."

with open("output.txt", "w") as f:
    f.write(message)

print(message)