# tiny-chess-4k: the engine lives in engine.b85 + engine2.b85 (lzma-compressed,
# base85-encoded, split into lines) and is unpacked here at startup.
import base64
import lzma
import os

_d = os.path.dirname(__file__)
blob = ""
for _n in ("engine.b85", "engine2.b85"):
    with open(os.path.join(_d, _n)) as f:
        blob += "".join(line.strip() for line in f)
exec(lzma.decompress(base64.b85decode(blob)))
