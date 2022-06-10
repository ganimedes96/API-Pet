from django.core.mail import send_mail

def send_email_confirmation(adoption):
    subject = "Adocao realizada com sucesso!"
    content = f"Parabens por realizar a adocao do  pet {adoption.pet.name} com o valor de {adoption.valor}" 
    sender = "ganimedes409@gmail.com"
    recipient = [adoption.email]
    send_mail(subject, content, sender, recipient)