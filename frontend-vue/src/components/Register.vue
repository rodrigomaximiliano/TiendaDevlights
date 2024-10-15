<template>
  <div>
    <h1>Registrar</h1>
    <form @submit.prevent="register">
      <input type="text" v-model="username" placeholder="Usuario" required />
      <input type="password" v-model="password" placeholder="Contraseña" required />
      <button type="submit">Registrar</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'

export default {
  name: 'Register',
  setup() {
    const username = ref('')
    const password = ref('')

    const register = async () => {
      try {
        await axios.post('http://localhost:8000/register', {
          username: username.value,
          password: password.value
        })
        alert('Registro exitoso')
      } catch (error) {
        console.error(error)
        alert('Error al registrar')
      }
    }

    return { username, password, register }
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
