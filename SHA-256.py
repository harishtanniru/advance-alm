import struct


class SHA256:
    def __init__(self) -> None:
        self.K = [
            0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
            0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
            0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
            0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
            0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
            0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
            0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
            0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
            0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
            0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
            0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
            0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
            0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
            0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
            0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
        ]

        self.H = [
            0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
            0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
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
    message = b"Hello"
    sha256 = SHA256()
    hash_value = sha256.hash(message)
    print(f"Hash Value for {message}: {hash_value}")

# 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969