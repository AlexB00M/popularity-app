<template>
    <nav class="menu">
        <button @click="changeRoute('/liderbord')" class="menu-item" :class="{ active: isActive('/liderbord') }">
            <nuxt-icon class="icon" name="liderbord"/>
            <span class="menu-text">
                Liderbord
            </span>
        </button>
        <button @click="changeRoute('/tasks')" class="menu-item" :class="{ active: isActive('/tasks') }">
            <nuxt-icon class="icon" name="tasks"/>
            <span class="menu-text">
                Tasks
            </span>
        </button>
        <button @click="changeRoute('/')" class="menu-item" :class="{ active: isActive('/') }">
            <nuxt-icon class="icon" name="store"/>
            <span class="menu-text">
                Store
            </span>
        </button>
        <button @click="changeRoute('/friends')" class="menu-item" :class="{ active: isActive('/friends') }">
            <nuxt-icon class="icon" name="friends"/>
            <span class="menu-text">
                Friends
            </span>
        </button>
        <button @click="changeRoute('/profile')" class="menu-item" :class="{ active: isActive('/profile') }">
            <nuxt-icon class="icon" name="profile"/>
            <span class="menu-text">
                Profile
            </span>
        </button>
    </nav>
</template>

<script setup>
import { useRoute } from 'vue-router';

const route = useRoute()
const router = useRouter()
const isSpining = useState('isSpining')

const changeRoute = (routeName) => {
    if (!isSpining.value) {
        router.push(routeName)
    }
}

const isActive = (path) => route.path === path;
</script>

<style>
.menu{
    bottom: 0;
    left: 0;
    height: var(--bottom-menu-height);
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    backdrop-filter: blur(10px);
    position: fixed;
    background-color: var(--tg-theme-section-bg-color);
    z-index: 200;
    border-top: 0.7px solid var(--tg-theme-section-separator-color);
}

.menu-item{
    width: 100px;
    height: 50px;
    display: flex;
    flex-direction: column;
    text-decoration: none;
    align-items: center;
    justify-content: space-around;
    color: var(--tg-theme-subtitle-text-color);
    outline: none;
    margin-bottom: 15px;
    cursor: pointer;
}

.menu-item.active{
    color: #003cff;
}

.menu-text{
    font-size: 12px;
    font-weight: 600;
}

.icon{
    font-size: 20px;
    /* margin-bottom: 4px; */
}
</style>