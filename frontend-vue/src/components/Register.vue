<template>
  <v-container class="mt-5" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card elevation="10" class="pa-5">
          <v-card-title>
            <span class="headline">Registrar</span>
          </v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-form ref="form" v-model="valid" lazy-validation>
              <v-text-field
                v-model="username"
                label="Usuario"
                required
                :rules="[rules.required]"
                prepend-icon="mdi-account"
                color="primary"
                outlined
              ></v-text-field>
              <v-text-field
                v-model="password"
                label="Contraseña"
                type="password"
                required
                :rules="[rules.required, rules.min]"
                prepend-icon="mdi-lock"
                color="primary"
                outlined
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions class="justify-end">
            <!-- Botón para cancelar e ir al inicio -->
            <v-btn text color="secondary" @click="goToHome">
              Cancelar
            </v-btn>
            <v-btn color="primary" :disabled="!valid" @click="register">
              Registrar
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
  name: 'Register',
  setup() {
    const router = useRouter();
    const username = ref('');
    const password = ref('');
    const valid = ref(false);
    const rules = {
      required: (v) => !!v || 'Este campo es requerido',
      min: (v) => (v && v.length >= 6) || 'La contraseña debe tener al menos 6 caracteres',
    };

    const register = async () => {
      if (!valid.value) return;

      try {
        await axios.post('http://localhost:8000/auth/register', {
  username: username.value,
  password: password.value,
      });

        alert('Registro exitoso');
        username.value = '';
        password.value = '';
      } catch (error) {
        console.error(error);
        alert('Error al registrar');
      }
    };

    const goToHome = () => {
      router.push('/');
    };

    return { username, password, valid, rules, register, goToHome };
  },
};
</script>

<style scoped>
.v-card {
  border-radius: 16px;
  background-color: #f9f9f9;
}
.headline {
  font-weight: bold;
}
.v-btn {
  font-weight: bold;
}
</style>
