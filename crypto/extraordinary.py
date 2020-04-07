'''
import binascii


k = b'6\x1d\x0cT*\x12\x18V\x05\x13c1R\x07u#\x021Jq\x05\x02n\x03t%1\\\x04@V7P\\\x17aN'
k=binascii.hexlify(k)
#k=int(k,16)
print(len(k))


a_string = b'\x00\x14\x02\x15\x07\x1a\x0fR\x17R3>\x13R4\x12R>\x18Q\x143>Q5\x11>YVS\x17\x02YXVS\x1c'
k=binascii.hexlify(a_string)
#k=int(k,16)
print(len(k))

A_string = b' 4"5\':/r7r\x13\x1e3r\x142r\x1e8q4\x13\x1eq\x151\x1eyvs7"yxvs<'
k=binascii.hexlify(A_string)
#k=int(k,16)
print(len(k))

num_string = b'QESDVK^\x03F\x03boB\x03eC\x03oIEbo'
k=binascii.hexlify(num_string)
print(len(k))
'''