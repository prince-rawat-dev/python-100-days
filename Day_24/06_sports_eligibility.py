sports_team = {"prince","sagar","alok","kishan","angad","bajrangi","ram","keshav","rohit","divyanshu"}
cricket_team = {"alok","prince","sagar","kishan"}
football_team = {"kishan","bholu","jai"}

print(f"\nSports team: {sports_team}\nCricket team: {cricket_team}\nFootball team: {football_team}")
print(f"\nFootball Team ⊆ Sports Team: {football_team.issubset(sports_team)}\nCricket Team ⊆ Sports Team: {cricket_team.issubset(sports_team)}\n")