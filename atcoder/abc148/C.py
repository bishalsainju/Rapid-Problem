def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x


inp = input().split()
x = int(inp[0])
y = int(inp[1])

print(int(x*y/compute_gcd(x, y)))
