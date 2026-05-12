class Solution(object):

    def __init__(self):
        self.buffer = [""] * 4
        self.buf_ptr = 0
        self.buf_count = 0

    def read(self, buf, n):

        total = 0

        while total < n:

            # refill buffer if empty
            if self.buf_ptr == self.buf_count:
                self.buf_count = read4(self.buffer)
                self.buf_ptr = 0

                # no more data
                if self.buf_count == 0:
                    break

            # consume buffer
            while total < n and self.buf_ptr < self.buf_count:
                buf[total] = self.buffer[self.buf_ptr]
                total += 1
                self.buf_ptr += 1

        return total
