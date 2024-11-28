const notification = document.getElementById('notification');

function showNotification(message, type = 'info') {
    notification.textContent = message;
    notification.className = type;
    setTimeout(() => (notification.textContent = ''), 5000);
}

document.getElementById('sshForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const response = await fetch('/login', { method: 'POST', body: formData });
    const result = await response.json();
    showNotification(result.message || result.error, response.ok ? 'success' : 'error');
});

document.getElementById('ifconfigForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const response = await fetch('/fetch_ifconfig', { method: 'POST', body: formData });
    const result = await response.json();
    showNotification(result.message || result.error, response.ok ? 'success' : 'error');
});

document.getElementById('nmapForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const response = await fetch('/run_nmap', { method: 'POST', body: formData });
    const result = await response.json();
    showNotification(result.message || result.error, response.ok ? 'success' : 'error');
});
