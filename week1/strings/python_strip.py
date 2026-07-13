#.strip(): This function removes the leading and trailing whitespaces or characters from strings

def whitespaces():
    val:str = "    Hello Google  "
    print(f"Before strip call: {val}")
    clean_val = val.strip()
    print(f"After strip call: {clean_val}")

whitespaces()

#.strip(characters)
# Parameter values: If you want to remove a set of characters from the beginning 
# or from the end of the string, you can pass them as parameters
# for instance:

def remove_characters():
    name:str = ",,,,AIENG Musharaf Hussain,,,"
    print(f"Name before .strip call: {name}")
    clean_name = name.strip(",GNEIAMn")
    print(f"Name after .strip call: {clean_name}")    

remove_characters()

def industrial_usecases():
    #1. Cleaning Up User Input (The "Fat Finger" Defense)
    submitted_email = " musharaf@google.com  "
    clean_email = submitted_email.strip()
    print(f"cleaned_email before storing in DB: {clean_email}")

    #2. Processing Data from Files or APIs (CSV/JSON Logs)
    #3. Parsing URL Query Parameters
    #Example 1: Standardizing API Endpoints (Trimming Trailing Slashes)
    #developers frequently run into the "trailing slash" problem.
    #  A user or an automated script might request [https://api.google.com/v1/users/]
    #while the server expects [https://api.google.com/v1/users](https://api.google.com/v1/users).
    #To prevent routing errors, developers use .rstrip("/") to ensure the endpoint is clean.
    def handle_request(url_path: str):
        # url_path might come in as "/v1/users/" or "/v1/users"
        # .rstrip("/") strips '/' only from the right side
        clean_path = url_path.rstrip("/")
        
        print(f"Routing to: {clean_path}")

    handle_request("/v1/users/")  # Output: Routing to: /v1/users
    handle_request("/v1/users")   # Output: Routing to: /v1/users

    #Example 2: Cleaning Messy Query Parameter Strings
    # A messy raw query string pulled from an incoming HTTP request
    raw_query = " ?utm_source=google&utm_medium=cpc&? "
    # 1. strip() removes the wrapping spaces
    # 2. lstrip("?") removes the starting '?' if it exists
    clean_query = raw_query.strip().lstrip("?").rstrip("?&")
    print(f"Clean query: '{clean_query}'")
    # Now it's perfectly clean and ready to be safely parsed!
    try:
        params = dict(item.split("=") for item in clean_query.split("&"))
        print(params)
    except:
        print(ValueError)
    #Example 3: Parsing Path Parameters safely
    url_endpoint = " /items/45021/ "

    # Clean up outer spaces, split by the slashes, and filter out empties
    path_segments = [seg for seg in url_endpoint.strip().split("/") if seg]

    # Extracting the last parameter (the item ID)
    item_id = path_segments[-1]
    print(f"Extracted ID: {item_id}")

industrial_usecases()




#Indusrial Best practices for when to use .strip() and when not to use it
#1. The Performance Danger of Heavy Stripping
"""
-> Bad Habit: Stripping a string over and over down a pipeline.

-> Pro Approach: Clean the string once as soon as it enters your system, and pass the clean version around.

"""

#2. The Order of Execution (It doesn't care about your order)
#When you pass a set of characters to strip, 
# the order you write them in does not matter at all.
text = "www.google.com"

# Both of these do the EXACT same thing:
print(text.strip("w."))   # Output: google.com
print(text.strip(".w"))   # Output: google.com

"""3. The removesuffix / removeprefix Alternative"""
#If you want to remove an exact phrase from the end of a string (like a file extension or a specific word),
#  .rstrip() will eventually bite you.
filename = "protocol.log"

# The Junior mistake:
clean_name = filename.rstrip(".log")
print(f"using .rstrip: {clean_name}") 
# Expected: "protocol"
# Actual Output: "protoc"  <-- Wait, where did the 'log' in 'error_log' go?!
#Because .rstrip(".log") doesn't look for the word ".log".
#  It looks for ., l, o, and g. After it ate the extension, 
# it kept moving left, saw the g, o, and l in the word _log_, and ate those too!

"""Always use .removesuffix() or .removeprefix() when dealing with whole words or exact strings."""
clean_name = filename.removesuffix(".log")
print(f"using .removesuffix: {clean_name}")  # Output: protocol (Perfect!)