<template>
  <v-container fluid class="d-flex align-center justify-center" style="height: 100vh;">
    <v-card>
      <v-card-title class="headline text-center">Iniciar Sesión</v-card-title>
      <v-card-text>
        <v-form ref="form" v-model="valid" lazy-validation>
          <v-text-field
            v-model="username"
            label="Usuario"
            :rules="[v => !!v || 'Usuario es requerido']"
            required
          ></v-text-field>

          <v-text-field
            v-model="password"
            label="Contraseña"
            type="password"
            :rules="[v => !!v || 'Contraseña es requerida']"
            required
          ></v-text-field>

          <v-btn :disabled="!valid" @click="login" color="primary" class="mt-4" block>
            Iniciar Sesión
          </v-btn>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text @click="goToRegister">¿No tienes una cuenta? Regístrate</v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router'; // Importa useRouter

export default {
  name: 'Login',
  setup() {
    const username = ref('');
    const password = ref('');
    const valid = ref(false);
    const router = useRouter(); // Inicializa el enrutador

    const login = async () => {
      try {
        await axios.post('http://localhost:8000/login', {
          username: username.value,
          password: password.value
        });
        alert('Inicio de sesión exitoso');
        // Redirigir al usuario después de un inicio de sesión exitoso
        router.push('/dashboard'); // Cambia '/dashboard' por la ruta a la que quieras redirigir
      } catch (error) {
        console.error(error);
        alert('Error al iniciar sesión');
      }
    };

    const goToRegister = () => {
      router.push('/register'); // Cambia '/register' por la ruta de tu página de registro
    };

    return { username, password, valid, login, goToRegister };
  }
}
</script>

<style scoped>
.v-card {
  max-width: 400px;
  margin: auto;
}
</style>
