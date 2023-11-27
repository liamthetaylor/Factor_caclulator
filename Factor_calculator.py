def statement_generator(text, decoration):
    ends = decoration * 5
    statement = "{} {} {}".format(ends, text, ends)
    print()
    print(statement)
    print()
    return ""


def instructions():
    statement_generator("Instructions", "=")
    print()
    print("Enter a number between 1 and 200. The factor calculator will give you the factors of that number.")
    print()
    return ""


error = "Please enter a number between 1 and 200"
primes = ["2", "3", "5", "7", "11", "13", "17", "19", "23", "29", "31", "37", "41", "43", "47", "53", "59", "61", "67",
          "71", "73", "79", "83", "89", "97", "101", "103", "107", "109", "113", "127", "131", "137", "139", "149",
          "151", "157", "163", "167", "173", "179", "181", "191", "193", "197", "199"]
statement_generator("Factor Calculator", "<>")
first_time = input("Press <enter> to see instructions, any other key to continue: ")
if first_time == "":
    instructions()
run = False
while not run:
    try:
        print()
        number = input("enter an number between 1 and 200: ")
        if number in primes:
            print(number, "is a prime. This means only factors are 1 and", number)
        else:
            if number == "1":
                print("one only has one factor, 1")
            elif number == "4":
                print("1, 2, 4")
                print("This number is a perfect square")
            elif number == "6":
                print("1, 2, 3, 6")
            elif number == "8":
                print("1, 2, 4, 8")
            elif number == "9":
                print("1, 3, 9")
                print("This number is a perfect square")
            elif number == "10":
                print("1, 2, 5, 10")
            elif number == "12":
                print("1, 2, 3, 4, 6, 12")
            elif number == "14":
                print("1, 2, 7, 14")
            elif number == "15":
                print("1, 3, 5, 15")
            elif number == "16":
                print("1, 2, 4, 8, 16")
                print("This number is a perfect square")
            elif number == "18":
                print("1, 2, 3, 6, 9, 18")
            elif number == "20":
                print("1, 2, 4, 5, 10, 20")
            elif number == "21":
                print("1, 3, 7, 21")
            elif number == "22":
                print("1, 2, 11, 22")
            elif number == "24":
                print("1, 2, 3, 4, 6, 8, 12, 24")
            elif number == "25":
                print("1, 5, 25")
                print("This number is a perfect square")
            elif number == "26":
                print("1, 2, 13, 26")
            elif number == "27":
                print("1, 5, 25")
            elif number == "28":
                print("1, 2, 4, 7, 14, 28")
            elif number == "30":
                print("1, 2, 3, 5, 6, 10, 15, 30")
            elif number == "32":
                print("1, 2, 4, 8, 16, 32")
            elif number == "33":
                print("1, 3, 11, 33")
            elif number == "34":
                print("1, 2, 17, 34")
            elif number == "35":
                print("1, 5, 7, 35")
            elif number == "36":
                print("1, 2, 3, 4, 6, 9, 12, 18, 36")
                print("This number is a perfect square")
            elif number == "38":
                print("1, 2, 19, 38")
            elif number == "39":
                print("1, 3, 13, 39")
            elif number == "40":
                print("1, 2, 4, 5, 8, 10, 20, 40")
            elif number == "42":
                print(" 1, 2, 3, 6, 7, 14, 21, 42")
            elif number == "44":
                print("1, 2, 4, 11, 22, 44")
            elif number == "45":
                print("1, 3, 5, 9, 15, 45")
            elif number == "46":
                print("1, 2, 23, 46")
            elif number == "48":
                print("1, 2, 3, 4, 6, 8, 12, 16, 24, 48")
            elif number == "49":
                print("1, 7, 49")
                print("This number is a perfect square")
            elif number == "50":
                print("1, 2, 5, 10, 25, 50")
            elif number == "51":
                print(" 1, 3, 17, 51")
            elif number == "52":
                print("1, 2, 4, 13, 26, 52")
            elif number == "54":
                print("1, 2, 3, 6, 9, 18, 27, 54")
            elif number == "55":
                print("1, 5, 11, 55")
            elif number == "56":
                print("1, 2, 4, 7, 8, 14, 28, 56")
            elif number == "57":
                print("1, 3, 19, 57")
            elif number == "58":
                print("1, 2, 29, 58")
            elif number == "60":
                print(" 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60")
            elif number == "62":
                print(" 1, 2, 31, 62")
            elif number == "63":
                print("1, 3, 7, 9, 21, 63")
            elif number == "64":
                print("1, 2, 4, 8, 16, 32, 64")
                print("This number is a perfect square")
            elif number == "65":
                print("1, 5, 13, 65")
            elif number == "66":
                print("1, 2, 3, 6, 11, 22, 33, 66")
            elif number == "68":
                print("1, 2, 4, 17, 34, 68")
            elif number == "69":
                print("1, 3, 23, 69")
            elif number == "70":
                print("1, 2, 5, 7, 10, 14, 35, 70")
            elif number == "72":
                print("1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72")
            elif number == "74":
                print("1, 2, 37, 74")
            elif number == "75":
                print("1, 3, 5, 15, 25, 75")
            elif number == "76":
                print("1, 2, 4, 19, 38, 76")
            elif number == "77":
                print("1, 7, 11, 77")
            elif number == "78":
                print("1, 2, 3, 6, 13, 26, 39, 78")
            elif number == "80":
                print("1, 2, 4, 5, 8, 10, 16, 20, 40, 80")
            elif number == "81":
                print("1, 3, 9, 27, 81")
                print("This number is a perfect square")
            elif number == "82":
                print("1, 2, 41, 82")
            elif number == "84":
                print(" 1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84")
            elif number == "85":
                print("1, 5, 17, 85")
            elif number == "86":
                print("1, 2, 43, 86")
            elif number == "87":
                print("1, 3, 29, 87")
            elif number == "88":
                print("1, 2, 4, 8, 11, 22, 44, 88")
            elif number == "90":
                print(" 1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45, 90")
            elif number == "91":
                print("1, 7, 13, 91")
            elif number == "92":
                print("1, 2, 4, 23, 46, 92")
            elif number == "93":
                print("1, 3, 31, 93")
            elif number == "94":
                print("1, 2, 47, 94")
            elif number == "95":
                print("1, 5, 19, 95")
            elif number == "96":
                print(", 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 96")
            elif number == "98":
                print("1, 2, 7, 14, 49, 98")
            elif number == "99":
                print("1, 3, 9, 11, 33, 99")
            elif number == "100":
                print("1, 2, 4, 5, 10, 20, 25, 50, 100")
                print("This number is a perfect square")
            elif number == "102":
                print("1, 2, 3, 6, 17, 34, 51, 102")
            elif number == "104":
                print("1, 2, 4, 8, 13, 26, 52, 104")
            # 107", "109", "113", "127", "131", "137", "139", "149", "151", "157", "163", "167", "173", "179",
            # "181",  "191", "193", "197", "199
            elif number == "105":
                print("1, 3, 5, 7, 15, 21, 35, 105")
            elif number == "106":
                print("1, 2, 53, 106")
            elif number == "108":
                print("1, 2, 3 , 4, 6, 9, 12, 18, 27, 36, 54, 108")
            elif number == "110":
                print("1, 2, 5, 10, 11, 22, 55, 110")
            elif number == "111":
                print("1, 3, 37, 111")
            elif number == "112":
                print("1, 2, 4, 7, 8, 14, 16, 28, 56, 112")
            elif number == "114":
                print("1, 2, 3, 6, 19, 38, 57, 114")
            elif number == "115":
                print("1, 5, 23, 115")
            elif number == "116":
                print("1, 2, 4, 29, 58, 116")
            elif number == "117":
                print("1, 3, 9, 13, 39, 117")
            elif number == "118":
                print("1, 2, 59, 118")
            elif number == "119":
                print("1, 7, 17, 119")
            elif number == "120":
                print(" 1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120")
            elif number == "121":
                print("1, 11, 121")
                print("This number is a perfect square")
            elif number == "122":
                print("1, 2, 61, 122")
            elif number == "123":
                print("1, 3, 41, 123")
            elif number == "124":
                print("1, 2, 4, 31, 62, 124")
            elif number == "125":
                print("1, 5, 25, 125")
            elif number == "126":
                print("1, 2, 3, 6, 7, 9, 14, 18, 21, 42, 63, 126")
            elif number == "128":
                print("1, 2, 4, 8, 16, 32, 64, 128")
            elif number == "130":
                print("1, 2, 5, 10, 13, 26, 65, 130")
            elif number == "132":
                print("1, 2, 3, 4, 6, 11, 12, 22, 33, 44, 66, 132")
            elif number == "133":
                print("1, 7, 19, 133")
            elif number == "134":
                print("1, 2, 67, 134")
            elif number == "135":
                print("1, 3, 5, 9, 15, 27, 45, 135")
            elif number == "136":
                print("1, 2, 4, 8, 17, 34, 68, 136")
            elif number == "138":
                print("1, 2, 3, 6, 23, 46, 69, 138")
            elif number == "140":
                print("1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140")
            elif number == "141":
                print("1, 3, 47, 141")
            elif number == "142":
                print("1, 2, 71, 142")
            elif number == "143":
                print("1, 11, 13, 143")
            elif number == "144":
                print("1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 36, 48, 72, 144")
                print("This number is a perfect square")
            elif number == "145":
                print("1, 5, 29, 145")
            elif number == "146":
                print("1, 2, 73, 146")
            elif number == "147":
                print("1, 3, 7, 21, 49, 147")
            elif number == "148":
                print("1, 2, 4, 37, 74, 148")
            elif number == "150":
                print("1, 2, 3, 5, 6, 10, 15, 25, 30, 50, 75, 150")
            elif number == "152":
                print("1, 2, 4, 8, 19, 38, 76, 152")
            elif number == "153":
                print("1, 2, 4, 8, 19, 38, 76, 152")
            elif number == "154":
                print("1, 2, 7, 11, 14, 22, 77, 154")
            elif number == "155":
                print("1, 5, 31, 155")
            elif number == "156":
                print("1, 2, 3, 4, 6, 12, 13, 26, 39, 52, 78, 156")
            elif number == "158":
                print("1, 2, 79, 158")
            elif number == "159":
                print("1, 3, 53, 159")
            elif number == "160":
                print("1, 2, 4, 5, 8, 10, 16, 20, 32, 40, 80, 160")
            elif number == "161":
                print("1, 7, 23, 161")
            elif number == "162":
                print("1, 2, 3, 6, 9, 18, 27, 54, 81, 162")
            elif number == "164":
                print("1, 2, 4, 41, 82, 164")
            elif number == "165":
                print("1, 3, 5, 11, 15, 33, 55, 165")
            elif number == "166":
                print("1, 2, 83, 166")
            elif number == "168":
                print("1, 2, 3, 4, 6, 7, 8, 12, 14, 21, 24, 28, 42, 56, 84, 168")
            elif number == "169":
                print("1, 13, 169")
                print("This number is a perfect square")
            elif number == "170":
                print("1, 2, 5, 10, 17, 34, 85, 170")
            elif number == "171":
                print("1, 3, 9, 19, 57, 171")
            elif number == "172":
                print("1, 2, 4, 43, 86, 172")
            elif number == "174":
                print("1, 2, 3, 6, 29, 58, 87, 174")
            elif number == "175":
                print("1, 5, 7, 25, 35, 175")
            elif number == "176":
                print("1, 2, 4, 8, 11, 16, 22, 44, 88, 176")
            elif number == "177":
                print("1, 3, 59, 177")
            elif number == "178":
                print("1, 2, 89, 178")
            elif number == "180":
                print("1, 2, 3, 4, 5, 6, 9, 10, 12, 15, 18, 20, 30, 36, 45, 60, 90, 180")
            elif number == "182":
                print("1, 2, 7, 13, 14, 26, 91, 182")
            elif number == "183":
                print("1, 3, 61, 183")
            elif number == "184":
                print("1, 2, 4, 8, 23, 46, 92, 184")
            elif number == "185":
                print("1, 5, 37, 185")
            elif number == "186":
                print(" 1, 2, 3, 6, 31, 62, 93, 186")
            elif number == "187":
                print("1, 11, 17, 187")
            elif number == "188":
                print("1, 2, 4, 47, 94, 188")
            elif number == "189":
                print("1, 3, 7, 9, 21, 27, 63, 189")
            elif number == "190":
                print("1, 2, 5, 10, 19, 38, 95, 190")
            elif number == "192":
                print("1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 192")
            elif number == "194":
                print("1, 2, 97, 194")
            elif number == "195":
                print("1, 3, 5, 13, 15, 39, 65, 195")
            elif number == "196":
                print("1, 2, 4, 7, 14, 28, 49, 98, 196")
                print("This number is a perfect square")
            elif number == "198":
                print("1, 2, 3, 6, 9, 11, 18, 22, 33, 66, 99, 198")
            elif number == "200":
                print("1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 200")
            else:
                print()
                print(error)
                print()
    except ValueError:
        print()
        print(error)
        print()
    end_loop = input("Press <enter> to go again, any other key to finish: ")
    if end_loop == "":
        run = False
    else:
        run = True
print()
print("Thank you for using the factor calculator")
