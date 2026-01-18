class Codec:

    def __init__(self):
        self.map = {} #'0':https://leetcode.com/problems/design-tinyurl
        self.counter = 0 


    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.map[self.counter] = longUrl
        self.counter +=1
        return "http://tinyurl.com/" + str(self.counter-1)
        
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        array = shortUrl.split("/")
        return self.map[int(array[-1])]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))