# Find The Runner Up Score Program : 
if __name__ == '__main__':
    
    n = int(input())
    
    arr = map(int, input().split())  
    
    
    scores = list(set(arr))   
    
    
    scores.sort(reverse=True)
    
    runner_up_score = scores[1]
    
    print(runner_up_score)