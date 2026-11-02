class EventQueue:

  def __init__(self):
    self.queue = []

  def add_event(self, event):
    self.queue.append(event)
    print(f"Added Event: {event}")

  def process_event(self):
    if not self.queue:
      print("No pending events to process.")
      return
    processed = self.queue.pop(0)
    print(f"Processed Event: {processed}")

  def display_events(self):
    print("Pending Events:", self.queue)

  def cancel_event(self, event):
    if event in self.queue:
      self.queue.remove(event)
      print(f"Canceled Event: {event}")
    else:
      print("Event not found in queue.")


# Driver Code
eq = EventQueue()
eq.add_event("Login")
eq.add_event("Click Button")
eq.display_events()
eq.process_event()
eq.cancel_event("Click Button")
eq.display_events()