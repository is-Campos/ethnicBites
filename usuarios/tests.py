from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.hashers import check_password

from usuarios.models import CustomUser

class Usuarios(TestCase):

    def verify_password(self,usuario,password):
        if(check_password(password, usuario.password)): return True
        else: return False

    def test_registro(self):
         
        response = self.client.post(reverse('usuarios:registro'), {
            'password1': '123',
            'password2': '123',
            'username': 'usuario_test'
        })
    
        self.assertEqual(response.status_code, 302)
    
        usuario_agregado = CustomUser.objects.filter(username='usuario_test').first()
        self.assertIsNotNone(usuario_agregado)
        self.assertEqual('usuario_test', usuario_agregado.username)
        self.assertTrue(self.verify_password(usuario_agregado,'123'))
        

    def test_login(self):
         
        self.client.post(reverse('usuarios:registro'), {
            'password1': '123',
            'password2': '123',
            'username': 'usuario_test'
        })

        response = self.client.post(reverse('usuarios:iniciarsesion'), {
            'username': 'usuario_test',
            'password': '123'
        })
    
        self.assertEqual(response.status_code, 302)
        usuario = CustomUser.objects.filter(username='usuario_test').first()
        self.assertTrue(self.verify_password(usuario,'123'))