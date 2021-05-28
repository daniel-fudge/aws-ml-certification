import base64


def print_base64(base64_string):
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    print(sample_string)


data = 'eyJGSVJTVCI6IkdlcGtlIiwiTEFTVCI6IlZhbiBXb3VkZW5iZXJnIiwiQUdFIjozNSwiR0VOREVSIjoiZmVtYWxlIiwiTEFUSVRVREUiOjQuMDYyNywiTE9OR0lUVURFIjotNzcuNzAwOH0='
data_string = base64.b64decode(data.encode("ascii")).decode("ascii") + '\n'

data_new = base64.b64encode(data_string.encode("ascii")).decode("ascii")

print_base64(data_new)

