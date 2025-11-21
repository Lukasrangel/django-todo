from django.core.mail import send_mail

def  chamar_atencao():
    send_mail(
        subject="Teste do homelab",
        message="Funcionou!",
        from_email=None,
        recipient_list=["luks_dev@outlook.com"],
    )