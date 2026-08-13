# KBC Game (Agniveer Vayu Edition)(Revision)
# Built using Python Fundamentals




questions = [["An object is projected with a velocity of \(20\text{ m/s}\) at an angle of \(30^{\circ }\) with the horizontal. What is the maximum height attained by the object? (Take \(g = 10\text{ m/s}^2\))",
              "A. 5 m",
              "B. 10 m",
              "C. 15 m",
              "D. 20 m",
              "A",
              "(Explanation: The maximum height is calculated using the formula \(H = frac{u^2 \sin^2 theta}{2g}\). Substituting the values, \(H = frac{20^2 times \sin^2(30^\circ)}{2 times 10} = frac{400 times 0.25}{20} = 5text{ m}\).)"],
              ["If a matrix \(A\) is both symmetric and skew-symmetric, then \(A\) must be a:",
               "A. Diagonal matrix",
               "B. Zero matrix",
               "C. Identity matrix",
               "D. Square matrix",
               "B","(Explanation: For a symmetric matrix, \(A^T = A\), and for a skew-symmetric matrix, \(A^T = -A\). Equating both gives \(A = -A\), which implies \(2A = 0\), so \(A\) is a zero matrix.)"],
               ["Which of the following laws defines the concept of temperature?",
                "A. Zeroth Law of Thermodynamics",
                "B. First Law of Thermodynamics",
                "C. Second Law of Thermodynamics",
                "D. Third Law of Thermodynamics",
                "A",
                "(Explanation: The Zeroth Law states that if two systems are in thermal equilibrium with a third system, they are in thermal equilibrium with each other, providing the basis for measuring temperature.)"],
                ["Evaluate the limit: \(\lim_{x \to 0} \frac{\sin 5x}{3x}\)",
                 "A. 1",
                 "B. 3/5",
                 "C. 5/3",
                 "D. 0",
                 "C",
                 "(Explanation: Multiply and divide by \(5\) to use the standard limit property \(\lim_{theta to 0} frac{\sin theta}{theta} = 1\), giving \(\lim_{x to 0} frac{\sin 5x}{5x} times frac{5}{3} = 1 times frac{5}{3} = frac{5}{3}\).)"],
                 ["The dimensional formula for the Universal Gravitational Constant (\(G\)) is:",
                  "A. \([M^{-1} L^3 T^{-2}]\)",
                  "B. \([M^1 L^3 T^{-2}]\)",
                  "C. \([M^{-1} L^2 T^{-2}]\)",
                  "D. \([M^{-2} L^3 T^{-1}]\)",
                  "A",
                  "(Explanation: From \(F = frac{G m_1 m_2}{r^2}\), we get \(G = frac{F r^2}{m_1 m_2}\). Substituting dimensions, \([M L T^{-2}] times [L^2] div [M^2] = [M^{-1} L^3 T^{-2}]\).)"],
                  ["If \(\log_2 (x - 1) = 3\), then the value of \(x\) is:",
                   "A. 7",
                   "B. 8",
                   "C. 9",
                   "D. 10",
                   "C",
                   "(Explanation: Converting the logarithmic equation to exponential form gives \(x - 1 = 2^3\). Therefore, \(x - 1 = 8\), which means \(x = 9\).)"],
                   ["Choose the word that is closest in meaning (Synonym) to (ABANDON):",
                    "A. Retain",
                    "B. Forsake",
                    "C. Cherish",
                    "D. Adopt",
                    "B",
                    "(Explanation: (Abandon) means to completely leave or give up on something, which directly matches the definition of (forsake).)"],
                    ["Fill in the blank with the correct option: (He has been living in Delhi ______ ten years.)",
                     "A. since",
                     "B. for",
                     "C. from",
                     "D. during",
                     "B",
                     "(Explanation: (For) is used to denote a specific duration or period of time (ten years), whereas (since) is used for a specific starting point in time.)"],
                     ["Identify the error in the following sentence: (Neither the teacher (A) / nor the students (B) / was present in the class (C) / No error (D))",
                      "A. A",
                      "B. B",
                      "C. C",
                      "D) D",
                      "C",
                      "(Explanation: When two subjects are joined by (neither... nor), the verb agrees with the closer subject. Since (students) is plural, (was) must be corrected to (were).)"],
                      ["What is the active voice of: (The match was won by the Indian team.)",
                       "A. The Indian team wins the match.",
                       "B) The Indian team has won the match.",
                       "C. The Indian team won the match.",
                       "D) The Indian team is winning the match.",
                       "C",
                       "(Explanation: The passive voice is in the simple past tense (was won), so its corresponding active voice form must use the simple past verb (won).)"],
                       ["Who is known as the (Father of the Indian Constitution)?",
                        "A. Mahatma Gandhi",
                        "B) Dr. B.R. Ambedkar",
                        "C. Jawaharlal Nehru",
                        "D) Dr. Rajendra Prasad",
                        "B",
                        "(Explanation: Dr. Bhimrao Ramji Ambedkar served as the Chairman of the Drafting Committee and played a pivotal role in drafting the Indian Constitution.)"],
                        ["The (Kaziranga National Park), famous for the one-horned rhinoceros, is located in which Indian state?",
                        "A. West Bengal",
                        "B) Assam",
                        "C. Arunachal Pradesh",
                        "D) Odisha",
                        "B",
                        "(Explanation: Kaziranga National Park is a highly celebrated wildlife sanctuary situated in the state of Assam.)"],
                        ["Find the missing number in the series: 4, 9, 16, 25, 36, ?",
                        "A. 45",
                        "B) 47",
                        "C. 49",
                        "D) 50",
                        "C",
                        "(Explanation: The series consists of consecutive perfect squares (\(2^2, 3^2, 4^2, 5^2, 6^2\)). The next number is \(7^2 = 49\).)"],
                        ["Pointing to a photograph, a man said, (I have no brother or sister, but that man’s father is my father’s son.) Whose photograph was it?",
                        "A. His own",
                        "B) His son's",
                        "C. His father's",
                        "D) His nephew's",
                        "B",
                        "(Explanation: Because the man has no siblings, (my father’s son) is the man himself. Since that man's father is himself, the photo belongs to his son.)"],
                        ["If 'ROSE' is coded as '6821' and 'CHAIR' is coded as '73456', how is 'SEARCH' coded in that language?",
                        "A. 214673",
                        "B) 214763",
                        "C. 216473",
                        "D) 241673",
                        "A",
                        "(Explanation: By matching direct letter-to-digit positions from the given words, S=2, E=1, A=4, R=6, C=7, and H=3, which spells out 214673.)"]
                        ]
money = [1000,2000,5000,10000,20000,40000,80000,120000,150000,200000]
winning = 0
print("\n\nWelcome To KBC(Kaun Banega Crorepati)!!!!!💸💰💹🤑\n","Toh ye rha aapka sawaal Computer Screen par")

for i in range(len(questions)):
    print ("\n\n Question", i+1 ,"for ₹",money[i],"\n\n",questions[i][0],"\n\n",questions[i][1],"\n",questions[i][2],"\n",questions[i][3],"\n",questions[i][4])
    answer = input("Enter option(A/B/C/D)🔒: ")
    if(answer.upper() == questions[i][5]):
        winning = money[i]
        print("Correct Answer😃\n\n","Congratulations!!!!!\n\n","You won ₹",winning,"🥲 💵")
        print(questions[i][6])
        if(i < len(questions)-1):
            print("\n\nThe Next Question is for ₹",money[i+1],"😮")
    else:
        print("\n\nSorry!!!!!\n It's a Wroooong Answer.😔")
        print(questions[i][6])
        print("\nThe Correct Answer by Computer Mahaseh is🗝️ 🔓",questions[i][5])
        break
print("\n\nCongratulations!!\nYou are taking ₹",winning,"home.🥳\n\n")




# this code  and its logic is by harry
questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
]

levels = [5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 30000000, 50000000, 70000000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 80000
      print("Most Congratulations, You have achieved FIRST major Milestone/Level 1🎁🎁🎉💵🤑💹")
    elif(i == 9):
      money = 2500000
      print("Most Congratulations, You have achieved SECOND major Milestone/Level 2🎊✨💵🎁🎁")
    elif(i == 14):
      money = 70000000
      print("Saaaaaaaaaat crooooooooore!!!!!(7 Crores)😮🤯😱😵‍💫 - JACKPOT🤑🤑🤑💰💹🎉🎆🎇🎊✨")
  else:
    print("Wrong answer!😫😭")
    break 

print(f"Your take home money is {money}")