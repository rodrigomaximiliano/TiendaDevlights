<template>
  <v-app>
    <!-- Barra de navegación -->
    <v-app-bar app color="primary" dark>
      <v-app-bar-title>Tienda Devlights</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-btn icon @click="goToHome">
        <v-icon>mdi-home</v-icon>
      </v-btn>
      <v-btn icon @click="goToProducts">
        <v-icon>mdi-cart</v-icon>
      </v-btn>
      <v-btn icon @click="goToLogin">
        <v-icon>mdi-login</v-icon>
      </v-btn>
    </v-app-bar>

    <!-- Contenido principal -->
    <v-container fluid class="fill-height" style="background-color: #f5f5f5;">
      <v-row align="center" justify="center">
        <v-col cols="12" sm="10" md="8" lg="6">
          <v-card class="elevation-26" outlined>

            <v-card-title class="text-h4 text-center">
              Bienvenido a Tienda Devlights
            </v-card-title>
            <v-divider></v-divider>

            <v-card-text class="text-center">
              <p class="mb-4">Descubre nuestros productos y servicios.</p>
            </v-card-text>

            <v-card-actions class="justify-center flex-column">
              <v-btn @click="goToHome" color="primary" class="mx-2 mb-2" width="100%">
                <v-icon left>mdi-home</v-icon>Inicio
              </v-btn>
              <v-btn @click="goToLogin" color="success" class="mx-2 mb-2" width="100%">
                <v-icon left>mdi-login</v-icon>Iniciar Sesión
              </v-btn>
              <v-btn @click="goToRegister" color="info" class="mx-2 mb-2" width="100%">
                <v-icon left>mdi-account-plus</v-icon>Registrar
              </v-btn>
              <v-btn @click="goToProducts" color="warning" class="mx-2" width="100%">
                <v-icon left>mdi-cart</v-icon>Ver Productos
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
  name: 'HomePage',
  setup() {
    const router = useRouter();

    const goToHome = () => {
      router.push('/');
    };

    const goToLogin = () => {
      router.push('/login');
    };

    const goToRegister = () => {
      router.push('/register');
    };

    const goToProducts = () => {
      router.push('/products');
    };

    return { goToHome, goToLogin, goToRegister, goToProducts };
  },
};
</script>

<style scoped>
.v-card {
  border-radius: 16px;
}

.v-card-title {
  font-weight: bold;
}

.v-card-text {
  margin: 20px 0;
  color: #666;
}

.v-btn {
  font-weight: bold;
  text-transform: none;
}

.v-icon {
  font-size: 20px;
}

.card-img {
  border-top-left-radius: 16px;
  border-top-right-radius: 16px;
}
</style>
