morning_batch = {"prince","alok","sagar","kishan"}
evening_batch = {"ravi","shankar","prince","kishan"}

print(f"\nmorning batch: {morning_batch}\nevening batch: {evening_batch}")
print(f"\nstudents present only in one batch not in both batches: {morning_batch.symmetric_difference(evening_batch)}\n")