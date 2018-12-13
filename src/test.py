def test(health_min, health_max, health_cur):
    _min = min(health_min, -health_min)
    _max = max(health_max, -health_max)
    _cur = min(max(health_cur, _min), _max)

    res = _min <= _cur and _cur <= _max
    print(str(res) + ' ' + str((_min, _cur, _max)))

test(-2,  2,  1)
test( 2,  2,  1)
test( 2, -2,  1)
test( 2,  2,  3)
test( 2,  2, -3)

dic = {'test': 0, 'dada': 1}
print(dic[0])