# Employee Skill Management(OR Skill Menu)

skills = {"coding","leadership","speaking"}
print(f"\nEmployee Skills set: {skills}\n")

print("\n--Employee Skill Management(Menu)--\n1 Add Skill\n2 Delete Skill\n3 Merge New Skills\n4 Show Skills\n5 Exit")

def skill():
    select = int(input("Choose any one no. : "))
    match select:
      case 1:
        n = input("Enter the skill you want to add: ")
        skills.add(n)
        print(f"Skills after adding: {skills}\n")
      case 2:
        m = input("Enter the skill you want to remove: ")
        skills.discard(m)
        print(f"Skills after removing: {skills}\n")
      case 3:
        new_skills = {"singing","dancing","consistency"}
        print(f"New skills set: {new_skills}")
        skills.update(new_skills)
        print(f"(Skills) set after merging  it with (new skills) set: {skills}\n")
      case 4:
        print(f"Showing Skills Set: {skills}\n")
      case 5:
        print("Thank-You\n")
    skill()

skill()