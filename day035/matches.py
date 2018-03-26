options = [
  [
    range(-27, -14),
    range(-14, -11),
    range(-11, -7),
    range(-7, -4),
    range(-4, -0),
    range(0, 6),
    range(6, 28)
  ], [
    range(-26, -4),
    range(-5, -2),
    range(-2, 1),
    range(1, 3),
    range(3, 6),
    range(6, 8),
    range(8, 29)
  ],
  [
    range(-27, -4),
    range(-4, 0),
    range(0, 3),
    range(3, 6),
    range(6, 9),
    range(9, 12),
    range(12, 27)
  ], [
    range(-26, -8),
    range(-8, -4),
    range(-5, -2),
    range(-2, 0),
    range(0, 3),
    range(3, 6),
    range(6, 25)
  ]
]

def matches(answers):
  myArr = []
  for i, a in enumerate(answers):
    for j, ops in enumerate(options[i]):
      if a in ops:
        myArr.append(j + 1)
  return myArr

res = [3, -4, 4, 6]

key = matches(res)
