# Jason Polanco
#10/17/19
# This program will determine if user is elegible for a seat in the U.S. Senate
#Or house of representatives

def main():
    
#Declare constants 
    SENYEARS = 9
    REPYEARS = 7

#Initialze and declare variables age and name and citizenship
    age = 0
    name =""
    yearsUs = 0
    
#Display welcome to the user, and describe program
    print("\nThis program determines  eligibility for a seat in the house or senate.")

#prompt name and age, and years of U.S. citizenship for users
    name = input("\nEnter your name:")
    #age = int(input("\nEnter your age:"))
    # try/except for user input strings instead of integers
    try:
        age = int(input("\nEnter your age:"))
    except ValueError:

        print("\nAge must be a number")
        age = int(input("\nEnter your age:"))
        
    if age< 18:
        print("\nYou must be 18 years of age")
        main()

    try:
        yearsUs = int(input("\nEnter the years of citzenship:"))
    except ValueError:
         print("Age must be a number")
         yearsUs = int(input("\nEnter the years of citzenship:"))

         
    if yearsUs <1:
        print(" You must have at least one year of citizenship")
        main()

#Use a two-way decision structure to determine if the user is elegible
# if age is equal to 18 and Citizenship is equal to 1 then
# they possibly can qualify for us senate or house under conditions
    if age == 18 and yearsUS == 1:
        print("You qualify  for house or senate")

    # first condition must be >= to 25 yrs of age and citiizenship must be >= to 7yrs for house
    if age >=25 and yearsUs >= 7:
        print("\nYou are eligible  for a seat in the House Of Representatives")

#second condition must be >= 30 yrs of age and citizenship must >= 9 for us senate
    if age >= 30 and yearsUs >= 9:
        print("\nYou are eligible for a seat in the U.S. Senate")

#third if under age of 18 and citizenship is less than one, then they do not qualify.
# If they do not qualify then restart program.
    else:
        print("\nYou are not eligible for the house or senate due to age/years restrictions .")
        print(main())



main()
