# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
 #   print('dd')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

Chk_phrase = int()
a = input()

for i in range(len(a)):
    if a[i] == " ":
        Chk_phrase += 1

if Chk_phrase >= 14:
    print("OK" + str(Chk_phrase+1))
else:
    print("어절갯수 : " + str(Chk_phrase+1))
