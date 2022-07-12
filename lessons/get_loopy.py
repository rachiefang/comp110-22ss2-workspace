

def up(haystack: str, needle: str) -> int:
    print("up")
    i: int = 0
    count: int = 0
    while i < len(haystack):
        if haystack [i] == needle:
                count = count + 1
        i = i + 1
    return count

def down(search: str) -> int:
    print("down")
    s: str = ""
    h: int
    i: int = up(search, "w")
    while i>= 0:
        s = s + str(i)
        h = i + 1

        while h < 2:
            s = s +  str(h)
            h = h + 1
        
        i = i - 2

    return s

print (down("wow"))