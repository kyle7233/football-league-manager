# 축구 리그 승점 관리 프로그램

league_name = input("리그 이름을 입력하세요: ")

teams = []

team_count = int(input("팀 수를 입력하세요: "))

for i in range(team_count):
    print(f"\n[{i + 1}번째 팀 정보 입력]")

    name = input("팀 이름: ")
    win = int(input("승: "))
    draw = int(input("무: "))
    lose = int(input("패: "))

    games = win + draw + lose
    points = win * 3 + draw

    team = {
        "name": name,
        "games": games,
        "win": win,
        "draw": draw,
        "lose": lose,
        "points": points
    }

    teams.append(team)


teams.sort(
    key=lambda x: (x["points"], x["win"]),
    reverse=True
)

print("\n" + "=" * 60)
print(f"{league_name + ' 순위표':^60}")
print("=" * 60)

print("순위 | 팀명 | 경기 | 승 | 무 | 패 | 승점")
print("-" * 60)

for i, team in enumerate(teams):
    print(
        f"{i + 1}위 | "
        f"{team['name']} | "
        f"{team['games']} | "
        f"{team['win']} | "
        f"{team['draw']} | "
        f"{team['lose']} | "
        f"{team['points']}"
    )

print("=" * 60)
