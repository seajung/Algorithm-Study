def solution(genres, plays):
    answer = []

    genre_total_play = {}
    genre_musics = { }

    for i,genre in enumerate(genres):
        play = plays[i]
        if genre in genre_total_play:
            genre_total_play[genre] += play
            genre_musics[genre].append((play, i))
        else:
            genre_total_play[genre] = play
            genre_musics[genre] = [(play, i)]
            
        
    genreSort = sorted(genre_total_play.items(), key=lambda x: x[1], reverse=True)
    
    for (genre, totalPlay) in genreSort:
        genre_musics[genre] = sorted(genre_musics[genre], key=lambda x: (-x[0], x[1]))
        answer += [ i for (play, i) in genre_musics[genre][:2] ]
        
    return answer