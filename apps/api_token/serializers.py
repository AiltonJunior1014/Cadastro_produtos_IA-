from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class Autenticacao(TokenObtainPairSerializer):
    def valida_dados(self, attrs):
        data = super.valida_dados(attrs)
        data['email'].self.user.username
        data['senha'].self.user.password

        return data