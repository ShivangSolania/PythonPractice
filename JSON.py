from json import JSONDecoder, JSONEncoder
import json
class ComplexEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(z, complex):
            return {z.__class__.__name__: True, "real":z.real, "imag":z.imag}
        # Let the base class default method handle other objects or raise a TypeError
        return JSONEncoder.default(self, o)
z = 5 + 9j
#Method 1
zJSON = json.dumps(z, cls=ComplexEncoder)
print(zJSON)
#Method 2 (use encoder directly):
zJson = ComplexEncoder().encode(z)
print(zJSON)

class CompleDecoder(JSONDecoder):
    def decode_complex(dct):
        if complex.__name__ in dct:
            return complex(dct["real"], dct["imag"])
        return dct

    # Now the object is of type complex after decoding
    z = json.loads(zJSON, object_hook=decode_complex)
    print(type(z))
    print(z)