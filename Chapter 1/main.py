first_name:str = "ada"
last_name:str = "lovelace"
full_name:str = f"{first_name} {last_name}"
message:str = f"Hello, {full_name.title()}!"
print(message)

print(first_name.capitalize())
print(first_name.casefold())
print(first_name.replace("f", "t"))

# Count how many characters in stones are also in jewels.
def count_jewels_in_stones(jewels: str, stones: str) -> int:
    count = 0
    for stone in stones:
        if stone in jewels:
            count += 1
    return count

count = count_jewels_in_stones("aA", "aAAbbbb")
print(f"Count: {count}")