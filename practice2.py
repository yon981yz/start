# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다".format(balance))
#         return balance


# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# balance = 0
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission,balance))


# def profile(name, age=17, main_lang="Japan"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
#         .format(name, age, main_lang))

# profile("Honoka", 26, "Japan")
# profile("Eva", 26, "Malaysia")

# profile("Honoka")
# profile("Eva")

# def profile(name, age, main_lang) :
#     print(name, age, main_lang)

# profile(name="Honoka", main_lang="Japan", age=20)
# profile(main_lang="Japan", age=20, name="Honoka")

# def profile(name, age, lang1, lang2, lang3, lang4, lang5, lang6):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()


# profile("Honoka", 26, "Japan", "Korea", "China", "Malaysia", "England", "Scotlant")
# profile("Eva", 28, "Indo", "US")

# gun = 10 

# def checkpoint(soilders): 
#     global gun 
#     gun = gun - soilders
#     print("[함수 내] 남은 총 : {0}".format(gun))


# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

# gun = 10

# def checkpoint_ret(gun, soilders):
#     gun = gun - soilders
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))


