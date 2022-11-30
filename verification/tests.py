"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [""],
            "answer": "",
        },
        {
            "input": ["Django framework"],
            "answer": '''Django
framework''',
        },
        {
            "input": ["Zen of Python"],
            "answer": '''Zen
of
Python _''',
        },
        {
            "input": ["There are three kinds of lies: Lies, damned lies, and the benchmarks."],
            "answer": '''There
are
three kinds
of lies: Lies,
damned lies, and the benchmarks.''',
        },
    ],
    "Extra": [
        {
            "input": ["Python"],
            "answer": "Python",
        },
        {
            "input": ["How did the programmer die in the shower? He read the shampoo bottle instructions: Lather. Rinse. Repeat."],
            "answer": '''How
did
the programmer
die in the
shower? He read the shampoo
bottle instructions: Lather. Rinse. Repeat. _ _ _''',
        },
        {
            "input": ['''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea-- let's do more of those!'''],
            "answer": '''Beautiful
is
better than
ugly. Explicit is
better than implicit. Simple is
better than complex. Complex is better than complicated.
Flat is better than nested. Sparse is better than dense. Readability counts. Special
cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In
the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch.
Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea-- let's do more of those! _ _ _ _ _ _ _''',
        },
    ]
}
