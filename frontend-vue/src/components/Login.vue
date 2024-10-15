<template>
  <div>
    <h1>Iniciar Sesión</h1>
    <form @submit.prevent="login">
      <input type="text" v-model="username" placeholder="Usuario" required />
      <input type="password" v-model="password" placeholder="Contraseña" required />
      <button type="submit">Iniciar Sesión</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'

export default {
  name: 'Login',
  setup() {
    const username = ref('')
    const password = ref('')

    const login = async () => {
      // Implementa la lógica de inicio de sesión
      try {
        await axios.post('http://localhost:8000/login', {
          username: username.value,
          password: password.value
        })
        alert('Inicio de sesión exitoso')
      } catch (error) {
        console.error(error)
        alert('Error al iniciar sesión')
      }
    }

    return { username, password, login }
  }
}
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  max-width: 300px;
  margin: auto;
}

input {
  margin: 5px 0;
  padding: 10px;
}

button {
  padding: 10px;
  background-color: blue;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: darkblue;
}
</style>
