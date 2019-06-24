#!/usr/bin/python3

proto= ['ssh', 'http', 'https']

protoa= ['ssh', 'http', 'https']
print(proto)

print(proto[1])

#proto.extend('dns')

#print(proto)

#proto.append('dns')

#print(proto)

#proto.extend(["dns"])

#print(proto)


proto.append('dns')
protoa.append('dns')

print(proto)
print(protoa)

proto2= [22, 80, 443, 53] 

proto.extend(proto2)

print(proto2)




