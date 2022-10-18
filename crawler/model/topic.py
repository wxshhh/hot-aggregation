class Topic:
    def __init__(self, id, title, link):
        self.id = id
        self.title = title
        self.link = link
        # self.create_time = create_time
        # self.update_time = update_time

    def print(self):
        print(self.id, self.title, self.link)

    def to_list(self):
        return [self.id, self.title, self.link]


class Zhihu(Topic):
    def __init__(self, id, title, describe, image_url, link, heat):
        super().__init__(id, title, link)
        self.image_url = image_url
        self.describe = describe
        self.heat = heat

    def to_list(self):
        return [self.id, self.title, self.describe, self.image_url, self.link, self.heat]


class Weibo(Topic):
    pass


class Tieba(Topic):
    def __init__(self, id, title, link, image_url, describe, heat):
        super().__init__(id, title, link)
        self.image_url = image_url
        self.describe = describe
        self.heat = heat

    def to_list(self):
        return [self.id, self.title, self.describe, self.image_url, self.link, self.heat]


class Bilibili(Topic):
    def __init__(self, id, title, describe, image_url, link, author, view, like, reply, favorite, coin, share):
        super().__init__(id, title, link)
        self.image_url = image_url
        self.describe = describe
        self.author = author
        self.view = view
        self.like = like
        self.reply = reply
        self.favorite = favorite
        self.coin = coin
        self.share = share

    def to_list(self):
        return [self.id, self.title, self.link, self.image_url, self.describe, self.author, self.view, self.like,
                self.reply,
                self.favorite, self.coin, self.share]
