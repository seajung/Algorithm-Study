# 시간복잡도 O(nlogn)
# n: song의 개수 (len(genres))
# m: genre의 개수 (len(total_plays_in_genre))
# m < n (m<100)

def solution(genres, plays):
    answer = []
    song_dict = {}  # {genre: list of (idx, plays)}
    total_plays_in_genre = {}   # {genre: total plays}
    
    # dictionary 에 값 넣어주기
    for idx, genre in enumerate(genres):    #O(n)
        if genre not in song_dict.keys():   #O(1)
            song_dict[genre] = [(idx, plays[idx])]  #O(1)
            total_plays_in_genre[genre] = plays[idx]    
        else:
            song_dict[genre].append((idx, plays[idx]))  #O(1)
            total_plays_in_genre[genre] += plays[idx]   
    
    # 총 재생 많이 된 장르 순으로 정렬
    total_lst = list(total_plays_in_genre.items())
    total_lst.sort(key = lambda x: -x[1])   # O(mlogm)-->O(nlogn)
    
    # 장르 별로 노래 수록하기
    for tup in total_lst:
        lst_in_genre = song_dict[tup[0]]      
        for i in range(len(lst_in_genre)):
            max_song = max(lst_in_genre, key = lambda x: (x[1], -x[0]))
            lst_in_genre.remove(max_song)
            answer.append(max_song[0])
            if i == 1: 
                break
        
    return answer

# testcase
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))
# [4, 1, 3, 0]