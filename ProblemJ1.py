# P = 5 * B - 400
print("Input:")
B = int(input()) # boiling point
# inputSeaLevel = int(input()) 
P = (5 * B) - 400

# higher atmospheric pressure = higher boiling point
if P > 100: 
    seaLevel = -1 
elif P < 100:
    seaLevel = 1
else: 
    seaLevel = 0

print(P)
print(seaLevel)





