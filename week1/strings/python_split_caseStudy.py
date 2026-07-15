"""
Let’s look at a highly practical, industrial case study.

The Scenario: You are building an automated analytics dashboard. Your server produces raw log files. You need to parse each log line to extract:
1.The Timestamp
2.The Log Level (INFO, ERROR, WARNING)
3.The Message
The Raw Log Format:
"2026-07-14 10:26:35 [ERROR] Database connection failed to host 10.0.0.5"

"""

#The Naive Approach (And why it fails)
#If you try to split simply by spaces:
#log = "2026-07-14 10:26:35 [ERROR] Database connection failed to host 10.0.0.5"
# parts = log.split(" ")
#Because the actual message "Database connection failed to host 10.0.0.5" contains spaces, 
# your message gets shattered into 6 different list items.
#  Reconstructing it is messy and slow.

#========The Production-Grade Solution (Using maxsplit)=========

def parse_log_line(raw_log: str) -> dict:
    # We want to split by spaces, but only make 3 cuts:
    # Cut 1: Separates Date from Time
    # Cut 2: Separates Time from Log Level
    # Cut 3: Separates Log Level from the rest of the Message
    parts = raw_log.split(" ", 3)
    
    # If the log is malformed, handle it gracefully
    if len(parts) < 4:
        return {"error": "Malformed log line"}
        
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2].strip("[]"), # Clean up the brackets using strip!
        "message": parts[3]
    }

# Test the system
raw_line = "2026-07-14 10:26:35 [ERROR] Database connection failed to host 10.0.0.5"
parsed_data = parse_log_line(raw_line)

import json
print(json.dumps(parsed_data, indent=2))

#=====expected output=====
# {
#   "date": "2026-07-14",
#   "time": "10:26:35",
#   "level": "ERROR",
#   "message": "Database connection failed to host 10.0.0.5"
# }