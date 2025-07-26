import pandas as pd
import numpy as np
import random

np.random.seed(42)
random.seed(42)

# 1️⃣ Define hobbies & music lists
HOBBIES = ['Travel', 'Sports', 'Movies', 'Gaming', 'Reading', 'Cooking', 'Music', 'Dancing', 'Hiking', 'Photography']
MUSIC = ['Pop', 'Rock', 'Classical', 'EDM', 'Jazz']

# 2️⃣ Create 2000 fake people (larger pool)
people = []
for i in range(2000):
    age = np.random.normal(28, 5)
    age = max(18, min(40, age))

    income = np.random.normal(5000, 2000)
    income = max(2000, min(12000, income))

    spending_style = np.random.choice([0, 1], p=[0.7, 0.3])
    personality = np.random.choice([0, 1])
    is_planner = np.random.choice([0, 1], p=[0.4, 0.6])
    savings_focus = np.random.choice([0, 1], p=[0.7, 0.3])

    hobbies = random.sample(HOBBIES, k=np.random.randint(2, 5))
    music = random.sample(MUSIC, k=np.random.randint(1, 3))

    people.append({
        'PersonID': i,
        'Age': int(age),
        'Income': int(income),
        'SpendingStyle': spending_style,
        'Personality': personality,
        'IsPlanner': is_planner,
        'SavingsFocus': savings_focus,
        'Hobbies': hobbies,
        'Music': music
    })

people_df = pd.DataFrame(people)
print(f"✅ Created {len(people_df)} fake people")

# 3️⃣ Make 10,000 random pairs
pairs = []
for _ in range(10000):
    a, b = np.random.choice(people, 2, replace=False)

    age_gap = abs(a['Age'] - b['Age'])
    income_gap = abs(a['Income'] - b['Income'])
    same_spending = int(a['SpendingStyle'] == b['SpendingStyle'])
    same_personality = int(a['Personality'] == b['Personality'])
    same_planner = int(a['IsPlanner'] == b['IsPlanner'])

    shared_hobbies = len(set(a['Hobbies']).intersection(b['Hobbies']))
    shared_music = len(set(a['Music']).intersection(b['Music']))

    compat = (
        (1 - age_gap / 25) * 0.2 +
        (1 - income_gap / 10000) * 0.2 +
        (shared_hobbies / len(HOBBIES)) * 0.3 +
        (shared_music / len(MUSIC)) * 0.1 +
        same_personality * 0.1 +
        same_spending * 0.1
    )

    label = 1 if compat > 0.5 else 0

    pairs.append({
        'AgeGap': age_gap,
        'IncomeGap': income_gap,
        'SameSpending': same_spending,
        'SamePersonality': same_personality,
        'SamePlanner': same_planner,
        'SharedHobbies': shared_hobbies,
        'SharedMusic': shared_music,
        'GoodFriends': label
    })

pairs_df = pd.DataFrame(pairs)
print(f"✅ Created {len(pairs_df)} pairs")
print(pairs_df.head())

pairs_df.to_csv('friendship_pairs.csv', index=False)
print("\n✅ Saved to friendship_pairs.csv ✅")
