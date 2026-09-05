# Binary File Read/Write
# wb → write bytes
# rb → read bytes

# if text: "Hello"
# then its binary: b"Hello"


data = b"Python Binary data"

with open("data.bin","wb")as file:
    file.write(data)

print("Binary file written successfully")

with open("data.bin", "rb") as file:
    result = file.read()

print("Read text:",result)