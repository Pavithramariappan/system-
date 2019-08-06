x=[[12,7,3],[4,5,6],[6,8,4]]
y=[[4,6,9],[6,5,0],[1,9,2]]
res=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
  for j in range(len(x[0])):
    res[i][j]=x[i][j]+y[i][j]
for r in res:
  print(r)
