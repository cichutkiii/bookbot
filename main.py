def sort_on(dict):
    return dict["value"]

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
lower_str = file_contents.lower()
words = file_contents.split()
print("--- Begin report of books/frankenstein.txt ---")
print(f"{len(words)} words found in the document\n")
charss = list(lower_str)
slownik = {}
for litera in charss:
    if litera not in slownik.keys():
        slownik[litera] = 1
    else:
        slownik[litera] = slownik[litera] + 1
mlista = []
for literka in slownik:
    mlista.append({ 'letter': literka, 'value':slownik[literka]})
mlista.sort(reverse=True, key=sort_on)    
for lit in mlista:
    # print(lit)
    if lit['letter'].isalpha():
        print(f"The '{lit['letter']}' character was found {lit['value']} times")