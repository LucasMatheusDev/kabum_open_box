class SendEmailInfo:
    def __init__(self, email_from: str, email_password: str, email_to: str, smtp_server: str, smtp_port: int):
        self.email_from = email_from
        self.email_password = email_password
        self.email_to = email_to
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
