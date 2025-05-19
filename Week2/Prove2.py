adj1 = input("Give me an adjective: ")
animal1 = input("Give me an animal: ")
verb1 = input("Give me a verb: ")
exclamation1 = input("Give me an exclamation: ").upper()
verb2 = input("Give me a verb: ")
verb3 = input("Give me a verb: ")
person1 = input("Name of person: ")
thing = input("Give me a thing: ")
verb4 = input("Give me a past tense verb: ")

vowels = ["a", "e", "i", "o", "u"]

aOrAn = "a"
if(thing[0].lower() in vowels):
    aOrAn = "an"

print(
f"""The other day, I was really in trouble. It all started when I saw a very
{adj1} {animal1} {verb1} down the hallway. "{exclamation1}!" I yelled. But all
I could think to do was to {verb2} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb3}
right in front of {person1}.

All of a sudden {person1} pulled {aOrAn} {thing} out from behind their back and {verb4} towards the {animal1}
"""
)