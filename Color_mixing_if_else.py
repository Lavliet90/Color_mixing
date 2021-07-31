#Red, blue and yellow are called primary colors because they cannot be obtained by mixing other colors. When two primary colors
# are mixed, a secondary color is obtained:

#if you mix red and blue, you get purple;
#if you mix red and yellow, you get orange;
#if you mix blue and yellow, you get green.
#Write a program that reads the names of two primary colors for mixing. If the user enters anything other than red, blue,
# or yellow, the program should display an error message. Otherwise, the program should print the name of the secondary color, which will be the result.

a=input()
b=input()
if (a=="красный" and b=="синий") or (b=="красный" and a=="синий"):
    print("фиолетовый")
elif (a=="красный" and b=="желтый") or (b=="красный" and a=="желтый"):
    print("оранжевый")
elif (a=="синий" and b=="желтый") or (b=="синий" and a=="желтый"):
    print("зеленый")
elif a=="синий" and b=="синий":
    print("синий")
elif a=="желтый" and b=="желтый":
    print("желтый")
elif a=="красный" and b=="красный":
    print("красный")
else:
    print("ошибка цвета")

