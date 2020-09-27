from abc import ABC, abstractmethod


class Email:
    def __init__(self, subject, content):
        self.subject = subject
        self.content = content


class EmailInbox:
    def __init__(self):
        self.emails = {}

    def receive(self, email):
        category = EmailFilter.apply_filter(email)
        print(f'storing email in {category} folder')
        if category not in self.emails.keys():
            self.emails[category] = []
        self.emails[category].append(email)


class Filter(ABC):
    @classmethod
    def apply_filter(cls, email):
        category = cls.categorize(email)
        if not category:
            category = cls.next_filter().apply_filter(email)
        return category

    @abstractmethod
    def categorize():
        raise NotImplementedError

    @abstractmethod
    def next_filter():
        raise NotImplementedError


class EmailFilter(Filter):
    @classmethod
    def categorize(cls, email):
        return None

    @staticmethod
    def next_filter():
        return ImportantFilter()


class ImportantFilter(Filter):
    _important_subjects = [
        'free food',
    ]

    @classmethod
    def categorize(cls, email):
        if any(sub in email.subject for sub in cls._important_subjects):
            return 'important'
        return None

    @staticmethod
    def next_filter():
        return UnwantedFilter()


class UnwantedFilter(Filter):
    _unwanted_subjects = [
        'free',
        'work',
    ]
    _unwanted_content = [
        'nigerian prince',
        'prince of nigeria',
        'boss',
    ]

    @classmethod
    def categorize(cls, email):
        if any(sub in email.subject for sub in cls._unwanted_subjects):
            return 'spam'
        if any(cont in email.content for cont in cls._unwanted_content):
            return 'spam'
        return None

    @staticmethod
    def next_filter():
        return DefaultFilter()


class DefaultFilter(Filter):
    @classmethod
    def categorize(cls, email):
        print('failed to categorize email: ', end='')
        return 'other'

    @staticmethod
    def next_filter():
        raise RuntimeError('did you call next_filter directly?')


if __name__ == '__main__':
    # create mailbox and emails
    inbox = EmailInbox()
    unwanted1 = Email(
        'opportunity for free money with no risk',
        'would you like some money? best, nigerian prince'
    )
    unwanted2 = Email(
        'important!',
        'we need to discuss your job performance. -your boss'
    )
    no_category = Email(
        'one two three',
        'just testing your mail filter'
    )
    important = Email(
        'get free food today with no work',
        'i have food as well. xo, nigerian prince'
    )
    # receive emails
    inbox.receive(unwanted1)
    inbox.receive(unwanted2)
    inbox.receive(no_category)
    inbox.receive(important)
