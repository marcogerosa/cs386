class Barbecue {
    private MailServer mailServer;
    private int food = 0;

    public Barbecue (MailServer mailServer) {
        this.mailServer = mailServer;
    }

    public int getFood() {
        return food;
    }

    public void add(Person p) throws InvalidEmailException {
        if (p.getAge() > 2 && p.getAge() <= 14) {
            food += 100;
        }
        else if (p.getAge() > 14 && p.getAge() <= 25) {
            food += 400;
        }
        else if (p.getAge() > 25) {
            food += 300;
        }
        this.mailServer.sendMail(p.getEmail(), "Your participation is confirmed");
    }
}
