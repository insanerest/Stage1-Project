class Broadcast:
    def __init__(self):
        self.listeners = {}

    def listen(self, event_name, callback):
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(callback)

    def fire(self, event_name, *args, **kwargs):
        if event_name in self.listeners:
            for callback in self.listeners[event_name]:
                callback(*args, **kwargs)

# Create a global event manager instance
broadcast = Broadcast()
