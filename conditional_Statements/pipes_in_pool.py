v = int(input())
b1 = int(input())
b2 = int(input())
h = float(input())

tube1_ph = b1 * h
tube2_ph = b2 * h
tube = tube1_ph + tube2_ph

total = (tube / v) * 100

pipe1 = tube1_ph / tube * 100
pipe2 = tube2_ph / tube * 100
diff = tube - v
if tube <= v:
  print(f"The pool is {total:.2f}% full. Pipe 1: {pipe1:.2f}%. Pipe 2: {pipe2:.2f}%.")
else:
  print(f"For {h:.2f} hours the pool overflows with {diff} liters.")