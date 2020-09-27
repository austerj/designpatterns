from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update():
        raise NotImplementedError


class Subject(ABC):
    def __init__(self):
        self.subscribers = set()

    def register(self, subscriber):
        self.subscribers.add(subscriber)

    def unregister(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update()


class Subscriber(Observer):
    def update(self):
        print(f'{self.__hash__()} received blog update')


class Blog(Subject):
    def post_article(self):
        print('posting article on blog!')
        self.notify()


if __name__ == '__main__':
    # create blog
    blog = Blog()
    # create subscribers
    subscriber1 = Subscriber()
    subscriber2 = Subscriber()
    subscriber3 = Subscriber()
    # subscribe to blog
    blog.register(subscriber1)
    blog.register(subscriber2)
    blog.register(subscriber3)
    # post blog post
    blog.post_article()
    # the article was unpopular - most people unsubscribed
    blog.unregister(subscriber1)
    blog.unregister(subscriber3)
    # post to remaining audience
    blog.post_article()
