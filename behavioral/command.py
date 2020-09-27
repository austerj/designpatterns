from abc import ABC, abstractmethod


class Document:
    def __init__(self):
        self._lines = []
        self._command_manager = CommandManager()

    def print(self):
        print('\n'.join(self._lines))

    def add_line(self, text, position=None):
        command = AddLine(self, position, text)
        self._command_manager.execute(command)

    def remove_line(self, position=None):
        command = RemoveLine(self, position)
        self._command_manager.execute(command)

    def undo(self):
        self._command_manager.undo()

    def redo(self):
        self._command_manager.redo()


class CommandManager:
    def __init__(self):
        self.undo_history = []
        self.redo_history = []

    def execute(self, command):
        command.execute()
        if command.is_reversible:
            self.undo_history.append(command)
            self.redo_history = []

    def undo(self):
        command = self.undo_history.pop()
        command.unexecute()
        self.redo_history.append(command)

    def redo(self):
        command = self.redo_history.pop()
        command.execute()
        self.undo_history.append(command)


class DocumentCommand(ABC):
    def __init__(self, document):
        self.document = document

    @abstractmethod
    def execute():
        raise NotImplementedError

    @abstractmethod
    def unexecute():
        raise NotImplementedError

    @property
    @abstractmethod
    def is_reversible(self):
        raise NotImplementedError


class AddLine(DocumentCommand):
    def __init__(self, document, position, text):
        super().__init__(document)
        if not position:
            position = len(self.document._lines)
        elif position > len(self.document._lines) or position < 0:
            raise IndexError('position out of range')
        self.position = position
        self.text = text

    def execute(self):
        self.document._lines.insert(self.position, self.text)

    def unexecute(self):
        del self.document._lines[self.position]

    @property
    def is_reversible(self):
        return True


class RemoveLine(DocumentCommand):
    def __init__(self, document, position):
        super().__init__(document)
        if not position:
            position = len(self.document._lines)
        elif position > len(self.document._lines) or position < 0:
            raise IndexError('position out of range')
        self.position = position
        self.text = self.document._lines[position]

    def execute(self):
        del self.document._lines[self.position]

    def unexecute(self):
        self.document._lines.insert(self.position, self.text)

    @property
    def is_reversible(self):
        return True


if __name__ == '__main__':
    # create document
    doc = Document()
    doc.add_line('i scream from the top of my lungs')
    doc.add_line('what\'s up')
    doc.undo()
    doc.add_line('what\'s going on?')
    doc.undo()
    doc.redo()
    doc.add_line('and i say')
    doc.add_line('HEEEEYEEAAAAAHYEAAAAH')
    doc.print()
