class library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displaybook(self):
        print(f"we have follwing books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("lander-book hase been updated.youcan take the book now")
        else:
            print(f"book is alredy being taken{self.lendDict[book]}")

    def addbook(self,book):
        self.booklist.append(book)
        print("book hase been adeed to the list")

    def returnbook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    akshay = library(["chemistry","physics","biology","maths","scince"],"newtonlib")

    while(True):
        print(f"welcome to the{akshay.name} library. Enter your choise to continue")
        print("1.Display book")
        print("2.lend a book")
        print("3.add a book")
        print("4.return a book")
        user_choice = int(input())
        
        if user_choice not in [1,2,3,4]:
            print("please enter valid option")
            continue
        else:
            user_choice = int(user_choice)
        
        if user_choice == 1:
            akshay.displaybook()

        elif user_choice == 2:
            book = input("Enter the name of book you want to land:")
            user = input("inter your name")
            akshay.lendbook(user, book)

        elif user_choice == 3:
            book = input("Enter the nane of book you want to add:")
            akshay.addbook(book)

        elif user_choice == 4:
            book = input("Enter the name of bool you want to return")
            akshay.returnbook(book)

        else:
            print("not a valid option")


        print("press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue