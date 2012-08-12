#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys, random

# 試行回数
AVG_TRIALS = 10

"""
M枚分割されているコンプガチャ1枚を、
単純に出現率の少ないスーパーレアカード1枚に移行したとき、
損にならない程度の出現確率を求める
"""
def main(part):
    # ガチャコンプリートまでの平均回数を求める
    cnt = 0
    for i in range(0, AVG_TRIALS):
        cnt += getCompGachaCount(part)

    # ガチャコンプリート平均回数
    comp_times = cnt / AVG_TRIALS

    # 上で求めた回数回したとして、ギリギリ出現する程度になる
    # スーパーレアカードの平均確率を求める
    cnt = 0.00
    for i in range(0, AVG_TRIALS):
        cnt += getSuperRareOdds(comp_times)

    # 対応するスーパーレアの確率"
    s_rare_odds = cnt / AVG_TRIALS

    return (comp_times, s_rare_odds)


'''
part 枚分割のガチャをコンプするのに必要な回数を求める
'''
def getCompGachaCount(part):
    # 分割カードを準備
    p = (int)(part)
    list = [False] * p  # 初期状態
    comp = [True] * p   # コンプ状態

    # 全部コンプするまで回す
    cnt = 0
    while(list != comp):
        i = random.randint(0, part - 1)
        list[i] = True
        cnt += 1

    return cnt


'''
times 回数回してギリギリ出現する程度のスーパーレアカードの
確率を求める
'''
def getSuperRareOdds(times):
    i = 0
    # 10%から0.1%刻みで減らしていく
    ### ここのメソッドもっといい方法ないか？
    odds = 0.1
    while(True):
        i += 1
        # レアカードが出現した場合
        if (random.random() <= odds):
            odds -= 0.01
            i = 0
            continue

        # 規定回数回しきった場合、その時の確率値を返す
        if times <= i:
            return odds


# main method
if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    if (argc != 3):
        print 'usage: python %s [part] [trials]' % argv[0]
        quit()

    part = (int)(argv[1])
    AVG_TRIALS = (int)(argv[2])

    timesum = 0.0
    s_raresum = 0.0
    for i in range(0, AVG_TRIALS):
        times, s_rare = main(part)
        timesum += times
        s_raresum += s_rare

    print "試行 %d回" % AVG_TRIALS
    print "ガチャコンプ平均回数 %f回" % (float)(timesum / AVG_TRIALS)
    print "対応スーパーレア平均確率 %g" % (float)(s_raresum / AVG_TRIALS)


