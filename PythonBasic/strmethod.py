# str method

name = 'leeSUNGhyun'

print("upper:",name.upper()) # upper: LEESUNGHYUN
print("lower:",name.lower()) # lower: leesunghyun
print("replace(sung,bun):",name.replace('SUNG','BUN')) # replace(sung,bun): leeBUNhyun
print("split(g):",name.split('G')) # split(g): ['leeSUN', 'hyun'] -> 리스트로 반환

cls = 'Full stack'

print("join:",name.join(cls)) # join: FleeSUNGhyunuleeSUNGhyunlleeSUNGhyunlleeSUNGhyun leeSUNGhyunsleeSUNGhyuntleeSUNGhyunaleeSUNGhyuncleeSUNGhyunk

print("strip:",cls.strip('Fk')) # strip: ull stac
print("lstrip:",cls.lstrip('F')) # lstrip: ull stack
print("rstrip:",cls.rstrip('k')) # rstrip: Full stac

print("find:",cls.find('tac')) # find: 6
print("count:",cls.count('l')) # count: 2

