# Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the array.

# For example: ["3:1", "2:2", "0:1", ...]

# Write a function that takes such list and counts the points of our team in the championship. Rules for counting points for each match:

# if x>y - 3 points
# if x<y - 0 point
# if x=y - 1 point
# Notes:

# there are 10 matches in the championship
# 0 <= x <= 4
# 0 <= y <= 4

def points(games):
    count = 0
    for points in games:
        if points[0] > points[2]:
            count += 3
        elif points[0] == points[2]:
            count += 1
    
    return count


# Notes: Read the directions. I was trying to do something a lot harder than the 
# actual problem cause I didn't read the directions carefully