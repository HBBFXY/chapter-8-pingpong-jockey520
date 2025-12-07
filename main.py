import random

def simulate_one_game(ability_A, ability_B):

    score_A, score_B = 0, 0
    serving = 'A' 
    
    while score_A < 15 and score_B < 15:
        round_prob = random.random()
        
        if serving == 'A':
            if ability_A > round_prob:
                score_A += 1
            else:
                serving = 'B'
        else:
            if ability_B > round_prob:
                score_B += 1

            else:

                serving = 'A'

    if score_A >= 15:
        return 'A'
    else:
        return 'B'

def simulate_matches(ability_A, ability_B, num_matches):

    wins_A, wins_B = 0, 0
    
    for _ in range(num_matches):
        winner = simulate_one_game(ability_A, ability_B)
        if winner == 'A':
            wins_A += 1
        else:
            wins_B += 1
    
    return wins_A, wins_B

def main():

    ability_A = float(input("请输入球员A的能力值(0~1):"))
    ability_B = float(input("请输入球员B的能力值(0~1):"))
    num_matches = int(input("请输入模拟比赛场次："))
    
    if not (0 <= ability_A <= 1 and 0 <= ability_B <= 1):
        print("错误:能力值必须在0到1之间")
        return
    
    if num_matches <= 0:
        print("错误:模拟场次必须大于0")
        return

    wins_A, wins_B = simulate_matches(ability_A, ability_B, num_matches)

    print(f"\n模拟比赛数量:{num_matches}")
    print(f"球员A获胜场次:{wins_A} ({wins_A/num_matches*100:.1f}%)")
    print(f"球员B获胜场次:{wins_B} ({wins_B/num_matches*100:.1f}%)")

if __name__ == "__main__":
    main()
