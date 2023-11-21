def solution(picks, minerals):
    def solve(picks, minerals, fatigue):
        print(f'picks={picks},minerals={minerals},fatigue={fatigue}')
        if sum(picks) == 0 or len(minerals) == 0:
            return fatigue
        result = [float('inf')]
        for i, fatigues in enumerate(({"diamond": 1, "iron": 1, "stone": 1},
                                      {"diamond": 5, "iron": 1, "stone": 1},
                                      {"diamond": 25, "iron": 5, "stone": 1},)):
            print(f'i={i},fatigues={fatigues}')
            if picks[i] > 0:
                temp_picks = picks.copy()
                print(f'temp_picks={temp_picks}')
                temp_picks[i] -= 1
                result.append(
                    solve(temp_picks, minerals[5:], fatigue + sum(fatigues[mineral] for mineral in minerals[:5])))
        return min(result)

    return solve(picks, minerals, 0)


#picks = [1,3,2]
picks = [0,1,1]
#minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]

print(solution(picks,minerals))
