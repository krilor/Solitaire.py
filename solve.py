import solitaire as sol

soli = sol.Solitaire()
result = 0

for i in xrange(1000000000):
  result = soli.solve()
  if result < 5:
    print result
  soli.reset()
