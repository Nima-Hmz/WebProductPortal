const themeToggleMobile = document.getElementById('themeToggleMobile');
const lightIconMobile = document.getElementById('lightIconMobile');
const darkIconMobile = document.getElementById('darkIconMobile');


// Check the current theme from localStorage
const currentTheme = localStorage.getItem('theme') || 'dark';
if (currentTheme === 'dark') {
    document.documentElement.classList.add('dark');
    lightIconDesktop.classList.remove('hidden');
    darkIconDesktop.classList.add('hidden');
    lightIconMobile.classList.remove('hidden');
    darkIconMobile.classList.add('hidden');
} else {
    document.documentElement.classList.remove('dark');
    lightIconDesktop.classList.add('hidden');
    darkIconDesktop.classList.remove('hidden');
    lightIconMobile.classList.add('hidden');
    darkIconMobile.classList.remove('hidden');
}

// Toggle theme button functionality for Mobile
themeToggleMobile.addEventListener('click', () => {
    document.documentElement.classList.toggle('dark');
    if (document.documentElement.classList.contains('dark')) {
        localStorage.setItem('theme', 'dark');
        lightIconDesktop.classList.remove('hidden');
        darkIconDesktop.classList.add('hidden');
        lightIconMobile.classList.remove('hidden');
        darkIconMobile.classList.add('hidden');
    } else {
        localStorage.setItem('theme', 'light');
        lightIconDesktop.classList.add('hidden');
        darkIconDesktop.classList.remove('hidden');
        lightIconMobile.classList.add('hidden');
        darkIconMobile.classList.remove('hidden');
    }
});

// Toggle theme button functionality for Desktop
themeToggleDesktop.addEventListener('click', () => {
    document.documentElement.classList.toggle('dark');
    if (document.documentElement.classList.contains('dark')) {
        localStorage.setItem('theme', 'dark');
        lightIconDesktop.classList.remove('hidden');
        darkIconDesktop.classList.add('hidden');
        lightIconMobile.classList.remove('hidden');
        darkIconMobile.classList.add('hidden');
    } else {
        localStorage.setItem('theme', 'light');
        lightIconDesktop.classList.add('hidden');
        darkIconDesktop.classList.remove('hidden');
        lightIconMobile.classList.add('hidden');
        darkIconMobile.classList.remove('hidden');
    }
});