<template>
  <div>
    <h1>Página de Inicio</h1>
    <router-link to="/login">Iniciar Sesión</router-link>
    <router-link to="/register">Registrar</router-link>
    <router-link to="/products">Ver Productos</router-link>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
}
</script>

<style scoped>
/* Estilos aquí */
</style>
