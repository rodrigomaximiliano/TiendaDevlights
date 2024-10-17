<template>
  <v-app>
    <!-- Barra de navegación -->
    <v-app-bar app color="purple darken-2" dark>
      <v-toolbar-title class="d-flex align-center">
        <v-img src="@/assets/logo.png" height="40" contain></v-img>
        <span class="ml-2 font-weight-bold white--text">Tienda Devlights</span>
      </v-toolbar-title>

      <v-spacer></v-spacer>

      <!-- Botones de navegación -->
      <v-btn text @click="goToHome" aria-label="Ir a Inicio">
        <v-icon left>mdi-home</v-icon> Inicio
      </v-btn>
      <v-btn text @click="goToProducts" aria-label="Ver Productos">
        <v-icon left>mdi-cart</v-icon> Productos
      </v-btn>
      <v-btn text @click="goToLogin" aria-label="Iniciar Sesión">
        <v-icon left>mdi-login</v-icon> Iniciar Sesión
      </v-btn>
      <v-btn text @click="goToRegister" aria-label="Registrarse">
        <v-icon left>mdi-account-plus</v-icon> Registrarse
      </v-btn>
    </v-app-bar>

    <!-- Contenedor principal -->
   

    <!-- Footer Moderno -->
    <v-footer color="purple darken-2" app>
      <v-container>
        <v-row>
          <v-col class="text-center">
            <p class="footer-text">&copy; 2024 Tienda Devlights. Todos los derechos reservados.</p>
          </v-col>
        </v-row>
      </v-container>
    </v-footer>
  </v-app>
</template>

<script>
import { useRouter } from 'vue-router';

export default {
  name: 'HomePage',
  setup() {
    const router = useRouter();

    const goToHome = () => router.push('/');
    const goToLogin = () => router.push('/login');
    const goToRegister = () => router.push('/register');
    const goToProducts = () => router.push('/products');

    return { goToHome, goToLogin, goToRegister, goToProducts };
  },
};
</script>

<style scoped>
.v-toolbar-title {
  display: flex;
  align-items: center; /* Asegura que el logo y el texto estén centrados verticalmente */
}

.footer-text {
  margin: 16px 0; /* Espaciado vertical */
  font-weight: bold; /* Negrita para mayor énfasis */
  color: white; /* Asegura que el texto del footer sea legible */
}

/* Ajusta el margen izquierdo si es necesario */
.ml-2 {
  margin-left: 12px; /* Espaciado ajustado */
}
</style>
