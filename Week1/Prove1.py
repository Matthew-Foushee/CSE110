RESET = '\033[0m'
def get_color_escape(rgbColor):
    return '\033[38;2;{};{};{}m'.format(rgbColor[0], rgbColor[1], rgbColor[2])

#This function is NOT foolproof but it does its job
def convertHexToDecimal(hex):
    hex = hex.lstrip("#")
    r = int(hex[0:2], 16)
    g = int(hex[2:4], 16)
    b = int(hex[4:6], 16)
    return [r,g,b]

favoriteColor = input("Please type your favorite color: ")
response = favoriteColor


print(len(favoriteColor), favoriteColor[0])
if(favoriteColor[0] == "#" and len(favoriteColor) == 7):
    rgbColor = convertHexToDecimal(favoriteColor)
    response = get_color_escape(rgbColor) + favoriteColor + RESET
    print("hi")

print("Your favorite color is")
print(response)