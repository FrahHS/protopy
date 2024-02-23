import gzip
import io
from nbt.nbt import NBTFile

b'\n\x00\nhoverEvent\n\x00\x08contents\x08\x00\x04name\x00\x0eCiccioFumaerba\x0b\x00\x02id\x00\x00\x00\x04\xd6\xbe6D\xe0D3\xa4\x85\xf1P\xacI\xdb\x92\xa1\x08\x00\x04type\x00\x10minecraft:player\x00\x08\x00\x06action\x00\x0bshow_entity\x00\n\x00\nclickEvent\x08\x00\x06action\x00\x0fsuggest_command\x08\x00\x05value\x00\x15/tell CiccioFumaerba \x00\x08\x00\tinsertion\x00\x0eCiccioFumaerba\x08\x00\x04text\x00\x0eCiccioFumaerba\x00\x00'

data = b'\n\t\x00\x05extra\x08\x00\x00\x00\x01\x00\x15Kicked by an operator\x08\x00\x04text\x00\x00\x00'

#data = b'\n\x00\x07content' + data
file = io.BytesIO(gzip.compress(data))
nbtfile = NBTFile(fileobj=file)

buffer = io.BytesIO()
nbtfile.write_file(fileobj=buffer)
data = data[len(gzip.decompress(buffer.getvalue())):]

print(nbtfile, data)
