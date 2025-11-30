const API_URL = 'http://158.160.172.217:8000/api/chat/message';

function sendMessage() {
    const input = document.getElementById('messageInput');
    const message = input.value.trim();
    
    if (!message) return;
    
    // Добавляем сообщение пользователя сразу
    addMessage(message, 'user');
    input.value = "";
    
    // Показываем индикатор загрузки
    const loadingDiv = document.createElement('div');
    loadingDiv.id = 'loading';
    loadingDiv.className = 'message bot';
    loadingDiv.textContent = 'AI thinking...';
    document.getElementById('chat').appendChild(loadingDiv);
    
    fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            message: message,
            user_id: 'test_user'
        })
    })
    .then(response => {
        if (!response.ok) throw new Error('Network Error');
        return response.json();
    })
    .then(data => {
        const loadingElement = document.getElementById('loading');
        if (loadingElement) {
            loadingElement.remove();
        }
        
        if (data.response) {
            addMessage(data.response, 'bot');
        } else {
            addMessage('answer is empty', 'bot');
        }
    })
    .catch(error => {
        const loadingElement = document.getElementById('loading');
        if (loadingElement) {
            loadingElement.remove();
        }
        addMessage('Error: ' + error.message, 'bot');
    });
}

function addMessage(text, sender) {
    const chat = document.getElementById('chat');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    messageDiv.textContent = text;
    chat.appendChild(messageDiv);
    chat.scrollTop = chat.scrollHeight;
}

document.getElementById('messageInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});
