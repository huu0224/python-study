def solution(s, query):
    # s의 각 문자 인덱스(1부터 시작)가 어느 그룹 ID에 속하는지 관리
    parent = {i + 1: 0 for i in range(len(s))}

    # group_map: {그룹ID: {인덱스 집합}}
    group_map = {0: set(range(1, len(s) + 1))}

    # creation_order: {그룹ID: 생성순서}
    creation_order = {0: 0}

    next_group_id = 1
    answer = []  # 변수명을 answer로 수정

    for q in query:
        parts = q.split()
        q_type = int(parts[0])

        if q_type == 1:
            x, y = int(parts[1]), int(parts[2])
            answer.append("YES" if parent[x] == parent[y] else "NO")

        elif q_type == 2:
            x, word = int(parts[1]), parts[2]
            target_gid = parent[x]
            extracted = extract_chars(s, group_map, creation_order, parent, word, [target_gid])
            if extracted:
                add_group(group_map, creation_order, parent, extracted, next_group_id)
                next_group_id += 1

        elif q_type == 3:
            x, y, word = int(parts[1]), int(parts[2]), parts[3]
            extracted = extract_chars(s, group_map, creation_order, parent, word, list(group_map.keys()), x, y)
            if extracted:
                add_group(group_map, creation_order, parent, extracted, next_group_id)
                next_group_id += 1

        elif q_type == 4:
            x, y = int(parts[1]), int(parts[2])
            gid1, gid2 = parent[x], parent[y]
            if gid1 != gid2:
                early, late = (gid1, gid2) if creation_order[gid1] < creation_order[gid2] else (gid2, gid1)
                for idx in group_map[late]:
                    parent[idx] = early
                    group_map[early].add(idx)
                del group_map[late]
                del creation_order[late]

        elif q_type == 5:
            sorted_gids = sorted(group_map.keys(), key=lambda gid: creation_order[gid])
            for gid in sorted_gids:
                counts = {}
                for idx in group_map[gid]:
                    char = s[idx - 1]
                    counts[char] = counts.get(char, 0) + 1

                alphabet_comp = []
                for char in sorted(counts.keys()):
                    alphabet_comp.append(f"{char} {counts[char]}")
                answer.append(" ".join(alphabet_comp))

    return answer


def extract_chars(s, group_map, creation_order, parent, word, target_gids, start=None, end=None):
    needed = {}
    for char in word:
        needed[char] = needed.get(char, 0) + 1

    extracted = []
    for gid in target_gids:
        if gid not in group_map: continue
        indices = sorted(list(group_map[gid]))
        for idx in indices:
            if start and (idx < start or idx > end): continue
            char = s[idx - 1]
            if needed.get(char, 0) > 0:
                extracted.append(idx)
                needed[char] -= 1
                group_map[gid].remove(idx)
        if not group_map[gid]:
            del group_map[gid]
            del creation_order[gid]
    return extracted


def add_group(group_map, creation_order, parent, indices, new_id):
    group_map[new_id] = set(indices)
    creation_order[new_id] = new_id
    for idx in indices:
        parent[idx] = new_id


# --- 테스트 실행 (오류가 났던 부분) ---
if __name__ == "__main__":
    # 따옴표와 괄호를 정확히 닫았는지 확인하세요!
    print(solution("abacadae", ["3 1 4 aa", "1 1 5", "4 1 7", "1 1 5", "5"]))