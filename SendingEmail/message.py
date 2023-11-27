import smtplib
import os
from email.message import EmailMessage


class Message:
    def send(self, msg, to, email, passwordapp,
             attachment=False, directory="", typeattachment="pdf",
             nameattachment="attachment"):
        """
                Envie um email com ou sem anexo.

                Parâmetros:
                - msg: str, Corpo da mensagem de email.
                - to: str, Endereço de email do destinatário.
                - email: str, Seu endereço de email.
                - passwordapp: str, Senha do aplicativo para autenticação SMTP.
                - attachment: bool, Indica se há um anexo a ser enviado.
                - directory: str, Caminho do arquivo de anexo (se attachment for True).
                - typeattachment: str, Tipo de arquivo do anexo (padrão: "pdf").
                - nameattachment: str, Nome do arquivo de anexo (padrão: "attachment").
                """
        # Criando mensagem
        email_msg = EmailMessage()

        email_msg['Subject'] = 'Certificado de Conclusão do Programa DAB'
        email_msg['From'] = email
        email_msg['To'] = to
        email_msg.set_content(msg)

        if attachment:
            with open(directory, "rb") as contentFile:
                content = contentFile.read()

                email_msg.add_attachment(content,
                                         maintype="aplication",
                                         subtype=typeattachment,
                                         filename=f"{nameattachment}.{typeattachment}")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email, passwordapp)
            smtp.send_message(email_msg)
