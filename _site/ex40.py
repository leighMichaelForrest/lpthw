class Song(object):

    def __init__(self, title, lyrics):
        self.title = title
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def print_title(self):
        return self.title

happy_bday = Song("Happy Birthday", ["Happy Birthday to You",
                        "I hope you don't get sued",
                        "so I'll stop right there"])

bulls_on_parade = Song("Bulls on Parade",
                       ["They rally around tha family",
                        "With pockets full of shells"])

thomas_edison = Song("Mary Had a Little Lamb",
                     ["Mary had a little lamb",
                      "whose fleece was as white as snow",
                      "everywhere Mary went",
                      "the lamb was sure to go"])

halsey = ["Got a girl with California eyes",
          "And I thought that she could really be the one this time",
          "But I never got the chance to make her mine",
          "Because she fell in love with little thin white lines",
          "London girl with an attitude",
          "We never told no one but we look so cute",
          "Both got way better things to do",
          "But I always think about it when I'm riding through",
          "\n",
          "\n",
          "I believe, I believe, I believe, I believe",
          "That I'm in too deep",
          "And jealousy, jealousy, jealousy, jealousy",
          "Get the best in me",
          "Look, I don't mean to frustrate",
          "But I always make the same mistakes, yeah",
          "Always make the same mistakes \'cause...",
          "\n\n",
          "I'm bad at love, ooh-ooh",
          "But you can't blame me for tryin\'",
          "You know I\'d be lyin' sayin\'",
          "You were the one, ooh-ooh",
          "That could finally fix me",
          "Lookin' at my history",
          "I'm bad at love, ooh-ooh",
          "Oh, you know, you know, you know, you know",
          "I'm bad at love, ooh-ooh",
          "I\'m bad at love, ooh-ooh"]


# construct an object with Halsey's lyrics
bad_at_love = Song("Bad at Love", halsey)

print(happy_bday.print_title())
happy_bday.sing_me_a_song()

print(bulls_on_parade.print_title())
bulls_on_parade.sing_me_a_song()

print(thomas_edison.print_title())
thomas_edison.sing_me_a_song()

print("And now for our feature presentation.....\n\n\n")
print(bad_at_love.print_title(), "\n\n")
bad_at_love.sing_me_a_song()
