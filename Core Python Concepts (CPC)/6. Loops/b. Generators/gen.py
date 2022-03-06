def gen(samples):
    count = 0
    while True:
        yield count
        count += 1
        try: count = samples
        except: pass

a = gen(10)
while True:
    try: print(next(a))
    except: break
