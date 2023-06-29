from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return answer
    
    else:
        visited = [0] * len(words)
        queue = deque([(begin, answer)])
        
        while queue:
            current, level = queue.popleft()
            
            if current == target:
                return level
            
            for i, word in enumerate(words):
                if not visited[i] and sum(c1 != c2 for c1, c2 in zip(current, word)) == 1:
                    visited[i] = 1
                    queue.append((word, level+1))

find_result = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])