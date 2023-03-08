import struct


class SHA256:
    def __init__(self) -> None:
        self.K = [
            0x428A2F98,
            0x71374491,
            0xB5C0FBCF,
            0xE9B5DBA5,
            0x3956C25B,
            0x59F111F1,
            0x923F82A4,
            0xAB1C5ED5,
            0xD807AA98,
            0x12835B01,
            0x243185BE,
            0x550C7DC3,
            0x72BE5D74,
            0x80DEB1FE,
            0x9BDC06A7,
            0xC19BF174,
            0xE49B69C1,
            0xEFBE4786,
            0x0FC19DC6,
            0x240CA1CC,
            0x2DE92C6F,
            0x4A7484AA,
            0x5CB0A9DC,
            0x76F988DA,
            0x983E5152,
            0xA831C66D,
            0xB00327C8,
            0xBF597FC7,
            0xC6E00BF3,
            0xD5A79147,
            0x06CA6351,
            0x14292967,
            0x27B70A85,
            0x2E1B2138,
            0x4D2C6DFC,
            0x53380D13,
            0x650A7354,
            0x766A0ABB,
            0x81C2C92E,
            0x92722C85,
            0xA2BFE8A1,
            0xA81A664B,
            0xC24B8B70,
            0xC76C51A3,
            0xD192E819,
            0xD6990624,
            0xF40E3585,
            0x106AA070,
            0x19A4C116,
            0x1E376C08,
            0x2748774C,
            0x34B0BCB5,
            0x391C0CB3,
            0x4ED8AA4A,
            0x5B9CCA4F,
            0x682E6FF3,
            0x748F82EE,
            0x78A5636F,
            0x84C87814,
            0x8CC70208,
            0x90BEFFFA,
            0xA4506CEB,
            0xBEF9A3F7,
            0xC67178F2,
        ]

        self.H = [
            0x6A09E667,
            0xBB67AE85,
            0x3C6EF372,
            0xA54FF53A,
            0x510E527F,
            0x9B05688C,
            0x1F83D9AB,
            0x5BE0CD19,
        ]

    def rotr(self, x, n):
        return (x >> n) | (x << (32 - n))

    def ch(self, x, y, z):
        return (x & y) ^ (~x & z)

    def maj(self, x, y, z):
        return (x & y) ^ (x & z) ^ (y & z)

    def sigma0(self, x):
        return self.rotr(x, 2) ^ self.rotr(x, 13) ^ self.rotr(x, 22)

    def sigma1(self, x):
        return self.rotr(x, 6) ^ self.rotr(x, 11) ^ self.rotr(x, 25)

    def gamma0(self, x):
        return self.rotr(x, 7) ^ self.rotr(x, 18) ^ (x >> 3)

    def gamma1(self, x):
        return self.rotr(x, 17) ^ self.rotr(x, 19) ^ (x >> 10)

    def hash(self, msg):
        # padding message
        bit_len = 8 * len(msg)
        msg += b"\x80"
        while (8 * len(msg) + 64) % 512 != 0:
            msg += b"\x00"
        msg += struct.pack(">Q", bit_len)

        a, b, c, d, e, f, g, h = self.H

        for i in range(0, len(msg), 64):
            x = [0] * 64
            for j in range(16):
                x[j] = struct.unpack(">I", msg[i + j * 4 : i + j * 4 + 4])[0]
            for j in range(16, 64):
                s0 = self.gamma0(x[j - 15])
                s1 = self.gamma1(x[j - 2])
                x[j] = (x[j - 16] + s0 + x[j - 7] + s1) & 0xFFFFFFFF

            # compression
            for j in range(64):
                S1 = self.sigma1(e)
                ch_res = self.ch(e, f, g)
                temp1 = (h + S1 + ch_res + self.K[j] + x[j]) & 0xFFFFFFFF
                S0 = self.sigma0(a)
                maj_res = self.maj(a, b, c)
                temp2 = (S0 + maj_res) & 0xFFFFFFFF

                h = g
                g = f
                f = e
                e = (d + temp1) & 0xFFFFFFFF
                d = c
                c = b
                b = a
                a = (temp1 + temp2) & 0xFFFFFFFF

            # hash values update
            self.H[0] = (self.H[0] + a) & 0xFFFFFFFF
            self.H[1] = (self.H[1] + b) & 0xFFFFFFFF
            self.H[2] = (self.H[2] + c) & 0xFFFFFFFF
            self.H[3] = (self.H[3] + d) & 0xFFFFFFFF
            self.H[4] = (self.H[4] + e) & 0xFFFFFFFF
            self.H[5] = (self.H[5] + f) & 0xFFFFFFFF
            self.H[6] = (self.H[6] + g) & 0xFFFFFFFF
            self.H[7] = (self.H[7] + h) & 0xFFFFFFFF

        return "".join(f"{x:08x}" for x in self.H)


if __name__ == "__main__":
    with open("BookofMark.txt", "rb") as f:
        message = bytearray(f.read())

    sha256 = SHA256()
    hash_value = sha256.hash(message)
    print(f"Hash Value: {hash_value}")
