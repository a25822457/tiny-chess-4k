# tiny-chess-4k: the engine lives in engine.b85 (lzma-compressed,
# base85-encoded, split into lines) and is unpacked here at startup.
import base64
import lzma
import os

with open(os.path.join(os.path.dirname(__file__), "engine.b85")) as f:
    blob = "".join(line.strip() for line in f)
exec(lzma.decompress(base64.b85decode(blob)))
