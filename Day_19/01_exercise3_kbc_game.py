# KBC Game (Agniveer Vayu Edition)
# Built using Python Fundamentals




questions = [["(English) Choose the synonym of 'Abundant'?",
              "A. Scarce",
              "B. Plentiful",
              "C. Little",
              "D. Harsh",
              "B"],
              ["(Physics) What is the SI unit of magnetic induction?",
               "A. Weber",
               "B. Tesla",
               "C. Henry",
               "D. Gauss",
               "B"],
               ["(Mathematics) If \(f(x) = x^3\), what is the derivative \(f'(2)\)?",
                "A. 6",
                "B. 8",
                "C. 12",
                "D. 4",
                "C"],
                ["(Reasoning) Find the missing number in the series: 2, 6, 12, 20, 30,?",
                 "A. 40",
                 "B. 42",
                 "C. 44",
                 "D. 48",
                 "B"],
                 ["(General Awareness) Who is known as the 'Missile Man of India'?",
                  "A. Dr. Homi Bhabha",
                  "B. Dr. Vikram Sarabhai",
                  "C. Dr. A.P.J. Abdul Kalam",
                  "D. C.V. Raman",
                  "C"],
                  ["(English) Fill in the blank with the correct preposition: He is blind ___ one eye.",
                   "A. in",
                   "B. of",
                   "C. to",
                   "D. with",
                   "B"],
                   ["(Physics) The dimensional formula of universal gravitational constant (\(G\)) is:",
                    "A. \([M^{-1} L^3 T^{-2}]\)",
                    "B. \([M L^2 T^{-2}]\)",
                    "C. \([M^{-1} L^2 T^{-2}]\)",
                    "D. \([M L^3 T^{-2}]\)",
                    "A"],
                    ["(Mathematics) What is the value of \(\sin(30^\circ) \cos(60^\circ) + \cos(30^\circ) \sin(60^\circ)\)?",
                     "A. 0",
                     "B. 1",
                     "C. 1/2",
                     "D. \(\sqrt{3}/2\)",
                     "B"],
                     ["(Reasoning) If ROAD is coded as URDG, then SWAN is coded as:",
                      "A. VZDQ",
                      "B. VZDP",
                      "C. VZCP",
                      "D) VZCR",
                      "A"],
                      ["(General Awareness) Where is the headquarters of the Indian Air Force located?",
                       "A. Kochi",
                       "B) New Delhi",
                       "C. Bengaluru",
                       "D) Kolkata",
                       "B"]]
money = [1000,2000,5000,10000,20000,40000,80000,120000,150000,200000]
winning = 0
print("\n\nWelcome To KBC(Kaun Banega Crorepati)!!!!!💸💰💹🤑\n","Toh ye rha aapka sawaal Computer Screen par")

for i in range(len(questions)):
    print ("\n\n Question", i+1 ,"for ₹",money[i],"\n\n",questions[i][0],"\n\n",questions[i][1],"\n",questions[i][2],"\n",questions[i][3],"\n",questions[i][4])
    answer = input("Enter option(A/B/C/D)🔒: ")
    if(answer.upper() == questions[i][5]):
        winning = money[i]
        print("Correct Answer😃\n\n","Congratulations!!!!!\n\n","You won ₹",winning,"🥲 💵")
        if(i < len(questions)-1):
            print("\n\nThe Next Question is for ₹",money[i+1],"😮")
    else:
        print("\n\nSorry!!!!!\n It's a Wroooong Answer.😔")
        print("\nThe Correct Answer by Computer Mahaseh is🗝️ 🔓",questions[i][5])
        break
print("\n\nCongratulations!!\nYou are taking ₹",winning,"home.🥳\n\n")




# # this code  and its logic is by harry
# questions = [
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
#   [
#     "Which language was used to create fb?", "Python", "French", "JavaScript",
#     "Php", "None", 4
#   ],
# ]

# levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
# money = 0
# for i in range(0, len(questions)):
  
#   question = questions[i]
#   print(f"\n\nQuestion for Rs. {levels[i]}")
#   print(f"a. {question[1]}          b. {question[2]} ")
#   print(f"c. {question[3]}          d. {question[4]} ")
#   reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
#   if (reply == 0):
#     money = levels[i-1]
#     break
#   if(reply == question[-1]):
#     print(f"Correct answer, you have won Rs. {levels[i]}")
#     if(i == 4):
#       money = 10000
#     elif(i == 9):
#       money = 320000
#     elif(i == 14):
#       money = 10000000
#   else:
#     print("Wrong answer!")
#     break 

# print(f"Your take home money is {money}")