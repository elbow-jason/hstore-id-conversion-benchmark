import timeit
import json

data = [1,2,3,45,55555, 5123,3123123,54,13123,51,4124]
excludes = {' ', ',', '[', ']'}

# This will not work with hstore due to arrays of differing sizes DataError.
# to_string['list_of_str']    = '[str(x) for x in {}]'

to_string = {}
to_string['baseline']       = "pass"
to_string['json_dumps']     = 'json.dumps({})'
to_string['join_on_space']  = '" ".join([str(x) for x in {}])'
to_string['list_to_str']    = 'str({})'

from_string = {}
from_string['baseline']     = "pass"
from_string['json_loads']   = 'json.loads("{}")'
from_string['set_to_list']  = 'list(set("{}").symmetric_difference(excludes))'


def avg(val):
    return sum(val)/len(val)

def time_code(code):
    results = timeit.Timer(code, setup="from __main__ import json, excludes;").repeat(3)
    return avg(results)

def pprint(key, val, base):
    print ("%15s {:10.4f}sec" % key).format(val-base)

to_string_results = {}
for key, template in to_string.items():
    print "starting", key
    to_string_results[key] = time_code(template.format(data))
to_string_base = to_string_results.pop('baseline')


from_string_results = {}
for key, template in from_string.items():
    print "starting", key
    from_string_results[key] = time_code(template.format(data))
from_string_base = from_string_results.pop('baseline')


print "\n=== TO STRING RESULTS ==="
pprint('baseline', to_string_base, 0)
for item, val in to_string_results.items():
    pprint(item, val, to_string_base)

print "\n=== FROM STRING RESULTS ==="
pprint('baseline', from_string_base, 0)
for item, val in from_string_results.items():
    pprint(item, val, from_string_base)

print "\n"
