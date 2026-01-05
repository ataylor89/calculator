expressions = '''

1/0
1/-0
1+
%
+
1+2/
-
_
**
^

'''

def test_data():
    data = []
    for line in expressions.split('\n'):
        line = line.strip()
        if line:
            data.append(line)
    return data
