def sub(x, y, z, cost):
    users = [("Алиса", x), ("Боб", y), ("Чарли", z)]
    # Сортируем список пользователей по количеству денег в обратном порядке
    users.sort(key=lambda user: user[1], reverse=True)
    for i in range(len(users)):
        for j in range(i + 1, len(users)):
            if users[i][1] + users[j][1] >= cost:
                return (users[i][0], users[j][0])
    return None
x = 20
y = 30
z = 50
cost = 45
result = sub(x, y, z, cost)
if result is None:
    print("Никакие два пользователи не могут купить подписку на Netflix")
else:
    print(f"Купят подписку пользователи {result[0]} и {result[1]}")