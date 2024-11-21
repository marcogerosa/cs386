class Barbecue:
    def __init__(self, mail_server):
        self._mail_server = mail_server
        self._food = 0

    def get_food(self):
        return self._food

    def add(self, person):
        if 2 < person.get_age() <= 14:
            self._food += 100
        elif 14 < person.get_age() <= 25:
            self._food += 400
        elif person.get_age() > 25:
            self._food += 300
        
        self._mail_server.send_mail(person.get_email(), "Your participation is confirmed")
