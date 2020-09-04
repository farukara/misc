import re

with open("README2.md", "r") as f:
    with open("README3.md", "w") as g:
        for line in f:
            finder = re.compile(r'(Problem .)( - Project Euler)')
            mo = finder.sub(r'\1', line)
            g.write(mo)
            
    
