first_name:str = "ada"
last_name:str = "lovelace"
full_name:str = f"{first_name} {last_name}"
message:str = f"Hello, {full_name.title()}!"
print(message)

print(first_name.capitalize())
print(first_name.casefold())
print(first_name.replace("f", "t"))

# Count how many characters in stones are also in jewels.

def numJewelsInStones(self, jewels: str, stones: str) -> int:
    return sum(stones.count(j) for j in jewels)

print (numJewelsInStones("hello", "masfa"))