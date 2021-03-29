import mido


class Listener():

    def __init__(self):
        self.running_note_limit = 30
        self.patterns = []
        self.running_notes = []
        self.print_notes = False

    def append_to_running_notes(self, note):
        """Appends the latest note played to running notes"""
        if len(self.running_notes) > self.running_note_limit - 1:
            # pop oldest note off the list
            self.running_notes.pop(0)
        self.running_notes.append(note)

    def check_patterns(self):
        """Checks latest running notes against all patterns in reverse"""
        for pattern in self.patterns:
            iterator = -1
            while True:
                if len(pattern['pattern']) == abs(iterator):
                    pattern['callback']()
                    return
                if self.running_notes[iterator] == pattern['pattern'][iterator]:
                    iterator = iterator - 1
                    continue
                else:
                    break

    def message_is_valid(self, message):
        """Determines if the incoming message is a key press"""
        return message.type == 'note_on'

    def add_pattern(self, pattern, callback):
        if len(pattern) > self.running_note_limit - 1:
            raise Exception('Maximum pattern length is {}'.format(self.running_note_limit))
        self.patterns.append({
            'pattern': pattern,
            'callback': callback,
        })

    def listen(self):
        """Listens for incoming events from MIDI device"""
        print('Starting listening...')
        try:
            keyboard_name = mido.get_input_names()[1]
        except IndexError:
            keyboard_name = None
        with mido.open_input(keyboard_name) as inport:
            for message in inport:
                if self.message_is_valid(message):
                    note = int(message.note)
                    if self.print_notes:
                        print(note)
                    self.append_to_running_notes(note)
                    self.check_patterns()
