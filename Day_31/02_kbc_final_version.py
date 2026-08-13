# KBC Game (Agniveer Vayu Edition)(THE FINAL VERSION)

# ABOUT GAME :-
# ============================================================
# KBC GAME — AGNIVEER VAYU EDITION
# A console-based quiz game built using Python fundamentals.
#
# Features:
# • 15 Agniveer Vayu-style MCQs with explanations.
# • Progressive prize money with 3 major milestones.
# • Quit option, wrong-answer handling and take-home winnings.
# • Case-insensitive answer checking and interactive input.
#
# Concepts Used:
# Lists & Nested Lists | for Loop | Conditions | break
# Indexing | String Methods | Functions | f-strings | User Input
#
# Purpose: Combines Python programming practice with
# Agniveer Vayu exam preparation.
# ============================================================




questions = [["1. An object is projected with a velocity of \(20\text{ m/s}\) at an angle of \(30^{\circ }\) with the horizontal. What is the maximum height attained by the object? (Take \(g = 10\text{ m/s}^2\))",
              "A. 5 m",
              "B. 10 m",
              "C. 15 m",
              "D. 20 m",
              "A",
              "(Explanation: The maximum height is calculated using the formula \(H = frac{u^2 \sin^2 theta}{2g}\). Substituting the values, \(H = frac{20^2 times \sin^2(30^\circ)}{2 times 10} = frac{400 times 0.25}{20} = 5text{ m}\).)"],
              ["2. If a matrix \(A\) is both symmetric and skew-symmetric, then \(A\) must be a:",
               "A. Diagonal matrix",
               "B. Zero matrix",
               "C. Identity matrix",
               "D. Square matrix",
               "B","(Explanation: For a symmetric matrix, \(A^T = A\), and for a skew-symmetric matrix, \(A^T = -A\). Equating both gives \(A = -A\), which implies \(2A = 0\), so \(A\) is a zero matrix.)"],
               ["3. Which of the following laws defines the concept of temperature?",
                "A. Zeroth Law of Thermodynamics",
                "B. First Law of Thermodynamics",
                "C. Second Law of Thermodynamics",
                "D. Third Law of Thermodynamics",
                "A",
                "(Explanation: The Zeroth Law states that if two systems are in thermal equilibrium with a third system, they are in thermal equilibrium with each other, providing the basis for measuring temperature.)"],
                ["4. Evaluate the limit: \(\lim_{x to 0} frac{\sin 5x}{3x}\)",
                 "A. 1",
                 "B. 3/5",
                 "C. 5/3",
                 "D. 0",
                 "C",
                 "(Explanation: Multiply and divide by \(5\) to use the standard limit property \(\lim_{theta to 0} frac{\sin theta}{theta} = 1\), giving \(\lim_{x to 0} frac{\sin 5x}{5x} times frac{5}{3} = 1 times frac{5}{3} = frac{5}{3}\).)"],
                 ["5. The dimensional formula for the Universal Gravitational Constant (\(G\)) is:",
                  "A. \([M^{-1} L^3 T^{-2}]\)",
                  "B. \([M^1 L^3 T^{-2}]\)",
                  "C. \([M^{-1} L^2 T^{-2}]\)",
                  "D. \([M^{-2} L^3 T^{-1}]\)",
                  "A",
                  "(Explanation: From \(F = frac{G m_1 m_2}{r^2}\), we get \(G = frac{F r^2}{m_1 m_2}\). Substituting dimensions, \([M L T^{-2}] times [L^2] div [M^2] = [M^{-1} L^3 T^{-2}]\).)"],
                  ["6. If \(\log_2 (x - 1) = 3\), then the value of \(x\) is:",
                   "A. 7",
                   "B. 8",
                   "C. 9",
                   "D. 10",
                   "C",
                   "(Explanation: Converting the logarithmic equation to exponential form gives \(x - 1 = 2^3\). Therefore, \(x - 1 = 8\), which means \(x = 9\).)"],
                   ["7. Choose the word that is closest in meaning (Synonym) to (ABANDON):",
                    "A. Retain",
                    "B. Forsake",
                    "C. Cherish",
                    "D. Adopt",
                    "B",
                    "(Explanation: (Abandon) means to completely leave or give up on something, which directly matches the definition of (forsake).)"],
                    ["8. Fill in the blank with the correct option: (He has been living in Delhi ______ ten years.)",
                     "A. since",
                     "B. for",
                     "C. from",
                     "D. during",
                     "B",
                     "(Explanation: (For) is used to denote a specific duration or period of time (ten years), whereas (since) is used for a specific starting point in time.)"],
                     ["9. Identify the error in the following sentence: (Neither the teacher (A) / nor the students (B) / was present in the class (C) / No error (D))",
                      "A. A",
                      "B. B",
                      "C. C",
                      "D) D",
                      "C",
                      "(Explanation: When two subjects are joined by (neither... nor), the verb agrees with the closer subject. Since (students) is plural, (was) must be corrected to (were).)"],
                      ["10. What is the active voice of: (The match was won by the Indian team.)",
                       "A. The Indian team wins the match.",
                       "B) The Indian team has won the match.",
                       "C. The Indian team won the match.",
                       "D) The Indian team is winning the match.",
                       "C",
                       "(Explanation: The passive voice is in the simple past tense (was won), so its corresponding active voice form must use the simple past verb (won).)"],
                       ["11. Who is known as the (Father of the Indian Constitution)?",
                        "A. Mahatma Gandhi",
                        "B) Dr. B.R. Ambedkar",
                        "C. Jawaharlal Nehru",
                        "D) Dr. Rajendra Prasad",
                        "B",
                        "(Explanation: Dr. Bhimrao Ramji Ambedkar served as the Chairman of the Drafting Committee and played a pivotal role in drafting the Indian Constitution.)"],
                        ["12. The (Kaziranga National Park), famous for the one-horned rhinoceros, is located in which Indian state?",
                        "A. West Bengal",
                        "B) Assam",
                        "C. Arunachal Pradesh",
                        "D) Odisha",
                        "B",
                        "(Explanation: Kaziranga National Park is a highly celebrated wildlife sanctuary situated in the state of Assam.)"],
                        ["13. Find the missing number in the series: 4, 9, 16, 25, 36, ?",
                        "A. 45",
                        "B) 47",
                        "C. 49",
                        "D) 50",
                        "C",
                        "(Explanation: The series consists of consecutive perfect squares (\(2^2, 3^2, 4^2, 5^2, 6^2\)). The next number is \(7^2 = 49\).)"],
                        ["14. Pointing to a photograph, a man said, (I have no brother or sister, but that man’s father is my father’s son.) Whose photograph was it?",
                        "A. His own",
                        "B) His son's",
                        "C. His father's",
                        "D) His nephew's",
                        "B",
                        "(Explanation: Because the man has no siblings, (my father’s son) is the man himself. Since that man's father is himself, the photo belongs to his son.)"],
                        ["15. If 'ROSE' is coded as '6821' and 'CHAIR' is coded as '73456', how is 'SEARCH' coded in that language?",
                        "A. 214673",
                        "B) 214763",
                        "C. 216473",
                        "D) 241673",
                        "A",
                        "(Explanation: By matching direct letter-to-digit positions from the given words, S=2, E=1, A=4, R=6, C=7, and H=3, which spells out 214673.)"]
                        ]


money = [5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 30000000, 50000000, 70000000]
winning = 0
print("\n\nWelcome To KBC(Kaun Banega Crorepati)!!!!!💸💰💹🤑\nRules: -\n- There are 3 levels - 1st at Rs. 80000, 2nd at Rs. 2500000, 3rd at Rs. 70000000\n- If you are anywhere between level 1 and 2 and you get a wrong answer,then your home taking money will only be the 1st level money and similarly for level 2 and level 3\n- You can Quit the Game at any Question just by entering (q) instead of other options in (answer section),and if you quit, you will get the money you earned in the question just before the question you Quit\n\n Toh ye rha aapka sawaal Computer Screen par")

for i in range(len(questions)):
    print ("\n\n Question", i+1 ,"for ₹",money[i],"\n\n",questions[i][0],"\n\n",questions[i][1],"\n",questions[i][2],"\n",questions[i][3],"\n",questions[i][4])
    answer = input("Enter option(A/B/C/D)🔒: ")

    # if user wants to quit:-
    if (answer == "q"):
        winning = money[i-1]
        break

    # if the answer is correct:-
    if(answer.upper() == questions[i][5]):
        # winning = money[i]
        print(f"Correct Answer😃\n\nCongratulations!!!!!\n\nYou won ₹ {money[i]}🥲 💵")
        print(questions[i][6])
        if(i == 4):
            winning = 80000
            print("Most Congratulations, You have achieved FIRST major Milestone/Level 1🎁🎁🎉💵🤑💹")
        elif(i == 9):
            winning = 2500000
            print("Most Congratulations, You have achieved SECOND major Milestone/Level 2🎊✨💵🎁🎁")
        elif(i == 14):
            winning = 70000000
            print("Saaaaaaaaaat crooooooooore!!!!!(7 Crores)😮🤯😱😵‍💫 - JACKPOT🤑🤑🤑💰💹🎉🎆🎇🎊✨")
        # telling about next question:-
        if(i < len(questions)-1):
            print("\n\nThe Next Question is for ₹",money[i+1],"😮")

    # if the answer is wrong:-
    else:
        print("\n\nSorry!!!!!\n It's a Wroooong Answer.😔😫😭")
        print("\nThe Correct Answer by Computer Mahaseh is🗝️ 🔓",questions[i][5])
        print(questions[i][6])
        break

print(f"\n\nCongratulations!!\nYour take home money is ₹ {winning}🥳\n\n")


