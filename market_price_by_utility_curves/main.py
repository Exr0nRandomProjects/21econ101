# plan
# always give the next battery to the bestest person
# why? market price means the closest sale to working given the optimal distribution
# and the optimal distribution can be found greedily, by proof by contradiction
# -> suppose it were false. then, you skipped someone all the way till the end, and gave a battery to someone who gained lower utility (and thus would lose less utility than the skipped person would gain from buying). thus, there's a mutually beneficial trade, so this must not be the optimal solution. so you must not have skipped anyone.

# why is the hardware store equivalent? because you are just adding another player whose utility curve is 0. we were told that the initial distribution doesn't for the final total utility, and the hardware store owner won't have any batteries remaining so they don't affect the supply

from queue import PriorityQueue

UTILITY_CURVES = [
    lambda x: 27  - 3  *x,
    lambda x: 50  - 10 *x,
    lambda x: 100 - 20 *x,
    lambda x: 200 - 40 *x,
    lambda x: 18  - 3  *x,
    lambda x: 49  - 7  *x,
    lambda x: 72  - 12 *x,
    lambda x: 64  - 8  *x,
    lambda x: 45  - 9  *x,
    lambda x: 60  - 15 *x,
    lambda x: 35  - 5  *x,
    lambda x: 84  - 14 *x,
    lambda x: 32  - 4  *x,
    lambda x: 35  - 7  *x,
    lambda x: 45  - 5  *x,
    lambda x: 80  - 10 *x,
    lambda x: 50  - 10 *x,
    lambda x: 48  - 8  *x,
    lambda x: 44  - 11 *x
]

def populate_queue():
    pq = PriorityQueue()
    for i, curve in enumerate(UTILITY_CURVES):
        pq.put([-curve(0), i])
    return pq

def simulate():
    num_batteries = [0]*len(UTILITY_CURVES)
    tot_utility = [0]*len(UTILITY_CURVES)
    pq = populate_queue()
    # for n in range(total_batteries):
    while True:
        recent_sale, i = pq.get()
        if recent_sale == 0:
            break

        tot_utility[i] -= recent_sale
        num_batteries[i] += 1
        yield (i, -recent_sale, num_batteries[i], tot_utility[i])
        # print(f"player {i+1:2d} gets battery {n+1:2d} for {-recent_sale:3d}, now has {num_batteries[i]} batteries and {tot_utility[i]:3d} utility.")

        next_gained_util = max(UTILITY_CURVES[i](num_batteries[i]), 0)
        pq.put([-next_gained_util, i])


if __name__ == '__main__':
    # free batteries
    # for i, (player, gain, num, util) in enumerate(simulate()):
    #     print(f"player {player+1:2d} gets battery {i+1:2d} for {gain:3d}, now has {num} batteries and {util:3d} utility.")

    # find best price
    recent_sale = 0
    second_recent_sale = 0
    for i, (player, gain, num, util) in enumerate(simulate()):
        if gain != recent_sale:
            second_recent_sale = recent_sale
        recent_sale = gain
        if i > 50:
            break
        # print(f"player {player+1:2d} gets battery {i+1:2d} for {gain:3d}, now has {num} batteries and {util:3d} utility.")
    print(f"the market price for 50 batteries is between {recent_sale} and {second_recent_sale} utility")

    # find how many
    for i, (player, gain, num, util) in enumerate(simulate()):
        if gain < 40:
            print(f"at 40 utility a battery, you would sell {i} batteries")
            break
