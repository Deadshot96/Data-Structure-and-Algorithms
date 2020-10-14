from stack import StackWithList

def html_tag_checker(raw: str) -> bool:
    S = StackWithList()
    i = raw.find('<')
    if i == -1:
        return True

    while i != -1:
        j = raw.find('>', i + 1)
        if j == -1:
            return False

        tag = raw[i + 1 : j]
        if not tag.startswith('/'):
            S.push(tag)

        else:
            if S.isEmpty():
                return False
            
            if tag[1:] != S.pop():
                return False
        i = raw.find('<', j + 1)

    return S.isEmpty()

if __name__ == "__main__":
    raw = """
<body>
<center>
<h1> The Little Boat </h1>
</center>
<p> The storm tossed the little
boat like a cheap sneaker in an
old washing machine. The three
drunken fishermen were used to
such treatment, of course, but
not the tree salesman, who even as
a stowaway now felt that he
had overpaid for the voyage. </p>
<ol>
<li> Will the salesman die? </li>
<li> What color is the boat? </li>
<li> And what about Naomi? </li>
</ol>
</body>
"""
    print(html_tag_checker(raw))