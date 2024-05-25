def count_overlapping_intervals(N, intervals):
    events = []
    for l, r in intervals:
        events.append((l, 1))  # 区間の開始を表すイベント
        events.append((r + 1, -1))  # 区間の終了を表すイベント（重ならないようにr+1）

    # イベントをソート（位置が同じ場合、終了イベントを先に処理）
    events.sort()

    count = 0
    active_intervals = 0

    for pos, event_type in events:
        if event_type == 1:
            active_intervals += 1
        elif event_type == -1:
            active_intervals -= 1
        # active_intervalsが2以上のとき、重なりがある
        if event_type == 1:
            count += active_intervals - 1

    return count

# 入力の読み込み
N = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(N)]

# 結果の出力
result = count_overlapping_intervals(N, intervals)
print(result)
