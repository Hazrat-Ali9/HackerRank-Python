 # Time Delta 
from datetime import datetime, timedelta

def time_delta(t1, t2):
    
    format_str = "%a %d %b %Y %H:%M:%S %z"
    time1 = datetime.strptime(t1, format_str)
    time2 = datetime.strptime(t2, format_str)

    
    time_difference = abs(int((time1 - time2).total_seconds()))

    return time_difference

if __name__ == "__main__":
    
    t = int(input().strip())

    for _ in range(t):
        
        timestamp1 = input().strip()
        timestamp2 = input().strip()

        
        result = time_delta(timestamp1, timestamp2)
        print(result)