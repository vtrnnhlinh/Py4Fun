width = input("Flag width:\n")
width = int(width)
height = input("Flag height:\n")
height = int(height)
# Put the rest of your code here!
midHeight = (int)(height/2)
midStar = (int)(width/2)
star = '#' * midStar
dash = '-' * (width-midStar)
for i in range(midHeight):
    print(star+dash)
for x in range((height-midHeight)):
    print(dash+dash)1