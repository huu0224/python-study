def get_spell_from_index(idx):
    """
    0부터 시작하는 전체 인덱스를 규칙에 맞는 문자열로 변환합니다.
    """
    length = 1
    count = 26

    # 1. 문자열의 길이를 결정합니다.
    while idx >= count:
        idx -= count
        length += 1
        count = 26 ** length

    # 2. 해당 길이 내에서 몇 번째인지(idx)를 가지고 문자열을 생성합니다.
    res = []
    for i in range(length - 1, -1, -1):
        res.append(chr(ord('a') + (idx // (26 ** i))))
        idx %= (26 ** i)
    return "".join(res)


def get_index_from_spell(spell):
    """
    문자열을 규칙에 따른 0부터 시작하는 인덱스로 변환합니다.
    """
    length = len(spell)
    idx = 0
    # 짧은 길이의 문자열 개수를 모두 더함
    for i in range(1, length):
        idx += 26 ** i

    # 같은 길이 내에서 사전 순서 계산
    for i, char in enumerate(spell):
        power = length - 1 - i
        idx += (ord(char) - ord('a')) * (26 ** power)
    return idx


def solution(n, bans):
    # 1. n은 1-based index이므로 계산 편의를 위해 0-based로 변경
    target_n = n - 1

    # 2. 삭제된 주문들을 인덱스로 변환하여 정렬
    ban_indices = sorted([get_index_from_spell(b) for b in bans])

    # 3. 삭제된 주문이 타겟 인덱스 이전에 있다면 target_n을 뒤로 미룸
    # target_n이 변함에 따라 새롭게 포함되는 금지어도 체크해야 함
    for b_idx in ban_indices:
        if b_idx <= target_n:
            target_n += 1
        else:
            # ban_indices는 정렬되어 있으므로, 이후 값들은 target_n보다 큼
            break

    return get_spell_from_index(target_n)