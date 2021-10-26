# https://www.codewars.com/kata/5e41c408b72541002eda0982
# Multi Line Task: Hello World (Easy One)

# First Implementation 04/10/2021
f\
=\
t(
""
,
()
,{
"\
_\
_\
n\
e\
w\
_\
_\
":
k(
"\
H\
e\
l\
l\
o\
,\
 \
w\
o\
r\
l\
d\
!\
")
})

# --------------------

# actual readeable answer
t = type
k = lambda x: lambda _: x

f = t("", (), {"__new__":k("Hello, world!")})

# f is a new class of name ""
# the __new__ function of this class is the function lambda _: "Hello, world!"
# when we call f() the __new__ function is called, returning "Hello, world!"
