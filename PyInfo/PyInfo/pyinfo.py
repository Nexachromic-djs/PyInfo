class PyInfo:
    def set_data(self, s, a, t):
        self.subject = s
        self.author = a
        self.time = t

    def info(self):
        print(self.subject, self.author, self.time)

intro = PyInfo()
intro.set_data("Hello There! I'm Nexachromic and I welcome you to PyInfo! This module is made for developers as an aid for errors and methods to code.", " Nexachromic (Developer of PyInfo)", " May 28th 2022")

python = PyInfo()
python.set_data("Python is a high-level, interpreted, general-purpose programming language. It was invented by Guido Van Rossum in the 1990s. It was an instant hit because of it being a very easy language to read. ", "- Nexachromic (Developer of PyInfo) ", "- May 28th 2022")

