import random

def simulate_one_game(ability_A, ability_B):
    """
    模拟一局比赛
    返回赢家 'A' 或 'B'
    """
    score_A, score_B = 0, 0
    serving = 'A'  # A先发球
    
    while score_A < 15 and score_B < 15:
        # 生成回合随机概率值
        round_prob = random.random()
        
        if serving == 'A':
            # A发球回合
            if ability_A > round_prob:
                # A赢得回合，得分并继续发球
                score_A += 1
                # 发球权不变（还是A发球）
            else:
                # A输掉回合，交换发球权
                serving = 'B'
        else:
            # B发球回合
            if ability_B > round_prob:
                # B赢得回合，得分并继续发球
                score_B += 1
                # 发球权不变（还是B发球）
            else:
                # B输掉回合，交换发球权
                serving = 'A'
    
    # 判断胜者
    if score_A >= 15:
        return 'A'
    else:
        return 'B'

def simulate_matches(ability_A, ability_B, num_matches):
    """
    模拟多场比赛
    返回A和B的获胜次数
    """
    wins_A, wins_B = 0, 0
    
    for _ in range(num_matches):
        winner = simulate_one_game(ability_A, ability_B)
        if winner == 'A':
            wins_A += 1
        else:
            wins_B += 1
    
    return wins_A, wins_B

def main():
    # 输入
    ability_A = float(input("请输入球员A的能力值（0~1）："))
    ability_B = float(input("请输入球员B的能力值（0~1）："))
    num_matches = int(input("请输入模拟比赛场次："))
    
    # 验证输入
    if not (0 <= ability_A <= 1 and 0 <= ability_B <= 1):
        print("错误：能力值必须在0到1之间")
        return
    
    if num_matches <= 0:
        print("错误：模拟场次必须大于0")
        return
    
    # 处理：模拟比赛
    wins_A, wins_B = simulate_matches(ability_A, ability_B, num_matches)
    
    # 输出
    print(f"\n模拟比赛数量：{num_matches}")
    print(f"球员A获胜场次：{wins_A} ({wins_A/num_matches*100:.1f}%)")
    print(f"球员B获胜场次：{wins_B} ({wins_B/num_matches*100:.1f}%)")

if __name__ == "__main__":
    main()
